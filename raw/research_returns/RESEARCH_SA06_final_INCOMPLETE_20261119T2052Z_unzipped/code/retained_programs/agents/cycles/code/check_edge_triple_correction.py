"""Bounded exact checks for ET; no descent or geometric theorem is certified."""
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
checks = []

def record(name, condition, scope):
    if not bool(condition):
        raise AssertionError(name)
    checks.append({"name": name, "passed": True, "scope": scope})

def complex_check(name, vertices, faces):
    edges = sorted({edge for face in faces for edge in combinations(face, 2)})
    d0 = sp.zeros(len(edges), len(vertices))
    for row, (i, j) in enumerate(edges):
        d0[row, vertices.index(i)] = -1
        d0[row, vertices.index(j)] = 1
    d1 = sp.zeros(len(faces), len(edges))
    for row, face in enumerate(faces):
        for omitted in range(3):
            edge = tuple(v for pos, v in enumerate(face) if pos != omitted)
            d1[row, edges.index(edge)] = (-1)**omitted
    record(name+"_cochain_square", d1*d0 == sp.zeros(len(faces), len(vertices)),
           "Ordered edge/face signs; repeated faces remain separate rows.")
    cycles = d1.T.nullspace()
    annihilator = sp.Matrix.vstack(*(z.T for z in cycles)) if cycles else sp.zeros(0, len(faces))
    record(name+"_annihilator_image", annihilator*d1 == sp.zeros(len(cycles), len(edges))
           and d1.rank()+annihilator.rank() == len(faces),
           "Exact rational image-annihilator equality in this finite complex.")
    edge_values = sp.Matrix([row+1 for row in range(len(edges))])
    defect = d1*edge_values
    solution, params = d1.gauss_jordan_solve(defect)
    solution = solution.subs({x: 0 for x in params})
    record(name+"_constant_edge_correction", d1*solution == defect,
           "A defect known to satisfy the period constraint has an exact edge correction.")
    for index, z in enumerate(cycles):
        record(name+f"_period_degree_{index}", d1.T*z == sp.zeros(len(edges), 1),
               "Each triple-point divisor has degree zero edge by edge.")
    return {"name": name, "vertices": len(vertices), "edges": len(edges),
            "faces": len(faces), "h2": len(cycles), "d1_rank": d1.rank()}

complexes = [
    complex_check("one_triangle", [0,1,2], [(0,1,2)]),
    complex_check("two_triangle_disk", [0,1,2,3], [(0,1,2),(0,2,3)]),
    complex_check("tetrahedral_sphere", [0,1,2,3], list(combinations(range(4),3))),
    complex_check("two_distinct_triple_points", [0,1,2], [(0,1,2),(0,1,2)]),
]

t = sp.symbols("t")
p = (t-2)/2
record("lift_polynomial_weights", p.subs(t,2)==0 and p.subs(t,4)==1,
       "No semisimplicity of the intermediate homotopy group is used.")
q = sp.prod(t-a for a in (1,2,8))/sp.prod(4-a for a in (1,2,8))
record("projective_threefold_weight2_projector",
       [q.subs(t,a) for a in (1,2,4,8)] == [0,0,1,0],
       "Elementary projector polynomial, conditional on the separately proved finite gamma filtration.")

a,b,c,x,y,z,h12,h23,h31,n12,n23,n31 = sp.symbols(
    "a b c x y z h12 h23 h31 n12 n23 n31")
# C12^2 on E1 is n12, on E2 is (-h12-b*n12-c)/a;
# similarly for the other two edges.  Each triple intersection has length one.
s12 = (-h12-b*n12-c)/a
s23 = (-h23-c*n23-a)/b
s31 = (-h31-a*n31-b)/c
square = (a*((b*x)**2*n12+(c*z)**2*s31-2*b*c*x*z)
          + b*((a*x)**2*s12+(c*y)**2*n23-2*a*c*x*y)
          + c*((b*y)**2*s23+(a*z)**2*n31-2*a*b*y*z))
energy = -a*b*h12*x*x-b*c*h23*y*y-c*a*h31*z*z-a*b*c*(x+y+z)**2
record("one_triple_weighted_energy_identity", sp.cancel(square-energy)==0,
       "Symbolic identity after the displayed normal-bundle degree relations; ampleness is a separate theorem hypothesis.")

report = {"statement": "C.3bq / ET.1-ET.12", "started_at_utc": started,
          "completed_at_utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": perf_counter()-tic, "checks_passed": len(checks),
          "checks_failed": 0, "complexes": complexes, "checks": checks,
          "limitations": "These finite linear-algebra and polynomial checks do not prove K-theory descent, proper-family realization, the universal period condition, or any geometric existence statement."}
out = Path(__file__).resolve().parents[1]/"output"
out.mkdir(exist_ok=True)
encoded = json.dumps(report, indent=2)
(out/"edge_triple_correction_certificate.json").write_text(encoded+"\n")
(out/"edge_triple_correction_certificate.out").write_text(encoded+"\n")
print(encoded)
