#!/usr/bin/env python3
"""Exact marked reflection automorphism of the full mixed finite image."""
from pathlib import Path
import pickle,json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon';FIVE=HERE.parent/'five_level_six'

class Reflection:
    def __init__(self,rebuild_graph=False):
        args,st=pickle.loads((FIVE/'hurwitz_full_mixed_groups_state.pkl').read_bytes())[0]
        self.M=PermutationGroup(args);self.M.__dict__.update(st)
        A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];s=A[B[A]]
        self.x=C[C];self.y=s[s];self.z=np.argsort(self.x[self.y]);self.n=1344;self.I=np.arange(self.n)
        self.cache={self.M.generators[0]:self.x,self.M.generators[1]:self.z,Permutation(self.I.tolist()):self.I}
        assert np.array_equal(self.M.generators[0].array_form,self.x)
        assert np.array_equal(self.M.generators[1].array_form,self.y)
        if rebuild_graph:
            n=self.n
            G=PermutationGroup([Permutation(np.r_[self.x,n+self.x].tolist()),Permutation(np.r_[self.y,n+self.z].tolist())])
            assert G.order()==self.M.order()==40122452017152
            self.graph_order=int(G.order())
        else:self.graph_order=40122452017152
        for g in self.M.strong_gens:
            t=self(g);assert self.M.contains(Permutation(t.tolist()))
            assert np.array_equal(self(t),self.x[np.array(g.array_form)[np.argsort(self.x)]])

    def __call__(self,g):
        if not isinstance(g,Permutation):g=Permutation(g.tolist())
        if g in self.cache:return self.cache[g]
        gi=g**-1
        if gi in self.cache:self.cache[g]=np.argsort(self.cache[gi]);return self.cache[g]
        if g in self.M._strong_gens_slp:word=self.M._strong_gens_slp[g]
        elif gi in self.M._strong_gens_slp:
            self.cache[g]=np.argsort(self(gi));return self.cache[g]
        else:word=self.M.generator_product(g,original=False)
        first=self.I.copy();second=self.I.copy()
        for h in word:
            first=first[np.array(h.array_form)];second=second[self(h)]
        assert np.array_equal(first,np.array(g.array_form))
        self.cache[g]=second;return second

if __name__=='__main__':
    start=time.monotonic();r=Reflection(rebuild_graph=True)
    out={'marked_generators':'theta(x)=x; theta(y)=(xy)^-1','group_order':int(r.M.order()),
        'joined_graph_order':r.graph_order,'strong_generators_checked':len(r.M.strong_gens),
        'theta_squared_is_conjugation_by_x':True,'elapsed_seconds':time.monotonic()-start,'result':'PASS'}
    (HERE/'records/hurwitz_full_mixed_reflection.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
