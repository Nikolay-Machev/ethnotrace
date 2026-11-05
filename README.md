# EthnoTrace

Team: **ethnotrace**

**EthnoHack 2026 · Track 1: Traditional Knowledge Mining.** A shared plant name can hide differences in the plant part, preparation and outcome. EthnoTrace helps a researcher trace those differences from a Canadian traditional-use account to a cited experiment.

**How closely do experimental studies test documented Canadian traditional plant uses associated with blood-glucose regulation and diabetes-related symptoms, and where does the indexed evidence leave gaps in comparability or documentation?**

The atlas compares species, plant part, preparation and outcome for each documented account. An experiment may be useful because it reveals a mismatch. Its result is reported separately from how closely it tests the documented use.

| Current collection | Status |
| --- | --- |
| Traditional accounts | 12 Canadian accounts; nine identified species and two unresolved plant names |
| Experimental evidence | 12 extracted units from six publications; 51 publications indexed |
| Human retrieval relevance | All 33 pairs reviewed: 22 useful, eight context only, one provisionally useful, two unresolved. Provisional judgments are excluded from confirmed relevance metrics. T008, T009 and T012 have complete decisions. |
| Ranking | Lexical, semantic and hybrid. On three completely judged accounts, macro recall@5 was 0.833 lexical, 0.833 semantic and 0.917 hybrid. Lexical remains the default. |

## Demo

![Evidence atlas showing separate lingonberry and tamarack accounts and clickable counts by comparison dimension](docs/images/atlas-preview.png)

Atlas interface during development. In the current app, try **Pitcher plant · T008 → Different part**. The E004 experiment used roots and measured cell survival; the traditional account describes leaves and slow-healing infections. Switch rankers to compare order, open the source, or [read the sample exported report](docs/reports/T008-evidence.md).

## Technologies, installation and keys

The viewer uses HTML, CSS and plain JavaScript. Python 3.10+ serves the static files and runs the standard-library data pipeline; Node.js is needed only to rebuild or test report exports. Optional local model inference uses Sentence Transformers, Transformers, PyTorch and NumPy; [model attribution and setup](docs/semantic_retrieval.md) are documented separately.

No API keys or external inference services are required for viewing, rebuilding or testing the committed rankings. No environment file is needed. External links open the cited publications.

## Run locally

Download and unzip the repository from GitHub (**Code → Download ZIP**), or clone it with Git. Open a terminal in the directory containing this README. No packages need to be installed to view the app; with Python 3.10+ installed, run:

```sh
python3 -m http.server 8000 --directory web
```

Open <http://localhost:8000>. The app uses committed data and rankings; viewing it requires no model installation or API keys. Stop the server with Ctrl+C.

To rebuild the committed outputs or check them without writing (Python 3.10+ and Node.js):

```sh
python3 scripts/rebuild.py
python3 scripts/rebuild.py --check
```

## Limits

The Canadian scope applies to the accounts; experimental studies may come from anywhere. The collection is selective. Missing indexed evidence does not establish that no study exists. Preserve the original symptom descriptions, attribution and source-specific rights.

The six-query benchmark measures recovery of seeded links. Ten of twelve links share a publication across the account and experiment. Human relevance metrics cover only the three fully judged accounts. The reviews were made with access to assistant screening and include abstract and secondary-source judgments. These development results establish neither general retrieval accuracy nor clinical efficacy.

[Documentation and build history](docs/README.md) · [Sources and licences](docs/rights.md) · [Hackathon provenance and AI disclosure](docs/provenance.md)

Human-reviewed lexical, semantic and hybrid results: [retrieval comparison](docs/human_retrieval_comparison.md). Only accounts with complete confirmed judgments enter these development metrics.

Next experiment: [new-paper review packet](docs/generalization_review_packet.md) and [frozen pilot protocol](docs/generalization_protocol.md). All ten new candidates currently have unresolved reviews; no generalization result is claimed. The atlas now gives a checkable completion criterion for each research gap.

[Product verification and remaining review work](docs/product_audit.md) covers browser checks, source-link availability and current review provenance.
