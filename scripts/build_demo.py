"""Export baseline results and recorded review status to a static, offline demo."""

import json
from collections import defaultdict
from current_retrieve import Baseline, ROOT, VERSION, rows
from atlas import summarize
from gaps import explain
from current_semantic import load_snapshot


def group_by(records, key):
    """Group records by a field, keeping the original order within each group."""
    grouped = defaultdict(list)
    for record in records:
        grouped[record[key]].append(record)
    return grouped


def build():
    b = Baseline()
    semantic = load_snapshot(b)
    reviews = {key: {r['case_id']: r for r in rows(ROOT / f'data/review/reviewer_{key}.jsonl')} for key in ('a', 'b')}
    cases = {
        (r['traditional_record_id'], r['evidence_id']): r['case_id']
        for r in rows(ROOT / 'data/review/review_cases.jsonl')
    }
    display = json.loads((ROOT / "data/curated/display_text.json").read_text(encoding='utf-8'))
    targeted = group_by(rows(ROOT / "data/curated/targeted_extractions.jsonl"), 'claim_id')
    missing_field_evidence = rows(ROOT / "data/curated/missing_field_source_evidence.jsonl")
    relevance_reviews = group_by(rows(ROOT / "data/review/retrieval_relevance.jsonl"), 'claim_id')
    claims = []
    names = {'T011': 'Lingonberry', 'T007': 'Tamarack', 'T008': 'Pitcher plant'}
    names.update(
        {
            tid: '; '.join(r['raw'].get('species') or r['raw'].get('original_plant_name') or [tid])
            for tid, r in b.claims.items()
            if tid not in names
        }
    )
    for tid, name in names.items():
        retrieved = b.retrieve(tid, 1000)
        results = retrieved['results']
        for result in results:
            cid = cases.get((tid, result['evidence_id']))
            result['case_id'] = cid
            result['human_comparison_reviews'] = sum(
                reviews[k].get(cid, {}).get('comparison_review_status') == 'completed' for k in reviews
            )
            result['extraction_verifications'] = sum(
                reviews[k].get(cid, {}).get('extraction_verified') is True for k in reviews
            )
            result['human_judgments'] = [
                {
                    'reviewer': key,
                    'label': reviews[key].get(cid, {}).get('pair_label'),
                    'provenance': reviews[key].get(cid, {}).get('comparison_review_provenance'),
                }
                for key in reviews
                if reviews[key].get(cid, {}).get('comparison_review_status') == 'completed'
            ]
            raw = b.documents[result['evidence_id']]['raw']
            result['title'] = raw.get('title') or result['study'].get('endpoint') or result['evidence_id']
        claims.append(
            {
                'id': tid,
                'name': name,
                'claim': b.cited_account(tid),
                'display_use': display.get(tid, {}).get('use'),
                'results': results,
                'retrieval_status': retrieved['status'],
                'atlas': summarize(results),
                'gaps': explain(
                    b.claims[tid]['raw'],
                    results,
                    retrieved['status'],
                    relevance_reviews[tid],
                ),
                'targeted_extractions': targeted[tid],
                'supplemental_missing_field_evidence': [
                    r
                    for r in missing_field_evidence
                    if (r['record_type'] == 'traditional' and r['record_id'] == tid)
                    or (
                        r['record_type'] == 'experimental'
                        and r['record_id'] in {item['evidence_id'] for item in results}
                    )
                ],
                'rankings': semantic['rankings'][tid] if semantic else None,
            }
        )
    data = {
        'retrieval_provider': {
            'id': 'lexical_baseline',
            'version': VERSION,
            'semantic_enabled': bool(semantic),
            'semantic_model': semantic['model'] if semantic else None,
            'semantic_revision': semantic['revision'] if semantic else None,
            'input_sha256': semantic['input_sha256'] if semantic else None,
        },
        'baseline_version': VERSION,
        'claims': claims,
        'review_note': '; '.join(
            f"Reviewer {key.upper()}: {sum(r.get('comparison_review_status') == 'completed' for r in records.values())} completed comparison reviews, {sum(r.get('extraction_verified') is True for r in records.values())} extraction verifications"
            for key, records in reviews.items()
        ),
    }
    target = ROOT / 'web/data.js'
    target.parent.mkdir(exist_ok=True)
    target.write_text(
        '// Generated, do not edit. Run python3 scripts/rebuild.py.\nwindow.ETHNOTRACE_DATA = '
        + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
        + ';\n',
        encoding='utf-8',
        newline='\n',
    )
    return data


if __name__ == '__main__':
    d = build()
    print(f"Exported {len(d['claims'])} accounts to web/data.js")
