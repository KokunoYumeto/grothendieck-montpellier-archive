#!/usr/bin/env python3
"""Independent finite-character check of root G017's proposed Q module."""
from pathlib import Path
from fractions import Fraction
import sys
import csv
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z
from five_point_positive import LABELS
t=s.symbols('t')
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
sixclasses=((1,1,1,1,1,1),(2,2,2),(2,2,1,1),(3,3),(6,),(4,1,1),(5,1))
base=s.prod(1-t**j for j in (2,4,6,10))
traces={}
for cyc,six in zip(classes,sixclasses):
    eps=(-1)**(5-len(cyc))
    chiE=cyc.count(1)-1
    chiU=character((3,2),cyc)
    series=(chiE+t-chiU*t**2)*(1-eps*t)/s.prod(1-eps**j*t**j for j in six)
    quotient=s.cancel(series*base)
    assert s.denom(quotient)==1,(cyc,quotient)
    traces[cyc]=s.Poly(quotient,t)
    assert traces[cyc].degree()<=19
    assert traces[cyc].eval(1)==(4320 if cyc==classes[0] else 0)

rows=[]
for lam in LABELS:
    multiplicities=[]
    for degree in range(20):
        val=sum(s.Rational(character(lam,cyc),z(cyc))*traces[cyc].nth(degree) for cyc in classes)
        assert val.is_Integer and val>=0,(lam,degree,val)
        multiplicities.append(int(val))
        rows.append(dict(partition=','.join(map(str,lam)),degree=degree,multiplicity=int(val),status='PASS'))
    assert sum(multiplicities)==36*character(lam,classes[0])
    print(lam,multiplicities,'total',sum(multiplicities))

with (HERE/'Q_MODULE_CHARACTER_CHECK.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=('partition','degree','multiplicity','status'),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
(HERE/'Q_MODULE_CHARACTER_CHECK.txt').write_text(
    'PASS: all seven exact rational characters become degree<=19 polynomials; all140 irreducible coefficients are nonnegative integers.\n'
    'The ungraded finite module is36 copies of the regular S5 representation;4320 total dimension and at most216 tags per outer label.\n')
