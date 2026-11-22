"""Integral projections and Koszul maps of tautological extension tensors."""
import math,random
from itertools import combinations
from br_linear import Space

PRIME=1000003

def fixed_projection(n,d=7,seed=0,factor=2):
 rng=random.Random(20261122+seed+d+factor)
 return [[rng.randrange(-3,4) for _ in range(n)] for z in range(d)]

def columns(v,P,f,p):
 d=len(P)
 for I in combinations(range(d),p):
  out={}
  for (a,b),x in v.items():
   h,o=(a,b) if f==1 else (b,a)
   for z in range(d):
    if z in I or not P[z][h]:continue
    key=tuple(sorted(I+(z,))),o
    out[key]=out.get(key,0)+x*P[z][h]*(-1)**sum(i<z for i in I)
  yield {k:x for k,x in out.items() if x}

def modular(v,prime=PRIME):
 return {k:(x.numerator*pow(x.denominator,-1,prime))%prime if hasattr(x,'denominator') else x%prime for k,x in v.items()}

def projected_extension_rank(E,P,f,p,prime=PRIME):
 s=Space(prime)
 for v in E:
  for col in columns(v,P,f,p):s.append(modular(col,prime) if prime else col)
 return s.rank()
