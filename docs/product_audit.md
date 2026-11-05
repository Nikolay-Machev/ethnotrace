# Product verification — 5 November 2026

This check covers retrieval evaluation, the generalization pilot, actionable atlas gaps and the research workflow. Presentation and pitch work is outside its scope.

| Area | Status |
| --- | --- |
| Retrieval comparison | Lexical, semantic and hybrid rankings are evaluated on the same three completely judged development accounts. Provisional and unresolved pairs are excluded. See the [comparison report](human_retrieval_comparison.md). |
| Generalization | The new-paper pilot and ranking rules are frozen. All ten submitted decisions are unresolved. The evaluator withholds rankings and metrics until complete human review; no generalization result is available. |
| Atlas gaps | Gaps describe missing information, a next research step and a completion criterion. Sources and underlying comparisons remain accessible. Downloaded evidence reports include the completion criteria. |
| Research workflow | Browser checks passed for all twelve accounts, three rankers and desktop, tablet and phone widths. |

## Review state

The current inputs contain 36 retrieval-review submissions for 33 distinct pairs: 30 confirmed decisions, one provisional pair and two unresolved pairs. Separate unresolved submissions are counted once per pair without changing either review. Multiple final submissions require adjudication rather than silently selecting one.

Both comparison-review files currently mark their twenty cases pending, with no completed extraction verifications. The interface reports these current records rather than the earlier completion claims. Retrieval relevance, comparison judgments and extraction verification are separate review tasks. No human review records were edited during this product check.

## Checks performed

- 55 Python tests, both JavaScript suites and the generated-file freshness check passed.
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

The remaining research task is source review of the ten pilot candidates. Unreachable sources should remain unresolved. Reviewers should follow the frozen protocol without seeing ranking positions or assistant labels.
