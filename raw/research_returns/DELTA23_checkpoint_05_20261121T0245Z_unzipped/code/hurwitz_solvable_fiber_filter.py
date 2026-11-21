#!/usr/bin/env python3
"""Test the actual mixed conjugacy fibers in the first/mixed common-word image."""
from pathlib import Path
import numpy as np,json,time
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1]
def pg(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def run():
    start=time.monotonic()
    data=np.load(ROOT/'records/hurwitz_solvable_commonword.npz')
    D=pg(data['derived_generators']);assert D.order()==1083306204463104
    print('Derived common-word group built',flush=True)
    p21=np.load(ROOT/'agents/pentagon/hurwitz_first_four_block_lifts.npz')
    F=np.r_[p21['first_f_1'],448+np.arange(24)]
    qidentity=np.arange(472);mixedidentity=np.arange(1344)
    pure_cubic=Permutation(np.r_[F,472+mixedidentity].tolist())
    cubic_independent=bool(D.contains(pure_cubic))
    print('Cubic normalized value with all mixed values identity:',cubic_independent,flush=True)
    fiber=np.load(ROOT/'agents/characters/records/hurwitz_mixed_derived_fibers.npz')
    reps=fiber['derived_representatives'];C=pg(fiber['derived_centralizer_generators']);assert C.order()==432
    # Representatives of C/(C intersect ker(common-quotient map)).
    cs=[np.array(g.array_form)for g in C.generate_schreier_sims()]
    cosets=[]
    for c in cs:
        if not any(D.contains(Permutation(np.r_[qidentity,472+np.argsort(r)[c]].tolist()))for r in cosets):
            cosets.append(c)
    print('Centralizer image in common quotient:',len(cosets),flush=True)
    record=[];witnesses=[]
    # The complete first-subgroup normalizer index set, independently recorded in F34.
    ids=[0,1,4,5,10,11,12,13,18,19,22,23,26,27,30,31,34,35,38,39,40,41,46,47,50,51,52,53,56,57,60,61,64,65,68,69]
    for i in ids:
        good=[]
        for j,c in enumerate(cosets):
            r=reps[i][c]
            if D.contains(Permutation(np.r_[F,472+r].tolist())):good.append(j)
        record.append({'base_index':i,'passing_centralizer_cosets':good})
        if good:witnesses.append(reps[i][cosets[good[0]]])
        print('candidate',i,'passing cosets',good,flush=True)
    out={'statement':'D23.H7 fiber probe','cubic_first_value_independent_of_full_mixed':cubic_independent,
         'centralizer_order':432,'centralizer_common_quotient_image_order':len(cosets),
         'candidate_count':len(ids),'surviving_candidates':sum(bool(r['passing_centralizer_cosets'])for r in record),
         'cases':record,'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact same-word first-solvable/full-mixed commutator test; no actual gentle or fullGT lift asserted.'}
    (ROOT/'records/hurwitz_solvable_fiber_filter.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(ROOT/'records/hurwitz_solvable_fiber_filter.npz',base_indices=np.array(ids),
                        R_witnesses=np.array(witnesses),centralizer_coset_representatives=np.array(cosets))
    print(json.dumps({k:v for k,v in out.items()if k!='cases'}),flush=True)
if __name__=='__main__':run()
