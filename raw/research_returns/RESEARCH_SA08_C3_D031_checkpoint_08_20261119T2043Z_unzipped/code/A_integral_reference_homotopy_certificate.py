"""Finite supplement to AT28, not a substitute for its all-index proof.
Checks actual coordinate PD/cochain projections in a truncated free even
identity disk, and every monotone naturality square through n=5,m=4.
The obstruction itself is the independently certified AT11--AT12 example.
"""
from itertools import combinations_with_replacement
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json,time,hashlib
start=time.perf_counter(); checks=0
B=[(a,e) for e in (0,1) for a in range(5-e)]
def clean(x): return {k:v for k,v in x.items() if v}
def add(x,y):
 z=dict(x)
 for k,v in y.items(): z[k]=z.get(k,0)+v
 return clean(z)
def scale(x,c): return clean({k:c*v for k,v in x.items()})
def mul(x,y):
 z={}
 for (a,e),v in x.items():
  for (b,f),w in y.items():
   if e+f>1 or a+b+e+f>4: continue
   key=(a+b,e+f); z[key]=z.get(key,0)+v*w*comb(a+b,a)
 return clean(z)
def diff(x):
 z={}
 for (a,e),v in x.items():
  if not e and a: z[(a-1,1)]=v
 return clean(z)
def proj(x,bit): return x if bit else clean({(0,0):x.get((0,0),0)})
def gamma(x,n):
 z={(0,0):Fraction(1)}
 for _ in range(n): z=mul(z,x)
 return scale(z,Fraction(1,factorial(n)))
def eq(a,b):
 global checks
 assert a==b,(a,b); checks+=1
for bit in (0,1):
 for k in B:
  x={k:1}; eq(diff(proj(x,bit)),proj(diff(x),bit))
  for l in B:
   y={l:1}; eq(proj(mul(x,y),bit),mul(proj(x,bit),proj(y,bit)))
 for x in [{(1,0):1},{(2,0):1},{(1,0):1,(2,0):2,(3,0):-1}]:
  for n in range(1,5):
   gx=gamma(x,n)
   assert all(v.denominator==1 for v in gx.values()); checks+=1
   eq(proj(gx,bit),gamma(proj(x,bit),n))
for n in range(6):
 triples_n=list(combinations_with_replacement(range(n+1),3))
 alphas=[tuple([0]*k+[1]*(n+1-k)) for k in range(n+2)]
 for alpha in alphas:
  mask={t:alpha[t[0]] for t in triples_n}
  eq({t:mask[t]*mask[t] for t in triples_n},mask)
  if all(a==0 for a in alpha): eq(set(mask.values()),{0})
  if all(a==1 for a in alpha): eq(set(mask.values()),{1})
  for m in range(5):
   triples_m=list(combinations_with_replacement(range(m+1),3))
   for eta in combinations_with_replacement(range(n+1),m+1):
    alpha_eta=tuple(alpha[eta[i]] for i in range(m+1))
    for t in triples_m:
     pulled=tuple(eta[i] for i in t)
     eq(mask[pulled],alpha_eta[t[0]])
record={'statement':'AT28','scope':'Finite actual PD/cochain projection and monotone-coordinate naturality supplement; all-prime noncompletion uses AT11--AT12 proof and its independent certificate.','checks':checks,'max_target_simplex':5,'max_source_simplex':4,'truncated_PD_disk_arity':4,'result':'PASS','runtime_seconds':time.perf_counter()-start}
path=Path(__file__).resolve().parents[1]/'logs/A_integral_reference_homotopy_certificate.json'
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
