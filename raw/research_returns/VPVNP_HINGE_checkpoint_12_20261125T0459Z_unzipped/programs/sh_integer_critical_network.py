#!/usr/bin/env python3
"""Exact cuts, Euclidean cost and convex stationarity for the SH34 graph."""
import json
import sys
from pathlib import Path
import sympy as sp

cfg = json.loads(Path(sys.argv[1]).read_text())
n = cfg['vertices']
edges = cfg['edges']
cuts = {}
for terminal_mask in range(1, 8):
    options = []
    for inner_mask in range(1 << (n-4)):
        mask = terminal_mask | (inner_mask << 4)
        value = sum(c for a,b,c in edges if ((mask >> a) ^ (mask >> b)) & 1)
        options.append((value, inner_mask))
    value, witness = min(options)
    cuts[str(terminal_mask)] = {'capacity':value, 'inner_mask':witness}
assert [cuts[str(s)]['capacity'] for s in (1,2,4,7)] == [6]*4
assert cuts['3']['capacity'] == 12
assert cuts['6']['capacity'] == 5
assert cuts['5']['capacity'] == 8
degrees = [sum(c for a,b,c in edges if v in (a,b)) for v in range(n)]
assert degrees == [6,6,6,6,3,3]
h = (1-1/sp.sqrt(3))/2
p = [sp.Matrix(z) for z in cfg['terminal_positions']] + [sp.Matrix([h,-h]),sp.Matrix([-h,h])]
cost = sp.simplify(sum(c*sp.sqrt((p[a]-p[b]).dot(p[a]-p[b])) for a,b,c in edges))
assert sp.simplify(cost-(8+7*sp.sqrt(2)+sp.sqrt(6))) == 0
forces = []
for v in (4,5):
    f = sp.zeros(2,1)
    for a,b,c in edges:
        if v in (a,b):
            z = p[v]-p[b if a==v else a]
            f += c*z/sp.sqrt(z.dot(z))
    f = f.applyfunc(sp.simplify)
    assert f == sp.zeros(2,1)
    forces.append([str(x) for x in f])
# Exact rational estimates: sqrt(2)>7/5 and sqrt(6)>12/5.
assert sp.Rational(7,5)**2 < 2 and sp.Rational(12,5)**2 < 6
assert 8+7*sp.Rational(7,5)+sp.Rational(12,5) > 20
# Enumerate the augmented source/sink cut conditions used in SH34b.
flow_cases = []
for mask in range(16):
    imbalance = ((mask&1)>0)+((mask&2)>0)-((mask&4)>0)-((mask&8)>0)
    needed = max(0,6*imbalance)
    if needed:
        assert mask in (1,2,3,7,11)
    flow_cases.append({'terminal_mask':mask,'required_original_cut':needed})
result = {'config':cfg,'terminal_cuts':cuts,'degrees':degrees,'cost_exact':str(cost),
          'cost_float':float(cost),'internal_gradients':forces,
          'fixed_topology_global_minimum':'convex sum of norms with zero gradient at the displayed points',
          'source_sink_cut_conditions':flow_cases,
          'scope':'An exact integer geometric network, not a tensor identity or a universal network lower bound.'}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2))
print(json.dumps({'cost':str(cost),'cuts':cuts,'gradients':forces,'PASS':True}))
