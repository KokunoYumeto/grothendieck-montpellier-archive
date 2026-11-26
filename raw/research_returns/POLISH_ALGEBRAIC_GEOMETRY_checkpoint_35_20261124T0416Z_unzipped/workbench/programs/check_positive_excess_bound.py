#!/usr/bin/env python3
"""Exact arithmetic checks for the positive-excess theorem, not a geometry proof.

Method: sparse integer-polynomial coefficient arithmetic and rational recurrence
evaluation, independent of the worker's hand calculation. Save before execution.
Run: python3 programs/check_positive_excess_bound.py
"""
from fractions import Fraction
from math import prod
import json

# Sparse polynomials in p,m,d,G,L,D (conductor length and curve defect).
N=6
def const(n): return {(0,)*N:n} if n else {}
def var(i):
    a=[0]*N; a[i]=1; return {tuple(a):1}
def add(*polys):
    out={}
    for q in polys:
        for e,c in q.items(): out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def scale(q,n): return {e:c*n for e,c in q.items() if c*n}
def mul(a,b):
    out={}
    for e,c in a.items():
        for f,v in b.items():
            h=tuple(x+y for x,y in zip(e,f));out[h]=out.get(h,0)+c*v
    return {e:c for e,c in out.items() if c}
p,m,d,G,L,D=[var(i) for i in range(N)]
pm1=add(p,const(-1)); delta=add(G,scale(mul(m,d),-1))
identities=[]
def equal(name,a,b):
    assert add(a,scale(b,-1))=={},name
    identities.append(name)
equal('adjunction defect rearrangement',
      add(mul(p,G),scale(mul(mul(m,pm1),d),-1),scale(L,-1),scale(G,-1),scale(D,-2)),
      add(mul(pm1,delta),scale(L,-1),scale(D,-2)))
# Clear p from G - (m/p)(p*d-2*(p-1)*delta).
equal('one-step excess factor after clearing p',
      add(mul(p,G),scale(mul(m,mul(p,d)),-1),scale(mul(m,mul(pm1,delta)),2)),
      mul(add(p,scale(mul(pm1,m),2)),delta))
# Blowup loss versus four times arithmetic-genus loss, with m as multiplicity.
equal('blowup coefficient gap mu(mu-2)',
      add(scale(mul(m,add(m,const(-1))),2),scale(mul(m,m),-1)),
      mul(m,add(m,const(-2))))

def valuation(n,p):
    r=0
    while n%p==0: n//=p;r+=1
    return r
def Q(p,m): return prod(1+2*(p-1)*(m//p**j) for j in range(1,valuation(m,p)+1))
examples=[]
for prime,order,want in [(2,2,Fraction(1)),(2,4,Fraction(2,7)),(3,3,Fraction(3,4)),(3,9,Fraction(9,64))]:
    q=Q(prime,order);coef=Fraction(order,q-1);assert coef==want
    examples.append({'p':prime,'m':order,'Q':q,'delta_over_d_lower_bound':str(coef)})
steps=0;cases=0
for prime in [2,3,5,7,11]:
    for r in range(1,7):
        for unit in [1,2,3,4,5,7,11]:
            if unit%prime==0: continue
            order=unit*prime**r; q=Q(prime,order)
            if r==1: assert Fraction(order,q-1)==Fraction(prime,2*(prime-1))
            # Hypothetical strict failure Q*delta<G; exact rationals only.
            for frac in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(99,100)]:
                genus=Fraction(2*q+2);excess=frac*genus/q
                square=(genus-excess)/order;bound=Fraction(1)
                for j in range(1,r+1):
                    next_order=order//prime
                    loss=2*(prime-1)*excess
                    next_square=prime*square-loss
                    factor=1+2*(prime-1)*next_order
                    next_excess=genus-next_order*next_square
                    assert next_square>0
                    assert next_excess==factor*excess
                    bound*=factor
                    order,square,excess=next_order,next_square,next_excess
                    steps+=1
                assert order%prime!=0 and excess<genus
                assert bound==q
                cases+=1
                order=unit*prime**r
print(json.dumps({'status':'PASS','method':'sparse integer coefficient identities and exact rational recurrence at worst permitted resolution loss','symbolic_identities':identities,'examples':examples,'recurrence_cases':cases,'recurrence_steps':steps,'limits':'No geometry, conductor formula, surface resolution existence, or independent proof is certified by this program.'},indent=2))
