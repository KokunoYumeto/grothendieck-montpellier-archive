"""Discovery LP for the 26 remaining colored TU templates; no certificate claim."""
from pathlib import Path
import json,itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
ns={};exec(Path('work/k12_trimodular_classification_certificate.py').read_text().split('VERTEX_RECORDS =')[0],ns)
dual=ns['reconstruct_dual'];dot=ns['dot']
records=json.loads(Path('work/k12_ternary_glue_orbits.json').read_text())
tri=np.triu_indices(10);fac=np.where(tri[0]==tri[1],1,2)
def qr(v):
 v=np.asarray(v,dtype=np.int64);return v[...,tri[0]]*v[...,tri[1]]*fac
def canon(v):
 v=tuple(int(x)for x in v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
out=[]
for rec in records:
 for k,orb in enumerate(rec['orbits']):
  B=[];colors=[]
  for b,mask in zip(rec['B'],orb['state']):
   for c in range(3):
    if mask>>c&1:B.append(tuple(b));colors.append(c)
  z=orb['zero_count'];zw=orb['zero_weight']
  B.extend([(0,0,0)]*z);colors.extend([]if z==0 else[zw]if z==1 else[0,1])
  assert len(B)==13
  Vlist,bnorm,order=dual(B);V=np.asarray(Vlist,dtype=np.int64);cnew=np.asarray([colors[j]for j in order],dtype=np.int64)
  Bnew=[B[j]for j in order];T={canon(v)for v in V};assert len(T)==13 and all(any(v)for v in V)
  E=np.c_[qr(V),np.zeros(13)];rhsE=np.ones(13)
  seen=set();vecs=[];dens=[];pd=[]
  def add(v,d=1,is_pd=False):
   if not any(v):return
   v=canon(v)
   if not is_pd and d==1 and v in T:return
   key=(v,d,is_pd)
   if key in seen:return
   seen.add(key);vecs.append(v);dens.append(d);pd.append(is_pd)
  for i,j in itertools.combinations(range(10),2):
   for sign in [-1,1]:
    v=[0]*10;v[i]=1;v[j]=sign;add(v)
  for lam in itertools.product(range(3),repeat=3):
   coeff=np.asarray([((c+dot(lam,b)+1)%3)-1 for c,b in zip(cnew,Bnew)],dtype=np.int64)
   w=coeff@V;add(w,3)
   for v in V:
    add(w-3*v,3);add(w+3*v,3)
  result=None
  for it in range(15):
   A=np.c_[-qr(vecs),np.asarray([sum(x*x for x in v)if isp else d*d for v,d,isp in zip(vecs,dens,pd)])]
   bb=np.asarray([0 if isp else -d*d for d,isp in zip(dens,pd)])
   cost=np.r_[np.zeros(55),-1.]
   res=linprog(cost,A_ub=A,b_ub=bb,A_eq=E,b_eq=rhsE,bounds=[(None,None)]*55+[(0,1)],method='highs')
   if not res.success:
    result={'status':res.message};break
   eps=res.x[-1]
   if eps<1e-7:
    result={'status':'margin_zero','epsilon':eps,'vectors':vecs,'denominators':dens,'positive_definite_cuts':pd,'inequality_marginals':res.ineqlin.marginals.tolist(),'equality_marginals':res.eqlin.marginals.tolist()};break
   Q=np.zeros((10,10));Q[tri]=res.x[:55];Q=Q+Q.T-np.diag(np.diag(Q));eig,U=np.linalg.eigh(Q)
   if eig[0]<.0001:
    for j,t in enumerate(eig):
     if t<.0001:add(np.rint(U[:,j]*100).astype(int),1,True)
    continue
   result={'status':'positive_relaxation','epsilon':eps,'min_eigenvalue':float(eig[0]),'gram':Q.tolist()};break
  if result is None:result={'status':'iteration_limit'}
  result.update(record=rec['record'],orbit=k+1,V=Vlist,colors=cnew.tolist(),B=Bnew,state=orb)
  out.append(result);print(json.dumps({k:v for k,v in result.items()if k in('record','orbit','status','epsilon','min_eigenvalue')}),flush=True)
  Path('work/k12_ternary_glue_lp.json').write_text(json.dumps(out,indent=2)+'\n')
