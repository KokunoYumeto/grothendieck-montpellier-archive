#!/usr/bin/env python3
"""Induced finite detector for the next cubic-descent half-character.

At this exploratory stage this constructs and validates the exact source
quotient only. No equality of iterated characters is presumed.
"""
import collections,json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent

def nf(word):
 out=[]
 for a in word:
  if out and (out[-1]==0)==(a==0):
   b=out.pop()
   if a:
    c=(a+b)%3
    if c:out.append(c)
  else:out.append(a)
 return tuple(out)
def bi(w):return tuple(0 if a==0 else 3-a for a in w[::-1])
def bm(a,b):return nf(a+b)
def fp(w,x,y,one,mul,inv):
 gs={1:x,2:y,-1:inv(x),-2:inv(y)};a=one
 for k in w:a=mul(a,gs[k])
 return a

def build(modulus=2):
 # B=C2*C3, F=ker(B->S3), x=(sr)^-2, y=sxs.
 s=(0,);r=(1,);tau=(0,1);x=bm(bi(tau),bi(tau));y=bm(bm(s,x),s)
 T=[(),r,(2,),s,(0,1),(0,2)]
 S=np.array([1,0,2]);R=np.array([1,2,0]);I3=np.arange(3)
 def qb(w):
  a=I3
  for t in w:a=a[S if t==0 else (R if t==1 else R[R])]
  return tuple(map(int,a))
 ti={qb(t):j for j,t in enumerate(T)};assert len(ti)==6
 edges={}
 needed=set()
 for name,g in [('s',s),('r',r)]:
  for j,t in enumerate(T):
   gt=bm(g,t);k=ti[qb(gt)];v=bm(bi(T[k]),gt)
   edges[name,j]=(k,v);needed.add(v)
 fw={():()};todo=collections.deque([()]);fg={1:x,2:y,-1:bi(x),-2:bi(y)}
 while needed-set(fw):
  a=todo.popleft();aw=fw[a]
  if len(aw)>=8:raise RuntimeError('Schreier edge bound')
  for k,g in fg.items():
   b=bm(a,g)
   if b not in fw:fw[b]=aw+(k,);todo.append(b)
 m=modulus;n=m*m
 def add(a,b):return (a%m+b%m)%m+m*((a//m+b//m)%m)
 def mul(a,b):
  u,v=a%m,a//m;w,t=b%m,b//m
  return (u*w-v*t)%m+m*((u*t+v*w-v*t)%m)
 omega=m
 X=np.array([mul(omega,a) for a in range(n)]);Y=np.array([add(1,a) for a in range(n)])
 co=lambda a,b:a[b];one=np.arange(n)
 ps=[];edge_rows=[]
 for name in ['s','r']:
  pp=np.empty(6*n,dtype=np.int64)
  for j in range(6):
   k,v=edges[name,j];a=fp(fw[v],X,Y,one,co,np.argsort)
   pp[j*n:(j+1)*n]=k*n+a;edge_rows.append({'generator':name,'coset':j,'target':k,'F_word':list(fw[v])})
  ps.append(pp)
 SS,RR=ps;I=np.arange(6*n);assert np.array_equal(SS[SS],I) and np.array_equal(RR[RR[RR]],I)
 tauB=co(SS,RR);XX=co(np.argsort(tauB),np.argsort(tauB));YY=co(co(SS,XX),SS)
 assert np.array_equal(XX[:n],X) and np.array_equal(YY[:n],Y)
 return {'s':SS,'r':RR,'x':XX,'y':YY,'degree':6*n,'fiber_degree':n,'edge_words':edge_rows}

def run():
 st=time.monotonic();d=build(2);S,R=d['s'],d['r'];T=S[R[S]];X=d['x'];G=PermutationGroup([Permutation(S.tolist()),Permutation(R.tolist())]);E=PermutationGroup([Permutation(R.tolist()),Permutation(T.tolist())])
 out={'statement':'iterated cubic half-character source probe','coefficient_modulus':2,'degree':d['degree'],'B_image_order':int(G.order()),'E_image_order':int(E.order()),'E_derived_orders':[int(g.order()) for g in E.derived_series()],'source_s_r_relations':'PASS','source_x_y_fiber_marking':'PASS','edge_words':d['edge_words'],'elapsed_seconds':time.monotonic()-st,'scope':'Exact finite induced source quotient only; character comparison remains open.'}
 np.savez_compressed(ROOT/'cubic_descent_iterate_mod2.npz',s=S,r=R,x=X,y=d['y'],t=T)
 (ROOT/'cubic_descent_iterate_mod2.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':run()
