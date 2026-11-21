#!/usr/bin/env python3
"""Fixed-table and explicit-polytope checks for T038/T039."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import sys
import csv
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z,partitions
from five_point_positive import LABELS,TAGS,TENSOR,polytope_tags,coefficient,witnesses

def tableaux(lam):
    m=sum(lam);r=len(lam);answer=[]
    def visit(shape,rows):
        if len(rows)==m:
            answer.append(sum(m-i for i in range(1,m) if rows[i]>rows[i-1]))
            return
        for i in range(r):
            if shape[i]<lam[i] and (i==0 or shape[i]<shape[i-1]):
                new=list(shape);new[i]+=1;visit(tuple(new),rows+(i,))
    visit((0,)*r,())
    return tuple(sorted(answer))

classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
q=s.symbols('q')
checks=[]
for rho in LABELS:
    assert tableaux(rho)==TAGS[rho],(rho,tableaux(rho),TAGS[rho])
    for nu in LABELS:
        actual=sum(Fraction(character((3,2),cyc)*character(rho,cyc)*character(nu,cyc),z(cyc)) for cyc in classes)
        assert actual==TENSOR[rho].count(nu),(rho,nu,actual)
    expected=sum(q**j for j in TAGS[rho])/s.prod(1-q**j for j in range(2,6))
    actual=sum(s.Rational(character(rho,cyc),z(cyc))*(1-q)/s.prod(1-q**j for j in cyc) for cyc in classes)
    assert s.cancel(actual-expected)==0,rho
    checks.append(dict(check='tableau/tensor/rational identity',index=str(rho),status='PASS'))

for cyc in classes:
    chiE=cyc.count(1)-1
    sign=(-1)**(5-len(cyc))
    perm=cyc.count(1)
    traceS=1
    for j in cyc:traceS/=1-q**j
    traceS*=1-q
    traceA=1+chiE*q+perm*q**2/(1-q)
    numerator=s.cancel(traceA/traceS)
    expected=1-character((3,2),cyc)*q**2+character((2,2,1),cyc)*q**3-sign*q**5
    assert s.expand(numerator-expected)==0,(cyc,numerator,expected)
    checks.append(dict(check='equivariant resolution numerator',index=str(cyc),status='PASS'))

total_witnesses=0
for a in range(31):
    for d in (0,1):
        for mu in LABELS:
            values=list(witnesses(a,d,mu))
            assert len(values)==coefficient(a,d,mu)
            for tag,point in values:
                assert min(point)>=0 and sum(v*w for v,w in zip(point,(2,3,4,5)))==tag['R']
            total_witnesses+=len(values)
            assert len(polytope_tags(a,d,mu))<=36
            checks.append(dict(check='tagged lattice enumeration',index=f'{a},{d},{mu}',status='PASS'))
    for d in (0,1):
        expected_support=(a>=1) if (a+d)%2==0 else (a>=4)
        assert (coefficient(a,d,(5,))>0)==expected_support

with (HERE/'FIVE_POINT_POSITIVE_CHECK.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=('check','index','status'),delimiter='\t')
    writer.writeheader();writer.writerows(checks)
receipt=f'PASS: 7 fake-degree identities,49 tensor entries,7 equivariant resolution numerators,434 tagged counts; {total_witnesses} explicit lattice witnesses.\n'
(HERE/'FIVE_POINT_POSITIVE_CHECK.txt').write_text(receipt)
print(receipt,end='')
