#!/usr/bin/env python3
"""Exact arithmetic for the dyadic logarithm gate; no curve pairs enumerated."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
started=perf_counter()
S=sp.Matrix([[0,-1],[1,-1]])
tau=sp.diag(sp.eye(2),S)
projector=(sp.eye(4)+tau+tau**2)/3
assert tau**3==sp.eye(4)
assert projector==sp.diag(1,1,0,0)
assert projector**2==projector
def step(a,q):return min(a+q,1+2*q,4*q)
def sequence(a,n):
    seq=[1]
    for unused in range(n):seq.append(step(a,seq[-1]))
    return seq
rows=[]
for r in range(7):
    a=3*2**r;qs=sequence(a,8)
    crossing=next(u for u,q in enumerate(qs) if q>a)
    assert crossing==(2 if r==0 else r+1)
    rows.append({'r':r,'a':a,'q_sequence':qs,'first_crossing':crossing})
tables=[]
for n in range(4,9):
    left=[r['a'] for r in rows if r['first_crossing']>=n]
    expected=[3*2**r for r in range(n-1,7)]
    assert left==expected
    tables.append({'torsion_level':2**n,'manuscript_index':n-1,'remaining_joint_degrees':left})
log_cases=0
for a in range(1,193):
    qs=sequence(a,9)
    q=next(q for q in qs if q>a)
    for m in range(1,1001):
        l=m.bit_length()-1
        assert l<=m-1
        assert m*q-a*l>=q
        log_cases+=1
coefficient_cases=0
for a in range(1,193):
    for q in range(1,129):
        bound=step(a,q)
        assert bound==min(a+q,1+2*q)
        assert a+q>=bound and 1+2*q>=bound and 1+3*q>=bound and 4*q>=bound
        coefficient_cases+=1
out={'status':'PASS','scope':'Cubic projector and exact logarithm/recurrence arithmetic only; the Cartier-module proof is separate and no sixteen-congruence is evaluated',
     'projector':projector.tolist(),'joint_order_sequences':rows,'necessary_condition_table':tables,
     'logarithm_degree_cases':log_cases,'coefficient_valuation_cases':coefficient_cases,
     'retained_correction':'The first draft incorrectly wrote first crossing r+1 also at r=0. Its a=3 sequence1,3,6 is now treated separately; every level16-or-higher table entry was unchanged.',
     'elapsed_seconds':perf_counter()-started}
Path(__file__).with_name('B45_independent_check_output.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
