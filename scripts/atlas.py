"""Summaries of indexed extracted evidence; independent of the retrieval scorer."""

DIMENSIONS = {
    'species': (
        'taxon',
        {
            'overlap_in_reported_species': 'Species overlap',
            'different_species': 'Different species',
            'unknown': 'Unresolved',
        },
    ),
    'part': (
        'plant_part',
        {'overlap_in_parts': 'Part overlap', 'different_parts': 'Different part', 'unknown': 'Unknown part'},
    ),
    'preparation': ('preparation_equivalence', {'not_established': 'Equivalence unknown'}),
    'outcome': ('outcome', {'not_established': 'Alignment unknown', 'different_endpoint': 'Different endpoint'}),
}


def summarize(results):
    experiments = [r for r in results if r['evidence_level'] == 'selected_full_text_experimental_unit']
    dimensions = {}
    for dimension, (field, labels) in DIMENSIONS.items():
        buckets = {}
        for r in experiments:
            value = r['comparison'][field]
            buckets.setdefault(value, {'label': labels.get(value, value), 'evidence_ids': []})['evidence_ids'].append(
                r['evidence_id']
            )
        dimensions[dimension] = buckets
    for dimension in ('setting', 'finding'):
        buckets = {}
        labels = {
            'animal_in_vivo': 'Animal study',
            'in_vitro': 'Cell / laboratory study',
            'human_clinical': 'Human study',
            'favourable_effect': 'Favourable finding',
            'no_detected_effect': 'No detected effect',
            'condition_dependent': 'Condition-dependent',
            'statistically_inconclusive': 'Statistically inconclusive',
        }
        for r in experiments:
            value = (
                r['study'].get('study_setting')
                if dimension == 'setting'
                else r['comparison'].get('experimental_result_direction')
            ) or 'unknown'
            if isinstance(value, list):
                value = ', '.join(value)
            buckets.setdefault(value, {'label': labels.get(value, value.replace('_', ' ')), 'evidence_ids': []})[
                'evidence_ids'
            ].append(r['evidence_id'])
        dimensions[dimension] = buckets
    return {
        'experimental_units': len(experiments),
        'unique_publications': len({r['paper_id'] for r in experiments if r['paper_id']}),
        'literature_leads': len(results) - len(experiments),
        'dimensions': dimensions,
        'comparison_reviews': sum(r['human_comparison_reviews'] > 0 for r in experiments),
        'note': 'Automated dimension summaries. Human comparison review is an overall pair judgment, not verification of every dimension.',
    }
