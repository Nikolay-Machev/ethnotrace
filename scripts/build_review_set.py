"""Build source-linked review packets and separate development expectations. No reviews are fabricated."""

import json
from pathlib import Path
from current_retrieve import ROOT, Baseline, rows


def save(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        ''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in records),
        encoding='utf-8',
        newline='\n',
    )


def packet(raw):
    fields = (
        'record_id',
        'species',
        'original_plant_name',
        'plant_part',
        'preparation',
        'original_use_description',
        'reported_use_or_outcome',
        'study_setting',
        'model',
        'endpoint',
        'comparator',
        'community_or_nation',
        'source_url',
        'source_id',
        'supporting_passage',
        'passage_locator',
        'licence',
        'citation',
    )
    return {k: raw.get(k) for k in fields}


def build():
    b = Baseline()
    actual = rows(ROOT / 'data/processed/extracted_claim_study_pairs.jsonl')
    pairs = [
        (r['raw']['traditional_record_id'], r['raw']['experimental_record_id'], 'existing_extracted_link')
        for r in actual
    ]
    pairs += [
        (a, e, 'constructed_species_mismatch_comparison')
        for a, e in [
            ('T011', 'E010'),
            ('T008', 'E001'),
            ('T007', 'E008'),
            ('T011', 'E003'),
            ('T008', 'E008'),
            ('T013', 'E008'),
            ('T014', 'E011'),
            ('T007', 'E005'),
        ]
    ]
    cases, expectations, pending = [], [], []
    for n, (tid, eid, origin) in enumerate(pairs, 1):
        t, e = b.claims[tid], b.experiments[eid]
        # Development species expectation comes from explicit scientific identity, not the retriever's output.
        ta, ea = set(t['raw']['species'] or []), set(e['raw']['species'] or [])
        expected = 'overlap_in_reported_species' if ta & ea else 'different_species'
        case_id = f'RC{n:03}'
        source = b.sources[t['raw']['source_key']]
        tp = packet(t['raw'])
        tp['citation'] = source['attribution']
        cases.append(
            {
                'case_id': case_id,
                'traditional_record_id': tid,
                'evidence_id': eid,
                'construction': origin,
                'traditional': tp,
                'experiment': packet(e['raw']),
                'claim_evaluation_group_id': t['evaluation_group_id'],
                'evidence_evaluation_group_id': e['evaluation_group_id'],
                'split': 'development_only',
                'independent_review_status': 'pending',
                'instruction': 'Open both cited sources, verify the recorded fields, and record unknowns. Do not infer clinical benefit from preclinical results.',
            }
        )
        expectations.append(
            {
                'case_id': case_id,
                'traditional_record_id': tid,
                'evidence_id': eid,
                'expected_taxon': expected,
                'expected_retrieval_membership': bool(ta & ea),
                'basis': 'Curated scientific-name fields only; not a clinical relevance judgement',
                'gold_standard': False,
                'use': 'development_structural_check_only',
            }
        )
        pending.append(
            {
                'case_id': case_id,
                'reviewer_a': None,
                'reviewer_b': None,
                'status': 'pending',
                'retrieval_relevant': None,
                'pair_label': None,
                'taxon': None,
                'plant_part': None,
                'solvent': None,
                'outcome': None,
                'rationale': None,
                'source_locators': [],
                'disagreement': None,
            }
        )
    save(ROOT / 'data/review/review_cases.jsonl', cases)
    save(ROOT / 'data/evaluation/development_expectations.jsonl', expectations)
    adjudicated = ROOT / 'data/review/adjudicated.jsonl'
    if not adjudicated.exists():
        save(adjudicated, pending)
    else:
        existing = {r['case_id'] for r in rows(adjudicated)}
        if existing != {r['case_id'] for r in cases}:
            raise ValueError('Review IDs changed; preserve existing annotations and reconcile explicitly.')
    for slot in ('a', 'b'):
        path = ROOT / f'data/review/reviewer_{slot}.jsonl'
        if path.exists():
            continue
        save(
            path,
            [
                {
                    'schema_version': 2,
                    'case_id': r['case_id'],
                    'reviewer_id': f'reviewer_{slot}',
                    'status': 'pending',
                    'retrieval_relevant': None,
                    'extraction_verified': False,
                    'corrections': [],
                    'extraction_verification_provenance': None,
                    'comparison_review_status': 'pending',
                    'claim_comparability': {
                        'label': None,
                        'interpretation': 'narrow_documented_traditional_use',
                        'rationale': None,
                    },
                    'experimental_findings': {
                        'result_direction': None,
                        'reported_result': None,
                        'study_setting': None,
                        'endpoint': None,
                        'source_id': None,
                        'source_url': None,
                        'passage_locator': None,
                    },
                    'experimental_findings_review_status': 'pending',
                    'comparison_review_provenance': {
                        'method': None,
                        'confirmation': None,
                        'independent_blinded_annotation': None,
                        'partner_comparison_review': None,
                    },
                    'pair_label': None,
                    'taxon': None,
                    'plant_part': None,
                    'solvent': None,
                    'outcome': None,
                    'rationale': None,
                    'source_locators': [],
                    'reviewed_on': None,
                }
                for r in cases
            ],
        )
    print(f'Built {len(cases)} review packets. Existing reviewer/adjudication files were not overwritten.')


if __name__ == '__main__':
    build()
