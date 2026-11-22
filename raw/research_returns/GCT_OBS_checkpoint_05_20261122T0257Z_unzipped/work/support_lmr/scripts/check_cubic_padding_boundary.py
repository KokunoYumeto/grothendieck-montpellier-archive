#!/usr/bin/env python3
"""Exact S-008 character and polarized-coefficient checks; stdlib only."""
from collections import Counter
from itertools import combinations_with_replacement, permutations
from math import comb
import argparse
import json
from pathlib import Path

generators=[(a,b,9-a-b) for a in range(10) for b in range(10-a)]
weights=Counter(tuple(sum(g[i] for g in triple) for i in range(3))
                for triple in combinations_with_replacement(generators,3))
assert sum(weights.values())==comb(57,3)
def multiplicity(shape):
    value=0
    for p in permutations(range(3)):
        sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        target=tuple(shape[i]+p[i]-i for i in range(3))
        value+=sign*weights[target]
    return value
expected={(9,9,9):0,(10,9,8):0,(10,10,7):1,(11,8,8):1,
          (11,9,7):0,(11,10,6):0,(11,11,5):0}
for shape,value in expected.items():assert multiplicity(shape)==value

# Variables: a0,a1,b0,b1,b2,c0,c2. We have specialized a2=c1=0.
zero=(0,)*7
def term(*indices):
    m=[0]*7
    for i in indices:m[i]+=1
    return {tuple(m):1}
def add(a,b):
    c=dict(a)
    for m,v in b.items():c[m]=c.get(m,0)+v
    return {m:v for m,v in c.items() if v}
def scale(a,c):return {m:v*c for m,v in a.items() if v*c}
def mul(a,b):
    c={}
    for m,v in a.items():
        for n,w in b.items():
            k=tuple(x+y for x,y in zip(m,n));c[k]=c.get(k,0)+v*w
    return {m:v for m,v in c.items() if v}
def power(a,n):
    out={zero:1}
    for _ in range(n):out=mul(out,a)
    return out
E=add(term(0,3),scale(term(1,2),-1))
Delta=add(mul(term(6),E),term(1,4,5))
G1=mul(mul(power(Delta,7),E),term(1,3,5,5))
G2=mul(power(Delta,8),term(0,2,5))
m1=(4,5,2,5,2,4,5)
m2=(3,6,4,2,3,4,5)
assert G1[m1]==315==comb(7,2)*comb(6,2)
assert G2[m2]==-560==-comb(8,3)*comb(5,3)
assert all(m[i]>=2 for m in (m1,m2) for i in (0,2,5))
exception=scale(mul(power(E,8),term(0,2)),2)
assert exception[(6,3,4,5,0,0,0)]==-112==-2*comb(8,3)
assert 6>=3 and 4>=3
result={"status":"PASS","Sym3Sym9_multiplicities":{str(k):v for k,v in expected.items()},
       "cubic_restriction_coefficients":[315,-560],
       "weight28_exception_restriction_coefficient":-112,
       "weight_count_total":sum(weights.values())}
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,default=Path('work/support_lmr/results/cubic_padding_boundary.json'))
args=parser.parse_args()
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

