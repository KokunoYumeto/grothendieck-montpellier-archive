#!/usr/bin/env python3
"""Check projection of every raw colored mixed34 orbit preimage to its base image."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];s=A[B[A]];full=np.array([C[C],s[s]])
base=np.load(HERE/'hurwitz_colored_inverse_12_mixed.npz');rows=json.loads((HERE/'hurwitz_colored_inverse_12_mixed.json').read_text())['cases']
byid={r['mixed_orbit']:r for r in rows};first=[52,58,32,34,33,50];ordering=first+[r['mixed_orbit']for r in rows if r['mixed_orbit']not in first]
outputs=[];saved={};states={}
for k in ordering:
 sub=base[f'orbit_{k}'];rr=np.array([6*int(i)+j for i in sub for j in range(6)]);loc=np.full(len(A),-1,dtype=int);loc[rr]=np.arange(len(rr));gs=loc[full[:,rr]];assert min(gs.flat)>=0
 G=PermutationGroup([Permutation(g.tolist())for g in gs]);order=int(G.order());bo=byid[k]['order'];assert order%bo==0
 out={'component':k,'base_degree':len(sub),'raw_preimage_degree':len(rr),'base_order':bo,'raw_order':order,'kernel_order':order//bo,'raw_orbit_degrees':sorted(map(len,G.orbits()))}
 outputs.append(out);saved[f'raw_subset_{k}']=rr;saved[f'raw_generators_{k}']=gs;states[k]=(G.args,G.__dict__)
 print(out,flush=True)
 (HERE/'hurwitz_colored_raw_mixed_projection.json').write_text(json.dumps({'cases':outputs,'status':'IN_PROGRESS','elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
np.savez_compressed(HERE/'hurwitz_colored_raw_mixed_projection.npz',**saved)
(HERE/'hurwitz_colored_raw_mixed_projection_state.pkl').write_bytes(pickle.dumps(states))
(HERE/'hurwitz_colored_raw_mixed_projection.json').write_text(json.dumps({'cases':outputs,'all_marked_projections_isomorphisms':all(r['kernel_order']==1 for r in outputs),'status':'PASS','elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
