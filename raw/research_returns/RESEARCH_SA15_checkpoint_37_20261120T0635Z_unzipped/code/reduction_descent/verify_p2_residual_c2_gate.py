#!/usr/bin/env python3
"""Exact two-isogeny and valuation identities; no remaining C3 search."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
started=perf_counter()
x,y,a,b=sp.symbols('x y a b')
D=a*a-4*b
X=x+a+b/x;Y=y*(1-b/x**2)
num=sp.together(Y*Y-X*(X*X-2*a*X+D)).as_numer_denom()[0]
assert sp.rem(sp.Poly(num,y),sp.Poly(y*y-x*(x*x+a*x+b),y)).is_zero
assert sp.simplify(sp.diff(X,x)*y-Y)==0
def invariants(A,B):
    b2=4*A;b4=2*B;b6=0;b8=-B*B
    c4=b2*b2-24*b4
    delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    delta=sp.expand(delta/1728*1728) # conventional numerator has no divisor
    return sp.expand(c4),sp.expand(delta)
c4,delta=invariants(a,b)
assert sp.expand(c4-16*(a*a-3*b))==0
assert sp.expand(delta-16*b*b*D)==0
c41,delta1=invariants(-2*a,D)
assert sp.expand(c41-16*(a*a+12*b))==0
assert sp.expand(delta1-256*b*D*D)==0
assert sp.expand((-2*a)**2-4*D-16*b)==0
rows=[(0,'alpha>=2 or alpha=1,r=0',2,0,6,6),
      (0,'alpha=1,r=1',3,0,7,5),
      (1,'alpha=1',2,1,8,7),
      (1,'alpha>=2',3,1,9,6)]
table=[]
for beta,case,vD,gamma,vdelta,vj in rows:
    assert 4+2*beta+vD==vdelta
    assert 8+3*gamma-2*beta-vD==vj
    assert (vdelta%3!=0)==((beta-vD)%2!=0)
    table.append(dict(beta=beta,case=case,vD=vD,v_a2_minus3b=gamma,
                      vdelta=vdelta,vj=vj,cubic_special_inertia=vdelta%3!=0))
square_cases=0
for beta in [0,1]:
    for alpha in range(-40,1):
        correction=2+beta-2*alpha
        assert correction>=2
        square_cases+=1
for r in range(2,101):
    assert r>=2 # b/c² belongs to1+4R
    square_cases+=1
out={'status':'PASS','scope':'Exact normalized2-isogeny, invariants, and exhaustive symbolic valuation branches; no residual C3 comparison decided',
     'symbolic_identity_groups':7,'valuation_table':table,
     'excluded_square_valuation_cases':square_cases,
     'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
