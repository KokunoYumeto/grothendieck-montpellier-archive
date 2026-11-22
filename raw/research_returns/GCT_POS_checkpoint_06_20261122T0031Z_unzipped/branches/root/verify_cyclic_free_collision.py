"""Exact arithmetic for R-DIAG-001; no tensor-ring conclusion."""
from pathlib import Path
import json
import sympy as sp

v, u = sp.symbols('v u')
dimension = (1 + v**9) / (1 - v**6)**3
trace = (1 + v**9) / (1 - v**18)
assert sp.cancel(trace - 1 / (1 - v**9)) == 0
local = (1 - (1-u)**sp.Rational(9, 2)) / (1 - (1-u)**3)**3
top = sp.limit(u**2 * local, u, 0)
simple = sp.limit(u * (local - top/u**2), u, 0)
assert top == sp.Rational(1, 6)
assert simple == sp.Rational(5, 24)
assert 3 * sp.Rational(1, 2) * sp.Rational(1, 9) == top
dimension_sample = sp.series(dimension, v, 0, 121).removeO()
trace_sample = sp.series(trace, v, 0, 121).removeO()
difference = sp.expand(dimension_sample - trace_sample)
values = [int(difference.coeff(v, degree)) for degree in range(121)]
assert all(value >= 0 and value % 3 == 0 for value in values)
result = {
    'status': 'PASS',
    'series_in_u_1_minus_t_to_M': str(sp.series(local, u, 0, 1)),
    'top_coefficient': str(top),
    'simple_coefficient': str(simple),
    'v3_both': -1,
    'cyclic_trace_in_v': '1/(1-v^9)',
    'checked_difference_nonnegative_multiples_of_3_through': 120,
    'scope': 'Exact symbolic diagnostic, not the tensor ring; the monic-hypersurface module proof establishes the whole character identity.'
}
out = Path(__file__).resolve().parent / 'explorations'
out.mkdir(exist_ok=True)
(out/'cyclic_free_collision_arithmetic.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
