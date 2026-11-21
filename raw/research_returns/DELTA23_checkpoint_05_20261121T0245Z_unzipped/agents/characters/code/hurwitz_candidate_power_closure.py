#!/usr/bin/env python3
"""Actual-source power normalization of the eighteen finite mixed candidates."""
from pathlib import Path
import json,math,numpy as np
from sympy.combinatorics import Permutation
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'

def run():
    raw=np.load(PENT/'hurwitz_raw_pentagon45.npz')
    mixed=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz')
    vs=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1'];items=[]
    for k,(i,j)in enumerate(raw['labels']):
        if np.array_equal(raw['pentagon_defects'][k],np.arange(8064)):
            items.append((int(i),int(j),vs[i],mixed[f'R_{i}'][j]))
    assert len(items)==18
    def key(v,a):return v.astype(np.int16).tobytes()+a.astype(np.int16).tobytes()
    lookup={key(v,a):(i,j)for i,j,v,a in items};rows=[];cubes=[];saved=[]
    for i,j,v,a in items:
        u=np.argsort(a)[v];ov=int(Permutation(v.tolist()).order());ou=int(Permutation(u.tolist()).order())
        order=math.lcm(ov,ou);assert order in[2,6]
        vp=np.arange(1344);up=np.arange(1344);odd=[]
        for k in range(1,order+1):
            vp=vp[v];up=up[u]
            if k%2:
                target=lookup.get(key(vp,vp[np.argsort(up)]));assert target is not None
                odd.append({'power':k,'target':target})
        v3=v[v[v]];u3=u[u[u]];a3=v3[np.argsort(u3)]
        cube=lookup[key(v3,a3)];cubes.append(cube);saved.append((i,j,*cube))
        rows.append({'base_index':i,'fiber_index':j,'V_order':ov,'U_order':ou,'pair_order':order,
                     'all_odd_powers_retained':True,'odd_powers':odd,'cube':cube})
    assert sorted(set(cubes))==[(1,0),(19,0),(23,1),(27,2)]
    out={'statement':'D23.C30','cases':rows,'cube_targets':sorted(set(cubes)),'passes':18,'result':'PASS',
        'scope':'Existential actual-source normalization by h cubed, not rejection of individual original candidates.'}
    (HERE/'records/hurwitz_candidate_power_closure.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_candidate_power_closure.npz',cube_map=np.array(saved))
    print(json.dumps({'statement':'D23.C30','cube_targets':out['cube_targets'],'passes':18,'result':'PASS'},indent=2))

if __name__=='__main__':run()
