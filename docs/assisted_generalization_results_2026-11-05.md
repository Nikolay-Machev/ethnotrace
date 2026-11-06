# Assisted exploratory new-paper ranker evaluation

Source: [successful GitHub Actions scoring run](https://github.com/Nikolay-Machev/makeathon-2026-ethnotrace-traditional-knowledge-mining/actions/runs/42146625815). Structured results: [assisted_exploratory_results.json](../data/generalization/assisted_exploratory_results.json).

The original ten-paper `new-papers-v1` frozen protocol and pinned ranking/model inputs were preserved byte-for-byte. The ten source-based relevance judgments were first prepared by an assistant and explicitly approved by Alex Karadjov before the ranker predictions were inspected. Accordingly, the reference `scripts/evaluate_generalization.py --score` gate **still rejects** these labels as non-blinded. A separate `scripts/evaluate_assisted_generalization.py` reports this result as **assisted exploratory**, not independently adjudicated generalization.

## Macro averages across two existing traditional accounts

| Method | Precision@5 | Recall@5 | MRR | Precision@3 | Recall@3 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Lexical | 0.800 | 0.900 | 1.000 | 0.833 | 0.575 |
| Semantic | 0.800 | 0.900 | 1.000 | 1.000 | 0.675 |
| Hybrid | 0.800 | 0.900 | 1.000 | 1.000 | 0.675 |

Precision@5 uses five slots, including unfilled slots for the four-candidate T008 pool. Recall@5 divides retrieved useful papers by all useful papers in the fixed candidate pool. Precision@3 uses three slots; recall@3 uses all useful papers. MRR is reciprocal rank of the first useful hit. These are equal-weight macro averages across T008 and T011.

## Per-account scores

| Account | Candidate pool | Useful | Ranker | P@5 | R@5 | P@3 | R@3 |
| --- | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| T008, pitcher plant | 4 | 4 | Lexical | 0.800 | 1.000 | 1.000 | 0.750 |
| T008, pitcher plant | 4 | 4 | Semantic | 0.800 | 1.000 | 1.000 | 0.750 |
| T008, pitcher plant | 4 | 4 | Hybrid | 0.800 | 1.000 | 1.000 | 0.750 |
| T011, lingonberry | 6 | 5 | Lexical | 0.800 | 0.800 | 0.667 | 0.400 |
| T011, lingonberry | 6 | 5 | Semantic | 0.800 | 0.800 | 1.000 | 0.600 |
| T011, lingonberry | 6 | 5 | Hybrid | 0.800 | 0.800 | 1.000 | 0.600 |

With T008 all four candidates assessed useful, none of these rankers is meaningfully distinguishable on precision or recall within that pool. For T011, semantic and hybrid rank three useful papers in the first three; lexical ranks two useful papers in the first three. All three rank four of the five useful papers in the first five, and all methods put a useful candidate first.

## Scope and limitations

- The ten candidates were assistant-selected, belong to only two existing traditional accounts and are highly enriched for useful labels (9/10). These results cannot be generalized to new plants, communities or an independently sampled paper collection.
- Alex approved assistant-prepared literature judgments. This is not a second independent paper review. The approving reviewer was exposed to assistant labels, though model rankings were not supplied before approval.
- Papers within the lingonberry and antiviral research groups may share researchers, participants or assays. They were not established as independent studies.
- Semantic model: `sentence-transformers/all-MiniLM-L6-v2`, fixed revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`; reciprocal rank fusion `k=60`. Frozen original scoring inputs: account descriptions versus publication species/title metadata; no retraining, tuning or preparation-based leakage.
- Original blinded evaluator remains unchanged. Do not use this exploratory report as independent proof of superiority, clinical efficacy, or held-out generalization.
- A truly blinded evaluation requires a separate human reviewer with no exposure to these assistant decisions or ranker predictions, under a versioned evaluation plan.

To reproduce the exploratory run:

```sh
python scripts/evaluate_assisted_generalization.py --check
python -m pip install -r requirements-semantic.txt
python scripts/evaluate_assisted_generalization.py
```

Source run: `42146625815`. The workflow uploaded the scored JSON as an artifact and produced no bot-authored Git commits.
