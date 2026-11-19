"""Exact algebraic checks for the explicit split semistable pairing diagnostic.

The geometric and cohomological proof is in root_post08_zhang_audit.md.
The program certifies polynomial identities and finite graph calculations;
it does not pretend that a finite point search proves geometric smoothness.
"""
from datetime import datetime, timezone
from pathlib import Path
from itertools import product
import json
import time
import sympy as s

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
x, y, v, w, a, b, P, X, Y = s.symbols('x y v w a b P X Y')
F = y*y - x*(x-1)*(x-5)
assert s.expand(F) == y*y - x**3 + 6*x*x - 5*x
disc = 16 * 5**2 * (5-1)**2
c4 = 16 * (5**2 - 5 + 1)
assert (disc, c4) == (6400, 336)
assert disc % 25 == 0 and disc % 125 != 0 and c4 % 5 != 0

# On the x chart, 5=xw and y=xv. The strict-transform equation is
# v^2-x+6-w=0; substitute w=v^2-x+6 to obtain xw=5.
x_chart_relation = x*(v*v-x+6)-5
assert s.expand(F.subs(y, x*v) - (x*x*(v*v-x+6)-5*x)) == 0
assert s.expand(F.subs(y, x*v) - x*x*(v*v-x+6-w) - x*(x*w-5)) == 0

# On the 5 chart, x=5a and y=5b.
p_chart = b*b-5*a**3+6*a*a-a
assert s.expand(F.subs({x:5*a, y:5*b})/25-p_chart) == 0

# The tangent cone, in homogeneous coordinates [P:X:Y], is a smooth conic.
Q = Y*Y+X*X-P*X
grad = [s.diff(Q,z) for z in (P,X,Y)]
proj = []
for point in product(range(5), repeat=3):
    if point == (0,0,0):
        continue
    first = next(t for t in point if t)
    normalized = tuple(t*pow(first,-1,5)%5 for t in point)
    if normalized != point:
        continue
    values = dict(zip((P,X,Y),point))
    if int(Q.subs(values)) % 5 == 0:
        assert any(int(g.subs(values)) % 5 for g in grad)
        proj.append(point)
assert len(proj) == 6
intersections = [u for u in range(5) if (u*u+1)%5 == 0]
assert intersections == [2,3]
assert all((2*u)%5 for u in intersections)

# Normalization of the original nodal cubic over F5.
norm = s.Poly(F.subs({x:v*v+1,y:v*(v*v+1)}),v, modulus=5)
assert norm.is_zero
incidence = s.Matrix([[1,-1],[1,-1]])
assert incidence.rank() == 1
graph_h1 = 2-incidence.rank()
assert graph_h1 == 1

out = dict(
    recorded_utc=datetime.now(timezone.utc).isoformat(),
    field='Q5; residue field F5; ell=3; base change to completed maximal unramified extension for the source convention',
    elliptic_curve='y^2=x(x-1)(x-5)',
    discriminant=disc, c4=c4,
    x_chart_relation=str(x_chart_relation),
    p_chart_relation=str(p_chart),
    exceptional_conic=str(Q),
    exceptional_F5_points=proj,
    component_intersection_parameters=intersections,
    normalization_identity_mod5=True,
    graph_incidence=[[int(t) for t in row] for row in incidence.tolist()],
    graph_incidence_rank=int(incidence.rank()),
    graph_h1_dimension=int(graph_h1),
    assertion_runtime_seconds=round(time.perf_counter()-start, 6),
    status='All exact checks passed',
    run_history='The first two runs stopped on syntactic expanded-versus-factored expression equalities in the two x-chart identities. Both assertions were corrected to compare expanded differences with zero. The third run passed all assertions but failed JSON serialization of SymPy integers; output now converts them to ordinary integers. No mathematical formula changed.',
    scope='Polynomial substitutions and finite incidence calculation only. The note proves regularity over the algebraic closure, strict semistability, supported duality, and degeneracy of the one-dimensional alternating pairing.'
)
target=root/'code/check_zhang_pairing_example_output.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
