#!/usr/bin/env python3
"""Exact, bounded theta-13 search on the A27 curve over F_256.

The Taylor-jet idea follows gt_certificates/theta13_direct.py. This is
an adapted search, not a claimed independent verification of that code.
No Jacobian package, floating-point operation, or probabilistic test is used.
The field is F_2[z]/(z^8+z^4+z^3+z+1); u is the smaller root of u^2+u+1.
After X=1/x, Y=y X^2 the A27 equation is
    Y^2+X^2Y=u X^5+X^3+u X.
The unique infinity W has pole orders 2 and 5. A function with poles
at most 13W is A(X)+B(X)Y, deg A<=6, deg B<=4. Exact jets decide
whether a nonramified rational R satisfies 13(R-W)~0.
"""
from pathlib import Path
import hashlib
import json

MOD = 0x11B
Q = 256


def slow_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & Q:
            a ^= MOD
    return out


TABLE = [[slow_mul(a, b) for b in range(Q)] for a in range(Q)]


def mul(a, b):
    return TABLE[a][b]


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


INVERSES = [0] + [power(a, Q - 2) for a in range(1, Q)]
assert all(mul(a, INVERSES[a]) == 1 for a in range(1, Q))


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def pmul(a, b):
    out = [0] * max(0, len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] ^= mul(ai, bj)
    return trim(out)


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, a)
    return out


def peval(a, x):
    out = 0
    for ai in reversed(a):
        out = mul(out, x) ^ ai
    return out


def translate(a, x):
    out = []
    for ai in reversed(a):
        out = add(pmul(out, [x, 1]), [ai])
    return out


def nullspace(matrix):
    mat = [r[:] for r in matrix]
    ncols = len(mat[0])
    pivots = []
    row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, len(mat)) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[row], mat[pivot] = mat[pivot], mat[row]
        scale = INVERSES[mat[row][col]]
        mat[row] = [mul(scale, x) for x in mat[row]]
        for i in range(len(mat)):
            if i != row and mat[i][col]:
                scale = mat[i][col]
                mat[i] = [x ^ mul(scale, y) for x, y in zip(mat[i], mat[row])]
        pivots.append(col)
        row += 1
    free = [i for i in range(ncols) if i not in pivots]
    vectors = []
    for fcol in free:
        vector = [0] * ncols
        vector[fcol] = 1
        for i, col in reversed(list(enumerate(pivots))):
            value = 0
            for j in free:
                value ^= mul(mat[i][j], vector[j])
            vector[col] = value
        assert all(not sum_in_field(mul(aij, vj) for aij, vj in zip(r, vector))
                   for r in matrix)
        vectors.append(vector)
    return vectors, len(pivots)


def sum_in_field(items):
    value = 0
    for x in items:
        value ^= x
    return value


def main():
    roots = [a for a in range(Q) if mul(a, a) ^ a ^ 1 == 0]
    assert len(roots) == 2
    u = roots[0]
    h, f = [0, 0, 1], [0, u, 0, 1, 0, u]
    points = [(x, y) for x in range(Q) for y in range(Q)
              if mul(y, y) ^ mul(mul(x, x), y) ^ peval(f, x) == 0]
    assert len(points) + 1 == 256
    candidates = []
    ranks = {}
    for x, y in points:
        if x == 0:
            # Its difference from infinity is nonzero two-torsion, not 13-torsion.
            assert y == 0
            continue
        fy = translate(f, x)
        coeff = [y]
        for i in range(1, 13):
            rhs = fy[i] if i < len(fy) else 0
            if i % 2 == 0:
                rhs ^= mul(coeff[i // 2], coeff[i // 2])
            if i >= 2:
                rhs ^= coeff[i - 2]
            coeff.append(mul(rhs, INVERSES[mul(x, x)]))
        matrix = [[coeff[i-j] for j in range(5)] for i in range(7, 13)]
        vectors, rank = nullspace(matrix)
        ranks[rank] = ranks.get(rank, 0) + 1
        if not vectors:
            continue
        assert len(vectors) == 1
        bt = vectors[0]
        assert bt[-1]
        scale = INVERSES[bt[-1]]
        bt = [mul(scale, b) for b in bt]
        at = [sum_in_field(mul(bt[j], coeff[i-j])
                          for j in range(min(i, 4)+1)) for i in range(7)]
        a, b = translate(at, x), translate(bt, x)
        norm = add(add(pmul(a, a), pmul(pmul(a, b), h)), pmul(pmul(b, b), f))
        target = [mul(u, c) for c in ppow([x, 1], 13)]
        assert norm == target
        assert peval(a, x) ^ mul(peval(b, x), y) == 0
        conj = peval(a, x) ^ mul(peval(b, x), y ^ mul(x, x))
        assert conj != 0
        candidates.append({'R': [x, y], 'A': a, 'B': b,
                           'norm': norm, 'conjugate_value': conj, 'rank': rank})
    result = {
        'curve_A27': 'y^2+y=u*x^3+x+u/x over F4, u^2+u+1=0',
        'transformed_curve': 'Y^2+X^2*Y=u*X^5+X^3+u*X',
        'field': {'size': Q, 'modulus': MOD, 'u': u,
                  'encoding': 'binary polynomial coefficients, increasing powers'},
        'rational_point_count': len(points)+1,
        'rational_nonramified_points_tested': len(points)-1,
        'Taylor_matrix_rank_counts': ranks,
        'nonzero_rational_theta13_points': candidates,
        'scope': 'Only exact order13 theta incidence on this displayed model over F256; no universal or geometric absence conclusion from a negative search.',
        'method_credit': 'Taylor jet method adapted from work/gt_certificates/positive_rank_theta/theta13_direct.py; not an independent check of that implementation.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
