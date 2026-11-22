#!/usr/bin/env python3
"""Exact identity checks for D-E8-LAT-01/02, not a substitute for its proof.

Verifies the binary complement identities symbolically, sign repair, and
both denominator directions for twelve exact block examples, including
large integral shears. The small-zero/existence argument is a proof check,
not a search over all lattices or a numerical assertion from these examples.
"""
from pathlib import Path
import json,time
import sympy as S
HERE=Path(__file__).resolve().parent;start=time.monotonic();ii=S.I
def star(A):return A.conjugate().T
def integral(A):return all(S.re(S.expand(x)).is_Integer and S.im(S.expand(x)).is_Integer for x in A)
def simplify(A):return A.applyfunc(S.simplify)
a,c,b0,b1,p0,p1,q0,q1=S.symbols('a c b0 b1 p0 p1 q0 q1',real=True)
A=S.Matrix([[a,b0+ii*b1],[b0-ii*b1,c]])
v=S.Matrix([p0+ii*p1,q0+ii*q1]);ell=star(v)*A;u=S.Matrix([-ell[0,1],ell[0,0]])
n=(star(v)*A*v)[0];B=v.row_join(u)
assert S.expand((star(v)*A*u)[0])==0
assert S.expand((star(u)*A*u)[0]-A.det()*n)==0
assert S.expand(B.det()-n)==0
J3=S.diag(1,-3);U=S.Matrix([[1+ii,-3],[1,-1+ii]])
assert U.det()==1 and simplify(star(U)*(-J3)*U)==J3 and integral(U.inv())
Z=S.zeros(2);I2=S.eye(2)
H0=Z.row_join(I2).row_join(Z).col_join(I2.row_join(Z).row_join(Z)).col_join(Z.row_join(Z).row_join(J3))
examples=[]
for k in range(1,13):
    P=S.Matrix([[k+1,1+ii],[1,k+2-ii]])
    # An arbitrarily large integral shear has no effect on determinant denominators.
    P=P*S.Matrix([[1,10**k+ii*(10**k-1)],[0,1]])
    A=star(P)*J3*P;d=int(-S.expand(A.det()));assert d>0
    beta=3*S.expand(P.det());assert S.expand(beta*S.conjugate(beta))==3*d
    vv=simplify(P.inv()*S.Matrix([1,0]));tt=int(S.expand(P.det()*S.conjugate(P.det())))
    assert integral(tt*vv) and (star(vv)*A*vv)[0].simplify()==1
    ell=simplify(star(vv)*A);uu=S.Matrix([-ell[0,1],ell[0,0]])
    TA=simplify(vv.row_join(uu*S.conjugate(beta)/d))
    assert simplify(star(TA)*A*TA)==J3
    qa=3*d*tt
    assert integral(qa*TA) and integral(qa*TA.inv())
    BB=S.diag(k+ii,k+1-2*ii);nb=int(S.expand(BB.det()*S.conjugate(BB.det())))
    F=S.Matrix([[2*k,3*k+ii],[3*k-ii,-k]])
    E=S.Matrix([[10**k+ii,k-ii],[2-k*ii,-3]])
    H=Z.row_join(BB).row_join(Z).col_join(star(BB).row_join(F).row_join(E)).col_join(Z.row_join(star(E)).row_join(A))
    Delta=int(-S.expand(H.det()));assert Delta==nb*d
    TH=I2.row_join(-star(BB).inv()*F*BB.inv()/2).row_join(-star(BB).inv()*E).col_join(Z.row_join(BB.inv()).row_join(Z)).col_join(Z.row_join(Z).row_join(I2))
    TH=simplify(TH)
    HA=Z.row_join(I2).row_join(Z).col_join(I2.row_join(Z).row_join(Z)).col_join(Z.row_join(Z).row_join(A))
    assert simplify(star(TH)*H*TH-HA)==S.zeros(6)
    qh=2*nb
    assert integral(qh*TH) and integral(qh*TH.inv())
    T=simplify(TH*S.diag(S.eye(4),TA));q=qh*qa
    assert q==6*Delta*tt and tt<=11664*d*d and q<=69984*Delta**3
    assert simplify(star(T)*H*T)==H0
    assert integral(q*T) and integral(q*T.inv())
    examples.append({'example':k,'residual_d':d,'pairing_norm':nb,'Delta':Delta,'t':tt,'clearing_integer':q,'bound':69984*Delta**3,'both_directions':True})
assert 6*144*9**2==69984
out={'status':'PASS','symbolic_binary_complement':True,'symbolic_complement_determinant':True,
     'integral_sign_repair':True,'exact_block_examples':examples,'all_two_sided_inclusions':True,
     'constant_identity':'6*144*9^2=69984','source_projector_denominator':'M=2|G| (safe bound)',
     'scope':'Symbolic identities and exact denominator examples; Landherr, Gaussian reduction and minimum-zero descent are separately proved in the TeX',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'check_nonsplit_lattice.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='exact_block_examples'}))
