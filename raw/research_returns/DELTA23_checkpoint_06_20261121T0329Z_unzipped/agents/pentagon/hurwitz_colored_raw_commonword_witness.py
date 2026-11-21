#!/usr/bin/env python3
"""Evaluate the certified H9+38 common-word witness on the raw colored first and mixed pairs."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;FIVE=HERE.parent/'five_level_six';CHAR=HERE.parent/'characters';start=time.monotonic()
def restore(name):
 args,state=pickle.loads((FIVE/name).read_bytes());G=PermutationGroup(args);G.__dict__.update(state);return G
old=restore('hurwitz_first_full_cyclic_core_state.pkl');G=restore('hurwitz_colored_full_commonword_state.pkl')
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];N=len(A);I=np.arange(N);s=A[B[A]]
xs=np.r_[A[A],N+C[C]].astype(np.int32);ys=np.r_[B[B],N+s[s]].astype(np.int32)
for g in [xs,ys]:
 q=np.arange(2*N)
 for _ in range(12):q=g[q]
 assert np.array_equal(q,np.arange(2*N))
class Evaluator:
 def __init__(self,group,seed_values):
  self.G=group;self.memo={};self.I=np.arange(len(seed_values[0][0]),dtype=np.int32)
  assert len(seed_values)==len(group.generators)
  for p,(v,e)in zip(group.generators,seed_values):
   self.memo[p]=(v,np.array(e,dtype=int)%12);self.memo[p**-1]=(np.argsort(v).astype(np.int32),-np.array(e,dtype=int)%12)
 def evaluate(self,p):
  if p.is_identity:return self.I,np.zeros(2,dtype=int)
  if p in self.memo:return self.memo[p]
  if p in self.G._strong_gens_slp:fac=self.G._strong_gens_slp[p]
  elif p**-1 in self.G._strong_gens_slp:
   a,e=self.evaluate(p**-1);v=np.argsort(a).astype(np.int32);e=-e%12;self.memo[p]=(v,e);return v,e
  else:fac=self.G.generator_product(p,original=False)
  v=self.I.copy();e=np.zeros(2,dtype=int)
  for q in fac:
   w,d=self.evaluate(q);v=v[w];e=(e+d)%12
  self.memo[p]=(v,e);self.memo[p**-1]=(np.argsort(v).astype(np.int32),-e%12);return v,e
first=Evaluator(old,[(xs,[1,0]),(ys,[0,1])]);seeds=[]
assert len(old.strong_gens)==len(G.generators)
for i,(p,q)in enumerate(zip(old.strong_gens,G.generators)):
 assert np.array_equal(q.array_form[:1948],p.array_form)
 seeds.append(first.evaluate(p))
print('lifted old strong generators',len(seeds),flush=True)
second=Evaluator(G,seeds)
core=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz');idx=next(i for i,l in enumerate(core['passing_labels'])if np.array_equal(l,[1,0]))
f=np.load(HERE/'hurwitz_first_four_block_lifts.npz')['first_f_1'];target0=np.r_[f,448+np.arange(24),472+core['passing_tuples'][idx]]
colored=np.load(HERE/'hurwitz_colored_full_core.npz');target=np.r_[target0,1948+colored['target_0']]
p=Permutation(target.tolist());assert G.contains(p)
image,exponents=second.evaluate(p);assert np.array_equal(exponents,[0,0])
F,R=image[:N],image[N:]-N
sphere=np.load(HERE/'hurwitz_spherical_five_orbit.npz');co=np.load(HERE/'hurwitz_order5_cochains.npz');idx=next(i for i,l in enumerate(co['labels'])if np.array_equal(l,[1,0]))
Fb=co['f12'][idx];rho=sphere['rho'];Rb=np.argsort(rho)[Fb[rho]];Fb=Fb[1344:]-1344;Rb=Rb[1344:]-1344
f_matches=bool(np.array_equal(F//6,Fb[I//6]));r_matches=bool(np.array_equal(R//6,Rb[I//6]))
phase=np.load(HERE/'hurwitz_colored_last_gentle.npz')['potential_0'];V=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V'];W=6*V[I//6]+(I%6+phase[I//6])%6;Wi=np.argsort(W)
newB=W[B[Wi]];wantB=np.argsort(F)[B[F]];newC=W[C[Wi]];wantC=R[C[np.argsort(R)]]
beq=np.array_equal(newB,wantB);ceq=np.array_equal(newC,wantC)
np.savez_compressed(HERE/'hurwitz_colored_raw_commonword_witness.npz',raw_F=F,raw_R=R,raw_V=W,B_defect=newB[np.argsort(wantB)],C_defect=newC[np.argsort(wantC)],source_target=target)
out={'source_target_membership':True,'word_exponents_mod12':exponents.tolist(),'raw_generator_orders_divide12':True,'first_projective_value_matches':f_matches,'mixed_projective_value_matches':r_matches,
 'raw_B_covariance':beq,'raw_C_covariance':ceq,'B_disagreement_points':int(np.sum(newB!=wantB)),'C_disagreement_points':int(np.sum(newC!=wantC)),
 'old_evaluator_memo':len(first.memo),'joint_evaluator_memo':len(second.memo),'elapsed_seconds':time.monotonic()-start,
 'scope':'One unrestored ordinary commutator-word witness chosen by the Qsol-based H9 source SLP. Its original first perfect residual has not been corrected. Projection failure rejects this word choice only, not the remaining raw action.'}
(HERE/'hurwitz_colored_raw_commonword_witness.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
