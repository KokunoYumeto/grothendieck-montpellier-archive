#!/usr/bin/env python3
"""Exact finite check of D-NR04's cubic trace-multiplication example.

This is not an implementation or a run of the generic-model enumeration.
All branch parameters remain symbolic: only their distinctness is required.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json


def exact_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivots = []
    r = 0
    for c in range(len(a[0])):
        j = next((j for j in range(r, len(a)) if a[j][c]), None)
        if j is None:
            continue
        a[r], a[j] = a[j], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c]:
                q = a[j][c]
                a[j] = [x - q * y for x, y in zip(a[j], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return r, pivots


def main():
    # y^3=P Q^2, deg P=deg Q=6; all twelve zeros are distinct.
    degree = 3
    genus = 1 + (degree * (-2) + 12 * (degree - 1)) // 2
    assert genus == 10
    vals = []
    for a in range(5):
        # At finite branch exponent k, ord(dz)=2, ord(y)=k,
        # and ord(Q)=3 exactly at a branch with k=2.
        va = [2 - k for k in (1, 2)] + [6 - 2 - a]
        vb = [2 + (3 if k == 2 else 0) - 2 * k for k in (1, 2)]
        vb += [12 - 6 - 2 - a]
        assert min(va + vb) >= 0
        vals.append({'exponent': a, 'alpha_orders': va, 'beta_orders': vb})
    assert 6 - 2 - 5 == -1  # the next monomial in either list is not regular
    columns = [(a, b) for a in range(5) for b in range(5)]
    matrix = [[int(a + b == k) for a, b in columns] for k in range(9)]
    rank, pivots = exact_rank(matrix)
    minor = [[row[c] for c in pivots] for row in matrix]
    assert rank == 9
    assert minor == [[int(i == j) for j in range(9)] for i in range(9)]
    # 5 independent forms in each of two distinct characters account for
    # the full genus10 Hodge space, so the local regularity lists are bases.
    result = {
        'statement': 'D-NR04 finite cubic example',
        'status': 'PASS',
        'generic_model_search_executed': False,
        'group': 'C3',
        'branch_exponents': [1] * 6 + [2] * 6,
        'genus': genus,
        'eigenspace_dimensions': [5, 5],
        'valuation_order': ['exponent1 branch', 'exponent2 branch', 'infinity'],
        'valuation_checks': vals,
        'matrix_size': [9, 25],
        'matrix': matrix,
        'rank': rank,
        'pivot_columns': pivots,
        'pivot_pairs': [columns[c] for c in pivots],
        'nonzero_minor': 1,
        'proof': 'products alpha_a beta_b=z^(a+b)(dz)^2/(P Q); powers0..8 span',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out = Path(__file__).with_name('nielsen_rank_example.json')
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in
                      ['status', 'genus', 'eigenspace_dimensions', 'matrix_size',
                       'rank', 'nonzero_minor', 'generic_model_search_executed']}))


if __name__ == '__main__':
    main()
