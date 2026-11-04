# Retrieval baseline

The offline baseline indexes 59 evidence documents: 12 extracted experimental units, 45 publication records without extracted units, and two additional literature leads. The six parent publications represented by extracted units are excluded as duplicate retrieval entries. Bibliographic leads remain explicitly distinguished from extracted experiments.

## Retrieval

A query is one of the 12 traditional-use records. Candidates must overlap an explicitly recorded scientific species. Unresolved species return no candidates; common names are not silently resolved. A multi-species record with an overlap is a candidate, not proof of a single-species preparation.

Candidates receive 10 points for species overlap, two for overlapping plant parts (minus two for known different parts), and one for a shared explicit solvent (minus one for different explicit solvents). Unknown fields contribute zero. A token-overlap score compares the original use description with the experimental endpoint or publication title. Ties are ordered by evidence ID. This is a transparent lexical baseline, not a semantic outcome model.

Experimental result direction, earlier screening labels and reported result text do not influence ranking. Each output includes score components, citations, available passages and locations, evidence level and comparison limitations.

## Comparison limits

Rules identify explicit species, part and solvent differences. A narrow outcome rule flags neuronal viability experiments as different from the pitcher-plant infection account. Other outcome relationships remain unestablished. Preparation equivalence is never inferred from a shared solvent. The current comparator outputs `not_directly_comparable` or `insufficient_evidence`; it does not automatically assign support, null or mixed claim-level labels.

## Development results

The 20-case development set contains 12 seeded links and eight constructed species mismatches. Scientific-name agreement and species-gate membership checks both pass for all 20 cases. Across the six seeded queries, baseline 1.1 scores macro recall at five 0.917 and mean reciprocal rank 0.561 (version 1.0 scored 0.667 and 0.408). Candidate pools hold only four to seven items, so expected scores under uniform random ordering are 0.869 and 0.595; version 1.1's recall is barely above that level and its MRR is below it. These measure recovery of existing links, not independently verified scientific relevance, and ten of the twelve seeded links pair a traditional account with an experiment from the same paper. They also show that species matching alone does not reliably rank extracted evidence first.

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
