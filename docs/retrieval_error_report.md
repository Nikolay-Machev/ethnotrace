# Retrieval error analysis

Six development accounts have 12 seeded experimental links and 33 candidate pairs with complete matching assisted relevance judgments. Seeded-link recovery and human relevance are separate benchmarks. Eight constructed species mismatches are excluded from query-level recovery metrics.

| Seeded-link measure | Baseline 1.0 | Baseline 1.1 | Current 1.2 |
| --- | ---: | ---: | ---: |
| Macro recall@5 | 0.667 | 0.917 | 0.917 |
| Mean reciprocal rank | 0.408 | 0.561 | 0.561 |

Version 1.1 added parent-paper titles to the text available for extracted units, improving parity with literature leads. Version 1.2 removed the -2 plant-part mismatch penalty. E004 rises from score 8 to 10 but remains sixth of six for T008. Part overlap still contributes +2; the mismatch remains visible separately in the interface. Candidate order and metrics are unchanged by the 1.2 change.

Under uniformly random ordering of these short pools, expected seeded recall@5 is 0.869 and MRR is 0.595. The lexical MRR remains below that expectation. These changes were inspected on development data; they are not a held-out improvement claim.

## Current retrieval errors

For pitcher plant, lexical and hybrid ranking miss E004 at five; semantic ranking retrieves E004 but misses E003. Equal seeded recall therefore hides different omissions. The root experiment can be useful evidence of a part mismatch without directly testing the documented leaf use.

The interface groups extracted experiments and literature leads separately, retaining rank order within each group. Evaluation scores the complete ungrouped list. Display grouping is not a retrieval improvement.

## Human relevance results

All 33 candidate pairs have two matching completed assisted submissions: 25 useful and eight context-only pairs. No current pair remains unresolved or provisional. Source access limitations and assistant exposure remain documented; these are not independent gold labels.

| Ranker | Macro precision@5 | Macro recall@5 |
| --- | ---: | ---: |
| Lexical | 0.667 | 0.828 |
| Semantic | 0.733 | 0.889 |
| Hybrid | 0.733 | 0.903 |

See the generated [human retrieval comparison](human_retrieval_comparison.md) for per-account movements and source checks. Historical review decisions are retained separately from current records.

Reproduce the seeded comparison with `python scripts/analyze_retrieval.py`, or rebuild all current reports with `python scripts/rebuild.py`. Scores and full ranks are in `data/evaluation/retrieval_comparison.json` and `data/evaluation/semantic_comparison.json`.
