#!/usr/bin/env python3
"""Exact small symmetric-projector constants for the six remaining fields.
HD-D04, 2026-11-21, GPT-6 Astra Pro, inherited effort not exposed.
All calculations use integers/rationals and exact radical-ceiling witnesses.
"""
from pathlib import Path
from math import gcd,prod
import json
import sympy as sp
from quadratic_projector_constants import Quadratic
from small_weil_projectors import add,scale,mul,endo,verify,nm

def make(d,n=3):
    if d==2:
        ring=Quadratic(0,-2);a=(1,1);basis="sqrt(-2)";aname="1+sqrt(-2)"
    else:
        ring=Quadratic(1,-(d+1)//4);a=(0,1)
        basis=f"(1+sqrt(-{d}))/2";aname=basis
    abar=ring.conj(a);N=nm(ring,a);Q=N**n
    tr=lambda z:ring.add(z,ring.conj(z))[0]
    sj=[N**j*tr(ring.pow(a,2*n-2*j)) for j in range(n+1)]
    assert len(set(sj))==n+1 and sj[-1]==2*Q
    X=sp.Symbol("X")
    polynomial=sp.Poly(prod(X-sj[j] for j in range(1,n+1)),X)
    R=prod(sj[0]-sj[j] for j in range(1,n+1))
    if R<0: R=-R;polynomial=-polynomial
    c=[int(polynomial.nth(j)) for j in range(4)]
    p=[c[0]+2*Q*Q*c[2],c[1]+3*Q*Q*c[3],c[2],c[3]]
    assert gcd(R,gcd(abs(p[0]),gcd(abs(p[1]),gcd(abs(p[2]),abs(p[3])))))==1
    P=scale(p[0],endo((1,0)))
    for j in (1,2,3):
        P=add(P,scale(p[j],add(endo(ring.pow(a,j)),endo(ring.pow(abar,j)))))
    common=gcd(2,abs(sj[0]))
    zA=2//common;z0=-sj[0]//common
    Z=add(scale(zA,endo(a)),scale(z0,endo((1,0))))
    sval=(4*Q*Q-sj[0]*sj[0])//(common*common)
    out=verify(f"n{n}_Qsqrt_minus_{d}",ring,n,P,R,Z,sval)
    out.update(squarefree_d=d,basis=basis,a=aname,a_coordinates=list(a),norm_a=N,
               half_spectrum=sj,polynomial_in_S_coefficients_ascending=c,
               reduced_operator_coefficients_p0_p1_p2_p3=p,
               polynomial_reduction=f"S²=A²+Abar²+2Q²; S³=A³+Abar³+3Q²S onH{2*n}",
               rotation_coefficient_A=zA,rotation_constant=z0,
               conductor_extraction_exponent=8*n,
               gcd_reduction=1,
               non_root_reason="a/bar(a) has nonintegral coordinates in the displayed maximal-order integral basis")
    ratio_num=ring.pow(a,2)
    assert any(x%N for x in ratio_num)
    out["a_over_abar_coordinates"]=[str(sp.Rational(x,N)) for x in ratio_num]
    return out

def main():
    cases=[make(d,n) for n in [3,2] for d in [2,11,19,43,67,163]]
    output=dict(statement="HD-D04",date="2026-11-21",
                author="GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds",
                arithmetic="exact integer quadratic pairs, rational coefficients, integer ceilings",
                convention="A=[a]^* onH^(2n); S=A+Abar; P=p0+p1(A+Abar)+p2(A²+Abar²)+p3(A³+Abar³); p3=0 for n2",
                cases=cases)
    p=Path(__file__).with_suffix(".json");p.write_text(json.dumps(output,indent=2)+"\n")
    for c in cases:
        print("n",c["n"],"d",c["squarefree_d"],"a",c["a"])
        for key in ["norm_a","half_spectrum","reduced_operator_coefficients_p0_p1_p2_p3","R","m","s","L","A0","A1"]:
            print(" ",key,c[key])
    print("PASS all seven eigenvalues, primitive integer numerator, equal signed parts, skew rotation, nonroot ratios, exact ceilings")
    print("Saved",p)
if __name__=="__main__": main()

