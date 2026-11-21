"""Exact finite graph checks and the complete integer comparison in O014."""
import json
from datetime import datetime, timezone
from math import comb
from pathlib import Path

import sympy as sp

from check_padding_degree_split import indices, matrix_for


symbolic_cases = []
for b, r, caps in [(3, 3, (3, 1)), (4, 3, (4, 1))]:
    L = sp.Symbol("L")
    z = sp.symbols(f"z0:{r-1}")
    support = [a for a in indices(r - 1, b)
               if all(x <= c for x, c in zip(a, caps))]
    coefficients = dict(zip(support, sp.symbols(f"c0:{len(support)}")))
    matrix, form = matrix_for(b, r, L, z, coefficients, caps)
    residual = sp.expand(matrix.det() - L ** (matrix.rows - b) * form)
    assert residual == 0
    symbolic_cases.append({"b": b, "r": r, "caps": caps,
                           "size": matrix.rows, "residual": str(residual)})

integer_cases = []
for b, r, caps in [(4, 3, (4, 1)), (5, 3, (5, 1)),
                   (6, 3, (6, 2)), (5, 4, (5, 1, 2)),
                   (6, 4, (6, 2, 2))]:
    support = [a for a in indices(r - 1, b)
               if all(x <= c for x, c in zip(a, caps))]
    coefficients = {a: (7*j + 3) % 19 - 9 for j, a in enumerate(support)}
    z = tuple((j+1) * (-1 if j % 2 else 1) for j in range(r-1))
    for L in (1, 2):
        matrix, form = matrix_for(b, r, L, z, coefficients, caps)
        determinant = matrix.det(method="domain-ge")
        expected = L ** (matrix.rows - b) * form
        assert determinant == expected
        integer_cases.append({"b": b, "r": r, "caps": caps, "L": L,
                              "size": matrix.rows, "determinant": str(determinant)})

m, b = 256, 32
r = m*m
R = r-2

def count(j):
    return sum((j-k+1) * sum(comb(R,t) * comb(R-t,k-2*t)
                             for t in range(k//2+1)) for k in range(j+1))

u, v = (b-1)//2, b//2
n = count(u) + count(v) - 1
d = n
unbounded = comb(r-1+u,u) + comb(r-1+v,v) - 1
group_size = (r-1+1)//2
Tm_lower, Tb_lower = comb(group_size,m), comb(group_size,b)
tail = b+2*(r-2)
adaptive_threshold = d*b - comb(b,2) - 1
assert m**25 <= n < 2**m-1
assert n < unbounded
assert Tm_lower > n and Tb_lower > n
assert d*(d-1) > n and adaptive_threshold > n
assert tail <= m*d and d >= r+b-2
assert r > 51 and b > 25
certificate = {
    "finding": "O-014.a/b",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "symbolic_graph_identities": symbolic_cases,
    "integer_graph_identities": integer_cases,
    "strict_example": {
        "m": m, "r": r, "b": b, "u": u, "v": v,
        "N_u": str(count(u)), "N_v": str(count(v)), "n_equals_d": str(n),
        "unbounded_B": str(unbounded), "unbounded_B_minus_n": str(unbounded-n),
        "m_to_25": str(m**25), "Grenet_size": str(2**m-1),
        "T_m_lower": str(Tm_lower), "T_b_lower": str(Tb_lower),
        "quadratic_Chow_threshold": str(d*(d-1)),
        "adaptive_Chow_threshold": str(adaptive_threshold),
        "tail": tail, "positive_permanent_polynomial_degree": r+b-2,
        "four_copy_seed_and_multiplier_degree": r+b-8,
        "all_claimed_comparisons": "PASS",
        "scope": "The integer checks certify only the listed size comparisons; positivity and full-copy assertions use the saved proofs."
    },
    "status": "PASS"
}
destination = Path(__file__).with_name("boxed_degree_split_certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(json.dumps({"status": "PASS", "symbolic_identities": len(symbolic_cases),
                  "integer_identities": len(integer_cases), "strict_example": "PASS",
                  "certificate": str(destination)}))
