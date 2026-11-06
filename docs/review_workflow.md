# Source review

The review set contains 20 comparisons: the 12 existing extracted links and eight deliberately mismatched pairings of existing records. These are review packets, not reviewed ground truth. They cover positive, null and mixed experimental findings without treating result direction as proof that a traditional claim was tested.

[Case index](review_cases.md) links to both sources. The complete packets are in `data/review/review_cases.jsonl`, including attribution, passages, locations, preparation and outcomes. No new source verification is claimed by constructing these packets.

## Reviewing a new comparison

The current completed reviews are assisted and non-blinded. The following steps apply to new reviews; do not retrospectively mark existing assistant-exposed decisions as independent.

1. One team member edits `data/review/reviewer_a.jsonl`; the other edits `reviewer_b.jsonl`. Work separately before discussing decisions. Avoid consulting the earlier screening labels, baseline predictions or development expectations first.
2. Open both cited sources. Check the species, part, preparation, solvent, exposure, study setting and outcome against the source. Preserve original symptom wording and community attribution. If a source is inaccessible or a detail is absent, record that limitation rather than infer it.
3. Set `reviewer_id` to your own identifier and `reviewed_on` to the date. Record your findings in `taxon`, `plant_part`, `solvent` and `outcome` (use `unknown` when needed). Add a concise `rationale` and precise `source_locators`, such as a section, table or figure for each source.
4. Set `retrieval_relevant` to true if the evidence is useful for assessing the account, including useful null results or preparation mismatches. It need not support the account. Assign a `pair_label` using the definitions below. Keep `claim_comparability.label` equal to `pair_label`, and set both `comparison_review_status` and its compatibility alias `status` to `completed` only after checking the sources. Record assistant exposure in `comparison_review_provenance`; do not claim independent annotation after seeing suggested labels.
5. Compare your decisions. In `adjudicated.jsonl`, record both reviewer identifiers, the agreed fields and label, source locators, rationale and whether there was a `disagreement`. Explain how any disagreement was resolved. Leave unresolved cases pending. Use `assisted_consensus` for agreement on assisted comparisons, retaining its provenance and leaving consensus retrieval relevance null. Use `adjudicated` only for a separately documented adjudication meeting the evaluator’s independent-review requirements; two matching reviewer IDs or labels are not enough.
6. Run `python scripts/evaluate.py`. The script rejects adjudications without two distinct completed reviewer records and supporting provenance. Identifiers alone cannot establish genuine independence; that depends on how the review was conducted.

| Pair label | Meaning |
| --- | --- |
| `support` | A sufficiently comparable experiment detects the relevant effect in its stated experimental setting. This does not establish clinical efficacy. |
| `no_detected_effect` | A sufficiently comparable experiment reports no statistically significant relevant effect. This is not proof that no effect exists. |
| `mixed_evidence` | Comparable results differ across relevant outcomes, arms or studies explicitly included in the comparison. |
| `not_directly_comparable` | A documented species, part, preparation or outcome difference prevents a direct test of the account. |
| `insufficient_evidence` | Missing information or an unclear claim prevents a defensible comparison. |

A positive laboratory result can still be `not_directly_comparable` or `insufficient_evidence`. Missing preparation details are not a demonstrated preparation mismatch. A shared solvent alone does not establish equivalent recipes or exposure.

## Evaluation scope

All current cases are development cases. Source and programme group identifiers are retained. Do not distribute experiments from the same paper, shared traditional account or linked evaluation block across future training and test sets. The small, connected collection does not currently support an independent held-out performance claim.

The 20 packets do not judge every bibliographic retrieval candidate. All 33 candidates across six evaluated accounts now have matching assisted relevance decisions in `retrieval_relevance.jsonl`. The resulting retrieval metrics are development results; complete coverage does not make those annotations independent. Do not fill label quotas with unsupported judgments.

Rebuilding the packets does not overwrite existing reviewer forms. Keep completed reviews under version control. Source rights and attribution remain those of the underlying records.

## Separate comparability and findings

The project now treats claim comparability and experimental findings as separate outputs, rather than a five-class training target. Traditional uses are interpreted narrowly. The baseline already retains `experimental_result_direction` separately from its comparison `status`; reviewer A now records explicit `claim_comparability` and `experimental_findings` objects, with findings linked to the original experimental source. Existing `pair_label` values are retained for compatibility.

Reviewer B (Alex Karadjov) explicitly reviewed and approved AI-prepared comparisons for all 20 cases on 5 November 2026: 6 insufficient evidence and 14 not directly comparable. The canonical Reviewer B file records the completed labels, rationales, original source locators and explicit non-blinded, assisted provenance. Reviewer A has now completed 20 comparisons. The 20 submitted comparison labels agree with Reviewer B's decisions and are recorded as `assisted_consensus` in `adjudicated.jsonl`. No independently blinded gold adjudication is claimed. Reviewer B's 20 previously confirmed extraction checks remain separate from these comparison judgments.

Use these cases for development evaluation, not fine-tuning. The eight constructed species mismatches are challenge cases, not a representative sample of natural retrieval results. Positive, null and condition-dependent experimental findings remain visible even when the traditional claim cannot be directly assessed. Do not reinterpret nonspecific historical symptoms as glucose-regulation claims to create positive labels.
