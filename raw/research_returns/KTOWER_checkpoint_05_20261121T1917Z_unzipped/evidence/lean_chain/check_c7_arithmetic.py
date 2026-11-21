#!/usr/bin/env python3
"""Exact small-integer checks for KT-C7-EXPLICIT; no huge b(D,n) is expanded."""
import json
from pathlib import Path

Ds = [3, 7, 11, 19, 43, 67]
rows = []
for D, n in [(3, 3)] + [(D, 2) for D in Ds]:
    I = D**n * (2*n)**(2*n)
    R = n**n * I**2
    assert I < 10**7
    assert 2*R + 1 < 10**14
    t_exp = 14*(2*n)
    a_exp = 7*(1+2*n*n)
    b_exp = t_exp*(2*n*n)
    h_exp = a_exp + 2*b_exp + n*t_exp
    if n == 3:
        assert (t_exp,a_exp,b_exp,h_exp) == (84,133,1512,3409)
        # log10 b < h_exp+a_exp+b_exp*10**h_exp < 10**3413
        assert h_exp+a_exp+b_exp*10**h_exp < 10**3413
    else:
        assert (t_exp,a_exp,b_exp,h_exp) == (56,63,448,1071)
        assert h_exp+a_exp+b_exp*10**h_exp < 10**1074
    rows.append(dict(D=D,n=n,I=I,R=R,t_exp=t_exp,a_exp=a_exp,b_exp=b_exp,h_exp=h_exp))

# Minkowski norm cutoffs using pi>3: (2/pi)*sqrt(D)<limit
class_rows=[]
for D, limit, primes in [(3,2,[]),(7,2,[]),(11,3,[2]),(19,3,[2]),(43,5,[2,3]),(67,6,[2,3,5])]:
    assert 4*D < 9*limit*limit  # (2/3)*sqrt(D)<limit
    checks=[]
    for p in primes:
        if p==2:
            assert (-D) % 8 == 5
        else:
            assert pow((-D)%p,(p-1)//2,p)==p-1
        checks.append(dict(prime=p,inert=True))
    class_rows.append(dict(D=D,minkowski_norm_strict_upper=limit,inert_checks=checks))

assert 6**18 < 10**15
assert 18**8 < 10**11
assert 20*(10**15+192*10**11)<10**18
assert 18+10**3413<10**3414
assert 3414<3500
out = dict(status='passed',constant='10^(10^3500)',source_formula_rows=rows,class_number_one_checks=class_rows,
           meaning='Checks arithmetic in a proof using cited source theorems; not a standalone K-theory certificate.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
