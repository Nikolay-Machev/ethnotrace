# Candidate review: assistant screening pass

The [screen](../data/review/assistant_relevance_screen.jsonl) covers all 33 candidate–account pairs. It is an assistant assessment of indexed author abstracts plus existing source packets, not a human or blinded relevance judgment. Previous rank results were known. Use the original reviewer packet without this file for a fresh independent assessment. No human answers, experimental classifications, ranking inputs or traditional claims were changed.

A candidate is useful here if it clarifies how the account's material, preparation or indication was tested, including a specific contrast. Safety-only drug metabolism endpoints are outside this narrow use question. A negative finding can still be useful. In this screening, 28 pairs are useful, four are outside that scope and one is unresolved (T011/P19526043: verify the species-specific assay in the full text).

## T008: leaf preparations and slow-healing infections

| Candidate | Useful for this account? | Reason |
| --- | --- | --- |
| E003 | Yes | Leaf arm; the glucose-toxicity cell endpoint differs from infection healing. |
| E004 | Yes | Root arm; informative within-paper part contrast and a different endpoint. |
| P26626246 | Yes | Compares chemistry of water and ethanol leaf extracts. |
| P22738356 | Yes | Leaf-derived material tested against metabolic cellular endpoints. |
| P21186373 | No | Drug-metabolism safety assay; no healing or leaf preparation comparison identified. |
| P26626249 | No | Transcriptional safety study; no test of infection healing or preparation equivalence. |

All three rankers retrieve 3 of the 4 assistant-screened useful candidates in the top five. Lexical and hybrid omit E004; semantic omits E003 and places P21186373 first. These are assisted, exploratory observations on one query, not human-reviewed metrics. Leave the default unchanged.

## Rebuild and browser check

The semantic evaluation, evaluation page and demo were regenerated from the available main-branch inputs. At the checked revision (fe66068), Alex Karadjov's comparison form still had 20 pending entries. The validation PR does not change the reviewer form. The reported partner submission was not incorporated or overwritten. No human-reviewed retrieval metrics are available in this snapshot.

Live preview: selecting Different part displayed E004 alone under lexical, semantic and hybrid, retaining the same Harris et al. source link. Clicking the source opened its PMC URL. Clicking Download cited report did not yield a confirmed browser download event. The [T008 hybrid report](reports/T008-evidence.md) was therefore generated with the app's export formatter and checked for all six candidates and the E004 source URL.
