"""Source-checked experimental finding directions remain distinct from human review."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return [json.loads(line) for line in (ROOT / path).read_text(encoding="utf-8").splitlines() if line.strip()]


class ExperimentalFindingSourceReviewTests(unittest.TestCase):
    def test_all_twelve_source_checks_match_current_normalized_endpoints(self):
        checks = load("data/review/experimental_finding_source_checks_2026-11-06.jsonl")
        units = load("data/processed/experimental_records.jsonl")
        self.assertEqual(len(checks), 12)
        self.assertEqual({c["experimental_id"] for c in checks}, {u["id"] for u in units})
        expected = {u["id"]: u for u in units}
        allowed = {"favourable_effect", "no_detected_effect", "condition_dependent", "statistically_inconclusive"}
        for c in checks:
            unit = expected[c["experimental_id"]]
            self.assertIn(c["source_derived_direction"], allowed)
            self.assertEqual(c["paper_id"], unit["raw"]["paper_id"])
            self.assertEqual(c["source_url"], unit["raw"]["source_url"])
            self.assertEqual(c["reported_endpoint"], unit["raw"]["endpoint"])
            self.assertTrue(c["consistent_with_current_active_direction"])
            self.assertEqual(c["source_derived_direction"], unit["features"]["experimental_result_direction"])
            self.assertTrue(c["source_sections_checked"])
            self.assertTrue(c["source_rationale"])
            self.assertFalse(c["research_provenance"]["human_approved"])
            self.assertFalse(c["research_provenance"]["independent_blinded_review"])

    def test_null_and_adverse_effects_are_not_hidden(self):
        checks = {c["experimental_id"]: c for c in load("data/review/experimental_finding_source_checks_2026-11-06.jsonl")}
        self.assertEqual(checks["E005"]["source_derived_direction"], "statistically_inconclusive")
        self.assertIn("exacerbated", checks["E004"]["source_rationale"])
        self.assertEqual(checks["E001"]["source_derived_direction"], "no_detected_effect")
        self.assertEqual(checks["E002"]["source_derived_direction"], "favourable_effect")
        self.assertEqual(checks["E009"]["source_derived_direction"], "no_detected_effect")
        self.assertEqual(checks["E012"]["source_derived_direction"], "no_detected_effect")


if __name__ == "__main__":
    unittest.main()
