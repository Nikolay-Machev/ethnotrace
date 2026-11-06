# Semantic retrieval challenger

## What runs

The experiment uses the pretrained `sentence-transformers/all-MiniLM-L6-v2` model, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, on the local CPU. It is an English general-purpose sentence encoder, not a clinically validated biomedical model. No fine-tuning or external inference service is used. The model has 384-dimensional embeddings and a 256-word-piece input limit. Model licence: Apache-2.0; source-data rights are separate.

Official references: [model card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2), [Sentence Transformers semantic-search documentation](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html).

This first version ranks structured record text, not full papers or arbitrary passages. Queries use the original documented-use description. Candidate text uses the paper title (or parent-paper title for extracted units) and experimental endpoint. Supporting passages, result summaries, direction labels and review rationales are excluded. Titles can themselves mention findings; the model is not guaranteed to be free of all publication framing. No clinical equivalence is inferred.

## Three methods

- **Lexical:** current baseline 1.2, including species eligibility, part and solvent scores, and text overlap.
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
python scripts/current_semantic.py --revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41
python scripts/rebuild.py
python scripts/rebuild.py --check
```

The first inference run downloads model weights. Dataset text stays local. No API key is required. Actual library versions, model revision, scores, input-field policy and an input fingerprint are saved in `data/evaluation/semantic_rankings.json`. No weights or embeddings are added to GitHub. Hashes cover allowed query/document text, candidate eligibility and lexical scores. Rebuilding the app rejects a stale snapshot instead of silently showing obsolete rankings. Reviewer-only changes do not require recomputing embeddings; run `python scripts/rebuild.py` to refresh all dependent outputs.

## Observed development results

| Ranker | Seeded-link macro recall@5 | Seeded-link MRR |
| --- | ---: | ---: |
| Uniform random order (expected) | 0.869 | 0.595 |
| Lexical | 0.917 | 0.561 |
| Semantic | 0.917 | 0.658 |
| Hybrid | 0.917 | 0.631 |

Ten of the twelve links share a publication across the account and experimental record. Short pools give high recall even under random ordering. These are six existing development queries with twelve seeded links, not held-out test results or complete relevance judgments. Per-query rankings and missed links are retained in `data/evaluation/semantic_comparison.json` and shown on the evaluation page. For pitcher plant (T008), semantic retrieves E004 within five but drops E003 below five; lexical and hybrid miss E004 instead. Equal aggregate recall therefore hides a different error. The improvement in first-relevant rank is descriptive; we make no statistical superiority claim and leave lexical as the default.

All six development accounts now have complete matching assisted relevance judgments across 33 pairs. Macro precision@5 is 0.667 lexical and 0.733 semantic/hybrid; recall@5 is 0.828, 0.889 and 0.903 respectively. These are development results, not independent test accuracy. Related sources and experiments must remain grouped for any future held-out study. Repeated experiments from the same publication are not independent samples; model pretraining overlap with literature is not known.

The current evaluator reconciles all submitted reviewers for a pair before scoring. Pending or provisional companion reviews exclude the whole account; conflicting completed labels raise an adjudication error. The historical `evaluate_semantic.py` remains unchanged for the frozen pilot, while current builds use `evaluate_retrieval.py`.

## Verification

Automated checks cover the species gate, unresolved names, exclusion of annotation fields, unchanged comparability, deterministic rank fusion, stale-snapshot rejection, empty-positive-set handling and the three-mode renderer. The actual pretrained model was run successfully on the current collection. Browser interaction, cited exports and responsive layouts passed the integration suite; see the product audit.

## Baseline 1.2

The current development ranker removes the -2 penalty for different plant parts. Part overlap retains its +2 contribution. Mismatches remain visible in the comparison table and do not imply irrelevant evidence. For T008/E004, the score rises from 8 to 10, but its rank remains sixth of six; the candidate order and reported development retrieval metrics are unchanged. No extra boost is applied to this example.

`retrieve.py`, `semantic_retrieval.py` and the original pilot evaluator remain frozen for pilot reproducibility. Active builds use `current_retrieve.py`, `current_semantic.py` and `evaluate_retrieval.py`. The semantic cache reuses identical text embeddings/cosine scores and refreshes only lexical inputs and rank fusion. This change was made after development review and is not a new held-out validation.
