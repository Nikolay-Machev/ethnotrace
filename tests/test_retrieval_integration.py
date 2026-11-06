"""Current evaluation must reconcile reviewers without changing the frozen pilot."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import evaluate_retrieval as current
import build_evaluation

class ReconciledEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.records=current.rows(current.ROOT/'data/review/retrieval_relevance.jsonl')
        self.original_rows=current.rows
    def evaluate(self, records):
        def read(path):
            return records if path.name=='retrieval_relevance.jsonl' else self.original_rows(path)
        with patch.object(current,'rows',side_effect=read):
            return current.evaluate()['human_reviewed_development']
    def test_submission_order_does_not_change_result(self):
        self.assertEqual(self.evaluate(self.records),self.evaluate(list(reversed(self.records))))
    def test_pending_companion_review_excludes_account_in_both_orders(self):
        records=copy.deepcopy(self.records)
        record=records[0];tid=record['claim_id']
        record['human_review_status']='pending';record['human_retrieval_relevant']=None
        for ordered in (records,list(reversed(records))):
            result=self.evaluate(ordered)
            self.assertNotIn(tid,[q['claim_id'] for q in result['queries']])
            self.assertIn(tid,[q['claim_id'] for q in result['excluded_queries']])
    def test_conflicting_completed_review_fails_closed(self):
        records=copy.deepcopy(self.records)
        records[0]['human_retrieval_relevant']=not records[0]['human_retrieval_relevant']
        for ordered in (records,list(reversed(records))):
            with self.assertRaisesRegex(ValueError,'require adjudication'):
                self.evaluate(ordered)
    def test_stale_pilot_result_is_not_displayed(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);folder=root/'data/generalization';folder.mkdir(parents=True)
            for name in ('manifest.json','reviews.jsonl','assisted_exploratory_results.json'):
                (folder/name).write_bytes((current.ROOT/'data/generalization'/name).read_bytes())
            with patch.object(build_evaluation,'ROOT',root):
                self.assertTrue(build_evaluation.pilot_summary()['recorded_result_current'])
                with (folder/'reviews.jsonl').open('a') as f:f.write('\n')
                result=build_evaluation.pilot_summary()
                self.assertFalse(result['recorded_result_current']);self.assertIsNone(result['result'])
