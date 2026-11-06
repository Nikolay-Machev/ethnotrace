"""Current development evaluation with reviewer reconciliation.

evaluate_semantic.py is retained byte-for-byte for the frozen pilot.
"""

import json
from collections import defaultdict
from math import fsum
from review_progress import grouped_review_records
from retrieve import Baseline, ROOT, rows
from semantic_retrieval import load_snapshot

METHODS = ("lexical", "semantic", "hybrid")


def metrics(order, relevant):
    hits = len(set(order[:5]) & relevant)
    return {
        "precision_at_5": hits / 5,
        "recall_at_5": hits / len(relevant) if relevant else None,
        "reciprocal_rank": next((1 / (i + 1) for i, e in enumerate(order) if e in relevant), 0) if relevant else None,
    }


def completed(record):
    return (
        record.get("human_review_status") == "completed"
        and type(record.get("human_retrieval_relevant")) is bool
        and bool(record.get("human_reviewer_id"))
        and bool(record.get("human_rationale"))
        and record.get("source_checked") is True
    )


def human_comparison(rankings, reviews):
    judged, excluded = [], []
    for tid, ranked in sorted(rankings.items()):
        pool = ranked["lexical"]
        if not pool:
            continue
        blocked = [eid for eid in pool if not completed(reviews.get((tid, eid), {}))]
        if blocked:
            excluded.append(
                {
                    "claim_id": tid,
                    "candidate_count": len(pool),
                    "blocking_candidates": [
                        {
                            "evidence_id": eid,
                            "status": reviews.get((tid, eid), {}).get("human_review_status", "missing"),
                        }
                        for eid in blocked
                    ],
                }
            )
            continue
        positives = {eid for eid in pool if reviews[(tid, eid)]["human_retrieval_relevant"]}
        movements = []
        for eid in sorted(positives):
            positions = {m: ranked[m].index(eid) + 1 for m in METHODS}
            review = reviews[(tid, eid)]
            movements.append(
                {
                    "evidence_id": eid,
                    "ranks": positions,
                    "movement_vs_lexical": {m: positions["lexical"] - positions[m] for m in METHODS if m != "lexical"},
                    "top_five": {m: positions[m] <= 5 for m in METHODS},
                    "human_rationale": review["human_rationale"],
                    "source": review.get("source", {}),
                    "sources_checked": review.get("human_review_details", {}).get("sources_checked", []),
                }
            )
        judged.append(
            {
                "claim_id": tid,
                "candidate_count": len(pool),
                "useful_count": len(positives),
                "relevant_ids": sorted(positives),
                "methods": {
                    m: {
                        **metrics(ranked[m], positives),
                        "ranked_ids": ranked[m],
                        "hits_at_5": len(set(ranked[m][:5]) & positives),
                        "missed_at_5": sorted(positives - set(ranked[m][:5])),
                    }
                    for m in METHODS
                },
                "useful_movements": movements,
            }
        )
    return judged, excluded


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
    reviews, reconciliation = grouped_review_records(rows(ROOT / "data/review/retrieval_relevance.jsonl"))
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
    judged, excluded = human_comparison(cache["rankings"], reviews)

    def aggregate(records):
        return {
            m: {
                key: fsum(vals) / len(vals) if vals else None
                for key in ("precision_at_5", "recall_at_5", "reciprocal_rank")
                for vals in [[r["methods"][m][key] for r in records if r["methods"][m][key] is not None]]
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
            "reviewer_reconciliation": reconciliation,
            "complete_query_count": len(judged),
            "candidate_count": sum(q["candidate_count"] for q in judged),
            "useful_count": sum(q["useful_count"] for q in judged),
            "excluded_queries": excluded,
            "metric_definitions": {
                "precision_at_5": "Useful results in the first five divided by five; unfilled slots count as zero.",
                "recall_at_5": "Useful results in the first five divided by all useful candidates in the indexed pool.",
                "aggregation": "Macro average: equal weight per complete account. Recall and reciprocal rank are undefined for accounts without useful candidates.",
                "movement": "Positive movement means a useful candidate moved up relative to lexical ranking.",
            },
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


def write_report(result):
    human = result["human_reviewed_development"]
    lines = [
        "# Human-reviewed retrieval comparison",
        "",
        "Generated, do not edit. Run python scripts/rebuild.py.",
        "",
        f"{human['complete_query_count']} complete accounts; "
        f"{human['candidate_count']} account–candidate pairs; "
        f"{human['useful_count']} judged useful.",
        "",
        "Assisted development review, not a held-out test. Source depth varies. "
        "A useful study need not support the traditional claim.",
        "",
        "Precision@5 uses five slots, including unfilled slots for short pools. "
        "Recall@5 uses all judged-useful candidates in the indexed pool. "
        "Metrics are macro averages with equal weight per complete account.",
        "",
        "| Method | Precision@5 | Recall@5 | MRR |",
        "| --- | ---: | ---: | ---: |",
    ]
    fmt = lambda value: "N/A" if value is None else f"{value:.3f}"
    for method, values in human["metrics"].items():
        lines.append(
            f"| {method} | {fmt(values['precision_at_5'])} | "
            f"{fmt(values['recall_at_5'])} | {fmt(values['reciprocal_rank'])} |"
        )
    for query in human["queries"]:
        lines.extend(
            [
                "",
                f"## {query['claim_id']}",
                "",
                f"{query['useful_count']} useful of {query['candidate_count']} candidates.",
                "",
                "| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |",
                "| --- | ---: | ---: | ---: | --- |",
            ]
        )
        for method, values in query["methods"].items():
            lines.append(
                f"| {method} | {values['hits_at_5']} | "
                f"{fmt(values['precision_at_5'])} | {fmt(values['recall_at_5'])} | "
                f"{', '.join(values['missed_at_5']) or 'None'} |"
            )
        lines.extend(
            [
                "",
                "| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |",
                "| --- | ---: | ---: | ---: |",
            ]
        )
        for item in query["useful_movements"]:
            ranks, delta = item["ranks"], item["movement_vs_lexical"]
            lines.append(
                f"| {item['evidence_id']} | {ranks['lexical']} | "
                f"{ranks['semantic']} ({delta['semantic']:+d}) | "
                f"{ranks['hybrid']} ({delta['hybrid']:+d}) |"
            )
        lines.extend(["", "Positive change means moving up relative to lexical ranking.", ""])
        for item in query["useful_movements"]:
            source = item["source"]
            lines.extend(
                [
                    f"### {item['evidence_id']}",
                    "",
                    item["human_rationale"],
                    "",
                    source.get("citation", ""),
                    source.get("url", ""),
                    "",
                ]
            )
            for checked in item["sources_checked"]:
                lines.append(f"- {checked['depth']}: {checked['url']}")
            lines.append("")
    lines.extend(
        [
            "## Exclusions",
            "",
            "Entire accounts are excluded when any candidate lacks a confirmed decision. "
            "Provisional, unresolved and missing decisions are not treated as negatives.",
            "",
        ]
    )
    for query in human["excluded_queries"]:
        blockers = ", ".join(f"{r['evidence_id']} ({r['status']})" for r in query["blocking_candidates"])
        lines.append(f"- {query['claim_id']}: {blockers}.")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "These results describe the frozen rankers on the existing development corpus. "
            "Small candidate pools and repeated papers across accounts limit interpretation. "
            "No significance or generalization claim is made. Lexical remains the default. "
            "Rank changes do not alter experimental findings or comparability judgments.",
            "",
            f"Model: {result['model']}; revision: {result['revision']}.",
            f"Ranking-input SHA-256: {result['input_sha256']}.",
            "",
        ]
    )
    (ROOT / "docs/human_retrieval_comparison.md").write_text("\n".join(lines), encoding='utf-8', newline='\n')


if __name__ == "__main__":
    result = evaluate()
    if result is None:
        raise SystemExit("Run semantic_retrieval.py first.")
    (ROOT / "data/evaluation/semantic_comparison.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding='utf-8', newline='\n'
    )
    write_report(result)
    print(
        json.dumps(
            {k: result[k] for k in ("seeded_development", "human_reviewed_development")},
            indent=2,
        )
    )
