#!/usr/bin/env python3
"""Actual commutator membership in each full mixed C-conjugator fiber."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1]
PENT=HERE.parent/'pentagon';FIVE=HERE.parent/'five_level_six'

def run():
    start=time.monotonic();state=pickle.loads((FIVE/'hurwitz_full_mixed_groups_state.pkl').read_bytes())
    M,D=[PermutationGroup(args)for args,st in state]
    for G,(_,st)in zip([M,D],state):G.__dict__.update(st)
    print('M,D orders',M.order(),D.order(),flush=True)
    bm=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'][2]
    ks=np.load(ROOT/'records/hurwitz_mixed_signed_kernel.npz')['full_kernel_generators']
    fixed=np.load(ROOT/'records/hurwitz_mixed_fixed_pair_witnesses.npz')
    nine=np.load(HERE/'records/hurwitz_mixed_nine_cycle_probe.npz')
    centgens=[];centers={};allsub=[]
    for name,data in [('fixed',fixed),('nine',nine)]:
        sub=data['subset'];c=data['C'];rr=data['R_0'];baseinv=np.argsort(rr[0])
        hh=baseinv[rr]
        assert all(np.array_equal(h[c],c[h])for h in hh)
        H=PermutationGroup([Permutation(h.tolist())for h in hh])
        assert H.order()==len(hh)
        centers[name]=hh;allsub.extend(sub.tolist())
        for p in H.generators:
            g=np.arange(1344);g[sub]=sub[np.array(p.array_form)];centgens.append(g)
    sub=np.flatnonzero(bm==11);ix=np.full(1344,-1,dtype=int);ix[sub]=np.arange(112)
    gg=np.array([ix[g[sub]]for g in ks]);K11=PermutationGroup([Permutation(g.tolist())for g in gg])
    assert K11.order()==24;c=ix[C[sub]]
    h11=np.array([p.array_form for p in K11.generate_schreier_sims()if np.array_equal(np.array(p.array_form)[c],c[np.array(p.array_form)])])
    assert len(h11)==6;centers['eleven']=h11;allsub.extend(sub.tolist())
    assert sorted(allsub)==list(range(1344))
    H11=PermutationGroup([Permutation(h.tolist())for h in h11])
    for p in H11.generators:
        g=np.arange(1344);g[sub]=sub[np.array(p.array_form)];centgens.append(g)
    Cent=PermutationGroup([Permutation(g.tolist())for g in centgens])
    assert Cent.order()==2592 and all(np.array_equal(g[C],C[g])for g in centgens)
    print('centralizer order',Cent.order(),'generators',len(centgens),flush=True)
    L=PermutationGroup(D.generators+[Permutation(g.tolist())for g in centgens])
    print('D times centralizer order',L.order(),'quotient',L.order()//D.order(),flush=True)
    index=int(L.order()//D.order())
    assert 2592%index==0
    CD=Cent.subgroup_search(lambda g:D.contains(g))
    assert CD.order()==2592//index
    transversal=[np.array(g.array_form)for g in Cent.coset_transversal(CD)]
    assert len(transversal)==index
    nine_vs=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1']
    subset9=nine['subset'];lookup={t.tobytes():i for i,t in enumerate(nine['targets'])}
    ix9=np.full(1344,-1,dtype=int);ix9[subset9]=np.arange(len(subset9))
    passing=[];representatives=[];derived_representatives=[]
    for no,v in enumerate(nine_vs):
        vv=ix9[v[subset9]];target=vv[nine['C'][np.argsort(vv)]]
        nine_index=lookup[target.astype(nine['targets'].dtype).tobytes()]
        fidx=int(fixed['target_index_1'][no])
        g=np.arange(1344);g[fixed['subset']]=fixed['subset'][fixed[f'R_{fidx}'][0]]
        g[subset9]=subset9[nine[f'R_{nine_index}'][0]]
        # The block11 target is unchanged by H4, so identity is a conjugator.
        assert np.array_equal(g[C[np.argsort(g)]],v[C[np.argsort(v)]])
        if L.contains(Permutation(g.tolist())):
            passing.append(no)
            corrections=[g[t]for t in transversal if D.contains(Permutation(g[t].tolist()))]
            assert len(corrections)==1
            derived_representatives.append(corrections[0])
        representatives.append(g)
    out={'statement':'D23.C26 probe','M_order':int(M.order()),'derived_order':int(D.order()),
        'signed_kernel_order':278628139008,'centralizer_in_signed_kernel_order':2592,
        'centralizer_abelian_image_order':index,'derived_conjugators_per_passing_V':2592//index,
        'a3_1_passing_indices':passing,'elapsed_seconds':time.monotonic()-start,
        'scope':'Exact full mixed commutator C-covariance. Gentle cycles and same word with first-pair f remain additional conditions.'}
    (HERE/'records/hurwitz_mixed_derived_fibers.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_mixed_derived_fibers.npz',centralizer_generators=np.array(centgens),
                        representatives=np.array(representatives),centralizer_11=h11,subset_11=sub,
                        derived_representatives=np.array(derived_representatives),
                        derived_centralizer_generators=np.array([g.array_form for g in CD.generators]),
                        derived_centralizer_coset_transversal=np.array(transversal),
                        passing_indices=np.array(passing))
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
