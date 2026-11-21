#!/usr/bin/env python3
"""Rebuild the exact order216 centralizer kernel in the H7 common-word map."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1]

def run():
    start=time.monotonic();data=np.load(ROOT/'records/hurwitz_solvable_commonword.npz')
    J=PermutationGroup([Permutation(g.tolist())for g in data['derived_generators']])
    assert J.order()==1083306204463104
    fibers=np.load(HERE/'records/hurwitz_mixed_derived_fibers.npz')
    C=PermutationGroup([Permutation(g.tolist())for g in fibers['derived_centralizer_generators']])
    assert C.order()==432
    identity=np.arange(472);out=[]
    for p in C.generate_schreier_sims():
        c=np.array(p.array_form)
        if J.contains(Permutation(np.r_[identity,472+c].tolist())):out.append(c)
    assert len(out)==216
    K=PermutationGroup([Permutation(g.tolist())for g in out]);assert K.order()==216
    np.savez_compressed(HERE/'records/hurwitz_commonword_centralizer216.npz',elements=np.array(out),
        generators=np.array([g.array_form for g in K.generators]))
    result={'order':216,'containing_centralizer_order':432,'commonword_derived_order':int(J.order()),
            'enumerated_entire_containing_centralizer':True,'elapsed_seconds':time.monotonic()-start,'result':'PASS'}
    (HERE/'records/hurwitz_commonword_centralizer216.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':run()
