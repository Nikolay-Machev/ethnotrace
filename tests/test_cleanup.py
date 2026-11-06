import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from retrieve import Baseline as FrozenBaseline, ROOT, rows
from current_retrieve import Baseline
from review_progress import grouped_review_records

class CleanupTests(unittest.TestCase):
    def test_current_reviews_preserve_decisions_and_resolve_history(self):
        history = {r['history_id']: r['record'] for r in rows(ROOT / 'data/review/history/retrieval_relevance_history.jsonl')}
        current = rows(ROOT / 'data/review/retrieval_relevance.jsonl')
        self.assertEqual(len(current), len(history))
        for record in current:
            prior = history[record['history_id']]
            for field in ('claim_id', 'evidence_id', 'human_reviewer_id', 'human_rationale', 'human_retrieval_relevant'):
                self.assertEqual(record[field], prior[field])
            self.assertFalse(any(k.endswith('_history') for k in record))
        grouped_review_records(current)

    def test_completed_unresolved_reason_rejected_but_scientific_unknown_allowed(self):
        record = copy.deepcopy(rows(ROOT / 'data/review/retrieval_relevance.jsonl')[0])
        record['human_review_details']['compares'] = {'preparation': 'not established'}
        grouped_review_records([record])
        record['human_review_details']['unresolved_reason'] = 'Still awaiting a relevance decision'
        with self.assertRaisesRegex(ValueError, 'unresolved_reason'):
            grouped_review_records([record])

    def test_part_mismatch_has_no_penalty_and_does_not_change_comparison(self):
        current, frozen = Baseline(), FrozenBaseline()
        claim, evidence = current.claims['T008'], current.documents['E004']
        old, new = frozen.score(claim, evidence), current.score(claim, evidence)
        self.assertEqual(new['parts'], 0)
        self.assertEqual(new['total'], old['total'] + 2)
        self.assertEqual(current.compare(claim, evidence), frozen.compare(claim, evidence))
        self.assertEqual(current.compare(claim, evidence)['plant_part'], 'different_parts')
