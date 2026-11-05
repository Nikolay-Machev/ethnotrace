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

A reviewer submission on 5 November 2026 records that TX001 pages 3 and 5 and TX002's full methods/figures could not be directly checked. No extraction fields were verified, and corrections could not be determined. Both notes remain explicitly unverified (`human_verified: false`); do not describe them as source-verified or use them as additional efficacy results until the sources can be inspected.


A subsequent 5 November 2026 attestation from Alex Karadjov reports that both targeted extractions were verified. The referenced uploaded document contains T008/P26626246 and T007/P23864882 relevance reviews but no TX001/TX002 source-verification checklist or completed verification of the specific missing methods and figures. The attestation is recorded under each extraction's `human_review.reviewer_attestation`. The source-level `human_verified` fields remain `false` until the exact checked sections, verified fields and any corrections are documented. This preserves the distinction between a reviewer-reported completion and evidenced extraction verification.

## Human retrieval submissions received 5 November 2026

The 27 case-level decisions supplied by Nikolay Machev are preserved in `data/review/retrieval_relevance_human_submissions.jsonl`, including rationale, checked-source notes, and assistant-screen exposure declarations. This is a submission ledger, not yet imported into the canonical 33-candidate queue: entries based only on summaries/secondary sources retain those access limitations, and three cases remain unresolved (T007/P18066122, T010/P20301057, T011/P19526043). Do not use the ledger as a completed retrieval evaluation until its decisions are reconciled into the canonical review file and validation is rerun. Reviews were not blind because assistant-screen exposure was reported for many cases.

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

All 27 remaining pairs have reviewer submissions. T010/P20301057 is provisionally useful under the reviewer’s adipogenesis scope reading, based on assistant-reported primary findings and a reviewer’s acknowledged prior pair review. T011/P19927274 remains unresolved pending accessible source text. T012/P26707751 remains unresolved pending inspection of adipogenic results. T008/P33144625, P38943782, P27174081 and P35807620 remain unreviewed after direct access failed. No source result was copied from an assistant screen into the human fields. See [source follow-up and reviewer decisions](relevance_followup.md) for source depths and remaining questions. Experimental extractions and claim-comparability labels are unchanged.
