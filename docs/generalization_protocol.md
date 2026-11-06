# New-paper generalization pilot v1

Status: awaiting named human review. All ten candidate publications now have an assistant-prepared [source evidence report](generalization_source_followup_2026-11-05.md) with nine useful and one context-only research assessments. These are not human labels. The ten frozen human-review rows remain unresolved, and no pilot rankings or performance results have been produced.

## Question and scope

Does frozen retrieval transfer to new papers for two existing traditional accounts? Six lingonberry papers and four pitcher-plant papers are held outside the development corpus and atlas. This tests candidate transfer, not new accounts, Nations or plants.

The ten papers were selected by assistant searches on 4 November 2026 for lingonberry postprandial/metabolic/oral research and pitcher-plant laboratory research. This is a purposive convenience sample, not an exhaustive or random literature sample. Selection was not based on ranker scores. The packet has no assistant relevance judgments. Authentic publication titles can themselves describe findings.

## Frozen before human relevance review

data/generalization/manifest.json pins the baseline commit, rule code, model revision, candidate metadata, traditional account snapshots and packet by SHA-256. Changes fail validation; create a new pilot version rather than silently overwriting the freeze.

All candidates are bibliographic leads. Scoring inputs are species and published title. Part, solvent and endpoint are unextracted for every candidate. These remain missing even if the reviewer learns more, so answers cannot alter ranker inputs. The original lexical scorer, pretrained semantic encoder, normalization, truncation and reciprocal-rank fusion remain unchanged. No tuning or fine-tuning on this pilot.

Candidates were checked against existing indexed publication IDs, DOIs and titles. Different papers may still share authors, participants or experiments; this has not been ruled out. Record any overlap during review. No claim of independent study groups is made.

## Review first

Open [the unranked packet](generalization_review_packet.md). Enter ten source-based decisions in data/generalization/reviews.jsonl. Each source needs url and depth (section, table or abstract). Decisions: useful, context_only or unresolved. Missing access stays unresolved. Apply the existing relevance rule and original symptom wording.

Declare whether you previously reviewed this pair or saw rankings/assistant labels. Neither declaration is prefilled. Exposure prevents a blinded-pilot claim: seek another reviewer or report that limitation under a separate protocol. Familiarity with the traditional account alone is not prior review of the new pair.

## Validation and scoring

Run from the repository root:

    python scripts/evaluate_generalization.py

This checks the freeze and readiness without inference or rankings. Scoring requires every pair to have a documented useful/context-only decision and truthful declarations of no prior pair review or ranking/label exposure. Do not turn unresolved into context just to unlock scoring.

After completing review, install the existing requirements-semantic.txt in the semantic environment and run:

    python scripts/evaluate_generalization.py --score

The frozen model revision may require a first download. Output goes to data/generalization/results.json, separate from development evaluation. No API key is required.

Report precision/recall at five per account and at three as a preregistered secondary measure. Pitcher plant has only four candidates, so top-five recall cannot distinguish ordering there. Precision@5 uses five slots including empty slots; recall uses useful candidates in that pool. Zero-useful recall is unavailable.

Two related, purposively selected accounts support only an exploratory pilot. No statistical significance or broad generalization claim. Lexical stays the deployed default pending a separate decision.
