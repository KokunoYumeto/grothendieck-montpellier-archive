#!/usr/bin/env python3
"""All36 projective orthogonal transition matrices of the twelve-block action."""
from pathlib import Path
import numpy as np,json,importlib.util,contextlib,io
HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon';FIVE=HERE.parent/'five_level_six'
spec=importlib.util.spec_from_file_location('signs112',HERE/'code/hurwitz_orthogonal_signs.py')
mod=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(mod)
o=mod.ort;d=np.load(PENT/'hurwitz_cubic216_four_13.npz')
bd=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz');small=bd['generators'];block=bd['block_map']
trans=np.load(FIVE/'hurwitz_block_correlations.npz')['transversals']
loc={int(v):j for j,v in enumerate(o.base)}
matrices=np.zeros((3,12,6,6),dtype=int);bits=np.zeros((3,12),dtype=int)
for gidx,g in enumerate(d['generators']):
    for i in range(12):
        j=int(small[gidx,i]);points=trans[i][o.base]
        assert np.all(block[points]==i)
        img=np.argsort(trans[j])[g[points]]
        perm=np.array([loc[int(v)]for v in img]);M,mu=o.lift_permutation(perm)
        assert mu==o.determinant(M)==1
        matrices[gidx,i]=M;bits[gidx,i]=int(mod.spinor(M)==2)
def evaluate(word,start):
    state=start;M=np.eye(6,dtype=int)
    for g in reversed(word):
        if g>0:
            idx=g-1;step=matrices[idx,state];state=int(small[idx,state])
        else:
            idx=-g-1;before=int(np.argsort(small[idx])[state]);step=o.inverse(matrices[idx,before]);state=before
        M=step@M%3
    return state,M
def same_projective(A,B):return np.array_equal(A,B)or np.array_equal(A,-B%3)
for i in range(12):
    for u,v in [([1,2,1],[2,1,2]),([2,3,2],[3,2,3]),([1,3],[3,1]),([1,2,3]*4,[])]:
        iu,Mu=evaluate(u,i);iv,Mv=evaluate(v,i)
        assert iu==iv and same_projective(Mu,Mv)
np.savez_compressed(HERE/'records/hurwitz_orthogonal_bundle.npz',block_generators=small,
                    matrices=matrices,spinor_bits=bits,transversals=trans)
out={'statement':'D23.C24 projective bundle certificate','block_count':12,'local_dimension':6,
     'transition_count':36,'all_multipliers':1,'all_determinants':1,
     'spinor_bits_by_braid_generator':bits.tolist(),
     'all_artin_and_central_relations_projectively':True,
     'scope':'Uniform markings by actual group transversals; each block uses C23 quadratic coordinates.',
     'result':'PASS'}
(HERE/'records/hurwitz_orthogonal_bundle.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
