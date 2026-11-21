#!/usr/bin/env python3
"""Concrete matrix and known-specialization checks for T042's evaluator."""
from pathlib import Path
from itertools import combinations,product
from math import comb
from q_plus_symmetric_positive import coefficient,polytopes
from q_plus_positive import coefficient as one_power
from five_point_positive import LABELS
HERE=Path(__file__).resolve().parent
checks=0;points=0
for k in range(181):
    for d in (0,1):
        for mu in LABELS:
            assert coefficient(1,k,d,mu)==one_power(k,d,mu)
            checks+=1
for ra,rk in product((0,1,5,59),repeat=2):
    for qa,qk in product(range(3),repeat=2):
        a=ra+60*qa;k=rk+60*qk
        for mu in LABELS:
            total=0
            for poly in polytopes(a,k,0,mu):
                i,j=poly['orders'];c=poly['constant']
                assert len(poly['variables'])<=8
                xs=list(combinations(range(1,qa+1),i));ys=list(combinations(range(1,qk+1),j))
                total+=c*len(xs)*len(ys)
                for x,y in product(xs,ys):
                    for z in {0,c-1}:
                        point=(qa,qk,z)+x+y
                        assert all(sum(v*w for v,w in zip(row,point))==rhs for row,rhs in poly['equalities'])
                        assert all(sum(v*w for v,w in zip(row,point))<=rhs for row,rhs in poly['inequalities'])
                        points+=1
            assert total==coefficient(a,k,0,mu)
            checks+=1
receipt=f'PASS: {checks} exact evaluator comparisons, including2534 T040 specializations and1008 explicit polytope matrix counts;{points} literal boundary witnesses.\n'
(HERE/'Q_PLUS_SYMMETRIC_EVALUATOR_CHECK.txt').write_text(receipt)
print(receipt,end='')
