"""Build the offline evaluation page data from current reviews and seeded checks."""
import json,hashlib
from math import comb, fsum
from statistics import mean
from evaluate import evaluate
from review_progress import report
from evaluate_retrieval import evaluate as semantic_evaluation
from retrieve import ROOT,rows

def random_expectation(n,m):
    # Uniform permutations of n distinct candidates, m of which are seeded links.
    if not 1 <= m <= n: raise ValueError('Invalid seeded candidate pool')
    return min(5,n)/n, fsum(comb(n-i,m-1)/comb(n,m)/i for i in range(1,n-m+2))

def benchmark(semantic):
    queries=[]
    for q in semantic['queries']:
        ids=q['methods']['lexical']['ranked_ids'];truth=set(q['seeded_links'])
        if not truth.issubset(ids): raise ValueError('Seeded link outside candidate pool')
        n=len(ids);m=len(truth);recall,mrr=random_expectation(n,m)
        queries.append(dict(claim_id=q['claim_id'],pool_size=n,seeded_links=m,recall_at_5=recall,mrr=mrr))
    pairs=[r['raw'] for r in rows(ROOT/'data/processed/extracted_claim_study_pairs.jsonl')]
    return dict(queries=queries,recall_at_5=mean(q['recall_at_5'] for q in queries),mrr=mean(q['mrr'] for q in queries),
                same_paper=sum(bool(p['traditional_source_url']) and p['traditional_source_url']==p['experimental_source_url'] for p in pairs),total_links=len(pairs))

def pilot_summary():
    from evaluate_generalization import check
    manifest, candidates, reviews, eligible = check()
    path = ROOT / 'data/generalization/assisted_exploratory_results.json'
    recorded = json.loads(path.read_text()) if path.exists() else None
    matches = bool(recorded and
        recorded.get('reviews_sha256') == hashlib.sha256((ROOT / 'data/generalization/reviews.jsonl').read_bytes()).hexdigest() and
        recorded.get('frozen_manifest_sha256') == hashlib.sha256((ROOT / 'data/generalization/manifest.json').read_bytes()).hexdigest() and
        recorded.get('evaluation_track') == 'assisted_exploratory_not_independent_blinded')
    return {'candidate_count': len(candidates),
            'assisted_completed': sum(r.get('review_status') == 'completed_assisted_not_blinded' for r in reviews),
            'independent_blinded_eligible': eligible,
            'recorded_result_current': matches,
            'result': recorded if matches else None}

def build():
    current,_=evaluate()
    historical=json.loads((ROOT/'data/evaluation/retrieval_comparison.json').read_text())
    sem=semantic_evaluation()
    value={'assisted_pilot':pilot_summary(),'random_benchmark':benchmark(sem) if sem else None,'semantic_comparison':sem,'current':current,'review':report(),'ranking_comparison':historical,
           'limitations':['All comparisons are development cases, not a held-out test set.',
           'Seeded-link recall measures recovery of known links, not all relevant literature.',
           'Earlier development review included assistant-proposed judgments; current review counts are reported separately.',
           'No independent scientific accuracy or clinical efficacy is established.',
           'Related papers and experiments must stay grouped in future evaluation splits.'],
           'snapshot_sha256':hashlib.sha256(json.dumps(current,sort_keys=True).encode()).hexdigest()}
    (ROOT/'web/evaluation-data.js').write_text('// Generated, do not edit. Run python3 scripts/rebuild.py.\nwindow.ETHNOTRACE_EVALUATION = '+json.dumps(value,ensure_ascii=False).replace('<','\\u003c')+';\n')
    return value
if __name__=='__main__':build();print('Built evaluation snapshot from current review files.')
