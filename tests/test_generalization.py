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
            (root / "candidates.jsonl").write_text("".join(json.dumps(r)+"\n" for r in candidates))
            ready = copy.deepcopy(reviews)
            for r in ready:
                r.update(decision="context_only", reviewer="Synthetic test", reviewed_on="2026-11-04",
                         rationale="Synthetic test only", sources_checked=[{"url":"https://example.org","depth":"test"}],
                         saw_rankings_or_assistant_labels=False, previously_reviewed_this_pair=False)
            def save():
                (root / "reviews.jsonl").write_text("".join(json.dumps(r)+"\n" for r in ready))
            with patch.object(pilot, "FOLDER", root):
                save();self.assertTrue(pilot.check()[3])
                ready[0]["saw_rankings_or_assistant_labels"]=True
                save();self.assertFalse(pilot.check()[3])
                ready[0]["saw_rankings_or_assistant_labels"]=False
                ready[0]["decision"]="unresolved"
                save();self.assertFalse(pilot.check()[3])
