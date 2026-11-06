> Archived development note. See [current documentation](../README.md) for status.

# Frozen ten-paper generalization pilot: source research (5 November 2026)

This document summarizes an **assistant-authored, pre-ranking primary-source literature assessment** of all ten candidate pairs. Detailed individual records, accessible source sections, uncertainty and overlap notes are in [the source review ledger](../../data/generalization/assistant_source_reviews_2026-11-05.jsonl). The frozen manifest and candidate files were not changed. No model predictions, lexical rankings, semantic rankings or fusion scores were opened to prepare these judgments.

**Critical status**: The findings here are **not** independently reviewed human labels. `data/generalization/reviews.jsonl` is unchanged (ten unresolved reviewer rows); the scoring gate remains closed until a named human accepts or revises each finding, records their own checked-source depth and truthful exposure history. An approval after reading this assessment is assisted, not independent blinded evaluation. For an independent claim, ask a reviewer who has not seen these labels or rankings to follow the original packet.

## Research dispositions before model scoring

| Original pair | Assistant research assessment | Primary evidence and boundary |
| --- | --- | --- |
| T011 / P23365108 | **useful** | Törrönen et al. (2013): whole lingonberry purée tested with wheat bread; reduced early insulin response, but no statistically significant lingonberry glycemic-profile improvement. J Nutr Results Tables 3–4, Figure 1; https://jn.nutrition.org/article/S0022-3166%2822%2901166-X/fulltext |
| T008 / P33144625 | **useful** | Kannan et al. (2020): S. purpurea aerial/pitcher extract inhibited HSV-1 attachment and replication in cells. Scientific Reports, Materials and methods and Results Figures 1–4; https://www.nature.com/articles/s41598-020-76151-w |
| T008 / P38943782 | **useful** | Puchalski et al. (2024): publisher highlights explicitly document S. purpurea ethanolic extract antiviral activity in vitro and comparison with other carnivorous/non-carnivorous plants. Full species-level tables not available. Virology publisher highlights/abstract; https://www.sciencedirect.com/science/article/pii/S004268222400165X |
| T008 / P27174081 | **useful** | Morrison et al. (2016): S. purpurea compounds from methanolic extract inhibit Mycobacterium tuberculosis H37Ra in vitro. This tests a different infection and comes from distinct Mi'kmaq/Wolastoqiyik medicinal traditions; no direct diabetes-associated slow-healing infection claim. Journal of Ethnopharmacology author abstract, Methods/Results; https://pubmed.ncbi.nlm.nih.gov/27174081/ |
| T011 / P28620479 | **useful** | Lingonberry nectar reduced postprandial insulin versus an inverted-sucrose drink in healthy people, while blackcurrant improved glycemic profile. British Journal of Nutrition author abstract; https://pubmed.ncbi.nlm.nih.gov/28620479/ |
| T011 / P22854401 | **useful** | Törrönen et al. (2012): whole lingonberries and nectar with added sucrose altered human postprandial glucose and insulin profiles, with late hypoglycemic effects. AJCN abstract, Design/Results; https://pubmed.ncbi.nlm.nih.gov/22854401/ |
| T008 / P35807620 | **useful** | Huang et al. (2022): direct comparison of leaf/pitcher, stem and root extracts using water, ethanol, methanol and acetone. The root acetone extract showed the strongest measured antibacterial and other laboratory activities; the historically documented leaf preparation is not the root-acetone test. Plants author abstract, extraction comparison; https://pubmed.ncbi.nlm.nih.gov/35807620/ |
| T011 / DOI2107 | **useful** | Ryyti et al. (2024): lingonberry skin press-cake extract partly reduced fasting hyperglycemia and glucose intolerance in high-fat-fed mice. Nutrients Abstract, Methods and Results; https://www.mdpi.com/2072-6643/16/13/2107 |
| T011 / P22901554 | **useful** | Linderborg et al. (2012): lingonberry powder human crossover tests showed condition-dependent / null postprandial glucose and lipid effects. Nutrition Research author abstract, trial design and Results; https://pubmed.ncbi.nlm.nih.gov/22901554/ |
| T011 / P36599454 | **context_only** | Pärnänen et al. (2023): fermented lingonberry mouthwash studied oral plaque, antimicrobial activity and gingival inflammation, without glycemia, insulin, frequent urination or a direct account-specific preparation comparison. European Journal of Dentistry author abstract; https://pmc.ncbi.nlm.nih.gov/articles/PMC10756786/ |

## Interpretation and limitations

- **Nine useful / one context-only** is the assistant's research screening result, **not** a human-reviewed pilot outcome, validated scientific accuracy metric or a ranking result.
- A study qualifies as useful through a relevant outcome or direct part/preparation comparison. Infection studies are useful to the wider T008 infection indication, without being direct demonstrations of diabetes-associated wound healing. Negative glucose findings may still help assess T011.
- T011 refers to Cree berries for frequent urination and other diabetes-related symptoms; postprandial metabolic assays do not test frequent urination.
- T008 refers to Cree leaf preparations for slow-healing infections. Other First Nations' historic tuberculosis-like use is contextual, not provenance for the Cree account.
- The Finnish lingonberry postprandial trials share researchers and similar designs. Cohort and experimental independence were not confirmed. The two S. purpurea antiviral papers also share authors/laboratory lineage.
- Source depth varies. The Virology 2024 and some older papers were accessible through primary publisher highlights/abstracts rather than full numerical tables.
- No candidate metadata or model inputs have been changed. This avoids label leakage into the frozen rankers.

## Human-review completion instructions

A named reviewer should inspect the links and sections, then decide `useful`, `context_only` or `unresolved` in the original ten rows of `data/generalization/reviews.jsonl`, supplying reviewer name, date, independent rationale, `sources_checked` url/depth, and truthful answers to `saw_rankings_or_assistant_labels` and `previously_reviewed_this_pair`. A reviewer who has read this document has seen assistant relevance assessments and must record exposure truthfully. Do not falsely mark exposure false merely to pass the scorer's gate.

The existing pilot evaluator intentionally withholds rankings when human review is unresolved or potentially exposed. Use a separately versioned assisted-evaluation track if the team wishes to score after reviewing assistant labels; do not change the frozen eligibility rule to bypass blinding or relabel these as independent gold.
