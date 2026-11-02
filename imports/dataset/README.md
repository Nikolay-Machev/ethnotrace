# EthnoTrace

A dataset for comparing Canadian traditional plant-use accounts with experimental research on blood-glucose regulation and diabetes-related symptoms.

## Current collection

Version 0.8 contains:

- **12 traditional-use records**, including nine identified species and two settler accounts with unresolved species.
- **51 scientific publications**, with complete citations and question-specific screening annotations.
- **12 experimental result units from six publications**, extracted from selected full-text methods, results and figures/tables.
- **12 source-checked taxonomic links** between traditional records and experiments, with preparation and outcome differences recorded separately.

Traditional sources include researcher reports of Cree knowledge from Eeyou Istchee, community-published Gwich’in accounts, a named Cowichan speaker, and French-Canadian/Franco-Ontarian settler records. This is a small attributed collection, not a representative survey of Canada. Multiple records can share an account or publication.

See the [extraction report](docs/extraction_report.md) for every new record and result. Missing traditional preparation or symptom detail remains unresolved. Experimental recipes are not assigned retrospectively to historical accounts. Neither settler account has been given an inferred scientific species.

## Organiser catalogue

[Screening of all 93 catalogue entries](docs/catalogue_screening.md) added one Canadian Salish diabetes-use database record, eight scientific-name crosswalk entries and two experimental literature leads. The leads are stored separately from the 51-paper collection. The Arbutus record retains an unresolved original reference; no preparation was inferred.

## Evidence status

Same-species linkage does not establish the same preparation, symptom or clinical effect. The extracted pair table records these dimensions separately from experimental result direction. Independent review remains pending; no pair is marked ready for training.

The publication screening counts are 12 support, 5 no detected effect, 16 mixed evidence, 10 not directly comparable and 8 insufficient evidence. These describe explicit study questions, not validated traditional-claim labels. Full-text extraction corrected the Larix paper from support to mixed evidence: its prevention and treatment protocols had different glycaemic outcomes.

## Files

| Path | Contents |
| --- | --- |
| `data/traditional_records.jsonl` | Attributed traditional uses, original wording or marked paraphrases, preparation and provenance |
| `data/experimental_records.jsonl` | Discrete experimental outcomes, controls, exposures, settings and source locators |
| `data/extracted_claim_study_pairs.jsonl` | Taxon-linked extracted pairs with separate comparability axes |
| `data/catalogue_resource_screening.jsonl` | Decisions and inspection depth for all 93 organiser catalogue entries |
| `data/taxon_crosswalk.jsonl` | Eight GBIF scientific-name matches linked to traditional records |
| `data/catalogue_literature_leads.jsonl` | Two cited experimental papers awaiting full-text extraction |
| `data/catalogue_imported_source_rows.jsonl` | Exact CC0 archive row behind T016 and download provenance |
| `data/catalogue_screening_summary.json` | Screen counts, filters and source document hashes |
| `data/sources.json` | Imported-source citations, rights and formats |
| `data/papers.jsonl` | All 51 publication citations and screening annotations |
| `data/expansion_summary.json` | Current extraction counts and verification limits |
| [Extraction report](docs/extraction_report.md) | Records, results, correction and limitations |
| [References](docs/references.md) / [Paper bibliography](docs/papers.md) | Full citations and source inspection history |
| [Data dictionary](docs/data_dictionary.md) | Schema and missing-value conventions |
| `data/study_reviews.jsonl` | Per-paper review history; some initial findings are superseded by selected full-text extraction |
| `data/claim_study_pair_assessments.jsonl` | Historical v0.6 audit of the 51 papers against T005/T006 only |
| `archive/v0.2/` | Initial out-of-scope examples |

Files are UTF-8. JSONL stores one object per line. Traditional and experimental records join to `sources.json` by `source_key`; extracted pairs reference their stable record IDs. Publication metadata is self-contained.

## Curation and reuse

Records were assembled with AI assistance and await independent review. A source quotation is a locator anchor and may establish only part of a record. Scientific names, attribution, preparation, experimental settings and missing information must remain attached to exported results.

Source-specific rights apply. Community text is summarised with short excerpts and attribution. Full articles, images, interview transcripts and community webpages are not redistributed. Indigenous knowledge provenance and access conditions must be preserved. Computational and laboratory findings are not established medical facts.

## Validation

Run from the repository root:

```bash
python scripts/validate.py
python scripts/validate_papers.py
python scripts/validate_review.py
python scripts/validate_extraction.py
python scripts/validate_catalogue.py
```

Structural checks detect broken references and inconsistent metadata; they do not establish medical validity or independent review.
