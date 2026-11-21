#!/usr/bin/env python3
"""Evaluate a fully first-restored common word at both raw colored pairs."""
from pathlib import Path
import sys,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';sys.path.insert(0,str(FIVE))
from hurwitz_colored_word_evaluator import colored_evaluator,WordEvaluator
start=time.monotonic();raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];N=len(A);I=np.arange(N);s=A[B[A]]
xab=np.array([12*((i//12+1)%12)+i%12 for i in range(144)]);yab=np.array([12*(i//12)+(i%12+1)%12 for i in range(144)])
x=np.r_[A[A],N+C[C],2*N+xab];y=np.r_[B[B],N+s[s],2*N+yab]
for g in[x,y]:
 q=np.arange(len(g))
 for _ in range(12):q=g[q]
 assert np.array_equal(q,np.arange(len(g)))
old_ev=colored_evaluator(x,y);d=np.load(HERE/'hurwitz_colored_full_first_join.npz');args,state=pickle.loads((HERE/'hurwitz_colored_full_first_join_state.pkl').read_bytes());G=PermutationGroup(args);G.__dict__.update(state)
seed_values=[old_ev.evaluate(p)for p in d['seed_old']];print('evaluated',len(seed_values),'fullfirst seed words',flush=True)
assert len(seed_values)==len(G.generators)
ev=WordEvaluator(G,seed_values);target=d['target'];assert G.contains(Permutation(target.tolist()));out=ev.evaluate(target)
F,R=out[:N],out[N:2*N]-N;assert np.array_equal(out[2*N:]-2*N,np.arange(144))
sphere=np.load(HERE/'hurwitz_spherical_five_orbit.npz');co=np.load(HERE/'hurwitz_order5_cochains.npz');idx=next(i for i,l in enumerate(co['labels'])if np.array_equal(l,[1,0]));Fb=co['f12'][idx];rho=sphere['rho'];Rb=np.argsort(rho)[Fb[rho]];Fb=Fb[1344:]-1344;Rb=Rb[1344:]-1344
fm=np.array_equal(F//6,Fb[I//6]);rm=np.array_equal(R//6,Rb[I//6]);assert fm and rm
V=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V'];pot=np.load(HERE/'hurwitz_colored_last_gentle.npz')['potential_0'];W=6*V[I//6]+(I%6+pot[I//6])%6;Wi=np.argsort(W)
nb=W[B[Wi]];wb=np.argsort(F)[B[F]];nc=W[C[Wi]];wc=R[C[np.argsort(R)]]
bdef=nb[np.argsort(wb)];cdef=nc[np.argsort(wc)]
np.savez_compressed(HERE/'hurwitz_colored_raw_restored_witness.npz',raw_F=F,raw_R=R,raw_V=W,B_defect=bdef,C_defect=cdef)
info={'full_first_restored_source_membership':True,'word_exponents_mod12_zero':True,'raw_generators_order12':True,'first_projective_matches':bool(fm),'mixed_projective_matches':bool(rm),
 'raw_B_covariance':bool(np.array_equal(nb,wb)),'raw_C_covariance':bool(np.array_equal(nc,wc)),
 'B_disagreement_points':int(np.sum(nb!=wb)),'C_disagreement_points':int(np.sum(nc!=wc)),
 'B_defect_order':int(Permutation(bdef.tolist()).order()),'C_defect_order':int(Permutation(cdef.tolist()).order()),'elapsed_seconds':time.monotonic()-start,
 'scope':'One ordinary commutator-word choice after explicit fullfirst restoration; failed raw equations reject this choice only.'}
(HERE/'hurwitz_colored_raw_restored_witness.json').write_text(json.dumps(info,indent=2)+'\n');print(info,flush=True)
