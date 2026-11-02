# EthnoTrace dataset

## Current scope

The project compares documented plant uses in Canada associated with blood-glucose regulation or diabetes-related symptoms with modern experimental research.

Traditional records may come from First Nations, Inuit, Métis or settler communities anywhere in Canada. Inclusion depends on documentation, attribution and reuse conditions; this is not a claim of complete national coverage. Modern research may come from any country.

Research question: **How closely does modern experimental research test documented Indigenous and settler plant uses in Canada associated with blood-glucose regulation and diabetes-related symptoms?**

The project was redirected from the initial general medicinal-use and digestive-use collection to this scope. The existing v0.1 data files remain as legacy examples of the record format. They are not the Canadian diabetes dataset and should not be included in its evaluation. Version 0.2 adds Canadian records T005–T006. Earlier traditional records T001–T004 and all five experimental records remain legacy examples. No diabetes-related experimental records have been imported.

## Imported Canadian records

| Record | Source | Attribution and recorded use |
| --- | --- | --- |
| T005 | [La Beauce : éveil à notre culture régionale](https://bv.cdeacf.ca/RA_PDF/76500.pdf), 2005; PDF page 43, footnote 70 | Émiliana Hince, Frampton, 1974, through Fonds Christine Audet and France Bélanger et al., p.236. Blueberry branches scalded with water, explicitly associated with diabetes. Species and administration route unspecified. |
| T006 | [Remèdes anciens](https://bv.cdeacf.ca/RA_PDF/6327.pdf), 1994; printed p.23 / PDF page 23 | Collective of older Franco-Ontarian residents in St-Albert and Embrun. Vinaigrier red clusters boiled in water, listed under diabetes; oral use described. Exact species unspecified. |

Both sources are PDF publications, represented as JSONL records in `data/traditional_records.jsonl` and joined to `data/sources.json` through `source_key`. Settler attribution identifies where use was documented, not where knowledge originated. Scientific names remain null pending verification. No open reuse licence was verified; factual summaries and brief excerpts are included, without copying the full PDFs.

[Marielle Cormier Boudreau's Médecine traditionnelle en Acadie](https://editionsfrancophonie.com/livres/medecine-traditionnelle-en-acadie/) remains a bibliographic lead. The publisher lists a print-only edition (2003, 290 pages, ISBN 2-923016-31-9). No accessible diabetes entry was verified, so no record was imported.

Current totals: **6 traditional records (2 Canadian diabetes records, 4 legacy), 5 legacy experimental records, 9 imported sources.** README discovery leads are not included in source counts.

Filter the current scope after loading traditional records:

```python
canadian = [r for r in traditional if r.get("dataset_scope") == "canadian_diabetes"]
```

## Canadian source leads

| Source | Attribution and geography | Relevant material | Status and limits |
| --- | --- | --- | --- |
| [Plants used by the Cree Nation of Eeyou Istchee for the treatment of diabetes](https://pubmed.ncbi.nlm.nih.gov/16297584/) | Eeyou Istchee Cree, Quebec | Ethnobotanical survey identifying potentially antidiabetic species through traditional-use knowledge | Publication identified. Inspect full study and its attribution/reuse conditions before extracting records. |
| [Gwich'in Social & Cultural Institute: Blueberry](https://gwichin.ca/plants/blueberry) | Gwich'in; source provides Gwichya and Teetł'it names | Names Vaccinium uliginosum and describes berries and plant teas in relation to diabetes; cites Alestine Andre's 2006 work | Page inspected. Diabetes reference is explicit. Preparation details for the diabetes passage must be kept separate from the page's cold-remedy passage. Copyright notice present; open reuse licence not verified. |
| [Theresa Thorne from kwa'mutsun on red huckleberry](https://plants.hwulmuhwqun.ca/stories/theresa-thorne-from-kwamutsun-shares-some-information-on-red-huckleberry/) | Named speaker from kwa'mutsun; Hul'q'umi'num' Language & Culture Society, British Columbia | Bilingual account explicitly mentions diabetes in connection with red huckleberry | Page inspected. Botanical species, diabetes-specific plant part and preparation are not established in this passage. Do not assign the roots mentioned for eye problems to the diabetes use. Open reuse licence not verified. |
| [Mi'kmaw Resource Guide excerpt hosted by Cape Breton University](https://www.cbu.ca/indigenous-initiatives/lnu-resource-centre/mikmaq-resource-guide/mikmaw-language-spirituality-medicine-mikmaw-tloti/) | Mi'kmaw Resource Guide 2007; collaborating Mi'kmaw organizations identified on page | Golden Thread entry explicitly includes diabetes; Ground Juniper entry describes a sugar-level claim | Page inspected. Common/local names need taxonomic verification. Keep preparation and indication links specific to each entry. Copyright attributed to Eastern Woodland Publishing; open reuse licence not verified. |
| [Traditional Metis Medicines and Healing](https://www.metismuseum.ca/media/document.php/14667.Traditional%20Metis%20Medicines.pdf) | Métis resource hosted by the Virtual Museum of Métis History and Culture | PDF page 21 (printed slide headed Diabetes) describes balsam poplar, aspen, blueberry/yarrow and other combinations | Diabetes slide inspected. Several records concern mixtures. Common names and exact community/location require further verification. Métis records belong to the Indigenous category, not the settler category. Open reuse licence not verified. |
| [Contemporary use of bark for medicine by two Salishan native elders](https://pubmed.ncbi.nlm.nih.gov/2345461/) | Southeast Vancouver Island, British Columbia | Abstract identifies diabetes among reported bark uses | Publication identified. Plant-specific diabetes attribution requires full text; abstract-level mention alone is insufficient for a species record. |
| [Anti-diabetic properties of the Canadian lowbush blueberry](https://pubmed.ncbi.nlm.nih.gov/16979328/) | Canadian research; Vaccinium angustifolium | Experimental research lead; abstract describes the plant as a natural health product recommended for diabetes in Canada | Not evidence of settler traditional use. Vaccinium angustifolium must not be substituted for the Gwich'in source's Vaccinium uliginosum. |
| [Antidiabetic compounds from Sarracenia purpurea](https://pubs.acs.org/doi/10.1021/np3001317) | Research associated with Eeyou Istchee Cree knowledge | Laboratory work on plant-derived compounds and glucose-related cellular outcomes | Experimental lead. Cell outcomes must remain distinct from human diabetes outcomes. |

Two French-Canadian settler records are included: T005 (Frampton, Beauce) and T006 (St-Albert/Embrun, Ontario). Anglo-Canadian and Acadian diabetes entries remain unverified. A Canadian research affiliation, commercial supplement claim or European folk-use description does not establish Canadian settler use. Inuit-specific qualifying records have not yet been verified either. These are coverage gaps, not evidence that such knowledge does not exist.

Public availability does not establish an open licence or unrestricted permission to republish traditional knowledge. The table records source locations and brief discovery summaries; record-level extraction still requires documenting attribution and access/reuse conditions.

## Fields for the redirected collection

The existing record fields remain applicable. The following fields are populated in T005–T006; they are absent from legacy records. The validator checks basic record structure and source joins, not these additional fields.

| Field | Representation |
| --- | --- |
| `knowledge_tradition` | `indigenous`, `settler`, `documented_exchange` or `unspecified`; preserve the source's specific attribution separately |
| `community_or_nation` | Community/Nation named in the source, or null |
| `knowledge_holder` | Named contributor where the source publicly attributes the account, or null |
| `location` | Documented place/region of use; do not substitute publisher location |
| `historical_period` | Period of reported use, or null; publication date alone does not establish antiquity |
| `original_use_description` | Original wording or explicitly marked paraphrase of the reported use, with source locator |
| `diabetes_relevance` | `explicit`, `symptom_associated` or `unclear` |
| `relevance_rationale` | Explanation and review status for the diabetes connection |
| `administration_route` | Route reported for the specific preparation/use, or null |
| `access_or_reuse_conditions` | Source licence, permissions or stated restrictions; unknown when unverified |

`explicit` means the source names diabetes or blood-sugar regulation. `symptom_associated` means the source reports potentially relevant symptoms and the connection requires review. `unclear` means there is insufficient detail to establish relevance. Thirst, frequent urination, general tonics and similar nonspecific descriptions are not automatically diabetes claims.

Traditional-use reports and modern experimental findings remain separate. Source-level mentions do not establish a specific preparation, botanical identity, dose or clinical effect.

---

## Legacy v0.1 collection

Initial medicinal-use and digestive-use examples, retained for reference.

Version 0.1 contains 4 traditional-use records and 5 experimental records from 7 sources. The experimental records cover 4 papers. E001 and E002 describe different experiments in the same paper.

## Files

| File | Contents |
| --- | --- |
| `data/traditional_records.jsonl` | Traditional-use reports and regulatory summaries |
| `data/experimental_records.jsonl` | Animal, isolated-tissue and human studies |
| `data/sources.json` | Source citations, original formats, import scope and licences |
| `scripts/validate.py` | Checks required fields, identifiers and source references |

The data files use UTF-8 JSONL: one JSON object per line. Missing information is stored as `null`, meaning it was not reported in the material inspected.

## Fields

| Field | Description |
| --- | --- |
| `species` | Array of scientific names, or `null` where the source does not establish the species |
| `original_plant_name` | Array of botanical or common names as recorded in the source |
| `plant_part` | Plant material used, such as leaves, flowers or aerial parts |
| `preparation` | Preparation method, solvent, formulation and route, where reported |
| `reported_use_or_outcome` | Paraphrase of the reported traditional use or experimental result |
| `study_setting` | Source or experiment category |
| `source_id` | PMID, PMCID, DOI or EMA reference |
| `source_url` | Source link |
| `supporting_passage` | Verbatim excerpt supporting part of the record; other fields may come from the sections listed in `passage_locator` |
| `licence` | Source licence or reuse status |
| `record_id` | Unique record identifier: T for traditional use, E for experimental research |
| `source_key` | Reference to an entry in `sources.json` |
| `passage_locator` | Source section containing the evidence |
| `notes` | Missing details, normalization decisions and interpretation limits |
| `curation_method` | How the record was assembled |
| `accessed_on` | Source access date in YYYY-MM-DD format |

The `study_setting` values are:

- `secondary_ethnobotanical_review`
- `regulatory_traditional_use_summary`
- `animal_in_vivo`
- `isolated_tissue_ex_vivo`
- `human_randomized_trial`

## Sources

| Source | Original format | Records |
| --- | --- | --- |
| Monari et al. (2022), PMC9370752 | Review article in HTML/JATS XML; supplementary dataset linked separately | T001–T002: selected passages on chamomile. Supplementary Table S1 was not imported. |
| EMA peppermint leaf summary | HTML summary with linked PDF monograph | T003: preparation types and traditional digestive-use indication from the summary |
| EMA chamomile flower summary | HTML summary with linked PDF monograph | T004: preparation types and traditional gastrointestinal-use indication from the summary |
| PMC4410481 / PMID25886126 | Full article in JATS XML, retrieved through Europe PMC | E001: mouse experiment; E002: isolated rabbit jejunum experiment |
| PMID24463157 | Structured abstract retrieved as Europe PMC JSON | E003: chamomile decoction experiment in rats |
| PMID31470006 | Structured abstract retrieved as Europe PMC JSON | E004: peppermint oil randomized trial |
| PMID14755152 | Structured abstract retrieved as Europe PMC JSON | E005: multi-herb randomized trial |

Europe PMC is listed as a retrieval service in `sources.json`; it is not counted as an evidence source.

Full articles, abstracts and supplementary archives are not included. The records contain selected excerpts and structured summaries.

## Normalization and limitations

- `Matricaria recutita` is mapped to `Matricaria chamomilla` using the synonym statement in PMC4410481. This mapping has not been checked against an external taxonomic authority.
- Scientific species names are left `null` when only common names appear in the inspected abstract.
- EMA preparation descriptions list alternatives at the source level. The exact preparation associated with each indication requires checking the full monograph.
- The multi-herb trial is stored as one record. Its result cannot be attributed to an individual ingredient.
- Traditional-use reports, animal experiments and human trials remain separate categories.
- Records join to the source catalogue through `source_key`. No validated claim–study matching or support/contradiction labels are included.
- Records from the same paper should remain in the same evaluation split.
- Records were assembled with AI assistance and have not been independently double-annotated. The validation script checks structure, not scientific accuracy.

## Licences

Source material retains its original rights.

| Material | Reuse status |
| --- | --- |
| Monari et al. (2022) article | CC BY 4.0 |
| PMC4410481 article | CC BY 4.0 |
| EMA summaries | Reuse with EMA attribution under its legal notice |
| Abstracts for PMID24463157, PMID31470006 and PMID14755152 | Open reuse licence not verified; only factual summaries and short excerpts are included |

Attribution, source URLs and licence links are recorded in `data/sources.json`.

## Validation

Run from the repository root:

```bash
python scripts/validate.py
```

## Loading records

```python
import json
from pathlib import Path

def load_records(path):
    return [
        json.loads(line)
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

traditional = load_records("data/traditional_records.jsonl")
experimental = load_records("data/experimental_records.jsonl")
```
