#!/usr/bin/env python3
"""Complete E6 outer-fixed count using the 45 twisted Weyl coboundaries."""
from pathlib import Path
from time import perf_counter
from datetime import datetime,timezone
from math import gcd
import json
import numpy as np
import sympy as sp
from coxeter_normalizers import cartan
start=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat(),flush=True)
A=cartan('E6');r=6;I=np.eye(r,dtype=np.int64);S=[]
for i in range(r):m=I.copy();m[i]-=A[i];S.append(m)
def key(m):return tuple(map(int,m.flat))
W=[I];index={key(I):0}
for w in W:
 for s in S:
  v=w@s;k=key(v)
  if k not in index:index[k]=len(W);W.append(v)
assert len(W)==51840
print('Weyl order',len(W),flush=True)
perm=[5,1,4,3,2,0];P=I[:,perm]
# Bipartite Coxeter: {1,4,6} then {2,3,5} in Bourbaki numbering.
c=S[0]@S[3]@S[5]@S[1]@S[2]@S[4]
assert np.array_equal(P@c@P.T,c)
pows=[I]
for i in range(11):pows.append(pows[-1]@c)
assert np.array_equal(pows[-1]@c,I)
assert len({key(x) for x in pows})==12
rho=np.array(sp.Matrix(A).inv()*sp.ones(r,1),dtype=np.int64).reshape(r)
normalizer={};Bt={};delta_counts={};delta_witness={};fixed=0
fixed_coxeter=set();folded_conjugates=set()
adj=np.array(sp.Matrix(A).adjugate(),dtype=np.int64);det=int(sp.Matrix(A).det())
for i,w in enumerate(W):
 for a in [1,5,7,11]:
  if np.array_equal(w@c,pows[a]@w):normalizer[i]=a
  if np.all((A@(w@rho-a*rho))%12==0):Bt[i]=a
 wi=(adj@w.T@A)//det
 assert np.array_equal(w@wi,I)
 conjugate=w@c@wi
 if np.array_equal(P@conjugate@P.T,conjugate):fixed_coxeter.add(key(conjugate))
 if np.array_equal(P@w@P.T,w):folded_conjugates.add(key(conjugate))
 d=P@w@P.T@wi;k=key(d)
 delta_counts[k]=delta_counts.get(k,0)+1;delta_witness.setdefault(k,i)
 if np.array_equal(P@w@P.T,w):fixed+=1
assert fixed_coxeter==folded_conjugates and len(fixed_coxeter)==96
print('All96 diagram-fixed E6 Coxeter elements form one folded-Weyl conjugacy class',flush=True)
assert len(normalizer)==48 and len(Bt)==12 and fixed==1152 and len(delta_counts)==45
assert set(delta_counts.values())=={1152}
Phi=[(b,a) for b,v in Bt.items() for a,u in normalizer.items() if u==v]
assert len(Phi)==144
contributing=[(b,a) for b,a in Phi if key(W[b]) in delta_counts and key(W[a]) in delta_counts]
num=sum(delta_counts.get(key(W[b]),0)*delta_counts.get(key(W[a]),0) for b,a in Phi)
assert num%144==0
F=num//144;N=51840**2//144
print('Coxeter normalizer',len(normalizer),'B_t',len(Bt),'Phi',len(Phi),flush=True)
print('Fixed Weyl subgroup',fixed,'twisted coboundaries',len(delta_counts),flush=True)
print('Contributing Phi pairs',len(contributing),contributing,flush=True)
print('Inner classes',N,'Aut=C2',F,'Aut=1',N-F,'full automorphism classes',(N+F)//2,flush=True)
print('PASS: each twisted fibre has independently counted size1152',flush=True)
print('Elapsed seconds',perf_counter()-start,flush=True)
out=Path(__file__).resolve().parents[1]/'logs'
(out/'e6_outer_stabilizers.json').write_text(json.dumps({'fixed_coxeter_elements':96,'unique_folded_coxeter_class':True,'cartan':A.tolist(),'coxeter':c.tolist(),'diagram_automorphism':P.tolist(),'Weyl_order':len(W),'fixed_Weyl_order':fixed,'Phi_order':len(Phi),'normalizer':[{'matrix':W[i].tolist(),'exponent':a} for i,a in normalizer.items()],'B_t':[{'matrix':W[i].tolist(),'exponent':a} for i,a in Bt.items()],'twisted_coboundaries':[{'matrix':np.array(k).reshape(r,r).tolist(),'witness':W[delta_witness[k]].tolist(),'fibre_size':v} for k,v in delta_counts.items()],'contributing_pairs':[{'first':W[b].tolist(),'second':W[a].tolist()} for b,a in contributing],'inner_classes':N,'C2_classes':F,'trivial_classes':N-F,'elapsed_seconds':perf_counter()-start},indent=2))
