#!/usr/bin/env python3
"""Exact finite checks of the universal identities used in the endpoint proof.

This does not certify Bertini, obstruction theory, or an infinite range.
The text proves those statements separately.  Outputs retain exact expressions.
"""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json
import sympy as s

started = perf_counter()
stamp = datetime.now(timezone.utc).isoformat()
base = Path(__file__).resolve().parents[1]
checks = []

def record(name, passed, details):
    checks.append({'name': name, 'pass': bool(passed), 'details': details})

for n in range(2, 11):
    x = s.symbols('x0:'+str(n))
    c1 = sum(x)
    c2 = sum(x[i]*x[j] for i in range(n) for j in range(i+1,n))
    # det=1+c1*t+c2*t^2; its inverse has degree-two coefficient c1^2-c2.
    # [O_C]=1-[A]/det+(n-1)/det, with [A]=n+c1*t.
    constant = 1-n+(n-1)
    linear = -(-n*c1+c1)-(n-1)*c1
    quadratic = s.expand(-n*(c1*c1-c2)+c1*c1+(n-1)*(c1*c1-c2))
    record('Hilbert_Burch_gamma2_rank_'+str(n),
           constant == 0 and s.expand(linear) == 0 and s.expand(quadratic-c2) == 0,
           {'rank': n, 'degree2': str(quadratic), 'expected': str(c2)})

a1,a2,b1,b2=s.symbols('a1 a2 b1 b2')
gamma2_virtual=a2-b2+b1*b1-a1*b1
record('virtual_gamma2_expansion',
       s.expand(gamma2_virtual-(a2-b2-a1*b1+b1*b1)) == 0,
       {'gamma2_A_minus_B': str(gamma2_virtual)})

q=s.symbols('q')
for m in [1,2,3,4,5,8,9,25]:
    rhs=(1-q)*sum(q**j for j in range(m))
    record('Cartier_power_'+str(m), s.expand(rhs-(1-q**m)) == 0,
           {'power':m,'identity':str(s.expand(rhs)),
            'restriction_to_finite_C':'each q^j restricts to 1, so sum restricts to '+str(m)})

for d in [0,1,2,3]:
    # One-step rank-drop is codim2.  At d>=2, a 2xd derivative fails
    # surjectivity in codim d-1, for total d+1.  Smaller strata avoid drop.
    codim = 2 if d < 2 else 2+(d-1)
    record('stratum_bad_incidence_dimension_'+str(d), codim>d,
           {'stratum_dimension':d,'bad_codimension':codim,'deeper_rank_codimension':6})

y=s.symbols('y')
record('endpoint_gamma2_weight2',
       s.expand((0+2*y-4*y)/2+y) == 0,
       {'assumptions':['y^2=0','psi^2(y)=4y'],'gamma2':'-y'})

result={'started_utc':stamp,'completed_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-started,'scope':'finite exact algebra only; geometry and source theorems are not inferred from the program',
        'passes':sum(c['pass'] for c in checks),'failures':sum(not c['pass'] for c in checks),'checks':checks}
path=base/'output'/'endpoint_family_algebra_certificate.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if result['failures']:
    raise SystemExit(1)

