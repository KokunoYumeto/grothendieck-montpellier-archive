#!/usr/bin/env python3
"""Different-method algebra checks for the isolated odd strict reconstruction.

Run: python workbench/programs/check_odd_strict_reconstruction.py
The geometric incidence and vanishing theorems are not certified by this code.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

p,L,N=s.symbols('p L N')
F=L-N;K=(p-1)*L+N;B=L+N
assert s.expand(K-(p-1)*F-p*N)==0
assert s.expand((K+F)*(-F)-(-p*L*F))==0
assert s.expand((-p*F)*(K+F)-p*((-F)*(K+F)))==0
count=3
cases=[]
for pp in (3,5,7,11,13,17,19,23,29,31):
    # Linear algebra on the p-dimensional truncated transverse algebra.
    # Its derivation matrix has one Jordan block; constants are its kernel.
    mat=s.zeros(pp)
    for j in range(1,pp):mat[j-1,j]=j
    assert all(int(x)%pp==0 for x in mat**pp)
    assert sum(1 for j in range(1,pp) if int(mat[j-1,j])%pp)==pp-1
    count+=2
    for dd in (2,4,6,12,30):
        rhs=1+(pp*pp-3*pp+1)*dd
        assert rhs%2==1
        euler=Fraction(-pp*dd,12)
        h2=Fraction(dd,pp)
        dimension=euler+h2/2
        assert dimension==Fraction(dd*(6-pp*pp),12*pp)
        assert dimension<0
        count+=3
    assert (pp-2)%2==1
    count+=1
    cases.append(dict(p=pp,transverse_rank=pp-1,radial_exterior_derivative=2%pp))
out={'status':'PASS','assertions':count,
     'methods':['formal Chern-root expansion','finite-field derivation matrices','exact rational RR and parity checks'],
     'prime_cases':cases,
     'scope':'Arithmetic and local-model checks only; complete geometric proof and source audit are separate'}
(Path(__file__).resolve().parents[1]/'records/ODD_STRICT_RECONSTRUCTION_ARITHMETIC.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
