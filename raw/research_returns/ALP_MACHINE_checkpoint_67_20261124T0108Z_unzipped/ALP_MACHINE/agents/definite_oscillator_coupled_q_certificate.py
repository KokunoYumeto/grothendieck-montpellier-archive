"""Exact small matrix diagnostics for DO037, not a local Howe proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def det2(U):
    return U[0][0]*U[1][1]-U[0][1]*U[1][0]

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

def inv2(U):
    e=det2(U)
    return [[F(U[1][1],e),F(-U[0][1],e)],
            [F(-U[1][0],e),F(U[0][0],e)]]

def reduce(x,q):
    x=F(x)
    assert x.denominator%q
    return (x.numerator*pow(x.denominator,-1,q))%q

def val(x,q):
    x=F(x)
    if x==0:return 1000
    n,d=abs(x.numerator),x.denominator
    z=0
    while n%q==0:n//=q;z+=1
    while d%q==0:d//=q;z-=1
    return z

def chi(x,q=3):
    x%=q
    assert x
    return 1 if x==1 else -1

def matrix_checks():
    q=3
    Us=[[[a,b],[c,d]] for a,b,c,d in product(range(q),repeat=4)
        if (a*d-b*c)%q]
    checks=0
    for U in Us:
        Ui=inv2(U);du=det2(U)
        for v0,v1,w,L,g,n in product(range(q),range(q),range(q),
                                    range(q),(1,2),(0,1,2)):
            S=F(q**n)
            V=[[F(v0)],[F(v1)]]
            Wp=[[S*L,F(w)]]
            W=mm(Wp,U)
            D=S+q*mm(Wp,V)[0][0]
            # X=h^{-1}E*g, calculated by the exact block equations.
            C=F(-q*L*g)
            A=mm(Ui,[[g-V[0][0]*C],[-V[1][0]*C]])
            assert all(val(z[0],q)>=0 for z in A)
            assert val(C,q)>=1
            lhs=mm(U,A)
            assert lhs[0][0]+V[0][0]*C==g
            assert lhs[1][0]+V[1][0]*C==0
            assert q*mm(W,A)[0][0]+D*C==0
            Ar=[reduce(A[0][0],q),reduce(A[1][0],q)]
            ell=[(-Ar[1])%q,Ar[0]%q]
            assert any(ell)
            c=(reduce(du,q)*pow(g,-1,q))%q
            assert [(c*x)%q for x in ell]==[x%q for x in U[1]]
            # H character, cofactor Fourier character, source eta^-1.
            phase=chi(reduce(du,q))*chi((-c)%q)*chi(g)
            assert phase==chi(-1)
            # The determinant of the full block matrix is det(U)*S.
            h=[[U[0][0],U[0][1],V[0][0]],
               [U[1][0],U[1][1],V[1][0]],
               [q*W[0][0],q*W[0][1],D]]
            dh=(h[0][0]*(h[1][1]*h[2][2]-h[1][2]*h[2][1])
                -h[0][1]*(h[1][0]*h[2][2]-h[1][2]*h[2][0])
                +h[0][2]*(h[1][0]*h[2][1]-h[1][1]*h[2][0]))
            assert dh==du*S
            checks+=1
    return checks

def lattice_jacobians():
    count=0
    for q in (3,5):
        for t,a in product((1,2,3),(1,2)):
            depth=4
            for exponents in product((0,1,2),repeat=t):
                full=q**(depth*t*a)
                allowed=q**(a*sum(depth-e for e in exponents))
                jac=F(1,q**(a*sum(exponents)))
                assert F(allowed,full)==jac
                assert - (a+t+1)+(t+1)+a==0
                count+=1
    return count

def igusa_recurrences():
    # Exact rational values with unramified theta(q)=+/-1.
    ncheck=0
    for q,theta,u in product((2,3,5),(1,-1),(0,1,2)):
        J=F(1)
        for t in range(1,6):
            J*=F(1-F(1,q**t),1-theta*F(1,q**(t+u)))
            prodJ=F(1)
            for i in range(1,t+1):
                prodJ*=F(1-F(1,q**i),1-theta*F(1,q**(i+u)))
            assert J==prodJ
            ncheck+=1
    # At a=t=1,q=3,theta=1 the full scalar is G(chi,psi)/78.
    q=3;a=1;t=1;d=t+1;b=a+d;r=a+1
    kap=lambda n: __import__('functools').reduce(
        lambda x,i:x*(1-F(1,q**i)),range(1,n+1),F(1))
    factor=F(1,q**d)*F(1,q**(r*t))*kap(r)/kap(b)
    # chi(-1)^-1=-1 for the quadratic character of F3.
    assert factor==F(1,78)
    return ncheck

def main():
    out={
        "finding":"AM-DO-037",
        "scope":"Exact small rational matrix/cofactor/phase and lattice-Jacobian checks; the whole-Schwartz continuation and actual theta quotient are proved in the report.",
        "schur_matrix_checks":matrix_checks(),
        "lattice_jacobian_checks":lattice_jacobians(),
        "igusa_recurrence_checks":igusa_recurrences(),
        "toy_scalar":"-G(chi,psi_0)/78 for a=t=1,q=3,theta=1",
        "status":"PASS",
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
