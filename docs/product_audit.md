# Product integration verification — 5 November 2026

The product now displays the current review state, supplementary source evidence and separate assisted pilot results. This integration changes code, documentation and generated reports; source records, reviewer submissions, pilot reviews, the manifest and frozen files are unchanged.

| Area | Current status |
| --- | --- |
| Retrieval review | 66 submissions across 33 pairs, all with matching completed decisions. Six development accounts are scored. |
| Comparison review | Both reviewers completed 20 cases. All labels match: six insufficient evidence and 14 not directly comparable. These are assisted consensus, not independent gold. |
| Extraction verification | Reviewer B has 20 confirmations; reviewer A has zero recorded extraction confirmations. TX001 and TX002 have confirmed source packets with assisted provenance. |
| New-paper pilot | Ten assisted approvals and a recorded exploratory result. All methods have macro P@5 0.800 and R@5 0.900. Independent blinded generalization remains unavailable. |
| Supplementary evidence | Source-supported context, original values, uncertainty, URLs and locators appear under each account's gaps and in its report. Original fields and comparison labels remain unchanged. |

## Integration safeguards

Current evaluation uses `scripts/evaluate_retrieval.py`. It reconciles all submitted reviews rather than choosing the final row. Pending or provisional companion reviews exclude the account; conflicting final decisions stop evaluation for adjudication. Matching reviews use deterministic reviewer ordering for the displayed rationale. The underlying submissions remain separate.

The historical evaluator and other checksum-frozen pilot files remain unchanged. The current evaluation page displays saved exploratory results only when their review and manifest hashes match current inputs. It does not run inference or claim independent validation.

Current aggregate metrics use `math.fsum`. Clean generated-file checks pass under Python 3.11 and 3.12 without rewriting outputs. CI tests both versions and runs both JavaScript suites; it has read-only repository permissions.

## Validation

- 63 Python tests pass under Python 3.11 and 3.12.
- Both JavaScript suites pass, including current counts, supplemental citations, targeted verification provenance and the stale-pilot-result fallback.
- Generated outputs pass a clean rebuild check under both Python versions.
- Review identifiers and links pass validation. This does not independently verify scientific source passages.
- Browser checks pass across all twelve accounts, all three rankers, and widths of 1280, 768 and 375 pixels. They cover filtering, empty states, gap drill-down, supplementary source expansion, status text and the evaluation page.
- Nine browser downloads retained citations and full-account scope while switching rankers. No JavaScript errors, local asset failures or page-wide overflow were observed.
- External source navigation was intercepted to test click behavior. External publisher availability was not rechecked during this integration.

## Reproduce

```sh
python3 scripts/rebuild.py --check
python3 -m unittest discover -s tests
node tests/test_web.cjs
node tests/test_reports.cjs
python3 scripts/validate_review_links.py
python3 scripts/evaluate_assisted_generalization.py --check
```

Optional browser checks require Playwright and Chromium:

```sh
npm install --no-save playwright
npx playwright install chromium
node tests/browser_workflow.cjs
```

A separately installed Chromium can be selected with `BROWSER_EXECUTABLE`; `BROWSER_ARGS` accepts a JSON array of launch arguments. These dependencies are not required to view the app.

The scientific limitations remain: assisted review is not independent accuracy evidence, supplementary community context does not establish an original account's missing recipe, and preclinical findings do not establish clinical efficacy. See the [retrieval comparison](human_retrieval_comparison.md) and [assisted pilot report](archive/assisted_generalization_results_2026-11-05.md). Pitch preparation remains outside this work.

## Cleanup — 6 November 2026

Python support is documented as 3.11 and 3.12, matching CI. Code and original technical documentation are MIT licensed; source-material rights are excluded. Earlier phase notes are archived under `docs/archive/`.

The 66 current relevance submissions are separated from their full historical snapshots. Eight approved follow-up rows had obsolete unresolved fields; these now use the approved source checks and explanations. Decisions and rationales are unchanged. The validator rejects an active unresolved reason on a completed row while permitting genuine scientific uncertainty.

Development baseline 1.2 removes the plant-part mismatch penalty. E004 increases from score 8 to 10 but remains sixth. All candidate orders, and therefore retrieval metrics, remain unchanged. The browser shows part comparison separately. Frozen pilot files and scientific inputs remain unchanged.

## Documentation verification — 6 November 2026

Checked the current code and visual update at `885c9f0ac2e8f1c47b85c8e5cdbba6aa51a182b9`. Corrected stale relevance/comparison progress, separate finding-review status, baseline 1.2 explanations, schema guidance and rebuild instructions. Historical frozen protocol status is explicitly distinguished from current pilot results. Review rationales retain their submitted wording and source-access limitations; current completion status comes from the structured review fields.

The documented clean rebuild and freshness check pass. All 77 Python tests pass on 3.11 and 3.12; both JavaScript suites pass. The real-browser workflow passes for 12 accounts, three rankers, widths 1280/768/375 and nine cited-report downloads, with no JavaScript or local HTTP errors. Review-link validation and the assisted-pilot preflight pass. Local Markdown file links and heading anchors were checked and one archived heading link was repaired.

This check does not reverify every scientific passage, rerun model inference, establish external publisher availability, or verify final Devpost/video/slide submission. Source data and review records were not edited.
