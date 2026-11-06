# Evidence atlas

## Research question

How closely do experimental studies test documented Canadian traditional plant uses associated with blood-glucose regulation and diabetes-related symptoms, and where does the indexed evidence leave gaps in comparability or documentation?

The atlas summarizes the collection; the explorer explains individual comparisons. Each row is a traditional-use account with its original indication and attribution. Accounts sharing a species remain separate. Canadian coverage is selective, not nationally representative.

## Generation and interpretation

`python scripts/build_demo.py` retrieves all same-species candidates for each account, uses the existing comparator, and calls `scripts/atlas.py` to group extracted experimental units by dimension. The generated `web/data.js` includes evidence IDs in each bucket so that a cell opens exactly the underlying comparisons. Literature leads are counted separately and excluded from experimental summaries.

| Dimension | Current rule |
| --- | --- |
| Species | Reported species overlap, difference or unresolved identity. Natural retrieval requires a shared scientific species; synthetic mismatched review cases are excluded. |
| Plant part | Overlap, difference or unknown using the baseline mappings. Overlap does not establish preparation equivalence. |
| Preparation | Equivalence remains unknown under the current comparator. Shared solvent alone cannot establish similarity. |
| Outcome | Explicit endpoint difference where the narrow rule applies; otherwise alignment remains unestablished. No symptom-to-disease inference. |
| Study setting | Setting recorded for the extracted experiment. |
| Experimental finding | Recorded favourable, null or condition-dependent result, independent of claim comparability. |

Counts are experimental units, not independent studies. Unique publication counts are shown separately per account; neither should be summed across accounts as independent evidence. Conflicting or different results retain separate buckets. A missing indexed experiment means none in this collection. An unresolved plant name blocks species retrieval and is shown explicitly.

Dimension summaries are automated. Recorded human judgments apply to the overall pair and are displayed separately with provenance. A human pair review does not verify every matrix cell. Both reviewers have 20 completed assisted comparison judgments with matching labels. These are not independent blinded annotations. This change does not alter review decisions or source records.

## Interaction

Search account names, IDs, attribution and use text. The setting filter selects accounts with at least one experiment in that setting; cells retain all evidence for the selected accounts. The missing-preparation filter selects accounts whose traditional preparation is absent. Selecting a cell filters the explorer to its experimental units; clearing the drill-down restores the account's extracted results. Selecting an account with only literature leads exposes those leads.

Citations, excerpts, passage locations, source rights and limitations remain accessible in the existing source disclosures. Missing information remains unknown.

## Retrieval extension boundary

The export identifies the retrieval provider and version. Default provider: lexical baseline; semantic and hybrid challengers are available through the ranking selector. The aggregator consumes returned evidence records, not retrieval scores, and uses the same comparisons as the explorer. Changing candidate ordering must not change dimension judgments.

If justified by reviewed retrieval errors and time, a semantic challenger can rank passages and return evidence IDs and scores to this boundary. Keep the scientific-name gate explicit, retain the lexical baseline, record the model and corpus versions, and avoid sending restricted source material to external services. Semantic similarity must never imply preparation or medical endpoint equivalence.

Evaluate candidate relevance separately from comparability and result direction. Use reviewed relevance judgments, fixed candidate pools and source-group-aware evaluation. The existing small connected development set does not support an independent generalization claim. No model was trained for the atlas. A later pretrained semantic challenger is documented in [semantic retrieval methods](semantic_retrieval.md).

## Verification

Python tests pass, including atlas checks for preserving part differences, excluding leads from finding counts, retaining unresolved accounts, separating units from publications, and keeping comparison summaries independent of ranking scores. JavaScript syntax validation and `node tests/test_web.cjs` pass. The latter checks the renderer and event handlers with a mock DOM, including filtering, drill-down, clearing and empty states; it is not a browser layout check. In a subsequent live check, “Different part” opened E004 under all three rankers and its citation opened the intended PMC URL. The integration browser suite subsequently confirmed nine cited-report downloads across three viewport widths and all three rankers.

## Display wording and navigation

The account column stays visible during horizontal scrolling, with a visible scrolling hint. Missing traditional preparation is described as absent from the record; this does not assert absence from the original source. Unresolved outcome alignment is labelled as an unresolved use–outcome relationship. Review counts report how many people have reviewed each comparison, without repeated pending-review notices. Underlying review records and completion status are unchanged.

## Gap explanations

`scripts/gaps.py` derives explanations and next actions from the same indexed results. Empty preparation fields are labelled `not_recorded_source_status_unresolved`; they are never automatically labelled absent from the source. Literature leads use `not_yet_extracted`. Outcome relationships are distinct from missing extraction fields. Every evidence ID in an explanation resolves to a candidate with a source citation. Selecting a preparation, outcome, part or setting bucket expands related explanations.

Source notes from `data/curated/targeted_extractions.jsonl` are displayed separately, with extraction depth, citations, locators, rights and limitations. The complete methods/table inspection of TX001 and partial indexed-section inspection of TX002 are not human verification, new clinical findings, or automatically validated traditional recipes. They are excluded from atlas experimental counts and the frozen development comparisons.

## Supplementary source evidence

Each account's gaps section displays its supplementary missing-field audit entries, including related experimental entries where indexed. Values from related sources, the original recorded value, source context, supporting URLs and locators, and limits remain distinct. Null original fields remain null. The same notes appear in downloaded evidence reports. These display changes do not alter comparison rules, frozen ranking inputs, or human decisions.

Targeted extraction cards and reports show the recorded verification status, reviewer, inspected sections and assisted provenance. A confirmed source packet is not labelled as an independent blinded review.
