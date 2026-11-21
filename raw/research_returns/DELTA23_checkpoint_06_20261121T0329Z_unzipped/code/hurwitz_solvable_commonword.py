#!/usr/bin/env python3
"""Join the explicit first solvable quotient to the entire mixed image."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1];PENT=ROOT/'agents/pentagon'
def group(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def run():
    st=time.monotonic()
    first=np.load(ROOT/'records/hurwitz_first_solvable_joint.npz')['generators']
    A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];s=A[B[A]]
    mixed=np.array([C[C],s[s]])
    joined=np.array([np.r_[g,472+h]for g,h in zip(first,mixed)])
    G=group(joined);go=int(G.order());print('joint order',go,flush=True)
    D=G.derived_subgroup();do=int(D.order());print('joint derived order',do,'generators',len(D.generators),flush=True)
    q=group(first);m=group(mixed);qo=int(q.order());mo=int(m.order())
    common=qo*mo//go;assert go*common==qo*mo
    out={'statement':'D23.H7 probe','first_order':qo,'mixed_order':mo,'joint_order':go,
         'common_quotient_order':common,'joint_derived_order':do,
         'elapsed_seconds':time.monotonic()-st,
         'scope':'Exact finite same-word image. Maximality of first solvable quotient checked separately.'}
    (ROOT/'records/hurwitz_solvable_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(ROOT/'records/hurwitz_solvable_commonword.npz',generators=joined,
                       derived_generators=np.array([p.array_form for p in D.generators],dtype=np.int16),
                       base=np.array(G.base),strong_generators=np.array([p.array_form for p in G.strong_gens],dtype=np.int16))
    print(json.dumps(out),flush=True)
if __name__=='__main__':run()
