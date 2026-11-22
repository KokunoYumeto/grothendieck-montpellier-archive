"""Exact tangent/first-curvature probe on tensor-product cubic lattices.

The coefficient calculation is in A/pi²=F3[pi]/pi². A prospective
nonzero length prediction must still be checked in an actual truncation.
"""
from pathlib import Path
import numpy as np
from itertools import product
from time import perf_counter
import json
exec(Path('code/C_finish_elementary_curvature_probe.py').read_text().split('TL1=')[0])
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def powm(')[0])
start=perf_counter()
def kron(A,B):
 return [[mul(A[i//len(B)][j//len(B[0])],B[i%len(B)][j%len(B[0])])
          for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
def ar(A):
 return (np.array([[redq(x[0]+x[1]) for x in row] for row in A],dtype=np.int64),
         np.array([[redq(x[1]) for x in row] for row in A],dtype=np.int64))
def aa(A,B):return (A[0]+B[0])%3,(A[1]+B[1])%3
def an(A):return -A[0]%3,-A[1]%3
def am(A,B):return A[0]@B[0]%3,(A[0]@B[1]+A[1]@B[0])%3
def asc(A,c):return A[0]*c%3,A[1]*c%3
def ab(A,B,C,D):return np.block([[A[0],B[0]],[C[0],D[0]]]),np.block([[A[1],B[1]],[C[1],D[1]]])
def image_map(G,C):
 B=G[:,rr(G,3)[1]]%3
 if not B.shape[1]:return np.zeros((0,0),dtype=np.int64)
 rows=rr(B.T,3)[1];square=B[rows,:]
 invs=rr(np.column_stack((square,np.eye(len(rows),dtype=np.int64))),3)[0][:,len(rows):]
 P=np.zeros((len(rows),B.shape[0]),dtype=np.int64);P[:,rows]=invs
 out=P@C@B%3
 assert not np.any((C@B-B@out)%3)
 return out
def ff(C):return dict(factors(tuple(int(x) for x in C.ravel()),C.shape[0]))
Tf=mat([[1,0,0],[1,zeta,0],[add(one,zeta),0,power(zeta,2)]])
Tq=mat([[1,0,0],[0,zeta,0],[neg(add(one,zeta)),neg(zeta),power(zeta,2)]])
pair=mat([[1,1],[0,zeta]])
runs=[];witnesses=[];total_ops=total_trials=0
for label,L,R in [('full_full',Tf,Tf),('full_plane',Tf,Tq),('plane_plane',Tq,Tq),('full_pair',Tf,pair)]:
 T1=kron(L,ident(len(R)));T2=kron(ident(len(L)),R);n=len(T1)
 H,dimensions=tangent_basis(T1,T2);d=H.shape[1]
 t1,t2=ar(T1),ar(T2);ii=ar(ident(n))
 x1,x2=aa(t1,an(ii)),aa(t2,an(ii))
 v1,v2=aa(aa(ii,t1),am(t1,t1)),aa(aa(ii,t2),am(t2,t2))
 by_s=[];gammas=None
 for s in (0,1):
  d0=ab(x1,an(asc(v2,s)),x2,v1);d1=ab(v1,asc(v2,s),an(x2),x1)
  assert not np.any(am(d0,d1)[0]) and not np.any(am(d0,d1)[1])
  h0,p0=homology(d0[0],d1[0],3);h1,p1=homology(d1[0],d0[0],3)
  gamma0=p1@d0[1]@h0%3;gamma1=p0@d1[1]@h1%3
  assert not np.any(gamma1@gamma0%3) and not np.any(gamma0@gamma1%3)
  if gammas is None:gammas=[]
  gammas.append((gamma0,gamma1))
  cs=[]
  for j in range(d):
   u1=(H[:n*n,j].reshape(n,n),np.zeros((n,n),dtype=np.int64));u2=(H[n*n:,j].reshape(n,n),np.zeros((n,n),dtype=np.int64))
   w1=aa(aa(u1,am(t1,u1)),am(u1,t1));w2=aa(aa(u2,am(t2,u2)),am(u2,t2))
   dd0=ab(u1,an(asc(w2,s)),u2,w1);dd1=ab(w1,asc(w2,s),an(u2),u1)
   cur0=aa(am(d1,dd0),am(dd1,d0));cur1=aa(am(d0,dd1),am(dd0,d1))
   assert not np.any(cur0[0]) and not np.any(cur1[0])
   c0=p0@cur0[1]@h0%3;c1=p1@cur1[1]@h1%3
   assert not np.any((c1@gamma0-gamma0@c0)%3) and not np.any((c0@gamma1-gamma1@c1)%3)
   cs.append((c0,c1))
  by_s.append(cs)
 total_ops+=4*d
 rng=np.random.default_rng(1903+n+len(label));found=[];trials=0;nonzero_ops=0
 samples=[]
 for j in range(d):
  v=np.zeros(d,dtype=np.int64);v[j]=1;samples.append(v)
 samples.extend(rng.integers(0,3,size=(1000,d),dtype=np.int64))
 for params in samples:
  for s in (1,2):
   c0=np.zeros_like(by_s[0][0][0]);c1=np.zeros_like(by_s[0][0][1])
   for a,x,y in zip(params,by_s[0],by_s[1]):
    c0+=int(a)*(x[0]+s*(y[0]-x[0]));c1+=int(a)*(x[1]+s*(y[1]-x[1]))
   c0%=3;c1%=3
   g0=(gammas[0][0]+s*(gammas[1][0]-gammas[0][0]))%3
   g1=(gammas[0][1]+s*(gammas[1][1]-gammas[0][1]))%3
   trials+=1
   if np.any(c0) or np.any(c1):nonzero_ops+=1
   fa=ff(image_map(g0,c1));fb=ff(image_map(g1,c0))
   delta={q:fa.get(q,0)-fb.get(q,0) for q in set(fa)|set(fb) if q!=(1,0) and fa.get(q,0)!=fb.get(q,0)}
   if delta:
    found.append({'parameters':params.tolist(),'s':s,'image_gamma0_factors':str(fa),'image_gamma1_factors':str(fb),'predicted_length_difference':str(delta)})
    break
  if found:break
 total_trials+=trials
 runs.append({'baseline':label,'rank':n,**dimensions,'homology_dimensions':[h0.shape[1],h1.shape[1]],'coefficient_operators':4*d,'trials':trials,'nonzero_operator_trials':nonzero_ops,'prospective_witnesses':found})
 if found:witnesses.append({'baseline':label,**found[0]})
 print(label,dimensions,'H',h0.shape[1],h1.shape[1],'nonzero ops',nonzero_ops,'witness',bool(found),flush=True)
report={'status':'EXACT FIRST-CURVATURE PROBE COMPLETE','scope':'Four specified tensor-product lattice baselines, full tangent quotient and symbolic Koszul-parameter coefficient operators; deterministic parameter samples test primary differences on the two pi-Bockstein images. Any nonzero prospective difference requires an actual truncated-complex certificate before a Swan nonvanishing claim.',
        'runs':runs,'coefficient_operators':total_ops,'parameter_trials':total_trials,'prospective_witnesses':witnesses,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_elementary_tensor_curvature.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
