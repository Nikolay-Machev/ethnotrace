# Semantic retrieval challenger

## What runs

The experiment uses the pretrained `sentence-transformers/all-MiniLM-L6-v2` model, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, on the local CPU. It is an English general-purpose sentence encoder, not a clinically validated biomedical model. No fine-tuning or external inference service is used. The model has 384-dimensional embeddings and a 256-word-piece input limit. Model licence: Apache-2.0; source-data rights are separate.

Official references: [model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), [Sentence Transformers semantic-search documentation](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html).

This first version ranks structured record text, not full papers or arbitrary passages. Queries use the original documented-use description. Candidate text uses the paper title (or parent-paper title for extracted units) and experimental endpoint. Supporting passages, result summaries, direction labels and review rationales are excluded. Titles can themselves mention findings; the model is not guaranteed to be free of all publication framing. No clinical equivalence is inferred.

## Three methods

- **Lexical:** unchanged baseline 1.1, including species eligibility, part and solvent scores, and text overlap.
- **Semantic:** normalized query/document embeddings scored by cosine similarity, among exactly the same species-eligible candidates.
- **Hybrid:** equal-weight reciprocal-rank fusion of lexical and semantic ranks, using `1/(60 + rank)` for each. The constant was fixed before inspecting results, not tuned to these cases.

Ties use evidence ID order. Unresolved scientific names return no candidates. All methods retain identical source records, comparison judgments, experimental findings and candidate sets. The atlas counts do not change when the ranking selector changes. Results remain grouped into extracted experiments and literature leads; evaluation uses the full ungrouped ranking, not the visual grouping. Rankings are not probabilities, confidence levels, evidence-quality assessments or treatment recommendations.

## Reproduce

The committed snapshots let the static app show all modes without installing ML dependencies. To regenerate scores, create a separate Python environment:

```bash
python3 -m venv .venv-semantic
source .venv-semantic/bin/activate
# Optional on Linux: install the CPU-only torch wheel first.
# pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-semantic.txt
python scripts/semantic_retrieval.py --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
python scripts/evaluate_semantic.py
python scripts/build_demo.py
python scripts/build_evaluation.py
```

The first inference run downloads model weights. Dataset text stays local. No API key is required. Actual library versions, model revision, scores, input-field policy and an input fingerprint are saved in `data/evaluation/semantic_rankings.json`. No weights or embeddings are added to GitHub. Hashes cover allowed query/document text, candidate eligibility and lexical scores. Rebuilding the app rejects a stale snapshot instead of silently showing obsolete rankings. Reviewer-only changes do not require recomputing embeddings; rerun evaluation and the two page builders.

## Observed development results

| Ranker | Seeded-link macro recall@5 | Seeded-link MRR |
| --- | ---: | ---: |
| Lexical | 0.917 | 0.561 |
| Semantic | 0.917 | 0.658 |
| Hybrid | 0.917 | 0.631 |

These are six existing development queries with twelve seeded links, not held-out test results or complete relevance judgments. Per-query rankings and missed links are retained in `data/evaluation/semantic_comparison.json` and shown on the evaluation page. For pitcher plant (T008), semantic retrieves E004 within five but drops E003 below five; lexical and hybrid miss E004 instead. Equal aggregate recall therefore hides a different error. The improvement in first-relevant rank is descriptive; we make no statistical superiority claim and leave lexical as the default.

No query currently has complete human relevance judgments, so human-reviewed retrieval metrics remain null. Unjudged candidates are never treated as negatives. Once the chosen candidate pools are fully reviewed, `evaluate_semantic.py` will additionally report human-reviewed development metrics. This still does not create an independent test set. Related sources and experiments must remain grouped for any future held-out study. Repeated experiments from the same publication are not independent samples; model pretraining overlap with literature is not known.

## Verification

Automated checks cover the species gate, unresolved names, exclusion of annotation fields, unchanged comparability, deterministic rank fusion, stale-snapshot rejection, empty-positive-set handling and the three-mode renderer. The actual pretrained model was run successfully on the current collection. Live browser interaction with the new selector remains to be checked locally.
