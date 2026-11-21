#!/usr/bin/env python3
"""Exact raw mixed group and its marked projection to the degree1344 image."""
from pathlib import Path
import time,numpy as np,json,pickle
from sympy.combinatorics import Permutation,PermutationGroup
def run():
    R=Path(__file__).resolve().parents[1]
    D=np.load(R/'records/hurwitz_product_fixed_cover.npz');A,B,C=D['generators']
    S=A[B[A]];gs=[C[C],S[S]];t=time.monotonic()
    G=PermutationGroup([Permutation(g.tolist())for g in gs]);o=int(G.order())
    meta={'raw_mixed_order':o,'projective_mixed_order':40122452017152,
          'projection_kernel_order':o//40122452017152,'elapsed_seconds':time.monotonic()-t}
    assert o%40122452017152==0 and meta['projection_kernel_order']==1
    (R/'records/hurwitz_raw_mixed_group.json').write_text(json.dumps(meta,indent=2)+'\n')
    np.savez_compressed(R/'records/hurwitz_raw_mixed_group.npz',generators=np.array(gs),
                        base=np.array(G.base),
                        strong_generators=np.array([p.array_form for p in G.strong_gens],dtype=np.int16))
    with(R/'private/hurwitz_raw_mixed_group.pkl').open('wb')as f:pickle.dump(G,f)
    print(meta,flush=True)
if __name__=='__main__':run()
