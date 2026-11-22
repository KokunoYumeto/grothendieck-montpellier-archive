#!/usr/bin/env python3
"""Exact norm, transverse-union, and degree-range identities for mixed products.

The geometric existence and Cartier upper bound are proved in the TeX file;
these finite calculations do not establish existence by extrapolation.
"""
from pathlib import Path
from time import perf_counter
import json
start=perf_counter()
odd_norm=[]
for c in range(1,65,2):
    for e in range(1,65):
        nodes=9*(c*e-1)
        genus=10+nodes
        full_rank=9+nodes
        assert genus==9*c*e+1 and full_rank==9*c*e
        assert full_rank-1==9*c*e-1
        odd_norm.append([c,e,nodes,genus,full_rank,full_rank-1])
unions=[]
for c in range(2,65,2):
    for e in range(2,65):
        g1,g2=10,9*(c-1)*(e-1)+1
        f1,f2=g1-1,g2-1
        intersection=9*(c+e-2)
        genus=g1+g2+intersection-1
        full=f1+f2+intersection-1
        assert genus==9*c*e+1 and full==9*c*e-1
        assert full-1==9*c*e-2
        unions.append([c,e,intersection,genus,full,full-1])
cases=0;excluded=[]
for a in range(1,65):
    for b in range(1,65):
        for d in range(1,17):
            c,e=a*d,b*d
            covered=(c%2==1 or e>=2)
            assert covered==(d>=2 or a%2==1 or b>=2)
            if not covered:excluded.append([a,b,d]);continue
            r=9*a*b*d*d-1-int(c%2==0)
            assert r==9*c*e-(1 if c%2 else 2)
            cases+=1
assert excluded==[[a,1,1] for a in range(2,65,2)]
out={'status':'PASS','scope':'Exact arithmetic supplement to a geometric proof; no sample-based existence assertion',
     'odd_norm_cases':len(odd_norm),'transverse_union_cases':len(unions),
     'covered_degree_cases':cases,'excluded_small_cases':excluded,
     'norm_rows':odd_norm,'union_rows':unions,
     'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['norm_rows','union_rows']},indent=2))
