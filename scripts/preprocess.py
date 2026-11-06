"""Reproducible, offline preprocessing of the pinned EthnoTrace source snapshot."""

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE_VERSION = '1.0'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def read_rows(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')


def jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in rows), encoding='utf-8')


def text(value):
    """NFC and whitespace only: preserve accents, case, Indigenous names and meaning."""
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', value)).strip()


def normalize(value):
    if isinstance(value, str):
        return text(value)
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    return value


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def identity(row, index):
    for key in ('record_id', 'pair_id', 'review_id', 'resource_screening_id', 'lead_id', 'taxon_record_id', 'paper_id'):
        if row.get(key):
            return str(row[key])
    return f'row-{index + 1:04d}'


def paper_key(row):
    if row.get('paper_id'):
        return row['paper_id']
    sid = row.get('source_id', '')
    return 'P' + sid[5:] if sid.startswith('PMID:') else None


def features(row, config):
    part = row.get('plant_part')
    result = row.get('result_direction')
    prep = row.get('preparation') or ''
    solvents = []
    if re.search(r'\bethanol\b|\bethanolic\b', prep, re.I):
        solvents.append('ethanol')
    if re.search(r'\bwater\b', prep, re.I):
        solvents.append('water')
    pct = re.search(r'\b(\d+(?:\.\d+)?)%\s+(?:aqueous\s+)?(?:ethanol|ethanolic)', prep, re.I)
    exposure = config['experimental_exposures'].get(row.get('record_id'), {})
    f = {
        'scientific_names': row.get('species'),
        'study_settings': (
            row['study_setting']
            if isinstance(row.get('study_setting'), list)
            else [row['study_setting']] if row.get('study_setting') else None
        ),
        'endpoint': config['endpoint_aliases'].get((row.get('endpoint') or '').casefold()),
        'administration_route': exposure.get('route') or row.get('administration_route'),
        'plant_parts': config['part_aliases'].get((part or '').casefold()),
        'part_mapping_status': (
            'missing' if not part else 'mapped' if part.casefold() in config['part_aliases'] else 'unmapped_preserved'
        ),
        'extraction_solvents_explicit': solvents or None,
        'ethanol_percent_explicit': float(pct.group(1)) if pct else None,
        'exposure': exposure or None,
        'exposure_basis': (
            'versioned curated rules from existing experimental record and its locator' if exposure else None
        ),
        'experimental_result_direction': config['result_direction_aliases'].get(result),
        'study_screening_category': (row.get('classification') or {}).get('label'),
        'claim_comparability': {
            k: row[k]
            for k in (
                'taxon_alignment',
                'part_alignment',
                'preparation_alignment',
                'outcome_alignment',
                'claim_evidence_label',
            )
            if k in row
        }
        or None,
        'training_eligible': False,
        'eligibility_reason': 'No independently reviewed training pairs are present in the source snapshot.',
    }
    if exposure.get('exposure_inherited_from'):
        f['preparation_context_inherited_from'] = exposure['exposure_inherited_from']
    # Canonical units for computational comparison; original units remain in raw and exposure.
    if exposure.get('duration_value') is not None:
        scale = {'hour': 1, 'day': 24, 'week': 168}[exposure['duration_unit']]
        f['exposure_duration_hours'] = exposure['duration_value'] * scale
    return f


class Groups:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def join(self, a, b):
        x, y = self.find(a), self.find(b)
        if x != y:
            self.parent[max(x, y)] = min(x, y)


def run(root=ROOT, output=None):
    source = root / 'imports/dataset'
    target = output or root / 'data/processed'
    config = read_json(root / 'config/normalization.json')
    manifest = read_json(root / 'imports/dataset_manifest.json')
    for entry in manifest['files']:
        path = source / entry['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError(f"Pinned source changed: {entry['path']}")
    tables = {p.stem: read_rows(p) for p in sorted((source / 'data').glob('*.jsonl'))}
    documents = {p.stem: read_json(p) for p in sorted((source / 'data').glob('*.json'))}
    # Check references before generating any files.
    traditional = {r['record_id']: r for r in tables['traditional_records']}
    experiments = {r['record_id']: r for r in tables['experimental_records']}
    papers = {r['paper_id']: r for r in tables['papers']}
    sources = {r['source_key']: r for r in documents['sources']['sources']}
    for row in list(traditional.values()) + list(experiments.values()):
        if row['source_key'] not in sources:
            raise ValueError('Unknown imported source')
    for row in tables['extracted_claim_study_pairs']:
        if row['traditional_record_id'] not in traditional or row['experimental_record_id'] not in experiments:
            raise ValueError('Broken extracted pair')
        if row['paper_id'] not in papers:
            raise ValueError('Unknown pair publication')
    groups = Groups()
    reasons = []

    def link(a, b, reason):
        groups.join(a, b)
        reasons.append({'left': a, 'right': b, 'reason': reason})

    for name, records in tables.items():
        if name not in ('traditional_records', 'experimental_records', 'papers'):
            continue
        for row in records:
            rid = row.get('record_id') or row['paper_id']
            groups.find(rid)
            pk = paper_key(row)
            if pk:
                link(rid, pk, 'same_publication')
            if row.get('source_key') and name != 'papers':
                link(rid, 'source:' + row['source_key'], 'same_source_account')
            community = json.dumps(row.get('community_or_nation', ''), ensure_ascii=False)
            if 'Cree' in community or 'Eeyou Istchee' in community:
                link(rid, 'programme:CEI', 'conservative_programme_block_not_proven_same_cohort')
    for pair in tables['extracted_claim_study_pairs']:
        link(pair['traditional_record_id'], pair['experimental_record_id'], 'linked_claim_and_experiment')
    members = defaultdict(list)
    for rid in sorted(groups.parent):
        members[groups.find(rid)].append(rid)
    group_ids = {node: 'G' + digest(m)[:12] for m in members.values() for node in m}
    evaluation_groups = [
        {
            'evaluation_group_id': 'G' + digest(m)[:12],
            'members': m,
            'split': None,
            'status': 'unassigned_pending_review',
            'caveat': 'Conservative source/programme grouping, not established cohort identity.',
        }
        for m in members.values()
    ]
    reference_rows = []
    for row in sources.values():
        reference_rows.append(
            {
                'reference_id': 'source:' + row['source_key'],
                'kind': 'imported_source',
                'citation': row['attribution'],
                'url': row['source_url'],
                'licence': row['licence'],
                'rights_uri': row.get('licence_url'),
                'original_metadata': row,
            }
        )
    for row in tables['papers'] + tables['catalogue_literature_leads']:
        refid = 'PMID:' + row['pmid']
        reference_rows.append(
            {
                'reference_id': refid,
                'kind': 'publication' if row.get('paper_id') else 'literature_lead',
                'citation': row['citation'],
                'url': row['source_url'],
                'doi': row.get('doi'),
                'licence': row.get('licence'),
                'rights_uri': None,
            }
        )
        if row.get('correction'):
            c = row['correction']
            reference_rows.append(
                {'reference_id': 'PMID:' + c['pmid'], 'kind': 'correction', 'citation': c['citation'], 'url': c['url']}
            )
    for row in tables['taxon_crosswalk']:
        reference_rows.append(
            {
                'reference_id': row['taxon_record_id'],
                'kind': 'taxonomic_lookup',
                'citation': row['citation'],
                'url': row['source_url'],
                'licence': row['licence_note'],
            }
        )
    cat = documents['catalogue_screening_summary']
    reference_rows.append(
        {
            'reference_id': 'organiser_catalogue',
            'kind': 'resource_catalogue',
            'citation': 'EthnoHack organisers. Datasets for all tracks. Retrieved ' + cat['retrieved_on'] + '.',
            'url': cat['catalogue_url'],
            'licence': 'No open reuse licence verified; full document not redistributed.',
        }
    )
    references = {r['reference_id'] for r in reference_rows}
    if len(references) != len(reference_rows):
        raise ValueError('Duplicate reference identifier')
    output_counts, issues, duplicates = {}, [], []
    for name, records in tables.items():
        out, seen_ids, fingerprints = [], set(), defaultdict(list)
        for i, raw in enumerate(records):
            rid = identity(raw, i)
            if rid in seen_ids:
                raise ValueError(f'Duplicate identifier in {name}: {rid}')
            seen_ids.add(rid)
            norm = normalize(raw)
            if norm.get('doi'):
                norm['doi'] = norm['doi'].lower().removeprefix('https://doi.org/')
            correction = config.get("audit_corrections", {}).get(name, {}).get(rid)
            if correction:
                norm.update(correction["fields"])
            f = features(norm, config)
            citation_refs = []
            if name in ('traditional_records', 'experimental_records'):
                citation_refs.append('source:' + raw['source_key'])
            if raw.get('pmid'):
                citation_refs.append('PMID:' + str(raw['pmid']))
            if raw.get('paper_id') and raw['paper_id'] in papers:
                citation_refs.append('PMID:' + papers[raw['paper_id']]['pmid'])
            for ref in citation_refs:
                if ref not in references:
                    raise ValueError('Unresolved citation: ' + ref)
            if name in ('traditional_records', 'experimental_records'):
                for field in ('species', 'plant_part', 'preparation', 'administration_route'):
                    # Experiments use curated route rules, not a missing traditional route field.
                    if field == 'administration_route' and name == 'experimental_records':
                        continue
                    if raw.get(field) is None:
                        issues.append({'table': name, 'record_id': rid, 'field': field, 'issue': 'not_established'})
                if f['part_mapping_status'] == 'unmapped_preserved':
                    issues.append(
                        {'table': name, 'record_id': rid, 'field': 'plant_part', 'issue': 'unmapped_preserved'}
                    )
                key = {
                    k: norm.get(k)
                    for k in (
                        'source_key',
                        'species',
                        'plant_part',
                        'preparation',
                        'reported_use_or_outcome',
                        'study_setting',
                    )
                }
                fingerprints[digest(key)].append(rid)
            group = group_ids.get(rid) or group_ids.get(raw.get('paper_id'))
            out.append(
                {
                    'id': rid,
                    'raw': raw,
                    'normalized': norm,
                    'features': f,
                    'provenance': {
                        'input_path': 'imports/dataset/data/' + name + '.jsonl',
                        'source_commit': manifest['source_commit'],
                        **({'audit_correction': correction} if correction else {}),
                        'row_sha256': digest(raw),
                        'pipeline_version': PIPELINE_VERSION,
                        'citation_refs': sorted(set(citation_refs)),
                    },
                    'evaluation_group_id': group,
                }
            )
        for fingerprint, ids in fingerprints.items():
            if len(ids) > 1:
                duplicates.append(
                    {'table': name, 'record_ids': ids, 'fingerprint': fingerprint, 'action': 'flagged_not_deleted'}
                )
        jsonl(target / (name + '.jsonl'), out)
        output_counts[name] = len(out)
    for name, raw in documents.items():
        dump(
            target / (name + '.json'),
            {
                'raw': raw,
                'normalized': normalize(raw),
                'provenance': {
                    'input_path': 'imports/dataset/data/' + name + '.json',
                    'source_commit': manifest['source_commit'],
                },
            },
        )
    jsonl(target / 'references.jsonl', reference_rows)
    jsonl(target / 'evaluation_groups.jsonl', sorted(evaluation_groups, key=lambda x: x['evaluation_group_id']))
    jsonl(target / 'grouping_edges.jsonl', reasons)
    missing = Counter(f"{r['table']}.{r['field']}: {r['issue']}" for r in issues)
    report = {
        'pipeline_version': PIPELINE_VERSION,
        'source_commit': manifest['source_commit'],
        'counts': output_counts,
        'json_documents_processed': len(documents),
        'reference_entries': len(reference_rows),
        'missing_or_unmapped_counts': dict(sorted(missing.items())),
        'issues': issues,
        'exact_duplicate_candidates': duplicates,
        'evaluation_groups': len(evaluation_groups),
        'training_eligible_records': 0,
        'limits': [
            'No human review is manufactured.',
            'No missing species or preparation is imputed.',
            'No automatic train/test split; cross-publication cohort identity remains unresolved.',
            'Curator summaries, labels and rationales remain separate from source passages; no model input export is created.',
            'Archive v0.2 is preserved as provenance and excluded from active preprocessing.',
        ],
    }
    dump(target / 'quality_report.json', report)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, help='Optional alternate output directory for reproducibility checks')
    args = parser.parse_args()
    report = run(output=args.output)
    print(
        json.dumps(
            {k: report[k] for k in ('counts', 'reference_entries', 'evaluation_groups', 'training_eligible_records')},
            indent=2,
        )
    )
