# Human-reviewed retrieval comparison

Generated, do not edit. Run python scripts/rebuild.py.

2 complete accounts; 10 account–candidate pairs; 6 judged useful.

Assisted development review, not a held-out test. Source depth varies. A useful study need not support the traditional claim.

Precision@5 uses five slots, including unfilled slots for short pools. Recall@5 uses all judged-useful candidates in the indexed pool. Metrics are macro averages with equal weight per complete account.

| Method | Precision@5 | Recall@5 | MRR |
| --- | ---: | ---: | ---: |
| lexical | 0.500 | 0.875 | 0.500 |
| semantic | 0.500 | 0.875 | 1.000 |
| hybrid | 0.600 | 1.000 | 1.000 |

## T009

2 useful of 4 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 2 | 0.400 | 1.000 | None |
| semantic | 2 | 0.400 | 1.000 | None |
| hybrid | 2 | 0.400 | 1.000 | None |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E005 | 2 | 2 (+0) | 3 (-1) |
| P20738101 | 3 | 1 (+2) | 1 (+2) |

Positive change means moving up relative to lexical ranking.

### E005

Its ethanolic Sorbus decora extract in food (about 200 mg/kg/day, 7 days, KK-Ay mice, n=6) shows a serial blood-glucose change with no significance assigned in the figure, so it gives an in vivo glucose outcome whose strength is weak and differs from the abstract's claim and from the paper's signifi…

Vianna R; Brault A; Martineau LC; Couture R; Arnason JT; Haddad PS. In Vivo Anti-Diabetic Activity of the Ethanolic Crude Extract of Sorbus decora C.K.Schneid. (Rosacea): A Medicinal Plant Used by Canadian James Bay Cree Nations to Treat Symptoms Related to Diabetes. Evidence-based complementary and alternative medicine : eCAM. 2011;2011:237941. doi:10.1093/ecam/nep158. PMID:19887507.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/

- full text: Methods, Results 3.3, Figure 7, Discussion (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/

### P20738101

This paper helps compare the activity of fractions and isolated compounds from Sorbus decora bark, the traditionally used part, by bioassay-guided antidiabetic testing, so it speaks to a glucose-related outcome and to which constituents of the bark extract carry the effect.

Guerrero-Analco JA; Martineau L; Saleem A; Madiraju P; Muhammad A; Durst T; Haddad P; Arnason JT. Bioassay-guided isolation of the antidiabetic principle from Sorbus decora (Rosaceae) used traditionally by the Eeyou Istchee Cree First Nations. Journal of natural products. 2010;73(9):1519-1523. doi:10.1021/np1003005. PMID:20738101.
https://pubmed.ncbi.nlm.nih.gov/20738101/

- full text of a plain-language lay summary of the paper (Cree Board of Health), not the journal abstract or paper: https://www.creehealth.org/sites/default/files/FRP-019-5-04-X%20Guerrero%202010-03-01%20%28PlainLanguage%29.pdf


## T012

4 useful of 6 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 3 | 0.600 | 0.750 | P25916863 |
| semantic | 3 | 0.600 | 0.750 | P26508979 |
| hybrid | 4 | 0.800 | 1.000 | None |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E010 | 5 | 4 (+1) | 5 (+0) |
| P25916863 | 6 | 3 (+3) | 3 (+3) |
| P26508979 | 3 | 6 (-3) | 4 (-1) |
| P26707751 | 2 | 1 (+1) | 1 (+1) |

Positive change means moving up relative to lexical ranking.

### E010

Labrador tea hot-water extract raised muscle-cell glucose uptake about as strongly as the ethanol extract in a 17-species screen, so it supports a preparation comparison closer to traditional tea use.

Shang N; Saleem A; Musallam L; Walshe-Roussel B; Badawi A; Cuerrier A; Arnason JT; Haddad PS. Novel Approach to Identify Potential Bioactive Plant Metabolites: Pharmacological and Metabolomics Analyses of Ethanol and Hot Water Extracts of Several Canadian Medicinal Plants of the Cree of Eeyou Istchee. PloS one. 2015;10(8):e0135721. doi:10.1371/journal.pone.0135721. PMID:26263160.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

- full text: Methods, Table 1, glucose-uptake Results, Figure 1 (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

### P25916863

This paper helps compare the documented antidiabetic use against direct in vivo outcomes (fasting blood glucose, oral glucose tolerance, plasma insulin, and Akt/GLUT4 signaling) in obese insulin-resistant mice given Rhododendron groenlandicum extract at three doses, though I could not confirm the pl…

Ouchfoun M; Eid HM; Musallam L; Brault A; Li S; Vallerand D; Arnason JT; Haddad PS. Labrador tea (Rhododendron groenlandicum) attenuates insulin resistance in a diet-induced obesity mouse model. European journal of nutrition. 2016;55(3):941-954. doi:10.1007/s00394-015-0908-z. PMID:25916863.
https://pubmed.ncbi.nlm.nih.gov/25916863/

- abstract and metadata only; the paywalled Methods, Results and Discussion were not visible: https://link.springer.com/doi/10.1007/s00394-015-0908-z

### P26508979

This paper compares how the adipogenic activity (glitazone-like, 3T3-L1 cell assay) of ethanol extracts of Rhododendron groenlandicum leaves varies across wild populations and with quercetin content, so it compares collection sites rather than plant parts or preparations and measures no glucose or i…

Rapinski M; Musallam L; Arnason JT; Haddad P; Cuerrier A. Adipogenic Activity of Wild Populations of Rhododendron groenlandicum, a Medicinal Shrub from the James Bay Cree Traditional Pharmacopeia. Evidence-based complementary and alternative medicine : eCAM. 2015;2015:492458. doi:10.1155/2015/492458. PMID:26508979.
https://pubmed.ncbi.nlm.nih.gov/26508979/

- abstract-level summary only, from a database aggregator: https://search.emarefa.net/ar/detail/BIM-1062378-adipogenic-activity-of-wild-populations-of-rhododendron-groe
- truncated abstract snippet only: https://openaccess.library.uitm.edu.my/Record/doaj-5b178100975c46de94da4326402b5955
- None: None

### P26707751

This paper helps compare preparations of Labrador tea by testing an 80% ethanol extract, its chromatographic fractions and the isolated compounds (+)-catechin and (-)-epicatechin in an adipogenesis assay, showing that the activity sits in a catechin pair and not in either compound alone.

Eid HM; Ouchfoun M; Saleem A; Guerrero-Analco JA; Walshe-Roussel B; Musallam L; Rapinski M; Cuerrier A; Martineau LC; Arnason JT; Haddad PS. A combination of (+)-catechin and (-)-epicatechin underlies the in vitro adipogenic action of Labrador tea (Rhododendron groenlandicum), an antidiabetic medicinal plant of the Eastern James Bay Cree pharmacopeia. Journal of ethnopharmacology. 2016;178:251-257. doi:10.1016/j.jep.2015.12.021. PMID:26707751.
https://pubmed.ncbi.nlm.nih.gov/26707751/

- abstract only (a library summary page): https://creehealth.org/about-us/departments/research-office/research-library/combination-catechin-and-epicatechin

## Exclusions

Entire accounts are excluded when any candidate lacks a confirmed decision. Provisional, unresolved and missing decisions are not treated as negatives.

- T007: P18066122 (unresolved).
- T008: P21186373 (unresolved), P26626249 (unresolved).
- T010: P20301057 (provisional).
- T011: P19526043 (unresolved).
- T013: CL12843638 (missing), CL39426763 (missing).
- T014: CL12843638 (missing), CL39426763 (missing).

## Interpretation

These results describe the frozen rankers on the existing development corpus. Small candidate pools and repeated papers across accounts limit interpretation. No significance or generalization claim is made. Lexical remains the default. Rank changes do not alter experimental findings or comparability judgments.

Model: sentence-transformers/all-MiniLM-L6-v2; revision: 1110a243fdf4706b3f48f1d95db1a4f5529b4d41.
Ranking-input SHA-256: 20ffbdee6867cd487a33aa6486b9923daac564a9e8b6872f9f6aba41f208309d.
