# Retrieval baseline

The offline baseline indexes 59 evidence documents: 12 extracted experimental units, 45 publication records without extracted units, and two additional literature leads. The six parent publications represented by extracted units are excluded as duplicate retrieval entries. Bibliographic leads remain explicitly distinguished from extracted experiments.

## Retrieval

A query is one of the 12 traditional-use records. Candidates must overlap an explicitly recorded scientific species. Unresolved species return no candidates; common names are not silently resolved. A multi-species record with an overlap is a candidate, not proof of a single-species preparation.

Candidates receive 10 points for species overlap, two for overlapping plant parts (minus two for known different parts), and one for a shared explicit solvent (minus one for different explicit solvents). Unknown fields contribute zero. A token-overlap score compares the original use description with the experimental endpoint or publication title. Ties are ordered by evidence ID. This is a transparent lexical baseline, not a semantic outcome model.

Experimental result direction, earlier screening labels and reported result text do not influence ranking. Each output includes score components, citations, available passages and locations, evidence level and comparison limitations.

## Comparison limits

Rules identify explicit species, part and solvent differences. A narrow outcome rule flags neuronal viability experiments as different from the pitcher-plant infection account. Other outcome relationships remain unestablished. Preparation equivalence is never inferred from a shared solvent. The current comparator outputs `not_directly_comparable` or `insufficient_evidence`; it does not automatically assign support, null or mixed claim-level labels.

## Development results

The 20-case development set contains 12 seeded links and eight constructed species mismatches. Scientific-name agreement and species-gate membership checks both pass for all 20 cases. Across the six seeded queries, macro recall at five is 0.667 and mean reciprocal rank is 0.408. These measure recovery of existing links, not independently verified scientific relevance. They also show that species matching alone does not reliably rank extracted evidence first.

No independently adjudicated cases are currently available. Independent comparison accuracy and retrieval recall are therefore null. The evaluator only reports independent retrieval recall for queries with complete candidate judgments. All cases remain in development; no held-out test result is claimed.

The generated report records review-input hashes. Predictions are saved separately from review packets to reduce anchoring during review. See [review instructions](review_workflow.md).

## Commands

```bash
python scripts/build_review_set.py
python scripts/retrieve.py --claim T011 --limit 5
python scripts/retrieve.py --claim T008 --compare E004
python scripts/evaluate.py
python -m unittest discover -s tests -v
```

Outputs are `data/evaluation/baseline_report.json` and `baseline_predictions.jsonl`. The implementation uses Python's standard library and performs no network calls or model training.

## Separate comparability and findings

The project now treats claim comparability and experimental findings as separate outputs, rather than a five-class training target. Traditional uses are interpreted narrowly. The baseline already retains `experimental_result_direction` separately from its comparison `status`; reviewer A now records explicit `claim_comparability` and `experimental_findings` objects, with findings linked to the original experimental source. Existing `pair_label` values are retained for compatibility.

Reviewer A confirmed all 20 assistant-proposed comparison judgments: 10 `insufficient_evidence` and 10 `not_directly_comparable`. This confirmation followed exposure to the assistant's judgments and is recorded as assisted review, not blinded independent annotation. Both reviewers' extraction confirmations do not imply partner agreement on comparison labels. Adjudication remains pending.

Use these cases for development evaluation, not fine-tuning. The eight constructed species mismatches are challenge cases, not a representative sample of natural retrieval results. Positive, null and condition-dependent experimental findings remain visible even when the traditional claim cannot be directly assessed. Do not reinterpret nonspecific historical symptoms as glucose-regulation claims to create positive labels.
