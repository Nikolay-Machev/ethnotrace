# Comparison adjudication readiness: RC001–RC020

Reviewer A: Nikolay-Machev. Reviewer B: Alex Karadjov.

Reviewer B explicitly approved 20 AI-prepared case-level draft judgments. Each was imported as a completed assisted review, with independent blinded annotation explicitly false. Reviewer A's 20 current case records have no completed labels, rationales or source-locator decisions.

Formal adjudication is blocked for all 20 cases because no completed Reviewer A comparison decisions are present. There is no evidence of case-level agreement, disagreement, or consensus. The adjudication records now identify both reviewers but retain pending status, null labels, null disagreement flags and null rationales.

| Case | Reviewer A label | Alex Karadjov label | Adjudication |
| --- | --- | --- | --- |
| RC001 | pending | insufficient_evidence (assisted) | pending |
| RC002 | pending | insufficient_evidence (assisted) | pending |
| RC003 | pending | not_directly_comparable (assisted) | pending |
| RC004 | pending | not_directly_comparable (assisted) | pending |
| RC005 | pending | insufficient_evidence (assisted) | pending |
| RC006 | pending | insufficient_evidence (assisted) | pending |
| RC007 | pending | insufficient_evidence (assisted) | pending |
| RC008 | pending | not_directly_comparable (assisted) | pending |
| RC009 | pending | not_directly_comparable (assisted) | pending |
| RC010 | pending | insufficient_evidence (assisted) | pending |
| RC011 | pending | not_directly_comparable (assisted) | pending |
| RC012 | pending | not_directly_comparable (assisted) | pending |
| RC013 | pending | not_directly_comparable (assisted) | pending |
| RC014 | pending | not_directly_comparable (assisted) | pending |
| RC015 | pending | not_directly_comparable (assisted) | pending |
| RC016 | pending | not_directly_comparable (assisted) | pending |
| RC017 | pending | not_directly_comparable (assisted) | pending |
| RC018 | pending | not_directly_comparable (assisted) | pending |
| RC019 | pending | not_directly_comparable (assisted) | pending |
| RC020 | pending | not_directly_comparable (assisted) | pending |

## What must happen before final adjudication

1. Nikolay completes the case-level Reviewer A entries using checked source evidence, the supported five-label scheme, rationales, locators, and truthful review provenance. If the Reviewer A decision is assisted or not blinded, record this explicitly.
2. Compare each A and B judgment, determine whether the labels differ, and document why. Consensus should be based on evidence rather than copying a prior proposed answer.
3. Fill the existing `data/review/adjudicated.jsonl` with the supported final label, retrieval relevance, rationale, agreement or disagreement indicator, matched source locators, and other adjudicated dimensions. Leave unresolved items pending.
4. `scripts/evaluate.py` requires both reviewers to have documented independently blinded source annotations before accepting a case into its independent gold accuracy metric. The currently approved Reviewer B judgments do **not** meet this criterion. If the team wants assisted consensus labels, store and report them separately, or revise the evaluation protocol transparently without describing them as independent gold.
5. Regenerate and validate reports following any review changes.

This document summarizes source-repository records. It is not an additional scientific source review.
