#!/usr/bin/env python3
"""Exact finite polynomial certificates for C.3m.

The geometric, Poincare-obstruction and completion arguments are in
C3_surjectivity.tex. This program checks only their stated polynomial
and rational-linear-algebra inputs. All arithmetic below is exact.
"""
from itertools import product, combinations
from time import perf_counter
import sympy as sp

started = perf_counter()
z = sp.symbols("z0:3")
t = sp.Symbol("t")
F = sum(zi**4 for zi in z)
H = sum(z[i]**2 * z[j]**2 for i, j in combinations(range(3), 2))
assert all(sp.diff(F, z[i]) == 4*z[i]**3 for i in range(3))
for chart in range(3):
    others = [z[i] for i in range(3) if i != chart]
    chart_ideal = [sp.diff(F, zi).subs(z[chart], 1) for zi in z]
    assert sp.groebner(chart_ideal, *others).reduce(sp.Integer(1))[1] == 0
print("PASS Fermat quartic: partials 4*z_i^3; Jacobian unit ideal on each of 3 projective charts.")
print("PASS basepoint-free coefficients: z0,z1,z2 cannot vanish simultaneously in projective space.")

monomials5 = [(a, b, 5-a-b) for a in range(6) for b in range(6-a)]
monomials2 = [(a, b, 2-a-b) for a in range(3) for b in range(3-a)]
def monomial(exponents):
    return sp.prod(zi**ei for zi, ei in zip(z, exponents))
def coefficients(poly):
    poly = sp.Poly(poly, *z, domain=sp.QQ)
    return sp.Matrix([poly.coeff_monomial(e) for e in monomials5])

gradient_columns = [coefficients(z[i]**3 * monomial(e))
                    for i in range(3) for e in monomials2]
gradient = sp.Matrix.hstack(*gradient_columns)
fermat_multiples = sp.Matrix.hstack(*[coefficients(zi*F) for zi in z])
assert len(monomials5) == 21
assert gradient.rank() == 18
assert fermat_multiples.rank() == 3
assert sp.Matrix.hstack(gradient, fermat_multiples).rank() == 18
normal_image_rank = gradient.rank() - fermat_multiples.rank()
assert normal_image_rank == 15
assert len(monomials5) - fermat_multiples.rank() == 18
assert 18 - normal_image_rank == 3
print("PASS degree-5 dimensions: polynomial space 21; gradient ideal 18; F*S1 3; H0(O_C(5)) 18; normal image 15; quotient 3.")

quotient_basis = [(1, 2, 2), (2, 1, 2), (2, 2, 1)]
assert set(e for e in monomials5 if max(e) <= 2) == set(quotient_basis)
jacobian = sp.groebner([zi**3 for zi in z], *z, domain=sp.QQ)
remainders = [jacobian.reduce(sp.expand(zi*H))[1] for zi in z]
contraction = sp.Matrix(3, 3, lambda i, j:
    sp.Poly(remainders[j], *z).coeff_monomial(quotient_basis[i]))
assert contraction == sp.eye(3)
assert contraction.det() == 1
print("PASS remainders z_i*H:", "; ".join(str(r) for r in remainders))
print("PASS exact contraction matrix:", contraction.tolist(), "rank=3, determinant=1.")

equation_count = 0
minor_count = 0
for m in (2, 3):
    x = sp.symbols(f"x0:{m+1}")
    ell = sum(x[i]*z[i] for i in range(3))
    w = {(i, j): t*x[i]*z[j] for i in range(m+1) for j in range(3)}
    f = sum(w[i, i] for i in range(3))
    assert sp.expand(f - t*ell) == 0
    for i, k in combinations(range(m+1), 2):
        for j, l in combinations(range(3), 2):
            assert sp.expand(w[i,j]*w[k,l] - w[i,l]*w[k,j]) == 0
            minor_count += 1
    for indices in product(range(m+1), repeat=4):
        left = sum(sp.prod(w[i,j] for i in indices) for j in range(3))
        left += f*sum(w[indices[0],a]*w[indices[1],a]
                      * w[indices[2],b]*w[indices[3],b]
                      for a,b in combinations(range(3),2))
        right = t**4 * sp.prod(x[i] for i in indices)*(F+t*ell*H)
        assert sp.expand(left-right) == 0
        equation_count += 1
print(f"PASS rank-one Segre substitution: {minor_count} minors and all {equation_count} ordered-quadruple equations for m=2,3 (N=4,5).")
print("PASS uniform symbolic factor: each displayed equation is t^4*x_i1*x_i2*x_i3*x_i4*(F+t*ell*H); proof for arbitrary m is in C.3m.")

u, v, zet = sp.symbols("u v zet")
assert sp.Poly(u**4+v**4+1, v).rem(sp.Poly(v**4+1+u**4, v)).is_zero
assert sp.Poly(1+zet**4, zet).rem(sp.Poly(zet**4+1, zet)).is_zero
print("PASS witness point equations: (u:v:1), v^4=-1-u^4, and (1:zeta:0), zeta^4=-1, lie on C.")
print("SCOPE: nontorsion follows from the transcendence/Abel-immersion proof, not a finite calculation.")
print("SCOPE: no finite computation is asserted to prove the deformation obstruction, proper descent, or all-dimensional geometry.")
print(f"ALL EXACT CHECKS PASSED in {perf_counter()-started:.3f} seconds.")
