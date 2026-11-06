"""Unit tests for Baseline.compare and Baseline.score using small hand-made records."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from retrieve import Baseline  # noqa: E402


def record(names=('Larix laricina',), parts=('bark',), solvents=(), use='', endpoint=None, setting=None, **raw):
    return {
        'id': 'X',
        'features': {
            'scientific_names': list(names),
            'plant_parts': list(parts),
            'extraction_solvents_explicit': list(solvents),
            'endpoint': endpoint,
            'study_settings': setting,
            'experimental_result_direction': None,
        },
        'raw': {'original_use_description': use, 'endpoint': endpoint, **raw},
    }


def baseline():
    b = Baseline.__new__(Baseline)  # compare() and score() read only their arguments and paper_titles
    b.paper_titles = {}
    return b


class CompareTests(unittest.TestCase):
    def setUp(self):
        self.b = baseline()

    def test_same_species_and_part_is_insufficient_not_comparable(self):
        c = self.b.compare(record(), record(endpoint='glycaemic AUC'))
        self.assertEqual(
            (c['taxon'], c['plant_part'], c['status']),
            ('overlap_in_reported_species', 'overlap_in_parts', 'insufficient_evidence'),
        )

    def test_different_species_is_not_directly_comparable(self):
        c = self.b.compare(record(), record(names=('Vaccinium vitis-idaea',)))
        self.assertEqual((c['taxon'], c['status']), ('different_species', 'not_directly_comparable'))

    def test_different_parts_is_not_directly_comparable(self):
        c = self.b.compare(record(parts=('leaf',)), record(parts=('root',)))
        self.assertEqual((c['plant_part'], c['status']), ('different_parts', 'not_directly_comparable'))

    def test_missing_part_or_species_stays_unknown(self):
        c = self.b.compare(record(parts=()), record(names=()))
        self.assertEqual((c['plant_part'], c['taxon'], c['status']), ('unknown', 'unknown', 'insufficient_evidence'))

    def test_different_explicit_solvents_are_a_mismatch(self):
        c = self.b.compare(record(solvents=('water',)), record(solvents=('ethanol',)))
        self.assertEqual((c['solvent'], c['status']), ('different_solvents', 'not_directly_comparable'))

    def test_shared_solvent_does_not_establish_equivalence(self):
        c = self.b.compare(record(solvents=('ethanol',)), record(solvents=('ethanol',)))
        self.assertEqual((c['solvent'], c['preparation_equivalence']), ('shared_solvent_only', 'not_established'))

    def test_slow_healing_use_against_cell_viability_is_a_different_endpoint(self):
        c = self.b.compare(
            record(use='Used for slow-healing infections'), record(endpoint='cell_viability_high_glucose')
        )
        self.assertEqual((c['outcome'], c['status']), ('different_endpoint', 'not_directly_comparable'))

    def test_preclinical_setting_adds_a_caveat_and_clinical_conclusions_stay_empty(self):
        c = self.b.compare(record(), record(setting=['animal_in_vivo']))
        self.assertIn('Preclinical results do not establish clinical efficacy in people.', c['reasons'])
        self.assertIsNone(c['medical_efficacy_conclusion'])
        self.assertFalse(c['independent_review'])


class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.b = baseline()

    def test_different_species_is_not_scored(self):
        self.assertIsNone(self.b.score(record(), record(names=('Vaccinium vitis-idaea',))))

    def test_part_overlap_outranks_unknown_which_outranks_mismatch(self):
        overlap = self.b.score(record(), record())['total']
        unknown = self.b.score(record(), record(parts=()))['total']
        mismatch = self.b.score(record(), record(parts=('root',)))['total']
        self.assertGreater(overlap, unknown)
        self.assertGreater(unknown, mismatch)

    def test_lexical_overlap_only_uses_endpoint_and_title_text(self):
        claim = record(use='frequent urination and sugar')
        with_overlap = self.b.score(claim, record(endpoint='sugar urination'))
        without = self.b.score(claim, record(endpoint='unrelated words entirely'))
        self.assertGreater(with_overlap['lexical'], without['lexical'])
        self.assertEqual(without['lexical'], 0)


if __name__ == '__main__':
    unittest.main()
