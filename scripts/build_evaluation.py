"""Build the offline evaluation page data from current reviews and seeded checks."""
import json,hashlib
from evaluate import evaluate
from review_progress import report
from retrieve import ROOT

def build():
    current,_=evaluate()
    historical=json.loads((ROOT/'data/evaluation/retrieval_comparison.json').read_text())
    value={'current':current,'review':report(),'ranking_comparison':historical,
           'limitations':['All comparisons are development cases, not a held-out test set.',
           'Seeded-link recall measures recovery of known links, not all relevant literature.',
           'Reviewer A confirmed assistant-proposed judgments; agreement is not independent accuracy.',
           'No independent scientific accuracy or clinical efficacy is established.',
           'Related papers and experiments must stay grouped in future evaluation splits.'],
           'snapshot_sha256':hashlib.sha256(json.dumps(current,sort_keys=True).encode()).hexdigest()}
    (ROOT/'web/evaluation-data.js').write_text('window.ETHNOTRACE_EVALUATION = '+json.dumps(value,ensure_ascii=False).replace('<','\\u003c')+';\n')
    return value
if __name__=='__main__':build();print('Built evaluation snapshot from current review files.')
