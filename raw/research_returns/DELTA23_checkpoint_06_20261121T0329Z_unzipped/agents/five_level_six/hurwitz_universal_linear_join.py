#!/usr/bin/env python3
"""Smaller exact quotient for a translation-module approach to F45."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_colored_word_evaluator import load_group,WordEvaluator,target_zero
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[1]
def run():
    start=time.monotonic();old=load_group(HERE/'hurwitz_first_full_cyclic_core_state.pkl')
    e=np.load(WORK/'records/affine216_universal_group.npz');prefix=9*len(e['old_kernel_ids'])
    gens=np.array([np.r_[p.array_form,1948+v[:prefix]]for p,v in zip(old.generators,e['generators'])])
    ev=WordEvaluator(old,gens);seeds=[Permutation(ev.evaluate(p).tolist())for p in old.strong_gens]
    G=PermutationGroup(seeds);G._schreier_sims(base=old.base);order=int(G.order())
    pickle.dump((list(G.args),G.__dict__),open(HERE/'hurwitz_universal_linear_join_state.pkl','wb'))
    rows=[];saved={'generators':gens,'base':np.array(G.base)}
    for case in range(4):
        t=np.r_[target_zero()[:1948],1948+e['normalized_f_lifts'][case,:prefix]]
        yes=bool(G.contains(Permutation(t.tolist())));rows.append({'case':case,'member':yes})
        saved[f'target_{case}']=t
    np.savez_compressed(HERE/'hurwitz_universal_linear_join.npz',**saved)
    out={'degree':len(gens[0]),'group_order':order,'cases':rows,'elapsed_seconds':time.monotonic()-start}
    (HERE/'hurwitz_universal_linear_join.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
