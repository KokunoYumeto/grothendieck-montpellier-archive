"""Exact symbolic corroboration of P15; not a proof or broad rank search."""
from pathlib import Path
import json
import sympy as s

x = s.symbols("x1:5")
t, y, z = s.symbols("t y z")
F = 2*x[0]*x[1] - (x[0]+x[1])*(x[2]+x[3]) + 2*x[2]*x[3]
u = [1, 1, -2, 0]
v = [0, 2, -1, -1]
product = s.eye(3)
for xi, ui, vi in zip(x, u, v):
    mat = s.eye(3)
    mat[0, 1] = ui*xi
    mat[1, 2] = vi*xi
    product *= mat

nodes = [1, -1, s.I, -s.I]
lagrange = [
    s.prod((y-nodes[j])/(ai-nodes[j]) for j in range(4) if j != i)
    for i, ai in enumerate(nodes)
]
centered = s.factor(F.subs(dict(zip(x, [t+z*li for li in lagrange])), simultaneous=True))

def cut_rank(indices):
    left = [x[i] for i in indices]
    right = [xi for xi in x if xi not in left]
    lm = list(s.utilities.iterables.subsets(range(len(left))))
    rm = list(s.utilities.iterables.subsets(range(len(right))))
    poly = s.Poly(F, *x)
    matrix = s.Matrix([
        [poly.coeff_monomial(s.prod(left[i] for i in a)*s.prod(right[j] for j in b))
         for b in rm]
        for a in lm
    ])
    return int(matrix.rank())

harmonic = []
for abscissas in [
    nodes,
    [s.Rational(0), s.Rational(1), s.Rational(2), s.Rational(2, 3)],
    [0, 3, 2, 6],
]:
    a, b, c, d = abscissas
    harmonic.append(str(s.simplify((a-c)*(b-d)+(a-d)*(b-c))))

result = {
    "matrix_product_identity": s.expand(product[0, 2]-F) == 0,
    "centered_SV1_identity": centered == 0,
    "balanced_cut_ranks": {
        "12|34": cut_rank([0, 1]),
        "13|24": cut_rank([0, 2]),
        "14|23": cut_rank([0, 3]),
    },
    "harmonic_residuals": harmonic,
    "scope": "Exact symbolic corroboration over characteristic zero; no general-width inference.",
}
assert result["matrix_product_identity"]
assert result["centered_SV1_identity"]
assert result["balanced_cut_ranks"] == {"12|34": 3, "13|24": 4, "14|23": 4}
assert harmonic == ["0", "0", "0"]
out = Path(__file__).with_name("P15_symbolic_checks.json")
out.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
