"""Exhaustive certificates for B.1 finite relational countermodels.
Python standard library only. GPT-6 Astra (OpenAI), 2026-11-19.
"""
from itertools import product,combinations
from time import perf_counter

def closure(n,pairs):
 R={(i,i) for i in range(n)}|set(pairs)
 while True:
  T=R|{(i,k) for i,j in R for jj,k in R if j==jj}
  if T==R:return R
  R=T

class Magasin:
 def __init__(self,names,le_pairs,ref_pairs,edges):
  self.names=names; self.n=len(names); self.M=range(self.n)
  self.le=closure(self.n,le_pairs);self.ref=closure(self.n,ref_pairs)|self.le
  self.ref=closure(self.n,self.ref)
  self.orth=set(edges)|{(j,i) for i,j in edges}
  self.down=[frozenset(j for j in self.M if (j,i) in self.le) for i in self.M]
  self.intern={(i,j) for i,j in self.ref if not any((i,k) in self.ref and (k,j) in self.le and k!=j for k in self.M)}
  self.compat={(i,j) for i,j in product(self.M,repeat=2) if all((a,b) in self.orth for a in self.down[i]-self.down[j] for b in self.down[j]-self.down[i])}
  self.F=[frozenset(i for i in self.M if (mask>>i)&1) for mask in range(1<<self.n)]
  self.F=[f for f in self.F if all(self.down[i]<=f for i in f) and all((i,j) in self.compat for i,j in product(f,repeat=2))]
  self.Fset=set(self.F)
  self.lieux=[i for i in self.M if all(j==i for j in self.M if (j,i) in self.ref)]
 def magaxioms(self,strong=True):
  assert all((j,i) not in self.le or i==j for i,j in self.le)
  assert all((j,i) not in self.ref or i==j for i,j in self.ref)
  assert self.le<=self.ref
  for i,j in self.ref:
   c=[k for k in self.down[j] if (i,k) in self.ref]
   assert sum(all((k,l) in self.le for l in c) for k in c)==1
  assert all(i!=j and (j,i) in self.orth for i,j in self.orth)
  assert all((ii,jj) in self.orth for i,j in self.orth for ii in self.M if (ii,i) in self.intern for jj in self.M if (jj,j) in self.intern)
  if strong:assert all(i==j or (i,j) in self.orth for x in self.M for i,j in product(self.down[x],repeat=2))
  else:assert all(i==j or (i,j) in self.orth for i,j in self.le)
 def primed_axioms(self,last='strong'):
  assert all((j,i) not in self.le or i==j for i,j in self.le)
  assert all((j,i) not in self.intern or i==j for i,j in self.intern)
  assert all((i,k) in self.intern for i,j in self.intern for jj,k in self.intern if j==jj)
  assert all(i!=j and (j,i) in self.orth for i,j in self.orth)
  for x,y in product(self.M,repeat=2):
   assert sum((x,z) in self.intern and (z,y) in self.le for z in self.M)<=1
  assert all(any((xx,yy) in self.intern and (yy,y) in self.le for yy in self.M) for x,y in self.intern for xx in self.down[x])
  assert all((xx,yy) in self.orth for x,y in self.orth for xx in self.M if (xx,x) in self.intern for yy in self.M if (yy,y) in self.intern)
  if last=='strong':assert all(x==y or (x,y) in self.orth for z in self.M for x,y in product(self.down[z],repeat=2))
  elif last=='positive':assert all(x==y or (x,y) in self.orth for x,y in self.le)
  elif last=='negative':assert all(x==y or (x,y) not in self.orth for x,y in self.le)
  else:raise ValueError(last)
 def fr(self,f,g):return all(any((i,j) in self.ref for j in g) for i in f)
 def fc(self,f,g):return f|g in self.Fset
 def fd(self,f,g):return self.fc(f,g) and not f&g
 def restriction(self,f,g):return frozenset(i for i in f if self.fr(self.down[i],g))
 def subdivision(self,f,g):return self.fr(f,g) and all(self.fd(h,f)==self.fd(h,g) for h in self.F)
 def shadow(self,f):return frozenset(i for i in self.lieux if self.fr(self.down[i],f))
 def core(self):
  assert frozenset() in self.Fset
  assert all(d in self.Fset for d in self.down)
  assert all(self.fr(f,f) for f in self.F)
  assert all(not(self.fr(f,g) and self.fr(g,f)) or f==g for f,g in product(self.F,repeat=2))
  assert all(not(self.fr(f,g) and self.fr(g,h)) or self.fr(f,h) for f,g,h in product(self.F,repeat=3))
  for i,f in product(self.M,self.F):
   c=[j for j in f if (i,j) in self.ref]
   if c:assert sum(all((j,k) in self.le for k in c) for j in c)==1
  assert all(not((i,j) in self.compat and (i,j) in self.ref) or (i,j) in self.le for i,j in product(self.M,repeat=2))
  assert all(not((i,j) in self.intern and (j,k) in self.intern) or (i,k) in self.intern for i,j,k in product(self.M,repeat=3))
 def flags(self):
  l1=all(any((p,x) in self.intern for p in self.lieux) for x in self.M)
  l2=all(self.fd(self.down[x],self.down[y])==all(self.fd(self.down[p],self.down[q]) for p in self.shadow(self.down[x]) for q in self.shadow(self.down[y])) for x,y in product(self.M,repeat=2))
  l3=all(not((x,y) in self.compat and x!=y and (p,x) in self.intern and (q,y) in self.intern) or self.fd(self.down[p],self.down[q]) for x,y in product(self.M,repeat=2) for p,q in product(self.lieux,repeat=2))
  cl=all((x,y) in self.compat or not all(self.fd(self.down[p],self.down[q]) for p in self.shadow(self.down[x])-self.shadow(self.down[x]&self.down[y]) for q in self.shadow(self.down[y])-self.shadow(self.down[x]&self.down[y])) for x,y in product(self.M,repeat=2))
  supp=all(not(self.fr(g,f) and any(self.fd(y,g) and not self.fd(y,f) for y in self.F)) or any(self.fr(y,f) and self.fd(y,g) and not self.fd(y,f) for y in self.F) for f,g in product(self.F,repeat=2))
  return dict(L1=l1,L2=l2,L3=l3,CL_spac=cl,At13=supp)
 def carrier(self,h,f):
  assert self.fr(h,f)
  return {i:next(j for j in f if (i,j) in self.ref and all((j,k) in self.le for k in f if (i,k) in self.ref)) for i in h}
 def extension_bis(self,f,g,gp,h,literal=False):
  if not self.subdivision(h,f) or self.restriction(h,g)!=gp:return False
  phi=self.carrier(h,f)
  out=h-gp;target=f-g
  if {phi[i] for i in out}!=target or len(out)!=len(target):return False
  if not all(((i,j) in self.le)==((phi[i],phi[j]) in self.le) for i,j in product(out,repeat=2)):return False
  return all(((i,j) in self.le)==((phi[i],phi[j]) in self.le) for i in gp for j in (h if literal else out))
 def all_later_for_two_point(self):
  assert all(self.flags().values())
  F=self.F
  # At12: all figure refinements, stronger than the elementary formulation.
  assert all(not(self.fc(f,g) and self.fr(p,f) and self.fr(q,g) and self.fc(self.restriction(p,f&g),self.restriction(q,f&g))) or self.fc(p,q) for f,g,p,q in product(F,repeat=4))
  # At11': equality of restrictions on the overlap implies compatibility.
  assert all(not(self.fc(f,g) and self.fr(p,f) and self.fr(q,g) and self.restriction(p,f&g)==self.restriction(q,f&g)) or self.fc(p,q) for f,g,p,q in product(F,repeat=4))
  # All finite gluing diagrams reduce to finitely many distinct components;
  # explicitly enumerate assignments to each subfigure cover.
  covers=0
  for f in F:
   subs=[g for g in F if g<=f]
   for mask in range(1<<len(subs)):
    cover=[subs[i] for i in range(len(subs)) if (mask>>i)&1]
    if frozenset().union(*cover)!=f:continue
    refinements=[[h for h in F if self.fr(h,g)] for g in cover]
    for pieces in product(*refinements):
     if all(self.restriction(p,g&h)==self.restriction(q,g&h) for (g,p),(h,q) in product(zip(cover,pieces),repeat=2)):
      sols=[z for z in F if self.fr(z,f) and all(self.restriction(z,g)==p for g,p in zip(cover,pieces))]
      assert len(sols)==1;covers+=1
  exts=0
  for f,g,gp in product(F,repeat=3):
   if g<=f and self.subdivision(gp,g):
    sols=[h for h in F if self.extension_bis(f,g,gp,h)]
    assert sols;exts+=1
  print('At1--At13, At14 and At14bis existence PASS; all finite gluing diagrams',covers,'extension diagrams',exts)
  f=frozenset({1});g=gp=frozenset()
  sols=[h for h in F if self.extension_bis(f,g,gp,h,literal=True)]
  assert len(sols)==2
  print('At14bis uniqueness FAIL, even literal cross-order condition:',[[self.names[i] for i in h] for h in sols])

def run():
 t=perf_counter()
 tiny=Magasin(['a','x'],[],[(0,1)],[]);tiny.magaxioms();tiny.core();tiny.all_later_for_two_point()
 l2=Magasin(['a','x','b','y'],[(0,1),(2,3)],[],[(0,1),(2,3),(0,2)]);l2.magaxioms();l2.core();print('Mag1--4, nonlocal four-object model',l2.flags());assert not l2.flags()['L2']
 cl=Magasin(['a','x','y'],[(0,1),(0,2)],[],[(0,1),(0,2)]);cl.magaxioms();cl.core();print('Mag1--4, three-object absolute compatibility model',cl.flags());assert not cl.flags()['CL_spac']
 weak=Magasin(['y','z','t'],[(0,2),(1,2)],[],[(0,2),(1,2)]);weak.magaxioms(False);weak.primed_axioms('positive')
 assert weak.intern=={(i,i) for i in range(3)}
 assert weak.down[2] not in weak.Fset
 print('weak Mag1\'--4\' PASS; two-strata Mag4 FAIL; principal deployment of t is not a figure')
 negative=Magasin(['a','t'],[(0,1)],[],[]);negative.primed_axioms('negative')
 assert (0,1) not in negative.orth
 print('negative-reading Mag1\'--4\' PASS on two-element chain; strong Mag4 FAIL')
 div=Magasin(['a','b','c','t'],[(0,3),(1,3)],[(2,3)],[(0,2),(1,2),(0,3),(1,3)])
 div.magaxioms(False)
 assert div.flags()['L1'];assert div.down[3] not in div.Fset
 print('weak Magdiv3 + divisibility PASS; principal deployment of t is not a figure')
 ext=Magasin(['a','b','c','d'],[(0,1),(1,2)],[],[(0,1),(0,2),(1,2),(0,3),(1,3)])
 ext.magaxioms();ext.core()
 f,g,gp=ext.down[2],ext.down[1],ext.down[0]
 assert ext.subdivision(gp,g)
 extensions=[h for h in ext.F if ext.subdivision(h,f) and ext.restriction(h,g)==gp]
 assert not extensions
 print('Mag1--4 four-object extension countermodel PASS; At14 FAIL; figures',len(ext.F),'Gprime=a subdivides G=b, F=c has no extension')
 divlocal=Magasin(['p','q','x','y'],[],[(0,2),(1,3)],[(0,1)])
 divlocal.magaxioms();divlocal.core()
 assert divlocal.flags()['L1'] and not divlocal.flags()['L2'] and not divlocal.flags()['CL_spac']
 print('Mag1--4 plus divisibility PASS; L2 and CL(spac) FAIL:',divlocal.flags())
 # This is a prime core, deliberately not a magasin: δ has no edges.
 glue=Magasin(['x','y','q'],[(0,1)],[(2,1)],[]);glue.core()
 assert glue.flags()['L1'] and glue.flags()['L2'] and glue.flags()['CL_spac'] and not glue.flags()['L3']
 counts=0
 for f in glue.F:
  ss=[g for g in glue.F if g<=f]
  for mask in range(1<<len(ss)):
   cover=[ss[i] for i in range(len(ss)) if mask>>i&1]
   if frozenset().union(*cover)!=f:continue
   for pieces in product(*[[h for h in glue.F if glue.fr(h,g)] for g in cover]):
    if all(glue.restriction(p,g&h)==glue.restriction(q,g&h) for (g,p),(h,q) in product(zip(cover,pieces),repeat=2)):
     sol=[z for z in glue.F if glue.fr(z,f) and all(glue.restriction(z,g)==p for g,p in zip(cover,pieces))]
     assert len(sol)==1;counts+=1
 assert all(not(glue.fd(f,g) and glue.fr(p,f) and glue.fr(q,g)) or glue.fd(p,q) for f,g,p,q in product(glue.F,repeat=4))
 assert not glue.fd(glue.down[0],glue.down[2])
 assert glue.fd(glue.restriction(glue.down[0],glue.down[0]),glue.restriction(glue.down[2],glue.down[0]))
 print('Prime At1--7, L1,L2,CL(spac),D0,At11 PASS; AtD and L3 FAIL; gluing diagrams',counts)
 def spatial_data(m):
  def perp(A):return frozenset(x for x in m.M if all((x,a) in m.orth for a in A))
  labels={i:perp(perp({i})) for i in m.M}
  deployments={x:(frozenset(labels[i] for i in m.down[x]),frozenset((labels[i],labels[j]) for i,j in product(m.down[x],repeat=2) if (i,j) in m.le)) for x in m.M}
  assert all(labels[i] for i in m.M)
  assert all(i==j or (labels[i]!=labels[j] and all((a,b) in m.orth for a in labels[i] for b in labels[j])) for x in m.M for i,j in product(m.down[x],repeat=2))
  return labels,deployments
 labels,deployments=spatial_data(tiny)
 assert labels[0]==labels[1]==frozenset(tiny.M) and deployments[0]==deployments[1]
 print('Strong local Mag plus At14bis existence does not imply typed Atspat3: two-object deployments coincide')
 spatial=Magasin(['a','t'],[(0,1)],[],[(0,1)]);spatial.magaxioms();spatial.core()
 labels,deployments=spatial_data(spatial)
 assert labels=={0:frozenset({0}),1:frozenset({1})}
 assert len(set(deployments.values()))==2
 spatial_internal=set()
 for x,y in product(spatial.M,repeat=2):
  choices={i:[j for j in spatial.down[y] if labels[i]<=labels[j]] for i in spatial.down[x]}
  if any(len(c)!=1 for c in choices.values()):continue
  carrier={i:c[0] for i,c in choices.items()}
  if carrier[x]==y and all((carrier[i],carrier[j]) in spatial.le for i,j in product(spatial.down[x],repeat=2) if (i,j) in spatial.le):
   spatial_internal.add((x,y))
 assert spatial_internal==spatial.intern and not spatial.flags()['L1']
 print('Typed Atspat1--3 two-element incidence chain PASS; reconstructed internal order identity; divisibility FAIL')
 print('seconds',perf_counter()-t)
if __name__=='__main__':run()
