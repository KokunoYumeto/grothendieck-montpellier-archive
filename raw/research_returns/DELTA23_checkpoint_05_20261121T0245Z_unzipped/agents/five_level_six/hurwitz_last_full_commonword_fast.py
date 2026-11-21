#!/usr/bin/env python3
"""Full H9 braid evaluations joined with same-word last-coordinate E0 data."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())
def run():
    start=time.monotonic()
    args,state=pickle.load(open(HERE/'hurwitz_first_full_cyclic_core_state.pkl','rb'))
    old=PermutationGroup(args);old.__dict__.update(state);assert old.degree==1948
    small=np.load(HERE/'affine216_last_commonword.npz');eg=small['generators'][:,:72]
    gens=np.array([np.r_[g.array_form,1948+e]for g,e in zip(old.generators,eg)])
    original=[pp(g)for g in gens];assert all(g.order()==12 for g in original)
    seedmemo={}
    for p,a in zip(old.generators,gens):
        seedmemo[p]=a;seedmemo[p**-1]=np.argsort(a)
    def lift(p):
        if p.is_identity:return np.arange(2020)
        if p in seedmemo:return seedmemo[p]
        if p in old._strong_gens_slp:fac=old._strong_gens_slp[p]
        elif p**-1 in old._strong_gens_slp:return np.argsort(lift(p**-1))
        else:fac=old.generator_product(p,original=False)
        out=np.arange(2020)
        for q in fac:out=out[lift(q)]
        assert np.array_equal(out[:1948],p.array_form)
        seedmemo[p]=out;seedmemo[p**-1]=np.argsort(out);return out
    seeds=[pp(lift(p))for p in old.strong_gens]
    G=PermutationGroup(seeds)
    print('building2020groupwithliftedSGS',len(seeds),'base',len(old.base),flush=True)
    G._schreier_sims(base=old.base);go=int(G.order())
    print('jointorder',go,'oldkernel',go//old.order(),'time',time.monotonic()-start,flush=True)
    pickle.dump((list(G.args),G.__dict__),open(HERE/'hurwitz_last_full_commonword_state.pkl','wb'))
    np.savez_compressed(HERE/'hurwitz_last_full_commonword_group.npz',generators=gens,
        strong_generators=np.array([g.array_form for g in G.strong_gens],dtype=np.int16),base=G.base)
    core=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz')
    cm={tuple(map(int,l)):p for l,p in zip(core['passing_labels'],core['passing_tuples'])}
    ff=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['first_f_1']
    ft=np.r_[ff,448+np.arange(24)]
    affine=small['affine_permutations'];rows=[];passed=[];counts={}
    memo={G.generators[0]:(1,0),G.generators[1]:(0,1),G.generators[0]**-1:(11,0),G.generators[1]**-1:(0,11)}
    def exp(p):
        if p.is_identity:return(0,0)
        if p in memo:return memo[p]
        pi=p**-1
        if pi in memo:return tuple((-v)%12 for v in memo[pi])
        if p in G._strong_gens_slp:fac=G._strong_gens_slp[p]
        elif pi in G._strong_gens_slp:
            r=tuple((-v)%12 for v in exp(pi));memo[p]=r;return r
        else:fac=G.generator_product(p,original=False)
        sums=np.zeros(2,dtype=int)
        for f in fac:sums+=exp(f)
        r=tuple(map(int,sums%12));memo[p]=r;return r
    for row in small['passed']:
        i,j,phase=map(int,row[:3]);vals=row[3:]
        target=np.r_[ft,472+cm[(i,j)],1948+np.concatenate([9*k+affine[v]for k,v in enumerate(vals)])]
        p=pp(target);yes=bool(G.contains(p));ee=(0,0)if yes else None
        # The old quotient already has abelianization C12^2, and the two
        # original generators still have order12. Hence the new group has
        # the same abelianization, so old derived membership suffices.
        rows.append({'label':[i,j,phase],'values':list(map(int,vals)),'membership':yes,'SLP_exponents_mod12':ee})
        counts.setdefault((i,j,phase),0)
        if yes:passed.append(row);counts[(i,j,phase)]+=1
    histogram={}
    for n in counts.values():histogram[n]=histogram.get(n,0)+1
    out={'statement':'D23.F41 full source-to-Hurwitz commonword computation',
         'degree':2020,'joint_order':go,'old_order':int(old.order()),'kernel_over_old':int(go//old.order()),
         'tested_assignments':len(rows),'passed_assignments':len(passed),'raw_case_histogram':histogram,
         'lifted_old_strong_generator_count':len(seeds),'cases':rows,'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact common ordinary commutator word preserving full H9 braid values, each raw phase and its last-coordinate table; actual gentle realization is not asserted.'}
    np.savez_compressed(HERE/'hurwitz_last_full_commonword.npz',passed=np.array(passed),kernel_ids=small['kernel_ids'])
    (HERE/'hurwitz_last_full_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='cases'},indent=2),flush=True)
if __name__=='__main__':run()
