# Handling unresolved retrieval-relevance candidates

This note documents how to preserve uncertainty in `data/review/retrieval_relevance.jsonl`. It does not create new source judgments or change the candidate records. A candidate is not a negative merely because the source could not be inspected sufficiently.

## Remaining non-confirmed decisions

The existing reviewer follow-up identifies these cases as unresolved because species-specific or assay-mapped evidence was not verified from the primary source:

- **T007 / P18066122** — the available abstract summary did not establish the species-specific results; leave unresolved unless the relevant source table or text is checked.
- **T011 / P19526043** — the available summary did not map assays to lingonberry; leave unresolved unless a source supports a defensible decision.

**T010 / P20301057** remains **provisional**. The reviewer considered adipogenesis relevant to the scope, but the primary source was not fully checked; the decision must not be counted as confirmed.

These statuses are excluded from confirmed retrieval metrics. The evaluator counts a decision as complete only when `human_review_status` is `completed`, relevance is explicitly boolean, a reviewer and rationale are recorded, and `source_checked` is true. Unresolved and provisional entries are not converted to false or treated as negatives.

## JSONL shapes

Keep the original `claim_id`, `evidence_id`, rank, source metadata, and other packet fields. These are examples of status handling, not new judgments; preserve the actual existing reason and provenance when editing an entry.

Unresolved (no defensible true/false decision):

```json
{
  "human_review_status": "unresolved",
  "human_retrieval_relevant": null,
  "human_rationale": "Unresolved: the available source material did not establish the candidate's account-specific result. Do not infer a negative.",
  "human_reviewer_id": "<reviewer identifier>",
  "source_checked": false
}
```

Provisional (a tentative interpretation exists, but primary-source verification is incomplete):

```json
{
  "human_review_status": "provisional",
  "human_retrieval_relevant": null,
  "human_provisional_retrieval_relevant": true,
  "human_rationale": "Provisional only: explain the tentative relevance and identify what source evidence remains unchecked.",
  "human_reviewer_id": "<reviewer identifier>",
  "source_checked": false
}
```

Only after source inspection supports a defensible decision should an entry become `completed`, with `human_retrieval_relevant` set to `true` or `false`, a source-based rationale, reviewer identifier, `source_checked: true`, and the actual source sections/tables recorded in the existing review-details fields. A completed judgment means relevant to assessing the documented use, not that the study supports the traditional claim.

## Validation and reporting

Run `python scripts/review_progress.py` and the review/evaluation tests after updating review records. Regenerate reports with `python3 scripts/rebuild.py`. Do not describe provisional or unresolved entries as completed, and do not claim independent or held-out accuracy from assisted development reviews.

See [the reviewer follow-up](archive/relevance_followup.md), [remaining source reviews](archive/next_reviews.md), and [review workflow](review_workflow.md) for case context and criteria.
