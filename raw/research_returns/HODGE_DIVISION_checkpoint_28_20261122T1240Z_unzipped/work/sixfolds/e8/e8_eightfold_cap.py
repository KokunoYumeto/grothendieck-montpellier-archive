#!/usr/bin/env python3
"""HD-S26 exact witness for the sharp branch-parameter cap.

The proof of the universal cap is in e8_eightfold_rank_cap.tex.
This script makes no claim that the example has period rank 15.
"""
import json
from pathlib import Path
import sympy as S
from e8_group_and_tuple import a, cartan, identity, integer

u = S.I * a**5
simple = []
for j in range(8):
    row = S.zeros(1, 8)
    row[j] = 1
    simple.append(identity - cartan[:, j] * row)
assert a**10 == -identity and u*u == identity
assert (identity-u).rank() == 4
assert all(s*s == identity and (identity-s).rank() == 1 for s in simple)
tuple_matrices = [u,u] + [s for s in simple for _ in range(2)]
product = identity
for g in tuple_matrices:
    product *= g
assert product == identity
codim = [(identity-g).rank() for g in tuple_matrices]
assert len(codim) == 18 and sum(codim) == 24
assert u*(a**5).inv() == S.I*identity
report = dict(statement='HD-S26', check='PASS', date='2026-11-21',
              branch_count=18, branch_codimensions=codim,
              parabolic_dimension=sum(codim)-16,
              hodge_dimensions=[4,4], hurwitz_dimension=15,
              universal_period_rank_upper_bound=15,
              full_group_generation='simple W(E8) reflections plus i recovered exactly',
              period_rank_equality_claimed=False)
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
