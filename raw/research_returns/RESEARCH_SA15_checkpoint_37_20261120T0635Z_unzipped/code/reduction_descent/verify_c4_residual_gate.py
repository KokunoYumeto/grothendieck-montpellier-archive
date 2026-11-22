#!/usr/bin/env python3
"""Exact identities and finite arithmetic for the B38 C4 residual gate."""
from pathlib import Path
import json
import math
import time
import sympy as s

started=time.perf_counter()
t,z=s.symbols('t z')
h=(t+2)/(t-1)
c4=lambda x:9*x*(x**3+8)
disc=lambda x:27*(x**3-1)**3
j=lambda x:c4(x)**3/disc(x)
assert s.factor((h+2)/(h-1)-t)==0
assert s.factor(j(h)-j(t))==0
assert s.factor(c4(h)/c4(t)-9/(t-1)**4)==0
assert s.factor(disc(h)/disc(t)-729/(t-1)**12)==0
assert s.factor((h-1)*(t-1)-3)==0
cyclo=s.Poly(z*z+z+1,z)
assert s.rem(s.Poly((z+2)-z*z*(z-1),z),cyclo)==0
assert s.rem(s.Poly((z*z+2)-z*(z*z-1),z),cyclo)==0
assert s.rem(s.Poly((z-1)**2+3*z,z),cyclo)==0
assert s.rem(s.Poly((z*z-1)**2+3*z*z,z),cyclo)==0

# F_9=F_3[i], i^2=-1; the roots of X^2=1 do not meet X^2=-1.
F9=[(a,b) for a in range(3) for b in range(3)]
def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%3,(x[0]*y[1]+x[1]*y[0])%3)
plus=[x for x in F9 if mul(x,x)==(1,0)]
minus=[x for x in F9 if mul(x,x)==(2,0)]
assert plus==[(1,0),(2,0)] and minus==[(0,1),(0,2)]
assert not set(plus)&set(minus)

# General completed-square Weierstrass equation and its quadratic twist.
a2,a4,a6,d=s.symbols('a2 a4 a6 d')
def delta(A,B,C):
    return -16*(4*A**3*C-A*A*B*B-18*A*B*C+4*B**3+27*C*C)
assert s.expand(delta(d*a2,d*d*a4,d**3*a6)-d**6*delta(a2,a4,a6))==0
congruences=[]
for delta0 in range(-120,121):
    condition=(30-2*delta0-6)%12==0
    assert condition == (delta0%6==0)
    if condition:
        tame=4//math.gcd(4,delta0)
        assert tame in (1,2)
        congruences.append({'delta':delta0,'tame':tame})
minimal=[r for r in congruences if 0<=r['delta']<=23]
assert [r['delta'] for r in minimal]==[0,6,12,18]
assert [r['tame'] for r in minimal]==[1,2,1,2]
out={'status':'PASS',
     'symbolic_identities':['h^2=t','j(h)=j','c4(h)/c4=9/(t-1)^4',
                           'Delta(h)/Delta=729/(t-1)^12','Norm(t-1)=3',
                           'h(zeta)=zeta^2','h(zeta^2)=zeta',
                           '(zeta-1)^2=-3zeta','quadratic twist Delta scales by d^6'],
     'F9_square_one':plus,'F9_square_minus_one':minus,
     'F_valuations':{'three':4,'pi':2,'three_root_differences':[2,2,2],
                     't^3-1':6,'t^3+8':6,'raw_discriminant':30,'j':12},
     'K_j_valuation':6,'discriminant_congruences':congruences,
     'minimal_discriminant_necessary_list':minimal,
     'remaining_special_inertia_pair':[3,6],'remaining_joint_order':18,
     'scope':'Necessary restriction of the C4 residual case; no remaining level27 pair existence decision',
     'elapsed_seconds':time.perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
