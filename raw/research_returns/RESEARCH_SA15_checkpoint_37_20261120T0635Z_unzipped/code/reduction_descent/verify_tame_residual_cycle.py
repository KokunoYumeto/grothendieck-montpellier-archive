#!/usr/bin/env python3
"""Exact finite character/valuation arithmetic for B53.

No finite experiment is claimed to establish the formal-point or descent lemma.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
from time import perf_counter
import json
import sympy as sp

started=perf_counter()
rows=[]
pair_count=0
valuation_cases=0
for p in sp.primerange(5,102):
    p=int(p)
    N=p*p-1
    n=(p+1)//2
    def orbit(c):
        return tuple(sorted({c%N,p*c%N}))
    def generic(c):
        return orbit(c+p-1)
    def affine(c):
        return (p*c+(p-1)**2)%N
    types=[orbit(1+(p-1)*2*k) for k in range(n)]
    assert len(set(types))==n and all(len(t)==2 for t in types)
    label={c:k for k,t in enumerate(types) for c in t}
    assert len(label)==p+1
    for c in label:
        assert c%(p-1)==1
        assert (c+p-1)%(p+1)!=0  # irreducible generic eigenpair
        assert affine(affine(c))==c
        assert gcd(gcd(N,c),affine(c))==1
        assert generic(c)==generic(affine(c))
    edges=set()
    for k in range(n):
        for ell in range(k+1,n):
            actual=any(affine(c)==d for c in types[k] for d in types[ell])
            expected=(ell-k)%n in (1,n-1)
            assert actual==expected
            # The relation is exactly equality of some oriented generic pairs.
            assert actual==any(generic(c)==generic(d)
                               for c in types[k] for d in types[ell])
            if actual:
                edges.add((k,ell))
            pair_count+=1
    assert len(edges)==n

    quadratic={k:label[(types[k][0]+N//2)%N] for k in range(n)}
    quad_edges={tuple(sorted((k,ell))) for k,ell in quadratic.items()
                if k!=ell and tuple(sorted((k,ell))) in edges}
    if p%4==3:
        assert all(quadratic[k]==(k+n//2)%n for k in range(n))
        assert not quad_edges
    else:
        assert all(quadratic[k]==((1-n)//2-k)%n for k in range(n))
        assert len(quad_edges)==1
    for t in sp.divisors(N):
        A=Fraction((p-1)*int(t),N)
        assert (A.denominator==1)==(int(t)%(p+1)==0)
        assert Fraction(N,int(t))*A==p-1
        valuation_cases+=1
    rows.append({'p':p,'N':N,'cycle_length':n,'types':types,
                 'edges':sorted(edges),'quadratic_edges':sorted(quad_edges)})

row7=next(r for r in rows if r['p']==7)
assert row7['types']==[(1,7),(13,43),(25,31),(19,37)]
assert row7['edges']==[(0,1),(0,3),(1,2),(2,3)]
row5=next(r for r in rows if r['p']==5)
assert row5['cycle_length']==3 and len(row5['edges'])==3

result={'status':'PASS','scope':'Finite character and rational valuation arithmetic only; the geometric leading-coordinate argument is proved in B_tame_residual_cycle.tex.',
        'prime_range':[5,101],'primes':len(rows),'pair_count':pair_count,
        'valuation_cases':valuation_cases,'rows':rows,
        'elapsed_seconds':perf_counter()-started}
destination=Path(__file__).with_suffix('.output.json')
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
