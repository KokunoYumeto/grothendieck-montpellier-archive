#!/usr/bin/env python3
"""Join the exact H9 source target with the complete raw48 gentle-core candidates."""
from pathlib import Path
import sys,pickle,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';CHAR=HERE.parent/'characters';sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import load_group,WordEvaluator
start=time.monotonic();old=load_group(FIVE/'hurwitz_first_full_cyclic_core_state.pkl');core=np.load(HERE/'hurwitz_colored_raw48_gentle.npz');eg=np.array([core['x'],core['y']]);n=1948+len(eg[0]);gens=np.array([np.r_[p.array_form,1948+q]for p,q in zip(old.generators,eg)])
assert all(Permutation(g.tolist()).order()==12 for g in gens)
ev=WordEvaluator(old,list(gens));seeds=[Permutation(ev.evaluate(p).tolist())for p in old.strong_gens];G=PermutationGroup(seeds)
print('building degree',n,'seeds',len(seeds),flush=True);G._schreier_sims(base=old.base);go=int(G.order());print('order',go,'kernel',go//old.order(),flush=True)
c28=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz');i=next(i for i,l in enumerate(c28['passing_labels'])if np.array_equal(l,[1,0]));f=np.load(HERE/'hurwitz_first_four_block_lifts.npz')['first_f_1'];oldtarget=np.r_[f,448+np.arange(24),472+c28['passing_tuples'][i]]
rows=[];targets=[]
for j,cc in enumerate(core['passing']):
 target=np.r_[oldtarget,1948+cc];yes=G.contains(Permutation(target.tolist()));rows.append({'gentle_index':j,'exact_commonword_member':bool(yes),'derived_if_present':bool(yes)});targets.append(target);print(rows[-1],flush=True)
np.savez_compressed(HERE/'hurwitz_colored_raw48_commonword.npz',generators=gens,targets=targets,old_target=oldtarget)
(HERE/'hurwitz_colored_raw48_commonword_state.pkl').write_bytes(pickle.dumps((G.args,G.__dict__)))
out={'degree':n,'group_order':go,'old_order':int(old.order()),'kernel_order':int(go//old.order()),'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Exact oldH9 actual-source target with complete raw48 gentle candidates; no optional38-kernel extension is fixed. Generatororders12 andoldabelC12² certify derived membership.'}
(HERE/'hurwitz_colored_raw48_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
