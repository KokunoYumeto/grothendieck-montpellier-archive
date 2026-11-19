#!/usr/bin/env python3
"""Inspect exact two-dimensional obstructions for the sparse doubling family."""
from pathlib import Path
import ast,itertools,json,time
started=time.perf_counter();w=Path(__file__).resolve().parents[1]
p=w/'code/ss_rectangular_sparse_templates.py';tree=ast.parse(p.read_text())
defs=ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
ns={'itertools':itertools};exec(compile(defs,str(p),'exec'),ns)
def kernel(rows,N):
 R=list(rows);piv=[]
 for j in range(N):
  k=next((i for i in range(len(piv),len(R)) if R[i]>>j&1),None)
  if k is None:continue
  i=len(piv);R[i],R[k]=R[k],R[i]
  for a in range(len(R)):
   if a!=i and R[a]>>j&1:R[a]^=R[i]
  piv.append(j)
 out=[]
 for j in range(N):
  if j in piv:continue
  v=1<<j
  for i,k in enumerate(piv):
   if R[i]>>j&1:v^=1<<k
  out.append(v)
 return out
def dot(a,b):return (a&b).bit_count()%2
pattern=62556;cases=[]
for q in [3,6,12,24,48,96,192]:
 system=ns['elementary'](q);B=system['basis'];ix={b:i for i,b in enumerate(B)};C=[0]*(6*q);s=0;ds=0
 for j in range(18):
  if not(pattern>>j&1):continue
  C=[a^b for a,b in zip(C,system['matrices'][j])]
  a,t=divmod(j,3);x,y=system['template'][a];s^=1<<(3*ix[x,y]+t)
  if x%2:ds^=1<<(3*ix[x-1,y]+t)
  if y:ds^=1<<(3*ix[x+2,0]+t)
 assert ns['apply'](C,s)==ns['apply'](C,ds)==0
 left=kernel(C,6*q);assert len(left)==2
 pairing=[[dot(l,v) for v in [s,ds]] for l in left]
 determinant=pairing[0][0]*pairing[1][1]^pairing[0][1]*pairing[1][0]
 def support(v):return [[B[i//3][0],B[i//3][1],i%3] for i in range(6*q) if v>>i&1]
 cases.append({'q':q,'left_kernel_bits':left,'left_support':[support(l) for l in left],
  'right_kernel_bits':[s,ds],'right_support':[support(s),support(ds)],
  'pairing':pairing,'determinant':determinant})
 assert determinant==1
out={'status':'PASS_FINITE_OBSTRUCTION_CHECK','scope':'Finite exact cokernel pairing, not a uniform proof',
 'pattern':pattern,'cases':cases,'elapsed_seconds':time.perf_counter()-started}
(w/'outputs/ss_sparse_dual_kernels.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
 'cases':[{'q':c['q'],'left_support_counts':[len(t) for t in c['left_support']],
 'pairing':c['pairing']} for c in cases]},indent=2))
