#!/usr/bin/env python3
"""Exploratory finite-block Bugár–Vrana crossing geometric mean, q=2.
No floating computation in this script certifies an asymptotic price.
Constructs the exact permutation Gram quotient and high-precision means.
"""
import argparse,itertools,math,json,time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp

def parts(n,top=None):
 if n==0: yield ();return
 for a in range(min(n,top or n),1-1,-1):
  for b in parts(n-a,a):yield(a,)+b
@lru_cache(None)
def char(lam,cyc):
 if not cyc:return int(not lam)
 k=cyc[0];ans=0;cells={(i,j) for i,a in enumerate(lam) for j in range(a)}
 for nu in parts(sum(lam)-k):
  if len(nu)>len(lam) or any(a>lam[i] for i,a in enumerate(nu)):continue
  rem=cells-{(i,j) for i,a in enumerate(nu) for j in range(a)}
  if len(rem)!=k or any((i+1,j) in rem and (i,j+1) in rem and (i+1,j+1) in rem for i,j in rem):continue
  seen=set();todo=[next(iter(rem))]
  while todo:
   x=todo.pop()
   if x in seen:continue
   seen.add(x)
   i,j=x;todo.extend(y for y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)) if y in rem and y not in seen)
  if len(seen)==k:ans+=(-1)**(len({i for i,j in rem})-1)*char(nu,cyc[1:])
 return ans

def main(n,q,ts,out):
 started=time.time();perms=list(itertools.permutations(range(n)));P=len(perms);idx={p:i for i,p in enumerate(perms)}
 mul=np.empty((P,P),dtype=np.int32);inv=np.empty(P,dtype=np.int32);ct=[]
 for a,p in enumerate(perms):
  inv[a]=idx[tuple(p.index(j) for j in range(n))]
  for b,r in enumerate(perms):mul[a,b]=idx[tuple(p[r[j]] for j in range(n))]
  unseen=set(range(n));cy=[]
  while unseen:
   x=min(unseen);s=0
   while x in unseen:unseen.remove(x);s+=1;x=p[x]
   cy.append(s)
  ct.append(tuple(sorted(cy,reverse=True)))
 conj=mul[mul[:,:,None],inv[None,:,None]] if False else np.empty((P,P),dtype=np.int32)
 for g in range(P):conj[g,:]=mul[mul[g,:],inv[g]]
 orb_of=np.full((P,P),-1,dtype=np.int32);orbs=[];reps=[]
 for a in range(P):
  for b in range(P):
   if orb_of[a,b]>=0:continue
   o=sorted(set(zip(conj[:,a].tolist(),conj[:,b].tolist())))
   j=len(orbs);orbs.append(o);reps.append((a,b))
   for c,d in o:orb_of[c,d]=j
 k=len(orbs);print('orbits',n,k,flush=True)
 cyc_count=np.array([len(c) for c in ct]);kernel=q**cyc_count
 G=[]
 for a,b in reps:
  G.append([sp.Rational(sum(int(kernel[mul[inv[a],c]])*int(kernel[mul[inv[b],d]]) for c,d in o),len(o)) for o in orbs])
 G=sp.Matrix(G);assert G==G.T
 _,basis=G.rref();r=len(basis);print('physical rank',r,flush=True)
 Gi=G.extract(basis,basis);Gba=G.extract(basis,range(k));e=idx[tuple(range(n))];psiindex=int(orb_of[e,e]);gpsi=G.extract(basis,[psiindex])
 lams=list(parts(n));projectors=[]
 for lam in lams:
  dim=char(lam,(1,)*n);weights=[sp.Rational(dim*char(lam,c),P) for c in ct]
  for typ in ['AB','AD']:
   M=sp.zeros(k,r)
   for j,oj in enumerate(basis):
    a,b=reps[oj]
    for pi,w in enumerate(weights):
     if w:
      v=(mul[pi,a],mul[pi,b]) if typ=='AB' else (mul[pi,a],mul[b,inv[pi]])
      M[int(orb_of[v]),j]+=w
   E=Gba*M
   assert E==E.T,(n,lam,typ,'not selfadjoint')
   projectors.append((lam,typ,E))
 print('exact operators built',time.time()-started,flush=True)
 if n==4 and q==2:
  ea=next(E for la,ty,E in projectors if la==(2,1,1) and ty=='AB')
  eb=next(E for la,ty,E in projectors if la==(2,1,1) and ty=='AD')
  TA=Gi.inv()*ea;TB=Gi.inv()*eb
  W=sp.Matrix.hstack(*(TA-sp.eye(r)).col_join(TB-sp.eye(r)).nullspace())
  v=W*(W.T*Gi*W).inv()*W.T*gpsi
  eta=(gpsi.T*v)[0]
  assert TA*v==v and TB*v==v and (v.T*Gi*v)[0]==eta and eta>0
  enc=lambda M:[[str(x) for x in row] for row in M.tolist()]
  certificate={'n':n,'q':q,'partition':[2,1,1],'entropy':'3/2','common_eigenspace_dimension':W.cols,'projection_squared_norm':str(eta),'basis_orbit_representatives':[[list(perms[reps[j][0]]),list(perms[reps[j][1]])] for j in basis],'gram':enc(Gi),'projector_AB':enc(TA),'projector_AD':enc(TB),'psi_inner_products':enc(gpsi),'common_projection_coordinates':enc(v),'meaning':'Exact rational witness: TA v=TB v=v, v^T G v=gpsi^T v=eta>0. Gives raw endpoint lower bound 2^(3/2), NOT a price.'}
  certpath=Path(out).with_name('pg_crossing_n4_exact.json');certpath.write_text(json.dumps(certificate,indent=2)+'\n')
  print('exact n4 common-projector certificate',eta,'dimension',W.cols,flush=True)
 mp.mp.dps=max(120, 100+math.ceil(2*n*math.log2(n)*max(ts)/math.log2(10)))
 conv=lambda M:mp.matrix([[mp.mpf(str(x.p))/mp.mpf(str(x.q)) for x in row] for row in M.tolist()])
 L=mp.cholesky(conv(Gi));R=L.T;Ri=R**-1
 ps=Ri.T*conv(gpsi)
 norm=sum(z*z for z in ps);assert abs(norm-q**(2*n))<mp.mpf('1e-80')
 ops=[(lam,typ,Ri.T*conv(E)*Ri) for lam,typ,E in projectors]
 # Check exact projector identities numerically only after exact Gram construction.
 for typ in ['AB','AD']:
  pp=[O for la,ty,O in ops if ty==typ]
  err=max(abs(x) for x in sum(pp,mp.zeros(r))-mp.eye(r))
  assert err<mp.mpf('1e-80'),err
 data=[]
 for t in ts:
  A=mp.zeros(r);B=mp.zeros(r)
  for lam,typ,O in ops:
   h=-sum(mp.mpf(a)/n*mp.log(mp.mpf(a)/n,2) for a in lam)
   val=mp.power(2,n*h*t)
   if typ=='AB':A+=val*O
   else:B+=val*O
  # Eigenprojectors also provide A powers with stable precision.
  Ah=mp.zeros(r);Aih=mp.zeros(r)
  for lam,typ,O in ops:
   if typ!='AB':continue
   h=-sum(mp.mpf(a)/n*mp.log(mp.mpf(a)/n,2) for a in lam)
   Ah+=mp.power(2,n*h*t/2)*O;Aih+=mp.power(2,-n*h*t/2)*O
  C=Aih*B*Aih;C=(C+C.T)/2
  ev,Q=mp.eigsy(C)
  if min(ev)<=0:raise ValueError(('negative eigenvalue',n,t,str(min(ev))))
  root=Q*mp.diag([mp.sqrt(z) for z in ev])*Q.T
  val=(ps.T*Ah*root*Ah*ps)[0]
  logval=mp.log(val,2)
  row={'t':t,'alpha':1/(t+1),'log2_expectation':mp.nstr(logval,60),'finite_F_log2':mp.nstr(logval/(n*(t+1)),60)}
  data.append(row);print(json.dumps(row),flush=True)
 slopes=[]
 for x,y in zip(data,data[1:]):
  slopes.append({'t1':x['t'],'t2':y['t'],'endpoint_log2_slope':str((mp.mpf(y['log2_expectation'])-mp.mpf(x['log2_expectation']))/(n*(y['t']-x['t'])))})
 result={'n':n,'q':q,'permutations':P,'orbit_dimension':k,'physical_rank':r,'precision_digits':mp.mp.dps,'values':data,'slopes':slopes,'elapsed_seconds':time.time()-started,'status':'exploratory; finite-block high-precision values only; no asymptotic certificate'}
 Path(out).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'slopes':slopes,'elapsed':result['elapsed_seconds']}),flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,required=True);ap.add_argument('--q',type=int,default=2);ap.add_argument('--t',type=int,nargs='+',default=[1,3,7,15]);ap.add_argument('--out',required=True);a=ap.parse_args();main(a.n,a.q,a.t,a.out)
