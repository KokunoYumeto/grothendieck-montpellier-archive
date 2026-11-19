"""Exact checks for the characteristic-two odd-degree Hasse--Witt obstruction.
Python 3.11+, SymPy 1.14 only for the projective smoothness certificate.
The universal identity is proved by symbolic monomial cancellation over F_2.
"""
from pathlib import Path
from itertools import product
from random import Random
from time import perf_counter
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
start=perf_counter()

def exponents(d,positive=False):
    low=1 if positive else 0
    return [(a,b,d-a-b) for a in range(low,d-2*low+1)
            for b in range(low,d-a-low+1)]

def hw(support,d):
    I=exponents(d,True)
    return [[int(tuple(2*v[i]-u[i] for i in range(3)) in support)
             for v in I] for u in I]

def rank(A):
    A=[r[:] for r in A]
    r=0
    for c in range(len(A[0]) if A else 0):
        k=next((k for k in range(r,len(A)) if A[k][c]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]
        for k in range(len(A)):
            if k!=r and A[k][c]:
                A[k]=[x^y for x,y in zip(A[k],A[r])]
        r+=1
    return r

def matrix_product(A,B):
    return [[sum(x*y for x,y in zip(row,col))%2 for col in zip(*B)] for row in A]

universal=[]
for d in range(3,24,2):
    I=exponents(d,True); allc=set(exponents(d))
    for v in I:
        terms=set()
        for u in I:
            if not all(t%2 for t in u): continue
            b=tuple(2*v[i]-u[i] for i in range(3))
            if b not in allc: continue
            term=tuple(sorted((u,b)))
            if term in terms: terms.remove(term)
            else: terms.add(term)
        expected={(v,v)} if all(t%2 for t in v) else set()
        assert terms==expected,(d,v,terms,expected)
    universal.append({'degree':d,'genus':len(I),'identity':'H^T w = w^[2]','result':True})

x,y,z=sp.symbols('x y z')
rng=Random(151904)
d=5; allc=exponents(d); I=exponents(d,True)
for attempt in range(10000):
    support={a for a in allc if rng.randrange(2)}
    H=hw(support,d)
    if rank(H)!=len(I): continue
    f=sum(x**a*y**b*z**c for a,b,c in support)
    deriv=[sp.diff(f,t) for t in (x,y,z)]
    charts=[]
    for t in (x,y,z):
        variables=tuple(s for s in (x,y,z) if s!=t)
        generators=[q.subs(t,1) for q in [f]+deriv]
        gb=sp.groebner(generators,*variables,modulus=2)
        charts.append([str(q.as_expr()) for q in gb.polys])
    if charts==[['1']]*3: break
else: raise AssertionError('search failed')
w=[int(all(t%2 for t in a) and a in support) for a in I]
assert any(w)
assert [sum(H[i][j]*w[i] for i in range(len(I)))%2 for j in range(len(I))]==w

# Exact point counting over F_(2^m), using fixed irreducible modulus polynomials.
moduli={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}
def multiply(a,b,m):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&(1<<m):a^=moduli[m]
    return c

def power(a,b,m):
    c=1
    while b:
        if b&1:c=multiply(c,a,m)
        a=multiply(a,a,m);b>>=1
    return c

def evaluate(pt,m):
    r=0
    for a in support:
        term=1
        for v,e in zip(pt,a):term=multiply(term,power(v,e,m),m)
        r^=term
    return r

point_counts=[]; Hp=[[int(i==j) for j in range(len(I))] for i in range(len(I))]
for m in moduli:
    q=1<<m
    points=[(a,b,1) for a in range(q) for b in range(q)]
    points +=[(a,1,0) for a in range(q)]+[(1,0,0)]
    N=sum(evaluate(P,m)==0 for P in points)
    Hp=matrix_product(Hp,H)
    tr=sum(Hp[i][i] for i in range(len(I)))%2
    assert N%2==(1-tr)%2
    point_counts.append({'extension_degree':m,'field_size':q,'points':N,'trace_H_power_mod2':tr,'count_congruence':True})

result={'universal_identity_checks':universal,
        'example':{'field':'F_2','degree':d,'seed':151904,'search_attempts':attempt+1,
                   'equation':str(f),'monomial_support':sorted(support),'cohomology_index_order':I,
                   'Hasse_Witt_matrix':H,'rank':rank(H),'canonical_covector':w,
                   'smoothness_Groebner_bases_x1_y1_z1':charts,'point_counts':point_counts},
        'runtime_seconds':perf_counter()-start,
        'scope':'Universal identity checks are exact for the recorded degrees; pairing proof in paper covers all odd degrees. One ordinary smooth quintic explicitly verified. Point counts are finite checks, not a computation of the full monodromy image.'}
(ROOT/'outputs/plane_char2.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
