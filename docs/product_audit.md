# Product verification and current review status — 5 November 2026

The original product audit covered retrieval evaluation, the generalization pilot, actionable atlas gaps and the research workflow. Browser and JavaScript checks described below were performed during that audit. The review counts and generated evaluation results were refreshed after the 5 November validation-and-rebuild merge. Presentation and pitch work remain outside this audit.

| Area | Status |
| --- | --- |
| Retrieval comparison | Lexical, semantic and hybrid rankings are compared on the same two fully judged accounts, T009 and T012, using concordant completed submissions from both reviewers. These are assisted development metrics, not independently adjudicated or held-out scores. See the [current comparison report](human_retrieval_comparison.md). |
| Generalization | The new-paper pilot and ranking rules are frozen. All ten submitted decisions are unresolved. The evaluator withholds rankings and metrics until complete human review; no generalization result is available. |
| Atlas gaps | Gaps describe missing information, a next research step and a completion criterion. Sources and underlying comparisons remain accessible. Downloaded evidence reports include the completion criteria. |
| Research workflow | Browser checks passed for all twelve accounts, three rankers and desktop, tablet and phone widths. |

## Review state

The current inputs contain 66 named retrieval-review submissions across 33 distinct pairs, with Alex Karadjov and Nikolay Machev each represented. Both reviewers have matching completed decisions on 28 pairs. Four pairs remain unresolved or pending, and one pair is provisional. The two fully judged accounts are T009 and T012. Concordant submissions are counted for assisted development reporting, not represented as independently adjudicated gold. Individual reviewer records remain intact. No final retrieval-relevance adjudication is inferred.

Reviewer A's 20 RC001–RC020 comparison cases remain pending. Reviewer B, Alex Karadjov, has 20 completed assisted comparison judgments following explicit review and approval of the AI-prepared drafts: 6 insufficient evidence and 14 not directly comparable. Reviewer B also has 20 recorded extraction-verification confirmations. Reviewer A has zero extraction-verification confirmations in the current reviewer form. No comparison case has a final independent adjudication, and experimental-finding direction labels have not received a separate completed review. The 20 approved Reviewer B labels explicitly record assistant-proposal exposure and do not qualify as blinded independent labels. Retrieval relevance, comparison judgments, extraction verification and adjudication are distinct review tasks.

TX001 and TX002 carry Alex Karadjov's reviewer-reported verification attestations, but their source-level `human_verified` flags remain false pending the specific page, method and figure checks documented in [remaining source reviews](next_reviews.md). All ten new-paper pilot reviews remain unresolved.

## Checks performed

- In the latest GitHub Actions validation-and-rebuild run, 55 Python tests, review-link checks, evaluation scripts and the generated-file freshness check passed. The prior product audit separately reported passing both JavaScript suites and browser checks. These were not rerun as part of the latest Python validation workflow.
- Review-link validation passed. This validates identifiers and relationships, not source accuracy.
- The browser suite exercised all accounts and rankers at widths of 1280, 768 and 375 pixels, account search, empty results, gap drill-down, clearing the drill-down and the evaluation page.
- Nine downloaded reports retained their citations. Switching rankers preserved the E004 part mismatch and its source.
- No JavaScript errors, local asset failures or page-wide horizontal overflow occurred. The atlas has its own scrolling region.
- Source-link navigation was tested using an intercepted response. External availability was checked separately.

An external GET check of 35 source URLs returned five HTTP 200 responses, 29 HTTP 203 responses and one HTTP 403 response. The blocked URL was the USDA Ag Data Commons record for Dr. Duke's databases. No 404 or 410 was returned. These responses do not establish full-text access, content correctness or reuse permission; HTTP 203 may reflect an intermediary. Original citations are retained.

## Reproduce

From the repository root:

```sh
python3 scripts/rebuild.py --check
python3 -m unittest discover -s tests
node tests/test_web.cjs
node tests/test_reports.cjs
python3 scripts/validate_review_links.py
python3 scripts/evaluate_generalization.py
```

The optional browser suite requires Playwright and Chromium:

```sh
npm install --no-save playwright
npx playwright install chromium
node tests/browser_workflow.cjs
```

A separately installed Chromium can be selected with `BROWSER_EXECUTABLE`; `BROWSER_ARGS` accepts a JSON array of launch arguments. Browser dependencies are only needed for this test, not for running the app.

Remaining research tasks include Reviewer A's 20 case-level comparison judgments, formal adjudication, four unresolved or pending relevance pairs, one provisional relevance pair, the source-specific TX001/TX002 checks, and source review of the ten pilot candidates. Unreachable sources should remain unresolved. Reviewers should follow the frozen pilot protocol without seeing ranking positions or assistant labels.

Current evaluation figures are maintained in [the generated human retrieval comparison](human_retrieval_comparison.md) and `data/evaluation/baseline_report.json`. The README summarizes those results. When review inputs change, rerun `python3 scripts/rebuild.py` and update this audit.
