#!/usr/bin/env python3
"""Exact characteristic-two polynomial identities for any ordinary elliptic pair.
No numerical specialization replaces the universal polynomial calculation.
"""
import json,time,itertools
from pathlib import Path
import sympy as sp
started=time.perf_counter()
A,B,C,D,x,y,z=sp.symbols('A B C D x y z')
vars=(A,B,C,D,x,y,z)
def mod2(e):return sp.Poly(sp.expand(e),*vars,modulus=2).as_expr()
def matmod(M):return M.applyfunc(mod2)
M=sp.Matrix([[x,B*z,B*y],[z,y+A*z,x+A*y],[0,z,y+z]])
R=sp.Matrix([[1,0,B],[0,0,B],[0,B,(1+A)*B]])
S=matmod(R*M)
assert matmod(S-S.T)==sp.zeros(3)
assert mod2(R.det()-B**2)==0
assert matmod(sp.Matrix([S[i,i] for i in range(3)])-R.T*sp.Matrix([x,y,z]))==sp.zeros(3,1)
Ms=[M.diff(t) for t in (x,y,z)]
for i,U in enumerate(Ms):
 for j in range(3):assert U[:,j]==Ms[j][:,i]
 assert U[:,i]==sp.eye(3)[:,i]
R2=R.subs({A:C,B:D});Ms2=[U.subs({A:C,B:D}) for U in Ms]
RT=sp.kronecker_product(R,R2)
for i,j in itertools.product(range(3),repeat=2):
 T=matmod(RT*sp.kronecker_product(Ms[i],Ms2[j]))
 assert matmod(T-T.T)==sp.zeros(9)
 assert matmod(sp.Matrix([T[k,k] for k in range(9)])-RT.T[:,3*i+j])==sp.zeros(9,1)
assert mod2(RT.det()-(B*D)**6)==0
# Every non-identity symmetric-determinant term is a matching, hence includes
# a square of a linear form. Test cancellation of permutations with long cycles.
for n in range(2,8):
 cancelled=0;involutions=0
 for p in itertools.permutations(range(n)):
  if all(p[p[i]]==i for i in range(n)):involutions+=1
  else:
   inv=tuple(p.index(i) for i in range(n));assert inv!=p;cancelled+=1
 assert cancelled%2==0
out={'scope':'Universal polynomial identities over F2[A,B,C,D], B*D nonzero',
 'one_factor_M':[[str(v) for v in row] for row in M.tolist()],
 'one_factor_R':[[str(v) for v in row] for row in R.tolist()],
 'symmetric_product':[[str(v) for v in row] for row in S.tolist()],
 'det_R':'B^2','det_tensor_R':'B^6 D^6',
 'tensor_coefficient_matrices_checked':9,'tensor_diagonal_map':'(R1 tensor R2)^transpose',
 'permutation_pairing_checked_through_n':7,'all_assertions_passed':True,
 'runtime_seconds':time.perf_counter()-started}
p=Path(__file__).resolve().parents[1]/'outputs'/'ordinary_product_universal_symmetrizer.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
