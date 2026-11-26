#!/usr/bin/env python3
"""Assemble D6 exact-certificate coverage and two integer moment prunes.

Selected Farkas certificates still require independent semantic replay.
The two prunes are recomputed directly from the 32-vertex cube here.
"""
import hashlib
import itertools
import json
import sys
from pathlib import Path


def growth(count, radius):
    order = [sum(1 << i for i in c) for k in range(6)
             for c in itertools.combinations(range(5), k)]
    return sum(min((x ^ y).bit_count() for y in order[:count]) <= radius
               for x in range(32))


def prune(assumptions):
    lower = []
    for k in range(1, 37):
        lower.append(max([0]+[growth(count, (level-k)//12)
                              for level, count in assumptions if k <= level]))
    square = sum((2*k-1)*value for k, value in enumerate(lower, 1))
    assert square > 22471
    return dict(high_tail_assumptions=assumptions, lower_tail_counts=lower,
                exact_moment_lower=square, allowed_moment_upper=22471,
                exact_margin=square-22471)


def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    root = Path(__file__).resolve().parents[1]
    selected = []
    for count in range(10):
        path = root/f'outputs/sh_D6_tail_top_{count}.json'
        data = json.loads(path.read_text())
        assert data['verification']['exact_cancellation']
        selected.append(dict(conditions={'36':count},
                             certificate=str(path.relative_to(root)),
                             sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    path = root/'outputs/sh_D6_tail_top10_next10.json'
    data = json.loads(path.read_text())
    assert data['verification']['exact_cancellation']
    selected.append(dict(conditions={'36':10,'35':10},
                         certificate=str(path.relative_to(root)),
                         sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    result = dict(config=config, selected=selected,
                  prunes=[prune([(36,11)]),prune([(36,10),(35,11)])],
                  coverage='q36>=11 is pruned; q36=0..9 is certified; q36=10 implies q35>=10, whose >=11 branch is pruned and =10 branch is certified.',
                  independent_replay='Required before mathematical promotion.')
    out = Path(sys.argv[2]); temp=out.with_suffix('.json.tmp')
    temp.write_text(json.dumps(result, separators=(',', ':')));temp.replace(out)
    print(json.dumps(dict(certificates=len(selected),
                          prunes=[x['exact_moment_lower'] for x in result['prunes']])))


if __name__ == '__main__':
    main()
