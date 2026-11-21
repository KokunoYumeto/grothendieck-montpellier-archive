#!/usr/bin/env python3
"""Adjoin the two admissible raw48 gentle residues to the fully restored source."""
from pathlib import Path
import sys,pickle,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import colored_evaluator,WordEvaluator
start=time.monotonic();args,state=pickle.loads((HERE/'hurwitz_colored_full_first_join_state.pkl').read_bytes());old=PermutationGroup(args);old.__dict__.update(state)
first=np.load(HERE/'hurwitz_colored_full_first_join.npz');core=np.load(HERE/'hurwitz_colored_raw48_gentle.npz')
ev0=colored_evaluator(core['x'],core['y']);ev=WordEvaluator(old,[ev0.evaluate(p)for p in first['seed_old']]);seed_old=list(old.strong_gens)
seed_arrays=np.array([np.r_[p.array_form,3634+ev.evaluate(p)]for p in seed_old]);G=PermutationGroup([Permutation(g.tolist())for g in seed_arrays])
print('building3922 with',len(seed_arrays),'lifted fullfirst strong generators',flush=True);G._schreier_sims(base=old.base);go=int(G.order());print('order',go,'kernel',go//old.order(),flush=True)
targets=[];rows=[]
for i,cc in enumerate(core['passing']):
 target=np.r_[first['target'],3634+cc];yes=G.contains(Permutation(target.tolist()));targets.append(target);rows.append({'raw48_choice':i,'commonword_member':bool(yes),'derived_if_present':bool(yes)});print(rows[-1],flush=True)
np.savez_compressed(HERE/'hurwitz_colored_raw48_full_join.npz',seed_old=np.array([p.array_form for p in seed_old]),seed_generators=seed_arrays,targets=targets)
(HERE/'hurwitz_colored_raw48_full_join_state.pkl').write_bytes(pickle.dumps((G.args,G.__dict__)))
out={'degree':3922,'group_order':go,'old_order':int(old.order()),'kernel_order':int(go//old.order()),'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Full originalfirst, H9, one fixed complete38E0 extension, and complete raw48 gentle/C-covariance residues. Membership is an ordinary commonword result, not actualGT existence.'}
(HERE/'hurwitz_colored_raw48_full_join.json').write_text(json.dumps(out,indent=2)+'\n')
