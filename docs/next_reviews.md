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

Nikolay Machev source-checked all six candidates after seeing the assistant screen. Four decisions are useful (P26626246, P22738356, E003, E004). Two source-checked safety candidates (P21186373, P26626249) remain unresolved; leaning against relevance is not a negative decision. Each entry retains the reviewer's reasoning, sources and inspection depth in the relevance file. No judgment about treatment efficacy or independent blinded review follows from these entries.

Before resolving the safety candidates, agree on a rule to apply consistently across accounts. One possible rule is to retain safety-only work as context when it neither measures the documented use nor directly compares a relevant plant part or preparation. This is a proposal for reviewers, not an adjudication.
