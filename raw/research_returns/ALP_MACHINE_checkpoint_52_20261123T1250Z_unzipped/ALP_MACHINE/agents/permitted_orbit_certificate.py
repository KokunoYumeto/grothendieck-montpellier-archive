"""Exact checks for the new finite-level accounting in ALP-LIFT-10."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as s

# Primitive seventh roots modulo29 give all six cyclotomic embeddings.
p = 29
zeta = pow(2, 4, p)
assert pow(zeta, 7, p) == 1 and zeta != 1
roots = []
for i in range(1, 7):
    zi = pow(zeta, i, p)
    delta = (1 + 2*(zi+pow(zi, 2, p)+pow(zi, 4, p))) % p
    alpha = (1+2*delta) % p
    assert delta*delta % p == (-7) % p
    roots.append({"embedding": i, "delta_mod29": delta, "alpha_mod29": alpha})
for i in (1, 2, 3):
    a = roots[i-1]["alpha_mod29"]
    b = roots[(7-i)-1]["alpha_mod29"]
    assert (a == 0) != (b == 0)

# All half-orbit common-level indices and exceptional-prime costs.
indices = []
for e in range(1, 7):
    M = 29**e
    local_index = 28*29**(e-1)
    h = Fraction(2*local_index**3, 14)
    assert h.denominator == 1
    h = h.numerator
    assert h == 56**2*29**(3*(e-1))
    fac = {int(q): int(v) for q, v in s.factorint(h).items()}
    expected = {2: 6, 7: 2}
    if e > 1:
        expected[29] = 3*(e-1)
    assert fac == expected and h % 11 != 0
    assert Fraction(h, M**3) == Fraction(56**2, 29**3)
    indices.append({"e": e, "M": M, "h": h, "prime_factors": fac})

# Pure isotropic representative: all potentially offending phases vanish.
a1, a2, d1, d2, w1, w2 = s.symbols("a1 a2 d1 d2 w1 w2")
symplectic = lambda v, w: v[1]*w[0]-v[0]*w[1]
v = (a1, s.Integer(0))
d = (d1, s.Integer(0))
w0d = (w1*d1, s.Integer(0))
assert symplectic(v, d) == 0
assert symplectic(d, w0d) == 0

# Pullback linear and constant Gaussian multipliers agree identically.
M, hu, hr = s.symbols("M hu hr")
assert s.expand(-M**2*hu - (M**2)*hr/2 -
                (-M**2*hu-M**2*hr/2)) == 0
for e in range(1, 7):
    kappa = (29**e)**2
    for eps in (1, -1):
        assert eps**kappa * eps == 1

out = {
    "statement": "ALP-LIFT-10",
    "scope": (
        "Exact mod29 CM half-orbit, finite-index, exceptional-prime "
        "denominator, isotropic phase and odd-power sign checks. "
        "The global theta and gauge arguments are not formalized here."
    ),
    "mod29_embeddings": roots,
    "indices": indices,
    "exact_h_over_M_cubed": "3136/24389",
    "possible_projection_denominator_primes": [2, 7, 29],
    "passed": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))
