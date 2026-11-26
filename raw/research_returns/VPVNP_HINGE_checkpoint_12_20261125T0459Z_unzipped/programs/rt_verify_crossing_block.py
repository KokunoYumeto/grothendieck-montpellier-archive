#!/usr/bin/env python3
"""Independent full 16^4-dimensional check of the n=4,q=2 witness.

Uses the explicit S4 character chi_(211)(g)=sgn(g)(fix(g)-1),
not the generator's character recursion or Gram quotient matrices.
"""
import itertools,json,math,hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np

work=Path(__file__).resolve().parents[1]
src=work/'outputs/pg_crossing_n4_exact.json'
data=json.loads(src.read_text())
assert (data['n'],data['q'],data['partition'])==(4,2,[2,1,1])
perms=list(itertools.permutations(range(4)))
def mul(p,q):return tuple(p[q[j]] for j in range(4))
def inv(p):return tuple(p.index(j) for j in range(4))
def act(p,x):return sum(((x>>j)&1)<<p[j] for j in range(4))
def orbit(p,q):
 return sorted({(mul(mul(g,p),inv(g)),mul(mul(g,q),inv(g))) for g in perms})
terms=[]
for (p,q),row in zip(data['basis_orbit_representatives'],data['common_projection_coordinates']):
 orb=orbit(tuple(p),tuple(q));coef=Fraction(row[0])/len(orb)
 for a,b in orb:terms.append((a,b,coef))
denom=math.lcm(*(c.denominator for a,b,c in terms))
v=np.zeros((16,16,16,16),dtype=np.int64)
for a,b,c in terms:
 z=int(c*denom)
 for x in range(16):
  for y in range(16):v[act(a,x),act(b,y),x,y]+=z
def project_scaled(axes):
 out=np.zeros_like(v)
 for g in perms:
  inversions=sum(g[i]>g[j] for i in range(4) for j in range(i+1,4))
  chi=(-1)**inversions*(sum(g[j]==j for j in range(4))-1)
  if not chi:continue
  pg=inv(g);idx=np.array([act(pg,x) for x in range(16)])
  a=np.take(v,idx,axis=axes[0]);a=np.take(a,idx,axis=axes[1])
  out+=chi*a
 return out
ab=project_scaled((0,1));ad=project_scaled((0,3))
assert np.array_equal(ab,8*v)
assert np.array_equal(ad,8*v)
# Python integers keep the norm check independent of fixed-width overflow.
norm=Fraction(sum(int(x)**2 for x in v.flat),denom**2)
inner=Fraction(sum(int(v[x,y,x,y]) for x in range(16) for y in range(16)),denom)
assert norm==inner==18
result={'status':'PASS','source':str(src.relative_to(work)),
 'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'ambient_dimension':16**4,'integer_denominator':denom,
 'projector_AB_check':True,'projector_AD_check':True,
 'projection_squared_norm':str(norm),'psi_inner_product':str(inner),
 'method':'Explicit full tensor coordinates and S4 character sign*(fixed_points-1); no generator matrices or recursion imported.',
 'scope':'Finite-block raw endpoint only. No lower bound on semiring power regularization.'}
out=work/'outputs/rt_crossing_block_verification.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
