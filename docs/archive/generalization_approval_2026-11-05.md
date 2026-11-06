> Archived development note. See [current documentation](../README.md) for status.

# Generalization pilot: reviewer approval of assisted source assessments

Date: 5 November 2026

Alex Karadjov approved all ten proposed assistant-prepared pilot relevance judgments in this conversation ("approve all 10"). The approved values are nine `useful` and one `context_only`. See `data/generalization/reviews.jsonl` for the ten attributed, approved entries and the preserved previous unresolved submissions in each `review_provenance.prior_review`.

The original assistant research source ledger is `data/generalization/assistant_source_reviews_2026-11-05.jsonl`. This ledger captures the earlier research stage before reviewer approval, so its original `human_confirmed: false` describes the state at initial source screening. The updated named reviewer file is the authoritative record of subsequent approval.

## Assessment status

- User-approved assisted judgments: **10 / 10** (nine useful, one context only).
- Named reviewer: **Alex Karadjov**. Approval was provided in chat, rather than by independently reading each full paper.
- Literature basis: assistant research with cited primary full texts, publisher highlights or author abstracts as recorded. The approving reviewer has not separately attested to inspecting every cited primary paper.
- Assistant-label exposure: **true**. The approving reviewer saw the assistant's proposed decisions. The `saw_rankings_or_assistant_labels` field is set to true for all ten entries, in accordance with the frozen protocol, even though ranking exposure itself is not reported.
- Prior case review: **false**, as previously recorded, with original unresolved records retained inside each approval record.
- Independent blinded human reviews: **0 / 10**. The existing frozen evaluator must keep rankings and performance results withheld because independent eligibility is not met.
- Do not describe an assisted agreement as independent validation, held-out accuracy or transfer-performance evidence.

## Next eligible evaluation

To make an independently evaluated claim, obtain a new set of paper-level relevance labels from a reviewer who has not seen assistant judgments or model rankings. Run the frozen scoring pathway only if all specified prerequisites and honest exposure declarations are satisfied. Otherwise create a separate, transparently named **assisted exploratory evaluation** version instead of bypassing or editing the frozen eligibility rule.

This update changes the review annotations, not the frozen manifest, candidate list, model configuration, or ranking inputs.
