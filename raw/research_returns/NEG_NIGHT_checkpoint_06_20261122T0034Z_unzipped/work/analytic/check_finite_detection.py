"""Certified constants and exact tangent example for NN-A014 / NN-A004.

Uses FLINT/Arb ball arithmetic for xi and exact SymPy algebra for the polynomial.
No numerical estimate of the Newman constant or unproved simplicity is used.
"""
import json
from pathlib import Path
from flint import acb, acb_series, arb, ctx
import sympy as sp

ctx.dps = 70
s = acb_series([0, 1], 4)
# This expression removes the apparent gamma pole at s=0 exactly.
xi = (s - 1) * (-s * arb.pi().log() / 2).exp() * (1 + s / 2).gamma() * s.zeta()
h = acb('0.5')
xi_half = (h - 1) * (-h * arb.pi().log() / 2).exp() * (1 + h / 2).gamma() * h.zeta()
C = 1 / (2 * xi_half)
A = 2 * xi[2] / (4 * xi_half)
assert C.real > 1 and C.real < 2
assert A.real > 0 and A.real < 1
assert C.imag.contains(0) and A.imag.contains(0)

z = sp.symbols('z')
rho = sp.Rational(1, 2) + sp.I
x = z - sp.Rational(1, 2)
L = (x**2 + 1) * (1 + sp.Rational(2, 3) * x**2)
L1 = L.subs(z, z + 1)
L2 = L.subs(z, z + 2)
v = sp.simplify((z * L1 / sp.diff(L, z)).subs(z, rho))
a = sp.simplify((-(sp.diff(L, z, 2) * v**2
    - 2 * (L1 + z * sp.diff(L1, z)) * v + z * (z + 1) * L2)
    / sp.diff(L, z)).subs(z, rho))
assert v == 25 * sp.I / 4
assert a == -208 + 4979 * sp.I / 16

out = {
    'arithmetic': 'FLINT/Arb complex balls, 70 decimal digits; SymPy exact rationals',
    'xi_half': str(xi_half), 'xi_second_at_zero': str(2 * xi[2]),
    'C': str(C), 'A': str(A),
    'certified_1_lt_C_lt_2': True, 'certified_0_lt_A_lt_1': True,
    'tangent_polynomial_velocity': str(v),
    'tangent_polynomial_acceleration': str(a),
    'kappa': '1/40000',
    'epsilon_R_lower_bound': '40000^(-floor((R+1)^2/4)) / (2^(R+1) * floor((R+1)^2/4)!^2 * (R+1)! * (R+1))'
}
dest = Path(__file__).with_name('finite_detection_certificate.json')
dest.write_text(json.dumps(out, indent=2) + '\n')
print(dest)
