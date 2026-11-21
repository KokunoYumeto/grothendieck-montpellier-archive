#!/usr/bin/env python3
"""One common commutator word for the eight last-coordinate kernels and a3."""
from pathlib import Path
import itertools,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters';PENT=HERE.parent/'pentagon'
def grp(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def run():
    start=time.monotonic()
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    data=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    fibers=np.load(CHAR/'records/affine216_last_meridian_fibers.npz')
    els=data['elements'];ix={tuple(map(int,g)):i for i,g in enumerate(els)}
    aff=[]
    for v0,v1,a,b,c,d in els:
        aff.append(np.array([3*((a*(z//3)+b*(z%3)+v0)%3)+(c*(z//3)+d*(z%3)+v1)%3 for z in range(9)]))
    aff=np.array(aff)
    kids=meta['last_pair_kernel_ids'];pairs=[meta['kernels'][k]['pair']for k in kids]
    pairs.append(meta['cubic_detector_pair']);pairs=np.array(pairs)
    joint=lambda values:np.concatenate([9*j+aff[v]for j,v in enumerate(values)])
    G=grp([joint(pairs[:,0]),joint(pairs[:,1])]);go=int(G.order())
    print('jointorder',go,flush=True)
    D=G.derived_subgroup();do=int(D.order());print('derivedorder',do,flush=True)
    known=ix[(1,1,1,0,0,1)]
    rows=[];passed=[]
    keys=[]
    for key in fibers.files:
        if key.startswith('fiber_'):
            bits=key.split('_');label=tuple(map(int,bits[1:4]))
            if label not in keys:keys.append(label)
    assert len(keys)==108
    for i,j,phase in sorted(keys):
        opts=[fibers[f'fiber_{i}_{j}_{phase}_{k}']for k in kids];num=0;tests=0
        for values in itertools.product(*opts):
            tests+=1;target=joint(list(values)+[known])
            if D.contains(Permutation(target.tolist())):
                num+=1;passed.append([i,j,phase]+list(map(int,values)))
        row={'label':[i,j,phase],'tested':tests,'passed':num};rows.append(row)
        if num==0:print('EXCLUDED',row,flush=True)
    counts={}
    for r in rows:counts[r['passed']]=counts.get(r['passed'],0)+1
    out={'statement':'D23.F41 draft computation','kernel_ids':kids,
         'pairs':pairs.tolist(),'known_cubic_value':int(known),'joint_order':go,
         'joint_derived_order':do,'cases':rows,'passing_count_histogram':counts,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact common ordinary commutator word only; full gentle Nielsen cycles are an additional constraint.'}
    np.savez_compressed(HERE/'affine216_last_commonword.npz',
        generators=np.array([g.array_form for g in G.generators]),
        derived_generators=np.array([g.array_form for g in D.generators]),
        passed=np.array(passed),pairs=pairs,affine_permutations=aff,kernel_ids=kids)
    (HERE/'affine216_last_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='cases'},indent=2),flush=True)
if __name__=='__main__':run()
