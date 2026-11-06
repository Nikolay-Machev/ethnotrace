# Handling unresolved retrieval-relevance candidates

This note documents how to preserve uncertainty in `data/review/retrieval_relevance.jsonl`. It does not create new source judgments or change the candidate records. A candidate is not a negative merely because the source could not be inspected sufficiently.

## Current decisions

All 33 candidate pairs now have completed matching assisted decisions from both reviewers (66 submissions). The earlier unresolved T007/P18066122 and T011/P19526043 decisions and provisional T010/P20301057 decision were resolved through approved source follow-ups. Their earlier states are preserved in `data/review/history/retrieval_relevance_history.jsonl`. Scientific limitations remain in the current source checks and explanations; completion does not imply independent primary-source verification.

For future reviews, unresolved and provisional submissions remain excluded from complete-query metrics. They must not be converted to negatives. If either reviewer is pending, the query is excluded; conflicting completed decisions require adjudication.

## JSONL shapes

Keep `claim_id`, `evidence_id`, the named reviewer and source-check provenance. Full source and account context is resolved from indexed records; do not copy it or nested history back into the current review file. These are examples of status handling, not new judgments; preserve the actual existing reason and provenance when editing an entry.

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

See [the reviewer follow-up](archive/relevance_followup.md), [historical review instructions](archive/next_reviews.md), and [review workflow](review_workflow.md) for case context and criteria.
