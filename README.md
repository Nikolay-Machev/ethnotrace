# EthnoTrace

EthnoTrace investigates how closely experimental research tests traditional plant uses documented in Canada for blood-glucose regulation and diabetes-related symptoms.

The same plant name can appear in a traditional account and a laboratory paper while referring to different plant parts, preparations, exposures or outcomes. The project makes those differences visible in an evidence atlas and individual comparisons, with a source passage and citation behind each comparison. Gaps describe this indexed collection, not the absence of research worldwide.

## Research question

**How closely do experimental studies test documented Canadian traditional plant uses associated with blood-glucose regulation and diabetes-related symptoms, and where does the indexed evidence leave gaps in comparability or documentation?**

The geographic scope applies to the traditional-use accounts. Experimental studies may come from any country. The collection includes Indigenous and settler accounts where the sources support that attribution; it does not represent every Canadian community or tradition.

Original symptom descriptions are retained. A historical reference to frequent urination, for example, is not automatically treated as a diabetes diagnosis. A cellular or animal result is not presented as an established medical effect in people.

## Project goals

A research tool that retrieves experimental evidence for a documented plant-use account and compares:

- Scientific species and unresolved original names.
- Plant part, preparation, solvent and administration route.
- Experimental setting, exposure, comparator and measured outcome.
- Result direction, uncertainty and relevance to the traditional account.

The output separates two questions:

| Component | What it reports |
| --- | --- |
| Claim comparability | Which species, parts, preparations and outcomes match, differ or remain unknown, interpreting the documented traditional use narrowly. |
| Experimental findings | What effect the experiment detected, including null or mixed findings, within its stated setting, endpoint and exposure. |

A positive experimental finding does not automatically support the traditional claim. Both components retain citations and source passages. The tool is not a remedy recommendation or a clinical validation service.

## Current implementation

This repository contains a versioned dataset import, offline preprocessing, a scientific-name-based retrieval baseline and 20 source-linked comparison packets. Retrieval returns citations and explains explicit mismatches. Development checks run automatically. Both reviewers have reported verifying the extractions. Reviewer A has confirmed the 20 comparison judgments after seeing the assistant's reasoning; partner comparison judgments remain outstanding. An interactive evidence atlas and comparison explorer are available in `web/`.

See the [retrieval methods and results](docs/baseline.md), [comparison index](docs/review_cases.md) and [review workflow](docs/review_workflow.md).

| Collection | Count | Meaning |
| --- | ---: | --- |
| Traditional-use records | 12 | Nine identified species; two records have unresolved species |
| Scientific publications | 51 | Publication-level citations and provisional screening annotations |
| Experimental results | 12 | Selected arm/protocol/outcome units from six publications |
| Extracted claim–study links | 12 | Same-species links with separate preparation and outcome limitations |
| Additional literature leads | 2 | Abstract-screened leads awaiting experimental extraction |

Several records share a publication or traditional account. These counts must not be added together or interpreted as independent studies. Extraction verification is recorded separately from comparison review. No pair has completed independent two-reviewer comparison adjudication or been marked ready for supervised training.

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
python scripts/build_review_set.py
python scripts/retrieve.py --claim T011 --limit 5
python scripts/evaluate.py
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

## Evidence explorer

Open `web/index.html` in a browser to explore all 12 traditional-use accounts. The atlas preserves each account separately, including unresolved plant names and accounts without extracted experiments. Search by plant, account ID or attribution; filter accounts by experimental setting or missing traditional preparation. Click a dimension count to open its cited comparisons. Counts distinguish experimental units, unique papers and literature leads. The demo includes a traditional-account selector, side-by-side fields, separate experimental findings and claim comparability, source passages, citations and per-case review counts. Extracted experiments are shown by default; uncheck the filter to include literature leads in baseline order.

The browser uses a reproducible snapshot generated by the existing Python retrieval baseline. It does not run a model or make external API requests. After changing the dataset, retrieval logic or review records, rebuild it:

```bash
python scripts/build_demo.py
python -m http.server 8000 --directory web
```

Then open http://localhost:8000. Opening `web/index.html` directly also works. Review status reflects the build snapshot: one human comparison review complete and the second pending for the reviewed comparisons. Other retrieved entries are explicitly marked outside the review set. This interface is committed to the repository; it has not been deployed to a hosting service.

## Review format and UI verification

[Review schema version 2](docs/review_schema.md) separates extraction checks, comparison judgments and experimental findings. Evaluation reports assisted reviewer agreement separately from independent accuracy.

The comparison renderer closes each table before rendering the findings panels. Browser checks covered all three plant selections, separate result cards, table visibility, the literature-lead filter, expandable source sections and source-link targets. Python tests cover review progress and schema consistency. After pulling an interface update, refresh the browser; JavaScript and CSS version parameters also prevent reuse of the earlier cached renderer.

## Retrieval development

Baseline 1.1 scores extracted units using their endpoint or parent-paper title, addressing the unequal text coverage of version 1.0. Seeded-link macro recall at five increased from 0.667 to 0.917 across six development queries; this is not held-out scientific accuracy. Extracted experiments and literature leads are displayed in separate groups, with baseline order retained inside each group.

See the [retrieval error report](docs/retrieval_error_report.md), [candidate relevance queue](data/review/retrieval_relevance.jsonl) and [evidence atlas methods](docs/evidence_atlas.md). Run `python scripts/analyze_retrieval.py` to reproduce the ranking comparison. Human candidate relevance review and reviewer B's comparison judgments remain pending.

## Optional semantic retrieval

Semantic retrieval remains future work. It would rank source passages alongside the lexical baseline and return evidence IDs through the same export boundary. It would not assign outcome equivalence or change comparison rules. We will consider it after candidate relevance review, only if a measured retrieval problem and available time justify it. Compare systems on fixed candidate sets with source-group-aware evaluation; report development results as development results.
