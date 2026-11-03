import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from gaps import explain
from retrieve import Baseline
class GapTests(unittest.TestCase):
 def test_unknown_is_record_missing_not_source_absent(self):
  b=Baseline();c=b.claims['T011']['raw'];r=b.retrieve('T011',1000)
  gaps=explain(c,r['results'],r['status'])
  prep=next(g for g in gaps if g['kind']=='traditional_preparation')
  self.assertEqual(prep['missingness'],'not_recorded_source_status_unresolved')
  self.assertIn('original source',prep['reason'])
 def test_unresolved_identity_is_not_claimed_unstudied(self):
  b=Baseline();r=b.retrieve('T005',1000)
  g=explain(b.claims['T005']['raw'],r['results'],r['status'])
  self.assertEqual(g[0]['kind'],'identity')
  self.assertFalse(any(x['kind']=='coverage' for x in g))
 def test_leads_are_not_experimental_findings(self):
  b=Baseline();r=b.retrieve('T013',1000)
  g=explain(b.claims['T013']['raw'],r['results'],r['status'])
  self.assertEqual(g[0]['missingness'],'not_yet_extracted')
  self.assertFalse(any(x['kind']=='setting' for x in g))
 def test_gap_ids_resolve_to_cited_evidence(self):
  b=Baseline()
  for tid,c in b.claims.items():
   r=b.retrieve(tid,1000);ids={e['evidence_id'] for e in r['results']}
   for gap in explain(c['raw'],r['results'],r['status']):self.assertTrue(set(gap['evidence_ids'])<=ids)
