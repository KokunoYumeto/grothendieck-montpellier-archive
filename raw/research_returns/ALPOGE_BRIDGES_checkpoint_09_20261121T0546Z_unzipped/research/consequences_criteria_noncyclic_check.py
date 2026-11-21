"""Exact finite checks accompanying CC-AG14.

This script checks displayed polynomial identities and finite enumerations.
The proof of the infinite-lift exclusion and the local Schur indices is in
consequences_criteria_noncyclic_descent.tex; it is not replaced by this script.
"""
import sympy as sp

t, z, s = sp.symbols("t z s")
gamma = 12 - 4 * s
gammabar = 12 + 4 * s


def reduce_quadratic(poly):
    return sp.rem(sp.Poly(sp.expand(poly), s), sp.Poly(s**2 + 23, s)).as_expr()


assert reduce_quadratic(gamma * gammabar) == 512
assert sp.expand(gamma + gammabar) == 24
assert reduce_quadratic(gamma**3 + gammabar**3) == -23040

p0 = t**6 - 24*t**3 + 512
p1 = t**12 + 24*t**9 + 64*t**6 + 12288*t**3 + 262144
assert reduce_quadratic((t**3-gamma)*(t**3-gammabar)) == p0
assert reduce_quadratic(
    (t**6+gamma*t**3+gamma**2) *
    (t**6+gammabar*t**3+gammabar**2)
) == p1
assert sp.expand(p0*p1) == t**18 + 23040*t**9 + 134217728

# The proof bounds n by 2^2 * 3^2 * 7 = 252 before this finite enumeration.
possible_orders = [n for n in range(1, 253) if 6 % sp.totient(n) == 0]
assert possible_orders == [1, 2, 3, 4, 6, 7, 9, 14, 18]

# The quadratic period in Q(zeta_7) has discriminant -7.
period = z + z**2 + z**4
phi7 = sp.Poly(sp.cyclotomic_poly(7, z), z)
assert sp.rem(sp.Poly(period**2 + period + 2, z), phi7).is_zero

phi9 = t**6 + t**3 + 1
assert sp.cyclotomic_poly(9, t) == phi9
assert [pow(2, n, 9) for n in range(1, 7)] == [2, 4, 8, 7, 5, 1]
assert sp.Poly(phi9, t, modulus=2).is_irreducible

# These exact factorization checks supplement, rather than supply, the written
# degree arguments proving that the two rational polynomials are irreducible.
assert sp.Poly(p0, t, domain=sp.QQ).is_irreducible
assert sp.Poly(p1, t, domain=sp.QQ).is_irreducible

print("PASS: quadratic norms; P0/P1 norm expansions; finite-target factorization;")
print("      all cyclotomic orders with phi(n)|6; quadratic period for zeta7;")
print("      order of 2 modulo 9; Phi9 over F2; exact rational irreducibility.")
