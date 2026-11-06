# Primary-source audit of missing species, plant parts and preparations

## Follow-up with additional source evidence, 5 November 2026

The earlier 18-slot audit below describes the state of the original pinned source records. A new research pass located additional original community/ethnobotanical publications supporting **four plant-part values at the level of the related Cree diabetes-use survey**, without proving the organ for every particular earlier paper or laboratory extract. These findings now appear in [a 18-slot machine-readable source evidence ledger](../data/curated/missing_field_source_evidence.jsonl) and in exported demo data as `supplemental_missing_field_evidence`. Source-context values do **not** silently override pinned claim raw fields or ranking features.

| Account | Additional source-supported part | Scope and source |
| --- | --- | --- |
| T007, *Larix laricina* | inner bark | Grandi (2006), diabetes-use survey Table 5.3.3.1; Cree Health (2008), p. 5, identifies bark |
| T009, *Sorbus decora* | inner bark; branches also separately recorded | Grandi (2006) reports 13 users of inner bark and two of branches for diabetes-associated symptoms; the 2008 Cree Health list identifies bark |
| T010, *Populus balsamifera* | inner bark | Grandi (2006), Table 5.3.3.1, lists inner bark; Cree Health lists bark |
| T012, *Rhododendron groenlandicum* | leaves | Grandi (2006), Table 5.3.3.1, and Cree Health (2008) both identify leaves |

**Provenance of the four supported fields**

- Sonia Grandi, [*Social and Health Implications of Plant Remedies of the James Bay Cree for Symptoms of Type 2 Diabetes Mellitus*](https://www.collectionscanada.ca/obj/s4/f2/dsk3/QMM/TC-QMM-18294.pdf) (McGill thesis, 2006), Chapter 5 §5.3.3, Table 5.3.3.1, printed pp. 41–43. Its study is principally Mistissini; the observations are community-level and not a claimed per-informant match to T007/T009/T010/T012.
- Cree Board of Health and Social Services of James Bay, [Harris et al., *Reducing bad effects from diabetes: The healing plants and AGEs*](https://www.creehealth.org/sites/default/files/FRP-009-5-03-XY%20Harris%202008-10-03%20%28PlainLanguage%29.pdf), 3 October 2008, Table 1 on printed p. 5.
- Hall et al., [*A Multivariate Approach to Ethnopharmacology: Antidiabetic Plants of Eeyou Istchee*](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.511078/full) (2022), Table 1, independently summarizes the linked research program's plant-part associations.

**Related preparations, not promoted to a specific T-record recipe**

- T007: [Cree Health's tamarack traditional-medicine page](https://creehealth.org/bush-camp-safety/traditional-medicine) identifies boughs, bark and bare branches for tea, without tying a definite recipe to the specific diabetes claim.
- T012: Grandi (2006), Chapter 5 §5.3.4, states Labrador tea is frequently consumed as herbal tea. It does not give a diabetes-specific brewing method.
- T016: [Washington Native Plant Society](https://www.wnps.org/native-plant-directory/40-arbutus-menziesii) lists bark infusion as a diabetes-related use for *Arbutus menziesii*, but the original Duke database entry ETHNO=15976 has not been traced to that exact account or community, so T016's fields remain null.
- T006: the folk name *vinaigrier* resembles the name for staghorn sumac; no plant voucher identifies the exact species in the Franco-Ontarian document.
- T008: an experimental boiling-water preparation documented in TX001 is not proof of the original slow-healing-infection recipe.

The original six traditional missing plant-part slots now have four source-associated values in the supplemental evidence ledger, but all six **original** fields remain null. The other two lack direct diabetes-specific part attribution. All eight original missing preparation fields, both original unknown species fields, and the two experimental *Larix* plant-part fields remain null. A future decision to promote community-associated values into the active comparison features would need documented per-account provenance and a re-evaluation of previously reviewed case comparisons and frozen rankings. No traditional knowledge is represented as experimentally validated efficacy.

The earlier 'no source-supported change' conclusion below refers to the original specific-account standard and preceded the additional evidence. It should not be read as a claim that no source documents these plant parts in related Cree diabetes use.

---



Audited 5 November 2026. Scope: the 12 traditional accounts and 12 experimental units in `data/processed/`, focusing on **18 missing field slots**: two traditional species, six traditional plant parts, eight traditional preparations and two experimental plant parts. A field slot is not an independent source or a unique case.

**Result:** No source-supported change to the 18 missing fields was justified. Current `null` values are preserved. This is a source-evidence outcome, not a failed data validation. No existing traditional account is silently combined with a different tradition, a laboratory extraction, or another study.

## Traditional accounts

| Record | Missing fields | Source check and decision |
| --- | --- | --- |
| T005: Beauce “bleuets” | Scientific species | *La Beauce: Éveil à notre culture régionale*, “La médecine,” PDF page 43 / zero-based 42, says “branches de bleuets ébouillantées.” The plant is not identified beyond the vernacular name. Leave species null; branches and boiling-water treatment are already represented. [Source](https://bv.cdeacf.ca/RA_PDF/76500.pdf) |
| T006: Franco-Ontarian “vinaigrier” | Scientific species | *Remèdes anciens*, “Diabète,” printed p. 23 / zero-based PDF 22, reports boiling “caboches rouges” in water and drinking repeatedly or as needed. The document does not give a Latin species. Leave species null and retain the original red-cluster term. Boiling and oral administration are already recorded. [Source](https://bv.cdeacf.ca/RA_PDF/6327.pdf) |
| T007: *Larix laricina* | Traditional part, preparation | The cited Harbilas et al. in-vivo study describes an 80% ethanol experimental extract but does not specify the traditional recipe or part for this account. A **different** 2012 bark-fractionation publication identifies bark as experimental input; this does not establish the traditional preparation for T007 or the part of the specific E001/E002 extract. Leave both null. [Cited study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/) · [Bark experiment](https://pubmed.ncbi.nlm.nih.gov/22542642/) |
| T008: *Sarracenia purpurea* | Traditional preparation | Harris et al., Background, identifies Cree medicinal **leaf preparations** and a slow-healing-infection context but gives no reproducible historical recipe for this particular use. The laboratory ethanol or methanol–water extraction must not be copied into T008. Leave preparation null. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC3556504/) |
| T009: *Sorbus decora* | Traditional part, preparation | Vianna et al. reports the Cree survey and an **experimental** ethanol extract. Related ethnobotanical literature refers to bark and water-boiled inner bark for *Sorbus* species but is not a verified account-specific recipe for this T009 claim. Leave both null until the original interview or sufficiently attributable source links part and preparation to this exact use. [Cited study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3163474/) · [Related Cree ethnobotanical thesis](https://www.creehealth.org/sites/default/files/2025-07/Inter%20and%20Intra-Specific%20Differences%20in%20Medicinal%20Plant%20Use%20for%20the%20Treatment%20of%20Type%20II%20Diabetes%20Symptoms%20by%20the%20Cree%20Elders%20of%20Eeyou%20Istchee%20%28QC%29.pdf) |
| T010: *Populus balsamifera* | Traditional part, preparation | The cited experimental article reports balsam poplar as survey-selected, but its inner-bark ethanol protocol is a study method, not an established traditional-use description. Independent Gwich'in and Métis sources describe other uses and preparations; they cannot be assigned to this particular Eeyou Istchee account. Leave both null. [Cited study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3678421/) · [Separate Gwich'in account](https://gwichin.ca/node/335) |
| T011: *Vaccinium vitis-idaea* | Traditional preparation | Eid et al., Introduction, identifies berries for frequent urination, alongside food uses, but does not associate a specific medicinal extraction or recipe with this individual symptom account. Laboratory ethanol extract is a separate experimental protocol. Leave preparation null. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC4072050/) |
| T012: *Rhododendron groenlandicum* | Traditional part, preparation | Shang et al. labels boiling water for 75 minutes as a **laboratory method mimicking** Cree preparations, with experimental leaves. Additional Labrador-tea literature reports medicinal tea use and leaf collection, but the cited T012 survey account does not directly identify the plant part and recipe associated with its specific antidiabetic use. Keep both null; flag the literature for a further account-specific provenance check. [Cited study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532419/) · [Related publication](https://pubmed.ncbi.nlm.nih.gov/25916863/) |
| T015: *Vaccinium parvifolium* | Diabetes-specific part, preparation | The community-published Theresa Thorne account mentions general medicine for diabetes and separately mentions roots for **eye problems**. These are distinct assertions. The text does not connect the diabetes use to roots or a preparation. Leave both null. [Source](https://plants.hwulmuhwqun.ca/stories/theresa-thorne-from-kwamutsun-shares-some-information-on-red-huckleberry/) |
| T016: *Arbutus menziesii* | Diabetes-specific part, preparation | The cited USDA page is the landing page for Dr. Duke's aggregated databases, not the underlying account or precise source row. Independent publications mention bark and other uses but do not establish a source-linked part/recipe for this exact diabetes record. Leave both null. The original database entry and its citation need to be located before updating the account. [Database landing page](https://agdatacommons.nal.usda.gov/articles/dataset/Dr_Duke_s_Phytochemical_and_Ethnobotanical_Databases/24660351) |

## Experimental units

| Records | Missing field | Result |
| --- | --- | --- |
| E001 and E002: *Larix laricina* | Experimental plant part | Harbilas et al., Materials and Methods §2.1, identifies collected *L. laricina* and crude 80% ethanolic extract, referring to another extraction method, without specifying the plant organ in the cited methods. Another publication tested *L. laricina* bark in a different experiment. Do **not** transfer that separate experiment's bark designation into E001/E002. Both remain null. [Cited study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3408811/) · [Related bark study](https://pubmed.ncbi.nlm.nih.gov/22542642/) |

## Data interpretation and next follow-up

- The two unidentified French vernacular plants cannot safely receive single-species names from common-name inference.
- Traditional-part and traditional-preparation fields must refer to the **specific documented use**, not merely a species' general medicinal use or a laboratory extraction method.
- The traditional account T006 already records boiling, oral use and vernacular plant material. T005 already records branches and treatment with boiling water. These are **not** missing recipe or part slots.
- Next follow-up priorities: obtain the underlying Eeyou Istchee survey's relevant per-use methods/interview evidence, and trace T016 to the precise Duke database row and original citation. A general archive landing page is insufficient.
- Additional independently attributable Cree or community publications should be retained as supplementary leads. Avoid changing an existing record's community or replacing its original source without a documented provenance decision.
- No inferred recipe, scientific species, plant part, source-verification flag or independent review outcome was written to the active data. A future supported correction should update the pinned normalization override or separately curated source record, preserve original imports, then rerun the validation/rebuild workflow.

## Verification limitations

The Beauce and Franco-Ontarian historical PDFs were inspected using the available extracted page text; the PDF screenshot endpoint did not load the pages. Several PMC URLs intermittently returned browser-check pages; accessible article text and indexed publication passages were used where possible. The underlying confidential or unpublished ethnobotanical interviews were not obtained. The audit distinguishes documentary evidence from inference and does not claim primary interviewer confirmation.
