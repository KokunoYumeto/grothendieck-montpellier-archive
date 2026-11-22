#!/usr/bin/env python3
"""Exact finite endpoint certificate for the L4 arc-type counterexample."""
from fractions import Fraction as Q
from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
def boundary(p):return max(abs(t) for t in p)==1
def inside(p):return max(abs(t) for t in p)<1
x=(Q(0),Q(0));b=(Q(1),Q(0));a=(Q(-1),Q(0));other=(Q(0),Q(1))
assert inside(x) and boundary(b) and boundary(a) and boundary(other)
tether=[x,b];chord=[a,b]
assert sum(map(boundary,tether))==1
assert sum(map(boundary,chord))==2
assert tether[0]!=tether[1] and chord[0]!=chord[1]
# Every point (t,0), 0<=t<1, is interior; the assertion is symbolic
# in the paper. Here the endpoint invariant and finite CW data are exact.
out={'disk':'[-1,1]^2','interior_lieu':[0,0],
     'tether_endpoints':[[0,0],[1,0]],'proper_chord_endpoints':[[-1,0],[1,0]],
     'tether_boundary_endpoint_count':1,'proper_chord_boundary_endpoint_count':2,
     'distinct_completions':[[[-1,0],[1,0]],[[0,1],[0,0],[1,0]]],
     'all_checks_passed':True}
(root/'audit'/'l4_endpoint_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
