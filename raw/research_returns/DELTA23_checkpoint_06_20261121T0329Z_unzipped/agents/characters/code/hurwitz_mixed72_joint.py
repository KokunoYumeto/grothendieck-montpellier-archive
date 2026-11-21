#!/usr/bin/env python3
"""Exact common-word matching of the two retained degree72 components."""
from pathlib import Path
import json,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1]
d=np.load(HERE/'records/hurwitz_mixed72_partial.npz')
for c in[9,10]:
    rr=d[f'component_{c}_R']
    G=PermutationGroup([Permutation(r.tolist())for r in rr])
    assert G.order()==16
    assert all(Permutation(r.tolist()).order()in[1,2]for r in rr)
g9,g10=[d[f'component_{c}_pair']for c in[9,10]]
G=PermutationGroup([Permutation(g.tolist()+[72+int(i)for i in v])for g,v in zip(g9,g10)])
D=G.derived_subgroup()
assert G.order()==995328 and D.order()==82944
pairs=[]
for i,r in enumerate(d['component_9_R']):
    for j,s in enumerate(d['component_10_R']):
        if D.contains(Permutation(r.tolist()+[72+int(v)for v in s])):pairs.append([i,j])
assert len(pairs)==16 and len({i for i,j in pairs})==len({j for i,j in pairs})==16
def vid(c,k):
    v=d[f'component_{c}_V'][k]
    return next(i for i,t in enumerate(d[f'component_{c}_unique_V'])if np.array_equal(v,t))
vpairs=sorted({(vid(9,i),vid(10,j))for i,j in pairs})
assert vpairs==[(0,0),(1,3),(2,1),(3,2)]
out={'statement':'D23.C25','joint_order':int(G.order()),'joint_derived_order':int(D.order()),
     'candidate_groups':'C2^4 in both components','candidate_pairs':pairs,
     'V_index_pairs':vpairs,'result':'PASS',
     'scope':'Exact same-word compatibility of two finite component values, not an actual profinite lifting statement.'}
(HERE/'records/hurwitz_mixed72_joint_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
