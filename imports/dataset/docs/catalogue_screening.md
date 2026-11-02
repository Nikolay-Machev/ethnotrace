# Organiser catalogue screening

The organiser document [Datasets for all tracks](https://docs.google.com/document/d/1L2xsq3sRqN9DHZddiZPLAbu8cP5s-Fx5/edit) was read through text and HTML exports on 1 November 2026. All 93 resource table entries were screened for the Canadian traditional-use and blood-glucose comparison. Repeated entries such as LOTUS and IMPPAT are separate catalogue rows, not distinct datasets. This is catalogue-level screening, not an exhaustive search of every provider.

The source document is referenced and fingerprinted; its full text is not redistributed. For most resources the access and licence notes were read from the catalogue only. Primary archive/API access was checked for Duke, GBIF and Europe PMC; access was attempted for Native American Ethnobotany. The machine-readable screen distinguishes these inspection depths.

## Imports

| Addition | Count | Interpretation |
| --- | ---: | --- |
| T016 — Arbutus menziesii | 1 | Diabetes use indexed as Canada(Salish); secondary database report, original reference unresolved |
| GBIF taxonomic crosswalk | 8 | Exact matches to existing scientific names; no resolution of historical common names |
| Species-specific literature leads | 2 | Abstracts inspected; full-text experimental extraction and pairing pending |

The active traditional-use table now has 12 records and nine named species; T005 and T006 still have unknown scientific species. The main publication catalogue remains 51 papers and the extracted experimental table remains 12 units. The two new leads are stored separately and are not counted as reviewed experiments.

## Duke archive

Citation: Duke, James A. (2016). Dr. Duke's Phytochemical and Ethnobotanical Databases. Ag Data Commons. Dataset. DOI: [10.15482/USDA.ADC/1239279](https://doi.org/10.15482/USDA.ADC/1239279). The repository metadata marks the archive CC0. The machine-readable record preserves the archive download URL and SHA-256.

The ETHNOBOT.csv member contains 82,873 rows. Filtering ACTIVITY for diabet or glyc returned 263 rows. Exactly one of those had canad in COUNTRY: ETHNO 15976, Arbutus menziesii, Diabetes, Canada(Salish), reference Eb25: 82. This filter is deliberately narrow: it does not establish that no additional Canadian knowledge exists under other indications or geography labels.

T016 preserves those fields. No plant part, preparation, route, individual informant or specific Nation has been inferred. The reference code did not resolve by exact lookup in REFERENCES.csv. A plausible historical publication was found in bibliographic searching, but its page 82 was not verified and it was not substituted as the record's primary citation.

The archive also has a lingonberry diabetes-use row attributed to Turkey. It was not imported as Canadian knowledge. Sixty-seven chemical-context rows for matching taxa were not imported as efficacy evidence; many lacked resolvable references. Database access rights do not remove Indigenous provenance and cultural-context considerations.

## Taxonomy

The GBIF Species API returned exact species-rank scientific-name matches for Larix laricina, Sarracenia purpurea, Sorbus decora, Populus balsamifera, Vaccinium vitis-idaea, Rhododendron groenlandicum, Vaccinium uliginosum and Vaccinium parvifolium. Input names, returned names, keys, provider scores, retrieval URLs and dates are retained in `taxon_crosswalk.jsonl`. These scores concern name matching, not confidence in a traditional identification.

This table stores factual identifiers and nomenclatural metadata; the underlying backbone licence was not independently verified during this pass. It does not resolve bleuets or vinaigrier and does not establish medicinal use, geographic provenance or efficacy.

## Literature leads

Zhou HB; Peng SH; Liu YM; Wang T; Weng XH; Liu G; Zhang JL. Structural changes of potato starch and activity inhibition of starch digestive enzymes by anthocyanin from lingonberry (Vaccinium uliginosum L.) retarded starch digestibility. International journal of biological macromolecules. 2024;281(Pt 4):136673. doi:10.1016/j.ijbiomac.2024.136673. PMID:39426763.

Anthocyanins, starch digestion and postprandial glucose; isolated fraction and food matrix differ from Gwich’in tea/berries. Full-text methods, experimental plant part, organism, exposure, controls and comparability require review. Common name lingonberry in the 2024 title conflicts with its scientific name; retain scientific wording rather than substitute V. vitis-idaea.

[PubMed](https://pubmed.ncbi.nlm.nih.gov/39426763/)

Kobayashi K; Baba E; Fushiya S; Takano F; Batkhuu J; Dash T; Sanchir C; Yoshizaki F. Screening of Mongolian plants for influence on amylase activity in mouse plasma and gastrointestinal tube. Biological & pharmaceutical bulletin. 2003;26(7):1045-1048. doi:10.1248/bpb.26.1045. PMID:12843638.

Methanolic plant extracts screened for amylase activity; a partial postprandial glucose effect reported for this species. Mongolian experimental material; not a Canadian traditional-use account. Specific experimental plant part is not established from the abstract.

[PubMed](https://pubmed.ncbi.nlm.nih.gov/12843638/)

The selected Europe PMC query explicitly named Vaccinium uliginosum or Vaccinium parvifolium and diabetes/glucose/insulin/glucosidase terms in title/abstract. Nine results were returned, including patents and irrelevant metabolism/ecology material. Two experimental articles were retained as leads; patents were not treated as clinical evidence. The 2024 paper calls V. uliginosum lingonberry: the scientific name is retained and the naming inconsistency is flagged rather than silently mapped to V. vitis-idaea.

## Access limitations and scope

Native American Ethnobotany is relevant, but its search endpoint returned HTTP 503; no records were obtained. Classical Mediterranean, Indian and East Asian traditions were not imported as Canadian records. Historical European herbals remain discovery leads until Canadian adoption is documented. Restricted datasets were not accessed, sponsor accounts were not created, and conservation or photographic data were not treated as medicinal-use evidence.

## Entry-by-entry decisions

| ID | Catalogue resource | Decision | Reason |
| --- | --- | --- | --- |
| CR001 | Dioscorides, De materia medica | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR002 | Alexander of Tralles, Therapeutics | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR003 | Hippocratic Corpus | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR004 | Pliny the Elder, Natural History, especially Books 20–27 | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR005 | Avicenna (Ibn Sīnā), Canon of Medicine | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR006 | Nicholas Culpeper, The Complete Herbal | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR007 | Household recipe books | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR008 | William Buchan, Domestic Medicine | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR009 | Medical Heritage Library / Internet Archive collections | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR010 | Wellcome Collection | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR011 | OpenITI (Open Islamicate Texts Initiative) | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR012 | Chinese Text Project (ctext.org) | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR013 | Logeion | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR014 | CLTK (Classical Language Toolkit) | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR015 | Biodiversity Heritage Library (BHL) | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR016 | Europeana | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR017 | Gallica / Bibliothèque nationale de France | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR018 | OPenn | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR019 | Perseus/Scaife | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR020 | Cambridge "Curious Cures" | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR021 | World Flora Online Plant List (WFO) | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR022 | IPNI (International Plant Names Index) | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR023 | Kew World Checklist of Vascular Plants / Plants of the World Online | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR024 | WCVP (bulk data) | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR025 | Kew Medicinal Plant Names Services (MPNS) | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR026 | GBIF Species API | used_for_import_or_enrichment | Imported exact scientific-name matches for eight existing identified taxa. |
| CR027 | Catalogue of Life / ChecklistBank | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR028 | BHL scientific-name tools | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR029 | Taxtree (NCBI TaxTree) | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR030 | NCBI Taxonomy | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR031 | Global Names Verifier | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR032 | Wikidata | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR033 | Dr. Duke's Phytochemical and Ethnobotanical Databases (USDA) | used_for_import_or_enrichment | Imported one Canadian diabetes use from the CC0 archive. |
| CR034 | IMPPAT | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR035 | Native American Ethnobotany Database | relevant_but_access_blocked | Canadian community-attributed uses could be relevant; direct search returned HTTP 503. No records imported. |
| CR036 | KNApSAcK Family | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR037 | LOTUS / Natural Products Online | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR038 | Plants For A Future (PFAF) | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR039 | Regional ethnobotanical datasets | potential_historical_source | May help locate Canadian accounts, but no Canadian diabetes passage verified here; historical European use alone is not Canadian settler evidence. |
| CR040 | TKDL (Traditional Knowledge Digital Library, India) (added) | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR041 | ChEBI | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR042 | PubChem | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR043 | ChEMBL | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR044 | LOTUS | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR045 | IMPPAT | outside_current_cultural_or_text_scope | The catalogue describes non-Canadian traditions or classical-language tasks; no Canadian provenance established. |
| CR046 | COCONUT | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR047 | BRENDA | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR048 | UniProt | optional_chemistry_context | Potential chemical/target support; occurrence or enzyme activity must not be treated as clinical efficacy. |
| CR049 | NAPRALERT | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR050 | PubMed / NCBI E-utilities | relevant_literature_or_trial_discovery | Suitable for targeted plant/outcome searches; not a reason to import all results. |
| CR051 | Europe PMC | used_for_import_or_enrichment | Retrieved two species-specific experimental literature leads; no new efficacy label assigned. |
| CR052 | ClinicalTrials.gov | relevant_literature_or_trial_discovery | Suitable for targeted plant/outcome searches; not a reason to import all results. |
| CR053 | EMA herbal monographs (HMPC) | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR054 | WHO monographs on selected medicinal plants | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR055 | NCCIH "Herbs at a Glance" | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR056 | LiverTox | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR057 | openFDA CAERS (food/supplement adverse events) | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR058 | EFSA Compendium of Botanicals | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR059 | EPA CompTox Chemicals Dashboard | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR060 | DrugBank | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR061 | Dr. Duke's / PubChem / BRENDA | optional_safety_or_regulatory_context | May support interpretation after species/product matching; no direct Canadian claim record established. |
| CR062 | GBIF occurrence API (with media) | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR063 | iDigBio | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR064 | LifeCLEF / PlantCLEF | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR065 | Pl@ntNet API | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR066 | BHL Flickr | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR067 | Wikimedia Commons: Herbals category | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR068 | IUCN Red List API | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR069 | CITES Species+ API | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR070 | TDWG WGSRPD | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR071 | WCVP / POWO distributions; GBIF occurrences | defer_images_geography_conservation | Not needed for the current text-evidence comparison; occurrence or conservation status does not establish medicinal use. |
| CR072 | MeSH | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR073 | Disease Ontology (DOID) | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR074 | ICD-11 | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR075 | UMLS Metathesaurus | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR076 | SNOMED CT | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR077 | RxNorm / ATC | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR078 | MedDRA | defer_access_or_licence | Restricted or licensed resource according to catalogue; no restricted payload imported. |
| CR079 | Plant Ontology (PO) | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR080 | ChEBI Ontology | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR081 | Uberon | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR082 | WFO IDs / GBIF taxon keys / Catalogue of Life IDs | supporting_taxonomy | Useful nomenclature or identifier cross-check; not evidence of traditional use or therapeutic efficacy. |
| CR083 | Darwin Core | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR084 | TDWG Economic Botany Data Collection Standard | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR085 | TEI P5 / TEI-XML | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR086 | IIIF | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR087 | ALTO XML / PAGE XML | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR088 | Dublin Core / DataCite | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR089 | PROV-O | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR090 | Web Annotation Data Model | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR091 | JSON-LD / RDF / SKOS | supporting_standard_not_evidence | Useful schema, terminology or provenance support; must not convert historical symptoms into modern diagnoses automatically. |
| CR092 | Anakin (YC 21) | tool_not_dataset | Sponsor product, not source evidence; no account created. |
| CR093 | Aitho | tool_not_dataset | Sponsor product, not source evidence; no account created. |

## Files and reproducibility

The screening summary stores document hashes, filtering rules and counts. `catalogue_imported_source_rows.jsonl` retains the exact CC0 archive row used for T016, including the abbreviated reference. `catalogue_literature_leads.jsonl` retains citations and limitations for the two new articles. No full abstracts or archive payloads are published.

The new traditional record and leads await independent review. The additions do not change the existing experimental or claim-pair evidence labels.
