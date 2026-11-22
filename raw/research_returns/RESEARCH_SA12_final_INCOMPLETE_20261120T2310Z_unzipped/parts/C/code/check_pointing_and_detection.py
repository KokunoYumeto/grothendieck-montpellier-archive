#!/usr/bin/env python3
"""Finite certificates for C:nori and C:detect-proper-subgroup.

We check the quadratic constant-field torsor and the two-copy permutation
construction on every proper subgroup of cyclic groups of orders 2--8.
The general group-scheme and geometric arguments remain proofs in TeX.
"""
import itertools
import json
import time

started = time.perf_counter()

def mul(a, b):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % 5,
            (a[0]*b[1] + a[1]*b[0]) % 5)

def power(a, n):
    r = (1, 0)
    for _ in range(n):
        r = mul(r, a)
    return r

elements = list(itertools.product(range(5), repeat=2))
u = (0, 1)
assert mul(u, u) == (2, 0)
assert not any(x*x % 5 == 2 for x in range(5))
assert all(power(x, 25) == x for x in elements)
assert power(u, 5) == (0, 4)
fixed = [x for x in elements if power(x, 5) == x]
assert fixed == [(x, 0) for x in range(5)]

cases = []
for n in range(2, 9):
    W = list(itertools.product(range(2), range(n)))
    for d in range(2, n + 1):
        if n % d:
            continue
        H = set(range(0, n, d))

        def tau(z):
            copy, x = z
            return (1-copy, x) if x in H else z

        def left(g, z):
            return (z[0], (g+z[1]) % n)

        def conjugate(g, z):
            return tau(left(g, tau(z)))

        assert all(tau(tau(z)) == z for z in W)
        assert all(left((g+h) % n, z) == left(g, left(h, z))
                   for g in range(n) for h in range(n) for z in W)
        assert all(conjugate((g+h) % n, z) == conjugate(g, conjugate(h, z))
                   for g in range(n) for h in range(n) for z in W)
        equalizer = {g for g in range(n)
                     if all(left(g, z) == conjugate(g, z) for z in W)}
        assert equalizer == H
        cases.append({'group_order': n, 'subgroup_order': len(H),
                      'letters': len(W), 'equalizer_is_subgroup': True})

print(json.dumps({
    'quadratic_torsor': {
        'field': 'GF(5)[u]/(u^2-2)',
        'elements_checked': len(elements),
        'frobenius_u': '-u',
        'frobenius_fixed_elements': len(fixed),
        'GF5_roots_of_x2_minus_2': 0,
        'chosen_geometric_embedding_exists': True,
    },
    'permutation_detection': {
        'group_orders': list(range(2, 9)),
        'proper_subgroups_checked': len(cases),
        'cases': cases,
    },
    'elapsed_seconds': time.perf_counter() - started,
    'scope': 'Exact finite-field and permutation certificates; general finite-group-scheme detection and the cuspidal-curve comparison are proved in paper_C.tex.'
}, indent=2))
