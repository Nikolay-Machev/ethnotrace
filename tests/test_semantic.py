import json, sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from retrieve import Baseline
from semantic_retrieval import inputs, digest, fuse, snapshot, load_snapshot
from evaluate_retrieval import metrics


class FakeEncoder:
    def encode_query(self, texts, **kwargs):
        return [[1.0, 0.0] for _ in texts]

    def encode_document(self, texts, **kwargs):
        return [[0.0, 1.0] for _ in texts]


class SemanticTests(unittest.TestCase):
    def test_same_species_gate_and_unresolved_names(self):
        b = Baseline()
        s = snapshot(b, FakeEncoder(), '0' * 40, {})
        for tid, r in s['rankings'].items():
            expected = {x['evidence_id'] for x in b.retrieve(tid, 10000)['results']}
            for method in ('lexical', 'semantic', 'hybrid'):
                self.assertEqual(set(r[method]), expected)
        self.assertEqual(s['rankings']['T005']['semantic'], [])
        self.assertNotIn('E008', s['rankings']['T013']['semantic'])

    def test_ranker_inputs_do_not_read_judgments_or_result_direction(self):
        b = Baseline()
        before = digest(inputs(b))
        for r in b.documents.values():
            r['raw']['reported_use_or_outcome'] = 'secret answer'
            r['raw']['supporting_passage'] = 'secret answer'
            r['raw']['classification'] = {'label': 'support'}
            r['features']['experimental_result_direction'] = 'favourable_effect'
        self.assertEqual(before, digest(inputs(b)))

    def test_fusion_is_deterministic_and_rejects_pool_mismatch(self):
        self.assertEqual(fuse(['a', 'b'], ['b', 'a'])[0], ['a', 'b'])
        with self.assertRaises(ValueError):
            fuse(['a'], ['b'])

    def test_stale_cache_fails_closed(self):
        b = Baseline()
        s = snapshot(b, FakeEncoder(), '0' * 40, {})
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'cache.json'
            p.write_text(json.dumps(s), encoding='utf-8', newline='\n')
            self.assertIsNotNone(load_snapshot(b, p))
            b.claims['T011']['raw']['original_use_description'] = 'changed query'
            with self.assertRaises(ValueError):
                load_snapshot(b, p)

    def test_empty_positive_set_not_zero_accuracy(self):
        self.assertIsNone(metrics(['a'], set())['recall_at_5'])

    def test_compare_is_unchanged_after_semantic_generation(self):
        b = Baseline()
        before = b.compare(b.claims['T008'], b.experiments['E004'])
        snapshot(b, FakeEncoder(), '0' * 40, {})
        self.assertEqual(before, b.compare(b.claims['T008'], b.experiments['E004']))


class HumanRankingEvaluationTests(unittest.TestCase):
    def test_precision_and_recall_use_different_denominators(self):
        result = metrics(['a', 'b', 'c', 'd', 'e', 'f'], {'a', 'f'})
        self.assertEqual(result['precision_at_5'], 0.2)
        self.assertEqual(result['recall_at_5'], 0.5)
        self.assertEqual(metrics(['a'], {'a'})['precision_at_5'], 0.2)
        self.assertEqual(metrics(['a'], set())['precision_at_5'], 0)

    def test_incomplete_account_is_excluded_without_shrinking_pool(self):
        from evaluate_retrieval import human_comparison

        ranking = {'T1': {m: ['a', 'b'] for m in ('lexical', 'semantic', 'hybrid')}}
        good = dict(
            human_review_status='completed',
            human_retrieval_relevant=True,
            human_reviewer_id='reviewer',
            human_rationale='Useful',
            source_checked=True,
        )
        for status in ('pending', 'provisional', 'missing'):
            reviews = {('T1', 'a'): good, ('T1', 'b'): {**good, 'human_review_status': status}}
            judged, excluded = human_comparison(ranking, reviews)
            self.assertEqual(judged, [])
            self.assertEqual(excluded[0]['blocking_candidates'][0]['status'], status)

    def test_movements_preserve_useful_mismatch_and_top_five_tradeoff(self):
        from evaluate_retrieval import human_comparison

        ranking = {
            'T1': dict(
                lexical=['a', 'b', 'c', 'd', 'e', 'f'],
                semantic=['b', 'c', 'd', 'e', 'f', 'a'],
                hybrid=['a', 'b', 'c', 'd', 'f', 'e'],
            )
        }
        reviews = {
            ('T1', eid): dict(
                human_review_status='completed',
                human_retrieval_relevant=eid in {'a', 'f'},
                human_reviewer_id='reviewer',
                human_rationale='Informative part mismatch',
                source_checked=True,
            )
            for eid in ranking['T1']['lexical']
        }
        judged, excluded = human_comparison(ranking, reviews)
        self.assertEqual(excluded, [])
        q = judged[0]
        self.assertEqual(q['methods']['hybrid']['recall_at_5'], 1)
        f = next(r for r in q['useful_movements'] if r['evidence_id'] == 'f')
        self.assertEqual(f['movement_vs_lexical']['semantic'], 1)
        self.assertFalse(f['top_five']['lexical'])
        self.assertTrue(f['top_five']['semantic'])
        self.assertEqual(f['human_rationale'], 'Informative part mismatch')
