"""HD-S34: exact examples of the coset and integral corner maps.

Rebuilds G(4,1,m), m=2,3, directly as weighted permutations.  The universal
proof is in gaussian_monomial_scope.tex and does not use these examples
as a classification or an extrapolation.
"""
from itertools import permutations, product
from collections import defaultdict
from pathlib import Path
import json


def compose(g, h):
    p, a = g
    q, b = h
    return tuple(p[qj] for qj in q), tuple((b[j]+a[q[j]]) % 4 for j in range(len(p)))


def left(g, coefficients):
    return {compose(g, h): n for h, n in coefficients.items()}


def right(coefficients, g):
    return {compose(h, g): n for h, n in coefficients.items()}


phase = [(1, 0), (0, 1), (-1, 0), (0, -1)]
rows = []
for m in (2, 3):
    identity = tuple(range(m)), (0,)*m
    elements = [(p, a) for p in permutations(range(m)) for a in product(range(4), repeat=m)]
    subgroup = [g for g in elements if g[0][0] == 0]
    D = len(subgroup)
    assert len(elements) == m*D
    numerator = {g: 2*phase[g[1][0]][0] for g in subgroup if g[1][0] % 2 == 0}
    h0 = tuple(range(m)), (1,)+(0,)*(m-1)
    swap = (1, 0)+tuple(range(2, m)), (0,)*m
    assert compose(h0, swap) != compose(swap, h0)
    assert left(h0, numerator) == right(numerator, h0)
    assert right(numerator, compose(h0, h0)) == {g: -n for g, n in numerator.items()}
    square = defaultdict(int)
    for g, a in numerator.items():
        for h, b in numerator.items():
            square[compose(g, h)] += a*b
    square = {g: n for g, n in square.items() if n}
    assert square == {g: D*n for g, n in numerator.items()}
    matrix = [[(0, 0) for j in range(m)] for i in range(m)]
    for (p, a), n in numerator.items():
        for j in range(m):
            x, y = matrix[p[j]][j]
            u, v = phase[a[j]]
            matrix[p[j]][j] = x+n*u, y+n*v
    assert matrix == [[(D if i == j == 0 else 0, 0) for j in range(m)] for i in range(m)]
    local_cycles = 0
    for p, a in elements:
        seen = set()
        for start in range(m):
            if start in seen:
                continue
            current = start
            exponent = 0
            length = 0
            while current not in seen:
                seen.add(current)
                exponent = (exponent+a[current]) % 4
                current = p[current]
                length += 1
            assert current == start
            u, v = phase[exponent]
            norm = (u-1)**2+v*v
            assert norm in (0, 2, 4)
            local_cycles += 1
    rows.append({'m': m, 'order': len(elements), 'H_order_and_D': D,
                 'noncentral_h0_verified': True,
                 'integer_group_algebra_identities': ['(D e)^2=D(D e)', '[D e,h0]=0', '(D e)h0^2=-(D e)'],
                 'natural_matrix_of_e': 'projection onto first coordinate',
                 'weighted_local_cycles_checked': local_cycles})

report = {'status': 'PASS', 'examples': rows,
          'scope': 'Exact actual examples of the integral corner and weighted-cycle maps; the universal K-defined-block proof is separate.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
