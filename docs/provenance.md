# Development provenance

This is a chronological development log. Review-status statements within earlier dated phases describe that phase, not the current collection. Current status is in the [README](../README.md) and [product audit](product_audit.md).

## Pre-existing material

The complete dataset repository snapshot is imported under `imports/dataset`. Source repository: `Nikolay-Machev/Dataset-`; commit: `b4ab9fe0dbafb4a9d97dfcd1cc9b0bf4947d1062`; import date: 2 November 2026.

The 37 imported files include curated records, source metadata, citations, bibliographies, source leads, earlier screening and extraction reports, original validators and historical archived examples. Their Git blob hashes and SHA-256 checksums are recorded in `imports/dataset_manifest.json`. These files are disclosed as pre-hackathon work. They are not new hackathon data discovery or independent scientific review.

## Additions during the hackathon

The official project repository adds a reproducible preprocessing script, versioned normalization rules, preservation and relationship tests, generated processed tables, an integrated reference index, evaluation grouping metadata, a missing-data report and project documentation.

The pipeline performs no new literature search, source verification, clinical assessment or human annotation. Such work should be recorded separately when performed. Generated outputs derive from the pinned imported snapshot; their provenance points to that input commit.

## AI contribution

An AI assistant substantially contributed to the earlier dataset discovery and curation and to this import, preprocessing implementation, tests and documentation. Team review is still required for scientific interpretation, attribution, rights and final claims. A second pass by the same assistant is not independent review.

## Retrieval and review preparation — 2 November 2026

Added the deterministic retrieval and comparison baseline, 20 source-linked review packets, separate reviewer and adjudication forms, evaluation scripts and nine baseline tests. Twelve packets preserve existing extracted links; eight deliberately pair different-species records to test mismatch handling. No new experiments or traditional accounts were invented. AI assisted with these additions. Human source review remains pending, and development checks are not independent scientific validation.

## Evidence atlas extension

The account-level atlas, deterministic aggregation, drill-down filters, tests and updated research framing were developed during the hackathon with substantial AI assistance. They reuse the pinned sources and comparison rules. They add no new source verification or independent human review. Semantic retrieval was not part of this extension; it is described in the later semantic retrieval section.

## Gap and review preparation extension

An AI assistant implemented gap explanations and prepared source-linked relevance review packets during the hackathon. The assistant inspected the publisher PDF methods and Table 2 for DOI 10.18433/J35W27; the source checksum and locators are retained in TX001, with no PDF redistribution. DOI 10.1155/2013/189819 was only partially inspected through indexed full-text sections; TX002 records the access limitations. No new human verification, comparison review, or adjudication was asserted. Existing source and review records remain intact.

## Evaluation and report export

AI-assisted implementation added an offline evaluation page and local Markdown evidence-report export. The page uses current review progress and seeded development checks while retaining the earlier baseline-comparison run as a labelled historical result. No new human decisions, independent metrics or clinical validation were added. Reports retain source rights, citations, gaps and review provenance.

## Pretrained semantic retrieval experiment

AI-assisted implementation added local pretrained MiniLM inference, semantic and reciprocal-rank-fusion challengers, immutable model-version provenance, candidate-set safeguards, development evaluation and a ranking selector. Model weights are pre-existing Apache-2.0 material from Sentence Transformers; no fine-tuning occurred. Inference used only documented-use text and paper-title/endpoint fields, never review labels or curator result-direction fields. All comparison rules and human-review records were preserved. The observed seeded development results are not independent scientific validation.

## Audit follow-up — 4 November 2026

A source-checked correction distinguishes the observed E005 trend from statistical evidence in the KK-Ay experiment. The original import and historical reviews were preserved. The evaluation page now computes uniform random-order expectations from the six actual pools and reports shared-publication links. Neither the audit nor these benchmarks create independent relevance judgments.
