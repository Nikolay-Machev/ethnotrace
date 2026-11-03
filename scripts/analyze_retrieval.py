"""Compare ranking versions on seeded development links and prepare a relevance queue."""
import json
from collections import defaultdict
from retrieve import Baseline, ROOT, rows, tokenise

class LegacyBaseline(Baseline):
    def score(self, claim, evidence):
        score = super().score(claim, evidence)
        if score is None: return None
        query = tokenise(claim['raw'].get('original_use_description'))
        target = tokenise(evidence['raw'].get('endpoint') or evidence['raw'].get('title'))
        lexical = len(query & target) / len(query | target) if query | target else 0
        return {**score, 'lexical': lexical, 'total': score['total'] - score['lexical'] + lexical}

def analyze():
    old, new = LegacyBaseline(), Baseline()
    truth = defaultdict(set)
    for r in rows(ROOT/'data/evaluation/development_expectations.jsonl'):
        if r['expected_retrieval_membership']: truth[r['traditional_record_id']].add(r['evidence_id'])
    metrics = {}; comparisons = []; queue = []
    for version, b in [('1.0', old), ('1.1', new)]:
        recalls=[]; reciprocal=[]
        for tid, linked in truth.items():
            ranked=b.retrieve(tid,1000)['results']; ids=[r['evidence_id'] for r in ranked]
            recalls.append(len(set(ids[:5]) & linked)/len(linked))
            reciprocal.append(next((1/(i+1) for i,e in enumerate(ids) if e in linked),0))
            comparisons.append({'version':version,'claim_id':tid,'seeded_links':sorted(linked),'ranked_ids':ids,'missed_at_5':sorted(linked-set(ids[:5]))})
            if version=='1.1':
                for rank,r in enumerate(ranked,1):
                    extracted=r['evidence_id'] in b.experiments
                    queue.append({'claim_id':tid,'evidence_id':r['evidence_id'],'rank':rank,'source':r['source'],
                        'claim_source_url':b.claims[tid]['raw'].get('source_url'),
                        'provisional_retrieval_relevant':True if extracted else None,
                        'rationale':('An extracted same-species experiment provides evidence or a documented mismatch useful for assessing this account. This does not imply claim support.' if extracted else 'Same-species title-screened literature lead. Full source assessment is needed before a relevance judgment.'),
                        'annotation_method':'assistant_prepared_from_existing_extraction_and_metadata',
                        'human_retrieval_relevant':None,'human_rationale':None,'human_review_status':'pending'})
        metrics[version]={'macro_recall_at_5':sum(recalls)/len(recalls),'mrr':sum(reciprocal)/len(reciprocal)}
    report={'scope':'six development queries; seeded links, not independent relevance gold','metrics':metrics,'queries':comparisons}
    out=ROOT/'data/evaluation';(out/'retrieval_comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    # Never overwrite later human judgments.
    p=ROOT/'data/review/retrieval_relevance.jsonl'
    existing={(r['claim_id'],r['evidence_id']):r for r in rows(p)} if p.exists() else {}
    for r in queue:
        prev=existing.get((r['claim_id'],r['evidence_id']),{})
        for field in ('human_retrieval_relevant','human_rationale','human_review_status','human_reviewer_id','source_checked','traditional_context','experimental_context','targeted_extraction_id'):
            if field in prev:r[field]=prev[field]
        if prev.get('annotation_method')=='assistant_targeted_source_inspection_not_human_review':
            for field in ('annotation_method','provisional_retrieval_relevant','rationale'): r[field]=prev[field]
    p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in queue))
    print(json.dumps({'metrics':metrics,'relevance_candidates':len(queue)}))
if __name__=='__main__':analyze()
