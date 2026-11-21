#!/usr/bin/env python3
"""Append the three new cabled E0 Nielsen orbits to the exact colored join."""
from pathlib import Path
import itertools,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_colored_word_evaluator import colored_evaluator,load_group,target_zero
HERE=Path(__file__).resolve().parent;PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())

def run():
    start=time.monotonic();old=load_group(HERE/'hurwitz_colored_full_commonword_state.pkl')
    oldgens=np.load(HERE/'hurwitz_colored_full_commonword_group.npz')['generators']
    invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    d=np.load(HERE/'hurwitz_cabling_last_gentle.npz')
    info=json.loads((HERE/'hurwitz_cabling_last_gentle.json').read_text())
    oldkids=set(map(int,np.load(PENT/'hurwitz_colored_full_core.npz')['kernel_ids']))
    neworbits=[(j,r['orbit'])for j,r in enumerate(info['gentle_orbits'])if not set(r['orbit'])&oldkids]
    kids=sorted(k for j,orb in neworbits for k in orb);assert len(kids)==15
    ix={k:j for j,k in enumerate(kids)}
    def affine(e):
        u,v,A,B,C,D=map(int,e)
        return np.array([3*((u+A*(j//3)+B*(j%3))%3)+(v+C*(j//3)+D*(j%3))%3 for j in range(9)])
    perms=np.array([affine(e)for e in invt['elements']])
    extra=np.array([np.concatenate([9*j+perms[meta['kernels'][k]['pair'][i]]for j,k in enumerate(kids)])for i in range(2)])
    gens=np.array([np.r_[o,2290+e]for o,e in zip(oldgens,extra)])
    assert all(pp(g).order()==12 for g in gens)
    ev=colored_evaluator(*gens);seeds=[]
    for p in old.strong_gens:
        q=ev.evaluate(p);assert np.array_equal(q[:2290],p.array_form);seeds.append(pp(q))
    print('building',len(gens[0]),'degree with',len(seeds),'lifted strong generators',flush=True)
    G=PermutationGroup(seeds);G._schreier_sims(base=old.base);go=int(G.order())
    print('order',go,'kernel',go//old.order(),'time',time.monotonic()-start,flush=True)
    pickle.dump((list(G.args),G.__dict__),open(HERE/'hurwitz_cabling_full_commonword_state.pkl','wb'))
    saved={'generators':gens,'new_kernel_ids':np.array(kids),'strong_generators':np.array([g.array_form for g in G.strong_gens]),'base':np.array(G.base)}
    lists=[d[f'orbit_{j}_chosen_compatible']for j,orb in neworbits]
    oldtarget=target_zero();tested=0;witness=None;choice=None;assigned=None
    for choices in itertools.product(*[range(len(a))for a in lists]):
        vals=np.zeros(len(kids),dtype=int)
        for (j,orb),aa,c in zip(neworbits,lists,choices):
            vals[[ix[k]for k in orb]]=aa[c]
        target=np.r_[oldtarget,2290+np.concatenate([9*j+perms[v]for j,v in enumerate(vals)])]
        tested+=1
        if G.contains(pp(target)):
            witness=target;choice=choices;assigned=vals;break
    if witness is not None:
        saved['target']=witness;saved['new_values']=assigned
    np.savez_compressed(HERE/'hurwitz_cabling_full_commonword.npz',**saved)
    out={'statement':'D23.F43 full cabled common-word probe','degree':len(gens[0]),'new_kernel_count':len(kids),
         'full_E0_kernel_count':len(oldkids)+len(kids),'group_order':go,'old_order':int(old.order()),
         'kernel_over_old':int(go//old.order()),'available_extension_count':int(np.prod([len(a)for a in lists])),
         'tested':tested,'common_commutator_word':witness is not None,'choice':list(choice)if choice else None,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'A passing target realizes all H9 braid values, the chosen colored38 table and all additional cabled gentle orbits by one ordinary commutator word. The old C12 squared abelianization and order12 original generators certify derived membership. No actual profinite gentle realization is asserted.'}
    (HERE/'hurwitz_cabling_full_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
