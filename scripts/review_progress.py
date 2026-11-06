"""Validate reviewer-level judgments without silently adjudicating between reviewers."""
import json
from collections import defaultdict
from retrieve import ROOT, rows


def grouped_review_records(records):
    """Return one conservative evaluation record per pair and reviewer diagnostics.

    Identical completed labels are reported as concordant submissions, not
    independently adjudicated gold. Missing or unfinished companion reviews
    block a pair from complete-query retrieval metrics.
    """
    grouped = defaultdict(list)
    for record in records:
        grouped[(record['claim_id'], record['evidence_id'])].append(record)

    unique = {}
    counts = {'concordant_completed_pairs': 0, 'discordant_completed_pairs': 0,
              'pairs_awaiting_review': 0, 'provisional_pairs': 0}
    for key, submissions in grouped.items():
        names = [r.get('human_reviewer_id') for r in submissions if r.get('human_reviewer_id')]
        if len(names) != len(set(names)):
            raise ValueError('Duplicate reviewer for relevance pair: ' + str(key))
        for r in submissions:
            if r.get('human_review_status') == 'completed':
                if 'unresolved_reason' in r or 'unresolved_reason' in r.get('human_review_details', {}):
                    raise ValueError('Completed relevance review retains unresolved_reason: ' + str(key))
                if not (type(r.get('human_retrieval_relevant')) is bool
                        and r.get('human_rationale') and r.get('human_reviewer_id')
                        and r.get('source_checked') is True):
                    raise ValueError('Completed relevance review requires decision, rationale, reviewer and source check: ' + str(key))
        finals = [r for r in submissions if r.get('human_review_status') == 'completed']
        values = {r['human_retrieval_relevant'] for r in finals}
        if len(values) > 1:
            counts['discordant_completed_pairs'] += 1
            raise ValueError('Multiple conflicting final relevance judgments require adjudication: ' + str(key))
        if finals and len(finals) == len(submissions):
            chosen = dict(min(finals, key=lambda r: r['human_reviewer_id']))
            counts['concordant_completed_pairs'] += 1
        else:
            chosen = dict(next((r for r in submissions if r.get('human_review_status') == 'provisional'),
                               next((r for r in submissions if r.get('human_review_status') in ('unresolved', 'pending')),
                                    submissions[0])))
            chosen['human_retrieval_relevant'] = None
            if any(r.get('human_review_status') == 'provisional' for r in submissions):
                chosen['human_review_status'] = 'provisional'
                counts['provisional_pairs'] += 1
            else:
                chosen['human_review_status'] = 'unresolved' if any(
                    r.get('human_review_status') == 'unresolved' for r in submissions) else 'pending'
                counts['pairs_awaiting_review'] += 1
            chosen['source_checked'] = any(r.get('source_checked') is True for r in submissions)
        unique[key] = chosen
    return unique, counts


def report():
    submissions = rows(ROOT / 'data/review/retrieval_relevance.jsonl')
    pairs, diagnostics = grouped_review_records(submissions)
    records = list(pairs.values())
    reviewers = {key: rows(ROOT / f'data/review/reviewer_{key}.jsonl') for key in ('a', 'b')}
    return {
        'relevance_candidates': len(records),
        'review_submission_count': len(submissions),
        'human_relevance_completed': sum(r.get('human_review_status') == 'completed' for r in records),
        'human_relevance_provisional': sum(r.get('human_review_status') == 'provisional' for r in records),
        'source_checked_unresolved': sum(
            r.get('source_checked') is True and r.get('human_retrieval_relevant') is None
            and r.get('human_review_status') != 'provisional' for r in records),
        'reviewer_reconciliation': diagnostics,
        'comparison_reviews': {
            key: sum(r.get('comparison_review_status') == 'completed' for r in entries)
            for key, entries in reviewers.items()},
        'note': 'Matching reviewer submissions are not adjudicated gold. No independent scientific accuracy is claimed.'
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
