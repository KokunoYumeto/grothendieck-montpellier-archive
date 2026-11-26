"""Exact r=5,b=2 certificate for the final algebraic CM interface.

This does not implement the CM construction or its analytic input.
It verifies the characteristic-zero compositum expression, its reduction,
and the full tame equivariance of the resulting order-25 unit at p=43.
All coefficients are derived from Phi_25; no coefficient table is used.
Run from the version root: python3 programs/check_fixed_wild_r5.py
Requires SymPy. Output is the exact JSON certificate on stdout only.
"""
import json
import sympy as sp

x = sp.Symbol("x")
phi25 = sp.Poly(sum(x ** (5 * j) for j in range(5)), x, domain=sp.QQ)


def red(poly):
    return sp.rem(sp.Poly(poly, x, domain=sp.QQ), phi25).as_expr()


def vector(poly):
    poly = sp.Poly(red(poly), x)
    return sp.Matrix([poly.nth(j) for j in range(20)])


tame = [a for a in range(1, 25) if pow(a, 4, 25) == 1]
theta = red(sum(x ** a for a in tame))
tpowers = [red(theta ** i) for i in range(6)]
power_matrix = sp.Matrix.hstack(*(vector(v) for v in tpowers[:5]))
relation = power_matrix.gauss_jordan_solve(-vector(tpowers[5]))[0]
y = sp.Symbol("y")
f = sp.Poly(y ** 5 + sum(relation[i] * y ** i for i in range(5)), y)
assert red(f.as_expr().subs(y, theta)) == 0

# The ordered basis is theta^i * zeta_5^j, with i varying first.
basis = [(i, j) for j in range(4) for i in range(5)]
matrix = sp.Matrix.hstack(*(vector(tpowers[i] * x ** (5 * j)) for i, j in basis))
coefficients = matrix.inv() * vector(x)
assert red(sum(coefficients[k] * tpowers[i] * x ** (5 * j)
               for k, (i, j) in enumerate(basis)) - x) == 0

p = 43
roots = [u for u in range(p) if int(f.eval(u)) % p == 0]
assert len(roots) == 5
u = roots[0]
phi5mod = sp.Poly(1 + x + x ** 2 + x ** 3 + x ** 4, x, modulus=p)


def redp(poly):
    return sp.rem(sp.Poly(poly, x, modulus=p), phi5mod).as_expr()


def mulp(a, b):
    return redp(a * b)


def powerp(a, exponent):
    result = sp.Integer(1)
    while exponent:
        if exponent & 1:
            result = mulp(result, a)
        a = mulp(a, a)
        exponent >>= 1
    return result


U = sp.Integer(0)
for coefficient, (i, j) in zip(coefficients, basis):
    numerator, denominator = map(int, coefficient.as_numer_denom())
    assert denominator % p
    U += (numerator * pow(denominator, -1, p) * pow(u, i, p) % p) * x ** j
U = redp(U)
assert powerp(U, 25) == 1 and powerp(U, 5) != 1
assert redp(powerp(U, 5) - x) == 0
equivariance = []
for c in range(1, 5):
    lift = next(a for a in tame if a % 5 == c)
    sigma_u = redp(U.subs(x, x ** c))
    expected = powerp(U, lift)
    assert redp(sigma_u - expected) == 0
    equivariance.append({"c": c, "teich_lift_mod_25": lift,
                         "coefficients_mod_p": [int(sp.Poly(expected, x).nth(j)) % p
                                                for j in range(4)]})

disc_f = int(sp.discriminant(f.as_expr(), y))
index_square = disc_f // 5 ** 8
index = sp.integer_nthroot(index_square, 2)
assert index[1]
record = {
    "scope": "Exact final algebraic-interface certificate; not a CM implementation",
    "parameters": {"r": 5, "b": 2, "p": p, "ord_r_p": 4,
                   "valuation_r_p_to_d_minus_1": 2},
    "cyclotomic_polynomial_25": str(phi25.as_expr()),
    "tame_subgroup_mod_25": tame,
    "theta_definition": "sum zeta_25^a over the tame subgroup",
    "theta_minimal_polynomial": str(f.as_expr()),
    "discriminant_theta_polynomial": disc_f,
    "wild_field_discriminant": 5 ** 8,
    "power_basis_index": int(index[0]),
    "compositum_basis_order": [list(ij) for ij in basis],
    "zeta_25_coefficients": [str(c) for c in coefficients],
    "roots_theta_polynomial_mod_p": roots,
    "chosen_root": u,
    "U_coefficients_mod_p": [int(sp.Poly(U, x).nth(j)) % p for j in range(4)],
    "excluded_power_basis_prime_7": {
        "distinct_roots": [v for v in range(7) if int(f.eval(v)) % 7 == 0],
        "explanation": "The power-basis index is 7; the theorem handles this fixed exceptional prime separately.",
    },
    "U_power_25": str(powerp(U, 25)),
    "U_power_5": str(powerp(U, 5)),
    "equivariance": equivariance,
    "all_assertions_passed": True,
}
print(json.dumps(record, indent=2))
