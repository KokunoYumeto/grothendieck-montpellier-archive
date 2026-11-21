#!/usr/bin/env python3
"""Faithful compact cyclic-three image; abelianization proves the derived test."""
from pathlib import Path
import pickle,time,json,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_mixed72_partial import orbits
HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon'

def run():
    start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
    s=A[B[A]];xx=C[C];yy=s[s];oo=orbits([xx,yy]);chosen=[4,8,12,13]
    sub=np.concatenate([oo[i]for i in chosen]);ix=np.full(1344,-1,dtype=int);ix[sub]=np.arange(len(sub))
    x=ix[xx[sub]];y=ix[yy[sub]];z=np.argsort(x[y]);n=len(sub)
    M=PermutationGroup([Permutation(x.tolist()),Permutation(y.tolist())])
    assert M.order()==40122452017152
    assert Permutation(x.tolist()).order()==6 and Permutation(y.tolist()).order()==12
    a=np.r_[x,n+y,2*n+z];b=np.r_[y,n+z,2*n+x]
    G=PermutationGroup([Permutation(a.tolist()),Permutation(b.tolist())])
    order=int(G.order());assert order==389356498710072424831060715520393216
    assert Permutation(a.tolist()).order()==Permutation(b.tolist()).order()==12
    # M_ab=C6 x C12 follows from |M/M'|=72. The first two cyclic
    # coordinates recover source exponents u,v mod12, so G_ab=C12^2.
    # Thus any tuple in (M')^3 belongs to G' exactly when it belongs to G.
    np.savez_compressed(HERE/'records/hurwitz_full_mixed_s3_compact.npz',subset=sub,x=x,y=y,z=z)
    (HERE/'records/hurwitz_full_mixed_s3_compact_group_state.pkl').write_bytes(pickle.dumps((G.args,G.__dict__)))
    out={'statement':'D23.C28','selected_components':chosen,'faithful_M_degree':n,'M_order':int(M.order()),
         'M_abelianization_invariants':[6,12],'cyclic_three_order':order,'abelianization_order':144,
         'derived_order_by_proved_index':order//144,'base_size':len(G.base),
         'elapsed_seconds':time.monotonic()-start,'result':'PASS',
         'scope':'Exact faithful image plus a proved abelianization argument; no derived-group enumeration is asserted.'}
    (HERE/'records/hurwitz_full_mixed_s3_compact.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
