"""Validate review entries and report readiness without converting assistant work to human review."""
import json
from retrieve import ROOT, rows

def report():
    candidates=rows(ROOT/'data/review/retrieval_relevance.jsonl')
    grouped = {}
    for record in candidates:
        grouped.setdefault((record['claim_id'], record['evidence_id']), []).append(record)
    unique = []
    for key, records in grouped.items():
        if len(records) > 1:
            # Multiple unresolved reviewer entries are not duplicate final judgments.
            # Refuse to combine any completed/boolean decisions without adjudication.
            if any(r.get('human_retrieval_relevant') is not None or r.get('human_review_status') == 'completed' for r in records):
                raise ValueError('Multiple final relevance judgments require adjudication: '+str(key))
            q = dict(next((r for r in records if r.get('human_review_status') == 'provisional'), records[0]))
            q['source_checked'] = any(r.get('source_checked') is True for r in records)
            unique.append(q)
        else:
            unique.append(records[0])
    submission_count = len(candidates)
    candidates = unique
    seen=set(); complete=0
    for q in candidates:
        key=(q['claim_id'],q['evidence_id'])
        if key in seen: raise ValueError('Duplicate relevance judgment: '+str(key))
        seen.add(key)
        if q['human_review_status']=='completed':
            if not (type(q['human_retrieval_relevant']) is bool and q.get('human_rationale') and q.get('human_reviewer_id') and q.get('source_checked') is True):
                raise ValueError('Completed relevance review requires decision, rationale, reviewer and source check: '+str(key))
            complete+=1
    reviewers={key:rows(ROOT/f'data/review/reviewer_{key}.jsonl') for key in ('a','b')}
    return {'relevance_candidates':len(candidates),'review_submission_count':submission_count,'human_relevance_completed':complete,
            'human_relevance_provisional':sum(q.get('human_review_status')=='provisional' for q in candidates),
            'source_checked_unresolved':sum(q.get('source_checked') is True and q.get('human_retrieval_relevant') is None and q.get('human_review_status')!='provisional' for q in candidates),
            'comparison_reviews':{k:sum(r.get('comparison_review_status')=='completed' for r in rs) for k,rs in reviewers.items()},
            'note':'Reported counts are not independent scientific accuracy. Do not start a semantic retrieval performance comparison until the chosen queries have complete human relevance judgments.'}
if __name__=='__main__':print(json.dumps(report(),indent=2))
