#!/usr/bin/env python3
"""Exploratory exact extension search over Z_(2)[e]/e^3.
Only explicit found extensions are certificates; absent witnesses prove nothing.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import numpy as np
import sympy as sp
import json
START=perf_counter()

def residue(x):
 x=sp.Rational(x)
 assert int(x.q)%2
 return int(x.p)%2

def rank2(a):
 a=[[residue(x) for x in row] for row in a.tolist()]
 if not a: return 0
 r=0
 for j in range(len(a[0])):
  piv=next((i for i in range(r,len(a)) if a[i][j]),None)
  if piv is None: continue
  a[r],a[piv]=a[piv],a[r]
  for i in range(len(a)):
   if i!=r and a[i][j]: a[i]=[x^y for x,y in zip(a[i],a[r])]
  r+=1
 return r

def poly_mul(a,b):
 return [sum((a[i]*b[j] for i in range(3) for j in range(3) if i+j==r),sp.zeros(a[0].rows,b[0].cols)) for r in range(3)]

def change(t,S):
 I=S[0].inv()
 inv=[I,-I*S[1]*I,I*S[1]*I*S[1]*I-I*S[2]*I]
 return poly_mul(poly_mul(inv,t),S)

def canonical(t):
 t=[sp.Matrix(x) for x in t]
 n=t[0].rows; regs=0; steps=[]
 while n and rank2(t[0]-sp.eye(n)):
  v=next(sp.eye(n)[:,j] for j in range(n) if rank2((t[0]-sp.eye(n))[:,j]))
  cols=[v,t[0]*v]
  for j in range(n):
   w=sp.eye(n)[:,j]
   if rank2(sp.Matrix.hstack(*cols,w))>len(cols): cols.append(w)
  S0=sp.Matrix.hstack(*cols);S1=sp.zeros(n);S2=sp.zeros(n)
  S1[:,1]=t[1]*v;S2[:,1]=t[2]*v
  tp=change(t,[S0,S1,S2])
  assert tp[0][:2,:2]==sp.Matrix([[0,1],[1,0]])
  assert tp[1][:2,:2]==sp.zeros(2) and tp[2][:2,:2]==sp.zeros(2)
  assert all(a[2:,:2]==sp.zeros(n-2,2) for a in tp)
  steps.append({'regular_generator':list(v),'S0':S0.tolist(),'S1':S1.tolist(),'S2':S2.tolist()})
  t=[a[2:,2:] for a in tp];n-=2;regs+=1
 if n>2: return None
 if n==0: return {'regular':regs,'plus':0,'minus':0,'extra':[0,0,0],'steps':steps}
 P=(sp.eye(n)+t[0])/2;Q=sp.eye(n)-P
 cols=[];a=0
 for j in range(n):
  v=P[:,j]
  if rank2(sp.Matrix.hstack(*(cols+[v])))>len(cols):cols.append(v);a+=1
 for j in range(n):
  v=Q[:,j]
  if rank2(sp.Matrix.hstack(*(cols+[v])))>len(cols):cols.append(v)
 S=sp.Matrix.hstack(*cols);t=[S.inv()*x*S for x in t]
 assert t[0]==sp.diag(*([1]*a+[-1]*(n-a)))
 if n<2 or a!=1:
  assert t[1]==sp.zeros(n) and t[2]==sp.zeros(n)
  return {'regular':regs,'plus':a,'minus':n-a,'extra':[0,0,0],'steps':steps}
 b,c=t[1][0,1],t[1][1,0]
 b1,c1=residue(b),residue(c)
 X=sp.Matrix([[0,(b1-b)/2],[(c-c1)/2,0]])
 t=change(t,[sp.eye(2),X,sp.zeros(2)])
 assert t[1]==sp.Matrix([[0,b1],[c1,0]]) and b1*c1==0
 assert t[2][0,0]==0 and t[2][1,1]==0
 b2,c2=residue(t[2][0,1]),residue(t[2][1,0])
 extra=[0,0,0]
 if b1==c1==0 and b2==c2==1:extra[0]=1
 if b1==1 and c2==1:extra[1]=1
 if c1==1 and b2==1:extra[2]=1
 return {'regular':regs,'plus':1,'minus':1,'extra':extra,'normalized_bits':[b1,c1,b2,c2],'steps':steps}

z1=np.zeros((1,1),dtype=np.int64);z2=np.zeros((2,2),dtype=np.int64)
ob=[('plus',[np.array([[1]]),z1,z1],[0,0,0]),('minus',[np.array([[-1]]),z1,z1],[0,0,0])]
for ex,(a,b) in enumerate([(2,2),(1,2),(2,1)]):
 u1=np.zeros((2,2),dtype=np.int64);u2=u1.copy()
 (u1 if a==1 else u2)[0,1]=1;(u1 if b==1 else u2)[1,0]=1
 ev=[0,0,0];ev[ex]=1
 ob.append((f'M{a}{b}',[np.diag([1,-1]),u1,u2],ev))
candidates=valid=classified=0;relations={}
for na,ta,ea in ob:
 for nb,tb,eb in ob:
  a,b=len(ta[0]),len(tb[0]);z=np.zeros((b,a),dtype=np.int64)
  for ent in product(range(2),repeat=3*a*b):
   candidates+=1
   xs=[np.array(ent[r*a*b:(r+1)*a*b]).reshape(a,b) for r in range(3)]
   t=[np.block([[ta[r],xs[r]],[z,tb[r]]]) for r in range(3)]
   if not np.array_equal(t[0]@t[0],np.eye(a+b,dtype=np.int64)) or np.any(t[0]@t[1]+t[1]@t[0]) or np.any(t[0]@t[2]+t[2]@t[0]+t[1]@t[1]):continue
   valid+=1
   can=canonical(t)
   if can is None:continue
   classified+=1
   rel=tuple(ea[i]+eb[i]-can['extra'][i] for i in range(3))
   if rel!=(0,0,0) and rel not in relations:
    relations[rel]={'A':na,'B':nb,'X':[x.tolist() for x in xs],'quotient':can}
report={'scope':'0/1 extension blocks, endpoints plus/minus/M22/M12/M21','candidates':candidates,'admissible':valid,'classified_after_regular_removal':classified,'relations':[{'vector':r,**v} for r,v in relations.items()],'runtime':perf_counter()-START}
Path('logs/C_finish_epsilon3_probe.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(report,indent=2,default=str))
