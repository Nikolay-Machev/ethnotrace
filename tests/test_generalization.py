import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evaluate_generalization as pilot


class GeneralizationTests(unittest.TestCase):
    def test_unready_review_blocks_inference(self):
        manifest, candidates, reviews, ready = pilot.check()
        self.assertEqual(len(candidates), 10)
        with patch.object(pilot, "check", return_value=(manifest, candidates, reviews, False)):
            with self.assertRaisesRegex(ValueError, "Rankings withheld"):
                pilot.run(None)

    def test_assistant_source_research_and_assisted_approval_remain_non_blinded(self):
        source_path = (
            Path(__file__).resolve().parents[1] / "data/generalization/assistant_source_reviews_2026-11-05.jsonl"
        )
        researched = [json.loads(line) for line in source_path.read_text().splitlines() if line.strip()]
        _, candidates, reviews, ready = pilot.check()
        self.assertEqual(len(researched), 10)
        self.assertEqual(
            {(r["claim_id"], r["evidence_id"]) for r in researched},
            {(r["claim_id"], r["evidence_id"]) for r in candidates},
        )
        self.assertEqual(sum(r["source_assessment"] == "useful" for r in researched), 9)
        self.assertEqual(sum(r["source_assessment"] == "context_only" for r in researched), 1)
        for r in researched:
            self.assertTrue(r["sources_checked"])
            self.assertTrue(all(s["url"] and s["depth"] for s in r["sources_checked"]))
            self.assertFalse(r["research_provenance"]["human_confirmed"])
            self.assertFalse(r["research_provenance"]["rankings_or_model_labels_consulted"])
            self.assertTrue(r["original_human_review_not_overwritten"])
        self.assertFalse(ready)
        self.assertEqual(sum(r["decision"] == "useful" for r in reviews), 9)
        self.assertEqual(sum(r["decision"] == "context_only" for r in reviews), 1)
        self.assertTrue(all(r["reviewer"] == "Alex Karadjov" for r in reviews))
        self.assertTrue(all(r["saw_rankings_or_assistant_labels"] is True for r in reviews))
        self.assertTrue(all(r["review_status"] == "completed_assisted_not_blinded" for r in reviews))
        self.assertTrue(all(r["review_provenance"]["prior_review"]["decision"] == "unresolved" for r in reviews))

    def test_freeze_detects_changed_input(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "frozen").write_text("altered")
            (root / "manifest.json").write_text(json.dumps({"sha256": {"frozen": "wrong"}}))
            with patch.object(pilot, "ROOT", root), patch.object(pilot, "FOLDER", root):
                with self.assertRaisesRegex(ValueError, "Frozen input changed"):
                    pilot.check()

    def test_review_exposure_and_unresolved_block_scoring(self):
        _, candidates, reviews, _ = pilot.check()
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "manifest.json").write_text(json.dumps({"sha256": {}}))
            (root / "candidates.jsonl").write_text("".join(json.dumps(r) + "\n" for r in candidates))
            ready = copy.deepcopy(reviews)
            for r in ready:
                r.update(
                    decision="context_only",
                    reviewer="Synthetic test",
                    reviewed_on="2026-11-04",
                    rationale="Synthetic test only",
                    sources_checked=[{"url": "https://example.org", "depth": "test"}],
                    saw_rankings_or_assistant_labels=False,
                    previously_reviewed_this_pair=False,
                )

            def save():
                (root / "reviews.jsonl").write_text("".join(json.dumps(r) + "\n" for r in ready))

            with patch.object(pilot, "FOLDER", root):
                save()
                self.assertTrue(pilot.check()[3])
                ready[0]["saw_rankings_or_assistant_labels"] = True
                save()
                self.assertFalse(pilot.check()[3])
                ready[0]["saw_rankings_or_assistant_labels"] = False
                ready[0]["decision"] = "unresolved"
                save()
                self.assertFalse(pilot.check()[3])
