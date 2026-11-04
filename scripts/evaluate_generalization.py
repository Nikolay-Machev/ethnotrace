"""Frozen new-paper pilot. Validate first; reveal ranks only after complete blind review."""
import argparse
import hashlib
import json
from retrieve import Baseline, ROOT, rows
from semantic_retrieval import snapshot
from evaluate_semantic import metrics

FOLDER = ROOT / "data/generalization"


def check():
    manifest = json.loads((FOLDER / "manifest.json").read_text())
    for name, expected in manifest["sha256"].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Frozen input changed: " + name + ". Create a new pilot version.")
    candidates = rows(FOLDER / "candidates.jsonl")
    reviews = rows(FOLDER / "reviews.jsonl")
    keys = {(r["claim_id"], r["evidence_id"]) for r in candidates}
    review_keys = [(r["claim_id"], r["evidence_id"]) for r in reviews]
    if len(keys) != len(candidates) or len(set(review_keys)) != len(reviews) or set(review_keys) != keys:
        raise ValueError("Pilot candidates and review keys must match exactly without duplicates.")
    complete = []
    for r in reviews:
        if r["decision"] not in (None, "useful", "context_only", "unresolved"):
            raise ValueError("Invalid decision")
        complete.append(
            r["decision"] in ("useful", "context_only")
            and bool(r["reviewer"]) and bool(r["reviewed_on"]) and bool(r["rationale"])
            and bool(r["sources_checked"])
            and all(s.get("url") and s.get("depth") for s in r["sources_checked"])
            and r["saw_rankings_or_assistant_labels"] is False
            and r["previously_reviewed_this_pair"] is False
        )
    return manifest, candidates, reviews, all(complete)


def pilot_baseline(candidates):
    b = Baseline()
    b.claims = json.loads((FOLDER / "accounts.json").read_text())
    b.documents = {}
    b.experiments = {}
    b.paper_titles = {}
    for r in candidates:
        b.documents[r["evidence_id"]] = {
            "id": r["evidence_id"], "raw": r,
            "features": {
                "scientific_names": r["species"], "plant_parts": [],
                "extraction_solvents_explicit": [], "study_settings": [],
                "endpoint": None, "experimental_result_direction": None,
            },
        }
    return b


def run(encoder):
    manifest, candidates, reviews, ready = check()
    if not ready:
        raise ValueError("Rankings withheld: all ten pairs need complete source-based review without prior ranking/label exposure.")
    b = pilot_baseline(candidates)
    frozen = snapshot(b, encoder, manifest["model_revision"], {})
    output = {"pilot_id": manifest["pilot_id"], "scope": manifest["scope"],
              "review_sha256": hashlib.sha256((FOLDER / "reviews.jsonl").read_bytes()).hexdigest(),
              "queries": [], "limitations": manifest["limitations"]}
    for tid, rankings in frozen["rankings"].items():
        relevant = {r["evidence_id"] for r in reviews if r["claim_id"] == tid and r["decision"] == "useful"}
        output["queries"].append({
            "claim_id": tid, "candidate_count": len(rankings["lexical"]),
            "useful_count": len(relevant),
            "methods": {m: {**metrics(rankings[m], relevant), "ranked_ids": rankings[m],
                            "precision_at_3": len(set(rankings[m][:3]) & relevant) / 3,
                            "recall_at_3": len(set(rankings[m][:3]) & relevant) / len(relevant) if relevant else None}
                        for m in ("lexical", "semantic", "hybrid")},
        })
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score", action="store_true", help="Reveal ranks only after complete review.")
    args = parser.parse_args()
    manifest, candidates, reviews, ready = check()
    if not args.score:
        print(json.dumps({"pilot_id": manifest["pilot_id"], "candidates": len(candidates),
                          "ready": ready, "rankings_revealed": False,
                          "status": "Ready for scoring" if ready else "Awaiting complete human review"}, indent=2))
    else:
        if not ready:
            raise SystemExit("Review incomplete or exposed. Rankings remain withheld.")
        from sentence_transformers import SentenceTransformer
        import torch
        torch.set_num_threads(2)
        torch.manual_seed(0)
        model = SentenceTransformer(manifest["model"], revision=manifest["model_revision"],
                                    device="cpu", trust_remote_code=False)
        model.max_seq_length = 256
        target = FOLDER / "results.json"
        target.write_text(json.dumps(run(model), indent=2) + "\n")
        print("Wrote separate pilot results to", target)
