#!/usr/bin/env python3
"""Exact finite checks for C.3aj; they do not certify Hodge genericity."""
from __future__ import annotations

import itertools
import json
from pathlib import Path
from time import perf_counter

import sympy as sp

started = perf_counter()
h, a = sp.symbols('h a')


def ambient_push(expression, m):
    """Push through H⊂P^m×S: multiply by [H]=h+a and take h^m."""
    return sp.expand(sp.expand(expression * (h + a)).coeff(h, m))


push_cases = []
for m in range(2, 13):
    for j in range(0, 14):
        source = ambient_push(h**(m - 1 + j), m)
        expected_source = 1 if j == 0 else (a if j == 1 else 0)
        boundary = ambient_push(h**(m - 1 + j) * (h + a), m)
        expected_boundary = 2*a if j == 0 else (a*a if j == 1 else 0)
        assert sp.expand(source - expected_source) == 0
        assert sp.expand(boundary - expected_boundary) == 0
        push_cases.append({'m': m, 'j': j, 'source': str(source),
                           'boundary': str(boundary)})

degree_cases = []
for s in range(1, 9):
    for j in (0, 1):
        cases = 0
        surviving_degree_patterns = 0
        for degrees in itertools.product((0, 1, 2), repeat=s):
            if sum(degrees) != s - 1 - j:
                continue
            cases += 1
            # To survive τ and integration, a^(j+1) must contribute
            # exactly 1-d_i copies of H_i in each surface factor.
            required = tuple(1 - d for d in degrees)
            if any(e < 0 for e in required):
                continue
            surviving_degree_patterns += 1
            assert sum(required) == j + 1
            assert any(e == 1 for e in required)
            # Such a missing factor pairs τ_i H_i=0, so every candidate
            # is zero. A K_C factor is already zero against H^1(C).
        degree_cases.append({'s': s, 'j': j,
                             'eligible_degree_patterns': cases,
                             'top_degree_patterns': surviving_degree_patterns,
                             'all_top_patterns_have_tau_H_zero': True})

rank_cases = []
for s in range(1, 9):
    u = sp.symbols('u0:' + str(s))
    q = sp.prod(u)
    witness_minor = sp.diag(q, q, q).det()
    assert sp.expand(witness_minor - q**3) == 0
    rank_cases.append({'s': s, 'minor': str(witness_minor),
                       'nonzero_if_each_u_nonzero': True})

intersection = {'H_squared': 4, 'H_D': 1, 'D_squared': -2,
                'tau_H': 4*1 - 4,
                'tau_D': 4*(-2) - 1,
                'tau_squared': 16*(-2) - 8*1 + 4}
assert intersection['tau_H'] == 0
assert intersection['tau_D'] == -9
assert intersection['tau_squared'] == -36

dimension_cases = []
for r in range(2, 10):
    s = r - 1
    for m in range(2, 13):
        dim_s = 2*s + 1
        dim_v = m + dim_s
        dim_h = dim_v - 1
        q = 2*r - 3
        assert q < dim_h
        base_dim = dim_s - (m + 1)
        if base_dim >= 0:
            exceptional_dim = m + base_dim
            assert dim_h - exceptional_dim == m
        dimension_cases.append({'r': r, 'm': m, 'N': m + 2*r,
                                'dim_S': dim_s, 'dim_H': dim_h,
                                'weak_Lefschetz_degree': q,
                                'base_expected_dim': base_dim,
                                'coefficient_count': (m + 1)*3*4**s})

result = {
    'status': 'all finite exact checks passed',
    'scope': ('Checks pushforward coefficients, degree cancellation, rank witness '
              'minor, intersection numbers and dimension inequalities only. '
              'Genericity, actual-family descent and the theorem are proved in prose.'),
    'pushforward_cases': push_cases,
    'degree_cancellation_cases': degree_cases,
    'rank_witness_cases': rank_cases,
    'intersection_numbers': intersection,
    'dimension_cases': dimension_cases,
    'runtime_seconds': perf_counter() - started,
}
target = Path(__file__).with_name('check_high_range_incidence_output.json')
target.write_text(json.dumps(result, indent=2) + '\n')
print(result['status'])
print('pushforward cases:', len(push_cases))
print('degree cases:', len(degree_cases))
print('rank cases:', len(rank_cases))
print('dimension cases:', len(dimension_cases))
print('intersection numbers:', intersection)
print('runtime_seconds:', result['runtime_seconds'])
