# Retrieval error analysis

Six development queries have 12 seeded experimental links. These links are useful for regression checks, but are not a complete independently judged relevance set. Eight constructed species mismatches are excluded from these query-level recovery metrics.

| Measure | Baseline 1.0 | Baseline 1.1 |
| --- | ---: | ---: |
| Macro recall at 5, seeded links | 0.667 | 0.917 |
| Mean reciprocal rank, seeded links | 0.408 | 0.561 |

These figures describe the combined ranked list before UI grouping. They are not clinical accuracy, held-out performance or proof of better relevance across all papers. The change was selected after inspecting this development set. Candidate pools hold four to seven items, so the expected scores under uniform random ordering of the same pools are macro recall at five 0.869 and MRR 0.595; version 1.1's MRR of 0.561 is below that level.

## Failure analysis

- Tamarack E002 ranked sixth: four literature titles matched contextual words, while the extracted endpoint had no token overlap. E001 ranked fifth.
- Pitcher-plant E004 ranked sixth: roots differ from the traditional leaf account, so the plant-part penalty pushed it below other candidates. This is a useful mismatch to inspect, not necessarily a ranking mistake.
- Labrador-tea E010 ranked sixth: five publication titles contained traditional-use context unavailable in the extracted endpoint text.

Version 1.0 compared full titles for literature leads against short endpoints for extracted units. Version 1.1 uses the maximum query overlap with the endpoint or parent publication title. This gives both document types access to title context without double-counting the title and endpoint, changing species eligibility, adding a positive-result bonus or reading reviewer labels. Preparation and outcome comparability rules are unchanged.

E004 remains outside the top five. Its part mismatch is explicitly explained. Recovering every seed is not sufficient reason to remove a meaningful mismatch penalty.

## Presentation and relevance review

The UI separates extracted experiments and literature leads and preserves baseline order inside each group. This is a completeness grouping, not a scientific quality hierarchy. It must not be reported as an improvement in the combined ranking metric.

`data/review/retrieval_relevance.jsonl` covers all 33 same-species candidates across the six queries, with citations and source URLs. The 12 extracted candidates and two publications that received targeted source inspection (P23864882, P26626246) have provisional assistant judgments of useful evidence, including null findings and mismatches. The other 19 publications remain undecided pending source assessment. A separate assistant screen of all 33 pairs is in `data/review/assistant_relevance_screen.jsonl` (see `retrieval_screen_notes.md`). No new full-text review is claimed.

T008 has four completed human relevance decisions and two source-checked unresolved candidates; 27 candidates elsewhere still await human review. Review whether each entry helps assess the account, separately from whether it supports the claim. Record a boolean in `human_retrieval_relevant`, a reason in `human_rationale`, and completion in `human_review_status`. This queue is a review artifact; independent retrieval metrics remain unavailable until completed judgments are integrated into evaluation. The script preserves human fields on rerun.

Reviewer B's comparison judgments remain pending. No agreement or adjudication was fabricated.

Reproduce with `python scripts/analyze_retrieval.py`. Full ranks are in `data/evaluation/retrieval_comparison.json`.
