"""Evaluate an ordinary word selected by the H9+colored marked quotient.

The joined BSGS starts with lifted H9 strong generators, so there are
two SLP layers.  Evaluation in a further target is a word choice, not
an assertion that its kernel factors through either stored quotient.
"""
from pathlib import Path
import pickle
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent

def load_group(path):
    args,state=pickle.load(open(path,'rb'));G=PermutationGroup(args);G.__dict__.update(state)
    return G

class WordEvaluator:
    def __init__(self,group,seed_values):
        self.G=group;self.I=np.arange(len(seed_values[0]));self.memo={}
        assert len(group.generators)==len(seed_values)
        for p,q in zip(group.generators,seed_values):
            self.memo[p]=np.asarray(q);self.memo[p**-1]=np.argsort(q)
    def evaluate(self,p):
        if not isinstance(p,Permutation):p=Permutation(np.asarray(p).tolist())
        if p.is_identity:return self.I
        if p in self.memo:return self.memo[p]
        if p in self.G._strong_gens_slp:word=self.G._strong_gens_slp[p]
        elif p**-1 in self.G._strong_gens_slp:return np.argsort(self.evaluate(p**-1))
        else:word=self.G.generator_product(p,original=False)
        out=self.I.copy()
        for q in word:out=out[self.evaluate(q)]
        self.memo[p]=out;self.memo[p**-1]=np.argsort(out)
        return out

def colored_evaluator(x,y):
    old=load_group(HERE/'hurwitz_first_full_cyclic_core_state.pkl')
    joined=load_group(HERE/'hurwitz_colored_full_commonword_state.pkl')
    first=WordEvaluator(old,[x,y])
    assert len(joined.generators)==len(old.strong_gens)
    return WordEvaluator(joined,[first.evaluate(p)for p in old.strong_gens])

def target_zero():
    pent=HERE.parent/'pentagon';char=HERE.parent/'characters'
    core=np.load(char/'records/hurwitz_full_mixed_s3_membership.npz')
    i=next(i for i,l in enumerate(core['passing_labels'])if list(l)==[1,0])
    f=np.load(pent/'hurwitz_first_four_block_lifts.npz')['first_f_1']
    e=np.load(pent/'hurwitz_colored_full_core.npz')['target_0']
    return np.r_[f,448+np.arange(24),472+core['passing_tuples'][i],1948+e]

if __name__=='__main__':
    gens=np.load(HERE/'hurwitz_colored_full_commonword_group.npz')['generators']
    E=colored_evaluator(*gens);target=target_zero()
    assert np.array_equal(E.evaluate(target),target)
    np.savez_compressed(HERE/'hurwitz_colored_full_commonword_target.npz',target_0=target)
    print('PASS: exact two-level word evaluation in the defining quotient.')
