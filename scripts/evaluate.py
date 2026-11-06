"""Report development checks separately from metrics on independently adjudicated cases."""
import argparse
from math import fsum
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from retrieve import ROOT, VERSION, Baseline, rows

LABELS = {'support', 'no_detected_effect', 'mixed_evidence', 'not_directly_comparable', 'insufficient_evidence'}

def evaluate(root=ROOT):
    b = Baseline(root)
    cases = rows(root / 'data/review/review_cases.jsonl')
    expected = rows(root / 'data/evaluation/development_expectations.jsonl')
    gold = rows(root / 'data/review/adjudicated.jsonl')
    ar_rows = rows(root / 'data/review/reviewer_a.jsonl')
    cr_rows = rows(root / 'data/review/reviewer_b.jsonl')
    a = {r['case_id']: r for r in ar_rows}
    c = {r['case_id']: r for r in cr_rows}
    known = {r['case_id'] for r in cases}
    if len(known) != len(cases) or {r['case_id'] for r in expected} != known or {r['case_id'] for r in gold} != known:
        raise ValueError('Missing or duplicate evaluation case IDs')
    if any(len(rs) != len(known) or {r['case_id'] for r in rs} != known for rs in (expected, gold, ar_rows, cr_rows)):
        raise ValueError('Missing or duplicate review IDs')
    predictions, structural_taxon, membership, hits, reciprocal = [], [], [], [], []
    relevant = defaultdict(set)
    for r in expected:
        t, e = b.claims[r['traditional_record_id']], b.experiments[r['evidence_id']]
        prediction = b.compare(t, e)
        ids = [x['evidence_id'] for x in b.retrieve(r['traditional_record_id'], 1000)['results']]
        structural_taxon.append(prediction['taxon'] == r['expected_taxon'])
        membership.append((r['evidence_id'] in ids) == r['expected_retrieval_membership'])
        if r['expected_retrieval_membership']:
            relevant[r['traditional_record_id']].add(r['evidence_id'])
        predictions.append({'case_id': r['case_id'], 'traditional_record_id': r['traditional_record_id'],
                            'evidence_id': r['evidence_id'], 'comparison': prediction})
    for tid, truth in relevant.items():
        ranked = [x['evidence_id'] for x in b.retrieve(tid, 1000)['results']]
        hits.append(len(set(ranked[:5]) & truth) / len(truth))
        reciprocal.append(next((1 / (i + 1) for i, rid in enumerate(ranked) if rid in truth), 0))
    # Assisted consensus is a documented agreement, not independent gold.
    # Preserve missing retrieval judgments rather than guessing labels.
    assisted_consensus = []
    for r in gold:
        if r['status'] != 'assisted_consensus':
            continue
        ar, cr = a.get(r['case_id'], {}), c.get(r['case_id'], {})
        provenance = r.get('consensus_provenance') or {}
        if not (
            ar.get('status') == cr.get('status') == 'completed'
            and ar.get('comparison_review_status') == cr.get('comparison_review_status') == 'completed'
            and ar.get('reviewer_id') != cr.get('reviewer_id')
            and r.get('reviewer_a') == ar.get('reviewer_id')
            and r.get('reviewer_b') == cr.get('reviewer_id')
            and ar.get('pair_label') == cr.get('pair_label') == r.get('pair_label')
            and r['pair_label'] in LABELS
            and r.get('disagreement') is False
            and r.get('rationale')
            and r.get('source_locators')
            and ar.get('rationale') and cr.get('rationale')
            and ar.get('source_locators') and cr.get('source_locators')
            and all(r.get(field) == ar.get(field) == cr.get(field) for field in ('taxon', 'plant_part', 'solvent', 'outcome'))
            and r.get('retrieval_relevant') is None
            and provenance.get('independently_blinded') is False
            and provenance.get('independent_gold_eligible') is False
        ):
            raise ValueError('Invalid assisted comparison consensus: ' + r['case_id'])
        assisted_consensus.append(r)
    # Gold metrics require two distinct completed source reviewers plus explicit adjudication.
    accepted = []
    for r in gold:
        if r['status'] != 'adjudicated': continue
        ar, cr = a.get(r['case_id'], {}), c.get(r['case_id'], {})
        if not (ar.get('status') == cr.get('status') == 'completed' and ar.get('reviewer_id') and cr.get('reviewer_id')
                and ar['reviewer_id'] != cr['reviewer_id'] and r['reviewer_a'] == ar['reviewer_id'] and r['reviewer_b'] == cr['reviewer_id']
                and r['pair_label'] in LABELS and type(r['retrieval_relevant']) is bool and r['rationale'] and r['source_locators']
                and ar.get('rationale') and cr.get('rationale') and ar.get('source_locators') and cr.get('source_locators')
                and ar.get('pair_label') in LABELS and cr.get('pair_label') in LABELS and r.get('disagreement') is not None
                and all(x.get('comparison_review_provenance', {}).get('independent_blinded_annotation') is True for x in (ar, cr))):
            raise ValueError('Adjudicated case lacks independent review provenance: ' + r['case_id'])
        accepted.append(r)
    by_case = {r['case_id']: r for r in predictions}
    accuracy = sum(by_case[r['case_id']]['comparison']['status'] == r['pair_label'] for r in accepted) / len(accepted) if accepted else None
    # Report query-level retrieval only when a complete candidate judgement set exists for that query.
    gold_recall = []
    by_tid = defaultdict(list)
    for r in accepted: by_tid[by_case[r['case_id']]['traditional_record_id']].append(r)
    for tid, judged in by_tid.items():
        ranked = [x['evidence_id'] for x in b.retrieve(tid, 1000)['results']]
        judged_ids = {by_case[r['case_id']]['evidence_id'] for r in judged}
        positive = {by_case[r['case_id']]['evidence_id'] for r in judged if r['retrieval_relevant']}
        if set(ranked) <= judged_ids and positive:
            gold_recall.append(len(set(ranked[:5]) & positive) / len(positive))
    review_progress = {}
    for key, records in (('a', ar_rows), ('b', cr_rows)):
        completed = [r for r in records if r.get('comparison_review_status') == 'completed']
        for r in records:
            if r.get('schema_version') != 2:
                raise ValueError('Expected review schema version 2')
            if r.get('pair_label') != r.get('claim_comparability', {}).get('label'):
                raise ValueError('Conflicting comparability labels: ' + r['case_id'])
        agreement = sum(by_case[r['case_id']]['comparison']['status'] == r['pair_label'] for r in completed)
        review_progress[key] = {
            'extraction_verified_cases': sum(r.get('extraction_verified') is True for r in records),
            'comparison_completed_cases': len(completed),
            'comparison_pending_cases': len(records) - len(completed),
            'assisted_comparison_cases': sum(r.get('comparison_review_provenance', {}).get('independent_blinded_annotation') is False for r in completed),
            'baseline_label_agreement': agreement / len(completed) if completed else None,
            'warning': 'Reviewer agreement is not held-out accuracy; assisted confirmations are not independent gold.',
            'experimental_finding_label_reviews': sum(r.get('experimental_findings_review_status') == 'completed' for r in records)}
    report = {'review_progress': review_progress,
              'assisted_comparison_consensus': {
                  'completed_cases': len(assisted_consensus),
                  'matching_labels': len(assisted_consensus),
                  'disagreement_cases': 0 if assisted_consensus else None,
                  'label_distribution': {
                      label: sum(r['pair_label'] == label for r in assisted_consensus)
                      for label in sorted(LABELS) if any(r['pair_label'] == label for r in assisted_consensus)
                  },
                  'independent_gold_eligible': False,
                  'retrieval_relevance_adjudicated': 0,
                  'note': 'Assisted agreement between completed reviews, not independently blinded adjudication or held-out gold.'
              },
              'experimental_findings_evaluation': {'status': 'no_separate_result_direction_gold', 'accuracy': None,
                  'note': 'Extraction verification is recorded separately. Finding directions are source-derived metadata, not model predictions evaluated against independent labels.'},
              'baseline_version' : VERSION, 'case_count': len(cases), 'index_documents': len(b.documents),
              'scope': 'development set, not held-out; known source/programme blocks retained',
              'development_checks': {'scientific_name_taxon_agreement': sum(structural_taxon) / len(structural_taxon),
                                     'species_gate_membership_agreement': sum(membership) / len(membership),
                                     'macro_recall_at_5_for_seeded_links': fsum(hits) / len(hits),
                                     'mean_reciprocal_rank_for_seeded_links': fsum(reciprocal) / len(reciprocal),
                                     'query_count': len(relevant),
                                     'warning': 'Seeded expectations use curated names/links and test implemented structure. These are not independently reviewed relevance or scientific accuracy scores.'},
              'independent_review': {'adjudicated_cases': len(accepted), 'comparison_accuracy': accuracy,
                                     'complete_retrieval_query_count': len(gold_recall),
                                     'macro_recall_at_5': fsum(gold_recall) / len(gold_recall) if gold_recall else None,
                                     'status': 'no_independent_gold_available' if not accepted else 'development_gold_only'},
              'input_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root / 'data/review').glob('*.jsonl'))}}
    return report, predictions

if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--output', type=Path, default=ROOT / 'data/evaluation'); args = parser.parse_args()
    report, predictions = evaluate()
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'baseline_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    (args.output / 'baseline_predictions.jsonl').write_text(''.join(json.dumps(p, ensure_ascii=False, sort_keys=True) + '\n' for p in predictions))
    print(json.dumps(report, indent=2))
