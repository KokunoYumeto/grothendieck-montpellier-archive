#!/usr/bin/env python3
"""Independent tuple-arithmetic witness for the universal F9 descent proof."""
from itertools import product
from fractions import Fraction
from pathlib import Path
import json,time

F=list(product(range(3),repeat=2)); Z=(0,0); O=(1,0); I=(0,1); TWO=(2,0)
def add(x,y): return ((x[0]+y[0])%3,(x[1]+y[1])%3)
def neg(x): return ((-x[0])%3,(-x[1])%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
def bar(x): return (x[0],-x[1]%3)
def inv(x):
    assert x!=Z
    return next(y for y in F if mul(x,y)==O)
def scale(x,v): return tuple(mul(x,z) for z in v)
def vadd(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vsub(x,y): return tuple(sub(a,b) for a,b in zip(x,y))
def det(A): return sub(mul(A[0],A[3]),mul(A[1],A[2]))
def mat(A,B): return (add(mul(A[0],B[0]),mul(A[1],B[2])),
                     add(mul(A[0],B[1]),mul(A[1],B[3])),
                     add(mul(A[2],B[0]),mul(A[3],B[2])),
                     add(mul(A[2],B[1]),mul(A[3],B[3])))
def mv(A,v): return (add(mul(A[0],v[0]),mul(A[1],v[1])),add(mul(A[2],v[0]),mul(A[3],v[1])))
def form(v,w): return sub(mul(v[0],w[1]),mul(v[1],w[0]))
def trace(x):
    z=add(x,bar(x)); assert z[1]==0; return z[0]
def dot(v,w): return add(mul(v[0],w[0]),mul(v[1],w[1]))

def main():
    start=time.monotonic(); gl=cocycles=bases=identities=0; V=list(product(F,repeat=2))
    eye=(O,Z,Z,O); roots={mul(z,z) for z in F if z!=Z}
    assert roots=={z for z in F if mul(z,bar(z))==O}
    for H in product(F,repeat=4):
        mu=det(H)
        if mu==Z: continue
        gl+=1; HH=mat(H,tuple(map(bar,H)))
        if HH[1]!=Z or HH[2]!=Z or HH[0]!=HH[3]: continue
        c=HH[0]; assert c[1]==0 and c!=Z
        assert mul(mu,bar(mu))==mul(c,c)==O
        z=next(z for z in F if z!=Z and mul(z,bar(z))==inv(c))
        K=scale(z,H); assert mat(K,tuple(map(bar,K)))==eye
        beta=det(K); d=next(d for d in F if mul(d,d)==beta)
        def semi(v): return mv(K,tuple(map(bar,v)))
        fixed=[v for v in V if semi(v)==v]
        assert len(fixed)==9; cocycles+=1
        for x in V:
            sx=semi(x); x0=scale(TWO,vadd(x,sx)); x1=scale(inv(mul(TWO,I)),vsub(x,sx))
            assert semi(x0)==x0 and semi(x1)==x1
            assert vadd(x0,scale(I,x1))==x; identities+=1
        count=0
        for v in fixed:
            for w in fixed:
                b=mul(d,form(v,w)); assert b[1]==0
                if b!=O: continue
                P=(v[0],w[0],v[1],w[1]); assert det(P)==inv(d)
                assert mat(K,tuple(map(bar,P)))==P
                count+=1
        assert count==24; bases+=count
    assert (gl,cocycles,bases,identities)==(5760,240,5760,19440)
    dual=0
    for w in V:
        for v in V:
            assert trace(dot(w,tuple(map(bar,v))))==trace(dot(tuple(map(bar,w)),v)); dual+=1
    fixed=sum(tuple(map(bar,w))==w for w in V); assert fixed==9 and dual==6561
    assert Fraction(81-9,4*81)==Fraction(2,9)>Fraction(3,16)
    assert Fraction(3,16)*12-2==Fraction(1,4)
    out={'status':'PASS','method':'independent tuple model F3[zeta]/(zeta^2+1)',
         'invertible_matrices':gl,'projective_semilinear_involutions':cocycles,
         'symplectic_descent_bases':bases,'vector_descent_identities':identities,
         'dual_trace_pairings':dual,'fixed_dual_weights':fixed,
         'q9_support_ratio':'2/9','uniform_ratio':'3/16','Hurwitz_degree_ceiling':24,
         'seconds':round(time.monotonic()-start,6)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
