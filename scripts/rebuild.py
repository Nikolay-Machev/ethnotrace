"""Offline rebuild. Review files are read as inputs, never published as outputs."""
import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = (
    "docs/retrieval_review_packet.md",
    "docs/reports/T008-evidence.md",
    "web/data.js",
    "web/evaluation-data.js",
    "data/evaluation/baseline_report.json",
    "data/evaluation/baseline_predictions.jsonl",
    "data/evaluation/retrieval_comparison.json",
    "data/evaluation/semantic_comparison.json",
)


def rebuild(check=False):
    with tempfile.TemporaryDirectory() as directory:
        stage = Path(directory)
        for folder in ("imports", "config", "scripts", "data/review", "data/curated"):
            shutil.copytree(ROOT / folder, stage / folder, ignore=shutil.ignore_patterns("__pycache__"))
        for file in ("web/report.js", "data/evaluation/development_expectations.jsonl",
                     "data/evaluation/semantic_rankings.json"):
            (stage / file).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / file, stage / file)
        (stage / "docs").mkdir()
        # Both packet and ranking builders can enrich the queue. Evaluate the
        # checked-in review bytes, not their temporary reserialization.
        queue = stage / "data/review/retrieval_relevance.jsonl"
        original = queue.read_bytes()
        for script in ("preprocess", "analyze_retrieval", "prepare_relevance_review",
                       "evaluate", "evaluate_semantic", "build_demo", "build_evaluation"):
            if script == "evaluate":
                queue.write_bytes(original)
            subprocess.run([sys.executable, f"scripts/{script}.py"], cwd=stage,
                           check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["node", "scripts/render_example.cjs"], cwd=stage, check=True)
        produced = {p.relative_to(stage) for p in (stage / "data/processed").iterdir()}
        existing = {p.relative_to(ROOT) for p in (ROOT / "data/processed").iterdir() if p.is_file()}
        if existing - produced:
            raise SystemExit(f"Obsolete processed outputs; inspect before removing: {sorted(existing-produced)}")
        changed = []
        for file in sorted(produced | set(map(Path, OUTPUTS))):
            target = ROOT / file
            new = (stage / file).read_bytes()
            if not target.exists() or target.read_bytes() != new:
                changed.append(str(file))
                if not check:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(new)
        return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail on stale outputs without writing")
    args = parser.parse_args()
    changed = rebuild(args.check)
    if changed:
        print(("Stale" if args.check else "Updated") + ":\n" + "\n".join(changed))
        if args.check:
            raise SystemExit(1)
    else:
        print("Generated files are up to date.")
