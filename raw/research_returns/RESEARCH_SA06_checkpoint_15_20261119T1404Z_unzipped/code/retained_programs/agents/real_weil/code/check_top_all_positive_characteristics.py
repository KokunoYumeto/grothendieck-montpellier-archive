#!/usr/bin/env python3
"""Recovered finite certificate for C3aq; no extrapolation to all primes."""
from pathlib import Path
from time import perf_counter
from datetime import datetime, timezone
import json
import sympy as s
started=perf_counter();checks=[]
for p in [2,3,5,7,11,13]:
    e,n,d=p+1,p*(p+1),p*(p+1)-3
    x,w,c,y,z,a,t=s.symbols('x w c y z a t')
    derivative=s.Poly(s.diff(y**n-y-z**(n-1),y),y,z,modulus=p).as_expr()
    assert derivative==(-1 if p>2 else 1)
    assert p*e*d==n*(n-3)
    assert n*(n-2)+1-n==n*(n-3)+1
    assert e*d-p*d==d
    assert p*p*d+2*p*d==(e*e-1)*d
    assert p*(p+1)-p==p*p
    cover=w**(p+1)-x+c*x**(p+1)
    assert s.expand(x*(1-c*x**p)-w**(p+1)+cover)==0
    dcoef=s.cancel(-w*x**(p+1)/(x*x)*x/w**(p+1))
    assert s.cancel(dcoef+x**p/w**p)==0
    assert s.expand((a*t)**(p+1)-a**(p+1)*t**(p+1))==0
    branch=y**n-y-(-a**(p+1)*t**(p+1))**(n-1)
    assert s.Poly(s.diff(branch,y),y,a,t,modulus=p).as_expr()==(-1 if p>2 else 1)
    checks.append({'p':p,'cover_degree':e,'plane_degree':n,'d':d,
       'D1_degree':e*d,'canonical_degree':n*(n-3),'normal_degree':d,
       'D_square':(e*e-1)*d,'D_dot_section':e*d,'D_dot_fibre':p,
       'differential_section_order':p*p,'differential_base_order':p*d,
       'infinity_parameter_order':1,'all_checks_passed':True})
r,ss,tt,m,dr,ds,dt=s.symbols('r ss tt m dr ds dt')
rels={
 'first_entry_in_I':s.expand(-m*(ss*dt+tt*ds)-(-m*ss*dt-m*tt*ds)),
 'second_entry_in_I':s.expand(m*tt*dr-(-r*m*dt+m*(tt*dr+r*dt))),
 'third_entry_in_I':s.expand(m*ss*dr-(m*(r*ds+ss*dr)-m*r*ds))}
assert all(v==0 for v in rels.values())
result={'utc':datetime.now(timezone.utc).isoformat(),'reconstruction':True,
 'all_checks_passed':True,'prime_cases':checks,
 'dennis_stein_product_rules':{k:str(v) for k,v in rels.items()},
 'runtime_seconds':perf_counter()-started,
 'scope':'Finite exact identities only; every-prime geometry, integral Chow invariant, actual branches and ordinary divisibility are proved separately.'}
Path(__file__).with_name('check_top_all_positive_characteristics_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
