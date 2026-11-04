# Remaining source reviews

## Retrieval relevance

Read [the 33-candidate packet](retrieval_review_packet.md), then enter answers in `data/review/retrieval_relevance.jsonl`. Every candidate needs a decision for a query to support a complete retrieval evaluation. Negative results and explicit mismatches may still be useful evidence. Source access problems should leave a decision unresolved, not force it to false.

For a completed entry, supply all five human fields:

```json
{
  "human_retrieval_relevant": true,
  "human_rationale": "Your reason, with the source section you checked",
  "human_reviewer_id": "Your reviewer identifier",
  "source_checked": true,
  "human_review_status": "completed"
}
```

This is an example of the required shape, not a decision for any candidate. Retain the claim/evidence IDs and source information already present in each entry.

## Partner comparison review

Use the existing [comparison packets](review_cases.md) and `data/review/reviewer_b.jsonl`. Check the documented use narrowly against species, part, preparation, measured outcome and setting. Enter the comparison label and rationale under the existing schema, keep its compatibility fields consistent, and record whether assistant judgments were seen. Do not claim blind independence after seeing proposed answers. Extraction agreement alone does not complete comparison review. Preserve disagreements for adjudication.

## Targeted extraction review

`data/curated/targeted_extractions.jsonl` has two source notes. TX001 is a methods/table extraction from a phytochemical comparison; check PDF pages 3 and 5. TX002 is partial indexed-section extraction; full methods, figures, dose and plant part require inspection. Neither inherits the earlier human reviews. Both remain outside the 12-unit experimental index and the frozen 20-case comparison set. They are shown as context in the app, not additional efficacy results.

Run:

```bash
python scripts/review_progress.py
python scripts/evaluate.py
python scripts/build_demo.py
```

The first command validates relevance completion fields. The evaluator validates comparison schema and retains its independent-review safeguards. No human decision or adjudication is inferred from this preparation step. Semantic ranking is available experimentally. Complete candidate relevance judgments before claiming it improves retrieval; rerun `python scripts/evaluate_semantic.py` and `python scripts/build_evaluation.py` after recording reviews.

## T008 human submission, 4 November 2026

Nikolay Machev source-checked all six candidates after seeing the assistant screen. Four were useful (P26626246, P22738356, E003, E004). Two initially unresolved safety studies (P21186373, P26626249) were resolved as not retrieval-relevant to T008 under the reviewer-approved scope rule. They remain indexed as safety context. Earlier reasoning and source depths are preserved.

**Rule for all accounts:** count a candidate as useful if it helps assess the documented use through a relevant outcome or a direct comparison of plant parts or preparations. A safety-only study that does neither is context; a part match alone is insufficient. Keep unresolved cases pending when the source does not permit a decision. Relevance is distinct from a finding supporting the traditional use.

## Remaining batch, 4 November 2026

All 27 remaining pairs have reviewer submissions. Three need additional evidence before a decision: T007/P18066122 (species-specific part or preparation comparison?), T010/P20301057 (poplar outcomes or direct preparation comparison in the target article?), and T011/P19526043 (lingonberry-specific arm, material and outcome?). Preserve source depth: some checks used summaries or secondary material rather than the candidate paper itself. E012 compares experimental solvents; the traditional T011 preparation remains undocumented. No finding in a human rationale changes an experimental extraction automatically.
