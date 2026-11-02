"""Validate catalogue screening, original-row provenance and separate lead tables."""
import json
from pathlib import Path
R = Path(__file__).resolve().parents[1]
def records(name):
    return [json.loads(s) for s in (R / 'data' / name).read_text().splitlines() if s.strip()]
s = json.loads((R / 'data/catalogue_screening_summary.json').read_text())
screen = records('catalogue_resource_screening.jsonl')
assert len(screen) == len({r['resource_screening_id'] for r in screen}) == s['catalogue_resource_entries_screened']
assert all(r['rationale'] and r['inspection_depth'] for r in screen)
t = {r['record_id']: r for r in records('traditional_records.jsonl')}
raw = records('catalogue_imported_source_rows.jsonl')[0]
assert raw['row']['ETHNO'] == '15976'
assert raw['row']['TAXON'] == t['T016']['species'][0]
assert raw['row']['COUNTRY'] == 'Canada(Salish)' and raw['row']['ACTIVITY'] == 'Diabetes'
assert raw['row']['REFERENCE'] == t['T016']['underlying_reference_code'] == 'Eb25: 82'
assert t['T016']['plant_part'] is None and t['T016']['preparation'] is None
assert t['T016']['underlying_ethnobotanical_source_reviewed'] is False
assert t['T005']['species'] is None and t['T006']['species'] is None
crosswalk = records('taxon_crosswalk.jsonl')
assert len(crosswalk) == 8 and all(r['match_type'] == 'EXACT' for r in crosswalk)
for r in crosswalk:
    assert r['resolves_unidentified_common_names'] is False
    assert r['linked_traditional_record_ids']
    for rid in r['linked_traditional_record_ids']:
        assert r['input_scientific_name'] in t[rid]['species']
leads = records('catalogue_literature_leads.jsonl')
papers = records('papers.jsonl')
assert len(leads) == 2 and len(papers) == 51
assert not {r['pmid'] for r in leads} & {p['pmid'] for p in papers}
for r in leads:
    assert r['citation'] and r['limitations'] and r['doi']
    assert r['training_eligible'] is False and r['full_text_reviewed'] is False
assert len(records('experimental_records.jsonl')) == 12
print('PASS: 93 catalogue entries, one traceable Canadian use, eight scientific-name matches, two separate cited literature leads')
