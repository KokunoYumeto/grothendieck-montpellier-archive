#!/usr/bin/env python3
"""Exact F9 witnesses for the separately proved all-dimensional descent.

All GL2(F9) projective involution cocycles are checked, along with every
rank-two row-character pairing. Finite toy matrices are not claimed to
prove a higher-dimensional or all-representation theorem.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time

B=Path(__file__).resolve().parent

# a+3b represents a+b*zeta, zeta^2=-1 over F3.
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x):return ((-(x%3))%3)+3*((-(x//3))%3)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    a,b=x%3,x//3;c,d=y%3,y//3
    return (a*c-b*d)%3+3*((a*d+b*c)%3)
def power(x,k):
    r=1
    for _ in range(k):r=mul(r,x)
    return r
def inv(x):assert x;return power(x,7)
def sig(x):return power(x,3)
def norm(x):return mul(x,sig(x))
def trace(x):return add(x,sig(x))
def scale(c,v):return tuple(mul(c,x) for x in v)
def vadd(v,w):return tuple(add(x,y) for x,y in zip(v,w))
def vsub(v,w):return tuple(sub(x,y) for x,y in zip(v,w))
def msig(A):return tuple(sig(x) for x in A)
def mm(A,C):
    return tuple(add(mul(A[2*i],C[j]),mul(A[2*i+1],C[2+j])) for i in range(2) for j in range(2))
def mv(A,v):return tuple(add(mul(A[2*i],v[0]),mul(A[2*i+1],v[1])) for i in range(2))
def det(A):return sub(mul(A[0],A[3]),mul(A[1],A[2]))
def mi(A):return scale(inv(det(A)),(A[3],neg(A[1]),neg(A[2]),A[0]))
def pairing(v,w):return sub(mul(v[0],w[1]),mul(v[1],w[0]))
def dot(v,w):return add(mul(v[0],w[0]),mul(v[1],w[1]))

def main():
    start=time.perf_counter();I=(1,0,0,1);vecs=list(product(range(9),repeat=2))
    assert all(add(x,neg(x))==0 and sig(sig(x))==x for x in range(9))
    assert all(mul(x,inv(x))==1 for x in range(1,9))
    assert mul(3,3)==2 and sig(3)==neg(3)
    squares={mul(z,z) for z in range(1,9)}
    assert squares=={x for x in range(1,9) if norm(x)==1}
    stats={'invertible_matrices':0,'projective_involution_cocycles':0,
           'fixed_symplectic_bases':0,'vector_descent_identities':0,
           'dual_weight_pairings':0}
    cocycles=[]
    for h in product(range(9),repeat=4):
        mu=det(h)
        if not mu:continue
        stats['invertible_matrices']+=1
        hs=mm(h,msig(h));c=hs[0]
        if not c or hs!=(c,0,0,c):continue
        stats['projective_involution_cocycles']+=1
        assert c in (1,2) and norm(mu)==mul(c,c)==1 and mu in squares
        z=next(z for z in range(1,9) if norm(z)==inv(c))
        H=scale(z,h);assert mm(H,msig(H))==I
        beta=mul(mul(z,z),mu)
        d=next(d for d in range(1,9) if mul(d,d)==beta)
        s=lambda v:mv(H,tuple(sig(x) for x in v))
        fixed=[v for v in vecs if s(v)==v]
        assert len(fixed)==9
        bases=[]
        for u,v in product(fixed,repeat=2):
            if mul(d,pairing(u,v))!=1:continue
            P=(u[0],v[0],u[1],v[1]);assert det(P)==inv(d)
            assert mm(mi(P),mm(H,msig(P)))==I
            bases.append(P);stats['fixed_symplectic_bases']+=1
        assert len(bases)==24
        for x in vecs:
            sx=s(x)
            x0=scale(inv(2),vadd(x,sx));x1=scale(inv(mul(2,3)),vsub(x,sx))
            assert s(x0)==x0 and s(x1)==x1 and vadd(x0,scale(3,x1))==x
            stats['vector_descent_identities']+=1
        assert all(mul(d,pairing(u,v)) in (0,1,2) for u,v in product(fixed,repeat=2))
        cocycles.append({'h':h,'c':c,'scalar_z':z,'form_scale_d':d,'fixed_basis':bases[0]})
    assert stats['invertible_matrices']==5760
    assert stats['projective_involution_cocycles']==240
    assert stats['fixed_symplectic_bases']==5760
    assert stats['vector_descent_identities']==19440
    sigma=lambda v:tuple(sig(x) for x in v)
    fixed=[w for w in vecs if sigma(w)==w]
    assert len(fixed)==9
    pairs={tuple(sorted((w,sigma(w)))) for w in vecs if sigma(w)!=w}
    assert len(pairs)==36
    for w,v in product(vecs,repeat=2):
        assert trace(dot(w,sigma(v)))==trace(dot(sigma(w),v))
        stats['dual_weight_pairings']+=1
    assert stats['dual_weight_pairings']==6561
    assert F(81-9,4*81)==F(2,9)>F(3,16)
    assert F(5-3,2*5)==F(1,5)>F(3,16)
    assert F(25**3-1,2)>F(5**3-1,2)==62>24
    assert 13**2>24 and F(12*3,16)-2==F(1,4) and 6/F(1,4)==24
    out={'status':'PASS exact finite witnesses, universal proof separate',**stats,
         'row_weights':81,'fixed_row_weights':9,'paired_weight_orbits':36,
         'q9_support':'2/9','uniform_support':'3/16','maximum_total_degree':24,
         'cocycle_witnesses':cocycles,'seconds':round(time.perf_counter()-start,6)}
    (B/'f9_checked.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cocycle_witnesses'},indent=2))

if __name__=='__main__':main()
