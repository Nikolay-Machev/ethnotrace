# Data dictionary

One traditional record describes a documented use in a particular source and community context. One experimental record describes a study setting and outcome. Multiple records from one paper are not independent studies.

## Shared fields

| Field | Type | Meaning |
| --- | --- | --- |
| record_id | string | Stable identifier; T for traditional use, E for experimental findings. Existing identifiers are preserved across releases. |
| dataset_scope | string | canadian_diabetes for the active collection |
| source_key | string | Join key into sources.json |
| species | array of strings or null | Scientific names established by the source or a documented taxonomic check |
| original_plant_name | array of strings | Source plant names, preserving common names and relevant spelling |
| plant_part | string or null | Material used |
| preparation | string or null | Preparation, solvent and formulation where stated |
| reported_use_or_outcome | string | Factual paraphrase of reported use or experimental finding |
| study_setting | string | documented_folk_use for current records; animal_in_vivo, isolated_tissue_ex_vivo, in_vitro, human_randomized_trial or human_observational for future experiments |
| source_id | string | Bibliographic identifier |
| source_url | string | Source link |
| supporting_passage | string | Brief verbatim excerpt; line breaks and apostrophes may be normalized as noted |
| passage_locator | string | Section, page and reference locator |
| licence | string | Source-specific rights label; unknown does not mean open |
| notes | string | Interpretation limits and transformations |
| curation_method | string | Record preparation method |
| review_status | string | pending_independent_review or independently_reviewed |
| accessed_on | string | YYYY-MM-DD access date |
| language | string | Language of the inspected passage; fr for the current records |

## Traditional-use fields

| Field | Type | Meaning |
| --- | --- | --- |
| knowledge_tradition | string | indigenous, settler, documented_exchange or unspecified |
| community_or_nation | string or null | Specific source attribution; Métis is Indigenous |
| knowledge_holder | string or null | Publicly named contributor, where linked to the record |
| location | string or null | Documented place of use; publisher location is not a substitute |
| historical_period | string or null | Period reported by the source, with uncertainty preserved |
| original_use_description | string | Quotation or marked paraphrase |
| original_use_description_type | string | quotation or paraphrase |
| diabetes_relevance | string | explicit, symptom_associated or unclear |
| relevance_rationale | string | Basis for relevance classification |
| administration_route | string or null | Route stated for this preparation and use |
| access_or_reuse_conditions | string | Permissions, rights or unresolved restrictions |

## Conventions

- null means not established in the inspected material. It does not mean the detail is absent from all sources.
- explicit requires a source reference to diabetes or blood-glucose regulation. It does not establish efficacy.
- symptom_associated requires a written rationale and review. Thirst or frequent urination alone is insufficient.
- unclear records are retained for review and excluded from default evidence matching.
- Preserve mixtures as mixtures; do not attribute their effects to single ingredients.
- Split evaluation data by paper/source to avoid placing related records in both development and test sets.

## Source catalogue

sources.json contains dataset_version, scope, sources and retrieval_resources. Each source has source_key, title, source_url, source_id, licence, licence_url, original_format, import_scope, attribution and accessed_on. Bibliographic leads belong in docs/source_leads.md until material is actually imported.

## Publication catalogue (version 0.4)

`data/papers.jsonl` stores one object per publication. It is separate from traditional-use and experimental finding tables. No validated matching labels have been assigned.

| Field | Meaning |
| --- | --- |
| `paper_id`, `pmid`, `source_id` | Stable local ID `P<PMID>`, PubMed ID, and `PMID:<PMID>` |
| `source_key` | Local key `paper_pmid_<PMID>`; metadata is self-contained in this table |
| `dataset_scope` | `canadian_diabetes` |
| `title`, `authors`, `journal`, `citation` | Indexed title, all indexed author names, journal title, full formatted reference |
| `publication_year`, `first_publication_date` | Indexed issue year and first-publication date; these can differ |
| `volume`, `issue`, `pages_or_article_id` | Journal location metadata; null if unavailable |
| `doi`, `pmcid` | Persistent identifiers; null if unavailable |
| `source_url`, `doi_url`, `full_text_url` | PubMed, DOI and PMC links; a full-text link does not mean the article was reviewed |
| `inclusion_tier` | `core`, `supporting`, `context`, or `provisional_species`; relevance grouping, not a quality score |
| `species`, `species_list_scope` | Abstract-identified scientific names and completeness warning; null means not extracted, not no plants tested |
| `original_plant_name` | Scientific wording retained from the publication; not a historical plant name or independently verified taxonomy |
| `plant_part`, `preparation` | Abstract-supported description; null if not established |
| `reported_use_or_outcome` | Curator paraphrase of the abstract-level result or purpose, including null findings |
| `study_setting` | List of settings; one paper may contain multiple methods. Additional values include `human_pilot`, `ethnobotanical_survey`, `analytical_chemistry`, `review`, and `secondary_data_analysis` |
| `community_or_nation`, `canadian_link` | Source-reported cultural/geographic context and relevance to this collection; an empty list means no specific attribution was extracted |
| `supporting_passage`, `passage_locator`, `supporting_passage_type` | Exact abstract retrieval anchor, maximum 20 words; a quotation rather than a complete evidence extraction |
| `limitations` | Comparability issues, unresolved details and interpretation limits |
| `licence`, `licence_evidence`, `indexed_open_access` | Indexed article licence or an explicit unverified status, basis of that statement, and separate access flag |
| `original_format`, `screening_level`, `full_text_reviewed` | Material inspected and depth of review; all current papers are `abstract_reviewed` with `full_text_reviewed: false` |
| `review_status`, `curation_method`, `accessed_on`, `language` | Review state, AI-assisted curation provenance, retrieval date and indexed language |
| `indexed_publication_types` | Publication-type labels retained from the index; not independent verification |
| `publication_status_flags`, `status_check` | API-supplied notices and limits of the status check; null flags do not prove absence of a correction or retraction |
| `linked_traditional_record_ids`, `match_status` | Currently empty and `not_adjudicated`; no botanical or evidentiary match is assumed |

`data/paper_search_manifest.json` stores the provider, endpoint, parameters, exact queries, reported hit counts, retrieved counts, union size, included count and search limitations. It contains no redistributed abstracts.

## Provisional study classification (version 0.5)

Every publication contains a `classification` object:

| Field | Meaning |
| --- | --- |
| `label` | `support`, `no_detected_effect`, `mixed_evidence`, `not_directly_comparable`, or `insufficient_evidence` |
| `question` | Exact comparison or experimental proposition assessed; required to interpret the label |
| `rationale` | Source-based reason for the assignment |
| `scope` | `study_question_screening`; not an adjudicated traditional-claim pair |
| `basis` | Material used, with additional source inspections documented in the publication record |
| `status`, `classified_on` | Provisional independent-review status and annotation date |
| `claim_pair_label` | False for every current publication |
| `training_eligible` | False until review and properly defined training-unit annotation |
| `evidence_source_url` | Publication source link |
| `secondary_outcomes_note` | Overall outcome summary retained to prevent a narrow label hiding other findings |

`data/classification_summary.json` reports counts by publication, the requested minimum, added papers and zero validated training pairs. A category count does not establish scientific independence or clinical efficacy. `additional_inspection` and `correction` are optional provenance fields for new publications. Correction notices retain their own citation and are not counted as studies.

## Source review (version 0.6)

`study_reviews.jsonl` has one second-pass review per paper, identified by `review_id` and `paper_id`, with full citation, source URL, retrieved-abstract SHA-256, checked category, basis, interpretation notes, candidate record IDs and next action. `independent_review` and `training_eligible` are false. The embedded `source_review` in each paper provides the review identifiers and status.

`claim_study_pair_assessments.jsonl` stores one assessed combination of a current traditional record and a publication. Candidate status is distinct from an evidence label. It includes both source URLs, citation, study/traditional parts and preparations, unresolved species comparison, notes and date. `evidence_label` remains null for every unresolved combination. No-candidate status is not a negative finding or verified botanical exclusion. `review_summary.json` reports coverage and outstanding verification. No full abstracts are redistributed.

## Extracted results and pairs (version 0.7)

Traditional `account_type` distinguishes community-published accounts from investigator reports of traditional use. `underlying_ethnobotanical_source_reviewed` is false where the cited original book, survey or interview was not directly inspected. Source publication time is not the age of a practice.

Experimental records retain the shared fields plus `paper_id`, `model`, `endpoint`, `comparator`, `result_direction`, `extraction_depth`, `citation`, `independent_unit` and `training_eligible`. The unit is an arm/protocol/outcome, not an independent publication. Missing specimen part is null.

`extracted_claim_study_pairs.jsonl` links `traditional_record_id` to `experimental_record_id` and `paper_id`, preserving both source URLs and the study citation. `taxon_alignment`, `part_alignment`, `preparation_alignment` and `outcome_alignment` are separate. `study_result_label` describes the measured outcome; `claim_evidence_label` describes its relevance to the traditional account. `pairing_status` explicitly limits verification to taxonomic linkage. Independent review and training eligibility remain false.

`expansion_summary.json` gives current counts. The earlier `claim_study_pair_assessments.jsonl` and `review_summary.json` describe only the historical T005/T006 audit; they are not a full cross product of the expanded collection. Selected full-text inspections are tracked in each publication's `selected_full_text_extraction` with XML URL and SHA-256.

## Organiser catalogue imports (version 0.8)

`catalogue_resource_screening.jsonl` stores one row per catalogue entry: local ID, row number, resource name, reference numbers in the organiser document, decision, rationale, inspection depth, catalogue URL and screening date. Catalogue-only access/licence statements are not presented as independently checked. The summary stores retrieval hashes and counts.

`catalogue_imported_source_rows.jsonl` stores the original CC0 database row, member name, unique key, download URL, archive SHA-256, citation and rights URI. T016 joins to `sources.json` through `source_key`; `original_source_item_id` points to ETHNO:15976 and `underlying_reference_code` preserves Eb25: 82. No preparation or precise Nation is inferred.

`taxon_crosswalk.jsonl` stores input and matched scientific names, GBIF keys and taxon URLs, name status/rank, provider confidence, exact query URLs, citation, linked traditional record IDs and retrieval date. The provider confidence is a name-match score, not an efficacy or historical-identification probability. Scientific-name matches must not resolve null common-name identities automatically.

`catalogue_literature_leads.jsonl` stores a lead ID, PMID, DOI, complete citation, title, species, candidate traditional IDs, relevance, limitations, review depth, rights status and date. Leads are not part of the 51-paper classification totals or the extracted experimental table. `training_eligible` is false.
