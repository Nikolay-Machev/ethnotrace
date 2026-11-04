"""Validate review entries and report readiness without converting assistant work to human review."""
import json
from retrieve import ROOT, rows

def report():
    candidates=rows(ROOT/'data/review/retrieval_relevance.jsonl')
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
    return {'relevance_candidates':len(candidates),'human_relevance_completed':complete,
            'source_checked_unresolved':sum(q.get('source_checked') is True and q.get('human_retrieval_relevant') is None for q in candidates),
            'comparison_reviews':{k:sum(r.get('comparison_review_status')=='completed' for r in rs) for k,rs in reviewers.items()},
            'note':'Reported counts are not independent scientific accuracy. Do not start a semantic retrieval performance comparison until the chosen queries have complete human relevance judgments.'}
if __name__=='__main__':print(json.dumps(report(),indent=2))
