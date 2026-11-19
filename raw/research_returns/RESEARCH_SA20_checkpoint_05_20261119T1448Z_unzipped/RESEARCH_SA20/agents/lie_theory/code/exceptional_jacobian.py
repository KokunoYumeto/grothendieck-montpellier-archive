#!/usr/bin/env python3
"""Exact integral root-lattice Lie algebra and quotient-Jacobian certificates.
The implementation fixes a bimultiplicative cocycle in simple-root coordinates.
Every basis Jacobi identity can be exhaustively checked. No floating point.
"""
from pathlib import Path
from itertools import combinations
from datetime import datetime, timezone
from time import perf_counter
import json, random, argparse
import numpy as np
import sympy as sp
from coxeter_normalizers import cartan
OUT=Path(__file__).resolve().parents[1]/'logs'

def addto(out,v,c=1):
    for k,a in v:
        out[k]=out.get(k,0)+c*a
        if out[k]==0: del out[k]

class RootLie:
 def __init__(self,kind):
    self.kind=kind; self.A=cartan(kind); self.r=len(self.A)
    if kind=='D4':
        self.A[2,3]=self.A[3,2]=0;self.A[1,3]=self.A[3,1]=-1
    assert np.array_equal(self.A,self.A.T)
    r=self.r; I=np.eye(r,dtype=int); S=[]
    for i in range(r):
        q=I.copy();q[i]-=self.A[i];S.append(q)
    roots={tuple(map(int,I[:,i])) for i in range(r)};todo=list(roots)
    for a in todo:
        for s in S:
            b=tuple(map(int,s@a))
            if b not in roots: roots.add(b);todo.append(b)
    self.roots=sorted(roots); self.idx={a:i for i,a in enumerate(self.roots)}
    self.nr=len(roots);self.n=self.nr+r
    assert all(int(np.array(a)@self.A@np.array(a))==2 for a in roots)
    self.table=[[()] * self.n for _ in range(self.n)]
    for i,a in enumerate(self.roots):
      for j,b in enumerate(self.roots):
        c=tuple(x+y for x,y in zip(a,b))
        sign=(-1)**((sum(a[k]*b[k] for k in range(r))+sum(a[k]*b[l]*int(self.A[k,l]) for k in range(r) for l in range(k)))%2)
        if c in self.idx: self.table[i][j]=((self.idx[c],sign),)
        elif all(x==0 for x in c): self.table[i][j]=tuple((self.nr+k,sign*v) for k,v in enumerate(a) if v)
      for k in range(r):
        c=sum(int(self.A[k,l])*a[l] for l in range(r))
        if c:
          self.table[self.nr+k][i]=((i,c),)
          self.table[i][self.nr+k]=((i,-c),)
    for i in range(self.n):
      for j in range(self.n): assert self.table[i][j]==tuple((k,-c) for k,c in self.table[j][i])
 def bracket(self,a,b):
    out={}
    for i,c in a.items():
      for j,d in b.items(): addto(out,self.table[i][j],c*d)
    return out
 def adj(self,e):
    ans=[]
    for j in range(self.n):
      out={}
      for i,c in e.items():addto(out,self.table[i][j],c)
      ans.append(out)
    return ans
 def jacobi(self):
    total=0
    for i,j,k in combinations(range(self.n),3):
      out={}
      for a,b,c in ((i,j,k),(j,k,i),(k,i,j)):
        for l,v in self.table[b][c]:addto(out,self.table[a][l],v)
      assert not out,(i,j,k,out)
      total+=1
    return total
 def triple(self,diagram):
    deg=[sum(a*b for a,b in zip(root,diagram)) for root in self.roots]+[0]*self.r
    plus=[i for i,v in enumerate(deg) if v==2]
    minus=[i for i,v in enumerate(deg) if v==-2]
    zero=[i for i,v in enumerate(deg) if v==0]
    hc=sp.Matrix(self.A).T.inv()*sp.Matrix(diagram)
    h={self.nr+i:v for i,v in enumerate(hc) if v}
    rng=random.Random(20261119)
    for attempt in range(100):
      e={i:(1 if attempt==0 else rng.choice([-2,-1,1,2])) for i in plus}
      cols=[self.bracket(e,{i:1}) for i in minus]
      M=sp.Matrix(len(zero),len(minus),lambda i,j:cols[j].get(zero[i],0))
      rhs=sp.Matrix([h.get(i,0) for i in zero])
      try: sol,params=M.gauss_jordan_solve(rhs)
      except ValueError: continue
      sol=sol.subs({a:0 for a in params})
      f={j:v for j,v in zip(minus,sol) if v}
      assert self.bracket(e,f)==h
      assert self.bracket(h,e)=={i:2*c for i,c in e.items()}
      assert self.bracket(h,f)=={i:-2*c for i,c in f.items()}
      return e,h,f,deg,attempt
    raise AssertionError(('triple search exhausted',diagram))
 def powers_and_traces(self,e,deg,exponents):
    A=self.adj(e); cols=[{i:1} for i in range(self.n)]; ans={}
    for power in range(1,max(exponents)+1):
      new=[]
      for col in cols:
        out={}
        for k,c in col.items():addto(out,A[k].items(),c)
        new.append(out)
      cols=new
      if power not in exponents:continue
      vals=[]
      for y in range(self.n):
        if deg[y]!=-2*power:continue
        value=0
        for i in range(self.n):
          for j,c in self.table[y][i]:value+=c*cols[j].get(i,0)
        if value:vals.append((y,(power+1)*value))
      ans[power]=vals
    return ans
 def record_element(self,a):
    return [{'basis':list(self.roots[i]) if i<self.nr else 'h'+str(i-self.nr+1),'coefficient':str(c)} for i,c in sorted(a.items())]

def run(kind,diagram,jacobi=True):
    started=perf_counter(); utc=datetime.now(timezone.utc).isoformat()
    L=RootLie(kind)
    print(kind,'root count',L.nr,'dimension',L.n,flush=True)
    nj=L.jacobi() if jacobi else None
    print('All basis Jacobi triples:',nj,flush=True)
    e,h,f,deg,attempt=L.triple(diagram)
    exps={'E8':[1,7,11,13,17,19,23,29],'E7':[1,5,7,9,11,13,17]}[kind]
    vals=L.powers_and_traces(e,deg,exps)
    report={'type':kind,'diagram':diagram,'started_utc':utc,'cartan':L.A.tolist(),'root_count':L.nr,'dimension':L.n,
      'all_basis_jacobi_triples':nj,'e':L.record_element(e),'h':L.record_element(h),'f':L.record_element(f),
      'triple_search_attempt':attempt,'max_h_weight':max(deg),
      'derivatives':{m:[{'root':L.roots[i],'value':str(v)} for i,v in values] for m,values in vals.items()},
      'nonzero_exponents':[m for m in exps if vals[m]],'elapsed_seconds':perf_counter()-started}
    tag=kind+'_'+''.join(map(str,diagram))
    (OUT/('jacobian_'+tag+'.json')).write_text(json.dumps(report,indent=2))
    print('Exact sl2 triple found on attempt',attempt,'with maximum h-weight',max(deg),flush=True)
    for m,values in vals.items(): print('degree',m+1,'nonzero derivatives',[(L.roots[i],v) for i,v in values],flush=True)
    print('Nonzero exponents',report['nonzero_exponents'],flush=True)
    print('Elapsed seconds',report['elapsed_seconds'],flush=True)
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--skip-jacobi',action='store_true');a=p.parse_args()
    run('E8',[2,2,2,0,2,0,2,2],not a.skip_jacobi)

class Minuscule:
 """The 27-dimensional minuscule E6 module, checked on every bracket."""
 def __init__(self,L):
  assert L.kind=='E6'
  r=L.r;A=L.A
  weights={(1,0,0,0,0,0)};todo=list(weights)
  for w in todo:
   for i in range(r):
    v=tuple(w[j]-w[i]*int(A[j,i]) for j in range(r))
    if v not in weights:weights.add(v);todo.append(v)
  self.weights=sorted(weights);self.n=len(weights);assert self.n==27
  wi={w:i for i,w in enumerate(self.weights)}
  rho=[None]*L.n
  simple=[]
  for i in range(r):
   root=tuple(int(j==i) for j in range(r));simple.append(L.idx[root])
   ep=np.zeros((27,27),dtype=np.int64);em=ep.copy()
   for j,w in enumerate(self.weights):
    if w[i]==-1:
     v=tuple(w[k]+int(A[k,i]) for k in range(r));ep[wi[v],j]=1
    if w[i]==1:
     v=tuple(w[k]-int(A[k,i]) for k in range(r));em[wi[v],j]=-1
   rho[L.idx[root]]=ep;rho[L.idx[tuple(-x for x in root)]]=em
   rho[L.nr+i]=np.diag([w[i] for w in self.weights])
  for j in sorted(range(L.nr),key=lambda j:abs(sum(L.roots[j]))):
   if rho[j] is not None:continue
   a=L.roots[j];sign=1 if sum(a)>0 else -1
   for i in range(r):
    u=tuple(sign*int(k==i) for k in range(r));b=tuple(x-y for x,y in zip(a,u))
    if b in L.idx and abs(sum(b))<abs(sum(a)):
     ui=L.idx[u];bi=L.idx[b];br=L.table[ui][bi];assert len(br)==1 and br[0][0]==j
     c=br[0][1];rho[j]=c*(rho[ui]@rho[bi]-rho[bi]@rho[ui]);break
   assert rho[j] is not None
  total=0
  for i in range(L.n):
   for j in range(i+1,L.n):
    lhs=rho[i]@rho[j]-rho[j]@rho[i]
    rhs=sum((c*rho[k] for k,c in L.table[i][j]),np.zeros((27,27),dtype=np.int64))
    assert np.array_equal(lhs,rhs),(i,j)
    total+=1
  self.rho=rho;self.verified_brackets=total
 def derivatives(self,L,e,deg,exponents):
  a=sum((c*self.rho[i].astype(object) for i,c in e.items()),np.zeros((27,27),dtype=object))
  power=np.eye(27,dtype=object);out={}
  for m in range(1,max(exponents)+1):
   power=power@a
   if m not in exponents:continue
   vals=[]
   for j in range(L.n):
    if deg[j]!=-2*m:continue
    value=sum(power[i,k]*int(self.rho[j][k,i]) for i in range(27) for k in range(27))*(m+1)
    if value:vals.append((j,int(value)))
   out[m]=vals
  return out

class FoldLie(RootLie):
 """Pinned E6 involution / D4 triality fixed Lie algebra over the rationals."""
 def __init__(self,kind):
  if kind=='F4':
   L=RootLie('E6');perm=[5,1,4,3,2,0];orbits=[[1],[3],[2,4],[0,5]]
  elif kind=='G2':
   L=RootLie('D4');perm=[2,1,3,0];orbits=[[1],[0,2,3]]
  else:raise ValueError(kind)
  rootperm=[]
  for a in L.roots:
   b=[0]*L.r
   for i,x in enumerate(a):b[perm[i]]=x
   rootperm.append(L.idx[tuple(b)])
  signs={}
  for j in sorted(range(L.nr),key=lambda j:abs(sum(L.roots[j]))):
   a=L.roots[j];sgn=1 if sum(a)>0 else -1
   if abs(sum(a))==1:signs[j]=1;continue
   for i in range(L.r):
    u=tuple(sgn*int(k==i) for k in range(L.r));b=tuple(x-y for x,y in zip(a,u))
    if b in L.idx and abs(sum(b))<abs(sum(a)):
     ui=L.idx[u];bi=L.idx[b]
     c=L.table[ui][bi][0][1];d=L.table[rootperm[ui]][rootperm[bi]][0][1]
     signs[j]=c*d*signs[ui]*signs[bi];break
  used=set();vectors=[];roots=[]
  for i in range(L.nr):
   if i in used:continue
   v={};j=i;c=1
   while j not in v:
    v[j]=c;used.add(j);c*=signs[j];j=rootperm[j]
   assert j==i
   if c==-1:continue
   assert c==1
   vectors.append(v)
   roots.append(tuple(sum(L.roots[i][k] for k in o) for o in orbits))
  assert len(set(roots))==len(roots)
  order=sorted(range(len(roots)),key=lambda i:roots[i]);roots=[roots[i] for i in order];vectors=[vectors[i] for i in order]
  self.kind=kind;self.r=len(orbits);self.roots=roots;self.nr=len(roots);self.n=self.nr+self.r
  self.idx={a:i for i,a in enumerate(roots)}
  for o in orbits:vectors.append({L.nr+i:1 for i in o})
  self.table=[[()] * self.n for _ in range(self.n)]
  leads=[next(iter(v)) for v in vectors]
  for i in range(self.n):
   for j in range(self.n):
    b=L.bracket(vectors[i],vectors[j]);out=[];rec={}
    for k,lead in enumerate(leads):
     c=b.get(lead,0)
     if c:out.append((k,c));addto(rec,vectors[k].items(),c)
    assert rec==b
    self.table[i][j]=tuple(out)
  self.A=np.zeros((self.r,self.r),dtype=int)
  for i in range(self.r):
   for j in range(self.r):
    ri=self.idx[tuple(int(k==j) for k in range(self.r))]
    br=self.table[self.nr+i][ri]
    self.A[i,j]=br[0][1] if br else 0
  assert np.array_equal(self.A,cartan(kind)),(kind,self.A,cartan(kind))
  assert self.n==({'F4':52,'G2':14}[kind])
