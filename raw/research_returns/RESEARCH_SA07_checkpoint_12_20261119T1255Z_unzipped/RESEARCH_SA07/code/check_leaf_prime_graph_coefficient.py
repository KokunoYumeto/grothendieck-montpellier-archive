#!/usr/bin/env python3
"""Exact finite certificates for the degree-p formal graph coefficient lemma."""
from time import perf_counter
import sympy as sp

started=perf_counter()
t=sp.Symbol('t')
def multiply(f,g,p):
    return [sp.expand(sum(f[i]*g[n-i] for i in range(n+1))) for n in range(p+1)]
def compose(f,g,p):
    result=[sp.S(0)]*(p+1);power=[sp.S(1)]+[sp.S(0)]*p
    for coefficient in f:
        result=[sp.expand(a+coefficient*b) for a,b in zip(result,power)]
        power=multiply(power,g,p)
    return result
for p in (5,7):
    xs=sp.symbols('x2:'+str(p+1));ys=sp.symbols('y2:'+str(p+1))
    X=[sp.S(0),sp.S(1)]+list(xs[:-1])+[xs[-1]/p]
    Y=[sp.S(0),sp.S(0)]+list(ys[:-1])+[ys[-1]/p]
    g=[sp.S(0),sp.S(1)]+[sp.S(0)]*(p-1)
    for n in range(2,p+1):
        defect=compose(X,g,p)[n]
        g[n]=sp.expand(g[n]-defect)
    assert compose(X,g,p)==[sp.S(0),sp.S(1)]+[sp.S(0)]*(p-1)
    bp=compose(Y,g,p)[p]
    remainder=sp.expand(bp-ys[-1]/p)
    assert xs[-1] not in remainder.free_symbols and ys[-1] not in remainder.free_symbols
    polynomial=sp.Poly(remainder,*xs[:-1],*ys[:-1],domain=sp.ZZ)
    print('PRIME',p,'COEFFICIENT_b_p=y_p/p+INTEGER_POLYNOMIAL','TERMS',len(polynomial.terms()))
    print('INTEGER_REMAINDER',remainder)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
