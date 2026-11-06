import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from gaps import explain
from current_retrieve import Baseline
class GapTests(unittest.TestCase):
    def test_unknown_is_record_missing_not_source_absent(self):
        b = Baseline()
        c = b.claims['T011']['raw']
        r = b.retrieve('T011', 1000)
        gaps = explain(c, r['results'], r['status'])
        prep = next(g for g in gaps if g['kind'] == 'traditional_preparation')
        self.assertEqual(prep['missingness'], 'not_recorded_source_status_unresolved')
        self.assertIn('original source', prep['reason'])

    def test_unresolved_identity_is_not_claimed_unstudied(self):
        b = Baseline()
        r = b.retrieve('T005', 1000)
        g = explain(b.claims['T005']['raw'], r['results'], r['status'])
        self.assertEqual(g[0]['kind'], 'identity')
        self.assertFalse(any(x['kind'] == 'coverage' for x in g))

    def test_leads_are_not_experimental_findings(self):
        b = Baseline()
        r = b.retrieve('T013', 1000)
        g = explain(b.claims['T013']['raw'], r['results'], r['status'])
        self.assertEqual(g[0]['missingness'], 'not_yet_extracted')
        self.assertFalse(any(x['kind'] == 'setting' for x in g))

    def test_gap_ids_resolve_to_cited_evidence(self):
        b = Baseline()
        for tid, c in b.claims.items():
            r = b.retrieve(tid, 1000)
            ids = {e['evidence_id'] for e in r['results']}
            for gap in explain(c['raw'], r['results'], r['status']):
                self.assertTrue(set(gap['evidence_ids']) <= ids)

    def test_source_followup_is_cited_and_requires_a_checkable_result(self):
        b = Baseline()
        r = b.retrieve('T007', 1000)
        review = {
            'evidence_id': 'P18066122',
            'human_review_status': 'pending',
            'source_checked': True,
            'human_rationale': 'Species-specific tables inaccessible.',
        }
        g = explain(b.claims['T007']['raw'], r['results'], r['status'], [review])
        follow = next(x for x in g if x['kind'] == 'source_access')
        self.assertEqual(follow['evidence_ids'], ['P18066122'])
        self.assertIn('locator', follow['completion_criterion'])

    def test_unknown_alignment_does_not_assert_all_endpoints_differ(self):
        b = Baseline()
        r = b.retrieve('T011', 1000)
        g = explain(b.claims['T011']['raw'], r['results'], r['status'])
        self.assertFalse(any(x['kind'] == 'endpoint_coverage' for x in g))
