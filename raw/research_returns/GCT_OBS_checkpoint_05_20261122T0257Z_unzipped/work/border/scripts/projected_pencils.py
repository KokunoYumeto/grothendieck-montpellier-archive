"""Exact projected Koszul pencils; constant columns use SymPy DomainMatrix.

Eliminating the constant part first keeps rational-function arithmetic in
the small remaining quotient. This file does not assume generic ranks are
uniform: all determinant roots and infinity must still be checked.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix
from br_linear import Space,rank
from extension_projection import columns,fixed_projection
from pencil_rank import selected_minor,rank_at,t

def qconvert(x):
 if hasattr(getattr(x,'numer',None),'degree'):
  assert x.numer.degree()<=0 and x.denom.degree()<=0
  return QQ.convert(x.as_expr())
 if hasattr(x,'to_list'):
  coefficients=x.to_list();assert len(coefficients)<=1
  return coefficients[0] if coefficients else QQ.zero
 return QQ.convert(x)

def constant(v):
 def ok(x):
  if hasattr(getattr(x,'numer',None),'degree'):return x.numer.degree()<=0 and x.denom.degree()<=0
  if hasattr(x,'to_list'):return len(x.to_list())<=1
  return True
 return all(ok(x) for x in v.values())

@lru_cache(maxsize=128)
def fixed_rref(vectors,P,f,p,otherdim):
 vectors=[dict(v) for v in vectors];P=[list(v) for v in P]
 keys=[(J,o) for J in combinations(range(len(P)),p+1) for o in range(otherdim)];index={v:i for i,v in enumerate(keys)}
 rows=[]
 for v in vectors:
  for col in columns(v,P,f,p):
   row=[QQ.zero]*len(keys)
   for k,x in col.items():row[index[k]]=qconvert(x)
   rows.append(row)
 dm=DomainMatrix.from_list(rows,QQ);reduced,pivots=dm.rref();R=reduced.to_list();free=tuple(i for i in range(len(keys)) if i not in pivots)
 return keys,index,pivots,free,[[R[j][i] for i in free] for j in range(len(pivots))]

def projected_blocks(E0,X,Y,M,f=2,p=3,K=None,KS=None,remember=None):
 dim=len(M['bw']) if f==2 else len(M['aw']);otherdim=len(M['aw']) if f==2 else len(M['bw']);P=fixed_projection(dim,2*p+1,0,f)
 const=[v for v in E0 if constant(v)];variable=[v for v in E0 if not constant(v)]
 vectors=tuple(tuple(sorted((k,qconvert(x)) for k,x in v.items())) for v in const)
 keys,index,pivots,free,R=fixed_rref(vectors,tuple(tuple(v) for v in P),f,p,otherdim)
 if K:
  R=[[K.convert(x) for x in row] for row in R]
  if remember:
   for v in variable+[X,Y]:
    for x in v.values():remember(K.convert(x))
 else:R=[[Fraction(int(x.numerator),int(x.denominator)) for x in row] for row in R]
 zero=K.zero if K else Fraction(0)
 def convert(x):return K.convert(x) if K else Fraction(x)
 def project(v):
  v={index[k]:convert(x) for k,x in v.items()};out={j:v.get(i,zero) for j,i in enumerate(free) if v.get(i,zero)}
  for i,row in zip(pivots,R):
   x=v.get(i,zero)
   if not x:continue
   for j,y in enumerate(row):
    if y:out[j]=out.get(j,zero)-x*y
  return {j:x for j,x in out.items() if x}
 s=KS() if K else Space()
 for v in variable:
  for col in columns(v,P,f,p):s.append(project(col))
 B=[(s.reduce(project(a)),s.reduce(project(b))) for a,b in zip(columns(X,P,f,p),columns(Y,P,f,p))]
 from math import comb
 return len(pivots)+s.rank(),[B],comb(2*p,p)

def stratify_projected(E0,X,Y,M):
 base,B,cost=projected_blocks(E0,X,Y,M);generic=base;factors={}
 # The sample rank first avoids computing a determinant when no exclusion follows.
 from pencil_rank import combine
 rr=max(rank([combine(v,w,z) for v,w in B[0]]) for z in (0,1,-1,2))
 if base+rr<=17*cost:return {'status':'OPEN','generic_rank_lower':base+rr,'base_rank':base,'cost':cost}
 r,det=selected_minor(B[0]);generic+=r
 for fac,n in sp.factor_list(det)[1]:fac=fac.monic();factors[str(fac.as_expr())]=fac
 allowed=[];exceptions=[]
 for key,fac in sorted(factors.items()):
  rk=base+rank_at(B,fac);exceptions.append({'polynomial':key,'rank':rk})
  if rk<=17*cost:allowed.append(key)
 rk=base+rank_at(B,'infinity');exceptions.append({'polynomial':'infinity','rank':rk})
 if rk<=17*cost:allowed.append('infinity')
 return {'status':'FINITE' if allowed else 'EXCLUDED','generic_rank_lower':generic,'base_rank':base,'cost':cost,'exceptions':exceptions,'allowed':allowed}
