"""Construct an exact, independently checkable degree-(210)/(120) obstruction."""
from pathlib import Path
from itertools import combinations
import json,math
import sympy as s
import numpy as np

A,B=5,9
PA=list(combinations(range(A),2));PB=list(combinations(range(B),2))
IA={x:i for i,x in enumerate(PA)};IB={x:i for i,x in enumerate(PB)}
slices=[[(0,4),(1,3)],[(0,5),(2,3)],[(1,5),(2,4)],[(0,7),(1,6)],[(0,8),(2,6)]]
T=s.MutableDenseNDimArray.zeros(A,B,B)
for a,edges in enumerate(slices):
 for u,v in edges:T[a,u,v]=T[a,v,u]=1
U=s.Matrix(A*B,B,lambda r,c:T[r//B,r%B,c])
Z=[]
for i in range(A):
 M=s.zeros(len(PA)*B,A*B)
 for j in range(A):
  if i==j:continue
  pair=tuple(sorted((i,j)));sgn=1 if i<j else -1
  for k in range(B):M[IA[pair]*B+k,j*B+k]=sgn
 Z.append(M)
K=s.Matrix.hstack(*(M*U for M in Z))
null=K.T.nullspace()
rows=[]
for v in null:
 den=s.ilcm(*[x.q for x in v]);w=[int(x*den) for x in v];g=math.gcd(*w);rows.append([x//g for x in w])
L=s.Matrix(rows)
assert L*K==s.zeros(L.rows,K.cols)
H=s.Matrix.vstack(*(L*M for M in Z))
x=s.zeros(A*B,1);x[2*B]=1;E=U.row_join(x)
assert H*E==s.zeros(H.rows,E.cols)
R=s.zeros(len(PB)*A,B*E.cols)
for i in range(B):
 for j in range(B):
  if i==j:continue
  pair=tuple(sorted((i,j)));sgn=1 if i<j else -1
  for a in range(A):
   for k in range(E.cols):R[IB[pair]*A+a,i*E.cols+k]=sgn*E[a*B+j,k]

def rankcert(M,prime=1000003):
 n=np.array(M.tolist(),dtype=np.int64)%prime
 nr,nc=n.shape;rowids=list(range(nr));rs=[];cs=[];vals=[];r=0
 for c in range(nc):
  piv=next((i for i in range(r,nr) if n[i,c]),None)
  if piv is None:continue
  if piv!=r:n[[piv,r]]=n[[r,piv]];rowids[piv],rowids[r]=rowids[r],rowids[piv]
  val=int(n[r,c]);rs.append(rowids[r]);cs.append(c);vals.append(val)
  n[r,c:]=(n[r,c:]*pow(val,-1,prime))%prime
  fac=n[r+1:,c].copy();n[r+1:,c:]=(n[r+1:,c:]-fac[:,None]*n[r,c:])%prime
  r+=1
  if r==nr:break
 return {'shape':[nr,nc],'rank_minor_size':r,'rows':rs,'columns':cs,'determinant_mod_prime':math.prod(vals)%prime}
certs={name:rankcert(M) for name,M in [('K',K),('L',L),('H',H),('E',E),('R',R)]}
assert {n:c['rank_minor_size'] for n,c in certs.items()}=={'K':40,'L':50,'H':35,'E':10,'R':82}
out={'name':'permanent five-plane degree-(210)/(120) certificate','prime':1000003,'A_dimension':A,'B_dimension':B,'slices_edges':slices,'variable_labels':list('abcdefghi'),'left_annihilator_shape':[L.rows,L.cols],'left_annihilator_entries':[[i,j,int(L[i,j])] for i in range(L.rows) for j in range(L.cols) if L[i,j]],'extra_extension_entry':[2,0],'minor_certificates':certs}
p=Path(__file__).with_name('permanent_apolar_certificate.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'file':str(p),'left_annihilator_nonzero_entries':len(out['left_annihilator_entries']),'matrix_certified_ranks':{n:c['rank_minor_size'] for n,c in certs.items()}},indent=2))
