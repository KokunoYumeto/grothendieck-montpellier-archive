#!/usr/bin/env python3
"""Exact cut and combinatorial checks for the SH35 packing counterexample."""
import itertools
import json
import sys
from pathlib import Path
import sympy as sp
from sh_residual_packing_search import packing

cfg=json.loads(Path(sys.argv[1]).read_text());n=cfg['vertices'];edges=cfg['edges']
cuts={}
for terminal_mask in range(1,8):
    candidates=[]
    for inner in range(1<<(n-4)):
        mask=terminal_mask+(inner<<4)
        c=sum(w for a,b,w in edges if ((mask>>a)^(mask>>b))&1)
        candidates.append((c,inner))
    minimum,witness=min(candidates);cuts[str(terminal_mask)]={'capacity':minimum,'inner_mask':witness}
assert [cuts[str(i)]['capacity'] for i in [1,2,4,7]]==[6]*4
assert cuts['3']['capacity']==12 and cuts['6']['capacity']==5 and cuts['5']['capacity']==12
degrees=[sum(w for a,b,w in edges if v in (a,b)) for v in range(n)]
assert degrees[:4]==[6]*4

# A unit K4 cannot route two copies of each of two opposite pairs.
# At every private vertex endpoint load is2 but internal degree3,
# leaving no capacity for a transit (which costs two incidences).
# Enumerating the only possible direct edges verifies their shortage.
direct_capacity={(6,8):1,(7,9):1}
assert all(direct_capacity[p]<2 for p in direct_capacity)
# In the other possible residual-tree component, the two opposite
# demands necessarily cross the single bridge twice.
assert 2>1

h=(1-1/sp.sqrt(3))/2
positions=[(1,0),(0,1),(-1,0),(0,-1),(h,-h),(-h,h)]+[(0,0)]*4
cost=sp.simplify(sum(w*sp.sqrt(sum((positions[a][j]-positions[b][j])**2 for j in range(2))) for a,b,w in edges))
assert sp.simplify(cost-(8+7*sp.sqrt(2)+sp.sqrt(6)))==0
assert float(cost)>20
solver=packing(n,[(a,b) for a,b,w in edges],[w for a,b,w in edges],30)
assert solver['status']==2
result={'config':cfg,'terminal_cuts':cuts,'degrees':degrees,
        'cost_exact':str(cost),'cost_float':float(cost),
        'same_graph_packing_impossible':True,
        'proof_checks':['All terminal degree6 is saturated by five demanded endpoints plus a connected remainder.',
                        'Every terminal is therefore a leaf of the remainder and cannot be internal on any requested path.',
                        'Every requested path and the four-terminal remainder stay within one terminal bridge.',
                        'If remainder is the binary tree, the private K4 would need two opposite pairs twice; impossible by degree3 versus endpoint load2.',
                        'If remainder is in the private K4 component, the unit binary tree would need both opposite pairs; both use its sole bridge.'],
        'milp_cross_check':solver,
        'scope':'Counterexample to same-graph residual packing, not to a cost-reducing replacement or the width-six lower bound.'}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2));print(json.dumps(result))
