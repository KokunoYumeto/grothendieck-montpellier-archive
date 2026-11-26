#!/usr/bin/env python3
"""Search exact F2 sums of crossing coefficients for two-layout candidates.

Exhaustive on the q=2 and q=4 coefficient spans; deterministic random and
coordinate descent search on q=8.  Ranks are exact binary Gaussian ranks.
The output records the original coefficient degrees for the best witness.
"""
import json
from pathlib import Path
import random
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
settings = json.loads((ROOT / 'inputs/sh_crossing_subsets.json').read_text())
BINARY = sys.argv[1]


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            previous = pivots.get(pivot)
            if previous is None:
                pivots[pivot] = row
                break
            row ^= previous
    return len(pivots)


def flatten(vector, q):
    ab, ad = [0]*(q*q), [0]*(q*q)
    while vector:
        low = vector & -vector
        i = low.bit_length()-1
        vector ^= low
        d = i % q; i //= q
        c = i % q; i //= q
        b = i % q; a = i // q
        ab[a*q+b] |= 1 << (c*q+d)
        ad[a*q+d] |= 1 << (b*q+c)
    return ab, ad


def run_case(case):
    n, energy = case['size'], case['energy']
    path = ROOT / 'outputs' / f'sh_crossing_coeff_n{n}_e{energy}_p2.tsv'
    if not path.exists():
        result = subprocess.run([BINARY, str(n), str(energy), '2', 'binary-coefficients'],
                                capture_output=True, text=True, check=True)
        path.write_text(result.stdout)
    lines = path.read_text().splitlines()
    assert lines[1] == '# tail_bad=0 nonbinary=0 identity_bad=0 extra_bad=0 reflection_bad=0'
    meta = dict(t.split('=', 1) for t in lines[0].split()[1:])
    q = int(meta['q'])
    coefficients = {}
    basis = {}
    target = 0
    for line in lines[3:]:
        degree, packed = line.split('\t')
        degree = int(degree)
        value = int(packed[::-1], 16)
        coefficients[degree] = value
        target ^= value
        mask = 1 << degree
        while value:
            pivot = value.bit_length()-1
            if pivot in basis:
                value ^= basis[pivot][0]
                mask ^= basis[pivot][1]
            else:
                basis[pivot] = (value, mask)
                break
    vectors = list(basis.values())
    d = len(vectors)
    flat_basis = [flatten(v, q) for v, _ in vectors]
    target_ab, target_ad = flatten(target, q)
    best = None
    tested = set()

    def evaluate(mask):
        nonlocal best
        if mask in tested:
            return None
        tested.add(mask)
        ab, ad = [0]*(q*q), [0]*(q*q)
        original_mask = 0
        working = mask
        while working:
            low = working & -working; working ^= low
            bit = low.bit_length()-1
            original_mask ^= vectors[bit][1]
            ba, bd = flat_basis[bit]
            ab = [x^y for x,y in zip(ab, ba)]
            ad = [x^y for x,y in zip(ad, bd)]
        ranks = (rank(ab), rank(ad),
                 rank([x^y for x,y in zip(ab, target_ab)]),
                 rank([x^y for x,y in zip(ad, target_ad)]))
        objective = (max(min(ranks[:2]), min(ranks[2:])),
                     min(ranks[:2])+min(ranks[2:]))
        if best is None or objective < tuple(best['objective']):
            degrees = [i for i in coefficients if original_mask >> i & 1]
            reconstructed = 0
            for i in degrees:
                reconstructed ^= coefficients[i]
            assert flatten(reconstructed, q) == (ab, ad)
            best = {'objective': list(objective), 'ranks_ab_ad_complement_ab_ad': list(ranks),
                    'basis_mask': mask, 'coefficient_degrees': degrees}
        return objective

    if case['mode'] == 'exhaustive':
        assert d <= settings['max_exhaustive_dimension']
        for mask in range(1 << d):
            evaluate(mask)
    else:
        rng = random.Random(settings['seed'] + energy + 1000*n)
        evaluate(0)
        for bit in range(d):
            evaluate(1 << bit)
        for _ in range(case['random_trials']):
            evaluate(rng.getrandbits(d))
        for _ in range(case['descent_restarts']):
            current = rng.getrandbits(d)
            score = evaluate(current)
            if score is None:
                continue
            for _ in range(d):
                candidates = []
                for bit in range(d):
                    candidate = current ^ (1 << bit)
                    value = evaluate(candidate)
                    if value is not None and value < score:
                        candidates.append((value, candidate))
                if not candidates:
                    break
                score, current = min(candidates)
    result = {'size': n, 'energy': energy, 'q': q, 'coefficient_span_dimension': d,
              'mode': case['mode'], 'tested': len(tested), 'best': best}
    print(json.dumps(result), flush=True)
    return result


results = []
for case in settings['cases']:
    results.append(run_case(case))
    (ROOT / 'outputs/sh_crossing_subsets.json').write_text(json.dumps(results, indent=2)+'\n')
