#!/usr/bin/env python3
"""Exact projector and quadratic extraction constants for HD-D01.

GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds; 2026-11-21.
All field arithmetic, polynomial arithmetic, ceilings, and certificates use
integers/rationals. No floating-point or decimal radical evaluation occurs.
This is a symbolic computation certificate, not a proof-assistant verification.
"""
from pathlib import Path
from math import factorial, gcd, isqrt
from functools import reduce
import json
import sympy as sp

X=sp.Symbol("X")

class Quadratic:
    """Integer ring Z[b], b^2 = u*b+v."""
    def __init__(self,u,v): self.u,self.v=u,v
    def add(self,a,b): return a[0]+b[0],a[1]+b[1]
    def neg(self,a): return -a[0],-a[1]
    def mul(self,a,b):
        x,y=a; z,w=b
        return x*z+self.v*y*w,x*w+y*z+self.u*y*w
    def conj(self,a): return a[0]+self.u*a[1],-a[1]
    def pow(self,a,n):
        out=(1,0)
        while n:
            if n&1: out=self.mul(out,a)
            a=self.mul(a,a); n//=2
        return out
    def poly_roots(self,roots):
        out=[(1,0)]
        for r in roots:
            new=[(0,0)]*(len(out)+1)
            for j,c in enumerate(out):
                new[j]=self.add(new[j],self.neg(self.mul(r,c)))
                new[j+1]=self.add(new[j+1],c)
            out=new
        assert all(c[1]==0 for c in out)
        return sp.Poly(sum(c[0]*X**j for j,c in enumerate(out)),X,domain=sp.ZZ)
    def evaluate(self,coeffs,z):
        out=(0,0)
        for c in reversed(coeffs): out=self.add(self.mul(out,z),(int(c),0))
        return out

def ceil_fraction(a,b):
    assert a>=0 and b>0
    return (a+b-1)//b

def ceil_sqrt_fraction(a,b):
    """Least k >= 0 with (k*b)^2 >= a; no floating arithmetic."""
    assert a>=0 and b>0
    k=isqrt(a)//b
    if (k*b)**2 < a: k+=1
    assert (k*b)**2>=a
    assert k==0 or ((k-1)*b)**2<a
    return k

def case(label,u,v,a,n):
    ring=Quadratic(u,v); abar=ring.conj(a)
    Nm=ring.mul(a,abar)
    assert Nm[1]==0 and Nm[0]>0
    Nm=Nm[0]; Q=Nm**n
    eigen=[ring.mul(ring.pow(a,j),ring.pow(abar,2*n-j)) for j in range(2*n+1)]
    f=ring.poly_roots([eigen[0],eigen[-1]])
    g=ring.poly_roots(eigen[1:-1])
    signed_R=int(sp.resultant(f.as_expr(),g.as_expr(),X))
    assert signed_R!=0
    R=abs(signed_R)
    bezout_u,bezout_v,bezout_one=sp.gcdex(f,g)
    assert bezout_one==1
    scaled_u=sp.Poly(bezout_u.as_expr()*R,X)
    scaled_v=sp.Poly(bezout_v.as_expr()*R,X)
    assert all(sp.Rational(c).q==1 for c in scaled_u.all_coeffs()+scaled_v.all_coeffs())
    assert sp.expand(scaled_u.as_expr()*f.as_expr()+scaled_v.as_expr()*g.as_expr())==R
    P=sp.Poly(scaled_v.as_expr()*g.as_expr(),X,domain=sp.ZZ)
    coeffs=[int(P.nth(j)) for j in range(P.degree()+1)]
    common_gcd=reduce(gcd,[R]+[abs(c) for c in coeffs])
    a2n=ring.pow(a,2*n); abar2n=ring.conj(a2n)
    rr=ring.add(a2n,abar2n)
    assert rr[1]==0
    r=rr[0]; s=4*Q*Q-r*r; L=2*Q+abs(r)
    assert s>0
    assert ring.mul(a2n,abar2n)==(Q*Q,0)
    B=ring.add((2*a2n[0],2*a2n[1]),(-r,0))
    assert ring.mul(B,B)==(-s,0)
    nf=factorial(n)
    variants={}
    for name,divisor in [("resultant",1),("primitive_integral",common_gcd)]:
        RV=R//divisor; cv=[c//divisor for c in coeffs]
        assert all(c%divisor==0 for c in coeffs) and R%divisor==0
        evaluations=[ring.evaluate(cv,z) for z in eigen]
        assert evaluations==[(RV,0)]+[(0,0)]*(2*n-1)+[(RV,0)]
        middle=sum(c*Q**j for j,c in enumerate(cv))
        assert middle==0
        m=sum(c*Q**j for j,c in enumerate(cv) if c>0)
        mminus=sum(-c*Q**j for j,c in enumerate(cv) if c<0)
        assert m==mminus and m>0
        numerator0=s*RV**2
        A0=ceil_fraction(numerator0,nf**2)
        numerator1=(m*RV)**2*s*(s+L**2)
        A1=ceil_sqrt_fraction(numerator1,nf)
        assert (A0-1)*nf**2<numerator0<=A0*nf**2
        assert ((A1-1)*nf)**2<numerator1<=(A1*nf)**2
        variants[name]=dict(
            R=RV,coefficients_ascending=cv,m=m,kappa=2*m,
            A0=A0,A1=A1,
            A0_integer_witness=dict(numerator=numerator0,denominator=nf**2,
                                   lower=(A0-1)*nf**2,upper=A0*nf**2),
            A1_integer_witness=dict(squared_numerator=numerator1,denominator=nf,
                                   lower=((A1-1)*nf)**2,upper=(A1*nf)**2),
            spectral_checks=[list(z) for z in evaluations],
            weighted_negative_part=mminus,weighted_sum=middle)
    return dict(label=label,n=n,ring_relation=dict(u=u,v=v),a=list(a),
                norm=Nm,Q=Q,r=r,s=s,L=L,
                f_coefficients_ascending=[int(f.nth(j)) for j in range(f.degree()+1)],
                g_coefficients_ascending=[int(g.nth(j)) for j in range(g.degree()+1)],
                resultant_signed=signed_R,primitive_divisor=common_gcd,
                eigenvalues=[list(z) for z in eigen],variants=variants)

def main():
    cases=[case("n3_gaussian_a_2_plus_i",0,-1,(2,1),3),
           case("n3_eisenstein_a_3_plus_omega",-1,-1,(3,1),3),
           case("n4_eisenstein_a_3_plus_omega",-1,-1,(3,1),4)]
    out=dict(statement="HD-D01",date="2026-11-21",
             author="GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds",
             arithmetic="integer and rational only; independently rebuilt quadratic ring",
             ceil_A1="least integer k >= 0 satisfying (k*n!)^2 >= (m*R)^2*s*(s+L^2)",
             cases=cases)
    path=Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(out,indent=2)+"\n")
    for c in cases:
        print(c["label"])
        print(" Q,r,s,L =",c["Q"],c["r"],c["s"],c["L"])
        print(" primitive divisor =",c["primitive_divisor"])
        for name,vv in c["variants"].items():
            print(" ",name)
            for key in ("R","m","A0","A1"):
                print("  ",key,"=",vv[key])
    print("PASS exact spectral substitutions, equal signed parts, B^2=-s, and both minimal ceiling witnesses")
    print("Saved",path)

if __name__=="__main__": main()

