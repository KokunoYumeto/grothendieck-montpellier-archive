#!/usr/bin/env python3
"""Exact marked SL2 quotient on block11 and its local GT consequence."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1]
def pg(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def run():
    started=time.monotonic()
    raw=np.load(ROOT/'agents/pentagon/hurwitz_cubic216_four_13.npz')
    A,B,C=raw['generators'];S=A[B[A]]
    block=np.load(ROOT/'agents/pentagon/hurwitz_cubic216_four_13_block0.npz')['block_map']
    base=np.flatnonzero(block==0)
    trans=np.load(ROOT/'agents/five_level_six/hurwitz_block_correlations.npz')['transversals']
    pts=trans[11][base];index={int(v):j for j,v in enumerate(pts)}
    def restrict(g):
        assert all(int(g[v])in index for v in pts)
        return np.array([index[int(g[v])]for v in pts])
    X,Y=map(restrict,[C[C],S[S]]);c=restrict(C)
    G=pg([X,Y]);D=G.derived_subgroup()
    assert G.order()==72 and D.order()==8
    vec=[v for v in np.ndindex(3,3)if v!=(0,0)];vi={v:j for j,v in enumerate(vec)}
    U=np.array([[1,2],[0,1]]);L=np.array([[1,0],[1,1]])
    targets=[np.array([vi[tuple(M@v%3)]for v in vec])for M in [U,L]]
    joined=pg([np.r_[g,112+t]for g,t in zip([X,Y],targets)])
    assert joined.order()==72 and joined.derived_subgroup().order()==8
    assert pg(targets).order()==24 and pg(targets).derived_subgroup().order()==8
    lifts=np.load(ROOT/'records/hurwitz_h1_orthogonal_lifts.npz')
    cases=[];saved={}
    for a3 in [0,1]:
        vs=lifts[f'case_{a3}_11_permutations']
        passing=[i for i,V in enumerate(vs)if np.array_equal(V[c],c[V])]
        assert len(passing)==1
        i=passing[0];V=vs[i];M=lifts[f'case_{a3}_11_matrices'][i]
        order=int(Permutation(V.tolist()).order())
        assert order==(1 if a3==0 else 2)
        cases.append({'rho':0,'a3':a3,'passing_H3_index':i,'permutation_order':order,
                      'matrix':M.tolist(),'local_permutation':V.tolist()})
        saved[f'V_{a3}']=V;saved[f'M_{a3}']=M
    out={'statement':'D23.H4','mixed_block11_order':72,'mixed_derived_order':8,
         'marked_SL2_joint_order':72,'marked_SL2_joint_derived_order':8,
         'SL2_order':24,'SL2_derived_order':8,'cases':cases,
         'scope':'Actual rho-zero commutator value is identity by P10 linear part; covariance selects these local maps.',
         'elapsed_seconds':time.monotonic()-started,'result':'PASS'}
    (ROOT/'records/hurwitz_block11_harmonic.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(ROOT/'records/hurwitz_block11_harmonic.npz',**saved)
    print(json.dumps({k:v for k,v in out.items()if k!='cases'}))
    print('Passing candidates:',[(r['a3'],r['passing_H3_index'],r['permutation_order'])for r in cases])
if __name__=='__main__':run()
