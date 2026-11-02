# EthnoTrace

EthnoTrace investigates how closely experimental research tests traditional plant uses documented in Canada for blood-glucose regulation and diabetes-related symptoms.

The same plant name can appear in a traditional account and a laboratory paper while referring to different plant parts, preparations, exposures or outcomes. The project aims to make those differences visible, with a source passage and citation behind each comparison.

## Research question

**How closely do experimental studies test documented Canadian traditional plant uses associated with blood-glucose regulation and diabetes-related symptoms?**

The geographic scope applies to the traditional-use accounts. Experimental studies may come from any country. The collection includes Indigenous and settler accounts where the sources support that attribution; it does not represent every Canadian community or tradition.

Original symptom descriptions are retained. A historical reference to frequent urination, for example, is not automatically treated as a diabetes diagnosis. A cellular or animal result is not presented as an established medical effect in people.

## What we aim to build

A research tool that retrieves experimental evidence for a documented plant-use account and compares:

- Scientific species and unresolved original names.
- Plant part, preparation, solvent and administration route.
- Experimental setting, exposure, comparator and measured outcome.
- Result direction, uncertainty and relevance to the traditional account.

The intended output is a cited comparison showing what was tested, what differs and what remains unknown. It is not a remedy recommendation or a clinical validation service.

## Current implementation

This repository currently contains a versioned dataset import and an offline preprocessing pipeline. Retrieval, an interactive comparison interface and model evaluation are planned work, not completed features.

| Collection | Count | Meaning |
| --- | ---: | --- |
| Traditional-use records | 12 | Nine identified species; two records have unresolved species |
| Scientific publications | 51 | Publication-level citations and provisional screening annotations |
| Experimental results | 12 | Selected arm/protocol/outcome units from six publications |
| Extracted claim–study links | 12 | Same-species links with separate preparation and outcome limitations |
| Additional literature leads | 2 | Abstract-screened leads awaiting experimental extraction |

Several records share a publication or traditional account. These counts must not be added together or interpreted as independent studies. No current claim–study pair has completed independent review or been marked ready for supervised training.

## Data and preprocessing

The source snapshot is preserved without edits in [`imports/dataset`](imports/dataset). Its [manifest](imports/dataset_manifest.json) records the original repository commit, Git blob IDs and SHA-256 hashes for all 37 files. Historical out-of-scope examples are retained in the imported archive but excluded from active preprocessing.

The pipeline processes every active JSON and JSONL input into [`data/processed`](data/processed). It preserves each original record under `raw`, adds normalized text under `normalized`, and places derived comparison fields under `features`.

Preprocessing includes Unicode and whitespace normalization, explicit plant-part mappings, study-setting lists, endpoint terms, and versioned experimental exposure rules. It keeps dose separate from cell concentration and treatment duration separate from extraction time. Missing information stays null. No species, recipe, efficacy finding or independent review is invented.

Experimental result direction and claim comparability are separate fields. Publication-level screening categories remain provisional metadata, not training ground truth. Known shared sources and papers are grouped for evaluation, with a conservative block for the Cree research programme. Groups are unassigned; no train/test split is claimed.

See [preprocessing methods](docs/preprocessing.md) and the [quality report](docs/data_quality.md) for rules and limitations.

## Run locally

Python 3.10 or newer is required. The pipeline uses the standard library and needs no API keys, downloads or model services.

```bash
python scripts/preprocess.py
python -m unittest discover -s tests -v
```

For an alternate output directory:

```bash
python scripts/preprocess.py --output /tmp/ethnotrace-processed
```

An altered imported file causes preprocessing to stop with a checksum error. To adopt a new dataset version, import and document a new snapshot rather than editing the pinned copy.

## Citations and source rights

- [Complete source references](imports/dataset/docs/references.md).
- [Scientific paper bibliography](imports/dataset/docs/papers.md).
- [Machine-readable reference index](data/processed/references.jsonl).
- [Original data dictionary](imports/dataset/docs/data_dictionary.md).
- [Rights and attribution notes](docs/rights.md).

The reference index includes 74 entries across imported sources, publications, a correction, taxonomic lookups and the organiser catalogue. Some entries describe the same underlying publication at different stages; this is not an independent evidence count.

Source-specific rights remain attached to the records. No full PDFs, full abstracts, community webpages or images are imported. Indigenous knowledge retains its attribution, cultural context and access considerations. The project does not assert a blanket licence over third-party source material or imply that public access grants unrestricted training rights.

## Hackathon provenance 

The dataset, source curation,and documentation were prepared before the hackathon in `Nikolay-Machev/Dataset`. The pinned starting snapshot is commit [`b4ab9fe0dbafb4a9d97dfcd1cc9b0bf4947d1062`](https://github.com/Nikolay-Machev/Dataset-/tree/b4ab9fe0dbafb4a9d97dfcd1cc9b0bf4947d1062). It is disclosed as pre-existing work.

The import manifest, preprocessing implementation, normalization configuration, tests, processed outputs and research-focused documentation were added to this project during the hackathon. [Development provenance](docs/provenance.md) distinguishes the imported material from these additions.
