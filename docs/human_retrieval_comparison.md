# Human-reviewed retrieval comparison

Generated, do not edit. Run python scripts/rebuild.py.

3 complete accounts; 16 account–candidate pairs; 10 judged useful.

Assisted development review, not a held-out test. Source depth varies. A useful study need not support the traditional claim.

Precision@5 uses five slots, including unfilled slots for short pools. Recall@5 uses all judged-useful candidates in the indexed pool. Metrics are macro averages with equal weight per complete account.

| Method | Precision@5 | Recall@5 | MRR |
| --- | ---: | ---: | ---: |
| lexical | 0.533 | 0.833 | 0.667 |
| semantic | 0.533 | 0.833 | 0.833 |
| hybrid | 0.600 | 0.917 | 1.000 |

## T008

4 useful of 6 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 3 | 0.600 | 0.750 | E004 |
| semantic | 3 | 0.600 | 0.750 | E003 |
| hybrid | 3 | 0.600 | 0.750 | E004 |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E003 | 3 | 6 (-3) | 4 (-1) |
| E004 | 6 | 5 (+1) | 6 (+0) |
| P22738356 | 2 | 2 (+0) | 2 (+0) |
| P26626246 | 1 | 3 (-2) | 1 (+0) |

Positive change means moving up relative to lexical ranking.

### E003

Its 80% ethanol leaf extract matches the documented part, and its PC12 cell result under 150 mM glucose (protection up to 30 micrograms/mL, none at 100) measures cell survival rather than slow-healing infection, so it helps compare part (match) and outcome (mismatch).

Harris CS; Asim M; Saleem A; Haddad PS; Arnason JT; Bennett SA. Characterizing the cytoprotective activity of Sarracenia purpurea L., a medicinal plant that inhibits glucotoxicity in PC12 cells. BMC complementary and alternative medicine. 2012;12:245. doi:10.1186/1472-6882-12-245. PMID:23216659.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3556504/

- full text: Background, Methods, Results, Figure 1: https://link.springer.com/content/pdf/10.1186/1472-6882-12-245.pdf

### E004

Its root extract had no appreciable protective effect at low concentrations and worsened cell loss near its IC50 (56 micrograms/mL), which exposes a plant-part mismatch with the documented leaf use and makes the leaf-versus-root contrast informative.

Harris CS; Asim M; Saleem A; Haddad PS; Arnason JT; Bennett SA. Characterizing the cytoprotective activity of Sarracenia purpurea L., a medicinal plant that inhibits glucotoxicity in PC12 cells. BMC complementary and alternative medicine. 2012;12:245. doi:10.1186/1472-6882-12-245. PMID:23216659.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3556504/

- full text: Methods, Results, Figure 1: https://link.springer.com/content/pdf/10.1186/1472-6882-12-245.pdf

### P22738356

It tests a leaf extract and then fractions and eleven isolated compounds in muscle and liver cells (glucose uptake, glucose-6-phosphatase), so it helps compare the documented leaf part and an extract-versus-isolated-compound gap, while its outcomes are cellular glucose handling, not slow-healing infection, and the abstract does not state the extraction solvent.

Muhammad A; Guerrero-Analco JA; Martineau LC; Musallam L; Madiraju P; Nachar A; Saleem A; Haddad PS; Arnason JT. Antidiabetic compounds from Sarracenia purpurea used traditionally by the Eeyou Istchee Cree First Nation. Journal of natural products. 2012;75(7):1284-1288. doi:10.1021/np3001317. PMID:22738356.
https://pubmed.ncbi.nlm.nih.gov/22738356/

- abstract only: https://core.ac.uk/works/49920640

### P26626246

It compares the boiling-water leaf decoction the authors describe as traditional with an 80% ethanol leaf extract chemically (phenolics and morroniside similar; betulinic and ursolic acids about 107 and 93 times higher in ethanol), so it helps compare preparation for the documented leaf, but it measures no infection-healing or glucose outcome.

Cieniak C; Walshe-Roussel B; Liu R; Muhammad A; Saleem A; Haddad PS; Cuerrier A; Foster BC; Arnason JT. Phytochemical Comparison of the Water and Ethanol Leaf Extracts of the Cree medicinal plant, Sarracenia purpurea L. (Sarraceniaceae). Journal of pharmacy & pharmaceutical sciences : a publication of the Canadian Society for Pharmaceutical Sciences, Societe canadienne des sciences pharmaceutiques. 2015;18(4):484-493. doi:10.18433/j35w27. PMID:26626246.
https://pubmed.ncbi.nlm.nih.gov/26626246/

- abstract only: https://journals.library.ualberta.ca/jpps/index.php/JPPS/article/view/25093


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

Its ethanolic Sorbus decora extract in food (about 200 mg/kg/day, 7 days, KK-Ay mice, n=6) shows a serial blood-glucose change with no significance assigned in the figure, so it gives an in vivo glucose outcome whose strength is weak and differs from the abstract's claim and from the paper's significant STZ and insulin-resistant rat arms; the part and traditional preparation are not compared.

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

This paper helps compare the documented antidiabetic use against direct in vivo outcomes (fasting blood glucose, oral glucose tolerance, plasma insulin, and Akt/GLUT4 signaling) in obese insulin-resistant mice given Rhododendron groenlandicum extract at three doses, though I could not confirm the plant part or solvent.

Ouchfoun M; Eid HM; Musallam L; Brault A; Li S; Vallerand D; Arnason JT; Haddad PS. Labrador tea (Rhododendron groenlandicum) attenuates insulin resistance in a diet-induced obesity mouse model. European journal of nutrition. 2016;55(3):941-954. doi:10.1007/s00394-015-0908-z. PMID:25916863.
https://pubmed.ncbi.nlm.nih.gov/25916863/

- abstract and metadata only; the paywalled Methods, Results and Discussion were not visible: https://link.springer.com/doi/10.1007/s00394-015-0908-z

### P26508979

This paper compares how the adipogenic activity (glitazone-like, 3T3-L1 cell assay) of ethanol extracts of Rhododendron groenlandicum leaves varies across wild populations and with quercetin content, so it compares collection sites rather than plant parts or preparations and measures no glucose or insulin outcome. I count adipogenesis as a relevant antidiabetic-mechanism outcome, consistently with P22542642 and P26707751.

Rapinski M; Musallam L; Arnason JT; Haddad P; Cuerrier A. Adipogenic Activity of Wild Populations of Rhododendron groenlandicum, a Medicinal Shrub from the James Bay Cree Traditional Pharmacopeia. Evidence-based complementary and alternative medicine : eCAM. 2015;2015:492458. doi:10.1155/2015/492458. PMID:26508979.
https://pubmed.ncbi.nlm.nih.gov/26508979/

- abstract-level summary only, from a database aggregator: https://search.emarefa.net/ar/detail/BIM-1062378-adipogenic-activity-of-wild-populations-of-rhododendron-groe
- truncated abstract snippet only: https://openaccess.library.uitm.edu.my/Record/doaj-5b178100975c46de94da4326402b5955
- not read; blocked by a bot check on both URL forms tried: https://pmc.ncbi.nlm.nih.gov/articles/PMC4609817

### P26707751

This paper helps compare preparations of Labrador tea by testing an 80% ethanol extract, its chromatographic fractions and the isolated compounds (+)-catechin and (-)-epicatechin in an adipogenesis assay, showing that the activity sits in a catechin pair and not in either compound alone.

Eid HM; Ouchfoun M; Saleem A; Guerrero-Analco JA; Walshe-Roussel B; Musallam L; Rapinski M; Cuerrier A; Martineau LC; Arnason JT; Haddad PS. A combination of (+)-catechin and (-)-epicatechin underlies the in vitro adipogenic action of Labrador tea (Rhododendron groenlandicum), an antidiabetic medicinal plant of the Eastern James Bay Cree pharmacopeia. Journal of ethnopharmacology. 2016;178:251-257. doi:10.1016/j.jep.2015.12.021. PMID:26707751.
https://pubmed.ncbi.nlm.nih.gov/26707751/

- abstract only (a library summary page): https://creehealth.org/about-us/departments/research-office/research-library/combination-catechin-and-epicatechin

## Exclusions

Entire accounts are excluded when any candidate lacks a confirmed decision. Provisional, unresolved and missing decisions are not treated as negatives.

- T007: P18066122 (pending).
- T010: P20301057 (provisional).
- T011: P19526043 (pending).
- T013: CL12843638 (missing), CL39426763 (missing).
- T014: CL12843638 (missing), CL39426763 (missing).

## Interpretation

These results describe the frozen rankers on the existing development corpus. Small candidate pools and repeated papers across accounts limit interpretation. No significance or generalization claim is made. Lexical remains the default. Rank changes do not alter experimental findings or comparability judgments.

Model: sentence-transformers/all-MiniLM-L6-v2; revision: 1110a243fdf4706b3f48f1d95db1a4f5529b4d41.
Ranking-input SHA-256: 20ffbdee6867cd487a33aa6486b9923daac564a9e8b6872f9f6aba41f208309d.
