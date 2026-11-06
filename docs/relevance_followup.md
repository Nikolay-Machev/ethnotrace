# Source follow-up and reviewer decisions

This follow-up checked the author abstracts indexed in Europe PMC (4 November 2026). It is assistant research for the reviewer. It does not change the human judgments, the experimental index or any retrieval metric.

| Pair | What the primary abstract establishes | What remains to check |
| --- | --- | --- |
| T007 / [Fraser et al., PMID 18066122](https://europepmc.org/article/MED/18066122) | Tamarack is identified in an antioxidant screen. The authors discuss plant-part effects across the collection. | The abstract does not show a within-tamarack part or preparation comparison. Check the species-level methods and table before counting it as relevant under the narrow rule. |
| T010 / [Martineau et al., PMID 20301057](https://europepmc.org/article/MED/20301057) | The material was **inner bark**. In 3T3-L1 cells the authors report poplar-specific differentiation and proliferation findings, distinguish them from alder results, and discuss PPAR-γ activity. | This supplies the missing poplar-specific outcome. It is a cellular adipogenesis study, not a direct glucose endpoint. Given the reviewer's inclusion of adipogenesis as a mechanistic outcome for other accounts, this is a candidate for a reviewer-confirmed useful decision. Do not infer a traditional preparation match. |
| T011 / [Harbilas et al., PMID 19526043](https://europepmc.org/article/MED/19526043) | Lingonberry is named among nine species screened and singled out in the abstract. | The reported assay counts are pooled across species. The abstract does not identify which outcome belongs to lingonberry or establish the tested plant part. Check the results table before deciding. |

## Reviewer follow-up, 4 November 2026

**T010/P20301057: useful (provisional).** The reviewer accepts adipogenesis as a diabetes-related mechanism consistently with other reviews. The target abstract was blocked; the reviewer relied on the assistant description and a [secondary chapter](https://link.springer.com/chapter/10.1007/978-3-319-04045-5_4/fulltext.html). Inner bark and solvent were not independently confirmed. The provisional decision is excluded from confirmed relevance metrics.

**T007/P18066122: unresolved.** Scilit abstract summary only; species-specific tables were not reached. Partial access to [Fraser’s 2006 thesis](https://escholarship.mcgill.ca/downloads/7s75dc76x) did not establish a within-tamarack part/preparation comparison. A different dataset cannot supply this paper’s results.

**T011/P19526043: unresolved.** Scilit summary names lingonberry but does not map assays to species. Part, preparation and assay results remain unverified. Do not import berries or 80% ethanol from later studies. A glucose-uptake endpoint would be diabetes-related, not a direct test of frequent urination.

The primary-abstract descriptions above are assistant research, not primary sources independently read by the human reviewer. No full-text verification is claimed. Earlier judgments are preserved in review history. Confirmed evaluation remains 30 of 33 decisions; one provisional and two unresolved cases are excluded.


## Primary publication follow-up, 5 November 2026

The supplemental [five-pair source assessment](../data/review/retrieval_relevance_source_followup_2026-11-05.jsonl) documents source-supported dispositions for the five pairs whose joint human reviews were unfinished or inconsistent. **These are assistant literature assessments, not new judgments authored or approved by Nikolay Machev or Alex Karadjov.** The named review submissions, unresolved/provisional states and generated human ranking metrics are preserved. Each of the 10 corresponding rows in `retrieval_relevance.jsonl` includes an `assistant_source_followup` object with evidence and status provenance.

| Pair | Primary-source assessment | Why |
| --- | --- | --- |
| T007 / P18066122 | Useful source evidence (true, pending reviewer confirmation) | Fraser et al. (2007), Table 1, reports *Larix laricina* bark from Mistissini and cambium from Whapmagoostui, with different antioxidant rankings. Methods reports 80% ethanol extraction. Useful within-species material/collection context. Differences in part and collection site are confounded, and antioxidant activity is not blood-glucose evidence. |
| T008 / P21186373 | Not comparison-relevant (false, already confirmed by Nikolay) | Tam et al. (2011), PubMed abstract: CYP3A4 drug-interaction/safety findings, not infection-healing outcome or a direct plant-part/preparation comparison. The prior safety-context scope rule applies. Alex's original unresolved submission remains intact. |
| T008 / P26626249 | Not comparison-relevant (false, already confirmed by Nikolay) | Cieniak et al. (2015), Abstract and Methods: intestinal-cell microarray and CYP transcript safety, not infection healing or comparative preparations. Alex's original unresolved submission remains intact. |
| T010 / P20301057 | Useful source evidence (true, pending reviewer confirmation) | Martineau et al. (2010), primary abstract: *Populus balsamifera* inner-bark extract inhibits 3T3-L1 adipogenesis and antagonizes PPAR-γ. This supports the project's mechanistic-relevance scope, not the traditional preparation or a clinical effect. |
| T011 / P19526043 | Useful source evidence (true, pending reviewer confirmation) | Harbilas et al. (2009), Table 1, Plant Materials, and Results: *Vaccinium vitis-idaea* berries, 80% ethanol laboratory extraction, increased basal and insulin-stimulated glucose uptake in C2C12 and 3T3-L1 cells. This is diabetes-related mechanism evidence but not a direct test of frequent urination. |

Original paper access:

- Fraser et al. (2007), [full manuscript](https://drpatrickowen.com/wp-content/uploads/2016/09/d38d03_dde8f25c8ca74ddc87e266527a84ab01.pdf), journal pp. 1202–1207.
- Tam et al. (2011), [author abstract](https://pubmed.ncbi.nlm.nih.gov/21186373/).
- Cieniak et al. (2015), [author abstract](https://pubmed.ncbi.nlm.nih.gov/26626249/), [full paper](https://neurolipidomics.com/assets/pubs/2015_cieniak_therapeutics.pdf).
- Martineau et al. (2010), [author abstract](https://pubmed.ncbi.nlm.nih.gov/20301057/).
- Harbilas et al. (2009), [full manuscript](https://www.neurolipidomics.com/assets/pubs/2009_harbilas_therapeutics.pdf), journal pp. 481–486.

PDF text and document structure were accessible for the two complete manuscript follow-ups, but the remote PDF screenshot service returned cache-miss errors. The reported numerical results were checked against the primary text extraction, not visual inspection of figures. The original reviewer submissions remain separate because an assistant research pass does not independently establish the reviewers' final decisions.

To finalize the **two-reviewer human-relevance benchmark**, each reviewer must explicitly adopt or correct the source-backed assessments for any originally pending/provisional cases. Then update the `human_*` fields, retain original review history and assistant exposure disclosures, and rebuild. The source-based recommendations alone must never be silently counted as finalized named human judgments.
