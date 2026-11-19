#!/usr/bin/env python3
"""Exact certificate for the consulted-preprint counterexample G.2.2.

Input: the rational Eisenstein q-coefficients through q^6 and formal
values A=E4(i) nonzero, B=E6(i)=0, C=E2(i).  The proof of B=0 and
A!=0 is in G.2.2.  These finite checks verify the displayed rational
identities, not transcendence of any numerical value.
"""
from time import perf_counter
import sympy as s

started = perf_counter()
q = s.symbols('q')
N = 7
sigma = lambda n, k: sum(d**k for d in range(1, n + 1) if n % d == 0)
E2 = 1 - 24*sum(sigma(n, 1)*q**n for n in range(1, N))
E4 = 1 + 240*sum(sigma(n, 3)*q**n for n in range(1, N))
E6 = 1 - 504*sum(sigma(n, 5)*q**n for n in range(1, N))
F = s.series(E4 + E2*E6/E4, q, 0, N).removeO()
assert F.coeff(q, 0) == 2 and F.coeff(q, 1) == -528
print('Exact rational q expansion through q^6:', F)
print('Weights: E4=4; E2=2; E6/E4=2; depth=1.')
A, B, C, D = s.symbols('A B C D', nonzero=True)
F_value = A + C*B/A
j_value = 1728*A**3/(A**3-B**2)
assert F_value.subs(B, 0) == A
assert j_value.subs(B, 0) == 1728
assert s.simplify((A**3-B**2).subs(B, 0)) == A**3
print('At B=0: F=A, j=1728, discriminant denominator=A^3.')
print('All values lie in Qbar(q_i,A); the two-generator upper bound is proved in text.')
print('Positive-depth coefficient B/A specializes to zero.')
print('All exact checks passed.')
print('Runtime_seconds=', format(perf_counter()-started, '.6f'))
