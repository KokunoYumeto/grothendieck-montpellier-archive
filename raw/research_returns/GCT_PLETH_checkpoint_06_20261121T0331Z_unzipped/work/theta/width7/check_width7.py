#!/usr/bin/env python3
"""Exact checks for the width-seven end-node plethysm sector.

No external representation-theory package is used.  Weight multiplicities of
Sym^d(Lambda^3 C^7) are computed by the Newton recurrence for complete symmetric
functions.  The Weyl alternant then extracts highest-weight multiplicities.
This is a finite check, not the proof of the infinite-family theorem.
"""
from functools import lru_cache
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import csv
import sympy as sp

RANK = 7
TRIPLES = tuple(combinations(range(RANK), 3))
RHO = tuple(range(RANK - 1, -1, -1))
PERMS = []
for p in permutations(RHO):
    inversions = sum(p[i] < p[j] for i in range(RANK) for j in range(i + 1, RANK))
    PERMS.append((p, (-1) ** inversions))


@lru_cache(None)
def weight_multiplicity(d, weight):
    """Coefficient of x^weight in h_d[e_3(x_1,...,x_7)]."""
    if d == 0:
        return int(not any(weight))
    if min(weight) < 0 or max(weight) > d or sum(weight) != 3 * d:
        return 0
    total = 0
    for r in range(1, d + 1):
        for indices in TRIPLES:
            new = list(weight)
            for i in indices:
                new[i] -= r
            if min(new) < 0:
                continue
            total += weight_multiplicity(d - r, tuple(sorted(new, reverse=True)))
    assert total % d == 0
    return total // d


def schur_multiplicity(d, highest):
    if max(highest) > d:
        return 0
    total = 0
    for p, sign in PERMS:
        weight = tuple(highest[i] + RHO[i] - p[i] for i in range(RANK))
        if min(weight) >= 0 and max(weight) <= d:
            total += sign * weight_multiplicity(d, tuple(sorted(weight, reverse=True)))
    return total


def wedge(f, g):
    result = {}
    for I, a in f.items():
        for J, b in g.items():
            if set(I) & set(J):
                continue
            sign = (-1) ** sum(i > j for i in I for j in J)
            K = tuple(sorted(I + J))
            result[K] = sp.expand(result.get(K, 0) + sign * a * b)
    return {I: a for I, a in result.items() if a != 0}


def contract(f, i):
    result = {}
    for I, a in f.items():
        if i in I:
            j = I.index(i)
            result[I[:j] + I[j + 1:]] = (-1) ** j * a
    return result


def metric(f):
    vol = tuple(range(7))
    return sp.Matrix(7, 7, lambda i, j: wedge(wedge(contract(f, i), contract(f, j)), f).get(vol, 0))


def main():
    out = Path(__file__).parent
    rows = []
    max_degree = 10
    checked = 0
    for d in range(max_degree + 1):
        for s in range(3 * d // 7 + 1):
            for b in range((3 * d - 7 * s) // 6 + 1):
                a = 3 * d - 7 * s - 6 * b
                highest = (a + b + s,) + (b + s,) * 5 + (s,)
                expected = int(a % 2 == 0 and b % 2 == 0 and s >= a // 2)
                # Central-degree congruence makes (s-a/2)/3 integral when a even.
                if a % 2 == 0:
                    assert (s - a // 2) % 3 == 0
                actual = schur_multiplicity(d, highest)
                assert actual == expected, (d, highest, actual, expected)
                checked += 1
                rows.append((d, ','.join(map(str, highest)), a, b, s, actual, expected))
    with (out / 'END_NODE_CHECK.tsv').open('w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(('degree', 'highest_weight', 'first_gap', 'last_gap', 'last_part', 'computed', 'predicted'))
        writer.writerows(rows)
    print(f'PASS: {checked} end-node partitions in all degrees 0..{max_degree}.', flush=True)
    print(f'Newton cache: {weight_multiplicity.cache_info()}', flush=True)

    for m in range(41):
        harmonic = comb(m + 6, 6) - (comb(m + 4, 6) if m >= 2 else 0)
        weyl = (m + 1)*(m + 2)*(m + 3)*(m + 4)*(2*m + 5)//120
        assert harmonic == weyl
    print('PASS: harmonic/G2 Weyl dimension identity at m=0..40.', flush=True)

    t = sp.symbols('t')
    # Manivel Example 4.3.3: open orbit for t!=0, codimension-one orbit at t=0.
    phi = {(0,1,2): 1, (0,3,4): 1, (0,5,6): t, (1,3,5): 1, (2,4,6): 1}
    B = metric(phi)
    detB = sp.factor(B.det())
    assert B.subs(t, 0).rank() == 4
    assert B.subs(t, 1).rank() == 7
    # Only the order matters; the nonzero scalar depends on the metric convention.
    quotient = sp.cancel(detB/t**3)
    assert quotient != 0 and not quotient.has(t), detB
    adj = B.adjugate()
    assert all(sp.cancel(v/t**2).is_polynomial(t) for v in adj)
    assert any(sp.cancel(v/t**2).subs(t,0) != 0 for v in adj)
    assert B*adj == detB*sp.eye(7)
    (out / 'METRIC_PATH_CHECK.txt').write_text(
        'Exact symbolic transverse-path check\n'
        'phi(t)=e123+e145+t e167+e246+e357\n'
        f'B(t)={B}\n'
        f'det B(t)={detB}\n'
        'rank B(0)=4; rank B(1)=7\n'
        'Every entry of adj B is divisible by t^2; at least one has order exactly2.\n'
        'The degree7 discriminant is a nonzero scalar multiple of t on this path.\n')
    print('PASS: cubic metric rank4 boundary; determinant order3; adjugate order2.', flush=True)


if __name__ == '__main__':
    main()
