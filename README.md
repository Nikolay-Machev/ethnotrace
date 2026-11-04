# EthnoTrace

**How closely do experimental studies test documented Canadian traditional plant uses associated with blood-glucose regulation and diabetes-related symptoms, and where does the indexed evidence leave gaps in comparability or documentation?**

The atlas compares species, plant part, preparation and outcome for each documented account. An experiment may be useful because it reveals a mismatch. Its result is reported separately from how closely it tests the documented use.

| Current collection | Status |
| --- | --- |
| Traditional accounts | 12 Canadian accounts; nine identified species and two unresolved plant names |
| Experimental evidence | 12 extracted units from six publications; 51 publications indexed |
| Human retrieval relevance | **Pitcher plant (T008) complete: 6 of 33 candidate decisions.** Four useful; two retained as safety context. The other 27 await review. |
| Ranking | Lexical, semantic and hybrid. All three recovered three of four useful T008 candidates in their top five. Lexical remains the default. |

## Run locally

From the repository root:

```sh
python3 -m http.server 8000 --directory web
```

Open <http://localhost:8000>. The app uses committed data and rankings; viewing it requires no model installation or API keys. Select **Pitcher plant · T008**, then **Different part**, to see why a root experiment can inform comparison with a leaf account.

To rebuild the committed outputs or check them without writing (Python 3.10+ and Node.js):

```sh
python3 scripts/rebuild.py
python3 scripts/rebuild.py --check
```

## Limits

The Canadian scope applies to the accounts; experimental studies may come from anywhere. The collection is selective. Missing indexed evidence does not establish that no study exists. Preserve the original symptom descriptions, attribution and source-specific rights.

The six-query benchmark measures recovery of seeded links. Ten of twelve links share a publication across the account and experiment. Only T008 has complete human relevance judgments, made after seeing the assistant screen. These development results establish neither general retrieval accuracy nor clinical efficacy.

[Documentation and build history](docs/README.md) · [Sources and licences](docs/rights.md) · [Hackathon provenance and AI disclosure](docs/provenance.md)
