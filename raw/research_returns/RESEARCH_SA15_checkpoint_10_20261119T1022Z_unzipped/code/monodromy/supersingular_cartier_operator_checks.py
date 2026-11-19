#!/usr/bin/env python3
"""Local exact Cartier identities and a bounded non-extrapolation check.

The finite symmetrizer list does not claim a theorem for untested degrees.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
x,z,a,b,c,e=sp.symbols('x z a b c e');vs=(x,z,a,b,c,e)
def mod2(f):return sp.Poly(sp.expand(f),*vs,modulus=2).as_expr()
def Cartier(f):
 ans=0
 for powers,coeff in sp.Poly(f,*vs,modulus=2).terms():
  if not(powers[0]%2 and powers[1]%2):continue
  assert all(v%2==0 for v in powers[2:])
  new=((powers[0]-1)//2,(powers[1]-1)//2)+tuple(v//2 for v in powers[2:])
  ans+=int(coeff)*sp.prod(v**q for v,q in zip(vs,new))
 return mod2(ans)
s=a*a+x*b*b+z*c*c+x*z*e*e
D1=sp.diff(s,x);D2=sp.diff(s,z);D12=sp.diff(D1,z)
assert Cartier(s*s)==0
assert Cartier(s*D1)==0 and Cartier(s*D2)==0
assert Cartier(s*D12)==D12
assert mod2(sp.diff(D1,x))==0 and mod2(sp.diff(D2,z))==0

def mulE(u,v):
 i,j=u;k,l=v
 if j+l<2:return {(i+k,j+l)}
 return {(i+k,1),(i+k+3,0)}
def CartE(poly):
 out=set()
 for i,j in poly:
  t=None
  if j:t=((i-1)//2,1) if i%2 else(i//2+1,0)
  elif i%2:t=((i-1)//2,0)
  if t is not None:
   if t in out:out.remove(t)
   else:out.add(t)
 return out
checks=[]
for m in (3,5,7,9,11,13):
 B=[(i,0) for i in range(m//2+1)]+[(i,1) for i in range((m-3)//2+1)]
 bi={v:i for i,v in enumerate(B)};rows={}
 for u in B:
  C=[[0]*m for _ in range(m)]
  for j,v in enumerate(B):
   for w in CartE(mulE(u,v)):C[bi[w]][j]^=1
  # Unknown R; impose R*C symmetric with zero diagonal, for every u.
  for j in range(m):
   for k in range(j,m):
    eq=0
    for h in range(m):
     if C[h][k]:eq^=1<<(j*m+h)
     if j!=k and C[h][j]:eq^=1<<(k*m+h)
    while eq:
     at=eq.bit_length()-1
     if at in rows:eq^=rows[at]
     else:rows[at]=eq;break
 checks.append({'pole_degree':m,'constant_alternating_symmetrizer_space_dimension':m*m-len(rows)})
assert [q['constant_alternating_symmetrizer_space_dimension'] for q in checks]==[1,0,0,0,0,0]
out={'local_fixed_operator_identities':{'identity':0,'delta1':0,'delta2':0,'delta1delta2':'delta1delta2'},
 'scope':'Universal local polynomial identities; bounded exact one-factor linear-system probe only',
 'constant_alternating_symmetrizer_checks':checks,
 'all_assertions_passed':True,'runtime_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'supersingular_cartier_operator_checks.json'
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
