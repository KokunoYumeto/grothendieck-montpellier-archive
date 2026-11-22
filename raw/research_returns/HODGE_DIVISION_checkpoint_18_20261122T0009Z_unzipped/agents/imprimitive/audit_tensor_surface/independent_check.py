#!/usr/bin/env python3
"""Own tuple-monomial exterior reconstruction of E823; no author code imported.

Generators are interleaved x0,y0,x1,y1,x2,y2,x3,y3, unlike the author's
bit-mask/all-holomorphic-first convention. Ext and derived identities are
reviewed in PEER_AUDIT.md, not certified by this finite arithmetic.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
import hashlib,json,time
import sympy as s

start=time.monotonic()
def norm(a):
    return {w:s.expand(c) for w,c in a.items() if s.expand(c)!=0}
def add(*args):
    out={}
    for a in args:
        for w,c in a.items():out[w]=out.get(w,0)+c
    return norm(out)
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if set(u)&set(v):continue
            sign=(-1)**sum(i>j for i in u for j in v)
            w=tuple(sorted(u+v));out[w]=out.get(w,0)+sign*c*d
    return norm(out)
def scale(a,c):return norm({w:c*d for w,d in a.items()})
ONE={():s.Integer(1)}
def power(a,n):
    b=ONE
    for _ in range(n):b=mul(b,a)
    return b
def exp(a):return add(*(scale(power(a,n),Q(1,factorial(n))) for n in range(5)))
def contract(a,i):
    out={}
    for w,c in a.items():
        if i in w:
            j=w.index(i);out[w[:j]+w[j+1:]]=(-1)**j*c
    return norm(out)
def pi(a,i,j):return contract(contract(a,i),j)

k,q=s.symbols('k q')
line=[{(2*i,2*i+1):s.Integer(1)} for i in range(4)]
plus=add(line[0],line[1]);minus=add(line[2],line[3]);theta=add(plus,minus)
D=scale(theta,k)
M=add(scale(exp(scale(D,-1)),2),scale(exp(scale(D,-3)),-2),exp(scale(D,-4)))
M_expected=add(ONE,scale(power(D,3),-2),scale(power(D,4),4))
assert M==M_expected
v=mul(add(ONE,scale(power(plus,2),-q/2)),add(ONE,scale(power(minus,2),-q/2)))
h=mul(v,add(ONE,scale(power(D,3),2),scale(power(D,4),-4)))
assert mul(h,M)==v
assert {w:c for w,c in h.items() if len(w)==2}=={}
h2={w:c for w,c in h.items() if len(w)==4}
assert h2==scale(add(power(plus,2),power(minus,2)),-q/2)
planes=[]
for i,j,plane,other in [(0,2,plus,minus),(4,6,minus,plus)]:
    eta=scale(pi(power(plane,2),i,j),Q(1,2))
    assert add(pi(v,i,j),scale(mul(eta,v),q))=={}
    # Exact cancellation of the scalar term in the partial trace, per rank.
    assert add(pi(h2,i,j),scale(eta,q))=={}
    obs=pi(scale(power(D,3),-2),i,j)
    assert obs==scale(mul(eta,other),-12*k**3) and obs
    assert all(sum(t%2==0 for t in w)==1 and sum(t%2==1 for t in w)==3 for w in obs)
    planes.append({'holomorphic_indices':[i,j],
       'eta':{str(w):str(c) for w,c in eta.items()},
       'cubic_obstruction':{str(w):str(c) for w,c in obs.items()}})

# Independent non-diagonal exact B, not the author's numerical matrix.
BM=[[1,-2,3,1],[-2,4,1,-3],[3,1,-2,2],[1,-3,2,5]]
B={}
for i in range(4):
    for j in range(4):B=add(B,scale(mul({(2*i,):1},{(2*j+1,):1}),BM[i][j]))
eB=exp(B);emB=exp(scale(B,-1));assert mul(eB,emB)==ONE
def shifted(a,i):return add(contract(a,i),mul(contract(B,i),a))
basis=[w for n in range(9) for w in combinations(range(8),n)]
assert len(basis)==256
count=0
for i,j,plane in [(0,2,plus),(4,6,minus)]:
    for w in basis:
        a={w:1}
        assert mul(emB,pi(mul(eB,a),i,j))==shifted(shifted(a,i),j)
        count+=1
    eta=scale(pi(power(plane,2),i,j),Q(1,2))
    ch=mul(emB,v)
    assert add(shifted(shifted(ch,i),j),scale(mul(eta,ch),q))=={}

root=Path(__file__).resolve().parent
draft=root.parent.parent/'sixfolds/rm_tensor_surface_obstruction_draft.md'
out={'status':'PASS','reviewed_draft_sha256':hashlib.sha256(draft.read_bytes()).hexdigest(),
 'method':'independent tuple monomials with interleaved generators; no author code imported',
 'full_resolution_character':True,'full_compensation_character':True,
 'both_cap_kernels_and_partial_trace_scalar_cancellations':True,'planes':planes,
 'B_matrix':BM,'B_shear_full_basis_checks':count,
 'limits':'Finite exterior sign/character certificate only; derived partial trace and finite-action compatibility are separately proved and audited.',
 'seconds':round(time.monotonic()-start,3)}
(root/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
