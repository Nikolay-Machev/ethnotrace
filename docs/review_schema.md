# Review records, version 2

Both reviewer files use the same fields. The original extraction packets, source passages and citations remain in `review_cases.jsonl`, joined by `case_id`; reviewer A no longer duplicates those packets.

- `extraction_verified` and `corrections` record source-extraction checking. The provenance field distinguishes direct user reporting from the partner's verification reported by the user.
- `comparison_review_status` records whether the comparison judgment is complete. `status` is a compatibility alias.
- `claim_comparability` records the label, narrow interpretation of the documented use and rationale. `pair_label` is a compatibility alias and must match its label.
- `experimental_findings` records the result direction, endpoint, setting, reported result and source separately. An extraction confirmation does not automatically complete an independent direction-label review.
- `experimental_findings_review_status` tracks that separate step. Current records are `extraction_verified_not_separately_labelled`.
- `comparison_review_provenance` records whether judgments were made after seeing assistant labels. Unknown independence remains null; it must not be inferred from two reviewer IDs.
- `retrieval_relevant` is a separate relevance judgment and remains null until explicitly reviewed.

Current state: both reviewers reported extraction verification for all 20 cases. Reviewer A confirmed 20 assisted comparison judgments. Reviewer B's 20 comparison judgments remain pending. No adjudicated independent evaluation set exists.

`evaluate.py` reports extraction coverage, comparison progress and assisted baseline-label agreement separately from independent metrics. It refuses independent adjudication without explicit independent annotation provenance from both reviewers. Experimental-finding accuracy remains null until a separate reference-label evaluation is implemented; the baseline currently returns source-derived directions rather than predicting them.

Run `python scripts/evaluate.py` after review edits and `python scripts/build_demo.py` to refresh the demo snapshot. Do not change pending labels just to obtain metrics. The generator preserves existing reviews and creates version-2 forms only when missing.
