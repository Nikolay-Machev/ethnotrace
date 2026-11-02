# Data quality report

Generated from the pinned imported snapshot by `scripts/preprocess.py`. The machine-readable report is `data/processed/quality_report.json`. These checks describe data structure, not scientific validity.

| Table | Rows |
| --- | ---: |
| catalogue_imported_source_rows | 1 |
| catalogue_literature_leads | 2 |
| catalogue_resource_screening | 93 |
| claim_study_pair_assessments | 102 |
| experimental_records | 12 |
| extracted_claim_study_pairs | 12 |
| papers | 51 |
| study_reviews | 51 |
| taxon_crosswalk | 8 |
| traditional_records | 12 |

The pipeline also processed 6 JSON metadata documents and assembled 74 reference entries. It produced 21 unassigned evaluation groups. There are no training-eligible records.

## Missing or unmapped fields

| Field/issue | Records |
| --- | ---: |
| experimental_records.plant_part: not_established | 2 |
| traditional_records.administration_route: not_established | 9 |
| traditional_records.plant_part: not_established | 6 |
| traditional_records.plant_part: unmapped_preserved | 1 |
| traditional_records.preparation: not_established | 8 |
| traditional_records.species: not_established | 2 |

No exact duplicate candidates were found under the documented record fingerprint. This does not establish absence of repeated testimony, overlapping cohorts or paraphrased duplication.

The two unidentified settler species remain null. Eight traditional preparation fields remain null, six traditional plant-part fields remain null, and one plant-part description remains unmapped. No missing values have been imputed.

The existing scientific-review limits remain: incomplete full-text extraction, unresolved traditional preparation/outcome alignment, and no completed independent review. Human review and rights checks are not replaced by preprocessing.
