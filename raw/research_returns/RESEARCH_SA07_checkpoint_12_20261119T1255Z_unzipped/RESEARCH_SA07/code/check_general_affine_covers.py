#!/usr/bin/env python3
"""Exact finite cover checks for F.3.33.

Verifies the full eight-element UT3(F2) group and its regular cusp
permutation, the explicit boundary quotient matrices, and symbolic
Riemann--Hurwitz identities with nonnegative genus parameters.
The geometric/arithmetic realization and normalizer maps are proved in
LM6_A22_general_affine_composite.tex, not inferred from these checks.
"""
from itertools import product
from fractions import Fraction
from time import perf_counter
import sympy as sp

started=perf_counter()
G=set(product(range(2),repeat=3))
e=(0,0,0);x=(1,0,0);y=(0,1,0)
def mul(u,v):
    a,b,c=u;d,f,h=v
    return ((a+d)%2,(b+f)%2,(c+h+a*f)%2)
def inverse(u):
    a,b,c=u
    return (a,b,(c+a*b)%2)
def power(u,n):
    out=e
    for _ in range(n):out=mul(out,u)
    return out
for u in G:
    assert mul(u,e)==u==mul(e,u)
    assert mul(u,inverse(u))==e==mul(inverse(u),u)
    for v in G:
        assert mul(u,v) in G
        for w in G:
            assert mul(mul(u,v),w)==mul(u,mul(v,w))
seen={e};front=[e]
while front:
    u=front.pop()
    for v in (x,y):
        w=mul(u,v)
        if w not in seen:seen.add(w);front.append(w)
assert seen==G
comm=mul(mul(mul(x,y),inverse(x)),inverse(y))
assert comm==(0,0,1) and comm!=e and power(comm,2)==e
assert power(x,2)==e and power(y,2)==e
unseen=set(G);cycles=[]
while unseen:
    start=min(unseen);cycle=[];u=start
    while u not in cycle:
        cycle.append(u);unseen.remove(u);u=mul(u,comm)
    assert u==start
    cycles.append(cycle)
assert sorted(map(len,cycles))==[2,2,2,2]
cover_degree=len(G);cusp_count=len(cycles)
twogenusminus2=cover_degree*(2*1-2+1)-cusp_count
assert twogenusminus2==4 and (twogenusminus2+2)//2==3
print('UT3_F2_ORDER',len(G))
print('GENERATOR_IMAGES',x,y,'COMMUTATOR',comm)
print('REGULAR_CUSP_CYCLES',cycles)
print('PUNCTURED_TORUS_COVER_DEGREE',cover_degree,'CUSPS',cusp_count,'COMPACT_GENUS',3)

# The matrix is [I_(n-1) | -1]. Its identity minor gives the exact rank;
# every column is nonzero, so each peripheral image has exact order5.
def rank_mod5(M):
    A=[[int(z)%5 for z in row] for row in M];r=0
    for c in range(len(A[0])):
        j=next((j for j in range(r,len(A)) if A[j][c]),None)
        if j is None:continue
        A[r],A[j]=A[j],A[r]
        inv=pow(A[r][c],-1,5);A[r]=[(v*inv)%5 for v in A[r]]
        for j in range(len(A)):
            if j!=r:
                a=A[j][c];A[j]=[(v-a*w)%5 for v,w in zip(A[j],A[r])]
        r+=1
        if r==len(A):break
    return r
for n in range(2,9):
    B=sp.eye(n-1).row_join(-sp.ones(n-1,1))
    assert B[:,0:n-1].det()==1 and rank_mod5(B.tolist())==n-1
    assert B*sp.ones(n,1)==sp.zeros(n-1,1)
    for j in range(n):
        v=[int(B[i,j])%5 for i in range(n-1)]
        assert any(v)
        assert all((5*z)%5==0 for z in v)
        assert all(any((a*z)%5 for z in v) for a in (1,2,3,4))
print('BOUNDARY_MATRICES_CHECKED_n_2_TO_8: identity minor, sum relation, exact order5')

u,v,t=sp.symbols('u v t',integer=True,nonnegative=True)
# n>=2,g=0: hyperbolicity gives n=3+t.
original0=5**(t+2)*(-2+sp.Rational(4,5)*(3+t))
positive0=2*5**(t+1)*(2*t+1)
assert sp.simplify(original0-positive0)==0
assert positive0.subs(t,0)==10
# n>=2,g>=1: g=1+u,n=2+v.
original1=5**(2*(1+u)+(2+v)-1)*(2*(1+u)-2+sp.Rational(4,5)*(2+v))
positive1=5**(2*u+v+2)*(10*u+4*v+8)
assert sp.simplify(original1-positive1)==0
assert positive1.subs({u:0,v:0})==200
assert all(c>0 for c in sp.Poly(10*u+4*v+8,u,v).coeffs())
# n=1,g>=2: g=2+u, full mod2 abelian quotient is unramified at the cusp.
genus_unramified=1+2**(2*(2+u))*((2+u)-1)
positive_unramified=1+16*4**u*(1+u)
assert sp.simplify(genus_unramified-positive_unramified)==0
assert positive_unramified.subs(u,0)==17
print('ALL_PARAMETER_RH_IDENTITIES_PASSED')
print('MINIMUM_COMPACT_GENERA: n>=2 gives6; n=1,g>=2 gives17; (1,1) gives3')
# Exact arithmetic spot checks accompany, but do not replace, the identities.
for g in range(6):
    for n in range(2,9):
        if 2-2*g-n>=0:continue
        d=5**(2*g+n-1)
        two=Fraction(d)*(2*g-2+Fraction(4*n,5))
        genus=1+two/2
        assert genus.denominator==1 and genus>=6
print('FINITE_RH_ARITHMETIC_CHECKS_PASSED')
print('SCOPE: finite group, boundary matrix, and symbolic genus identities only.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
