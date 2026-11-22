#!/usr/bin/env python3
"""Exact finite polynomial checks for the constant-integer nodal example.

The finite certificate does not claim to compute an infinite étale topos.
The cohomological and completion arguments are proved in the accompanying TeX.
"""
from pathlib import Path
import json
import time
import sympy as s

start = time.perf_counter()
x, y, t = s.symbols('x y t')
f = y**2-x**2*(x+1)
checks = {}
checks['normalization_equation'] = s.expand(f.subs({x:t*t-1,y:t*(t*t-1)})) == 0
checks['integral_generator_equation'] = s.expand((t*t-x-1).subs(x,t*t-1)) == 0
checks['rational_inverse'] = s.cancel((y/x).subs({x:t*t-1,y:t*(t*t-1)})) == t
singular = s.solve([f,s.diff(f,x),s.diff(f,y)],[x,y],dict=True)
checks['unique_singular_point'] = singular == [{x:0,y:0}]
checks['node_preimages'] = s.solve([t*t-1,t*(t*t-1)],[t]) == [(-1,), (1,)]
checks['distinct_tangent_factors'] = s.expand((y-x)*(y+x)-(y*y-x*x)) == 0
checks['odd_simple_factor_at_minus_one'] = s.diff(x+1,x).subs(x,-1) == 1
assert all(checks.values()), checks
out = {
    'scope':'Seven exact polynomial identities for the specified nodal cubic and its normalization; no cohomology computation is asserted.',
    'checks':checks,
    'count':len(checks),
    'passed':sum(checks.values()),
    'singular_points':[{str(k):str(v) for k,v in p.items()} for p in singular],
    'normalization':{'x':'t^2-1','y':'t(t^2-1)'},
    'seconds':time.perf_counter()-start,
}
root = Path(__file__).resolve().parents[1]
(root/'logs/ROOT_nodal_constant_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
