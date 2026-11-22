"""Exploratory actual tangent/Tate computations for ramified extension lattices."""
from pathlib import Path
from time import perf_counter
import numpy as np
import json
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start=perf_counter();rows=[]
for p in (3,5,7):
 for e in range(1,5):
  n=p-1; P=np.zeros((e,e),dtype=np.int64)
  for j in range(e-1):P[j+1,j]=1
  P[0,e-1]=p
  powers=[np.linalg.matrix_power(P,i) for i in range(e)]
  C=np.zeros((n,n),dtype=np.int64)
  for j in range(n-1):C[j+1,j]=1
  C[:,n-1]=-1
  T=np.zeros((p*e,p*e),dtype=np.int64)
  T[:e,:e]=np.eye(e,dtype=np.int64)
  T[e:,e:]=np.kron(C,np.eye(e,dtype=np.int64))
  T[:e,(p-1)*e:p*e]=P
  assert np.array_equal(np.linalg.matrix_power(T,p),np.eye(p*e,dtype=np.int64))
  N=sum((np.linalg.matrix_power(T,j) for j in range(p)),np.zeros_like(T))
  Xs=[];cols=[]
  for a in range(p):
   for b in range(p):
    for i in range(e):
     X=np.zeros_like(T);X[a*e:(a+1)*e,b*e:(b+1)*e]=powers[i]
     Xs.append(X);cols.append((T@X-X@T).reshape(-1)%p)
  Z=ker(np.column_stack(cols),p)
  w=np.zeros(p*e,dtype=np.int64);w[0]=1
  w[e:2*e]=-np.linalg.matrix_power(P,e-1)[:,0]
  assert not np.any(N@w)
  table=[]
  for j in range(Z.shape[1]):
   X=sum((int(Z[i,j])*Xs[i] for i in range(len(Xs))),np.zeros_like(T))
   dc=T@X-X@T;nc=N@X-X@N
   assert not np.any(dc%p) and not np.any(nc%p)
   U,V=dc//p,nc//p
   assert not np.any(sum((np.linalg.matrix_power(T,i)@U@np.linalg.matrix_power(T,p-1-i) for i in range(p)),np.zeros_like(T)))
   uv=U[:,0]
   assert not np.any(N@uv)
   lv=sum((uv[a*e:(a+1)*e] for a in range(1,p)),np.zeros(e,dtype=np.int64))%p
   assert not np.any(lv[:e-1])
   b0=-int(lv[e-1])%p
   vw=V@w
   assert not np.any(vw[e:])
   b1=int(vw[0])%p
   table.append((b0,b1))
  spanrank=rank(np.array(table,dtype=np.int64).T,p)
  both=[(j,a,b,a*b%p) for j,(a,b) in enumerate(table) if a*b%p]
  rows.append({'p':p,'e':e,'rank_over_A':p,'centralizer_dimension_mod_p':Z.shape[1],
               'Bockstein_pair_image_rank':spanrank,'basis_pairs':table,'basis_unit_squares':both})
report={'status':'PASS exploration','scope':'M_pi extension lattice with Tate groups A/pi, actual tangent lifts [T,X]/p from full modp centralizer and explicit Tate generators; not a classification or completeness theorem for all lattices.','runs':rows,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_ramified_flat_probe.json').write_text(json.dumps(report,indent=2)+'\n')
for row in rows:print({k:v for k,v in row.items() if k!='basis_pairs'})
print('runtime',report['runtime_seconds'])
