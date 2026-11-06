# Reviewer B comparison draft awaiting case-level confirmation

The 20 entries in `data/review/reviewer_b_comparison_proposals.jsonl` are proposed comparisons prepared from the existing source-linked packets in `data/review/review_cases.jsonl`.

Alex Karadjov has explicitly reported completing the comparison review of all 20 cases. The previously uploaded 33-record relevance-review document contains T-series retrieval judgments, not RC001–RC020 final comparison labels. The proposals therefore are **not** claimed as Alex's own selections, direct re-verification of the cited sources, a blinded review or independent adjudication.

Each proposal states its exact RC identifier, source locators, narrow interpretation, and a label under the project's five-label scheme. Proposed outcomes remain distinct from clinical efficacy or evidence of direct comparability.

The official `data/review/reviewer_b.jsonl` stays unchanged in its case-level comparison fields. It already retains Alex's source-extraction confirmation. These draft entries require explicit case-level approval or correction before entering the official reviewer file.

On approval, record the actual review date and whether assistant-proposed labels were visible, maintain the compatibility fields `status`, `comparison_review_status`, `pair_label` and `claim_comparability.label`, preserve precise source locators, and set `independent_blinded_annotation` to false if proposals were inspected before the judgment. Never represent approval of these proposals as blinded independent review.

Nikolay's 20 comparison form entries and the 20 adjudication forms remain pending. No review outcome has been silently credited to either reviewer.

`python scripts/validate_review_links.py`, `python scripts/review_progress.py`, `python scripts/evaluate.py` and `python scripts/rebuild.py` must be rerun after approved data changes.
