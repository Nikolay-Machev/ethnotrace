# EthnoTrace documentation

| Topic | Read this |
| --- | --- |
| Where the data came from | [Build phases and reproduction notes](build_history.md), [provenance and AI disclosure](provenance.md), [pinned source manifest](../imports/dataset_manifest.json), [bibliography](../imports/dataset/docs/papers.md), [references](../imports/dataset/docs/references.md), [rights and attribution](rights.md) |
| How records are prepared | [Preprocessing](preprocessing.md), [quality findings and E005 correction](data_quality.md) |
| What the app does | [Atlas, gaps and cited drill-down](evidence_atlas.md), [targeted source notes](../data/curated/targeted_extractions.jsonl), [example report for T008](reports/T008-evidence.md) |
| How ranking is evaluated | [Baseline](baseline.md), [ranking errors](retrieval_error_report.md), [semantic and hybrid experiment](semantic_retrieval.md) |
| How to review evidence | [Comparison workflow](review_workflow.md), [schema](review_schema.md), [case index](review_cases.md), [candidate review packet](retrieval_review_packet.md), [human review instructions](next_reviews.md), [assistant screening pass](retrieval_screen_notes.md) |
| Historical plan | [Original atlas plan (archived)](archive/evidence_atlas_plan.md) |

## Rebuilding

From the repository root, run `python3 scripts/rebuild.py`. Use `--check` for a read-only byte comparison with a clean rebuild. The command stages inputs in a temporary directory, rebuilds processed records, evaluation reports, the review packet, both browser data files and the T008 example report, then copies back only changed generated outputs. Human and assistant review files, the pinned import and semantic ranking cache are inputs. They are never copied back. T008 is a worked example; the browser can export any selected account.

The cached semantic rankings are produced by a separate model run. If inputs to the model change, follow [the pinned-model reproduction instructions](semantic_retrieval.md) first. The regular rebuild checks the cache fingerprint and does not download weights.

Run `python3 -m unittest discover -s tests`, `node tests/test_web.cjs` and `node tests/test_reports.cjs` for validation. The Python suite includes the generated-file freshness check.
