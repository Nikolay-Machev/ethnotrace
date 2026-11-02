# Preprocessing methods

## Inputs and preservation

`imports/dataset_manifest.json` pins the complete source repository. Preprocessing verifies SHA-256 checksums for every imported file before reading active data. It reads all ten JSONL tables and six JSON documents under `imports/dataset/data`. The archived v0.2 digestive-use examples are preserved but are outside the active Canadian diabetes scope.

Every processed table has the same row count and original record order as its input. No source record is deleted or silently merged. Each output object contains:

| Field | Meaning |
| --- | --- |
| `id` | Original stable identifier where available; otherwise a snapshot-local row identifier |
| `raw` | Original parsed record, unchanged |
| `normalized` | Same structure with NFC Unicode, trimmed/collapsed whitespace, and lower-case DOI strings where present |
| `features` | Explicit mapping results and curated experimental exposure fields |
| `provenance` | Input path, pinned commit, original-record checksum, pipeline version and citation references |
| `evaluation_group_id` | Known-source/conservative-programme grouping where applicable; null for unrelated administrative tables |

JSON documents retain `raw`, `normalized` and input provenance. Original file bytes remain in the snapshot. Normalized passages are conveniences for matching; cite the raw passage and original locator. Indigenous-language accents, punctuation and capitalization are not removed. Scientific species are not inferred from common names or automatically replaced by taxonomic synonyms.

## Normalization rules

`config/normalization.json` is the versioned rule set. Plant parts are mapped only through explicit aliases. For example, leaves maps to leaf, berries remains berry, and inner bark remains inner_bark. An unfamiliar description is retained as text and flagged as unmapped; it is not guessed from context.

Solvents are identified only when ethanol/ethanolic or water occurs in the preparation field. Tea does not automatically acquire a boiling method or a numerical exposure. Ethanol percentage is parsed only when directly associated with ethanol in that field. These mappings are labels, not claims that two preparations have equal chemical composition.

The twelve existing experimental units have curated exposure mappings based on their original extracted methods and locators. Animal doses in mg/kg and mg/kg/day remain distinct. Concentrations in ug/mL are separate fields. Duration is retained in its recorded unit and converted to hours using 24 hours/day and 168 hours/week. Extraction durations are not treated as exposure durations. Dose alternatives such as 125 or 250 mg/kg remain a list, not an interpolated dose range or separate invented observations.

E007 explicitly refers to the same arm as E006. Its structured exposure points to E006 and uses the same shared-arm key. Values not established by the input remain null or absent. Configured route labels are experimental administration modes, not dosing instructions.

Study settings are represented as lists. Experimental endpoints use a small local vocabulary, such as blood_glucose_auc or cell_viability_high_glucose. These are computational labels rather than claims of equivalence to a modern disease ontology.

## Results and comparability

The extracted experimental direction support becomes favourable_effect, no_detected_effect is retained, and mixed_evidence becomes condition_dependent. This translation concerns the specified assay or endpoint only. Original labels and descriptions remain in raw.

The pair table separately retains taxon_alignment, part_alignment, preparation_alignment, outcome_alignment and claim_evidence_label. No favourable laboratory result is converted into support for a traditional recipe. Publication screening categories, review notes and curator rationales remain metadata. There is no model-input export that silently includes those answers as features.

Current normalized records explicitly remain ineligible for supervised training pending independent review. No new review or evidence label is created by preprocessing.

## Relationships and duplication

Known paper IDs, source keys and extracted pair links define connected evaluation groups. E006 and E007 also carry a curated shared-arm key. The Cree/Eeyou Istchee source programme is conservatively kept in one evaluation block when identified by attribution. This is a leakage precaution, not a claim that every paper in that programme shares animals or participants.

Evaluation groups remain unassigned. There is no automatically generated train/test split, and cross-publication cohort overlap remains an open review question. These grouping keys should be revisited before any performance claim. Species generalisation would require additional species-level split design.

Exact duplicate candidates among traditional and experimental records are flagged using source, species, part, preparation, outcome and setting. They are not removed. This test does not detect every paraphrase, reused cohort or duplicate publication. Original DOI and PMID identifiers are preserved and checked by the imported validators.

## Outputs and reproducibility

`references.jsonl` consolidates source attribution, all scientific paper citations, both literature leads, the correction, eight taxonomic lookups and the organiser catalogue. Source-level and publication-level entries can refer to the same work. Each processed record's reference links are checked against the index. All original bibliography documents remain in the imported snapshot.

`quality_report.json` lists counts, missing fields, unmapped values, exact duplicate candidates and limitations. `evaluation_groups.jsonl` and `grouping_edges.jsonl` expose the grouping members and reasons. Output is deterministic: there are no generated timestamps, random splits, downloads or API responses in the preprocessing run.

Run the tests with `python -m unittest discover -s tests -v`. They check preservation of every record/document, unresolved identities, dose versus concentration, shared-arm and pair grouping, citation links, source-tampering detection and byte-identical reruns.
