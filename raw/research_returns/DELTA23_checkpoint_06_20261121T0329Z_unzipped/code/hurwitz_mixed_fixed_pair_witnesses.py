#!/usr/bin/env python3
"""Complete simultaneous C-conjugators on the two fixed mixed blocks."""
from pathlib import Path
import numpy as np,json,time
from sympy.combinatorics import Permutation,PermutationGroup
def run():
    st=time.monotonic();R=Path(__file__).resolve().parents[1];p=R/'agents/pentagon'
    A,B,C=np.load(p/'hurwitz_cubic216_four_13.npz')['generators']
    bm=np.load(p/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    K=np.load(R/'records/hurwitz_mixed_signed_kernel.npz')['full_kernel_generators']
    pts=np.flatnonzero(np.isin(bm,[0,9]));idx={int(v):j for j,v in enumerate(pts)}
    ks=[np.array([idx[int(g[v])]for v in pts])for g in K]
    G=PermutationGroup([Permutation(g.tolist())for g in ks]);assert G.order()==104976
    c=np.array([idx[int(C[v])]for v in pts]);D=np.load(p/'hurwitz_global_conjugators.npz')
    targets=[];tindex={};maps={}
    for a3 in [0,1]:
        ix=[]
        for V in D[f'mixed72_V_{a3}']:
            v=np.array([idx[int(V[t])]for t in pts]);q=v[c[np.argsort(v)]];key=q.tobytes()
            if key not in tindex:tindex[key]=len(targets);targets.append(q)
            ix.append(tindex[key])
        maps[f'target_index_{a3}']=np.array(ix)
    witnesses=[[]for _ in targets]
    for pp in G.generate_schreier_sims():
        rr=np.array(pp.array_form);cc=rr[c[np.argsort(rr)]];j=tindex.get(cc.tobytes())
        if j is not None:witnesses[j].append(rr)
    assert all(len(w)==54 for w in witnesses)
    out={'subset':pts,'C':c,'targets':np.array(targets),**maps,
         **{f'R_{j}':np.array(w)for j,w in enumerate(witnesses)}}
    np.savez_compressed(R/'records/hurwitz_mixed_fixed_pair_witnesses.npz',**out)
    meta={'K09_order':104976,'target_count':len(targets),
          'conjugators_per_target':[len(w)for w in witnesses],
          'all72_candidates_both_bits_pass':True,'elapsed_seconds':time.monotonic()-st}
    (R/'records/hurwitz_mixed_fixed_pair_witnesses.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(meta)
if __name__=='__main__':run()
