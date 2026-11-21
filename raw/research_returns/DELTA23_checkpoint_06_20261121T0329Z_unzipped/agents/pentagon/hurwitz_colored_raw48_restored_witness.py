#!/usr/bin/env python3
"""Replay fullfirst+colored38+raw48 ordinary words in the raw colored action.

Every evaluation is a chosen ordinary word.  No additional marked-kernel
invariance or actual GT realization is asserted by a successful replay.
"""
from pathlib import Path
import sys,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
FIVE=HERE.parent/'five_level_six';sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import colored_evaluator,WordEvaluator

def restored(path):
    args,state=pickle.loads(path.read_bytes())
    g=PermutationGroup(args);g.__dict__.update(state);return g

def main():
    start=time.monotonic()
    raw=np.load(HERE/'hurwitz_colored_raw_cover.npz')
    A,B,C=raw['generators'];n=len(A);ii=np.arange(n);s=A[B[A]]
    ax=np.array([12*((k//12+1)%12)+k%12 for k in range(144)])
    ay=np.array([12*(k//12)+(k%12+1)%12 for k in range(144)])
    x=np.r_[A[A],n+C[C],2*n+ax]
    y=np.r_[B[B],n+s[s],2*n+ay]
    ident=np.arange(len(x))
    for g in [x,y]:
        z=ident.copy()
        for _ in range(12):z=g[z]
        assert np.array_equal(z,ident)
    ev0=colored_evaluator(x,y)
    first=np.load(HERE/'hurwitz_colored_full_first_join.npz')
    g1=restored(HERE/'hurwitz_colored_full_first_join_state.pkl')
    ev1=WordEvaluator(g1,[ev0.evaluate(p)for p in first['seed_old']])
    print('fullfirst seed words evaluated',flush=True)
    join=np.load(HERE/'hurwitz_colored_raw48_full_join.npz')
    g2=restored(HERE/'hurwitz_colored_raw48_full_join_state.pkl')
    ev2=WordEvaluator(g2,[ev1.evaluate(p)for p in join['seed_old']])
    print('raw48 seed words evaluated',flush=True)
    sphere=np.load(HERE/'hurwitz_spherical_five_orbit.npz')
    co=np.load(HERE/'hurwitz_order5_cochains.npz')
    j=next(j for j,l in enumerate(co['labels'])if np.array_equal(l,[1,0]))
    fb=co['f12'][j];rho=sphere['rho'];rb=np.argsort(rho)[fb[rho]]
    fb=fb[1344:]-1344;rb=rb[1344:]-1344
    v=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V']
    pot=np.load(HERE/'hurwitz_colored_last_gentle.npz')['potential_0']
    w=6*v[ii//6]+(ii%6+pot[ii//6])%6;wi=np.argsort(w)
    bnew=w[B[wi]];cnew=w[C[wi]]
    saved={'raw_V':w};rows=[]
    for j,target in enumerate(join['targets']):
        if not g2.contains(Permutation(target.tolist())):
            rows.append({'choice':j,'source_member':False});continue
        out=ev2.evaluate(target);f=out[:n];r=out[n:2*n]-n
        assert np.array_equal(out[2*n:]-2*n,np.arange(144))
        assert np.array_equal(f//6,fb[ii//6])
        assert np.array_equal(r//6,rb[ii//6])
        bwant=np.argsort(f)[B[f]];cwant=r[C[np.argsort(r)]]
        bd=bnew[np.argsort(bwant)];cd=cnew[np.argsort(cwant)]
        row={'choice':j,'source_member':True,'word_exponents_mod12_zero':True,
             'first_and_mixed_projective_match':True,
             'raw_B_covariance':bool(np.array_equal(bnew,bwant)),
             'raw_C_covariance':bool(np.array_equal(cnew,cwant)),
             'B_disagreement_points':int(np.sum(bnew!=bwant)),
             'C_disagreement_points':int(np.sum(cnew!=cwant)),
             'B_defect_order':int(Permutation(bd.tolist()).order()),
             'C_defect_order':int(Permutation(cd.tolist()).order())}
        rows.append(row);saved[f'F_{j}']=f;saved[f'R_{j}']=r
        saved[f'B_defect_{j}']=bd;saved[f'C_defect_{j}']=cd
        print(row,flush=True)
    np.savez_compressed(HERE/'hurwitz_colored_raw48_restored_witness.npz',**saved)
    rec={'cases':rows,'elapsed_seconds':time.monotonic()-start,
         'scope':'Chosen ordinary commutator words after fullfirst, H9, colored38 and complete raw48 gentle/C-covariance constraints. Failed equations reject these words only; successful covariance does not give an actual GT lift.'}
    (HERE/'hurwitz_colored_raw48_restored_witness.json').write_text(json.dumps(rec,indent=2)+'\n')

if __name__=='__main__':main()
