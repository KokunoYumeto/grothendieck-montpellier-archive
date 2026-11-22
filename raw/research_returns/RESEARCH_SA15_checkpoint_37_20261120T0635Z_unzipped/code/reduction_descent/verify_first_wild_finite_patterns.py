"""Finite exact recurrence and character supplement for B77."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from itertools import combinations
from math import gcd, isqrt
import json
import time

started = time.perf_counter()
primes = [p for p in range(5, 102) if all(p % d for d in range(2, isqrt(p) + 1))]
counts = Counter()
rows = []

for p in primes:
    N = p * p - 1
    e = p * (p - 1)
    for m in range(1, p + 2):
        if (p + 1) % m:
            continue
        a = e * m
        q1 = min(a + 1, 1 + p)
        q2 = min(a + q1, 1 + p * q1)
        assert q1 == p + 1
        assert q2 == min(a + p + 1, p * p + p + 1)
        assert (p - 1) * q2 >= a
        counts['norm_one_good_degree_rows'] += 1
        rows.append(dict(p=p, e=e, m=m, a=a, q1=q1, q2=q2,
                         threshold_numerator=a, threshold_denominator=p - 1))
        # The coefficientwise logarithm bound is checked at every degree,
        # including powers of p and equality at the rounded threshold.
        for degree in range(1, 2001):
            L = 0
            power = p
            while power <= degree:
                L += 1
                power *= p
            assert degree * q2 - a * L >= q2
            counts['coefficientwise_logarithm_checks'] += 1
        for q in (1, 2, p + 1, q2):
            simple = min(a + q, 1 + p * q)
            full = min(a + q, 1 + p * q, p * p * q)
            assert simple == full
            for degree in range(2, p * p):
                # A surviving coefficient not forced into (p) must have all
                # exponents divisible by p, hence total degree>=p.
                coefficient_bound = 1 if degree % p == 0 else a
                assert coefficient_bound + degree * q >= simple
                counts['unweighted_degree_bounds'] += 1
        assert e <= p * p
        counts['mixed_level_three_exclusions'] += 1

    a = e * N
    q = 1
    sequence = [q]
    for j in range(1, 4):
        q = min(a + q, p * q + p - 1)
        assert q == 2 * p ** j - 1
        sequence.append(q)
    assert q * (p - 1) > a
    assert e < p ** 4 and e > p
    counts['full_index_three_upper_rows'] += 1

p = 5
N = 24
norm_fibre = [c for c in range(N) if c % 4 == 1]
orbits = sorted({tuple(sorted({c, p * c % N})) for c in norm_fibre})
assert orbits == [(1, 5), (9, 21), (13, 17)]
names = {orbit: name for name, orbit in zip(('A', 'B', 'C'), orbits)}
pair_rows = []
for X, Y in combinations(orbits, 2):
    joint_order = N // gcd(N, gcd(X[0], Y[0]))
    assert joint_order == 24
    twisted = tuple(sorted(tuple(sorted((x + 12) % N for x in O)) for O in (X, Y)))
    pair_rows.append(dict(types=[names[X], names[Y]], joint_order=joint_order,
                          quadratic_twist=[names[O] for O in twisted]))
    counts['p5_distinct_primitive_norm_pairs'] += 1

for m in (8, 24):
    fibre = [c for c in range(N) if (c * m) % N == 0 and c % 4 == 1]
    f_orbits = {tuple(sorted({c, p * c % N})) for c in fibre}
    assert len(f_orbits) == (1 if m == 8 else 3)
    counts['p5_joint_degree_fibres'] += 1

out = dict(status='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
           runtime_seconds=time.perf_counter() - started,
           primes=primes, counts=dict(counts), norm_one_rows=rows,
           p5_primitive_norm_orbits=orbits, p5_pair_rows=pair_rows,
           scope='Finite checks of the unweighted and weighted coefficient recurrences, closed logarithm inequalities and exact p5 primitive-norm patterns. No geometric existence, actual torsion comparison or exact first-wild least index is inferred. The all-prime kernel and graph arguments are proved in the text.')
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
