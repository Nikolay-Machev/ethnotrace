> Archived development note. See [current documentation](../README.md) for status.

# Comparison adjudication results: RC001–RC020

Reviewer A: Nikolay-Machev. Reviewer B: Alex Karadjov. Updated 5 November 2026.

Both reviewers now have 20 completed comparison decisions. Their case-level comparability labels and structural review dimensions match on all 20 cases, so there are zero recorded comparison-label disagreements. The repository records 20 `assisted_consensus` outcomes in `data/review/adjudicated.jsonl`: 6 `insufficient_evidence`, 14 `not_directly_comparable`. Every entry retains both reviewer IDs, their rationales, source locators, matching dimensions, and the provenance of the agreement.

These are **assisted consensus outcomes**, not independently blinded gold. Nikolay's review form says `independent_blinded_annotation: false`, and Alex approved assistant-prepared proposals. No additional source review or separate joint adjudicator attestation was documented here. The canonical independent accuracy metric remains unavailable by design.

The `retrieval_relevant` field in the consensus records remains `null` because Nikolay's RC-level retrieval-relevance values are not recorded. The separate 33-pair retrieval relevance review ledger is a distinct task. The matching comparison labels must not be presented as a jointly adjudicated relevance set.

| Case | Reviewer A label | Alex Karadjov label | Consensus |
| --- | --- | --- | --- |
| RC001 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC002 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC003 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC004 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC005 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC006 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC007 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC008 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC009 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC010 | insufficient_evidence | insufficient_evidence | assisted_consensus |
| RC011 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC012 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC013 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC014 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC015 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC016 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC017 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC018 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC019 | not_directly_comparable | not_directly_comparable | assisted_consensus |
| RC020 | not_directly_comparable | not_directly_comparable | assisted_consensus |

## Interpretation

- 20 of 20 comparison labels agree. This indicates agreement on the submitted development judgments; it is not an independent accuracy score.
- No comparison-label conflicts need reconciliation. The recorded `disagreement: false` applies only to comparison labels and matching structural dimensions, not to unfilled retrieval-relevance fields.
- The comparison review set contains 12 existing source links and 8 constructed mismatched-species challenge pairs. It is a nonrepresentative development set.
- Separate experimental-finding direction label reviews have not been finalized.
- Additional independent, blinded reviews would be needed to produce the project's existing `independent_review.comparison_accuracy` metric, if desired.

Reproduce with `python scripts/validate_review_links.py`, `python scripts/evaluate.py` and `python scripts/rebuild.py --check`.
