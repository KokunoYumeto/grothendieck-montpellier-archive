#!/usr/bin/env python3
"""Exact product structure and nine-block C-conjugator fibers of signed kernel."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'

def group(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])

def run():
    start=time.monotonic();ks=np.load(ROOT/'records/hurwitz_mixed_signed_kernel.npz')['full_kernel_generators']
    bm=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'][2]
    K=group(ks);assert K.order()==278628139008
    np.savez_compressed(HERE/'records/hurwitz_mixed_full_kernel_bsgs.npz',base=np.array(K.base),
                        strong_generators=np.array([g.array_form for g in K.strong_gens]))
    orders={};nine=None
    for name,blocks,expected in [('fixed',[0,9],104976),('nine',[1,2,3,4,5,6,7,8,10],110592),('eleven',[11],24)]:
        sub=np.flatnonzero(np.isin(bm,blocks));ix=np.full(1344,-1,dtype=int);ix[sub]=np.arange(len(sub))
        gs=np.unique(np.array([ix[g[sub]]for g in ks]),axis=0);H=group(gs)
        assert H.order()==expected;orders[name]=expected
        if name=='nine':nine=(sub,ix,gs,H)
    assert int(K.order())==int(np.prod(list(orders.values())))
    print('K product orders',orders,'total',K.order(),flush=True)
    sub,ix,gs,H=nine;c=ix[C[sub]]
    vs=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1']
    vl=np.array([ix[v[sub]]for v in vs]);targets=np.unique(np.array([v[c[np.argsort(v)]]for v in vl]),axis=0)
    assert len(targets)==4
    # The short sample merely rejects candidates early. Every accepted
    # candidate is checked on all 1008 points.
    sample=np.array([np.flatnonzero(bm[sub]==b)[0]for b in sorted(set(bm[sub]))])
    witnesses=[[]for t in targets]
    for p in H.generate_schreier_sims():
        g=np.array(p.array_form)
        plausible=np.flatnonzero(np.all(targets[:,g[sample]]==g[c[sample]],axis=1))
        for no in plausible:
            if np.array_equal(g[c],targets[no][g]):witnesses[no].append(g)
    assert [len(w)for w in witnesses]==[8]*4
    np.savez_compressed(HERE/'records/hurwitz_mixed_nine_cycle_probe.npz',subset=sub,generators=gs,C=c,
                        targets=targets,**{f'R_{i}':np.array(w)for i,w in enumerate(witnesses)})
    out={'statement':'D23.C26','K_order':int(K.order()),'projection_orders':orders,
         'full_direct_product':True,'K9_order':110592,'a3':1,'target_count':4,
         'witness_counts':[8]*4,'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact signed-kernel C covariance; derived membership is handled by the separate fiber certificate.','result':'PASS'}
    (HERE/'records/hurwitz_mixed_nine_cycle_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    (HERE/'records/hurwitz_mixed_full_kernel_order.json').write_text(json.dumps({'order':int(K.order()),
        'base':K.base,'projection_orders':orders,'full_direct_product':True},indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
