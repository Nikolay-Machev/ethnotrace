import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('preprocess', ROOT / 'scripts/preprocess.py')
pipeline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pipeline)


def records(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s.strip()]


class PreprocessingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / 'first'
        cls.report = pipeline.run(output=cls.out)
        cls.trad = {r['id']: r for r in records(cls.out / 'traditional_records.jsonl')}
        cls.exp = {r['id']: r for r in records(cls.out / 'experimental_records.jsonl')}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_all_active_rows_and_documents_preserved(self):
        src = ROOT / 'imports/dataset/data'
        for path in src.glob('*.jsonl'):
            self.assertEqual([r['raw'] for r in records(self.out / path.name)], records(path))
        for path in src.glob('*.json'):
            self.assertEqual(
                json.loads((self.out / path.name).read_text(encoding='utf-8'))['raw'],
                json.loads(path.read_text(encoding='utf-8')),
            )

    def test_unknown_species_parts_and_preparations_stay_unknown(self):
        for rid in ['T005', 'T006']:
            self.assertIsNone(self.trad[rid]['features']['scientific_names'])
        self.assertIsNone(self.trad['T015']['features']['plant_parts'])
        self.assertIsNone(self.trad['T016']['features']['extraction_solvents_explicit'])
        self.assertIsNone(self.exp['E001']['features']['plant_parts'])

    def test_result_direction_is_not_claim_support(self):
        self.assertEqual(self.exp['E002']['features']['experimental_result_direction'], 'favourable_effect')
        self.assertEqual(self.exp['E001']['features']['experimental_result_direction'], 'no_detected_effect')
        pairs = records(self.out / 'extracted_claim_study_pairs.jsonl')
        self.assertTrue(all(r['features']['claim_comparability']['claim_evidence_label'] != 'support' for r in pairs))
        self.assertTrue(all(r['features']['training_eligible'] is False for r in pairs))

    def test_dose_and_concentration_do_not_conflate(self):
        a = self.exp['E002']['features']['exposure']
        b = self.exp['E010']['features']['exposure']
        self.assertEqual(a['dose_values'], [125, 250])
        self.assertEqual(a['dose_unit'], 'mg/kg')
        self.assertEqual(b['concentration_values'], [75])
        self.assertEqual(b['concentration_unit'], 'ug/mL')
        self.assertNotIn('dose_values', b)
        self.assertEqual(self.exp['E005']['features']['exposure_duration_hours'], 168)
        self.assertEqual(self.exp['E003']['features']['exposure_duration_hours'], 96)

    def test_shared_arm_exposure_and_grouping(self):
        a, b = self.exp['E006'], self.exp['E007']
        self.assertEqual(a['features']['exposure']['shared_arm_group'], b['features']['exposure']['shared_arm_group'])
        self.assertEqual(a['evaluation_group_id'], b['evaluation_group_id'])
        self.assertEqual(b['features']['preparation_context_inherited_from'], 'E006')
        for r in records(self.out / 'extracted_claim_study_pairs.jsonl'):
            raw = r['raw']
            self.assertEqual(
                self.trad[raw['traditional_record_id']]['evaluation_group_id'],
                self.exp[raw['experimental_record_id']]['evaluation_group_id'],
            )

    def test_all_citations_resolve_and_source_language_survives(self):
        refs = {r['reference_id'] for r in records(self.out / 'references.jsonl')}
        self.assertEqual(len(refs), self.report['reference_entries'])
        for path in self.out.glob('*.jsonl'):
            if path.name in ('references.jsonl', 'evaluation_groups.jsonl', 'grouping_edges.jsonl'):
                continue
            for r in records(path):
                self.assertTrue(set(r['provenance']['citation_refs']) <= refs)
        self.assertIn('sqw', self.trad['T015']['raw']['original_plant_name'][0])
        self.assertEqual(
            self.trad['T005']['raw']['supporting_passage'], self.trad['T005']['normalized']['supporting_passage']
        )

    def test_deterministic_rerun(self):
        second = Path(self.tmp.name) / 'second'
        pipeline.run(output=second)
        for path in self.out.iterdir():
            self.assertEqual(path.read_bytes(), (second / path.name).read_bytes(), path.name)

    def test_source_tampering_is_rejected(self):
        import shutil

        root = Path(self.tmp.name) / 'tampered'
        shutil.copytree(ROOT / 'imports', root / 'imports')
        shutil.copytree(ROOT / 'config', root / 'config')
        path = root / 'imports/dataset/data/traditional_records.jsonl'
        path.write_text(path.read_text(encoding='utf-8') + '\n', newline='\n')
        with self.assertRaisesRegex(ValueError, 'Pinned source changed'):
            pipeline.run(root=root, output=root / 'output')


if __name__ == '__main__':
    unittest.main()
