"""Exploratory exact two-generator periodic-Koszul curvature search.

This is a finite detector search, not a theorem about all deformations.
"""
from pathlib import Path
import numpy as np
exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('roots=[')[0])
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start=perf_counter()

def block(A,B,C,D):return [a+b for a,b in zip(A,B)]+[a+b for a,b in zip(C,D)]
def tangent_basis(T1,T2):
 n=len(T1);N1=np.array([[residue(x) for x in row] for row in T1])-np.eye(n,dtype=np.int64)
 N2=np.array([[residue(x) for x in row] for row in T2])-np.eye(n,dtype=np.int64)
 N1%=3;N2%=3;assert not np.any(N1@N1%3) and not np.any(N2@N2%3)
 units=[]
 for i in range(n):
  for j in range(n):
   U=np.zeros((n,n),dtype=np.int64);U[i,j]=1;units.append(U)
 c=[]
 for U in units:c.append(np.concatenate(((N1@U@N1).ravel(),np.zeros(n*n,dtype=np.int64),(U@N2-N2@U).ravel())))
 for U in units:c.append(np.concatenate((np.zeros(n*n,dtype=np.int64),(N2@U@N2).ravel(),(N1@U-U@N1).ravel())))
 d=np.column_stack(c)%3;Z=ker(d,3)
 G=np.column_stack([np.concatenate(((N1@U-U@N1).ravel(),(N2@U-U@N2).ravel())) for U in units])%3
 assert not np.any(d@G%3)
 base=G[:,rr(G,3)[1]];H=[]
 for i in range(Z.shape[1]):
  v=Z[:,i:i+1]
  if rank(np.column_stack((base,v)),3)>base.shape[1]:base=np.column_stack((base,v));H.append(v[:,0])
 return np.column_stack(H),{'tangent_dimension':Z.shape[1],'gauge_rank':rank(G,3),'quotient_dimension':len(H)}

TL1=mat([[1,0,0],[1,zeta,0],[0,0,1]])
TL2=mat([[1,0,0],[0,1,0],[1,0,zeta]])
TQ1=mat([[1,0,0],[0,zeta,0],[0,1,1]])
TQ2=mat([[1,0,0],[0,1,0],[-1,-1,zeta]])
baselines=[('three_character_residue_line',TL1,TL2),('three_character_residue_plane',TQ1,TQ2)]
runs=[];detections=[];actions=0;I=ident(3);m=3
for name,T01,T02 in baselines:
 assert mm(T01,T02)==mm(T02,T01)
 assert mm(mm(T01,T01),T01)==I and mm(mm(T02,T02),T02)==I
 H,dimensions=tangent_basis(T01,T02);nonzero_primary=0;found=0
 for params in product(range(3),repeat=H.shape[1]):
  v=H@np.array(params,dtype=np.int64)%3
  U1=mat(v[:9].reshape(3,3).tolist());U2=mat(v[9:].reshape(3,3).tolist())
  T1=ma(T01,scale(U1,power(pi,m-1)));T2=ma(T02,scale(U2,power(pi,m-1)))
  assert all(valuation(x)>=m for row in ma(mm(T1,T2),mn(mm(T2,T1))) for x in row)
  for T in (T1,T2):assert all(valuation(x)>=m for row in ma(mm(mm(T,T),T),mn(I)) for x in row)
  X1=ma(T1,mn(I));X2=ma(T2,mn(I))
  V1=ma(ma(I,T1),mm(T1,T1));V2=ma(ma(I,T2),mm(T2,T2))
  for s in (1,2):
   D0=block(X1,mn(scale(V2,el(s))),X2,V1)
   D1=block(V1,scale(V2,el(s)),mn(X2),X1)
   P0=mm(D1,D0);P1=mm(D0,D1)
   assert all(valuation(x)>=m for row in P0+P1 for x in row)
   C0=scale(P0,power(pi,-m));C1=scale(P1,power(pi,-m))
   assert mm(C1,D0)==mm(D0,C0)
   vals,lengths=smith_curvature(D0,C1,m);actions+=1
   relevant={str(q):v for q,v in lengths.items() if q!=(1,0)}
   if relevant:nonzero_primary+=1
   bad={q:v%m for q,v in relevant.items() if v%m}
   if bad:
    found+=1;detections.append({'baseline':name,'parameters':list(params),'koszul_parameter':s,'m':m,'smith_exponents':vals,'primary_lengths':relevant,'nonzero_residues':bad})
  if len(detections)>=8:break
 runs.append({'baseline':name,**dimensions,'parameter_classes':3**H.shape[1],
              'nonzero_primary_complexes':nonzero_primary,'detections':found})
 print(name,'done;',found,'detections',flush=True)
 if len(detections)>=8:break
report={'status':'BOUNDED SEARCH COMPLETE','scope':'Two rank3 E=C3xC3 lattice baselines with three affinely independent generic characters; every residual tangent gauge class unless eight detections stop the search; m3 and periodic-Koszul parameters1,2. Exact cyclotomic arithmetic, all group equations and complex equations, graded Smith-cokernel primary lengths. No all-rank or symmetric-group induction assertion.',
        'runs':runs,'complexes_computed':actions,'detections':detections,
        'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_elementary_curvature_probe.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
