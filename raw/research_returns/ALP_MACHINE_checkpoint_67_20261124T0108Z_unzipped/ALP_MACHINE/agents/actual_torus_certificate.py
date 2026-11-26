"""Exact finite algebra checks for ALP-LIFT-09; not a formalized theta proof."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as s

x, z = s.symbols("x z", real=True)
y = s.symbols("y", positive=True)
I, pi = s.I, s.pi
phi7 = sum(x**j for j in range(7))
realpoly = x**3 + x**2 - 2*x - 1
assert s.discriminant(phi7, x) == -(7**5)
assert s.discriminant(realpoly, x) == 49
factors = {
    p: sorted(s.degree(f, x) for f, m in s.factor_list(phi7, modulus=p)[1]
              for _ in range(m))
    for p in (2, 3)
}
assert factors == {2: [3, 3], 3: [6]}
upper_E = Fraction(4, 3)**3 * Fraction(720, 6**6) * 49 * Fraction(8, 3)
assert upper_E == Fraction(31360, 6561) and upper_E < 5
assert Fraction(14, 9) < 2
assert Fraction(2, 3)*Fraction(8, 3) < 2
signature_matrix = s.Matrix([[0, 1, 1], [1, 1, 0], [1, 1, 1]])
assert signature_matrix.det() % 2 == 1
assert pow(2, 3, 7) == 1 and all(pow(2, k, 7) != 1 for k in (1, 2))
assert pow(3, 6, 7) == 1 and all(pow(3, k, 7) != 1 for k in (1, 2, 3))
eps_minus_one = int(s.legendre_symbol(-1, 7))
assert eps_minus_one == -1
assert eps_minus_one * I**2 == 1

# For tau=i*y, apply creation to P(x)*exp(-pi*y*x^2).
# The real-part-of-tau gauge is unitary and does not change these norms.
P = s.Integer(1)
kernel = s.exp(pi*z*z/(2*y) + 2*pi*I*x*z)
checked_degrees = []
for k in range(7):
    derivative = s.diff(kernel, z, k).subs(z, 0)
    assert s.simplify(P-derivative) == 0
    norm_polynomial = s.Poly(s.expand(P*s.conjugate(P)), x)
    relative_norm = 0
    for (degree,), coefficient in norm_polynomial.terms():
        if degree % 2 == 0:
            m = degree//2
            moment = s.factorial2(2*m-1)/(4*pi*y)**m if m else s.Integer(1)
            relative_norm += coefficient*moment
    assert s.simplify(relative_norm-s.factorial(k)*(pi/y)**k) == 0
    checked_degrees.append(k)
    P = s.expand(-I/(2*y)*(s.diff(P, x)-4*pi*y*x*P))

out = {
    "statement": "ALP-LIFT-09",
    "scope": (
        "Exact polynomial, finite-field, rational-bound and Gaussian-moment "
        "checks only; the global splitting, Heisenberg eigenline, torus class "
        "argument and theta integral are proved in actual_torus_first_lift.md."
    ),
    "discriminants": {"E": -(7**5), "F": 49},
    "cyclotomic_factor_degrees": {str(p): [int(d) for d in ds] for p, ds in factors.items()},
    "Minkowski_rational_upper_E": str(upper_E),
    "signature_determinant_mod2": int(signature_matrix.det() % 2),
    "ramified_character_value_on_rational_7": "1",
    "creation_and_norm_degrees_checked_exactly": checked_degrees,
    "Gaussian_relative_norm_formula": "k!*(pi/y)^k",
    "passed": True,
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
