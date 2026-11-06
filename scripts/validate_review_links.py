"""Check that review judgments point to the source records and cases they describe.

These checks validate links and copied packet fields. They do not determine whether
source extractions or human scientific judgments are factually correct.
"""

import argparse
import json
from pathlib import Path

from current_retrieve import Baseline, ROOT, rows

PACKET_FIELDS = (
    'record_id',
    'species',
    'original_plant_name',
    'plant_part',
    'preparation',
    'original_use_description',
    'reported_use_or_outcome',
    'study_setting',
    'model',
    'endpoint',
    'comparator',
    'community_or_nation',
    'source_url',
    'source_id',
    'supporting_passage',
    'passage_locator',
    'licence',
    'citation',
)
REVIEW_SLOTS = ('a', 'b')


def _unique_by_case(records, label):
    indexed = {}
    for record in records:
        case_id = record.get('case_id')
        if not case_id:
            raise ValueError(f'{label} record is missing case_id')
        if case_id in indexed:
            raise ValueError(f'Duplicate {label} case_id: {case_id}')
        indexed[case_id] = record
    return indexed


def _packet(raw):
    return {key: raw.get(key) for key in PACKET_FIELDS}


def validate(root=ROOT):
    """Validate case-to-record and review-to-case correspondence; return counts."""
    root = Path(root)
    baseline = Baseline(root)
    cases = rows(root / 'data/review/review_cases.jsonl')
    expectations = rows(root / 'data/evaluation/development_expectations.jsonl')
    adjudications = rows(root / 'data/review/adjudicated.jsonl')
    case_by_id = _unique_by_case(cases, 'review case')
    expected_by_id = _unique_by_case(expectations, 'development expectation')
    adjudication_by_id = _unique_by_case(adjudications, 'adjudication')
    case_ids = set(case_by_id)

    if set(expected_by_id) != case_ids:
        raise ValueError('Development expectation case IDs do not match review cases')
    if set(adjudication_by_id) != case_ids:
        raise ValueError('Adjudication case IDs do not match review cases')

    extracted_pairs = {
        (record['raw']['traditional_record_id'], record['raw']['experimental_record_id'])
        for record in rows(root / 'data/processed/extracted_claim_study_pairs.jsonl')
    }

    for case_id, case in case_by_id.items():
        tid, eid = case.get('traditional_record_id'), case.get('evidence_id')
        if tid not in baseline.claims:
            raise ValueError(f'{case_id} references unknown traditional record: {tid}')
        if eid not in baseline.experiments:
            raise ValueError(f'{case_id} references unknown experimental record: {eid}')

        traditional = case.get('traditional')
        experiment = case.get('experiment')
        if not isinstance(traditional, dict) or not isinstance(experiment, dict):
            raise ValueError(f'{case_id} is missing its source packets')
        expected_traditional = _packet(baseline.claims[tid]['raw'])
        expected_traditional['citation'] = baseline.sources[baseline.claims[tid]['raw']['source_key']]['attribution']
        expected_experiment = _packet(baseline.experiments[eid]['raw'])
        if traditional != expected_traditional:
            raise ValueError(f'{case_id} traditional packet does not match record {tid}')
        if experiment != expected_experiment:
            raise ValueError(f'{case_id} experimental packet does not match record {eid}')
        if case.get('claim_evaluation_group_id') != baseline.claims[tid].get('evaluation_group_id'):
            raise ValueError(f'{case_id} has an incorrect traditional evaluation-group link')
        if case.get('evidence_evaluation_group_id') != baseline.experiments[eid].get('evaluation_group_id'):
            raise ValueError(f'{case_id} has an incorrect experimental evaluation-group link')

        construction = case.get('construction')
        if construction == 'existing_extracted_link' and (tid, eid) not in extracted_pairs:
            raise ValueError(f'{case_id} is marked as an extracted link but no such pair exists')
        if construction == 'constructed_species_mismatch_comparison':
            claim_species = set(baseline.claims[tid]['raw'].get('species') or [])
            evidence_species = set(baseline.experiments[eid]['raw'].get('species') or [])
            if not claim_species or not evidence_species or claim_species & evidence_species:
                raise ValueError(f'{case_id} is not a verified species-mismatch challenge pair')
        if construction not in ('existing_extracted_link', 'constructed_species_mismatch_comparison'):
            raise ValueError(f'{case_id} has unknown construction type: {construction}')

        expected = expected_by_id[case_id]
        if expected.get('traditional_record_id') != tid or expected.get('evidence_id') != eid:
            raise ValueError(f'{case_id} expectation points to a different record pair')
        claim_species = set(baseline.claims[tid]['raw'].get('species') or [])
        evidence_species = set(baseline.experiments[eid]['raw'].get('species') or [])
        expected_taxon = 'overlap_in_reported_species' if claim_species & evidence_species else 'different_species'
        if expected.get('expected_taxon') != expected_taxon:
            raise ValueError(f'{case_id} has an incorrect structural taxon expectation')
        retrieved_ids = {result['evidence_id'] for result in baseline.retrieve(tid, 1000)['results']}
        if expected.get('expected_retrieval_membership') is not (eid in retrieved_ids):
            raise ValueError(f'{case_id} has an incorrect retrieval-membership expectation')

    reviewers = {}
    for slot in REVIEW_SLOTS:
        records = rows(root / f'data/review/reviewer_{slot}.jsonl')
        indexed = _unique_by_case(records, f'reviewer {slot}')
        if set(indexed) != case_ids:
            raise ValueError(f'Reviewer {slot} case IDs do not match review cases')
        reviewers[slot] = indexed
        for case_id, record in indexed.items():
            if record.get('schema_version') != 2:
                raise ValueError(f'{case_id} reviewer {slot} has an unsupported schema version')
            if record.get('pair_label') != record.get('claim_comparability', {}).get('label'):
                raise ValueError(f'{case_id} reviewer {slot} has conflicting comparison labels')

    for case_id, adjudication in adjudication_by_id.items():
        for slot in REVIEW_SLOTS:
            reviewer_id = adjudication.get(f'reviewer_{slot}')
            if reviewer_id is not None and reviewer_id != reviewers[slot][case_id].get('reviewer_id'):
                raise ValueError(f'{case_id} adjudication reviewer_{slot} does not match reviewer file')

    return {
        'review_cases': len(cases),
        'extracted_links': sum(c.get('construction') == 'existing_extracted_link' for c in cases),
        'constructed_species_mismatches': sum(
            c.get('construction') == 'constructed_species_mismatch_comparison' for c in cases
        ),
        'reviewer_records': {slot: len(reviewers[slot]) for slot in REVIEW_SLOTS},
        'adjudications': len(adjudications),
        'scope_note': 'Link consistency only; source accuracy and judgment correctness require human source review.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    print(json.dumps(validate(args.root), ensure_ascii=False, indent=2))
