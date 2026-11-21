#!/usr/bin/env python3
"""Exact matrix identities used in host_sign_results.tex.

This is a finite algebra check, not a verification of deformation-theoretic
representability, local duality, or the global automorphic inputs.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

s = S.symbols("s")
a, b, c, d, aa, bb, cc, dd = S.symbols("a b c d aa bb cc dd")
t, z, v, c0, c1, c2, ell, y = S.symbols("t z v c0 c1 c2 ell y")
modulus = S.Poly(2*s*s + 1, s)


def reduced(x):
    num, den = S.fraction(S.cancel(x))
    assert S.rem(S.Poly(den, s), modulus).as_expr() != 0
    return (S.rem(S.Poly(num, s), modulus).as_expr(), den)


def zero(x):
    return reduced(x)[0] == 0


def matrix_equal(x, y):
    return all(zero(u-v) for u, v in zip(x, y))


def adj(g):
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    delta = a*d-b*c
    return S.Matrix([
        [a*a, -2*s*a*b, -b*b],
        [2*s*a*c, a*d+b*c, -2*s*b*d],
        [-c*c, 2*s*c*d, d*d],
    ])/delta


J = S.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
K = S.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
D = S.diag(-1, 1, -1)
g = S.Matrix([[a, b], [c, d]])
h = S.Matrix([[aa, bb], [cc, dd]])
Ag, Ah = adj(g), adj(h)
checks = {}
checks["adjoint_homomorphism"] = matrix_equal(adj(g*h), Ag*Ah)
checks["perfect_preserved_form"] = matrix_equal(Ag.T*K*Ag, K)
checks["theta_equals_D_conjugation"] = matrix_equal(J*adj(g.inv()).T*J, D*Ag*D)
checks["complex_conjugation_matrix"] = matrix_equal(adj(S.diag(1, -1)), D)
checks["JK_equals_minus_D"] = J*K == -D
checks["lower_adjoint_root_is_plus_line"] = matrix_equal(
    adj(S.Matrix([[1, 0], [t, 1]])).diff(t).subs(t, 0),
    S.Matrix([[0, 0, 0], [2*s, 0, 0], [0, 2*s, 0]])
)
minus = S.Matrix([[0, 0, 0], [1, 0, 0], [0, -1, 0]])
plus = S.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
tor = S.diag(z, 1, 1/z)
checks["minus_line_c_even"] = -J*minus.T*J == minus
checks["plus_line_c_odd"] = -J*plus.T*J == -plus
checks["both_lines_weight_minus_one"] = (
    matrix_equal(tor*minus*tor.inv(), minus/z)
    and matrix_equal(tor*plus*tor.inv(), plus/z)
)
for j in (0, 1):
    for k in (0, 1):
        rg, rh = Ag*D**j, Ah*D**k
        theta_rh = D*Ah*D*D**k
        product = rg*(rh if j == 0 else theta_rh)
        checks[f"GG_homomorphism_eta_{j}_{k}"] = matrix_equal(product, adj(g*h)*D**((j+k) % 2))
for j in (0, 1):
    eta = (-1)**j
    checks[f"exact_residual_r0_eta_{j}"] = matrix_equal(
        adj(S.diag(1, eta/z))*D**j, tor
    )
checks["saturator_factorization"] = zero(
    ell*(c0*c1*(y-v))*(c1*c2*(1-v/y))
    -ell*c0*c1*c1*c2*(y-v)**2/y
)
assert all(checks.values()), checks
result = {
    "coefficient_relation": "2*s^2+1=0; all identities in the rational function field with this relation",
    "checks": checks,
    "all_pass": True,
    "scope": "Exact matrix and scalar algebra only; no claimed proof of the deformation-theoretic or automorphic inputs.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
