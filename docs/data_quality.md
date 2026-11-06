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

A [source-by-source audit of the 18 missing species, plant-part and preparation fields](missing_field_source_audit_2026-11-05.md) checked the cited accounts and related source publications on 5 November 2026. None of the missing values was supported strongly enough for a source-specific overwrite. Original values remain null; related laboratory plant parts and recipes were not transferred into traditional-use records.

No exact duplicate candidates were found under the documented record fingerprint. This does not establish absence of repeated testimony, overlapping cohorts or paraphrased duplication.

The two unidentified settler species remain null. Eight traditional preparation fields remain null, six traditional plant-part fields remain null, and one plant-part description remains unmapped. No missing values have been imputed.

The existing scientific-review limits remain: incomplete full-text extraction, unresolved traditional preparation/outcome alignment, and no completed independent review. Human review and rights checks are not replaced by preprocessing.

## Known issues from the 3 November 2026 data review

- **E005 corrected on 4 November 2026.** The [Vianna et al. paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/) describes a downward trend in the seven-day KK-Ay mouse experiment; its Discussion explicitly says significance could not be established. The active E005 finding and T009/E005 study-result field now read `statistically_inconclusive`. This is neither evidence of a demonstrated benefit nor proof of no effect. `config/normalization.json` records the date, source and override; the original import, processed raw fields, historical reviewer answers and traditional claim remain intact.
- **Pinned data dictionary.** `imports/dataset/docs/data_dictionary.md` is left unchanged to preserve its checksum. Two statements are outdated: `language` is `fr` for two records and `en` for ten, and `full_text_reviewed: false` for every paper does not reflect the six papers with selected full-text extractions.
- **Leads linked to T013 and T014.** CL12843638 and CL39426763 are linked because their records name *Vaccinium uliginosum*. The 2024 paper's title calls *V. uliginosum* "lingonberry", a common name usually applied to *V. vitis-idaea*, and its source material has not been checked, so that species match is unverified.
