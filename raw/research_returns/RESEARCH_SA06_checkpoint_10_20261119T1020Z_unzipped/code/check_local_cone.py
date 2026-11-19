#!/usr/bin/env python3
"""Exact equation checks for C.3f; this does not certify Chow non-torsion."""
from pathlib import Path
import json
import sympy as s

x0, x1, x2, x3, u, v, w, zeta, t = s.symbols(
    'x0 x1 x2 x3 u v w zeta t')
F = x0**4 + x1**4 + x2**4 + x3**4
generic_relation = w**4 + u**4 + v**4 + 1
zeta_relation = zeta**4 + 1
f = x2-w*x3
checks = {}
checks['P_on_quartic'] = s.rem(F.subs({x0:u,x1:v,x2:w,x3:1}),
                              generic_relation,w) == 0
checks['a_on_quartic'] = s.rem(F.subs({x0:1,x1:zeta,x2:0,x3:0}),
                              zeta_relation,zeta) == 0
checks['P_on_plane'] = f.subs({x0:u,x1:v,x2:w,x3:1}) == 0
checks['a_on_plane'] = f.subs({x0:1,x1:zeta,x2:0,x3:0}) == 0
plane = s.expand(F.subs(x2,w*x3))
checks['plane_equation'] = s.expand(plane-x0**4-x1**4-(1+w**4)*x3**4) == 0
coefficient = s.rem(1+w**4,generic_relation,w)
checks['generic_plane_coefficient_nonzero'] = coefficient == -u**4-v**4
checks['quartic_partial_derivatives'] = all(
    s.diff(F,x) == 4*x**3 for x in (x0,x1,x2,x3))
# On each projective chart one derivative is a nonzero constant.
checks['quartic_projective_jacobian_chart_certificates'] = all(
    s.diff(F,x).subs(x,1) == 4 for x in (x0,x1,x2,x3))
aa, bb = s.symbols('aa bb')
plane_generic = x0**4+x1**4+aa*x3**4
plane_charts = {}
for x in (x0,x1,x3):
    polys = [plane_generic] + [s.diff(plane_generic,y)
                               for y in (x0,x1,x3)] + [aa*bb-1,x-1]
    gb = s.groebner(polys,x0,x1,x3,aa,bb,domain=s.QQ)
    plane_charts[str(x)] = list(gb) == [1]
checks['plane_smooth_when_coefficient_invertible'] = all(plane_charts.values())
checks['blowup_chart_factorization'] = s.expand(
    F.subs({x0:t*u,x1:t*v,x2:t*w,x3:t}) - t**4*generic_relation) == 0

result = {
    'statement':'C.3f',
    'arithmetic':'exact polynomials over Q; u,v algebraically independent',
    'checks':checks,
    'plane_chart_groebner_bases_equal_one':plane_charts,
    'plane_coefficient_mod_relation':str(coefficient),
    'all_passed':all(checks.values()),
    'scope':'Equation and smoothness certificates only. Non-torsion, strict local descent, and all-dimensional claims are proved in C.3e–g, not inferred from these computations.'
}
out=Path(__file__).resolve().parents[1]/'logs'/'local_cone_certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if not result['all_passed']:
    raise SystemExit(1)
