"""Exact search for integral ray transpositions on every survivor facet.

The source cell is simplicial. Finding an integral odd permutation for
each full-rank facet suffices to make its localized boundary zero.
This script makes no assertion that the cycle is not a boundary.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
from functools import reduce
import json
import sympy as sp

base=Path(__file__).parent
data=json.loads((base/'k12_survivor_certificate.json').read_text())
v=sp.Matrix(data['vectors']).T
b=sp.Matrix(data['normalized_relation_matrix'])
results=[]
for removed in range(12):
    keep=[j for j in range(12) if j!=removed]
    f=v[:,keep]
    piv=f.rref()[1]
    assert len(piv)==9
    inv=f[:,list(piv)].inv()
    null=b[:,removed].T.nullspace()
    c=sp.Matrix.hstack(*null).T
    bf=c*b[:,keep]
    found=None
    for i,j in combinations(range(11),2):
        for sign in (1,-1):
            if bf[:,i]!=sign*bf[:,j]:continue
            image=f.copy()
            image[:,i]=sign*f[:,j]
            image[:,j]=sign*f[:,i]
            g=image[:,list(piv)]*inv
            if g*f!=image:continue
            if any(x.q!=1 for x in g):continue
            assert abs(g.det())==1 and g*g==sp.eye(9)
            found={
                'facet_positions_swapped':[i,j],
                'original_vector_indices_zero_based':[keep[i],keep[j]],
                'both_vector_signs':sign,
                'integral_matrix':[[int(x) for x in row] for row in g.tolist()],
                'matrix_determinant':int(g.det()),
                'quadratic_ray_permutation_sign':-1,
            }
            break
        if found is not None:break
    results.append({
        'removed_vector_index_zero_based':removed,
        'remaining_vector_rank':len(piv),
        'generated_sublattice_index':reduce(gcd,(abs(int(x)) for x in b[:,removed])),
        'odd_integral_ray_transposition':found,
    })
out={'date':'2026-11-21','scope':'Explicit integral facet symmetries only; no nonboundary or K12 conclusion.','facets':results}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{'removed':r['removed_vector_index_zero_based'],'index':r['generated_sublattice_index'],'swap':None if r['odd_integral_ray_transposition'] is None else r['odd_integral_ray_transposition']['original_vector_indices_zero_based']} for r in results],indent=2))
