#!/usr/bin/env python3
"""Join the full H9 braid core with the colored thirty-eight E0 kernels."""
from pathlib import Path
import pickle,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())
def run():
    start=time.monotonic();args,state=pickle.load(open(HERE/'hurwitz_first_full_cyclic_core_state.pkl','rb'))
    old=PermutationGroup(args);old.__dict__.update(state)
    c=np.load(PENT/'hurwitz_colored_full_core.npz');eg=c['generators'];n=1948+eg.shape[1]
    gens=np.array([np.r_[g.array_form,1948+e]for g,e in zip(old.generators,eg)])
    assert all(pp(g).order()==12 for g in gens)
    memo={}
    for p,a in zip(old.generators,gens):memo[p]=a;memo[p**-1]=np.argsort(a)
    def lift(p):
        if p.is_identity:return np.arange(n)
        if p in memo:return memo[p]
        if p in old._strong_gens_slp:fac=old._strong_gens_slp[p]
        elif p**-1 in old._strong_gens_slp:return np.argsort(lift(p**-1))
        else:fac=old.generator_product(p,original=False)
        out=np.arange(n)
        for q in fac:out=out[lift(q)]
        assert np.array_equal(out[:1948],p.array_form)
        memo[p]=out;memo[p**-1]=np.argsort(out);return out
    seeds=[pp(lift(p))for p in old.strong_gens];G=PermutationGroup(seeds)
    print('building',n,'with',len(seeds),'liftedoldstronggens',flush=True)
    G._schreier_sims(base=old.base);go=int(G.order());print('order',go,'kernel',go//old.order(),flush=True)
    pickle.dump((list(G.args),G.__dict__),open(HERE/'hurwitz_colored_full_commonword_state.pkl','wb'))
    np.savez_compressed(HERE/'hurwitz_colored_full_commonword_group.npz',generators=gens,
        strong_generators=np.array([g.array_form for g in G.strong_gens],dtype=np.int16),base=G.base)
    core=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz')
    idx=next(i for i,l in enumerate(core['passing_labels'])if list(l)==[1,0])
    f=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['first_f_1']
    target0=np.r_[f,448+np.arange(24),472+core['passing_tuples'][idx]]
    rows=[]
    for assembly in[0,86,172]:
        target=pp(np.r_[target0,1948+c[f'target_{assembly}']]);yes=bool(G.contains(target))
        rows.append({'assembly':assembly,'chosen_full_extension_membership':yes,
                     'derived_membership_if_present':yes})
        print(rows[-1],flush=True)
    out={'statement':'D23.F41 colored commonword extension','degree':n,'group_order':go,
         'old_order':int(old.order()),'kernel_over_old':int(go//old.order()),'cases':rows,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'One specified full S3-extension witness perassembly is tested against exactH9label(1,0). Failure alone does not excludeanassembly because other extensions remain. Originalgeneratorsorder12 andoldabelianizationC12² certifyderivedmembership of passingtargets.'}
    (HERE/'hurwitz_colored_full_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
