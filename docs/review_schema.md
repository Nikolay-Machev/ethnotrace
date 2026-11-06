# Review records, version 2

Both reviewer files use the same fields. The original extraction packets, source passages and citations remain in `review_cases.jsonl`, joined by `case_id`; reviewer A no longer duplicates those packets.

- `extraction_verified` and `corrections` record source-extraction checking. The provenance field distinguishes direct user reporting from the partner's verification reported by the user.
- `comparison_review_status` records whether the comparison judgment is complete. `status` is a compatibility alias.
- `claim_comparability` records the label, narrow interpretation of the documented use and rationale. `pair_label` is a compatibility alias and must match its label.
- `experimental_findings` records the result direction, endpoint, setting, reported result and source separately. An extraction confirmation does not automatically complete an independent direction-label review.
- `experimental_findings_review_status` tracks that separate step. Both current reviewer files have 20 `pending` entries for this separate finding-review step.
- `comparison_review_provenance` records whether judgments were made after seeing assistant labels. Unknown independence remains null; it must not be inferred from two reviewer IDs.
- `retrieval_relevant` is a case-level relevance judgment when explicitly supplied. Complete-query retrieval evaluation uses `human_retrieval_relevant` in `retrieval_relevance.jsonl`; it does not infer decisions from the comparison forms.

Current state, checked 6 November 2026: both reviewers have 20 completed assisted comparison judgments, agreeing on 6 insufficient-evidence and 14 not-directly-comparable labels. Reviewer B (Alex Karadjov) has 20 recorded extraction confirmations; Reviewer A has none. All 20 pair labels are recorded as assisted consensus, with no independently adjudicated gold cases. These comparison records are separate from the 66 retrieval-relevance submissions for 33 candidate pairs.

`evaluate.py` reports extraction coverage, comparison progress and assisted baseline-label agreement separately from independent metrics. It refuses independent adjudication without explicit independent annotation provenance from both reviewers. Experimental-finding accuracy remains null until a separate reference-label evaluation is implemented; the baseline currently returns source-derived directions rather than predicting them.

Run `python scripts/review_progress.py` and `python scripts/rebuild.py` after review edits to validate relevance records and refresh all evaluation and demo outputs. Do not change pending labels just to obtain metrics. The generator preserves existing reviews and creates version-2 forms only when missing.

## Current relevance records and history

`data/review/retrieval_relevance.jsonl` stores the current named judgment, rationale, source checks and approval provenance. `history_id` links to an exact pre-normalization record in `data/review/history/retrieval_relevance_history.jsonl`. Historical records retain their earlier nested revisions; new revisions should append a snapshot to the history file rather than nest it in the current record.

Source and account snapshots can be reconstructed from the indexed data using `claim_id` and `evidence_id`. The review packet rebuild adds those contexts in staging. They are not duplicated in the current review file. A completed decision must not carry an active `unresolved_reason`. Unknown preparation or other scientific limitations remain valid in `compares` and `limitations`; completing a relevance review does not resolve them.
