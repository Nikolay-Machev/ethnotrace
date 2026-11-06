# Remaining source reviews

## Five-pair primary-source follow-up, 5 November 2026

A new [source assessment ledger](../data/review/retrieval_relevance_source_followup_2026-11-05.jsonl) includes five evidence-based dispositions: T007/P18066122 true, T008/P21186373 false, T008/P26626249 false, T010/P20301057 true and T011/P19526043 true. The full original publications were located for Fraser (2007) and Harbilas (2009); primary author abstracts support the remaining cases. The two T008 negative judgments already match Nikolay's completed reviewer submissions. Each of the 10 corresponding canonical review rows now links its assistant source assessment without changing the original named human submission.

The remaining step for the named, two-reviewer retrieval metric is explicit human adoption or correction of any pending or provisional labels. Assistant source research must not be silently converted into human-reviewed completion. See [source follow-up evidence](relevance_followup.md).

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

`data/curated/targeted_extractions.jsonl` has two source notes. Alex Karadjov explicitly confirmed the source-specific TX001/TX002 verification packet on 5 November 2026. Both records now retain the checked sections, source-derived fields, precise corrections, limitations, and an explicit assistant-assisted verification provenance statement. Their `human_verified` and `human_review.source_checked` fields are true, while `training_eligible` remains false. TX002's plant part and the exact historical T008 recipe remain unresolved. TX001 is a methods/table extraction from a phytochemical comparison; check PDF pages 3 and 5. TX002 is partial indexed-section extraction; full methods, figures, dose and plant part require inspection. Neither inherits the earlier human reviews. Both remain outside the 12-unit experimental index and the frozen 20-case comparison set. They are shown as context in the app, not additional efficacy results.

Earlier notes documented partial source access and an unsupported general attestation. The later source-specific verification packet supplies precise Methods, tables, figure references, values and limitations, which Alex approved. The original attestation is preserved in the record history. Neither targeted extraction is promoted to the 12-unit experimental index or counted as a clinical result.

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
