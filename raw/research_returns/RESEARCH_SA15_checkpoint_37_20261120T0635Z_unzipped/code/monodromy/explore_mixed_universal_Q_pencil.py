#!/usr/bin/env python3
"""A symbolic sharp simple-Hasse point for every ordinary mixed modulus.
Exploratory local calculation; no fixed-modulus full group conclusion.
"""
import json,time
from pathlib import Path
import sympy as sp
from sympy.polys.matrices import DomainMatrix
started=time.perf_counter()
a,z=sp.symbols('a z');u=sp.symbols('u0:3')
Mo=sp.Matrix([[u[0],a*u[2],a*u[1]],[u[2],u[1],u[0]],[0,u[2],u[1]+u[2]]])
Ms=sp.Matrix([[u[1],u[0],0],[u[2],0,u[0]],[0,u[2],u[1]]])
Ro=sp.Matrix([[1,0,a],[0,0,a],[0,a,a]])
J=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
R=sp.kronecker_product(Ro,J)
coeff=[sp.kronecker_product(Mo.diff(u[i]),Ms.diff(u[j])) for i in range(3) for j in range(3)]
K=sp.GF(2).frac_field(a,z)
def red(e):return K.to_sympy(K.from_sympy(e))
point=sp.Matrix([z**3/a,z,0,0,1,0,0,0,1])
M=sum((point[i]*coeff[i] for i in range(9)),sp.zeros(9))
rhs=point.applyfunc(lambda v:v*v)
Q=red((point.T*R*rhs)[0]);assert Q==0
assert red(sp.Matrix(3,3,list(point)).det())==z**3/a
aug=M[:,1:].row_join(rhs)
rr,piv=DomainMatrix.from_Matrix(aug).convert_to(K).rref()
assert piv==tuple(range(8))
rm=rr.to_Matrix();w=sp.Matrix([0]+[rm[i,8] for i in range(8)])
assert all(red(v)==0 for v in M*w-rhs)
pairing=red((point.T*R*w.applyfunc(lambda v:v*v))[0])
out=dict(status='PASS',scope='Exact symbolic point on Q, full Cartier rank8 and first relative stability obstruction; no monodromy claim.',
         point=[str(v) for v in point],determinant='z^3/a',Q=str(Q),
         kernel_lift=[str(v) for v in w],stable_pairing=str(pairing),
         runtime_seconds=time.perf_counter()-started)
Path(__file__).resolve().parents[1].joinpath('outputs/explore_mixed_universal_Q_pencil.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
