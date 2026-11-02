"""Validate the publication catalogue without treating it as claim-level extraction."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    papers = [json.loads(s) for s in (root / 'data/papers.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
    manifest = json.loads((root / 'data/paper_search_manifest.json').read_text(encoding='utf-8'))
    traditional = {json.loads(s)['record_id'] for s in (root / 'data/traditional_records.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()}
    seen, dois = set(), set()
    required = {'paper_id', 'title', 'authors', 'publication_year', 'journal', 'citation', 'pmid', 'doi', 'source_id', 'source_url', 'species', 'plant_part', 'preparation', 'reported_use_or_outcome', 'study_setting', 'supporting_passage', 'passage_locator', 'licence', 'limitations', 'inclusion_tier', 'screening_level', 'full_text_reviewed', 'linked_traditional_record_ids', 'match_status'}
    bibliography = (root / 'docs/papers.md').read_text(encoding='utf-8')
    for p in papers:
        pid = p.get('paper_id')
        assert required <= p.keys(), (pid, 'missing fields')
        assert pid == 'P' + p['pmid'] and re.fullmatch(r'P[0-9]+', pid), pid
        assert pid not in seen, (pid, 'duplicate publication')
        seen.add(pid)
        if p['doi']:
            doi = p['doi'].lower()
            assert re.fullmatch(r'10\.[0-9]{4,9}/\S+', doi), pid
            assert doi not in dois, (pid, 'duplicate DOI')
            dois.add(doi)
        assert p['source_id'] == 'PMID:' + p['pmid'], pid
        assert p['source_url'] == 'https://pubmed.ncbi.nlm.nih.gov/' + p['pmid'] + '/', pid
        assert p['citation'] in bibliography, (pid, 'missing citation in bibliography')
        assert p['authors'] and p['journal'] and p['limitations'], pid
        assert p['inclusion_tier'] in {'core', 'supporting', 'context', 'provisional_species'}, pid
        assert p['screening_level'] == 'abstract_reviewed' and p['full_text_reviewed'] is False, pid
        assert 1 <= len(p['supporting_passage'].split()) <= 20, (pid, 'excerpt length')
        assert p['species'] is None or isinstance(p['species'], list), pid
        assert set(p['linked_traditional_record_ids']) <= traditional, pid
        assert p['match_status'] == 'not_adjudicated' and not p['linked_traditional_record_ids'], pid
    assert manifest['included_publications'] == len(papers)
    assert manifest['unique_retrieved_records'] >= len(papers)
    # Regression checks: retain null findings and preparation limitations.
    by_id = {p['paper_id']: p for p in papers}
    assert 'no significant' in by_id['P32153825']['reported_use_or_outcome']
    assert 'no significant' in by_id['P30669469']['reported_use_or_outcome']
    assert 'no hypoglycaemic' in by_id['P21249104']['reported_use_or_outcome']
    assert 'without Labrasol' in by_id['P19303751']['reported_use_or_outcome']
    from collections import Counter
    summary = json.loads((root / 'data/classification_summary.json').read_text(encoding='utf-8'))
    expected = {'support', 'no_detected_effect', 'mixed_evidence', 'not_directly_comparable', 'insufficient_evidence'}
    for p in papers:
        c = p['classification']
        assert c['label'] in expected, p['paper_id']
        assert c['question'] and c['rationale'] and c['evidence_source_url'] == p['source_url']
        assert c['scope'] == 'study_question_screening'
        assert c['claim_pair_label'] is False and c['training_eligible'] is False
        assert p['paper_id'] in (root / 'docs/study_classification.md').read_text(encoding='utf-8')
    counts = dict(Counter(p['classification']['label'] for p in papers))
    assert counts == summary['counts'] and summary['total'] == len(papers)
    assert summary['minimum_met_at_study_screening_level'] == all(counts.get(k, 0) >= summary['requested_minimum'] for k in expected)
    assert summary['training_ready_count'] == 0
    assert by_id['P26024297']['classification']['label'] == 'no_detected_effect'
    assert by_id['P31136659']['classification']['label'] == 'no_detected_effect'
    assert by_id['P31136659']['correction']['counted_as_study'] is False
    assert by_id['P31136659']['correction']['pmid'] == '31667509'
    return len(papers)

if __name__ == '__main__':
    print(f'PASS: {validate()} publications; unique identifiers, citations, provenance, and matching status checked')
