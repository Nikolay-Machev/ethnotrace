# Experimental finding-direction source verification

Reviewed 6 November 2026. Scope: **12 extracted experimental units from six primary publications**, each defined by its existing reported endpoint. Source evidence and per-unit explanations live in [the machine-readable verification ledger](../data/review/experimental_finding_source_checks_2026-11-06.jsonl).

## Summary

| Category | Count | Experimental IDs |
| --- | ---: | --- |
| Favourable effect | 5 | E002, E006, E008, E010, E011 |
| No detected effect for the specifically extracted endpoint | 5 | E001, E004, E007, E009, E012 |
| Condition-dependent effect | 1 | E003 |
| Statistically inconclusive | 1 | E005 |
| **Total** | **12** | |

All twelve assessments match the current **normalized active endpoint direction** in `data/processed/experimental_records.jsonl`. No new correction of the active data was justified; E005's prior correction from raw `support` to `statistically_inconclusive` is retained, not overwritten.

**Provenance:** These are assistant-conducted checks against cited publication Results/Methods sections, not independent human finding-label reviews. `reviewer_a.jsonl` and `reviewer_b.jsonl` experimental-finding fields are not changed or marked as human completed. Researchers who subsequently approve this source packet should have a distinct, truthful assisted-approval record.

## Case-level source evidence and scope

| ID | Endpoint | Source-checked result | Source section |
| --- | --- | --- | --- |
| E001 | *Larix laricina*, prevention glycemic AUC | No significant change when given with HFD from outset | [Harbilas et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/), Results §3.1, Figure 1 |
| E002 | *L. laricina*, treatment glycemic AUC | 10% and 12% reductions at 125 and 250 mg/kg respectively, P<0.05, **separate treatment arm** | Same paper, §3.1, Figure 1 |
| E003 | *Sarracenia purpurea*, leaf glucose-stressed cell survival | Protected through 30 µg/mL, but not at 100 µg/mL; condition dependent | [Harris et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3556504/), Results, Figure 1 |
| E004 | *S. purpurea*, root glucose-stressed cell survival | **No protection** at low concentrations and **increased cell loss** near IC50. The current `no_detected_effect` label is narrowly about protective activity; retain the reported adverse outcome | Same paper, Results, Figure 1 |
| E005 | *Sorbus decora*, KK-Ay mouse serial blood glucose | Numerical downward trend without statistical significance due to variability. Separate rat experiments in the publication have different results | [Vianna et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/), Results §3.3, Figure 7, Discussion |
| E006 | *Populus balsamifera*, terminal insulin | 125 mg/kg significantly reduced terminal insulin (P<0.05) versus DIO controls | [Harbilas et al. 2013](https://onlinelibrary.wiley.com/doi/10.1155/2013/172537), Table 2 |
| E007 | *P. balsamifera*, terminal glucose | Same mice as E006. Table 2 terminal glucose is not marked significant versus DIO controls. **Other glycemia and insulin endpoints differ** | Same paper, Table 2 and significance legend |
| E008 | *Vaccinium vitis-idaea*, 250 mg/kg glucose AUC | 12% significant decrease (P<0.05) versus DIO controls | [Eid et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/), Results §3.1, Figure 1(b) |
| E009 | *V. vitis-idaea*, 500 mg/kg glucose AUC | 7% decrease not statistically significant for AUC; other endpoint observations must remain separate | Same paper, §3.1, Figure 1(b) |
| E010 | *Rhododendron groenlandicum*, C2C12 glucose uptake | Ethanol and hot-water leaves extracts enhanced uptake, hot-water preparation maintained activity | [Shang et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/), Table 1, Results glucose uptake, Figure 1 |
| E011 | *V. vitis-idaea*, ethanol extract C2C12 glucose uptake | Ethanol berry extract significantly enhanced uptake | Same paper, Table 1 and Figure 1 |
| E012 | *V. vitis-idaea*, hot-water extract C2C12 glucose uptake | Not among the three significantly active hot-water extracts | Same paper, Table 1, glucose uptake Results, Figure 1 |

## Scientific interpretation

- These direction labels describe a **particular assay endpoint, comparator, dosage and experimental setting**, not a scientific finding about clinical effectiveness or a traditional community account as a whole.
- 'No detected effect' is not proof of equivalence or absence of biological activity. E004 is especially important: the root-extract result also includes measurable worsening at higher concentrations.
- Statistical inconclusiveness (E005) is not interchangeable with a significantly favourable effect, despite the numerical reduction.
- E006 and E007 are outcomes from **the same mouse treatment group**. E010–E012 are linked panels in the same publication, not independent replications.
- Several methods are laboratory solvent extractions rather than verified traditional preparations. Plant-part and recipe uncertainties must be preserved.
- **Independent human experimental-finding labels remain outstanding**; source research here is a review packet, not attested Reviewer A or Reviewer B approval.

The pinned imports, baseline normalizations, development relevance judgments, frozen generalization protocol and saved exploratory ranker results were not edited. This work increases source traceability without changing the reported performance.
