import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from atlas import summarize


class AtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / 'web/data.js').read_text(encoding='utf-8').split(' = ', 1)[1].rstrip(';\n'))
        cls.accounts = {r['id']: r for r in cls.data['claims']}

    def test_all_accounts_including_unresolved_and_shared_species(self):
        self.assertEqual(len(self.accounts), 12)
        for tid in ['T005', 'T006']:
            self.assertEqual(self.accounts[tid]['retrieval_status'], 'unresolved_species')
            self.assertEqual(self.accounts[tid]['atlas']['experimental_units'], 0)
        self.assertNotEqual(
            self.accounts['T013']['claim']['preparation'], self.accounts['T014']['claim']['preparation']
        )

    def test_dimension_counts_partition_extracted_units_only(self):
        for c in self.accounts.values():
            expected = {
                r['evidence_id'] for r in c['results'] if r['evidence_level'] == 'selected_full_text_experimental_unit'
            }
            for buckets in c['atlas']['dimensions'].values():
                ids = [eid for b in buckets.values() for eid in b['evidence_ids']]
                self.assertEqual(set(ids), expected)
                self.assertEqual(len(ids), len(expected))

    def test_part_variation_and_shared_publication_preserved(self):
        a = self.accounts['T008']['atlas']
        self.assertEqual(a['dimensions']['part']['different_parts']['evidence_ids'], ['E004'])
        self.assertEqual(a['dimensions']['part']['overlap_in_parts']['evidence_ids'], ['E003'])
        self.assertEqual(a['unique_publications'], 1)
        self.assertEqual(a['experimental_units'], 2)

    def test_retrieval_scores_do_not_change_comparisons(self):
        import copy

        for c in self.accounts.values():
            altered = copy.deepcopy(c['results'])
            for r in altered:
                r['score'] = {'total': 9999}
            self.assertEqual(summarize(altered), c['atlas'])

    def test_leads_do_not_gain_findings_or_review(self):
        a = self.accounts['T013']['atlas']
        self.assertGreater(a['literature_leads'], 0)
        self.assertEqual(a['experimental_units'], 0)
        self.assertEqual(a['comparison_reviews'], 0)
        self.assertEqual(a['dimensions']['finding'], {})


if __name__ == '__main__':
    unittest.main()
