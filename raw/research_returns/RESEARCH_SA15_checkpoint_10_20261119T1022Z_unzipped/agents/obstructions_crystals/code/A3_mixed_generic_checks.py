#!/usr/bin/env python3
"""Exact auxiliary arithmetic for the mixed generic-product theorem.

The all-degree geometric rank theorem is proved in TeX.  This certificate
checks the Weierstrass invariants and the exact numerical identities used
in the nodal construction; finite checks are not used as an induction.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as S

started = perf_counter()
t, j = S.symbols('t j')
a1, a2, a3, a4, a6 = t, 0, 1, 0, 0
b2 = a1**2 + 4*a2
b4 = 2*a4 + a1*a3
b6 = a3**2 + 4*a6
b8 = a1**2*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3**2 - a4**2
c4 = S.expand(b2**2 - 24*b4)
delta = S.expand(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
assert c4 == t**4 - 24*t
assert delta == t**3 - 27
c4mod2 = S.Poly(c4, t, modulus=2).as_expr()
deltamod2 = S.Poly(delta, t, modulus=2).as_expr()
assert c4mod2 == t**4
assert deltamod2 == t**3 + 1
assert S.Poly(c4mod2**3, t, modulus=2).as_expr() == t**12
assert S.rem(t**12 - j*(t**3+1), t**3+1, t) == 1

degree_rows = []
for d in range(1, 10001):
    m = 3*d
    g = m*m + 1
    relative_dimension = m*m - 1
    relative_rank = m*m - (1 if d % 2 else 2)
    full_rank = relative_rank + 1
    assert g - full_rank == (1 if d % 2 else 2)
    assert relative_dimension - relative_rank == (0 if d % 2 else 1)
    if d % 2 == 0:
        n = 3*(d-1)
        intersections = 2*3*n
        genus_union = (3*3+1) + (n*n+1) + intersections - 1
        rank_union = 3*3 + n*n + intersections - 1
        assert genus_union == g
        assert rank_union == m*m-1 == full_rank
    if d <= 12:
        degree_rows.append({'d':d, 'relative_dimension':relative_dimension,
                            'relative_rank':relative_rank, 'full_genus':g,
                            'full_2_rank':full_rank})

result = {'status':'PASS',
          'scope':'Auxiliary exact invariants and numerical identities; geometric proof is in A3_mixed_generic_ranks.tex.',
          'c4_over_Z':str(c4), 'Delta_over_Z':str(delta),
          'c4_mod_2':str(c4mod2), 'Delta_mod_2':str(deltamod2),
          'j':str(t**12/(t**3+1)),
          'excluded_discriminant_root_remainder':1,
          'degrees_checked':10000, 'sample_degree_rows':degree_rows,
          'elapsed_seconds':perf_counter()-started}
Path(__file__).with_name('A3_mixed_generic_checks_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
