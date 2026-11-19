"""Finite countermodel checks for cote 156. GPT-6 Astra, 2026-11-19.
All checks are exhaustive over the explicitly listed structures, not sampling.
"""
from itertools import combinations,product
from pathlib import Path
import json,time

class SetFigures:
 def __init__(self,shapes,strict=True):
  self.shapes={k:frozenset(frozenset(a) for a in v) for k,v in shapes.items()}
  self.names=tuple(shapes);self.M=range(len(shapes));self.n=len(shapes)
  self.S=[self.shapes[x] for x in self.names]
  self.support=[frozenset().union(*s) for s in self.S]
  self.le=[[self.sub(self.S[i],self.S[j]) for j in self.M] for i in self.M]
  self.down=[sum(1<<j for j in self.M if self.le[j][i]) for i in self.M]
  self.ref=[[self.refine(self.S[i],self.S[j]) for j in self.M] for i in self.M]
  self.R=[]
  for i in self.M:
   row=[]
   for j in self.M:
    inter=self.down[i]&self.down[j]
    elementary=inter==0 or any(inter==d for d in self.down)
    row.append(self.compat(self.S[i],self.S[j]) and (elementary or not strict))
   self.R.append(row)
  self.figures=[f for f in range(1<<self.n) if all(self.down[i]&~f==0 for i in self.bits(f)) and all(self.R[i][j] for i in self.bits(f) for j in self.bits(f))]
  self.fset=set(self.figures)
 def bits(self,f):return [i for i in self.M if (f>>i)&1]
 @staticmethod
 def residual(S,a):return a-frozenset().union(*(b for b in S if b<a))
 @staticmethod
 def admissible(S):
  if any(not SetFigures.residual(S,a) for a in S):return False
  u=frozenset().union(*S)
  return all(any(x in a and all(a<=b for b in S if x in b) for a in S) for x in u)
 @staticmethod
 def sub(S,T):return S<=T and all(b in S for a in S for b in T if b<=a)
 @staticmethod
 def compat(S,T):return SetFigures.admissible(S|T) and SetFigures.sub(S,S|T) and SetFigures.sub(T,S|T)
 @staticmethod
 def refine(S,T):
  if not frozenset().union(*S)<=frozenset().union(*T):return False
  carrier={}
  for a in S:
   choices=[b for b in T if SetFigures.residual(S,a)<=SetFigures.residual(T,b)]
   if len(choices)!=1:return False
   carrier[a]=choices[0]
  return all(carrier[a]<=carrier[b] for a in S for b in S if a<=b)
 def fref(self,f,g):return all(any(self.ref[i][j] for j in self.bits(g)) for i in self.bits(f))
 def fc(self,f,g):return f|g in self.fset
 def internal(self,i,j):return self.ref[i][j] and not any(k!=j and self.le[k][j] and self.ref[i][k] for k in self.M)
 def restrict(self,f,g):return sum(1<<i for i in self.bits(f) if any(self.ref[i][j] for j in self.bits(g)))
 def check(self):
  n=self.n;M=self.M;F=self.figures
  assert all(self.admissible(s) for s in self.S)
  assert all(self.down[i] in self.fset for i in M)
  assert 0 in self.fset
  assert all((f&g in self.fset and (f|g in self.fset if any((f|g)&~h==0 for h in F) else True)) for f,g in product(F,repeat=2))
  assert all(self.fref(f,f) for f in F)
  assert all(not(self.fref(f,g) and self.fref(g,f)) or f==g for f,g in product(F,repeat=2))
  assert all(not(self.ref[i][j] and self.ref[j][k]) or self.ref[i][k] for i,j,k in product(M,repeat=3))
  assert all(not(self.le[i][j]) or self.ref[i][j] for i,j in product(M,repeat=2))
  assert all(not(self.R[i][j] and self.ref[i][j]) or self.le[i][j] for i,j in product(M,repeat=2))
  assert all(not(self.internal(i,j) and self.internal(j,k)) or self.internal(i,k) for i,j,k in product(M,repeat=3))
  for i,f in product(M,F):
   above=[j for j in self.bits(f) if self.ref[i][j]]
   if above:assert sum(all(self.le[j][k] for k in above) for j in above)==1
  lieux=[i for i in M if all(not self.ref[j][i] or j==i for j in M)]
  assert all(any(self.internal(l,i) for l in lieux) for i in M)
  def disj(i,j):return self.R[i][j] and self.down[i]&self.down[j]==0
  assert all(disj(i,j)==all(disj(a,b) for a in lieux if self.ref[a][i] for b in lieux if self.ref[b][j]) for i,j in product(M,repeat=2))
  assert all(not(self.R[i][j] and i!=j and self.internal(a,i) and self.internal(b,j)) or disj(a,b) for i,j in product(M,repeat=2) for a,b in product(lieux,repeat=2))
  for i,j in product(M,repeat=2):
   k=self.down[i]&self.down[j]
   ombk=[l for l in lieux if self.fref(self.down[l],k)]
   cond=all(disj(a,b) for a in lieux if self.ref[a][i] and a not in ombk for b in lieux if self.ref[b][j] and b not in ombk)
   sigma=k==0 or k in self.down
   assert self.R[i][j]==(cond and sigma)
  print('objects',self.names)
  print('figures',len(F),'lieux',[self.names[i] for i in lieux])
  print('At 1--8, At 9, At 10, At 9_Sigma (Sigma=empty or posets with top): PASS')
  refinements={f:[p for p in F if self.fref(p,f)] for f in F}
  restrictions={(p,k):self.restrict(p,k) for p in F for k in F}
  for f,g in product(F,repeat=2):
   if not self.fc(f,g):continue
   k=f&g
   for p,q in product(refinements[f],refinements[g]):
    rp,rq=restrictions[p,k],restrictions[q,k]
    if self.fc(rp,rq) and rp&rq==0:
     assert self.fc(p,q) and p&q==0
    if rp==rq:assert self.fc(p,q)
  print('At D and At11prime for every compatible figure pair and every refining figure pair: PASS')
  for i,j,p,q in product(M,repeat=4):
   if self.R[i][j] and self.ref[p][i] and self.ref[q][j]:
    k=self.down[i]&self.down[j]
    rp,rq=self.restrict(self.down[p],k),self.restrict(self.down[q],k)
    if self.fc(rp,rq) and not self.R[p][q]:
     print('At 12 FAIL',dict(X=self.names[i],Y=self.names[j],Xp=self.names[p],Yp=self.names[q],K=[self.names[t] for t in self.bits(k)],Xp_K=[self.names[t] for t in self.bits(rp)],Yp_K=[self.names[t] for t in self.bits(rq)]))
     return
  raise AssertionError('expected failure')

if __name__=='__main__':
 start=time.perf_counter()
 shapes={x:[x] for x in 'abcp'}
 shapes.update(k=['a','b','abc'],x=['a','b','abc','abcp'],xp=['a','b','abp'])
 m=SetFigures(shapes);m.check()
 print('seconds',time.perf_counter()-start)
