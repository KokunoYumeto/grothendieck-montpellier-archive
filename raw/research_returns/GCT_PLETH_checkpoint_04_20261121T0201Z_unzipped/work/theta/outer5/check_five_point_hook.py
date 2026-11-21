#!/usr/bin/env python3
"""Exact fixed rational and positive-tag identities for T041."""
from pathlib import Path
from fractions import Fraction
import sys,csv
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z
from five_point_positive import LABELS,TAGS,TENSOR
from five_point_hook_positive import FOUR,THREE,tags,coefficient
t=s.symbols('t')
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
D=s.prod(1-t**j for j in (2,3,4,5));D3=s.prod(1-t**j for j in (2,3,5))
for nu in LABELS:
    actual=0
    for cyc in classes:
        e=cyc.count(1)-1
        HS=(1-t)/s.prod(1-t**j for j in cyc)
        actual+=s.Rational(character(nu,cyc),z(cyc))*((e-1/t)*HS+1/t)
    positive=sum(t**i for i in FOUR[nu])/D+sum(t**i for i in THREE.get(nu,()))/D3
    assert s.cancel(actual-positive)==0,nu
rows=[]
for a in range(1,41):
    for d in (0,1):
        for mu in LABELS:
            value=coefficient(a,d,mu)
            assert len(tags(a,d,mu))<=90
            support=a>=2 if mu in ((5,),(1,1,1,1,1)) else True
            assert (value>0)==support
            rows.append(dict(a=a,d=d,outer=','.join(map(str,mu)),coefficient=value,status='PASS'))
with (HERE/'FIVE_POINT_HOOK_CHECK.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=tuple(rows[0]),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
(HERE/'FIVE_POINT_HOOK_CHECK.txt').write_text('PASS: seven exact rational identities;560 positive counts/support tests;90-tag bound.\n')
print('PASS:7 exact rational identities;560 positive count/support cases')
