"""Compare three rankers on identical candidate pools; never treat unjudged leads as negatives."""

import json
from collections import defaultdict
from retrieve import Baseline, ROOT, rows
from semantic_retrieval import load_snapshot

METHODS = ("lexical", "semantic", "hybrid")


def metrics(order, relevant):
    if not relevant:
        return {"recall_at_5": None, "reciprocal_rank": None}
    return {
        "recall_at_5": len(set(order[:5]) & relevant) / len(relevant),
        "reciprocal_rank": next(
            (1 / (i + 1) for i, e in enumerate(order) if e in relevant), 0
        ),
    }


def evaluate():
    b = Baseline()
    cache = load_snapshot(b)
    if cache is None:
        return None
    truth = defaultdict(set)
    for r in rows(ROOT / "data/evaluation/development_expectations.jsonl"):
        if r["expected_retrieval_membership"]:
            truth[r["traditional_record_id"]].add(r["evidence_id"])
    details = []
    judged = []
    reviews = {
        (r["claim_id"], r["evidence_id"]): r
        for r in rows(ROOT / "data/review/retrieval_relevance.jsonl")
    }
    for tid, relevant in sorted(truth.items()):
        ranked = cache["rankings"][tid]
        details.append(
            {
                "claim_id": tid,
                "seeded_links": sorted(relevant),
                "methods": {
                    m: {
                        **metrics(ranked[m], relevant),
                        "ranked_ids": ranked[m],
                        "missed_at_5": sorted(relevant - set(ranked[m][:5])),
                    }
                    for m in METHODS
                },
            }
        )
        records = [reviews.get((tid, e), {}) for e in ranked["lexical"]]
        if records and all(
            r.get("human_review_status") == "completed"
            and type(r.get("human_retrieval_relevant")) is bool
            and r.get("human_reviewer_id")
            and r.get("human_rationale")
            and r.get("source_checked") is True
            for r in records
        ):
            positives = {
                r["evidence_id"] for r in records if r["human_retrieval_relevant"]
            }
            judged.append(
                {
                    "claim_id": tid,
                    "methods": {m: metrics(ranked[m], positives) for m in METHODS},
                }
            )

    def aggregate(records):
        return {
            m: {
                key: sum(vals) / len(vals) if vals else None
                for key in ("recall_at_5", "reciprocal_rank")
                for vals in [
                    [
                        r["methods"][m][key]
                        for r in records
                        if r["methods"][m][key] is not None
                    ]
                ]
            }
            for m in METHODS
        }

    return {
        "model": cache["model"],
        "revision": cache["revision"],
        "input_sha256": cache["input_sha256"],
        "scope": "Same six seeded development queries and candidate pools; not held-out; no model fitting or hyperparameter tuning.",
        "seeded_development": aggregate(details),
        "queries": details,
        "human_reviewed_development": {
            "complete_query_count": len(judged),
            "metrics": aggregate(judged),
            "queries": judged,
        },
        "notes": [
            "Unjudged candidates are not negatives.",
            "Human-reviewed development is not independent held-out evaluation.",
            "Similarity is not preparation equivalence, medical endpoint equivalence or efficacy.",
            "Lexical remains the default; no ranker is adopted on seeded metrics alone.",
        ],
    }


if __name__ == "__main__":
    result = evaluate()
    if result is None:
        raise SystemExit("Run semantic_retrieval.py first.")
    (ROOT / "data/evaluation/semantic_comparison.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                k: result[k]
                for k in ("seeded_development", "human_reviewed_development")
            },
            indent=2,
        )
    )
