#!/usr/bin/env python3
"""Exact finite checks for B-RD24's bounded elliptic test.

These computations verify division-polynomial constants/resultants and the
stated integer bounds. They do not run the very large quantifier-elimination
formula at (p,e,n)=(3,216,3), and do not assert an answer to that wild gate.
"""
from functools import lru_cache
from fractions import Fraction
import json
import time
import sympy as sp

started = time.perf_counter()
x = sp.Symbol("x")

def division_polynomials(A, B):
    f = sp.Poly(x**3+A*x+B, x, domain=sp.ZZ)
    p2four = 16*f*f
    initial = {
        0: sp.Poly(0,x,domain=sp.ZZ),
        1: sp.Poly(1,x,domain=sp.ZZ),
        2: sp.Poly(1,x,domain=sp.ZZ),
        3: sp.Poly(3*x**4+6*A*x*x+12*B*x-A*A,x,domain=sp.ZZ),
        4: sp.Poly(2*(x**6+5*A*x**4+20*B*x**3-5*A*A*x*x
                      -4*A*B*x-8*B*B-A**3),x,domain=sp.ZZ),
    }
    @lru_cache(None)
    def P(n):
        if n in initial:
            return initial[n]
        if n % 2:
            r = (n-1)//2
            u, v = P(r+2)*P(r)**3, P(r-1)*P(r+1)**3
            return u-p2four*v if r%2 else p2four*u-v
        r=n//2
        return P(r)*(P(r+2)*P(r-1)**2-P(r-2)*P(r+1)**2)
    return P, f

records = []
for A,B,levels in [(-1,0,(3,5,7,9,27)),(1,1,(3,5,7,9))]:
    P,f = division_polynomials(A,B)
    delta = -16*(4*A**3+27*B*B)
    for m in levels:
        n=(m*m-1)//2
        polynomial=P(m)
        assert polynomial.degree()==n and polynomial.LC()==m
        disc=int(polynomial.discriminant())
        constant=Fraction(disc,delta**(n*(n-1)//6))
        expected=(-1)**((m-1)//2)*m**(n-1)
        assert constant==expected
        resultant=int(sp.resultant(polynomial,4*f,x))
        assert resultant==(-1)**((m-1)//2)*delta**(n//2)
        records.append({"A":A,"B":B,"m":m,"degree":n,
                        "discriminant_constant_matches":True,
                        "two_torsion_resultant_matches":True})

bound_checks=0
for p in (3,5,7,11,13):
    for e in range(1,101):
        d0=6*e+11 if p==3 else 11
        d=d0+1
        v48=e if p==3 else 0
        v864=3*e if p==3 else 0
        assert Fraction(d,3)-v48>=4
        assert Fraction(d,2)-v864>=6
        for n in range(1,5):
            m=p**n; N=(m*m-1)//2; a=n*e
            tm=n*(N-1)  # closed value checked above only for listed m
            DF=a*(N-1)*(N-2)+e*tm+N*(N-1)//6*d0
            D=2*DF+a*(4*N+3)+N*d0+1
            DA=2*DF+a*(4*N-3)+(N//2)*d0
            assert 0<=DF<D and 0<=DA<D
            H=max(2*D+1,3*e+7,d0+1)
            q=(H+e-1)//e
            assert e*q>=H>3*e+6 and H>2*D
            bound_checks+=1

# The first unresolved arithmetic pair: bounds only, not a decision output.
p,e,n=3,216,3
m=p**n; N=(m*m-1)//2; a=n*e; d0=6*e+11
tm=n*(N-1)
DF=a*(N-1)**2+N*(N-1)//6*d0
D=2*DF+a*(4*N+3)+N*d0+1
H=max(2*D+1,3*e+7,d0+1); q=(H+e-1)//e
result={
    "all_assertions_passed":True,
    "scope":"Exact polynomial identities and explicit bounds only; no quantifier-elimination decision at the first wild gap.",
    "polynomial_cases":records,
    "integer_bound_cases":bound_checks,
    "first_wild_gap_precision":{
        "p":p,"e":e,"n":n,"division_degree":N,"minimal_delta_bound":d0,
        "F_discriminant_bound":DF,"jacobian_bound":D,
        "pi_precision":H,"Witt_length":q,
        "decision_evaluated":False
    },
    "elapsed_seconds":time.perf_counter()-started
}
print(json.dumps(result,indent=2))
