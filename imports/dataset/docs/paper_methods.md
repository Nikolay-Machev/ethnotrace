> Historical screening context: source extraction expanded in version 0.7. See [the extraction report](extraction_report.md) for current records and the corrected Larix finding.

# Publication selection and limits

The initial collection added 49 publications to support comparisons between Canadian traditional plant-use accounts and modern research on glucose regulation or diabetes-related complications. The publication catalogue is an intermediate dataset. It does not yet provide verified claim–study pairs or a complete extraction of each experiment.

## Discovery

Europe PMC core records supplied bibliographic metadata and indexed abstracts on 30 October 2026. Searches combined Canadian ethnobotanical terms, Cree and Eeyou Istchee attribution, and selected plant names with diabetes, glucose and insulin terms. Exact queries and retrieval counts are in `data/paper_search_manifest.json`.

The search union contained 541 distinct indexed records. Broad queries returned at most 100 results each; more focused title/abstract queries recovered directly relevant older papers. The discovery pool was screened for suitable publications, and the 49 included abstracts were read and annotated. The remaining pool has not received complete abstract-level adjudication. This is not an exhaustive systematic review, and the counts are not a PRISMA flow diagram.

## Selection

Priority went to original ethnobotanical research with Canadian attribution, experiments explicitly connected to the Canadian traditional pharmacopoeia, and studies that permit comparisons of plant part, extraction method, model or measured outcome. Relevant null results were retained. Analytical and interaction studies were included when they help interpret comparability or uncertainty.

| Tier | Count | Purpose |
| --- | ---: | --- |
| `core` | 33 | Central ethnobotanical, glucose-related or complication-related studies; includes small human studies with limitations |
| `supporting` | 9 | Composition, variability, permeability, safety and drug-metabolism context |
| `context` | 7 | Broader ethnobotany, reviews and secondary analysis; not independent efficacy replication |
| `provisional_species` | 2 | Rhus typhina studies potentially relevant to vinaigrier, pending botanical identification of the traditional record |

Tier describes relevance, not study quality. No numerical quality score or formal risk-of-bias assessment has been assigned. Having a PMID, appearing in a journal, or having a detailed abstract does not establish that the study is reliable.

Unrelated cancer, antimicrobial and environmental-contaminant studies were not selected merely because they shared a plant or community name. Studies of other sumac species were not substituted for Rhus typhina. Research involving isolated compounds was distinguished from whole extracts and traditional preparations.

## Recommended first comparisons

- **P26263160:** ethanol versus hot-water extracts; directly tests whether laboratory extraction changes activity.
- **P26626246:** pitcher-plant leaf decoction versus ethanol chemistry; compositional comparison rather than clinical proof.
- **P23216659:** pitcher-plant leaf versus root; a useful plant-part difference with a null root result.
- **P16979328:** blueberry plant parts in cell assays; T005's common-name identity still needs resolution.
- **P19303751:** blueberry fractions with and without a delivery excipient; a clear formulation difference.
- **P30669469 / P32153825:** controlled human blueberry studies with null glycaemic findings; fruit differs from T005's branches.
- **P21249104:** devil's-club tea pilot with no detected hypoglycaemic effect; four participants and no adequate basis for a definitive efficacy conclusion.

## Extraction rules

A publication can include multiple plants, preparations, assays, animal protocols or cohorts. Do not expand a publication into experimental records until those units and their source passages have been verified. Papers from the same programme may share data or cohorts; a later paper is not automatically independent replication.

Scientific names in `species` are those explicitly identified during abstract review. Lists may contain only highlighted species, not the entire experimental panel. `original_plant_name` in this table preserves these publication names; it is not an extracted historical or Indigenous-language plant name. Missing plant part or preparation remains null. Author affiliations do not establish the origin of a traditional practice.

The short `supporting_passage` is a verbatim retrieval anchor from the indexed abstract. It does not substantiate every annotated field on its own. The outcome summary and limitations are curator paraphrases based on the abstract. Full text, tables, supplementary information and primary traditional-use attribution must be reviewed before fine-grained matching.

## Coverage gaps

The current scientific collection is concentrated in Eeyou Istchee because this search found a substantial, directly linked experimental programme there. This does not represent the full diversity of Indigenous knowledge in Canada. Saanich, Cowichan and Gitksan publications are included as contextual sources, with diabetes-specific attribution gaps made explicit.

No additional settler ethnobotanical journal paper was verified in this batch. T005 and T006 remain the documented French-Canadian and Franco-Ontarian records. Their species are unresolved, so no scientific paper is marked as a verified match. The Acadian book remains an unverified lead.

Older titles worth retrieving separately include PMID 18128670 (1949, Rhus typhina), PMID 20321017 (1938, devil's club) and PMID 6876853 (1983, devil's club). Metadata was located but no indexed abstract was available. They are not included among the 49 screened papers and no findings were inferred from their titles.

## Rights and review

Full abstracts and PDFs are not redistributed. Each record contains bibliographic facts, curator summaries and a quotation of no more than 20 words. An indexed open-access flag and an indexed licence are separate fields; neither replaces checking the applicable publisher terms. A PMC link does not necessarily indicate an open reuse licence.

Citations preserve all authors supplied in the indexed author list. The indexed publication year is retained separately from first-publication date because online and issue dates can differ. Publication-status fields reflect only the retrieved API metadata; an independent retraction/correction check has not been completed.

All records were curated with AI assistance and await independent review. Laboratory signals and animal findings are not established medical effects in humans. Publicly indexed traditional knowledge still requires appropriate provenance, community attribution and attention to access conditions.

## Classification update (version 0.5)

Two contextual clinical blueberry publications were added, bringing the total to 51. Their glycaemic endpoints had no detected benefit, while some other endpoints were favourable. The exact supplemental query, source identifiers and correction notice are recorded in the search manifest. The initial discovery-union count has not been recomputed for supplemental-search overlap.

All publications have question-specific provisional labels; see [Study classifications](study_classification.md). These are screening annotations, not validated training pairs. Complete full-text review remains pending, although selected preparation/methods sections and the relevant correction were additionally inspected for the new records.
