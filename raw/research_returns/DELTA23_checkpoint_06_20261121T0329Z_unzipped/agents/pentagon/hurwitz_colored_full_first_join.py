#!/usr/bin/env python3
"""Restore the full original first-pair value in the H9+38 common-word source."""
from pathlib import Path
import sys,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import colored_evaluator,load_group,target_zero
start=time.monotonic();old=load_group(FIVE/'hurwitz_colored_full_commonword_state.pkl')
a,b,c=np.load(HERE/'hurwitz_cubic216_four_13.npz')['generators'];x,y=a[a],b[b];ev=colored_evaluator(x,y)
seed_old=list(old.strong_gens);seed_arrays=np.array([np.r_[p.array_form,2290+ev.evaluate(p)]for p in seed_old]);seeds=[Permutation(g.tolist())for g in seed_arrays]
G=PermutationGroup(seeds);assert len(G.generators)==len(seed_old)
print('building',3634,'with',len(seeds),'lifted strong generators',flush=True)
G._schreier_sims(base=old.base);order=int(G.order());kernel=order//old.order();assert kernel==16796160000
print('group order',order,'kernel',kernel,flush=True)
fullF=np.load(HERE/'hurwitz_raw_survivor_covariance.npz')['F_1_0'][::6]//6;target=np.r_[target_zero(),2290+fullF];yes=G.contains(Permutation(target.tolist()));assert yes
np.savez_compressed(HERE/'hurwitz_colored_full_first_join.npz',seed_old=np.array([p.array_form for p in seed_old]),seed_generators=seed_arrays,target=target)
(HERE/'hurwitz_colored_full_first_join_state.pkl').write_bytes(pickle.dumps((G.args,G.__dict__)))
out={'degree':3634,'group_order':order,'old_order':int(old.order()),'kernel_order':int(kernel),'complete_first_target_membership':bool(yes),
 'derived_membership':'Follows from unchanged C12² abelianization; new kernel is perfect, and old target is derived.',
 'elapsed_seconds':time.monotonic()-start,'scope':'Explicit fullfirst-restored source target; no further-target kernel invariance asserted.'}
(HERE/'hurwitz_colored_full_first_join.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
