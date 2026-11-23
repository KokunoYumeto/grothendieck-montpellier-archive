#!/usr/bin/env python3
"""HD-D03: small unit-assisted integral Weil projectors, exact certificates.
GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds; 2026-11-21.
Uses the independent integer quadratic ring in quadratic_projector_constants.
All coefficients, spectral values, masses and ceilings are computed exactly.
"""
from pathlib import Path
from math import factorial
import json
from quadratic_projector_constants import Quadratic, ceil_fraction, ceil_sqrt_fraction

def add(*ops):
    out={}
    for op in ops:
        for a,c in op.items(): out[a]=out.get(a,0)+c
    return {a:c for a,c in out.items() if c}
def scale(k,op): return {a:k*c for a,c in op.items() if k*c}
def mul(ring,*ops):
    out={(1,0):1}
    for op in ops:
        temp={}
        for a,c in out.items():
            for b,d in op.items():
                z=ring.mul(a,b); temp[z]=temp.get(z,0)+c*d
        out={a:c for a,c in temp.items() if c}
    return out
def endo(a): return {a:1}
def eig(ring,op,n,j):
    ans=(0,0)
    for a,c in op.items():
        val=ring.mul(ring.pow(a,j),ring.pow(ring.conj(a),2*n-j))
        ans=ring.add(ans,(c*val[0],c*val[1]))
    return ans
def nm(ring,a):
    z=ring.mul(a,ring.conj(a))
    assert z[1]==0 and z[0]>0
    return z[0]
def terms(ring,op,n):
    return [dict(a=list(a),coefficient=c,norm=nm(ring,a),
                 degree_factor=nm(ring,a)**n) for a,c in sorted(op.items())]
def verify(label,ring,n,P,R,Z,s,extra=None):
    vals=[eig(ring,P,n,j) for j in range(2*n+1)]
    assert vals==[(R,0)]+[(0,0)]*(2*n-1)+[(R,0)]
    zvals=[eig(ring,Z,n,j) for j in (0,2*n)]
    assert zvals[1]==ring.conj(zvals[0])
    assert ring.add(zvals[0],zvals[1])==(0,0)
    assert ring.mul(zvals[0],zvals[0])==(-s,0)
    mp=sum(c*nm(ring,a)**n for a,c in P.items() if c>0)
    mm=sum(-c*nm(ring,a)**n for a,c in P.items() if c<0)
    assert mp==mm and mp>0
    L=sum(abs(c)*nm(ring,a)**n for a,c in Z.items())
    nf=factorial(n)
    A0=ceil_fraction(s*R*R,nf*nf)
    squared=(mp*R)**2*s*(s+L*L)
    A1=ceil_sqrt_fraction(squared,nf)
    assert A1>=A0
    out=dict(label=label,n=n,R=R,m=mp,s=s,L=L,A0=A0,A1=A1,
             P_terms=terms(ring,P,n),rotation_terms=terms(ring,Z,n),
             all_P_eigenvalues=[list(v) for v in vals],
             endpoint_rotation_eigenvalues=[list(v) for v in zvals],
             A1_integer_witness=dict(lower=((A1-1)*nf)**2,
                                    squared_numerator=squared,upper=(A1*nf)**2),
             bound="c_t <= A1*delta*ceil(sqrt(T))*D^2")
    if extra is not None: out["intermediate_spectra"]=extra
    return out

def main():
    i=Quadratic(0,-1); w=Quadratic(-1,-1)
    one=endo((1,0))
    I=endo((0,1)); A=endo((2,1)); Ac=endo((2,-1))
    Pi=mul(i,add(one,scale(-1,I)),
            add(scale(150,one),scale(-1,A),scale(-1,Ac)))
    ci=verify("n3_gaussian",i,3,Pi,768,endo((1,1)),64)
    Om=endo((0,1)); Om2=endo((-1,-1))
    B=endo((1,-1)); Aa=endo((3,1)); Aac=endo((2,-1))
    P3=mul(w,add(one,Om,Om2),add(scale(27,one),scale(-1,B)))
    c3=verify("n3_eisenstein",w,3,P3,162,add(Aa,scale(143,one)),97200)
    E=add(scale(2,one),scale(-1,Om),scale(-1,Om2))
    H=add(one,scale(-2,Om),Om2)
    P2=add(scale(9,E),scale(-1,mul(w,H,B)))
    c2=verify("n2_eisenstein",w,2,P2,54,add(Om,scale(-1,Om2)),3)
    F=add(scale(81,E),scale(-1,mul(w,H,B)))
    P4=mul(w,F,add(scale(1127,one),scale(-1,Aa),scale(-1,Aac)))
    # Independent check of the cohomological reduction:
    # bar(B) = (-omega^2)*(1-omega), and [-1]^* is +1 on H^8.
    Bc=endo(w.conj((1,-1)))
    Fraw=mul(w,E,add(scale(81,one),scale(-1,B),scale(-1,Bc)))
    assert all(eig(w,F,4,j)==eig(w,Fraw,4,j) for j in range(9))
    Fp=sum(c*nm(w,a)**4 for a,c in F.items() if c>0)
    Fm=sum(-c*nm(w,a)**4 for a,c in F.items() if c<0)
    assert Fp==Fm==324
    Frawp=sum(c*nm(w,a)**4 for a,c in Fraw.items() if c>0)
    Frawm=sum(-c*nm(w,a)**4 for a,c in Fraw.items() if c<0)
    assert Frawp==Frawm==486
    extra=dict(E=[list(eig(w,E,4,j)) for j in range(9)],
               F=[list(eig(w,F,4,j)) for j in range(9)],
               reduced_F_positive_mass=Fp,reduced_F_negative_mass=Fm,
               raw_F_positive_mass=Frawp,raw_F_negative_mass=Frawm,
               reduced_F_terms=terms(w,F,4))
    c4=verify("n4_eisenstein",w,4,P4,2624400,add(Om,scale(-1,Om2)),3,extra)
    seven=Quadratic(-1,-2)
    A7=endo((0,1)); A7c=endo((-1,-1))
    P7=add(scale(384,one),scale(-8,add(A7,A7c)),
           scale(6,add(mul(seven,A7,A7),mul(seven,A7c,A7c))),
           scale(-1,add(mul(seven,A7,A7,A7),mul(seven,A7c,A7c,A7c))))
    c7=verify("n3_discriminant_minus7",seven,3,P7,1029,
              add(scale(2,A7),scale(-9,one)),175)
    P72=add(scale(16,one),scale(2,add(A7,A7c)),
            scale(-1,add(mul(seven,A7,A7),mul(seven,A7c,A7c))))
    c72=verify("n2_discriminant_minus7",seven,2,P72,49,
               add(scale(2,A7),scale(-1,one)),63)
    out=dict(statement="HD-D03",date="2026-11-21",
             author="GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds",
             scope="integral maximal-order actions for discriminants -4,-3,-7",
             cases=[c2,ci,c3,c4,c7,c72])
    path=Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    for c in out["cases"]:
        print(c["label"],{k:c[k] for k in ("R","m","s","L","A0","A1")})
    print("PASS all exact spectra, rotations, signed masses, and ceiling witnesses")
    print("Saved",path)
if __name__=="__main__":main()

