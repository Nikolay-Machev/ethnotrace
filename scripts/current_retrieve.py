"""Current development ranker; retrieve.py preserves the frozen pilot baseline."""

from retrieve import Baseline as FrozenBaseline, ROOT, rows, tokenise

VERSION = '1.2'


class Baseline(FrozenBaseline):
    def score(self, claim, evidence):
        score = super().score(claim, evidence)
        if score is not None and self.compare(claim, evidence)['plant_part'] == 'different_parts':
            score = {**score, 'parts': 0, 'total': score['total'] + 2}
        return score


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--claim', required=True)
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--compare')
    args = parser.parse_args()
    baseline = Baseline()
    try:
        result = (
            baseline.present(baseline.claims[args.claim], baseline.documents[args.compare])
            if args.compare
            else baseline.retrieve(args.claim, args.limit)
        )
    except (ValueError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
