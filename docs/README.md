# EthnoTrace documentation

| Topic | Current documentation |
| --- | --- |
| Data and rights | [Provenance](provenance.md), [rights](rights.md), [preprocessing](preprocessing.md), [data quality](data_quality.md) |
| Product | [Evidence atlas](evidence_atlas.md), [product audit](product_audit.md), [example cited report](reports/T008-evidence.md) |
| Retrieval | [Baseline](baseline.md), [semantic retrieval](semantic_retrieval.md), [human evaluation](human_retrieval_comparison.md) |
| Reviews | [Workflow](review_workflow.md), [schema](review_schema.md), [case index](review_cases.md), [candidate packet](retrieval_review_packet.md), [validation](review_data_validation.md) |
| Pilot | [Frozen protocol](generalization_protocol.md), [frozen review packet](generalization_review_packet.md) |
| Submission | [Readiness](submission_readiness.md) |

The pilot protocol and packet are checksum-frozen historical inputs. Their original pending-status text describes the freeze date; current assisted pilot results are in the evaluation page and README. They are preserved unchanged for reproducibility.

Earlier plans, worksheets and follow-up discussions are in [archive/](archive/). They document development history; the current status is in the product audit and generated evaluation.

## Rebuilding and validation

Use Python 3.11 or 3.12 and Node.js. Run `python scripts/rebuild.py` to regenerate outputs, or `python scripts/rebuild.py --check` to check freshness. Reviews and source data remain inputs. The build stages them in a temporary directory and copies back only generated outputs.

Run `python -m unittest discover -s tests`, `node tests/test_web.cjs` and `node tests/test_reports.cjs`. See [semantic setup](semantic_retrieval.md) if model input text changes; the normal rebuild uses the committed cache without downloading weights.
