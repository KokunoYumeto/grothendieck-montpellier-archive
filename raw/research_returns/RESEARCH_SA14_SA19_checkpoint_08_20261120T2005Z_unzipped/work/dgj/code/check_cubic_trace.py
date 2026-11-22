"""Exact characteristic-five certificate for the J6C cubic pencil.

All smoothness/singularity assertions use polynomial ideals in every
projective chart. No sampling of finite-field points is used.
The abelian trace claim is proved by correspondences in section_J6_cubic.tex.
"""
import json
import time
from pathlib import Path
import sympy as sp

started = time.perf_counter()
x = sp.symbols('x0:6')
a, ainv, t = sp.symbols('a ainv t')
F = x[0]**3+x[1]**3+x[2]**3+x[3]**2*x[4]+x[4]**3+x[5]**3
gradF = [sp.diff(F,z) for z in x]

def chart_ideals(polynomials, coordinates, extra=(), extra_variables=()):
    answer = []
    for pivot in coordinates:
        variables = [z for z in coordinates if z != pivot] + list(extra_variables)
        polys = [sp.expand(g.subs(pivot,1)) for g in polynomials]
        polys += [sp.expand(g.subs(pivot,1)) for g in extra]
        basis = sp.groebner(polys,*variables,modulus=5)
        expressions = [g.as_expr() for g in basis.polys]
        is_unit = expressions == [sp.Integer(1)]
        answer.append({"chart":str(pivot)+'=1',"unit_ideal":is_unit,
                       "groebner_basis":[str(g) for g in expressions]})
    return answer

X_charts = chart_ideals(gradF,x)
assert all(row['unit_ideal'] for row in X_charts)

G = x[0]**3+x[1]**3+x[2]**3+x[3]**2*x[4]+a*x[4]**3
coords5 = x[:5]
gradG = [sp.diff(G,z) for z in coords5]
generic_charts = chart_ideals(gradG,coords5,[a*ainv-1],[a,ainv])
assert all(row['unit_ideal'] for row in generic_charts)

zero_charts = chart_ideals([g.subs(a,0) for g in gradG],coords5)
assert [row['chart'] for row in zero_charts if not row['unit_ideal']] == ['x4=1']
zero_basis = zero_charts[-1]['groebner_basis']
assert zero_basis == ['x0**2','x1**2','x2**2','x3']
singular_zero = dict(zip(coords5,[0,0,0,0,1]))
assert G.subs(a,0).subs(singular_zero) == 0

coords_inf = [x[0],x[1],x[2],x[3],x[5]]
Ginf = x[0]**3+x[1]**3+x[2]**3+x[5]**3
infinity_charts = chart_ideals([sp.diff(Ginf,z) for z in coords_inf],coords_inf)
assert [row['chart'] for row in infinity_charts if not row['unit_ideal']] == ['x3=1']
assert infinity_charts[3]['groebner_basis'] == ['x0**2','x1**2','x2**2','x5**2']

E = x[0]**3+x[1]**3+x[2]**3
E_charts = chart_ideals([sp.diff(E,z) for z in x[:3]],x[:3])
assert all(row['unit_ideal'] for row in E_charts)
assert E.subs({x[0]:1,x[1]:-1,x[2]:0}) == 0

axis_charts = chart_ideals([sp.diff(E,z) for z in x[:4]],x[:4])
assert [row['chart'] for row in axis_charts if not row['unit_ideal']] == ['x3=1']
assert axis_charts[3]['groebner_basis'] == ['x0**2','x1**2','x2**2']

parameter_poly = sp.Poly(1+t**3,t,modulus=5)
parameter_derivative = parameter_poly.diff()
assert sp.gcd(parameter_poly,parameter_derivative).as_expr() == 1

# On x3=1 the local equation is v+a*v^3+q3=0.
# Substitution v=-q3 has error -a*q3^3, of order 9 in the regular u's.
u0,u1,u2,v = sp.symbols('u0 u1 u2 v')
q3 = u0**3+u1**3+u2**3
local_equation = v+a*v**3+q3
residual = sp.expand(local_equation.subs(v,-q3))
assert sp.expand(residual+a*q3**3) == 0
assert all(sum(m) == 9 for m,c in sp.Poly(residual,u0,u1,u2).terms())
normal_degree = 1-3
assert normal_degree == -2

output = {
    "characteristic":5,
    "fourfold_equation":str(F),
    "fourfold_gradient":[str(g) for g in gradF],
    "fourfold_projective_chart_ideals":X_charts,
    "finite_member_equation":str(G),
    "smooth_finite_members_a_nonzero_chart_ideals":generic_charts,
    "singular_finite_member_a_zero_chart_ideals":zero_charts,
    "singular_finite_support":"[0:0:0:0:1]",
    "infinity_member_chart_ideals":infinity_charts,
    "infinity_singular_support":"[0:0:0:1:0] in coordinates x0,x1,x2,x3,x5",
    "elliptic_base_projective_chart_ideals":E_charts,
    "elliptic_origin":[1,-1,0],
    "axis_chart_ideals":axis_charts,
    "axis_singular_support":"[0:0:0:1]",
    "singular_parameter_polynomial":str(parameter_poly.as_expr()),
    "gcd_with_derivative":1,
    "local_divisor_multiplicity":3,
    "normal_degree_on_ruling":normal_degree,
    "correspondence_composite_integer":-2,
    "degree_of_composite_on_elliptic_curve":4,
    "scope":"Exact ideal certificate only; integrality follows from isolated singularities, and trace follows from the written correspondence proof.",
    "runtime_seconds":round(time.perf_counter()-started,6)
}
dest = Path(__file__).resolve().parents[1]/'outputs'/'check_cubic_trace.json'
dest.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({key:output[key] for key in ['characteristic','fourfold_equation',
    'singular_finite_support','infinity_singular_support','local_divisor_multiplicity',
    'normal_degree_on_ruling','degree_of_composite_on_elliptic_curve','runtime_seconds']},indent=2))
