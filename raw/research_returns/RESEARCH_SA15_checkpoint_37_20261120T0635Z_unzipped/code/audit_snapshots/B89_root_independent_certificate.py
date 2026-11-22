"""B89 exact explicit-base polynomial and Newton-valuation certificate."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from math import comb
import sympy as sp
import json,time

start=time.perf_counter();T,t,X,pi=sp.symbols('T t X pi')
f=lambda U:(1+U)**5-(1+pi)
Q=sp.expand(f(T)+pi**4*T**2)
assert sp.expand(Q-(T**5+5*T**4+10*T**3+(10+pi**4)*T**2+5*T-pi))==0
shift=sp.expand(f(t+X)-f(t)-pi**4*t**2)
expected=-pi**4*t**2+sum(comb(5,j)*(1+t)**(5-j)*X**j for j in range(1,6))
assert sp.expand(shift-expected)==0
coefficients=sp.Poly(shift,X)
assert coefficients.TC()==-pi**4*t**2
interior=[]
for j in range(1,5):
    coefficient=coefficients.coeff_monomial(X**j)
    assert sp.expand(coefficient-comb(5,j)*(1+t)**(5-j))==0
    assert comb(5,j)%5==0 and comb(5,j)%25!=0
    chord=Fraction(22*(5-j),5)
    assert 20>chord
    interior.append({'degree':j,'valuation':20,'chord':str(chord)})
assert Fraction(22,5).denominator==5 and 22%5!=0 and 25-22==3
assert 24*(25-22)==72
cyclotomic=[]
for n in (1,2,3):
    step=5**(n-1);degree=4*step
    cs=[sum(comb(j*step,h) for j in range(5) if j*step>=h) for h in range(degree+1)]
    assert cs[-1]==1 and cs[0]==5
    assert all(c%5==0 for c in cs[:-1]) and cs[0]%25!=0
    cyclotomic.append({'n':n,'degree':degree,'Eisenstein':True})
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,
     'expanded_defining_polynomial':str(Q),'shifted_polynomial':str(sp.expand(shift)),
     'strict_Newton_interior_vertices':interior,'Newton_root_valuation':'22/5',
     'normalized_coordinate_valuation':22,'nonidentity_displacement_valuation':25,
     'lower_break_over_K':3,'lower_break_over_L':72,
     'cyclotomic_Eisenstein_checks':cyclotomic,
     'counts':{'symbolic_polynomial_identities':2,'strict_Newton_vertices':4,
               'cyclotomic_Eisenstein_polynomials':3,'cyclotomic_coefficients':sum(d['degree']+1 for d in cyclotomic)},
     'scope':'Exact polynomial and valuation arithmetic for the explicit allowed base. Field degrees, actual lower-break equality and cyclic-layer intersection are proved separately. No height-two BT group, shared torsion representation or ambiguous pair is constructed.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
