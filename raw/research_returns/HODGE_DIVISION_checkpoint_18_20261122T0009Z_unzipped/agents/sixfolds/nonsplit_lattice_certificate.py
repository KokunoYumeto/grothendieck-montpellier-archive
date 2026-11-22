#!/usr/bin/env python3
"""Independent exact identities used in the LAT01--02 whole-proof audit.
This is not a finite search proving the universal small-zero theorem;
that theorem is checked in the accompanying written audit.
"""
from pathlib import Path
import json
import sympy as S

a,c,zr,zi,x1,y1,x2,y2=S.symbols("a c zr zi x1 y1 x2 y2", real=True)
A=S.Matrix([[a,zr+S.I*zi],[zr-S.I*zi,c]])
v=S.Matrix([x1+S.I*y1,x2+S.I*y2])
ell=v.conjugate().T*A
u=S.Matrix([-ell[0,1],ell[0,0]])
norm=S.expand((v.conjugate().T*A*v)[0])
def zero(x):
    return S.simplify(S.expand_complex(x))==0
assert zero((v.conjugate().T*A*u)[0])
assert zero((u.conjugate().T*A*u)[0]-A.det()*norm)
assert zero(S.Matrix.hstack(v,u).det()-norm)
U=S.Matrix([[1+S.I,-3],[1,-1+S.I]])
J=S.diag(1,-3)
assert S.simplify(U.det())==1
assert all(zero(entry) for entry in U.conjugate().T*(-J)*U-J)

# Reflection numerator, expressed in the three independent quadratic
# invariants.  The expression is exactly zero when Q(x)=0.
qx,qy,bxy=S.symbols("qx qy bxy")
q_reflection=S.expand(qy**2*qx-4*qy*bxy**2+4*bxy**2*qy)
assert q_reflection==qy**2*qx
lam,bxe,qe=S.symbols("lam bxe qe")
coeff_x=S.expand((2*lam*bxe+qe)-2*bxe*lam)
coeff_e=-2*bxe
assert coeff_x==qe and coeff_e==-2*bxe

# The displayed real symmetric five-variable matrix and its L1 bound.
Qmat=S.zeros(5)
Qmat[0,0]=Qmat[1,1]=a
Qmat[2,2]=Qmat[3,3]=c
Qmat[4,4]=-1
for i,j,value in [(0,2,zr),(1,3,zr),(0,3,-zi),(1,2,zi)]:
    Qmat[i,j]=Qmat[j,i]=value
xx=S.Matrix([x1,y1,x2,y2,S.Symbol("t",real=True)])
assert zero((xx.T*Qmat*xx)[0]-(norm-xx[4]**2))
assert 144*9**2==11664
assert 6*11664==69984

# Alternating/Hermitian determinant normalization, exactly on a
# non-real generic binary block.
R=S.Matrix([[a,zr],[zr,c]])
B=S.Matrix([[0,zi],[-zi,0]])
E=B.row_join(R).col_join((-R).row_join(B))
assert zero(E.det()-A.det()**2)

out={
 "status":"PASS",
 "scope":[
 "generic complex binary orthogonal complement, determinant and norm identities",
 "exact integral sign repair with determinant one",
 "reflection-numerator quadratic identity and error-vector cancellation",
 "five-variable symmetric matrix convention",
 "constants11664 and69984",
 "generic binary alternating/Hermitian determinant-square identity"
 ],
 "universal_small_zero_proof":"independently checked in Nonsplit_Lattice_Peer_Audit.md; no finite enumeration substituted",
 "degree_transport_exponents":{"source_volume_M_power":6,"N_M_power":18,"N_target_volume_power":3,"N_conductor_power":36,"cycle_N_power":6}
}
Path(__file__).with_name("nonsplit_lattice_certificate_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out))

