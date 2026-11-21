#!/usr/bin/env python3
"""Independent proved-boundary and literal-polytope checks for T043."""
from pathlib import Path
from itertools import combinations,product
from math import comb
import json
from hook_all_powers_positive import coefficient,polytopes,transpose
from five_point_hook_positive import coefficient as first_power
from five_point_positive import LABELS
HERE=Path(__file__).resolve().parent
WEDGE=json.loads((HERE.parent.parent/'root/FIVE_POINT_WEDGE2_NEWTON_TABLE.json').read_text())['labels']
checks=0;points=0
for a in range(1,121):
    for d in (0,1):
        for mu in LABELS:
            assert coefficient(a,1,d,mu)==first_power(a,d,mu);checks+=1
for k in range(181):
    for d in (0,1):
        for mu in LABELS:
            nu=transpose(mu) if (d+1)%2 else mu;q,r=divmod(k,60)
            expected=sum(c*comb(q,j) for j,c in enumerate(WEDGE[','.join(map(str,nu))][r]) if j<=q)
            assert coefficient(1,k,d,mu)==expected;checks+=1
for r,s in product((0,1,5,59),repeat=2):
    for q,p in product(range(3),repeat=2):
        a=1+r+60*q;k=s+60*p
        for mu in LABELS:
            total=0
            for poly in polytopes(a,k,0,mu):
                i,j=poly['orders'];c=poly['constant']
                xs=list(combinations(range(1,q+1),i));ys=list(combinations(range(1,p+1),j))
                total+=c*len(xs)*len(ys)
                for x,y in product(xs,ys):
                    for z in {0,c-1}:
                        point=(q,p,z)+x+y
                        assert all(sum(v*w for v,w in zip(row,point))==rhs for row,rhs in poly['equalities'])
                        assert all(sum(v*w for v,w in zip(row,point))<=rhs for row,rhs in poly['inequalities']);points+=1
            assert total==coefficient(a,k,0,mu);checks+=1
receipt=f'PASS:{checks} evaluator comparisons:1680 T041 boundaries,2534 G018 boundaries,1008 literal polytope counts;{points} matrix witnesses.\n'
(HERE/'HOOK_ALL_POWERS_EVALUATOR_CHECK.txt').write_text(receipt);print(receipt,end='')
