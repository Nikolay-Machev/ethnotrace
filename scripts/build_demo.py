"""Export baseline results and recorded review status to a static, offline demo."""
import json
from retrieve import Baseline, ROOT, VERSION, rows

def build():
    b = Baseline()
    reviews = {key: {r['case_id']: r for r in rows(ROOT / f'data/review/reviewer_{key}.jsonl')} for key in ('a', 'b')}
    cases = {(r['traditional_record_id'], r['evidence_id']): r['case_id'] for r in rows(ROOT / 'data/review/review_cases.jsonl')}
    claims = []
    names = {'T011': 'Lingonberry', 'T007': 'Tamarack', 'T008': 'Pitcher plant'}
    for tid, name in names.items():
        results = b.retrieve(tid, 1000)['results']
        for result in results:
            cid = cases.get((tid, result['evidence_id']))
            result['case_id'] = cid
            result['human_comparison_reviews'] = sum(reviews[k].get(cid, {}).get('comparison_review_status') == 'completed' for k in reviews)
            result['extraction_verifications'] = sum(reviews[k].get(cid, {}).get('extraction_verified') is True for k in reviews)
            raw = b.documents[result['evidence_id']]['raw']
            result['title'] = raw.get('title') or result['study'].get('endpoint') or result['evidence_id']
        claims.append({'id': tid, 'name': name, 'claim': b.claims[tid]['raw'], 'results': results})
    data = {'baseline_version': VERSION, 'claims': claims, 'review_note': 'One human comparison review complete; second pending. Reviewer A confirmed the assistant-proposed labels. Both reviewers reported extraction verification for the 20 review cases; other evidence entries are not covered.'}
    target = ROOT / 'web/data.js'
    target.parent.mkdir(exist_ok=True)
    target.write_text('window.ETHNOTRACE_DATA = ' + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c') + ';\n', encoding='utf-8')
    return data

if __name__ == '__main__':
    d = build()
    print(f"Exported {len(d['claims'])} accounts to web/data.js")
