import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from retrieve import Baseline
from evaluate import evaluate


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.b = Baseline()

    def test_unknown_species_abstains_instead_of_guessing_common_name(self):
        for rid in ('T005', 'T006'):
            r = self.b.retrieve(rid)
            self.assertEqual(r['status'], 'unresolved_species')
            self.assertEqual(r['results'], [])

    def test_same_genus_is_not_same_species(self):
        r = self.b.compare(self.b.claims['T013'], self.b.experiments['E008'])
        self.assertEqual(r['taxon'], 'different_species')
        self.assertEqual(r['status'], 'not_directly_comparable')
        self.assertNotIn('E008', [r['evidence_id'] for r in self.b.retrieve('T013', 100)['results']])

    def test_roots_and_neuronal_endpoint_do_not_validate_leaf_infection_use(self):
        r = self.b.compare(self.b.claims['T008'], self.b.experiments['E004'])
        self.assertEqual(r['plant_part'], 'different_parts')
        self.assertEqual(r['outcome'], 'different_endpoint')
        self.assertEqual(r['experimental_result_direction'], 'no_detected_effect')

    def test_ranking_does_not_read_annotations_or_positive_results(self):
        claim, evidence = self.b.claims['T011'], self.b.experiments['E008']
        first = self.b.score(claim, evidence)
        altered = copy.deepcopy(evidence)
        altered['features']['experimental_result_direction'] = 'no_detected_effect'
        altered['raw']['reported_use_or_outcome'] = 'different annotation'
        altered['raw']['classification'] = {'label': 'insufficient_evidence', 'rationale': 'do not read this'}
        self.assertEqual(first, self.b.score(claim, altered))

    def test_extraction_level_and_citations_are_explicit(self):
        r = self.b.retrieve('T011', 100)
        self.assertTrue(r['results'])
        for e in r['results']:
            self.assertTrue(e['source']['citation'])
            self.assertTrue(e['source']['url'])
            self.assertIsNone(e['comparison']['medical_efficacy_conclusion'])
        self.assertNotIn('P25013446', self.b.documents)  # extracted units, not duplicate paper
        self.assertIn('E008', self.b.documents)
        self.assertEqual(
            self.b.retrieve('T013', 10)['results'][0]['evidence_level'],
            'bibliographic_or_abstract_lead_not_extracted_experiment',
        )

    def test_pending_review_does_not_produce_scientific_accuracy(self):
        report, predictions = evaluate()
        self.assertEqual(len(predictions), 20)
        self.assertEqual(report['independent_review']['adjudicated_cases'], 0)
        self.assertIsNone(report['independent_review']['comparison_accuracy'])
        self.assertIsNone(report['independent_review']['macro_recall_at_5'])

    def test_assisted_review_is_not_independent_accuracy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / 'data/review/reviewer_a.jsonl'
            records = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            for r in records:
                r['comparison_review_status'] = 'completed'
                r['pair_label'] = r['claim_comparability']['label'] = 'insufficient_evidence'
                r['comparison_review_provenance']['independent_blinded_annotation'] = False
            path.write_text(''.join(json.dumps(r) + '\n' for r in records), encoding='utf-8', newline='\n')
            # This test deliberately changes all reviewer labels. Remove the
            # previously observed consensus from this temporary scenario.
            gold_path = root / 'data/review/adjudicated.jsonl'
            gold = [json.loads(line) for line in gold_path.read_text(encoding='utf-8').splitlines()]
            for item in gold:
                item['status'] = 'pending'
            gold_path.write_text(''.join(json.dumps(item) + '\n' for item in gold), encoding='utf-8', newline='\n')
            report, _ = evaluate(root)
        self.assertEqual(report['review_progress']['a']['comparison_completed_cases'], 20)
        self.assertEqual(report['review_progress']['a']['assisted_comparison_cases'], 20)
        self.assertIsNone(report['experimental_findings_evaluation']['accuracy'])
        self.assertIsNone(report['independent_review']['comparison_accuracy'])

    def test_assisted_consensus_is_reported_separately_from_independent_gold(self):
        report, _ = evaluate()
        self.assertEqual(report['assisted_comparison_consensus']['completed_cases'], 20)
        self.assertEqual(report['assisted_comparison_consensus']['disagreement_cases'], 0)
        self.assertFalse(report['assisted_comparison_consensus']['independent_gold_eligible'])
        self.assertEqual(report['independent_review']['adjudicated_cases'], 0)
        self.assertIsNone(report['independent_review']['comparison_accuracy'])

    def test_false_assisted_consensus_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / 'data/review/reviewer_a.jsonl'
            rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            rows[0]['pair_label'] = rows[0]['claim_comparability']['label'] = 'support'
            path.write_text(''.join(json.dumps(row) + '\n' for row in rows), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(ValueError, 'Invalid assisted comparison consensus'):
                evaluate(root)

    def test_supplemental_community_parts_do_not_change_original_claims(self):
        rows = [
            json.loads(line)
            for line in (ROOT / 'data/curated/missing_field_source_evidence.jsonl')
            .read_text(encoding='utf-8')
            .splitlines()
        ]
        self.assertEqual(len(rows), 18)
        supported = [r for r in rows if r['source_supported_value'] is not None]
        self.assertEqual({r['record_id'] for r in supported}, {'T007', 'T009', 'T010', 'T012'})
        for r in supported:
            self.assertEqual(r['field'], 'plant_part')
            self.assertEqual(r['source_context_status'], 'community_survey_supported')
            self.assertTrue(r['source_urls'])
            self.assertIsNone(self.b.claims[r['record_id']]['raw']['plant_part'])
            self.assertIsNone(self.b.claims[r['record_id']]['features']['plant_parts'])

    def test_reviewer_files_preserve_separate_labels_and_verification(self):
        for slot in ('a', 'b'):
            records = [
                json.loads(line)
                for line in (ROOT / f'data/review/reviewer_{slot}.jsonl').read_text(encoding='utf-8').splitlines()
            ]
            self.assertEqual(len({r['case_id'] for r in records}), 20)
            for record in records:
                self.assertEqual(record['schema_version'], 2)
                self.assertIsInstance(record['extraction_verified'], bool)
                self.assertEqual(record['pair_label'], record['claim_comparability']['label'])

    def test_false_adjudication_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / 'data', root / 'data')
            path = root / 'data/review/adjudicated.jsonl'
            rs = [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines()]
            rs[0]['status'] = 'adjudicated'
            path.write_text(''.join(json.dumps(r) + '\n' for r in rs), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(ValueError, 'independent review provenance'):
                evaluate(root)

    def test_review_packets_do_not_include_old_labels_or_expected_answers(self):
        packets = [
            json.loads(s) for s in (ROOT / 'data/review/review_cases.jsonl').read_text(encoding='utf-8').splitlines()
        ]
        self.assertEqual(len({p['case_id'] for p in packets}), 20)
        for p in packets:
            for key in ('traditional', 'experiment'):
                self.assertNotIn('classification', p[key])
                self.assertNotIn('result_direction', p[key])
            self.assertEqual(p['split'], 'development_only')

    def test_extracted_units_use_parent_title_without_result_leakage(self):
        claim = self.b.claims['T007']
        evidence = self.b.experiments['E002']
        original = self.b.score(claim, evidence)
        self.assertGreater(original['lexical'], 0)
        self.b.paper_titles[evidence['raw']['paper_id']] = ''
        self.assertEqual(self.b.score(claim, evidence)['lexical'], 0)

    def test_deterministic_ranking_and_invalid_input(self):
        self.assertEqual(self.b.retrieve('T011'), self.b.retrieve('T011'))
        with self.assertRaises(ValueError):
            self.b.retrieve('unknown')
        with self.assertRaises(ValueError):
            self.b.retrieve('T011', 0)


if __name__ == '__main__':
    unittest.main()
