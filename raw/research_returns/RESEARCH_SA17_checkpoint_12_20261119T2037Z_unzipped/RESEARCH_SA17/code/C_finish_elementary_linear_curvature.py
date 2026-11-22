"""Exact residual curvature-operator algebra for selected elementary cubic lattices.

This probes the detector, not the Swan classes themselves. If the generated
operator algebra is nilpotent, every parameter in this linear deformation
space has zero nonzero-primary curvature support at the tested first order.
"""
from pathlib import Path
import numpy as np
from itertools import product
from time import perf_counter
import json
exec(Path('code/C_finish_elementary_curvature_probe.py').read_text().split('TL1=')[0])
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def powm(')[0])
start=perf_counter()

def lattice(chars,axis,plane):
 roots=[power(zeta,c[axis]) for c in chars];n=len(chars);T=mat([[0]*n for _ in range(n)])
 if not plane:
  T[0][0]=roots[0]
  for i in range(1,n):T[i][i]=roots[i];T[i][0]=div(sub(roots[i],roots[0]),pi)
 else:
  for i in range(n-1):T[i][i]=roots[i];T[n-1][i]=div(sub(roots[i],roots[-1]),pi)
  T[n-1][n-1]=roots[-1]
 return T
def residual(A):return np.array([[residue(x) for x in row] for row in A],dtype=np.int64)
def linspace(mats,n):
 if not mats:return []
 A=np.column_stack([M.ravel() for M in mats])%3
 return [A[:,j].reshape(n,n) for j in rr(A,3)[1]]
def operator_algebra(gens,n):
 A=linspace(gens,n);stages=[len(A)]
 while True:
  B=linspace(A+[a@b%3 for a in A for b in gens],n)
  if len(B)==len(A):break
  A=B;stages.append(len(A))
 powers=[];B=A
 for j in range(1,n*n+2):
  powers.append(len(B))
  if not B:return {'dimension':len(A),'generation_dimensions':stages,'power_dimensions':powers,'nilpotence_index':j}
  C=linspace([a@b%3 for a in B for b in A],n)
  if len(C)==len(B):return {'dimension':len(A),'generation_dimensions':stages,'power_dimensions':powers,'nilpotence_index':None}
  B=C
 return {'dimension':len(A),'generation_dimensions':stages,'power_dimensions':powers,'nilpotence_index':None}

sets=[[(0,0),(1,0),(0,1)],[(0,0),(1,0),(0,1),(1,1)],[(0,0),(1,0),(2,0),(0,1)]]
runs=[];gen_count=0
for chars in sets:
 for plane in (False,True):
  T1,T2=[lattice(chars,i,plane) for i in (0,1)];n=len(chars);I=ident(n)
  assert mm(T1,T2)==mm(T2,T1)
  assert mm(mm(T1,T1),T1)==I and mm(mm(T2,T2),T2)==I
  H,dimensions=tangent_basis(T1,T2)
  X1=ma(T1,mn(I));X2=ma(T2,mn(I));V1=ma(ma(I,T1),mm(T1,T1));V2=ma(ma(I,T2),mm(T2,T2))
  generators=[];by_s=[]
  for s in (0,1):
   D0=block(X1,mn(scale(V2,el(s))),X2,V1);D1=block(V1,scale(V2,el(s)),mn(X2),X1)
   assert all(x==zero for row in mm(D0,D1)+mm(D1,D0) for x in row)
   d0,d1=residual(D0),residual(D1)
   h,proj=homology(d1,d0,3)
   mats=[]
   for j in range(H.shape[1]):
    v=H[:,j];U1=mat(v[:n*n].reshape(n,n).tolist());U2=mat(v[n*n:].reshape(n,n).tolist())
    W1=ma(ma(U1,mm(T1,U1)),mm(U1,T1));W2=ma(ma(U2,mm(T2,U2)),mm(U2,T2))
    delta0=block(U1,mn(scale(W2,el(s))),U2,W1)
    delta1=block(W1,scale(W2,el(s)),mn(U2),U1)
    Cur=scale(ma(mm(D0,delta1),mm(delta0,D1)),power(pi,-1))
    c=residual(Cur)
    assert not np.any(d1@c@h%3)
    mats.append(proj@c@h%3)
   by_s.append(mats)
  # Norms reduce to zero on these radical-square-zero residual lattices,
  # so residual homology bases do not depend on s. Curvature is linear in s.
  generators=by_s[0]+[(b-a)%3 for a,b in zip(by_s[0],by_s[1])]
  gen_count+=len(generators)
  alg=operator_algebra(generators,h.shape[1])
  # Deterministic finite parameter check even when the operator algebra is nonnil.
  rng=np.random.default_rng(3019+n+int(plane));nonnil=[]
  for k in range(200):
   pars=rng.integers(0,3,size=H.shape[1],dtype=np.int64);s=int(rng.integers(0,3))
   C=sum((int(a)*(b+s*(c-b)) for a,b,c in zip(pars,by_s[0],by_s[1])),np.zeros_like(generators[0]))%3
   P=np.eye(C.shape[0],dtype=np.int64)
   for j in range(C.shape[0]):P=P@C%3
   if np.any(P):nonnil.append({'parameters':pars.tolist(),'s':s,'operator':C.tolist()});break
  runs.append({'characters':chars,'residue_subspace':'plane' if plane else 'line',**dimensions,
               'odd_homology_dimension':h.shape[1],'curvature_coefficient_matrices':len(generators),
               'generated_algebra':alg,'random_nonnil_witnesses':nonnil})
  print(chars,plane,alg,'witnesses',len(nonnil),flush=True)
report={'status':'EXACT OPERATOR-ALGEBRA PROBE COMPLETE','scope':'Six explicitly specified rank3/rank4 lattices. Full residual tangent quotient bases and both coefficients of the symbolic Koszul parameter; exact generated-algebra and power-space calculations over F3, plus stated deterministic samples. No vanishing theorem for Swan classes or a symmetric-group induction claim.',
        'runs':runs,'curvature_coefficient_matrices':gen_count,
        'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_elementary_linear_curvature.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
