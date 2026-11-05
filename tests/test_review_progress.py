import json,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import review_progress
class ReviewProgressTests(unittest.TestCase):
 def fixture(self,root,entry):
  p=root/'data/review';p.mkdir(parents=True)
  (p/'retrieval_relevance.jsonl').write_text(json.dumps(entry)+'\n')
  for k in ('a','b'):(p/f'reviewer_{k}.jsonl').write_text('')
 def test_assistant_relevance_does_not_count_as_human_review(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.fixture(root,dict(claim_id='T008',evidence_id='P26626246',provisional_retrieval_relevant=True,human_review_status='pending'))
   with patch.object(review_progress,'ROOT',root):self.assertEqual(review_progress.report()['human_relevance_completed'],0)
 def test_completion_requires_named_source_review(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.fixture(root,dict(claim_id='T008',evidence_id='P26626246',human_review_status='completed',human_retrieval_relevant=True,human_rationale='Copied answer'))
   with patch.object(review_progress,'ROOT',root):
    with self.assertRaises(ValueError):review_progress.report()
 def test_provisional_decision_is_separate_from_confirmed_and_unresolved(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.fixture(root,dict(claim_id='T010',evidence_id='P20301057',human_review_status='provisional',human_retrieval_relevant=None,human_provisional_retrieval_relevant=True,source_checked=True))
   with patch.object(review_progress,'ROOT',root):
    result=review_progress.report()
   self.assertEqual(result['human_relevance_completed'],0)
   self.assertEqual(result['human_relevance_provisional'],1)
   self.assertEqual(result['source_checked_unresolved'],0)
