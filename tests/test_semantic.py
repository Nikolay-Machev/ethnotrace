import copy,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from retrieve import Baseline
from semantic_retrieval import inputs,digest,fuse,snapshot,load_snapshot
from evaluate_semantic import metrics
class FakeEncoder:
 def encode_query(self,texts,**kwargs):return [[1.0,0.0] for _ in texts]
 def encode_document(self,texts,**kwargs):return [[0.0,1.0] for _ in texts]
class SemanticTests(unittest.TestCase):
 def test_same_species_gate_and_unresolved_names(self):
  b=Baseline();s=snapshot(b,FakeEncoder(),'0'*40,{})
  for tid,r in s['rankings'].items():
   expected={x['evidence_id'] for x in b.retrieve(tid,10000)['results']}
   for method in ('lexical','semantic','hybrid'):self.assertEqual(set(r[method]),expected)
  self.assertEqual(s['rankings']['T005']['semantic'],[])
  self.assertNotIn('E008',s['rankings']['T013']['semantic'])
 def test_ranker_inputs_do_not_read_judgments_or_result_direction(self):
  b=Baseline();before=digest(inputs(b))
  for r in b.documents.values():
   r['raw']['reported_use_or_outcome']='secret answer';r['raw']['supporting_passage']='secret answer'
   r['raw']['classification']={'label':'support'};r['features']['experimental_result_direction']='favourable_effect'
  self.assertEqual(before,digest(inputs(b)))
 def test_fusion_is_deterministic_and_rejects_pool_mismatch(self):
  self.assertEqual(fuse(['a','b'],['b','a'])[0],['a','b'])
  with self.assertRaises(ValueError):fuse(['a'],['b'])
 def test_stale_cache_fails_closed(self):
  b=Baseline();s=snapshot(b,FakeEncoder(),'0'*40,{})
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'cache.json';p.write_text(json.dumps(s));self.assertIsNotNone(load_snapshot(b,p))
   b.claims['T011']['raw']['original_use_description']='changed query'
   with self.assertRaises(ValueError):load_snapshot(b,p)
 def test_empty_positive_set_not_zero_accuracy(self):
  self.assertIsNone(metrics(['a'],set())['recall_at_5'])
 def test_compare_is_unchanged_after_semantic_generation(self):
  b=Baseline();before=b.compare(b.claims['T008'],b.experiments['E004'])
  snapshot(b,FakeEncoder(),'0'*40,{})
  self.assertEqual(before,b.compare(b.claims['T008'],b.experiments['E004']))
