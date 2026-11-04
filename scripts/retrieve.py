"""Deterministic species-gated evidence retrieval; no LLM, labels or review answers used."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.1'

def rows(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines() if s.strip()]

def tokenise(s):
    return {t for t in re.findall(r'[^\W_]+', (s or '').casefold()) if len(t) > 3 and t not in {'with', 'from', 'this', 'that', 'used', 'plant', 'reported', 'symptoms'}}

class Baseline:
    def __init__(self, root=ROOT):
        base = root / 'data/processed'
        self.claims = {r['id']: r for r in rows(base / 'traditional_records.jsonl')}
        self.experiments = {r['id']: r for r in rows(base / 'experimental_records.jsonl')}
        # Active records use cited corrections; processed raw and pinned imports remain historical.
        for e in self.experiments.values():
            if e['provenance'].get('audit_correction'):
                e['raw'] = e['normalized']
        self.sources = {s['source_key']: s for s in json.loads((base / 'sources.json').read_text())['raw']['sources']}
        self.paper_titles = {r['id']: r['raw'].get('title', '') for r in rows(base / 'papers.jsonl')}
        self.documents = dict(self.experiments)
        extracted = {r['raw']['paper_id'] for r in self.experiments.values()}
        for r in rows(base / 'papers.jsonl'):
            if r['id'] not in extracted: self.documents[r['id']] = r
        for r in rows(base / 'catalogue_literature_leads.jsonl'): self.documents[r['id']] = r

    def cited_account(self, tid):
        raw = self.claims[tid]['raw']
        return {**raw, 'citation': raw.get('citation') or self.sources[raw['source_key']]['attribution']}

    def compare(self, claim, evidence):
        a, b = claim['features'], evidence['features']
        raw_a, raw_b = claim['raw'], evidence['raw']
        sa, sb = set(a['scientific_names'] or []), set(b['scientific_names'] or [])
        taxon = 'unknown' if not sa or not sb else 'overlap_in_reported_species' if sa & sb else 'different_species'
        pa, pb = set(a['plant_parts'] or []), set(b['plant_parts'] or [])
        part = 'unknown' if not pa or not pb else 'overlap_in_parts' if pa & pb else 'different_parts'
        wa, wb = set(a['extraction_solvents_explicit'] or []), set(b['extraction_solvents_explicit'] or [])
        solvent = 'unknown' if not wa or not wb else 'shared_solvent_only' if wa & wb else 'different_solvents'
        # A shared solvent does not establish equivalent extraction duration, formulation or dose.
        reasons = []
        if taxon == 'different_species': reasons.append('The inspected sources name different scientific species.')
        if taxon == 'unknown': reasons.append('Scientific identity is missing on at least one side; no common-name inference made.')
        if part == 'different_parts': reasons.append('The mapped plant parts do not overlap.')
        if part == 'unknown': reasons.append('A plant part is missing or unmapped; equality is not established.')
        if solvent == 'different_solvents': reasons.append('The explicitly recorded extraction solvents differ.')
        reasons.append('Preparation equivalence is not established by this baseline.')
        outcome = 'not_established'
        if 'slow-healing infections' in raw_a.get('original_use_description', '').casefold() and b.get('endpoint') == 'cell_viability_high_glucose':
            outcome = 'different_endpoint'
            reasons.append('Neuronal-cell survival does not test the reported slow-healing infection use.')
        else:
            reasons.append('The traditional indication has not been independently aligned to this experimental endpoint.')
        setting = b.get('study_settings')
        if setting and any(s in setting for s in ('in_vitro', 'animal_in_vivo')):
            reasons.append('Preclinical results do not establish clinical efficacy in people.')
        status = 'not_directly_comparable' if taxon == 'different_species' or part == 'different_parts' or solvent == 'different_solvents' or outcome == 'different_endpoint' else 'insufficient_evidence'
        return {'taxon': taxon, 'plant_part': part, 'solvent': solvent, 'preparation_equivalence': 'not_established',
                'outcome': outcome, 'status': status, 'reasons': reasons,
                'experimental_result_direction': b.get('experimental_result_direction'),
                'independent_review': False, 'medical_efficacy_conclusion': None}

    def score(self, claim, evidence):
        comparison = self.compare(claim, evidence)
        if comparison['taxon'] != 'overlap_in_reported_species': return None
        parts = {'overlap_in_parts': 2, 'different_parts': -2, 'unknown': 0}[comparison['plant_part']]
        solvent = {'shared_solvent_only': 1, 'different_solvents': -1, 'unknown': 0}[comparison['solvent']]
        query = tokenise(claim['raw'].get('original_use_description'))
        # Only endpoint/title relevance is used, never curator labels, rationales or result direction.
        targets = [tokenise(evidence['raw'].get('endpoint')), tokenise(evidence['raw'].get('title') or self.paper_titles.get(evidence['raw'].get('paper_id'), ''))]
        lexical = max((len(query & target) / len(query | target) if query | target else 0) for target in targets)
        return {'total': 10 + parts + solvent + lexical, 'taxon': 10, 'parts': parts, 'solvent': solvent, 'lexical': lexical}

    def present(self, claim, evidence, score=None):
        raw = evidence['raw']
        source = self.sources.get(raw.get('source_key'), {})
        return {'evidence_id': evidence['id'], 'paper_id': raw.get('paper_id'),
                'evidence_level': 'selected_full_text_experimental_unit' if evidence['id'] in self.experiments else 'bibliographic_or_abstract_lead_not_extracted_experiment',
                'score': score, 'comparison': self.compare(claim, evidence),
                'study': {k: raw.get(k) for k in ('species', 'plant_part', 'preparation', 'study_setting', 'model', 'endpoint', 'reported_use_or_outcome', 'notes')},
                'source': {'citation': raw.get('citation') or source.get('attribution'), 'url': raw.get('source_url'),
                           'supporting_passage': raw.get('supporting_passage'), 'locator': raw.get('passage_locator'), 'licence': raw.get('licence')},
                'review_status': 'pending_independent_review'}

    def retrieve(self, claim_id, limit=5):
        if limit < 1: raise ValueError('limit must be positive')
        if claim_id not in self.claims: raise ValueError('Unknown traditional record: ' + claim_id)
        claim = self.claims[claim_id]
        if not claim['features']['scientific_names']:
            return {'claim_id': claim_id, 'status': 'unresolved_species', 'results': [], 'reason': 'Scientific name unresolved; common names are not used to infer a species.'}
        scored = []
        for evidence in self.documents.values():
            score = self.score(claim, evidence)
            if score is not None: scored.append((evidence, score))
        scored.sort(key=lambda pair: (-pair[1]['total'], pair[0]['id']))
        return {'claim_id': claim_id, 'status': 'candidates_found' if scored else 'no_indexed_candidate',
                'claim_source': {k: claim['raw'].get(k) for k in ('source_url', 'supporting_passage', 'passage_locator', 'community_or_nation')},
                'candidate_count': len(scored), 'results': [self.present(claim, evidence, score) for evidence, score in scored[:limit]],
                'note': 'Relevance ranking is not a therapeutic-effect or evidence-quality score.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--claim', required=True)
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--compare', help='Compare a specific indexed evidence ID, including mismatches')
    args = parser.parse_args()
    try:
        baseline = Baseline()
        if args.compare:
            if args.claim not in baseline.claims or args.compare not in baseline.documents: raise ValueError('Unknown claim/evidence ID')
            result = baseline.present(baseline.claims[args.claim], baseline.documents[args.compare])
        else: result = baseline.retrieve(args.claim, args.limit)
    except ValueError as exc: parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
