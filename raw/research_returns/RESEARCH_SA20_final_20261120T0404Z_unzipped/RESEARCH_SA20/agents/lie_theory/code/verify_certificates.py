#!/usr/bin/env python3
"""Independent exact verifier; only Python integers and fractions, no numpy.

Reconstructs roots and all possible cyclic intertwiners independently, verifies
every supplied Weyl word, centralizer, all unit exponents, and splitting tests.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import gcd
import json

OUT=Path(__file__).resolve().parents[1]/'logs'
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col)) for col in zip(*b)) for row in a)
def mv(a,v):return tuple(sum(x*y for x,y in zip(row,v)) for row in a)
def mp(a,k):
    z=eye(len(a))
    for _ in range(k):z=mm(z,a)
    return z
def trans(a):return tuple(zip(*a))
def inv(a):
    n=len(a);b=[list(map(F,row))+list(map(F,e)) for row,e in zip(a,eye(n))]
    for i in range(n):
        j=next(j for j in range(i,n) if b[j][i]);b[i],b[j]=b[j],b[i]
        q=b[i][i];b[i]=[x/q for x in b[i]]
        for j in range(n):
            if j!=i:
                q=b[j][i];b[j]=[x-q*y for x,y in zip(b[j],b[i])]
    return tuple(tuple(row[n:]) for row in b)
def check(kind):
    data=json.loads((OUT/f'normalizer_{kind}.json').read_text());A=data['cartan'];n=len(A);I=eye(n)
    S=[]
    for i in range(n):
        s=[list(r) for r in I];s[i]=[x-y for x,y in zip(s[i],A[i])];S.append(tuple(map(tuple,s)))
    R=set(I);todo=list(R)
    for v in todo:
        for s in S:
            q=mv(s,v)
            if q not in R:R.add(q);todo.append(q)
    c=I
    for s in S:c=mm(c,s)
    h=data['h'];P=[mp(c,j) for j in range(h)]
    assert mp(c,h)==I and len(set(P))==h and len(R)==data['root_count']
    assert c==tuple(map(tuple,data['coxeter']))
    cert={tuple(map(tuple,e['matrix'])):e for e in data['all_normalizer_elements']}
    for w,e in cert.items():
        v=w
        for i in e['inverse_reduction_word']:v=mm(S[i-1],v)
        assert v==I and mm(w,c)==mm(P[e['unit']],w)
    r=tuple(data['cyclic_root']);piv=data['basis_powers']
    B=trans([mv(P[k],r) for k in piv]);BI=inv(B)
    all_candidates=set();G=tuple(map(tuple,data['gram']))
    # Determine Weyl membership independently from rho, using a different
    # negative-wall choice (last rather than first).
    rho=mv(inv(A),[1]*n)
    for a in range(h):
        if gcd(a,h)!=1:continue
        for q in R:
            w=mm(trans([mv(P[(a*k)%h],q) for k in piv]),BI)
            if any(x.denominator!=1 for row in w for x in row):continue
            w=tuple(tuple(int(x) for x in row) for row in w)
            if mm(w,c)!=mm(P[a],w) or mm(mm(trans(w),G),w)!=G:continue
            if {mv(w,v) for v in R}!=R:continue
            u=w;v=mv(w,rho)
            for _ in range(len(R)//2+1):
                neg=[i for i,x in enumerate(mv(A,v)) if x<0]
                if not neg:break
                i=neg[-1];u=mm(S[i],u);v=mv(S[i],v)
            else:raise AssertionError('chamber reduction failed')
            if u==I:all_candidates.add(w)
    assert all_candidates==set(cert)
    C={w for w,e in cert.items() if e['unit']==1};assert C==set(P)
    units={a for a in range(h) if gcd(a,h)==1}
    assert {e['unit'] for e in cert.values()}==units
    assert all(sum(e['unit']==a for e in cert.values())==h for a in units)
    hist=[]
    for a,o in data['unit_generators']:
        counts={}
        for w,e in cert.items():
            if e['unit']==a:
                t=mp(w,o);j=P.index(t);counts[j]=counts.get(j,0)+1
        hist.append({'unit':a,'order':o,'power_coxeter_exponent_counts':counts})
    if data['splits']:
        lifts=[tuple(map(tuple,e['matrix'])) for e in data['complement']]
        for w,(_,o) in zip(lifts,data['unit_generators']):assert mp(w,o)==I
        for u,v in product(lifts,repeat=2):assert mm(u,v)==mm(v,u)
    else:assert any(0 not in x['power_coxeter_exponent_counts'] for x in hist)
    print(f'{kind}: independent exhaustive verification OK; |N|={len(cert)}, C_W(c)=<c>, all units realized; {hist}')

if __name__=='__main__':
    for kind in ['G2','F4','E6','E7','E8']:check(kind)
