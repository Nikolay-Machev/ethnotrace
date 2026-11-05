# Alex Karadjov and Nikolay Machev: retrieval-review difference audit

Generated from `data/review/retrieval_relevance.jsonl`. This is a comparison of existing reviewer submissions, not an adjudicated gold standard.

## Summary

- Candidate pairs with both named reviewer records: 33.
- Same broad decision category: 31.
- Different broad category: 2.
- Different exact recorded statuses/decisions: 4.
- Two substantive differences are safety-only T008 papers where Alex remained unresolved and Nikolay selected context only.
- The other two status differences represent unresolved versus pending. Both signal that the evidence is not finalized.
- The T010/P20301057 provisional decision is shared, but it is not a confirmed true/false relevance judgment.

## Items needing follow-up

| Candidate | Alex Karadjov | Nikolay Machev | Next action |
| --- | --- | --- | --- |
| T008/P21186373 | Unresolved | Context only | Record whether Alex accepts the safety-only exclusion rule or remains unresolved after discussion. |
| T008/P26626249 | Unresolved | Context only | Resolve the relevance scope for transcriptional-safety findings without inventing a glucose or infection outcome. |
| T007/P18066122 | Unresolved | Pending (unresolved rationale) | Obtain Larix-specific source evidence, otherwise keep unresolved. |
| T011/P19526043 | Unresolved | Pending (unresolved rationale) | Obtain lingonberry-specific assay mapping, otherwise keep unresolved. |
| T010/P20301057 | Provisional | Provisional | Primary source confirmation is missing, so preserve provisional status. |

## Full side-by-side index

| Candidate | Alex Karadjov | Nikolay Machev | Match? |
| --- | --- | --- | --- |
| T007/E001 | useful | useful | Yes |
| T007/E002 | useful | useful | Yes |
| T007/P18066122 | unresolved/pending | unresolved/pending | Yes |
| T007/P22542642 | useful | useful | Yes |
| T007/P23864882 | useful | useful | Yes |
| T007/P27773798 | context_only | context_only | Yes |
| T008/E003 | useful | useful | Yes |
| T008/E004 | useful | useful | Yes |
| T008/P21186373 | unresolved/pending | context_only | No |
| T008/P22738356 | useful | useful | Yes |
| T008/P26626246 | useful | useful | Yes |
| T008/P26626249 | unresolved/pending | context_only | No |
| T009/E005 | useful | useful | Yes |
| T009/P19665535 | context_only | context_only | Yes |
| T009/P20738101 | useful | useful | Yes |
| T009/P27833811 | context_only | context_only | Yes |
| T010/E006 | useful | useful | Yes |
| T010/E007 | useful | useful | Yes |
| T010/P20301057 | provisional | provisional | Yes |
| T010/P22504062 | useful | useful | Yes |
| T011/E008 | useful | useful | Yes |
| T011/E009 | useful | useful | Yes |
| T011/E011 | useful | useful | Yes |
| T011/E012 | useful | useful | Yes |
| T011/P19526043 | unresolved/pending | unresolved/pending | Yes |
| T011/P19927274 | context_only | context_only | Yes |
| T011/P20087853 | useful | useful | Yes |
| T012/E010 | useful | useful | Yes |
| T012/P19665535 | context_only | context_only | Yes |
| T012/P25916863 | useful | useful | Yes |
| T012/P26508979 | useful | useful | Yes |
| T012/P26707751 | useful | useful | Yes |
| T012/P26916332 | context_only | context_only | Yes |

## Scope and provenance

The submitted `Alex-Karadjov-review-records.docx` contains 33 retrieval relevance entries, with claim IDs T007–T012 and evidence IDs. It is not a set of case-level comparability adjudications for RC001–RC020. The existing `data/review/adjudicated.jsonl` remains pending for all 20 cases. This audit does not manufacture a consensus label, a comparison rationale, a source locator, a review date, or independent blinded review.

To adjudicate RC001–RC020, both corresponding reviewer files must carry completed case-specific comparison judgments and recorded provenance before a defensible final adjudication and evaluation.
