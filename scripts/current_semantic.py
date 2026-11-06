"""Local pretrained semantic challenger. Candidate eligibility/comparisons remain Baseline's."""

import argparse, hashlib, json, math
from current_retrieve import Baseline, ROOT, VERSION

MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
RRF_K = 60
SCHEMA = 1


def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def inputs(b):
    # Deliberate allowlist: no findings, labels, reviewer rationale or supporting excerpts.
    queries = {tid: c['raw'].get('original_use_description') or '' for tid, c in sorted(b.claims.items())}
    documents = {
        eid: '\n'.join(
            filter(
                None,
                [d['raw'].get('title') or b.paper_titles.get(d['raw'].get('paper_id'), ''), d['raw'].get('endpoint')],
            )
        )
        for eid, d in sorted(b.documents.items())
    }
    candidates = {
        tid: [{'id': r['evidence_id'], 'score': r['score']} for r in b.retrieve(tid, 10000)['results']]
        for tid in queries
    }
    return dict(queries=queries, documents=documents, candidates=candidates, baseline_version=VERSION)


def rank(ids, scores):
    return sorted(ids, key=lambda eid: (-scores[eid], eid))


def fuse(lexical, semantic):
    if set(lexical) != set(semantic):
        raise ValueError('Candidate pools differ')
    scores = {eid: 0.0 for eid in lexical}
    for order in (lexical, semantic):
        for i, eid in enumerate(order, 1):
            scores[eid] += 1 / (RRF_K + i)
    return rank(lexical, scores), scores


def snapshot(b, encoder, revision, packages):
    source = inputs(b)
    qids = list(source['queries'])
    dids = list(source['documents'])
    qvectors = encoder.encode_query(
        list(source['queries'].values()), normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False
    )
    dvectors = encoder.encode_document(
        list(source['documents'].values()), normalize_embeddings=True, convert_to_numpy=True, show_progress_bar=False
    )
    docs = dict(zip(dids, dvectors))
    rankings = {}
    for tid, qv in zip(qids, qvectors):
        lexical = [r['id'] for r in source['candidates'][tid]]
        cosine = {eid: float(sum(float(a) * float(v) for a, v in zip(qv, docs[eid]))) for eid in lexical}
        if any(not math.isfinite(v) for v in cosine.values()):
            raise ValueError('Nonfinite similarity')
        semantic = rank(lexical, cosine)
        hybrid, rrf = fuse(lexical, semantic)
        rankings[tid] = dict(lexical=lexical, semantic=semantic, hybrid=hybrid, cosine=cosine, rrf=rrf)
    return dict(
        schema_version=SCHEMA,
        input_sha256=digest(source),
        model=MODEL,
        revision=revision,
        packages=packages,
        max_sequence_length=256,
        embedding_dimensions=384,
        rrf_k=RRF_K,
        inference='local CPU; pretrained weights; no fine-tuning',
        input_fields={'query': ['original_use_description'], 'document': ['title or parent-paper title', 'endpoint']},
        rankings=rankings,
    )


def load_snapshot(b, path=None):
    path = path or ROOT / 'data/evaluation/semantic_rankings.json'
    if not path.exists():
        return None
    value = json.loads(path.read_text())
    if value.get('schema_version') != SCHEMA or value.get('input_sha256') != digest(inputs(b)):
        raise ValueError('Semantic snapshot is stale; rerun scripts/current_semantic.py before exporting the demo.')
    expected = inputs(b)['candidates']
    for tid, records in expected.items():
        ids = {r['id'] for r in records}
        r = value['rankings'][tid]
        for method in ('lexical', 'semantic', 'hybrid'):
            if set(r[method]) != ids or len(r[method]) != len(ids):
                raise ValueError('Invalid semantic candidate pool')
    return value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--revision', required=True, help='Immutable Hugging Face model commit SHA')
    args = parser.parse_args()
    if len(args.revision) != 40 or any(c not in '0123456789abcdef' for c in args.revision):
        parser.error('Use an immutable 40-character model revision')
    try:
        from sentence_transformers import SentenceTransformer
        from importlib.metadata import version
        import torch
    except ImportError:
        parser.error('Install requirements-semantic.txt in a separate virtual environment first.')
    torch.set_num_threads(2)
    torch.manual_seed(0)
    encoder = SentenceTransformer(MODEL, revision=args.revision, device='cpu', trust_remote_code=False)
    encoder.max_seq_length = 256
    value = snapshot(
        Baseline(),
        encoder,
        args.revision,
        {p: version(p) for p in ('sentence-transformers', 'transformers', 'torch', 'numpy', 'huggingface-hub')},
    )
    (ROOT / 'data/evaluation/semantic_rankings.json').write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    print(
        json.dumps(
            {
                'model': MODEL,
                'revision': args.revision,
                'accounts': len(value['rankings']),
                'input_sha256': value['input_sha256'],
            }
        )
    )
