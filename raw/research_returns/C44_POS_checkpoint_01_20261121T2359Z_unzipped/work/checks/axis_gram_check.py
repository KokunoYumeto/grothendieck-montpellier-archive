"""Exact checks of the finite polynomial identities in C44-A04.

This checks formulas, not geometric existence or the general sign conjecture.
"""
from fractions import Fraction
from math import factorial
import json

out=[]
for r in range(1,13):
    coeff=[(-1)**j*(j+1) for j in range(r+1)]
    product=[sum(c*([1,2,1][i-j] if 0<=i-j<=2 else 0)
                 for j,c in enumerate(coeff)) for i in range(r+1)]
    assert product==[1]+[0]*r
    for d in (1,2,3):
        ds=factorial(r)*d**r
        dt=factorial(r+2)*d**(r+2)
        for number in sorted(set((1,2,dt-1,dt))):
            if number>dt: continue
            eig_special=Fraction((r+1)*ds*(dt-number),dt)
            assert eig_special>=0
        norm=Fraction((r+1)*ds*(dt-1),dt)
        out.append(dict(r=r,d=d,dS=ds,dT=dt,one_fibre_norm=str(norm),
                        denominator_cleared_norm=int(norm*dt**2),identity=True))
print(json.dumps({'scope':'r=1..12; d=1,2,3; symbolic coefficient identity and exact eigenvalues',
                  'passed':True,'cases':out},indent=2))
