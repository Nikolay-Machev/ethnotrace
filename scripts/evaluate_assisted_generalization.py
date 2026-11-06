"""Separate assisted-label evaluation of frozen new-paper rankers.

Preserves the frozen blinded protocol and input checks; never represents
assistant-exposed review labels as blinded human adjudication.
"""

import argparse
import hashlib
import json

import evaluate_generalization as frozen
from semantic_retrieval import snapshot
from evaluate_semantic import metrics

OUTPUT = frozen.FOLDER / "assisted_exploratory_results.json"
METHODS = ("lexical", "semantic", "hybrid")


def check_assisted_reviews():
    manifest, candidates, reviews, independently_eligible = frozen.check()
    if independently_eligible:
        raise ValueError("Use the frozen blinded evaluator for independently eligible reviews.")
    if len(reviews) != 10 or any(
        r.get("reviewer") != "Alex Karadjov"
        or r.get("review_status") != "completed_assisted_not_blinded"
        or r.get("decision") not in ("useful", "context_only")
        or r.get("saw_rankings_or_assistant_labels") is not True
        or r.get("review_provenance", {}).get("eligible_for_frozen_blinded_scoring") is not False
        for r in reviews
    ):
        raise ValueError("Expected all ten disclosed assisted reviews. No scores produced.")
    return manifest, candidates, reviews


def evaluate(encoder):
    manifest, candidates, reviews = check_assisted_reviews()
    b = frozen.pilot_baseline(candidates)
    ranked = snapshot(b, encoder, manifest["model_revision"], {})
    queries = []
    for tid in sorted(ranked["rankings"]):
        orders = ranked["rankings"][tid]
        relevant = {r["evidence_id"] for r in reviews if r["claim_id"] == tid and r["decision"] == "useful"}
        query = {
            "claim_id": tid,
            "candidate_count": len(orders["lexical"]),
            "useful_count": len(relevant),
            "methods": {},
        }
        for name in METHODS:
            order = orders[name]
            if len(order) != len(set(order)):
                raise ValueError("Duplicate candidate in frozen order")
            values = metrics(order, relevant)
            values["precision_at_3"] = len(set(order[:3]) & relevant) / 3
            values["recall_at_3"] = len(set(order[:3]) & relevant) / len(relevant) if relevant else None
            values["ranked_ids"] = order
            query["methods"][name] = values
        queries.append(query)

    aggregates = {}
    for name in METHODS:
        aggregates[name] = {}
        for key in ("precision_at_5", "recall_at_5", "reciprocal_rank", "precision_at_3", "recall_at_3"):
            vals = [q["methods"][name][key] for q in queries if q["methods"][name][key] is not None]
            aggregates[name][key] = sum(vals) / len(vals) if vals else None

    return {
        "pilot_id": manifest["pilot_id"],
        "evaluation_track": "assisted_exploratory_not_independent_blinded",
        "model": manifest["model"],
        "model_revision": manifest["model_revision"],
        "rrf_k": manifest["rrf_k"],
        "reference_evaluator_unchanged": True,
        "frozen_manifest_sha256": hashlib.sha256((frozen.FOLDER / "manifest.json").read_bytes()).hexdigest(),
        "reviews_sha256": hashlib.sha256((frozen.FOLDER / "reviews.jsonl").read_bytes()).hexdigest(),
        "reviewer": "Alex Karadjov",
        "assistant_prepared_labels_approved": True,
        "assistant_label_exposure": True,
        "independent_blinded_reviews": False,
        "no_fine_tuning_or_ranker_changes": True,
        "scope": "Two existing plant accounts, ten assistant-selected new papers; not new plant, new Nation, or population-wide generalization.",
        "limitations": manifest["limitations"]
        + [
            "Assistant-authored labels approved by named reviewer; not independent gold.",
            "Model rankings were not shown before the label approvals, but assistant relevance decisions were.",
            "Candidate pool is purposive and has nine of ten labelled useful; metrics are sensitive to class prevalence and top-k pool size.",
        ],
        "aggregates_macro": aggregates,
        "queries": queries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="Validate metadata and disclosed exposure without inference."
    )
    args = parser.parse_args()
    manifest, candidates, reviews = check_assisted_reviews()
    if args.check:
        print(
            json.dumps(
                {
                    "ready_for_assisted_exploratory_scoring": True,
                    "eligible_for_independent_blinded_scoring": False,
                    "candidates": len(candidates),
                    "useful": sum(r["decision"] == "useful" for r in reviews),
                }
            )
        )
        return
    from sentence_transformers import SentenceTransformer
    import torch

    torch.set_num_threads(2)
    torch.manual_seed(0)
    encoder = SentenceTransformer(
        manifest["model"], revision=manifest["model_revision"], device="cpu", trust_remote_code=False
    )
    encoder.max_seq_length = 256
    result = evaluate(encoder)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding='utf-8', newline='\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
