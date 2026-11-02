> Historical screening context: source extraction expanded in version 0.7. See [the extraction report](extraction_report.md) for current records and the corrected Larix finding.

# Study classifications

All 51 publications have one provisional screening category, an explicit question and a rationale in `data/papers.jsonl`. Full citations remain in [the bibliography](papers.md) and each publication record. The two added clinical comparators are P26024297 and P31136659. A linked correction is documented but is not counted as another study.

**These are study-question screening labels, not validated traditional-claim–study labels.** Support means support for the specified experimental outcome in the specified model, including laboratory proxies. It does not establish that a Canadian traditional preparation works in people. Comparability to T005 and T006 remains unadjudicated.

The requested five-per-category minimum is met at this screening level. It is not met for independently reviewed training pairs: there are currently zero validated pairs. Every classification has `training_eligible: false` pending verification.

| Category | Publications |
| --- | ---: |
| Support | 12 |
| No detected effect | 5 |
| Mixed evidence | 16 |
| Not directly comparable | 10 |
| Insufficient evidence | 8 |

## Rules

- Classify against the written question, not the title or the overall tone of the paper. A different question can yield a different category.
- Support: a favourable measured effect on the specified experimental target. Model, organ, solvent and formulation limits remain attached.
- No detected effect: no demonstrated improvement on the specified glucose or insulin endpoint. Other outcomes can still be positive; this category does not mean proof of no effect.
- Mixed evidence: the stated question spans conditions, compounds, organs or related endpoints and the reported results differ. This does not automatically mean conflicting independent studies.
- Not directly comparable: the tested preparation or endpoint does not directly answer the written traditional-use or glucose-regulation question. This includes analytical and interaction studies that remain useful context.
- Insufficient evidence: the available material cannot establish the comparison, or the item is a survey, review or secondary analysis without independently extracted primary efficacy results. It is not a claim that no evidence exists elsewhere.

Questions were selected for their relevance to the paper and EthnoTrace. These categories combine outcome direction, comparability and information sufficiency; they are useful screening tags but should not be used as a single efficacy target without further annotation. A later training schema should record these dimensions separately.

## Additional null-outcome studies

P26024297 reports no difference in insulin sensitivity after six weeks of mixed-species blueberry smoothies. P31136659 reports unchanged insulin resistance after six months. Both report other favourable outcomes. They are contextual fruit studies, not verified matches to the water-scalded blueberry branches in T005. Their addition does not identify the species in that historical account.

P31136659 has a published corrigendum (PMID 31667509; DOI 10.1093/ajcn/nqz214) correcting Table 2 insulin units to mU/L. The correction was inspected and is linked in the dataset. It is not counted as an independent experiment.

## Support

| Publication | Question | Reason |
| --- | --- | --- |
| [P22542642](https://pubmed.ncbi.nlm.nih.gov/22542642/) — Shang N (2012) | Do isolated Larix constituents stimulate adipogenesis in the tested cell model? | Active constituents increased the measured adipogenesis proxy; this does not establish human glucose lowering. |
| [P22738356](https://pubmed.ncbi.nlm.nih.gov/22738356/) — Muhammad A (2012) | Do the reported pitcher-plant constituents affect muscle glucose uptake or hepatic glucose production in vitro? | Active constituents were identified with effects on those cell-based endpoints; the inference is limited to those preparations and assays. |
| [P19887507](https://pubmed.ncbi.nlm.nih.gov/19887507/) — Vianna R (2011) | Does Sorbus extract improve glucose-related measures in the reported animal models? | The abstract reports glycaemic effects across several animal models; timing and magnitude vary and no human effect is established. |
| [P22504062](https://pubmed.ncbi.nlm.nih.gov/22504062/) — Harbilas D (2012) | Does Populus extract improve metabolic measures in the eight-week mouse experiment? | Favourable glycaemic and insulin-resistance measures were reported; reduced intake may contribute. |
| [P23781256](https://pubmed.ncbi.nlm.nih.gov/23781256/) — Harbilas D (2013) | Do Populus extract and salicortin improve metabolic indicators after obesity induction in mice? | Favourable metabolic changes were reported in the treatment protocol, with an intake-related interpretation limit. |
| [P20301057](https://pubmed.ncbi.nlm.nih.gov/20301057/) — Martineau LC (2010) | Do the two bark extracts inhibit adipogenesis in the reported cell system? | Both affected the adipogenesis endpoint through different mechanisms; this is a cellular proxy rather than proof of clinical benefit. |
| [P25916863](https://pubmed.ncbi.nlm.nih.gov/25916863/) — Ouchfoun M (2016) | Does Labrador-tea extract improve glycaemia and insulin-sensitivity measures in diet-induced obese mice? | The reported mouse experiment detected favourable changes in those measures. |
| [P31215420](https://pubmed.ncbi.nlm.nih.gov/31215420/) — Downing AD (2019) | Do the tested black-spruce organs protect PC12 cells from glucose toxicity? | The extracts showed cytoprotection, with potency varying by organ and environment; no clinical neuropathy outcome was measured. |
| [P29378549](https://pubmed.ncbi.nlm.nih.gov/29378549/) — Li S (2018) | Do selected extracts protect kidney cells against the imposed hypertonic stress? | Some extracts showed cytoprotective and anti-apoptotic effects; hypertonicity is an indirect diabetic-complication model. |
| [P26164238](https://pubmed.ncbi.nlm.nih.gov/26164238/) — Nachar A (2015) | Do isolated balsam-fir compounds modulate hepatic glucose-related enzymes in vitro? | The identified compounds affected the reported enzyme and signalling endpoints in the experimental system. |
| [P25013446](https://pubmed.ncbi.nlm.nih.gov/25013446/) — Eid HM (2014) | Does lingonberry extract lower glycaemia in the reported obese-mouse model? | Lower glycaemia and associated signalling changes were reported for the extract-treated mice. |
| [P19085814](https://pubmed.ncbi.nlm.nih.gov/19085814/) — McIntyre KL (2009) | Do the tested blueberry extracts inhibit glycation, with plant-part and seasonal variation? | The study reports measurable antiglycation activity and variation; this is not evidence of clinical glucose reduction. |

## No detected effect

| Publication | Question | Reason |
| --- | --- | --- |
| [P30669469](https://pubmed.ncbi.nlm.nih.gov/30669469/) — Stote K (2019) | Does the blueberry meal improve postprandial glucose metabolism versus matched placebo in healthy adults? | No significant glucose-metabolism change was detected; a separate pancreatic-polypeptide result does not change this glucose-specific label. |
| [P32153825](https://pubmed.ncbi.nlm.nih.gov/32153825/) — Stote KS (2017) | Does seven-day wild-blueberry juice intake improve fasting glucose, insulin or insulin sensitivity versus placebo? | No significant change in those glycaemic measures was detected in the small crossover trial. |
| [P21249104](https://pubmed.ncbi.nlm.nih.gov/21249104/) — Thommasen HV (1990) | Does devil's-club tea lower measured glucose in the four-person pilot? | The pilot did not detect a hypoglycaemic effect; its size and design do not establish absence of benefit generally. |
| [P31136659](https://pubmed.ncbi.nlm.nih.gov/31136659/) — Curtis PJ (2019) | Does six-month blueberry intake improve insulin resistance versus matched placebo in adults with metabolic syndrome? | The primary insulin-resistance endpoint was unchanged; favourable vascular or lipid results do not change this endpoint-specific label. |
| [P26024297](https://pubmed.ncbi.nlm.nih.gov/26024297/) — Stull AJ (2015) | Does six-week blueberry-smoothie intake improve insulin sensitivity versus placebo in adults with metabolic syndrome? | Insulin sensitivity did not differ between groups; the positive endothelial-function result concerns a different endpoint. |

## Mixed evidence

| Publication | Question | Reason |
| --- | --- | --- |
| [P22888363](https://pubmed.ncbi.nlm.nih.gov/22888363/) — Harbilas et al. (2012) | Are glycaemic results consistent between prevention and treatment? | No significant prevention effect, but lower treatment glycaemic AUC; full-text Results 3.1 and Figure 1. |
| [P17111029](https://pubmed.ncbi.nlm.nih.gov/17111029/) — Spoor DC (2006) | Are glucose-related and other antidiabetic screening effects consistent across the tested endpoints? | Some cellular effects were detected but insulin secretion was not enhanced; species and endpoints must be separated. |
| [P19526043](https://pubmed.ncbi.nlm.nih.gov/19526043/) — Harbilas D (2009) | Are the nine plants consistently active across the antidiabetic screening endpoints? | Several assays were positive while no species increased insulin secretion. |
| [P26263160](https://pubmed.ncbi.nlm.nih.gov/26263160/) — Shang N (2015) | Do hot-water and ethanol preparations retain the same glucose-related activity? | Activity was retained, lost or changed according to plant and extraction method. |
| [P23864882](https://pubmed.ncbi.nlm.nih.gov/23864882/) — Nachar A (2013) | Do the tested plant extracts consistently modulate hepatic glucose production and storage? | Effects differed among species and between glucose-6-phosphatase and glycogen-synthase endpoints. |
| [P20804840](https://pubmed.ncbi.nlm.nih.gov/20804840/) — Nistor Baldea LA (2010) | Is inhibition of glucose uptake consistent across the screened extracts and models? | Only a subset of extracts inhibited uptake or reduced rat peak glycaemia; model and species effects differ. |
| [P23216659](https://pubmed.ncbi.nlm.nih.gov/23216659/) — Harris CS (2012) | Do leaf and root preparations protect PC12 cells equally from glucose-associated cell loss? | The leaf preparation was protective while the root preparation was not. |
| [P20738101](https://pubmed.ncbi.nlm.nih.gov/20738101/) — Guerrero-Analco JA (2010) | Do all three newly isolated Sorbus compounds enhance muscle-cell glucose uptake? | One was active and two were not under the tested conditions. |
| [P26916332](https://pubmed.ncbi.nlm.nih.gov/26916332/) — Li S (2016) | Are the renal endpoints consistently improved by Labrador-tea treatment in mice? | Fibrosis and steatosis findings were favourable but albuminuria improvement was a tendency rather than a demonstrated significant effect. |
| [P26707751](https://pubmed.ncbi.nlm.nih.gov/26707751/) — Eid HM (2016) | Do individual catechins reproduce the full extract's adipogenic activity? | Individual constituents did not reproduce the full activity, whereas their combination came closer. |
| [P26508979](https://pubmed.ncbi.nlm.nih.gov/26508979/) — Rapinski M (2015) | Do population-level chemical differences translate consistently into adipogenic activity patterns? | Extracts were active but a spatial activity pattern was not detected; chemistry and activity did not align simply. |
| [P20087853](https://pubmed.ncbi.nlm.nih.gov/20087853/) — Eid HM (2010) | Do quercetin derivatives reproduce the same uptake and mitochondrial mechanism? | Glucose uptake was stimulated but mitochondrial effects differed between glycosides and aglycone. |
| [P19927274](https://pubmed.ncbi.nlm.nih.gov/19927274/) — Beaulieu LP (2010) | Are the tested lingonberry constituents consistently antiglycating? | Three selected phenolics were active while para-coumaric acid was not. |
| [P18066122](https://pubmed.ncbi.nlm.nih.gov/18066122/) — Fraser MH (2007) | Is the association between traditional importance and antioxidant activity consistent in both communities? | The association was significant in one community but not the other; antioxidant activity itself is not direct glycaemic evidence. |
| [P16979328](https://pubmed.ncbi.nlm.nih.gov/16979328/) — Martineau LC (2006) | Are effects consistent across blueberry organs and cell-based antidiabetic endpoints? | The reported effects depended on the plant part and assay; they cannot be collapsed into a universal blueberry effect. |
| [P19303751](https://pubmed.ncbi.nlm.nih.gov/19303751/) — Grace MH (2009) | Are blueberry fractions hypoglycaemic with and without the delivery excipient? | Activity was detected with Labrasol but was not significant without it. |

## Not directly comparable

| Publication | Question | Reason |
| --- | --- | --- |
| [P26626246](https://pubmed.ncbi.nlm.nih.gov/26626246/) — Cieniak C (2015) | Does the chemistry comparison directly establish glucose control from the traditional decoction? | It compares composition rather than measuring glucose control; chemical similarity alone does not establish equal efficacy. |
| [P27773798](https://pubmed.ncbi.nlm.nih.gov/27773798/) — Yong Y (2016) | Does the antioxidant and permeability study directly test glucose regulation? | Antioxidant capacity and transport across a cell monolayer do not measure glucose control. |
| [P27833811](https://pubmed.ncbi.nlm.nih.gov/27833811/) — Bailie A (2016) | Does the geographic Sorbus comparison directly demonstrate glucose regulation? | Gene expression and antioxidant capacity are not direct glucose-regulation outcomes. |
| [P19665535](https://pubmed.ncbi.nlm.nih.gov/19665535/) — Tam TW (2009) | Does CYP inhibition directly test the glucose-regulating traditional-use proposition? | Drug-metabolism inhibition is an interaction signal, not a glucose-lowering efficacy result. |
| [P21186373](https://pubmed.ncbi.nlm.nih.gov/21186373/) — Tam TW (2011) | Does mechanism-based CYP3A4 inhibition establish antidiabetic efficacy? | The enzyme interaction assay does not measure glucose regulation, regardless of whether inhibition is detected. |
| [P24184081](https://pubmed.ncbi.nlm.nih.gov/24184081/) — Cieniak C (2013) | Does the metabolism and transport study establish a glucose-lowering plant effect? | It addresses disposition of conventional drugs rather than plant efficacy; null transport results should remain separately identifiable. |
| [P20135709](https://pubmed.ncbi.nlm.nih.gov/20135709/) — Saleem A (2010) | Does the analytical method paper directly test a traditional antidiabetic effect? | Compound detection and method validation do not establish a therapeutic outcome. |
| [P17439018](https://pubmed.ncbi.nlm.nih.gov/17439018/) — Harris CS (2007) | Does plant-part chemical profiling establish antidiabetic efficacy? | Composition and analytical validation do not directly measure glucose regulation. |
| [P35861915](https://pubmed.ncbi.nlm.nih.gov/35861915/) — Sekowski S (2023) | Does the isolated sumac tannin test T006's boiled vinaigrier-cluster preparation? | Botanical identity remains unresolved, and an isolated tannin differs from the documented whole preparation. |
| [P32129622](https://pubmed.ncbi.nlm.nih.gov/32129622/) — Resetar M (2020) | Does receptor activation and docking directly demonstrate glucose lowering from devil's-club tea? | Isolated-compound target activity and mixed botanical origins do not directly test the tea or its glycaemic effect. |

## Insufficient evidence

| Publication | Question | Reason |
| --- | --- | --- |
| [P16297584](https://pubmed.ncbi.nlm.nih.gov/16297584/) — Leduc C (2006) | Does this survey establish an experimentally measured glucose-regulating effect? | It documents symptom-associated plant knowledge and prioritisation, not an experimental efficacy test. |
| [P26626249](https://pubmed.ncbi.nlm.nih.gov/26626249/) — Cieniak C (2015) | Does the microarray study establish overall antidiabetic efficacy or safety? | The null transcriptional mechanism result answers a narrow question and cannot establish clinical efficacy or overall safety. |
| [P40067068](https://pubmed.ncbi.nlm.nih.gov/40067068/) — Nazir M (2025) | Can this abstract support a reliable detailed match to T006? | The traditional species is unresolved and the abstract inconsistently identifies the experimental animals; full-text clarification is needed. |
| [P2345461](https://pubmed.ncbi.nlm.nih.gov/2345461/) — Turner NJ (1990) | Can the abstract establish a species-specific diabetes claim for matching? | Diabetes is mentioned but is not mapped to particular bark species in the inspected abstract. |
| [P16790066](https://pubmed.ncbi.nlm.nih.gov/16790066/) — Johnson LM (2006) | Can this abstract establish a plant-specific diabetes-use and experimental comparison? | The broad cultural analysis does not establish that specific comparison in the abstract. |
| [P22235232](https://pubmed.ncbi.nlm.nih.gov/22235232/) — Haddad PS (2012) | Is this review an independent primary experiment that can receive an efficacy outcome label? | It summarises a research programme; its experiments require original sources and must not be counted again. |
| [P35126097](https://pubmed.ncbi.nlm.nih.gov/35126097/) — Hall B (2021) | Does the secondary analysis supply independently extracted claim-specific efficacy results? | It reanalyses existing assays; endpoint-specific original results and independence need verification before efficacy labelling. |
| [P22101399](https://pubmed.ncbi.nlm.nih.gov/22101399/) — Calway T (2012) | Does the broad botanical review provide an independent diabetes-efficacy test? | The review is useful for locating original studies but is not itself an independent experimental test. |

## Review and evaluation

Classification uses the existing abstract-based annotations and current primary-source checks for the two new studies. Complete full-text and independent review are pending. Preserve the rationale and source with every exported label. Do not train on a rationale as an input when the task is to predict the label: it states the answer.

Split evaluation by publication and, where possible, shared cohort, source programme and related experiment. Do not split passages from the same study across training and test sets. Class counts are coverage checks, not a reason to relabel a result or treat multiple endpoints as independent studies.

## Full-text correction

P22888363 now has a mixed-evidence category: prevention glycaemia was not significantly changed, while treatment glycaemic AUC fell. E001 and E002 preserve the separate protocols. Any earlier support-row entry above is superseded by this correction and the machine-readable catalogue.
