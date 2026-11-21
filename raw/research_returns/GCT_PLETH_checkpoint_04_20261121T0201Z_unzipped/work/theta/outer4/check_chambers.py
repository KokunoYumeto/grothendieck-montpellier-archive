#!/usr/bin/env python3
"""Exact checks of the character identities used in T-033 and T-034.

The tests here compare rational characters, not floating-point evaluations.
Independent plethysm checks are performed separately by rectangular_cases.
"""
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
q = sp.symbols('q')
tags = {
    (4,): (0, 9),
    (1, 1, 1, 1): (3, 6),
    (2, 2): (2, 4, 5, 7),
    (3, 1): (2, 3, 4, 5, 6, 7),
    (2, 1, 1): (1, 3, 4, 5, 6, 8),
}
chars = {
    (4,): (1, 1, 1, 1, 1),
    (1, 1, 1, 1): (1, -1, 1, 1, -1),
    (2, 2): (2, 0, 2, -1, 0),
    (3, 1): (3, 1, -1, 0, -1),
    (2, 1, 1): (3, -1, -1, 0, 1),
}
sizes = (1, 6, 3, 8, 6)
harmonic_traces = (
    (1+q)/(1-q)**2,
    1/(1+q),
    1/(1+q),
    (1+q)/(1+q+q*q),
    (1+q)/(1+q*q),
)
rows = ['statement\tcheck\tinstances\tresult']
for mu in tags:
    molien = sum(s*c*f for s,c,f in zip(sizes, chars[mu], harmonic_traces))/24
    positive = sum(q**e for e in tags[mu])/((1-q**4)*(1-q**6))
    assert sp.cancel(molien-positive) == 0, mu
rows.append('T-033\tHarmonic character rational identities\t5\tPASS')

def band_polynomial(a, b):
    A, s = max(a,b), min(a,b)
    return sum(q**L for K in range(s,-1,-2)
               for L in (range(K,K+A+1) if K else range(A,-1,-2)))

def schur_specialized(a, b):
    return q**(-a-b)*(1-q**(a+1))*(1-q**(b+1))*(1-q**(a+b+2))/((1-q)**2*(1-q*q))

for a in range(25):
    for b in range(25):
        A, s = max(a,b), min(a,b)
        P = band_polynomial(a,b)
        numerator = q-q**(A+2)-q**(s+2)+q**(A+s+3)
        if A % 2 == 0 and s % 2 == 0:
            numerator += (1-q)**2
        assert sp.cancel(P-numerator/((1-q)*(1-q*q))) == 0, (a,b,'band')
        assert sp.cancel(P-q**-1*P.subs(q,1/q)-(1-q**-1)*schur_specialized(a,b)) == 0, (a,b,'character')
        dim = sum(2*L+1 for K in range(s,-1,-2)
                  for L in (range(K,K+A+1) if K else range(A,-1,-2)))
        assert dim == (a+1)*(b+1)*(a+b+2)//2
rows.append('T-033\tElliott rational identity and Weyl dimensions\t625\tPASS')

def coin46(N):
    return sum(1 for y in range(N//6+1) if (N-6*y)%4 == 0) if N >= 0 else 0

for a in range(16):
    for b in range(16):
        A, s = max(a,b), min(a,b)
        for mu, ee in tags.items():
            direct = sum(coin46(L-e) for K in range(s,-1,-2)
                         for L in (range(K,K+A+1) if K else range(A,-1,-2))
                         for e in ee)
            lattice = 0
            for e in ee:
                for j in range((s+1)//2):
                    K = s-2*j
                    for x in range((A+s)//4+1):
                        for y in range((A+s)//6+1):
                            lattice += K <= 4*x+6*y+e <= K+A
                if s % 2 == 0:
                    for j in range(A//2+1):
                        lattice += coin46(A-e-2*j)
            assert direct == lattice, (a,b,mu,direct,lattice)
rows.append('T-034\tTagged lattice-point bijection\t1280\tPASS')
(HERE/'CHAMBER_CHARACTER_CHECK.tsv').write_text('\n'.join(rows)+'\n')
print('\n'.join(rows))
