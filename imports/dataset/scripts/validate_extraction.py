"""Check extracted records, source links and partial-comparability safeguards."""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
def rows(name):
    return [json.loads(s) for s in (R / 'data' / name).read_text().splitlines() if s.strip()]
t = {r['record_id']: r for r in rows('traditional_records.jsonl')}
e = {r['record_id']: r for r in rows('experimental_records.jsonl')}
p = {r['paper_id']: r for r in rows('papers.jsonl')}
links = rows('extracted_claim_study_pairs.jsonl')
s = json.loads((R / 'data/expansion_summary.json').read_text())
assert len(t) == s['traditional_records'] and len(e) == s['experimental_units']
assert len({x for r in t.values() for x in (r['species'] or [])}) == s['identified_species']
assert len(links) == len({r['pair_id'] for r in links}) == s['taxon_aligned_extracted_pairs']
for link in links:
    tr, exp = t[link['traditional_record_id']], e[link['experimental_record_id']]
    assert set(tr['species']) & set(exp['species']), link['pair_id']
    assert exp['paper_id'] in p and exp['citation'] == p[exp['paper_id']]['citation']
    assert exp['result_direction'] == link['study_result_label']
    assert link['training_eligible'] is False and link['independent_review'] is False
    assert link['claim_evidence_label'] in {'not_directly_comparable', 'insufficient_evidence'}
assert e['E001']['result_direction'] == 'no_detected_effect'
assert e['E002']['result_direction'] == 'support'
assert p['P22888363']['classification']['label'] == 'mixed_evidence'
assert t['T005']['species'] is None and t['T006']['species'] is None
assert t['T015']['plant_part'] is None
assert t['T013']['preparation'] != 'boiled for cold symptoms'
assert len({r['paper_id'] for r in e.values()}) == s['experimental_publications']
print(f'PASS: {len(t)} traditional records, {len(e)} outcomes, {len(links)} taxonomic links; uncertainty preserved')
