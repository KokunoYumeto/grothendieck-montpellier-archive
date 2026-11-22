#!/usr/bin/env python3
"""Exhaustive tiny-family check for NN-C019's exposing-weight formula."""
import json
from pathlib import Path
cases=0
for n in range(1,5):
    for fam in range(1,1<<(1<<n)):
        witnesses=[x for x in range(1<<n) if fam>>x&1]
        s=min(witnesses)
        weights=[1 if s>>i&1 else n+1 for i in range(n)]
        values=[sum(weights[i] for i in range(n) if x>>i&1) for x in witnesses]
        m=min(values)
        assert values.count(m)==1 and witnesses[values.index(m)]==s
        assert m<=n and max(weights)<=2*n
        cases+=1
p=Path(__file__).with_name('FINITE_CHECK_ISOLATION_RESULTS.json')
p.write_text(json.dumps({'finding_id':'NN-C019','cases':cases,'method':'Exhaust all nonempty families on Boolean cubes of dimensions1--4; minimum integer order is a fixed lexicographic bit order','result':'pass','limitation':'Checks weight theorem only, not E counter'},indent=2)+'\n')
print({'cases':cases,'result':'pass'})
