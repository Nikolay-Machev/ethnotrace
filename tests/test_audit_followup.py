import itertools,sys,unittest
from pathlib import Path
from statistics import mean
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_evaluation import random_expectation
from current_retrieve import Baseline,ROOT,rows
class AuditTests(unittest.TestCase):
 def test_random_expectation_matches_exhaustive_uniform_orders(self):
  n,m=6,2
  orders=list(itertools.permutations(range(n)))
  expected=(mean(sum(i<m for i in order[:5])/m for order in orders),
            mean(1/next(j for j,i in enumerate(order,1) if i<m) for order in orders))
  for got,want in zip(random_expectation(n,m),expected):self.assertAlmostEqual(got,want)
 def test_corrected_finding_preserves_original_and_pair_judgment(self):
  b=Baseline()
  record=next(x for x in rows(ROOT/'data/processed/experimental_records.jsonl') if x['id']=='E005')
  pair=next(x for x in rows(ROOT/'data/processed/extracted_claim_study_pairs.jsonl') if x['id']=='T009__E005')
  self.assertEqual(record['raw']['result_direction'],'support')
  self.assertEqual(pair['raw']['claim_evidence_label'],pair['normalized']['claim_evidence_label'])
  result=b.present(b.claims['T009'],b.experiments['E005'])
  self.assertEqual(result['comparison']['experimental_result_direction'],'statistically_inconclusive')
  self.assertEqual(pair['normalized']['study_result_label'],'statistically_inconclusive')
  self.assertIn('Discussion',result['source']['locator'])
