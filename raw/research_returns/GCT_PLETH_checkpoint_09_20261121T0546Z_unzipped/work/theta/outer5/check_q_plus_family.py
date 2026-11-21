#!/usr/bin/env python3
"""Exact fixed residue certificate for T040, Q twisted by 2k+1."""
from pathlib import Path
from fractions import Fraction
import sys,csv,json
from math import comb
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z
from five_point_positive import LABELS
t=s.symbols('t')
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
sixclasses=((1,1,1,1,1,1),(2,2,2),(2,2,1,1),(3,3),(6,),(4,1,1),(5,1))
maxdeg=359
class_series={}
common_numerators={}
for cyc,six in zip(classes,sixclasses):
    eps=(-1)**(5-len(cyc))
    e=cyc.count(1)-1;u=character((3,2),cyc)
    numerator=e*e-1-eps*e*u*t+eps*e*t**2+eps*t**3
    series=numerator*(1-eps*t)/s.prod(1-eps**j*t**j for j in six)
    common=s.cancel(series*(1-t**60)**4)
    assert s.denom(common)==1
    common=s.Poly(common,t)
    assert common.degree()<=238
    common_numerators[cyc]=common
    coefficients=[0]*(maxdeg+1)
    coefficients[0]=1
    for j in six:
        sign=eps**j
        for d in range(j,maxdeg+1):coefficients[d]+=sign*coefficients[d-j]
    pn=s.Poly(s.expand(numerator*(1-eps*t)),t)
    coefficients=[sum(int(pn.nth(j))*coefficients[d-j]
                      for j in range(min(d,pn.degree())+1)) for d in range(maxdeg+1)]
    class_series[cyc]=coefficients

tables={};rows=[]
for lam in LABELS:
    values=[]
    for k in range(maxdeg+1):
        value=sum(Fraction(character(lam,cyc)*class_series[cyc][k],z(cyc)) for cyc in classes)
        assert value.denominator==1 and value>=0,(lam,k,value)
        values.append(int(value))
    newton=[]
    for r in range(60):
        diff=[values[r+60*q] for q in range(4)]
        coefficients=[]
        while diff:
            coefficients.append(diff[0]);diff=[b-a for a,b in zip(diff,diff[1:])]
        assert all(c>=0 for c in coefficients),(lam,r,coefficients)
        assert coefficients[3]>0
        dim=character(lam,classes[0]);chi2=character(lam,classes[1]);chi22=character(lam,classes[2])
        closed1=Fraction(dim*(9*r*r+590*r+12352)+chi2*(10*r+350)-chi22*(30 if r%2==0 else 15),4)
        closed2=dim*(270*r+16950)+150*chi2
        assert coefficients[1:]==[closed1,closed2,16200*dim]
        for q in range(6):
            assert values[r+60*q]==sum(c*comb(q,j) for j,c in enumerate(coefficients) if j<=q)
        newton.append(coefficients)
        rows.append(dict(partition=','.join(map(str,lam)),residue=r,
                         delta0=coefficients[0],delta1=coefficients[1],
                         delta2=coefficients[2],delta3=coefficients[3],status='PASS'))
    tables[','.join(map(str,lam))]=newton
    print(lam,'minima',[min(row[j] for row in newton) for j in range(4)],
          'maxima',[max(row[j] for row in newton) for j in range(4)],
          'initial',values[:10])

A,B,C,D,E=s.symbols('A B C D E')
T=s.Matrix([A,B,C,D,E])
BM=s.Matrix([[0,0,D-E,E-C,C-D],[E-B,A-E,0,0,B-A],[0,D,0,-B,0],[-C,0,A,0,0]])
assert (BM*T).applyfunc(s.expand)==s.zeros(4,1)
minors=[s.factor((-1)**i*BM[:,[j for j in range(5) if j!=i]].det()) for i in range(5)]
F=A*D*(E-B-C)-B*C*(E-A-D)
assert all(s.expand(m+F*v)==0 for m,v in zip(minors,T))

(HERE/'Q_PLUS_NEWTON_TABLE.json').write_text(json.dumps({'period':60,'max_polynomial_degree':3,'labels':tables},indent=2)+'\n')
with (HERE/'Q_PLUS_NEWTON_CHECK.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=tuple(rows[0]),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
(HERE/'Q_PLUS_NEWTON_CHECK.txt').write_text(
    'PASS: exact B(T)T=0 and all5 signed maximal minors=-F*T_i; primitive kernel.\n'
    'PASS: all7 exact class series have denominator dividing(1-t^60)^4 and numerator degree<=238.\n'
    'PASS: all1680 residue Newton coefficients are nonnegative integers; all420 cubic coefficients strictly positive.\n'
    'PASS: all2520 coefficients through k359 agree with the Newton polynomials; values are integral and nonnegative.\n'
    'PASS: every positive-order Newton coefficient agrees with the closed dimension/transposition/double-transposition formula.\n')
