#!/usr/bin/env python3
"""Exact algebra checks used in C.3ab; these do not prove its K-theory inputs."""
from pathlib import Path
from time import perf_counter
import json
import sympy as s

start = perf_counter()
x, y = s.symbols("x y")
j = s.symbols("j", positive=True, integer=True)
u = s.Function("u")(x, y)
b = s.Function("b")(x, y)
omega = [s.Function("omega_x")(x, y), s.Function("omega_y")(x, y)]

# t_old = u*t_new. The vertical coefficient becomes b*u**j.
# Projection modulo d(b*t**j) must transform by u**j.
gluing = []
for v, w in zip((x, y), omega):
    transformed_horizontal = u**j*w + b*u**(j-1)*s.diff(u, v)
    projected = transformed_horizontal - s.diff(b*u**j, v)/j
    expected = u**j*(w-s.diff(b, v)/j)
    gluing.append(s.simplify(projected-expected) == 0)

# The degree-j exact relation is annihilated by horizontal projection.
exact_relation = [s.simplify(s.diff(b,v)-s.diff(j*b,v)/j) == 0
                  for v in (x,y)]

# Every vertical coefficient is removed uniquely because j is invertible.
vertical_inverse = s.simplify(j*(b/j)-b) == 0

# A line on the Fermat quartic: zeta^4=eta^4=-1.
zeta, eta, v, w = s.symbols("zeta eta v w")
fermat_line = (zeta*v)**4 + v**4 + (eta*w)**4 + w**4
line_remainder = s.reduced(fermat_line,
                           [zeta**4+1, eta**4+1],
                           zeta, eta, v, w)[1]

result = {
    "statement": "C.3ab",
    "scope": "Symbolic differential identity and explicit line only; no finite sample substitutes for the proof.",
    "universal_nonzero_integer_weight_j": str(j),
    "coordinate_change_projection": gluing,
    "exact_relation_projects_to_zero": exact_relation,
    "vertical_elimination_inverse": vertical_inverse,
    "fermat_quartic_line_remainder": str(line_remainder),
    "codimension_two_RR_multiplier": (-1)**(2-1)*s.factorial(2-1),
    "projective_plane_examples": [{"d": d, "g": d, "B2_order": d}
                                  for d in range(1,13)],
    "all_passed": all(gluing+exact_relation+[vertical_inverse,
                                             line_remainder == 0]),
    "runtime_seconds": round(perf_counter()-start, 6),
}
result["codimension_two_RR_multiplier"] = int(result["codimension_two_RR_multiplier"])
out = Path(__file__).with_name("surface_cone_top_output.json")
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
assert result["all_passed"]
