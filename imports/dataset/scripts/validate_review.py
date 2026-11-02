"""Check review coverage, citations, unresolved pairing, and training exclusion."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def rows(name):
    return [json.loads(s) for s in (ROOT / 'data' / name).read_text().splitlines() if s.strip()]
papers = {p['paper_id']: p for p in rows('papers.jsonl')}
traditional = {t['record_id']: t for t in rows('traditional_records.jsonl')}
reviews = rows('study_reviews.jsonl')
pairs = rows('claim_study_pair_assessments.jsonl')
assert len(reviews) == len(papers) == len({r['paper_id'] for r in reviews})
assert {r['paper_id'] for r in reviews} == set(papers)
# v0.6 audit covers the original two records only.
expected = {(t, p) for t in ('T005', 'T006') for p in papers}
assert {(r['traditional_record_id'], r['paper_id']) for r in pairs} == expected
assert len(pairs) == len(expected)
for r in reviews:
    assert r['citation'] == papers[r['paper_id']]['citation']
    assert r['source_url'] == papers[r['paper_id']]['source_url']
    assert r['independent_review'] is False and r['training_eligible'] is False
    assert len(r['abstract_sha256']) == 64 and r['next_action']
for r in pairs:
    assert r['study_citation'] == papers[r['paper_id']]['citation']
    assert r['traditional_source_url'] == traditional[r['traditional_record_id']]['source_url']
    assert r['evidence_label'] is None
    assert r['training_eligible'] is False and r['independent_review'] is False
summary = json.loads((ROOT / 'data/review_summary.json').read_text())
assert summary['candidate_pairs'] == sum(p['candidate_from_common_name'] for p in pairs)
assert summary['verified_pairs'] == summary['training_eligible_pairs'] == 0
print(f'PASS: {len(reviews)} cited reviews and {len(pairs)} unique pair assessments; unresolved pairs excluded from training')
