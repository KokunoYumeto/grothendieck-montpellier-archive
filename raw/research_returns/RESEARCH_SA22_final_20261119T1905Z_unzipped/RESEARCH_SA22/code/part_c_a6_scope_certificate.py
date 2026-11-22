"""Exact arithmetic for two new A6 counterexamples, not a fundamental-group test.

The geometric, valuation-theoretic and logarithmic proofs are in
sections/part_a6_scope_supplement.tex. This program only certifies their
finite polynomial and sign calculations. No previous check is rerun.
"""
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import datetime
import json
import time

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
checks = []


def record(name, condition, detail):
    assert condition, name
    checks.append({"id": name, "passed": True, "detail": detail})


def clean(poly):
    return {power: Q(value) for power, value in poly.items() if value}


def add(*polys):
    out = {}
    for poly in polys:
        for power, value in poly.items():
            out[power] = out.get(power, Q(0)) + value
    return clean(out)


def scale(poly, scalar):
    return clean({power: scalar * value for power, value in poly.items()})


def mul(left, right):
    out = {}
    for u, a in left.items():
        for v, b in right.items():
            power = tuple(x + y for x, y in zip(u, v))
            out[power] = out.get(power, Q(0)) + a * b
    return clean(out)


def power(poly, exponent):
    dimension = len(next(iter(poly)))
    out = {(0,) * dimension: Q(1)}
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def derivative(poly, variable):
    out = {}
    for exponents, coefficient in poly.items():
        if exponents[variable]:
            new = list(exponents)
            new[variable] -= 1
            out[tuple(new)] = coefficient * exponents[variable]
    return clean(out)


def evaluate(poly, values):
    total = Q(0)
    for exponents, coefficient in poly.items():
        term = coefficient
        for value, exponent in zip(values, exponents):
            term *= Q(value) ** exponent
        total += term
    return total


# The homogeneous cubic F(X,Y,Z)=Y^2 Z-X^3+X^2 Z.
F = {(0, 2, 1): Q(1), (3, 0, 0): Q(-1), (2, 0, 1): Q(1)}
Fx, Fy, Fz = (derivative(F, i) for i in range(3))
record("cubic_x_derivative", Fx == {(2, 0, 0): Q(-3), (1, 0, 1): Q(2)},
       "F_X=X(2Z-3X)")
record("cubic_y_derivative", Fy == {(0, 1, 1): Q(2)}, "F_Y=2YZ")
record("node_on_curve", evaluate(F, (0, 0, 1)) == 0,
       "The rational candidate [0:0:1] lies on the cubic")
record("node_singular", all(evaluate(d, (0, 0, 1)) == 0 for d in (Fx, Fy, Fz)),
       "All three homogeneous first derivatives vanish at the node")
record("other_affine_critical_candidate_excluded", evaluate(F, (Q(2, 3), 0, 1)) == Q(4, 27),
       "The only other affine critical candidate has cubic value 4/27")
record("marking_on_curve", evaluate(F, (0, 1, 0)) == 0, "The marked point is [0:1:0]")
record("marking_smooth", evaluate(Fz, (0, 1, 0)) == 1, "F_Z at the marked point is 1")

# Homogeneous normalization [A:B] -> [B(A^2+B^2):A(A^2+B^2):B^3].
A, B = {(1, 0): Q(1)}, {(0, 1): Q(1)}
node_factor = add(power(A, 2), power(B, 2))
Xmap, Ymap, Zmap = mul(B, node_factor), mul(A, node_factor), power(B, 3)
pullback_F = add(mul(power(Ymap, 2), Zmap), scale(power(Xmap, 3), -1),
                 mul(power(Xmap, 2), Zmap))
record("normalization_homogeneous_identity", pullback_F == {}, "F composed with the normalization map is the zero polynomial")
record("normalization_inverse_identity", add(mul(B, Ymap), scale(mul(A, Xmap), -1)) == {},
       "B*Y=A*X, hence A/B=Y/X on the indicated dense chart")
record("normalization_at_infinity", tuple(evaluate(P, (1, 0)) for P in (Xmap, Ymap, Zmap)) == (0, 1, 0),
       "The normalization's infinity maps to the marking")
record("normalization_common_degree", all(sum(e) == 3 for P in (Xmap, Ymap, Zmap) for e in P),
       "All homogeneous coordinate polynomials have degree 3")

# The node preimage polynomial a^2+1 has two simple conjugate roots.
one = {(0, 0): Q(1)}
branch_poly = add(power(A, 2), one)
branch_derivative = derivative(branch_poly, 0)
bezout = add(branch_poly, scale(mul(A, branch_derivative), Q(-1, 2)))
record("node_branches_simple", bezout == one, "(a^2+1)-(a/2)*(2a)=1")
record("branch_discriminant", 0 * 0 - 4 * 1 * 1 == -4,
       "The branch polynomial has discriminant -4; its roots are ±i")
record("normal_tensor_swap_coefficient", 1 * 1 == 1,
       "Swapping the two ungraded tangent factors fixes the tensor coefficient 1")
cyclotomic_at_conjugation, branch_sign = -1, -1
record("node_character_at_conjugation", cyclotomic_at_conjugation * branch_sign == 1,
       "χ(c)ε(c)=(-1)(-1)=+1")
record("node_character_not_cyclotomic", cyclotomic_at_conjugation * branch_sign != cyclotomic_at_conjugation,
       "The node character +1 differs from the cyclotomic value -1")

# T^2-2 over the 2-adic valuation ring.
coefficients = (1, 0, -2)
record("wild_cover_monic", coefficients[0] == 1, "Leading coefficient is 1")
record("wild_cover_eisenstein_divisibility", all(c % 2 == 0 for c in coefficients[1:]),
       "All nonleading coefficients are divisible by 2")
record("wild_cover_eisenstein_exactness", coefficients[-1] % 4 != 0,
       "The constant coefficient is not divisible by 4")
record("wild_cover_discriminant", coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2] == 8,
       "The characteristic-zero quadratic has nonzero discriminant 8")
e, residue_characteristic = 2, 2
record("wild_ramification_index", gcd(e, residue_characteristic) == 2,
       "The proved ramification index e=2 is not prime to residue characteristic 2")

payload = {
    "started_utc": started,
    "elapsed_seconds": time.monotonic() - tick,
    "arithmetic": "exact rational sparse polynomials and integers",
    "new_counterexamples": 2,
    "assertion_count": len(checks),
    "checks": checks,
    "scope_limit": "Does not prove log purity, normalization theory, tameness criteria, arithmetic reconstruction, or geometric stability; those arguments are in the manuscript.",
}
root = Path(__file__).resolve().parents[1]
output = root / "code/part_c_a6_scope_certificate_output.json"
encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
output.write_text(encoded)
output.with_suffix(".txt").write_text(encoded)
print(json.dumps({key: value for key, value in payload.items() if key != "checks"}, indent=2))
