#!/usr/bin/env python3
"""Universal all-nine Pfaffian identities for every ordinary mixed product.
The second part explores a symbolic point on the simple Q component.
"""
import json,time
from pathlib import Path
from functools import lru_cache
import sympy as sp
from sympy.polys.matrices import DomainMatrix
started=time.perf_counter()
a,z=sp.symbols('a z');u=sp.symbols('u0:3');s=sp.symbols('s0:9')
variables=(a,)+s
Mo=sp.Matrix([[u[0],a*u[2],a*u[1]],[u[2],u[1],u[0]],[0,u[2],u[1]+u[2]]])
Ms=sp.Matrix([[u[1],u[0],0],[u[2],0,u[0]],[0,u[2],u[1]]])
Ro=sp.Matrix([[1,0,a],[0,0,a],[0,a,a]])
J=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
R=sp.kronecker_product(Ro,J)
coeff=[sp.kronecker_product(Mo.diff(u[i]),Ms.diff(u[j]))
       for i in range(3) for j in range(3)]
M=sum((s[i]*coeff[i] for i in range(9)),sp.zeros(9))
def md(e):return sp.Poly(sp.expand(e),*variables,modulus=2).as_expr()
A=(R*M).applyfunc(md)
assert (A-A.T).applyfunc(md)==sp.zeros(9)
assert all(A[i,i]==0 for i in range(9))
assert (M*sp.Matrix(s)).applyfunc(md)==sp.zeros(9,1)
D=md(sp.Matrix(3,3,s).det())
@lru_cache(None)
def pf(t):
    if not t:return sp.Integer(1)
    i=t[0]
    return md(sum(A[i,j]*pf(t[1:k]+t[k+1:]) for k,j in enumerate(t[1:],1)))
for i in range(9):
    assert md(pf(tuple(j for j in range(9) if j!=i))-a**3*D*s[i])==0
assert md(R.det()-a**6)==0
Q=md((sp.Matrix([v*v for v in s]).T*R*sp.Matrix(s))[0])
assert all(md(sp.diff(Q,s[i])-(R.T*sp.Matrix([v*v for v in s]))[i])==0
           for i in range(9))
rank_one={v:0 for v in s};rank_one[s[1]]=1
assert md(D.subs(rank_one))==0 and md(Q.subs(rank_one))==1

# A deliberately simple symbolic Q-point.  Retain its outcome even if the
# stable-loss test vanishes: it is an exploration, not the general theorem.
point=[1,0,0,0,z,0,0,0,1]
Mp=sum((point[i]*coeff[i] for i in range(9)),sp.zeros(9))
rhs=sp.Matrix([v*v if not isinstance(v,int) else v for v in point])
K=sp.GF(2).frac_field(a,z)
aug=Mp[:,1:].row_join(rhs)
dm=DomainMatrix.from_Matrix(aug).convert_to(K)
rr,piv=dm.rref();rrm=rr.to_Matrix()
assert piv==tuple(range(8))
w=sp.Matrix([0]+[rrm[i,8] for i in range(8)])
def redrat(e):return K.to_sympy(K.from_sympy(e))
assert all(redrat(v)==0 for v in Mp*w-rhs)
L=redrat((sp.Matrix(point).T*R.T*sp.Matrix([v*v for v in w]))[0])
out=dict(status='PASS',scope='Universal all-nine Pfaffians and one retained symbolic Q-point; no fixed-modulus group assertion.',
         pfaffian_vector='a^3 det(S) s',det_R='a^6',relative_Hasse='det(S)^2 (s^[2])^t R s',
         Q=str(Q),point=[str(v) for v in point],kernel_lift=[str(v) for v in w],
         stable_loss_pairing=str(L),runtime_seconds=time.perf_counter()-started)
Path(__file__).resolve().parents[1].joinpath('outputs/verify_mixed_degree_one_pfaffians.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
