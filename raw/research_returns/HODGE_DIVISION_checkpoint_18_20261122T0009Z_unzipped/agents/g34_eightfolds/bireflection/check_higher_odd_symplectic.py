#!/usr/bin/env python3
"""Exact rational, symbolic and F9 checks for D-HOS-03--06.

No character table is used. The unbounded-field/rank statements are
proved in the TeX; the finite F9 calculation only certifies the stated
scalar identities and the smallest-rank dual-weight count.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,json,time
import sympy as s

B=Path(__file__).resolve().parent

def equal(A,C):
    return A.shape==C.shape and all(s.expand(x-y)==0 for x,y in zip(A,C))

def main():
    start=time.perf_counter()
    delta=F(9234,55223)
    assert 1372>1369 and F(37,14)>1
    assert F(1,2)*F(6,7)*F(342,343)*F(9,23)==delta
    assert F(1,6)<delta<F(1,4)
    assert F(9,50)*F(15624,15625)>delta
    assert F(13,54)>delta
    assert 12*delta-2==F(362,55223)
    cap=6/(12*delta-2)
    assert cap==F(165669,181)<916<1029==3*7**3
    q,x=s.symbols('q x')
    def positive(poly,at):
        c=s.Poly(s.expand(poly.subs(q,at+x)),x).all_coeffs()
        assert all(a>=0 for a in c) and c[-1]>0
        return [int(a) for a in reversed(c)]
    numerical={
        'delta_star':str(delta),
        'delta25_over2':str(F(9,50)*F(15624,15625)),
        'q9_row_bound':'13/54',
        'degree_upper_bound':str(cap),
        'integer_degree_upper_bound':cap.numerator//cap.denominator,
        'degree_lower_bound':1029,
        'elliptic_ratio_polynomial':positive(q**3-3*q*q-4*q-2,7),
        'rank_growth_polynomial':positive(q*q-q-1,7),
    }

    # Complete symbolic line-parabolic Heisenberg identity in natural
    # dimension8 (the smallest rank used in the theorem).
    m=3
    JW=s.zeros(2*m)
    JW[:m,m:]=s.eye(m);JW[m:,:m]=-s.eye(m)
    J=s.zeros(2*m+2);J[0,-1]=1;J[-1,0]=-1;J[1:-1,1:-1]=JW
    vv=s.Matrix(s.symbols('v0:6'));ww=s.Matrix(s.symbols('w0:6'))
    z,t=s.symbols('z t')
    def H(v,c):
        A=s.eye(2*m+2);A[0,1:-1]=(v.T*JW);A[1:-1,-1]=v;A[0,-1]=2*c
        return A
    A=H(vv,z);C=H(ww,t)
    assert equal(A.T*J*A,J)
    assert equal(A*C,H(vv+ww,z+t+(vv.T*JW*ww)[0]/2))
    lam,a,b,c=s.symbols('lam a b c',nonzero=True)
    W=s.diag(a,b,c,1/a,1/b,1/c)
    h=s.diag(lam,*[W[i,i] for i in range(6)],1/lam)
    assert equal(h.T*J*h,J)
    assert equal(h*A*h.inv(),H(lam*W*vv,lam**2*z))

    # The shear construction and its normalized conjugation action.
    p0,p1,p2=s.symbols('p0 p1 p2')
    S=s.Matrix([[p0,p1],[p1,p2]])
    N=s.zeros(8)
    N[0,4]=p0;N[0,5]=p1;N[1,4]=p1;N[1,5]=p2
    Jstd=s.zeros(8);Jstd[:4,4:]=s.eye(4);Jstd[4:,:4]=-s.eye(4)
    assert N*N==s.zeros(8)
    assert equal((s.eye(8)+N).T*Jstd*(s.eye(8)+N),Jstd)
    # On a quadratic extension-field line, multiplication by sqrt(c)
    # is this exact companion matrix. Both possible multipliers have
    # nonzero minus-one symmetric shears.
    cc=s.symbols('cc',nonzero=True)
    K=s.Matrix([[0,cc],[1,0]])
    assert K*K==cc*s.eye(2)
    for mu in [cc,-cc]:
        image=K*S*K.T/mu
        assert equal(K*image*K.T/mu,S)
    assert equal(K*s.diag(cc,-1)*K.T/cc,-s.diag(cc,-1))
    swap=s.Matrix([[0,1],[1,0]])
    assert equal(K*swap*K.T/(-cc),-swap)

    # F9=F3[i], i^2=-1. Exhaustive norm/scalar-power repair and all
    # smallest-rank row-group dual orbits, independently of any matrix
    # or field code in previous certificates.
    digits=[(u%3,u//3) for u in range(9)]
    def enc(a,b):return a%3+3*(b%3)
    def add(a,b):
        u,v=digits[a];w,z=digits[b];return enc(u+w,v+z)
    def mul(a,b):
        u,v=digits[a];w,z=digits[b];return enc(u*w-v*z,u*z+v*w)
    def sig(a):
        u,v=digits[a];return enc(u,-v)
    def powr(a,n):
        z=1
        for _ in range(n):z=mul(z,a)
        return z
    inv={a:powr(a,7) for a in range(1,9)}
    assert all(mul(a,inv[a])==1 for a in inv)
    norm={a:mul(a,sig(a)) for a in inv}
    squares={mul(a,a) for a in inv}
    assert squares=={a for a in inv if norm[a]==1}
    scalar_checks=0
    for center in [1,2]:
        for mu in inv:
            if norm[mu]!=mul(center,center):continue
            assert mu in squares
            repairs=[a for a in inv if norm[a]==inv[center]]
            assert len(repairs)==4
            for a in repairs:
                newmu=mul(mul(a,a),mu)
                ds=[d for d in inv if mul(sig(d),inv[d])==newmu]
                assert len(ds)==2
                for d in ds:
                    assert mul(d,newmu)==sig(d)
                    scalar_checks+=1
    assert scalar_checks==64
    weights=list(product(range(9),repeat=3))
    fixed=[v for v in weights if tuple(sig(a) for a in v)==v]
    assert len(weights)==729 and len(fixed)==27
    unseen=set(weights);orbits=[]
    while unseen:
        v=min(unseen);o={v,tuple(sig(a) for a in v)}
        unseen-=o;orbits.append(len(o))
    assert orbits.count(1)==27 and orbits.count(2)==351
    assert F(729-27,4*729)==F(13,54)
    trace=lambda a:add(a,sig(a))
    for a in range(1,9):assert any(trace(mul(a,b))!=0 for b in range(9))
    for a,b in product(range(9),repeat=2):
        assert trace(mul(a,sig(b)))==trace(mul(sig(a),b))

    out={
        'status':'PASS exact arithmetic and explicit identities',
        'proof_sha256':hashlib.sha256((B/'higher_odd_symplectic_section.tex').read_bytes()).hexdigest(),
        'carrier_proof_sha256':hashlib.sha256((B/'heisenberg_carrier_section.tex').read_bytes()).hexdigest(),
        'numerical':numerical,
        'symbolic_natural_dimension':8,
        'symbolic_checks':['Heisenberg symplectic identity','Heisenberg group law',
            'exact lambda-twisted conjugation','symmetric shear symplectic identity',
            'both quadratic multiplier involutions','explicit nonzero minus-one shears'],
        'F9':{'scalar_repairs':64,'dual_weights':729,'fixed_dual_weights':27,
              'nontrivial_dual_orbits':351,'trace_pairings':81},
        'limits':'The written proof establishes all fields/ranks, quadratic-form existence and actual period factorization. This finite certificate does not replace those arguments.',
        'seconds':round(time.perf_counter()-start,6)
    }
    (B/'check_higher_odd_symplectic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
