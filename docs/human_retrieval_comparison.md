# Human-reviewed retrieval comparison

Generated, do not edit. Run python scripts/rebuild.py.

6 complete accounts; 33 account–candidate pairs; 25 judged useful.

Assisted development review, not a held-out test. Source depth varies. A useful study need not support the traditional claim.

Precision@5 uses five slots, including unfilled slots for short pools. Recall@5 uses all judged-useful candidates in the indexed pool. Metrics are macro averages with equal weight per complete account.

| Method | Precision@5 | Recall@5 | MRR |
| --- | ---: | ---: | ---: |
| lexical | 0.667 | 0.828 | 0.833 |
| semantic | 0.733 | 0.889 | 0.917 |
| hybrid | 0.733 | 0.903 | 1.000 |

## T007

5 useful of 6 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 4 | 0.800 | 0.800 | P23864882 |
| semantic | 5 | 1.000 | 1.000 | None |
| hybrid | 5 | 1.000 | 1.000 | None |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E001 | 3 | 1 (+2) | 1 (+2) |
| E002 | 4 | 2 (+2) | 4 (+0) |
| P18066122 | 1 | 4 (-3) | 2 (-1) |
| P22542642 | 2 | 3 (-1) | 3 (-1) |
| P23864882 | 6 | 5 (+1) | 5 (+1) |

Positive change means moving up relative to lexical ranking.

### E001

Its 80% ethanol Larix extract (125 and 250 mg/kg) did not significantly lower glycaemic AUC in the prevention protocol, so it gives a null in vivo glucose outcome that can be set against the treatment protocol (E002) to compare timing of dosing, though the plant part is not named and no water prepar…

Harbilas D; Vallerand D; Brault A; Saleem A; Arnason JT; Musallam L; Haddad PS. Larix laricina, an Antidiabetic Alternative Treatment from the Cree of Northern Quebec Pharmacopoeia, Decreases Glycemia and Improves Insulin Sensitivity In Vivo. Evidence-based complementary and alternative medicine : eCAM. 2012;2012:296432. doi:10.1155/2012/296432. PMID:22888363.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/

- full text: Methods 2.2, Results 3.1, Figure 1 (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/

### E002

The same 80% ethanol Larix extract lowered glycaemic AUC about 10-12% (P<0.05) when given as treatment, which is a direct glucose outcome that contrasts with the null prevention result (E001), though the plant part is unspecified and no traditional water preparation was tested.

Harbilas D; Vallerand D; Brault A; Saleem A; Arnason JT; Musallam L; Haddad PS. Larix laricina, an Antidiabetic Alternative Treatment from the Cree of Northern Quebec Pharmacopoeia, Decreases Glycemia and Improves Insulin Sensitivity In Vivo. Evidence-based complementary and alternative medicine : eCAM. 2012;2012:296432. doi:10.1155/2012/296432. PMID:22888363.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/

- full text: Methods 2.2, Results 3.1, Figure 1 (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/

### P18066122

Approved source follow-up: Fraser et al. (2007) Table 1 compares L. laricina bark collected in Mistissini (2003 and 2004) with cambium collected in Whapmagoostui (2004), reports differing antioxidant rankings, and Methods specifies 80% ethanol extracts. The paper provides a within-species plant-material/collection contrast and useful antioxidant context; plant part and community co-vary, so this is not a controlled part-effect test or a blood-glucose outcome. Limitations: Antioxidant assays are not direct tests of the recorded diabetes symptoms; independent effects of community vs plant part are not isolated.

Fraser MH; Cuerrier A; Haddad PS; Arnason JT; Owen PL; Johns T. Medicinal plants of Cree communities (Québec, Canada): antioxidant activity of plants used to treat type 2 diabetes symptoms. Canadian journal of physiology and pharmacology. 2007;85(11):1200-1214. doi:10.1139/y07-108. PMID:18066122.
https://pubmed.ncbi.nlm.nih.gov/18066122/

- Approved assistant source follow-up; direct independent primary-source inspection by the named reviewer is not separately documented.: https://drpatrickowen.com/wp-content/uploads/2016/09/d38d03_dde8f25c8ca74ddc87e266527a84ab01.pdf

### P22542642

It tests a bioassay-guided 80% ethanol extract of Larix laricina bark and identifies the constituents (a cycloartane triterpene and a labdane diterpene) that drive adipogenesis in 3T3-L1 cells, so it offers a mechanistic, diabetes-relevant outcome for the bark extract, though not a glucose or in viv…

Shang N; Guerrero-Analco JA; Musallam L; Saleem A; Muhammad A; Walshe-Roussel B; Cuerrier A; Arnason JT; Haddad PS. Adipogenic constituents from the bark of Larix laricina du Roi (K. Koch; Pinaceae), an important medicinal plant used traditionally by the Cree of Eeyou Istchee (Quebec, Canada) for the treatment of type 2 diabetes symptoms. Journal of ethnopharmacology. 2012;141(3):1051-1057. doi:10.1016/j.jep.2012.04.002. PMID:22542642.
https://pubmed.ncbi.nlm.nih.gov/22542642/

- abstract only (blog mirror of the abstract; fetch tool summary): https://tryl2012.blogspot.com/2016/04/2012-adipogenic-constituents-from-bark.html
- full text of a different paper (Shang et al. 2015 PLoS ONE, not a candidate), read only for context …: https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419

### P23864882

It shows that an 80% ethanol extract of Larix laricina (plant part not stated) did not significantly change G6Pase in liver cells but strongly increased glycogen synthase activity and GSK-3 phosphorylation, with AMPK and Akt signalling effects, so it offers a hepatic glucose-handling outcome that is…

Nachar A; Vallerand D; Musallam L; Lavoie L; Badawi A; Arnason J; Haddad PS. The action of antidiabetic plants of the canadian james bay cree traditional pharmacopeia on key enzymes of hepatic glucose homeostasis. Evidence-based complementary and alternative medicine : eCAM. 2013;2013:189819. doi:10.1155/2013/189819. PMID:23864882.
https://pubmed.ncbi.nlm.nih.gov/23864882/

- full text as returned by the fetch tool (a summary of Methods, Results and Discussion, not a verbatim read): https://pmc.ncbi.nlm.nih.gov/articles/PMC3707264


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

It tests a leaf extract and then fractions and eleven isolated compounds in muscle and liver cells (glucose uptake, glucose-6-phosphatase), so it helps compare the documented leaf part and an extract-versus-isolated-compound gap, while its outcomes are cellular glucose handling, not slow-healing inf…

Muhammad A; Guerrero-Analco JA; Martineau LC; Musallam L; Madiraju P; Nachar A; Saleem A; Haddad PS; Arnason JT. Antidiabetic compounds from Sarracenia purpurea used traditionally by the Eeyou Istchee Cree First Nation. Journal of natural products. 2012;75(7):1284-1288. doi:10.1021/np3001317. PMID:22738356.
https://pubmed.ncbi.nlm.nih.gov/22738356/

- abstract only: https://core.ac.uk/works/49920640

### P26626246

It compares the boiling-water leaf decoction the authors describe as traditional with an 80% ethanol leaf extract chemically (phenolics and morroniside similar; betulinic and ursolic acids about 107 and 93 times higher in ethanol), so it helps compare preparation for the documented leaf, but it meas…

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

Its ethanolic Sorbus decora extract in food (about 200 mg/kg/day, 7 days, KK-Ay mice, n=6) shows a serial blood-glucose change with no significance assigned in the figure, so it gives an in vivo glucose outcome whose strength is weak and differs from the abstract's claim and from the paper's signifi…

Vianna R; Brault A; Martineau LC; Couture R; Arnason JT; Haddad PS. In Vivo Anti-Diabetic Activity of the Ethanolic Crude Extract of Sorbus decora C.K.Schneid. (Rosacea): A Medicinal Plant Used by Canadian James Bay Cree Nations to Treat Symptoms Related to Diabetes. Evidence-based complementary and alternative medicine : eCAM. 2011;2011:237941. doi:10.1093/ecam/nep158. PMID:19887507.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/

- full text: Methods, Results 3.3, Figure 7, Discussion (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/

### P20738101

This paper helps compare the activity of fractions and isolated compounds from Sorbus decora bark, the traditionally used part, by bioassay-guided antidiabetic testing, so it speaks to a glucose-related outcome and to which constituents of the bark extract carry the effect.

Guerrero-Analco JA; Martineau L; Saleem A; Madiraju P; Muhammad A; Durst T; Haddad P; Arnason JT. Bioassay-guided isolation of the antidiabetic principle from Sorbus decora (Rosaceae) used traditionally by the Eeyou Istchee Cree First Nations. Journal of natural products. 2010;73(9):1519-1523. doi:10.1021/np1003005. PMID:20738101.
https://pubmed.ncbi.nlm.nih.gov/20738101/

- full text of a plain-language lay summary of the paper (Cree Board of Health), not the journal abstract or paper: https://www.creehealth.org/sites/default/files/FRP-019-5-04-X%20Guerrero%202010-03-01%20%28PlainLanguage%29.pdf


## T010

4 useful of 4 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 4 | 0.800 | 1.000 | None |
| semantic | 4 | 0.800 | 1.000 | None |
| hybrid | 4 | 0.800 | 1.000 | None |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E006 | 1 | 2 (-1) | 1 (+0) |
| E007 | 2 | 1 (+1) | 2 (+0) |
| P20301057 | 3 | 4 (-1) | 3 (+0) |
| P22504062 | 4 | 3 (+1) | 4 (+0) |

Positive change means moving up relative to lexical ranking.

### E006

Its 80% ethanol extract (inner bark per the Discussion; Methods do not name the part) at 125 mg/kg gave lower terminal insulin marked significant versus DIO control, an insulin-sensitivity outcome relevant to the account, though the 250 mg/kg dose was only P=0.052 and no water preparation or other p…

Harbilas D; Vallerand D; Brault A; Saleem A; Arnason JT; Musallam L; Haddad PS. Populus balsamifera Extract and Its Active Component Salicortin Reduce Obesity and Attenuate Insulin Resistance in a Diet-Induced Obese Mouse Model. Evidence-based complementary and alternative medicine : eCAM. 2013;2013:172537. doi:10.1155/2013/172537. PMID:23781256.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3678421/

- full text: Methods, Table 2 and footnote, AUC results (read this session): https://pmc.ncbi.nlm.nih.gov/articles/PMC3678421/

### E007

Terminal glucose in the same experiment was lower with the extract (105 and 121 vs 135) but not significantly, which makes it an informative null glucose outcome beside the insulin result, with the same inner-bark ethanol extract and no preparation comparison.

Harbilas D; Vallerand D; Brault A; Saleem A; Arnason JT; Musallam L; Haddad PS. Populus balsamifera Extract and Its Active Component Salicortin Reduce Obesity and Attenuate Insulin Resistance in a Diet-Induced Obese Mouse Model. Evidence-based complementary and alternative medicine : eCAM. 2013;2013:172537. doi:10.1155/2013/172537. PMID:23781256.
https://pmc.ncbi.nlm.nih.gov/articles/PMC3678421/

- full text: Methods, Table 2 and footnote, AUC results (read this session): https://pmc.ncbi.nlm.nih.gov/articles/PMC3678421/

### P20301057

Approved source follow-up: Martineau et al. (2010) explicitly tests Populus balsamifera inner-bark extract in 3T3-L1 cells. The source reports inhibition of adipocyte differentiation, reduced clonal expansion, and antagonistic PPAR-gamma activity. This supplies same-species metabolic-mechanism evidence aligned with the project's prior relevance scope for adipogenesis, though not a clinical glucose or traditional-use outcome. Limitations: Traditional part and preparation are unknown; neither species use nor human efficacy is established. This recommendation updates the earlier provisional source assessment, not the named reviewer's decision.

Martineau LC; Hervé J; Muhamad A; Saleem A; Harris CS; Arnason JT; Haddad PS. Anti-adipogenic activities of Alnus incana and Populus balsamifera bark extracts, part I: sites and mechanisms of action. Planta medica. 2010;76(13):1439-1446. doi:10.1055/s-0029-1240941. PMID:20301057.
https://pubmed.ncbi.nlm.nih.gov/20301057/

- Approved assistant source follow-up; direct independent primary-source inspection by the named reviewer is not separately documented.: https://pubmed.ncbi.nlm.nih.gov/20301057/

### P22504062

It tests a P. balsamifera extract mixed into the high-fat diet of diet-induced obese mice and reports glucose, insulin and insulin-sensitivity outcomes (lower blood glucose in the second half of feeding, lower insulin, higher adiponectin and a lower leptin/adiponectin ratio), so it informs the diabe…

Harbilas D; Brault A; Vallerand D; Martineau LC; Saleem A; Arnason JT; Musallam L; Haddad PS. Populus balsamifera L. (Salicaceae) mitigates the development of obesity and improves insulin sensitivity in a diet-induced obese mouse model. Journal of ethnopharmacology. 2012;141(3):1012-1020. doi:10.1016/j.jep.2012.03.046. PMID:22504062.
https://pubmed.ncbi.nlm.nih.gov/22504062/

- abstract only (as relayed by the page summary): https://creehealth.org/about-us/departments/research-office/research-library/populus-balsamifera-l-salicaceae-mitigates
- abstract only (as relayed by the page summary): https://www.curehunter.com/public/pubmed22504062.do
- None: None


## T011

6 useful of 7 candidates.

| Method | Useful in top five | Precision@5 | Recall@5 | Missed useful IDs |
| --- | ---: | ---: | ---: | --- |
| lexical | 4 | 0.800 | 0.667 | P19526043, P20087853 |
| semantic | 5 | 1.000 | 0.833 | P20087853 |
| hybrid | 4 | 0.800 | 0.667 | P19526043, P20087853 |

| Useful candidate | Lexical rank | Semantic rank (change) | Hybrid rank (change) |
| --- | ---: | ---: | ---: |
| E008 | 1 | 1 (+0) | 1 (+0) |
| E009 | 2 | 2 (+0) | 2 (+0) |
| E011 | 4 | 3 (+1) | 3 (+1) |
| E012 | 5 | 4 (+1) | 4 (+1) |
| P19526043 | 7 | 5 (+2) | 6 (+1) |
| P20087853 | 6 | 6 (+0) | 7 (-1) |

Positive change means moving up relative to lexical ranking.

### E008

Lingonberry berries at 250 mg/kg lowered glycaemic AUC about 12% (P<0.05) in mice, giving a glucose outcome for the documented berry part, with no comparison to other parts or a water preparation.

Eid HM; Ouchfoun M; Brault A; Vallerand D; Musallam L; Arnason JT; Haddad PS. Lingonberry (Vaccinium vitis-idaea L.) Exhibits Antidiabetic Activities in a Mouse Model of Diet-Induced Obesity. Evidence-based complementary and alternative medicine : eCAM. 2014;2014:645812. doi:10.1155/2014/645812. PMID:25013446.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/

- full text: Methods and Results (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/

### E009

The 500 mg/kg dose gave only a 7% AUC reduction that was not significant, so against E008 it shows a non-monotonic dose response in the berry extract, a useful comparison for outcome though not for part or preparation.

Eid HM; Ouchfoun M; Brault A; Vallerand D; Musallam L; Arnason JT; Haddad PS. Lingonberry (Vaccinium vitis-idaea L.) Exhibits Antidiabetic Activities in a Mouse Model of Diet-Induced Obesity. Evidence-based complementary and alternative medicine : eCAM. 2014;2014:645812. doi:10.1155/2014/645812. PMID:25013446.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/

- full text: Methods and Results (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/

### E011

Its lingonberry ethanol extract at 200 ug/mL raised glucose uptake significantly in muscle cells, a cellular glucose outcome that can be set against the hot-water extract (E012) to compare preparation.

Shang N; Saleem A; Musallam L; Walshe-Roussel B; Badawi A; Cuerrier A; Arnason JT; Haddad PS. Novel Approach to Identify Potential Bioactive Plant Metabolites: Pharmacological and Metabolomics Analyses of Ethanol and Hot Water Extracts of Several Canadian Medicinal Plants of the Cree of Eeyou Istchee. PloS one. 2015;10(8):e0135721. doi:10.1371/journal.pone.0135721. PMID:26263160.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

- full text: Methods, Table 1, glucose-uptake Results, Figure 1 (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

### E012

The hot-water lingonberry extract did not significantly raise glucose uptake while the ethanol extract did, which is the closest the set gets to the traditional water preparation and shows a preparation mismatch.

Shang N; Saleem A; Musallam L; Walshe-Roussel B; Badawi A; Cuerrier A; Arnason JT; Haddad PS. Novel Approach to Identify Potential Bioactive Plant Metabolites: Pharmacological and Metabolomics Analyses of Ethanol and Hot Water Extracts of Several Canadian Medicinal Plants of the Cree of Eeyou Istchee. PloS one. 2015;10(8):e0135721. doi:10.1371/journal.pone.0135721. PMID:26263160.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

- full text: Methods, Table 1, glucose-uptake Results, Figure 1 (read in an earlier session of this review): https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/

### P19526043

Approved source follow-up: Harbilas et al. (2009) identifies Vaccinium vitis-idaea berries in Table 1, describes the 80% ethanol extraction in Plant Materials, and in Results reports 18-hour C2C12 basal/insulin-stimulated glucose uptake increases of 21%/31%, with 3T3-L1 increases of 92%/118%. It also reports adipogenesis activity. These are source-specific diabetes-related assays of the same species and part, making the study useful to evaluate a broader mechanistic context without directly measuring frequent urination. Limitations: In vitro assays do not directly test frequent urination or establish equivalence with the unrecorded traditional medicinal preparation.

Harbilas D; Martineau LC; Harris CS; Adeyiwola-Spoor DC; Saleem A; Lambert J; Caves D; Johns T; Prentki M; Cuerrier A; Arnason JT; Bennett SA; Haddad PS. Evaluation of the antidiabetic potential of selected medicinal plant extracts from the Canadian boreal forest used to treat symptoms of diabetes: part II. Canadian journal of physiology and pharmacology. 2009;87(6):479-492. doi:10.1139/y09-029. PMID:19526043.
https://pubmed.ncbi.nlm.nih.gov/19526043/

- Approved assistant source follow-up; direct independent primary-source inspection by the named reviewer is not separately documented.: https://www.neurolipidomics.com/assets/pubs/2009_harbilas_therapeutics.pdf

### P20087853

This paper lets me compare lingonberry berry ethanol extract (which activated AMPK and a metformin-like mitochondrial effect) against its isolated quercetin glycosides and aglycone, which raised insulin-independent glucose uptake in muscle cells, so it ties the berry preparation to a glucose-handlin…

Eid HM; Martineau LC; Saleem A; Muhammad A; Vallerand D; Benhaddou-Andaloussi A; Nistor L; Afshar A; Arnason JT; Haddad PS. Stimulation of AMP-activated protein kinase and enhancement of basal glucose uptake in muscle cells by quercetin and quercetin glycosides, active principles of the antidiabetic medicinal plant Vaccinium vitis-idaea. Molecular nutrition & food research. 2010;54(7):991-1003. doi:10.1002/mnfr.200900218. PMID:20087853.
https://pubmed.ncbi.nlm.nih.gov/20087853/

- abstract only (as summarised by the fetch tool): https://read.qxmd.com/read/20087853/stimulation-of-amp-activated-protein-kinase-and-enhancement-of-basal-glucose-uptake-in-muscle-cells-by-quercetin-and-quercetin-glycosides-active-principles-of-the-antidiabetic-medicinal-plant-vaccinium-vitis-idaea


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

- T013: CL12843638 (missing), CL39426763 (missing).
- T014: CL12843638 (missing), CL39426763 (missing).

## Interpretation

These results describe the frozen rankers on the existing development corpus. Small candidate pools and repeated papers across accounts limit interpretation. No significance or generalization claim is made. Lexical remains the default. Rank changes do not alter experimental findings or comparability judgments.

Model: sentence-transformers/all-MiniLM-L6-v2; revision: 1110a243fdf4706b3f48f1d95db1a4f5529b4d41.
Ranking-input SHA-256: f06fd4730948d223286a406ec14c7667287290caf51c9ee37c1d2898f1a78870.
