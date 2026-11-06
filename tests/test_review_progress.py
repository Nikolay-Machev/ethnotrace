import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import review_progress


class ReviewProgressTests(unittest.TestCase):
    def fixture(self, root, entry):
        p = root / 'data/review'
        p.mkdir(parents=True)
        (p / 'retrieval_relevance.jsonl').write_text(json.dumps(entry) + '\n', encoding='utf-8', newline='\n')
        for k in ('a', 'b'):
            (p / f'reviewer_{k}.jsonl').write_text('', encoding='utf-8', newline='\n')

    def test_assistant_relevance_does_not_count_as_human_review(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(
                root,
                dict(
                    claim_id='T008',
                    evidence_id='P26626246',
                    provisional_retrieval_relevant=True,
                    human_review_status='pending',
                ),
            )
            with patch.object(review_progress, 'ROOT', root):
                self.assertEqual(review_progress.report()['human_relevance_completed'], 0)

    def test_completion_requires_named_source_review(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(
                root,
                dict(
                    claim_id='T008',
                    evidence_id='P26626246',
                    human_review_status='completed',
                    human_retrieval_relevant=True,
                    human_rationale='Copied answer',
                ),
            )
            with patch.object(review_progress, 'ROOT', root):
                with self.assertRaises(ValueError):
                    review_progress.report()

    def test_provisional_decision_is_separate_from_confirmed_and_unresolved(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self.fixture(
                root,
                dict(
                    claim_id='T010',
                    evidence_id='P20301057',
                    human_review_status='provisional',
                    human_retrieval_relevant=None,
                    human_provisional_retrieval_relevant=True,
                    source_checked=True,
                ),
            )
            with patch.object(review_progress, 'ROOT', root):
                result = review_progress.report()
            self.assertEqual(result['human_relevance_completed'], 0)
            self.assertEqual(result['human_relevance_provisional'], 1)
            self.assertEqual(result['source_checked_unresolved'], 0)

    def test_separate_unresolved_reviewers_count_as_one_pair(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            entry = dict(
                claim_id='T007',
                evidence_id='P18066122',
                human_review_status='pending',
                human_retrieval_relevant=None,
                source_checked=True,
            )
            self.fixture(root, entry)
            with (root / 'data/review/retrieval_relevance.jsonl').open('a', encoding='utf-8') as f:
                f.write(
                    json.dumps({**entry, 'human_review_status': 'unresolved', 'human_reviewer_id': 'second'}) + '\n'
                )
            with patch.object(review_progress, 'ROOT', root):
                result = review_progress.report()
            self.assertEqual(result['relevance_candidates'], 1)
            self.assertEqual(result['review_submission_count'], 2)
            self.assertEqual(result['source_checked_unresolved'], 1)

    def test_multiple_final_judgments_require_adjudication(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            entry = dict(
                claim_id='T007',
                evidence_id='P18066122',
                human_review_status='completed',
                human_retrieval_relevant=True,
                source_checked=True,
                human_reviewer_id='first',
                human_rationale='Checked',
            )
            self.fixture(root, entry)
            with (root / 'data/review/retrieval_relevance.jsonl').open('a', encoding='utf-8') as f:
                f.write(json.dumps({**entry, 'human_retrieval_relevant': False, 'human_reviewer_id': 'second'}) + '\n')
            with patch.object(review_progress, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'require adjudication'):
                    review_progress.report()
