#!/usr/bin/env python3
"""Exact D4 apposition double-Weyl quotient with full triality action."""
from pathlib import Path
from itertools import permutations,product
from datetime import datetime,timezone
from time import perf_counter
from math import gcd
import json
import numpy as np
import sympy as sp
start=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat())
r=4;A=np.array([[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]],dtype=np.int64)
I=np.eye(r,dtype=np.int64);S=[]
for i in range(r):m=I.copy();m[i]-=A[i];S.append(m)
def key(m):return tuple(map(int,m.flat))
W=[I];index={key(I):0}
for w in W:
 for s in S:
  v=w@s;k=key(v)
  if k not in index:index[k]=len(W);W.append(v)
n=len(W);assert n==192
mul=[[index[key(w@v)] for v in W] for w in W]
inv=[next(j for j in range(n) if mul[i][j]==0) for i in range(n)]
c=S[0]@S[2]@S[3]@S[1];ci=index[key(c)];powers=[0]
for i in range(5):powers.append(mul[powers[-1]][ci])
assert mul[powers[-1]][ci]==0 and len(set(powers))==6
normalizer={}
for i in range(n):
 for a in [1,5]:
  if mul[mul[i][ci]][inv[i]]==powers[a]:normalizer[i]=a
assert len(normalizer)==12
rho=sp.Matrix(A).inv()*sp.ones(4,1);Bt={}
for i,w in enumerate(W):
 for a in [1,5]:
  z=sp.Matrix(A)*(sp.Matrix(w)*rho-a*rho)/6
  if all(x.q==1 for x in z):Bt[i]=a
assert len(Bt)==8
Phi=[(b,a) for b,v in Bt.items() for a,u in normalizer.items() if u==v]
assert len(Phi)==48
# Diagram automorphisms: all permutations of the three outer nodes.
autos=[];perms=[]
for p in permutations([0,2,3]):
 perm=[None,1,None,None]
 for i,j in zip([0,2,3],p):perm[i]=j
 P=np.zeros((4,4),dtype=np.int64)
 for i,j in enumerate(perm):P[j,i]=1
 assert np.array_equal(P@c@P.T,c)
 autos.append([index[key(P@w@P.T)] for w in W]);perms.append(perm)
fixed_coxeter=set();folded_conjugates=set()
for w in range(n):
 cc=mul[mul[w][ci]][inv[w]]
 if all(aut[cc]==cc for aut in autos):fixed_coxeter.add(cc)
 if all(aut[w]==w for aut in autos):folded_conjugates.add(cc)
assert fixed_coxeter==folded_conjugates and len(fixed_coxeter)==2
print('Both triality-fixed D4 Coxeter elements form one folded-Weyl conjugacy class')
classof={};representatives=[]
for pair in product(range(n),repeat=2):
 if pair in classof:continue
 orbit={(mul[b][pair[0]],mul[a][pair[1]]) for b,a in Phi}
 assert len(orbit)==48
 k=len(representatives);representatives.append(pair)
 for x in orbit:assert x not in classof;classof[x]=k
assert len(representatives)==768
counts={1:0,2:0,3:0,6:0};records=[]
for k,(u,v) in enumerate(representatives):
 stab=[j for j,aut in enumerate(autos) if classof[(aut[u],aut[v])]==k]
 assert len(stab) in counts;counts[len(stab)]+=1
 records.append({'class':k,'representative':[u,v],'stabilizer_automorphisms':stab})
# Independent Burnside check using pair counts with a unique Phi correction.
fixedcounts=[]
for aut in autos:
 count=sum(classof[(aut[u],aut[v])]==k for k,(u,v) in enumerate(representatives))
 raw=0
 for b,a in Phi:
  pu=sum(aut[u]==mul[b][u] for u in range(n))
  pv=sum(aut[v]==mul[a][v] for v in range(n))
  raw+=pu*pv
 assert raw==count*len(Phi)
 fixedcounts.append(count)
print('Weyl order',n,'Coxeter normalizer',len(normalizer),'B_t',len(Bt),'Phi',len(Phi))
print('Inner quadruple classes',len(representatives))
print('Stabilizer counts by order',counts)
print('Triality permutation fixed-class counts',list(zip(perms,fixedcounts)))
print('Full automorphism orbits',sum(fixedcounts)//6)
print('PASS: complete quotient enumeration and independent twisted fixed-pair count agree')
print('Elapsed seconds',perf_counter()-start)
out=Path(__file__).resolve().parents[1]/'logs'
(out/'d4_outer_stabilizers.json').write_text(json.dumps({'fixed_coxeter_elements':2,'unique_folded_coxeter_class':True,'cartan':A.tolist(),'W':[w.tolist() for w in W],'coxeter':c.tolist(),'B_t':Bt,'normalizer':normalizer,'Phi':Phi,'diagram_automorphisms':perms,'counts':counts,'fixed_counts':fixedcounts,'classes':records,'elapsed_seconds':perf_counter()-start},indent=2))
