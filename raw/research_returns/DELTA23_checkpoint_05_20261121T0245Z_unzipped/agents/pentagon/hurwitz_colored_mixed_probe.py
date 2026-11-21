#!/usr/bin/env python3
"""Exact mixed-pair orbit groups in a colored Hurwitz action."""
from pathlib import Path
import json,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
kind=sys.argv[1]if len(sys.argv)>1 else'inverse'
no=int(sys.argv[2])if len(sys.argv)>2 else 12
data=np.load(HERE/f'hurwitz_colored_{kind}_orbit_{no}.npz')
A,B,C=data['generators'];ss=A[B[A]];x=C[C];y=ss[ss];N=len(x)
seen=set();orbits=[]
for v in range(N):
    if v in seen:continue
    q=[v];seen.add(v)
    for u in q:
        for p in[x,y]:
            w=int(p[u])
            if w not in seen:seen.add(w);q.append(w)
    orbits.append(q)
orbits.sort(key=len);print('mixed orbit degrees',list(map(len,orbits)),flush=True)
target=[np.array([1,2,0,3]),np.array([1,2,3,0])]
rows=[];saved={};start=time.monotonic()
for j,orb in enumerate(orbits):
    idx=np.full(N,-1,dtype=int);idx[orb]=np.arange(len(orb));gs=[idx[p[orb]]for p in[x,y]]
    G=PermutationGroup([Permutation(g.tolist())for g in gs]);order=int(G.order())
    J=PermutationGroup([Permutation(np.r_[g,len(orb)+q].tolist())for g,q in zip(gs,target)])
    joined=int(J.order());yes=joined==order
    derived=G.derived_subgroup();dorder=int(derived.order())
    row={'mixed_orbit':j,'degree':len(orb),'color':int(data['colors'][orb[0]]),
         'order':order,'derived_order':dorder,'markedS4_joined_order':joined,'retains_markedS4':yes}
    rows.append(row);saved[f'orbit_{j}']=np.array(orb);saved[f'pair_{j}']=np.array(gs)
    print(row,flush=True)
    (HERE/f'hurwitz_colored_{kind}_{no}_mixed.json').write_text(json.dumps({
        'orbit_degrees':list(map(len,orbits)),'cases':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
np.savez_compressed(HERE/f'hurwitz_colored_{kind}_{no}_mixed.npz',**saved)
