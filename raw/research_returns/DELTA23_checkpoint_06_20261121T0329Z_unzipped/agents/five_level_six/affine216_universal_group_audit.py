#!/usr/bin/env python3
"""Independent reconstruction of the universal146-kernel E0 word image."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_colored_word_evaluator import WordEvaluator
from hurwitz_universal_affine_join import row_basis
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[1];CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())

def run():
    start=time.monotonic();d=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    source=np.load(WORK/'records/affine216_universal_group.npz');kids=source['kernel_ids']
    assert sorted(map(int,kids))==list(range(146))
    oldkids=np.load(WORK/'records/sl2_3_gentle_core.npz')['kernel_ids']
    assert np.array_equal(kids[:len(oldkids)],oldkids)
    els=d['elements'];j=np.arange(9)
    permutations=np.array([3*((e[0]+e[2]*(j//3)+e[3]*(j%3))%3)+(e[1]+e[4]*(j//3)+e[5]*(j%3))%3 for e in els])
    gens=np.array([np.concatenate([9*k+permutations[meta['kernels'][int(kid)]['pair'][i]]for k,kid in enumerate(kids)])for i in range(2)])
    assert np.array_equal(gens,source['generators'])
    prefix=9*len(oldkids);old=PermutationGroup([pp(g[:prefix])for g in gens]);oo=int(old.order())
    assert oo==1179648
    ev=WordEvaluator(old,gens);seeds=[]
    for p in old.strong_gens:
        a=ev.evaluate(p);assert np.array_equal(a[:prefix],p.array_form);seeds.append(pp(a))
    G=PermutationGroup(seeds);G._schreier_sims(base=old.base);order=int(G.order())
    assert G.base[:len(old.base)]==old.base
    vec=[]
    for p in G.strong_gens:
        if any(p(b)!=b for b in old.base):continue
        a=np.array(p.array_form);assert np.array_equal(a[:prefix],np.arange(prefix))
        local=a.reshape(146,9)-9*np.arange(146)[:,None]
        v=np.c_[local[:,0]//3,local[:,0]%3]
        predicted=3*((v[:,0,None]+j[None,:]//3)%3)+(v[:,1,None]+j[None,:]%3)%3
        assert np.array_equal(local,predicted);vec.append(v.ravel())
    basis,piv=row_basis(vec);rank=len(basis)
    assert rank==90 and order==oo*3**rank
    assert order==10295924767167533787777935253869762453225215229952
    stored=source['translation_basis'].reshape(90,292)
    combined,_=row_basis(np.r_[basis,stored]);assert len(combined)==90
    # The four recorded linear fibers are independently replayed against
    # the supplied exact SL2 core values and the reconstructed full image.
    vals=np.load(WORK/'records/sl2_3_gentle_core.npz')['survivors']
    for v,lift in zip(vals,source['normalized_f_lifts']):
        target=np.concatenate([9*k+permutations[value]for k,value in enumerate(v)])
        assert np.array_equal(lift[:prefix],target)
        assert old.contains(pp(target))and G.contains(pp(lift))
    out={'statement':'independent audit of root universal E0 image','all146_literal_marked_generators_reconstructed':True,
         'group_order':order,'linear_quotient_order':oo,'translation_kernel_dimension':rank,
         'stored_translation_basis_span_equal':True,'four_normalized_lifts_checked':True,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Fresh exact whole group reconstruction and complete stabilizer-kernel identification. The classification of the four normalized SL2 gentle states is a separately supplied input.'}
    (HERE/'affine216_universal_group_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
