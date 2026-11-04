# Build phases and reproduction notes

| Phase | What changed | Details |
| --- | --- | --- |
| Dataset import | Pinned the pre-hackathon dataset and recorded file hashes. The import is preserved; corrections belong in the active pipeline. | [Manifest](../imports/dataset_manifest.json), [provenance](provenance.md) |
| Preprocessing | Added normalized text, explicit part and solvent mappings, exposure fields and source-based evaluation groups. Missing fields remain unknown. | [Methods](preprocessing.md), [quality audit](data_quality.md) |
| Comparison explorer | Separated experimental findings from claim comparability, linked source passages, and retained verification and comparison decisions separately. | [Review schema](review_schema.md), [case index](review_cases.md) |
| Retrieval and atlas | Added the lexical baseline and error analysis, one row per account, filters and cited drill-down. The 25 literature-lead appearances represent 22 distinct records; two are catalogue leads. | [Baseline](baseline.md), [errors](retrieval_error_report.md), [atlas](evidence_atlas.md) |
| Evidence gaps | Added next steps for unresolved preparation, endpoint and coverage; two targeted source notes supplement the frozen experiment set. | [Extractions](../data/curated/targeted_extractions.jsonl) |
| Evaluation and exports | Added development results, coverage, uncertainty and cited Markdown reports. The static app exports any account locally without sending its text to a service. | [Worked report](reports/T008-evidence.md), [current web evaluation](../web/evaluation.html) |
| Semantic experiment and audit | Compared a local pretrained ranker and rank fusion with lexical ranking; added the uniform random benchmark and corrected the E005 interpretation. | [Semantic methods](semantic_retrieval.md), [audit](data_quality.md) |

For an isolated preprocessing run, use `python3 scripts/preprocess.py --output /tmp/ethnotrace-processed`. To inspect retrieval for one account, use `python3 scripts/retrieve.py --claim T011 --limit 5`. For rebuilding committed outputs, use the [single rebuild command](README.md#rebuilding).
