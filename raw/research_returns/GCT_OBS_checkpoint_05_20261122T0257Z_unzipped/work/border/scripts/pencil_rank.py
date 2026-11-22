"""Exact projective-line rank stratification for a new homogeneous vector.

All fixed columns are eliminated over Q.  A selected square minor in every
weight block gives a generic rank lower bound.  The only exceptional points
are roots of those minors, plus infinity.  Ranks at irreducible polynomial
roots are computed in Q[t]/(f), so no roots are sampled or numerically rounded.
SymPy is used only for univariate polynomial arithmetic and determinants.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
import math
import sympy as sp
from br_linear import Space,add,rank

t=sp.Symbol('t')

def wp(v,f,I):
 out={};si=set(I)
 for (a,b),x in v.items():
  z,o=(a,b) if f==1 else (b,a)
  if z in si:continue
  key=(tuple(sorted(I+(z,))),o)
  out[key]=out.get(key,0)+x*((-1)**sum(i<z for i in I))
 return {k:x for k,x in out.items() if x}

def pencil_blocks(E0,X,Y,M,f,p):
 weights=M['aw'] if f==1 else M['bw'];dim=len(weights)
 Is=list(combinations(range(dim),p));iw={I:tuple(sum(weights[i][z] for i in I) for z in range(8)) for I in Is}
 spaces=defaultdict(Space)
 def wt(v):
  a,b=next(iter(v));w=add(M['aw'][a],M['bw'][b]);assert all(add(M['aw'][a],M['bw'][b])==w for a,b in v);return w
 for v in E0:
  w=wt(v)
  for I in Is:spaces[add(w,iw[I])].append(wp(v,f,I))
 assert wt(X)==wt(Y);w=wt(X);blocks=defaultdict(list)
 for I in Is:
  s=spaces[add(w,iw[I])]
  blocks[add(w,iw[I])].append((s.reduce(wp(X,f,I)),s.reduce(wp(Y,f,I))))
 return sum(s.rank() for s in spaces.values()),list(blocks.values()),math.comb(dim-1,p)

def combine(v,w,a):
 out={k:x+a*w.get(k,0) for k,x in v.items()}
 for k,x in w.items():
  if k not in v:out[k]=a*x
 return {k:x for k,x in out.items() if x}

def selected_minor(block):
 best=None
 for val in (0,1,-1,2):
  ss=Space();chosen=[]
  for j,(v,w) in enumerate(block):
   if ss.append(combine(v,w,val)):chosen.append(j)
  if best is None or ss.rank()>best[0]:best=(ss.rank(),chosen,sorted(ss.rows))
 r,cols,rows=best
 if not r:return 0,sp.Poly(1,t,domain=sp.QQ)
 mat=sp.Matrix([[sp.Rational(block[j][0].get(i,0))+t*sp.Rational(block[j][1].get(i,0)) for j in cols] for i in rows])
 determinant=sp.Poly(mat.det(method='domain-ge'),t,domain=sp.QQ)
 assert not determinant.is_zero
 return r,determinant

def field_rank(block,mod):
 """Rank over Q[t]/(monic irreducible mod); works also for degree one."""
 rows={};zero=sp.Poly(0,t,domain=sp.QQ)
 for v,w in block:
  col={k:sp.Poly(sp.Rational(v.get(k,0))+t*sp.Rational(w.get(k,0)),t,domain=sp.QQ).rem(mod) for k in v.keys()|w.keys()}
  col={k:x for k,x in col.items() if not x.is_zero}
  for pivot,row in sorted(rows.items()):
   x=col.get(pivot,zero)
   if x.is_zero:continue
   for k,y in row.items():
    z=(col.get(k,zero)-x*y).rem(mod)
    if z.is_zero:col.pop(k,None)
    else:col[k]=z
  if not col:continue
  pivot=min(col);inv=sp.invert(col[pivot],mod)
  rows[pivot]={k:(x*inv).rem(mod) for k,x in col.items()}
 return len(rows)

def rank_at(blocks,mod):
 if mod=='infinity':return sum(rank([w for v,w in block]) for block in blocks)
 if mod.degree()==1:
  val=Fraction(-mod.nth(0)/mod.nth(1))
  return sum(rank([combine(v,w,val) for v,w in block]) for block in blocks)
 return sum(field_rank(block,mod) for block in blocks)

def stratify(E0,X,Y,M,f,p,target=17):
 base,blocks,cost=pencil_blocks(E0,X,Y,M,f,p);generic=base;factors={}
 for block in blocks:
  r,d=selected_minor(block);generic+=r
  for fac,multiplicity in sp.factor_list(d)[1]:
   fac=fac.monic();factors[str(fac.as_expr())]=fac
 out={'factor':f,'p':p,'base_rank':base,'generic_rank_lower':generic,'pure_cost':cost,'threshold':target*cost}
 if generic<=target*cost:return {**out,'status':'INCONCLUSIVE'}
 exceptions=[];allowed=[]
 for key,fac in sorted(factors.items()):
  r=base+rank_at(blocks,fac);exceptions.append({'polynomial':key,'rank':r})
  if r<=target*cost:allowed.append(key)
 r=base+rank_at(blocks,'infinity');exceptions.append({'polynomial':'infinity','rank':r})
 if r<=target*cost:allowed.append('infinity')
 return {**out,'exceptions':exceptions,'allowed':allowed,'status':'FINITE' if allowed else 'EXCLUDED'}

def verify_at(E0,X,Y,M,f,p,point):
 base,blocks,cost=pencil_blocks(E0,X,Y,M,f,p)
 mod='infinity' if point=='infinity' else sp.Poly(sp.sympify(point),t,domain=sp.QQ)
 return base+rank_at(blocks,mod),cost
