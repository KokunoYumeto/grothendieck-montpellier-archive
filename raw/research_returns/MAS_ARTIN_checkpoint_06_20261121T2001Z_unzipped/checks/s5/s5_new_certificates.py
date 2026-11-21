"""Exact finite algebra checks for MA-S5-002--005.

This verifies stated character, Euler-polynomial and central-order identities.
It does not produce an arithmetic S5 extension or formally verify an analytic proof.
"""
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
cone = json.loads((HERE / "s5_hecke_cone.json").read_text())
names = cone["character_names"]
cycles = ["(1, 1, 1, 1, 1)", "(2, 1, 1, 1)", "(2, 2, 1)",
          "(3, 1, 1)", "(3, 2)", "(4, 1)", "(5,)"]
sizes = [1, 10, 15, 20, 20, 30, 24]
table = sp.Matrix([cone["character_table"][c] for c in cycles])
gram = table.T * sp.diag(*sizes) * table
assert gram == 120 * sp.eye(7)

end_xi = sp.Matrix([16, 0, 0, 1, 3, 0, 1])
end_xi_coefficients = table.T * sp.diag(*sizes) * end_xi / 120
assert list(end_xi_coefficients) == [1, 0, 0, 1, 1, 0, 1]
assert table * end_xi_coefficients == end_xi

w = table[:, 4]
w_square = w.applyfunc(lambda x: x*x)
w_square_coefficients = table.T * sp.diag(*sizes) * w_square / 120
assert list(w_square_coefficients) == [1, 0, 1, 1, 1, 1, 1]
assert table * w_square_coefficients == w_square

T = sp.Symbol("T")
i = sp.I
pi4 = [1, i, 1, i]
xi4 = [1, i, -1, -i]
pi5 = [1, 1, 1, i, -i]
w5 = [1, -1, -1, i, -i]

def poly(eigenvalues):
    return sp.Poly(sp.expand(sp.prod(1 - a*T for a in eigenvalues)), T)

def end_poly(eigenvalues):
    return poly([sp.simplify(a/b) for a in eigenvalues for b in eigenvalues])

P_pi4, P_xi4 = end_poly(pi4), end_poly(xi4)
P_pi5, P_w5 = end_poly(pi5), end_poly(w5)
ratio4 = sp.factor(P_xi4.as_expr() / P_pi4.as_expr())
ratio5 = sp.factor(P_w5.as_expr() / P_pi5.as_expr())
expected = ((1+T)/(1-T))**4
assert sp.cancel(ratio4 - expected) == 0
assert sp.cancel(ratio5 - expected) == 0
assert poly(pi5).as_expr() == sp.expand((1+T*T)*(1-T)**3)
assert poly(w5).as_expr() == sp.expand((1+T*T)*(1-T)*(1+T)**2)

# For the displayed exceptional projective lifts the similitude is nu=i.
# Its inverse twist is applied after the symmetric/exterior square.
def symmetric_square(eigenvalues, nu):
    return [sp.simplify(a*b/nu) for u, a in enumerate(eigenvalues)
            for b in eigenvalues[u:]]

def exterior_square(eigenvalues, nu):
    return [sp.simplify(a*b/nu) for u, a in enumerate(eigenvalues)
            for b in eigenvalues[u+1:]]

assert poly(exterior_square(pi4, i)) == poly([1]+pi5)
assert poly(exterior_square(xi4, i)) == poly([1]+w5)
P_sym_pi4 = poly(symmetric_square(pi4, i))
P_sym_xi4 = poly(symmetric_square(xi4, i))
ratio_sym4 = sp.factor(P_sym_xi4.as_expr()/P_sym_pi4.as_expr())
assert sp.cancel(ratio_sym4-((1+T)/(1-T))**2) == 0
sym_xi_coefficients = end_xi_coefficients-sp.Matrix([1,0,0,0,1,0,0])
assert list(sym_xi_coefficients) == [0,0,0,1,0,0,1]

power_checks = []
for j in range(1, 9):
    trace_end_pi4 = sp.simplify(sum((a/b)**j for a in pi4 for b in pi4))
    trace_end_xi4 = sp.simplify(sum((a/b)**j for a in xi4 for b in xi4))
    trace_end_pi5 = sp.simplify(sum((a/b)**j for a in pi5 for b in pi5))
    trace_end_w5 = sp.simplify(sum((a/b)**j for a in w5 for b in w5))
    difference4 = int(trace_end_pi4 - trace_end_xi4)
    difference5 = int(trace_end_pi5 - trace_end_w5)
    assert difference4 == difference5 == (8 if j % 2 else 0)
    power_checks.append([j, difference4, difference5])

# Orders in (1, sign, V, V*sign, W, W*sign, X) coordinates.
orders = [0, 0, 0, 2, 2, 0, 0]
monomial_values = [sum(a*b for a, b in zip(row["coefficients"], orders))
                   for row in cone["induced_linear_patterns"]]
assert len(monomial_values) == 43
assert min(monomial_values) >= 0
a, b, c, d, x, y, e = orders
n, n_eta, beta, f = 0, 2, 2, 0
k = beta-b-n
r4 = n+d+e-k
r5 = r4+c+f
q = d+e-k
assert k == 2 == x-n == n_eta-f
assert r4 == 0 == r5
assert q == 0 == r4-n
assert beta == b+x
assert f == a+y
assert all(v % 2 == 0 for v in orders+[n,n_eta,beta,f,k,r4,r5])

out = {
    "scope": "Exact finite algebra only; no arithmetic extension or formal analytic verification",
    "model": "GPT-6 Astra Pro; inherited effort not externally exposed",
    "date_utc": "2026-11-21",
    "character_names": names,
    "class_order": cycles,
    "character_orthogonality": "Gram matrix = 120 I_7",
    "End_xi_coefficients": [int(z) for z in end_xi_coefficients],
    "W_tensor_W_coefficients": [int(z) for z in w_square_coefficients],
    "Sym2_xi_twisted_coefficients": [int(z) for z in sym_xi_coefficients],
    "rank4_end_polynomials": {
        "P_Pi": str(sp.factor(P_pi4.as_expr())),
        "P_xi": str(sp.factor(P_xi4.as_expr())),
        "L_Pi_over_L_xi": str(ratio4),
    },
    "rank5_end_polynomials": {
        "P_varpi": str(sp.factor(P_pi5.as_expr())),
        "P_W": str(sp.factor(P_w5.as_expr())),
        "L_varpi_over_L_W": str(ratio5),
    },
    "power_trace_differences_j_1_through_8": power_checks,
    "symmetric_square_local_ratio": str(ratio_sym4),
    "central_order_witness": {
        "orders": orders, "n": n, "n_eta": n_eta, "beta": beta,
        "f": f, "k": k, "r4": r4, "r5": r5, "q": q,
        "43_monomial_values": monomial_values,
    },
    "all_assertions_passed": True,
}
(HERE / "s5_new_certificates.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"character_identities": 3, "Euler_ratio_identities": 3,
                  "power_trace_checks": len(power_checks)*2,
                  "central_monomial_checks": len(monomial_values),
                  "all_assertions_passed": True}))
