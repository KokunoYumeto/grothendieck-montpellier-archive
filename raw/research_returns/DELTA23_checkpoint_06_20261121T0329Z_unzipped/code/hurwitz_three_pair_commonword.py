"""Exact common commutator-word image of Qsol, mixed34, mixed45."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'work';PENT=W/'agents/pentagon'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist())for g in gs])
def run():
 start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 Z=A[B[A]];Z=Z[Z];T=C[B[C]];T=T[T]
 Q=np.load(W/'records/hurwitz_first_solvable_joint.npz')['generators'];gs=[np.r_[Q[0],472+C[C],1816+Z],np.r_[Q[1],472+Z,1816+T]]
 G=pg(gs);print('Joint3160 order',G.order(),flush=True)
 D=G.derived_subgroup();print('Joint3160derived',D.order(),flush=True)
 with (W/'private/hurwitz_three_pair_state.pkl').open('wb')as f:pickle.dump([(list(g.args),g.__dict__)for g in [G,D]],f)
 ff=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['first_f_1'];q=np.r_[ff,448+np.arange(24)]
 data=np.load(W/'records/hurwitz_pentagon45_fibers.npz');cases=[];records={}
 for idx in data['base_indices']:
  rr=data[f'R_{idx}'];hh=data[f'H_{idx}'];cs=data[f'centralizer_indices_{idx}'];passed=[]
  for j,(r,h,c)in enumerate(zip(rr,hh,cs)):
   ok=bool(D.contains(Permutation(np.r_[q,472+r,1816+h].tolist())))
   print('V',int(idx),'C216index',int(c),'sameword',ok,flush=True)
   cases.append({'candidate_index':int(idx),'centralizer_index':int(c),'commonword':ok})
   if ok:passed.append(j)
  records[f'R_{idx}']=rr[passed];records[f'H_{idx}']=hh[passed];records[f'centralizer_indices_{idx}']=cs[passed]
 np.savez_compressed(W/'records/hurwitz_three_pair_commonword.npz',generators=np.array(gs),derived_generators=np.array([p.array_form for p in D.generators]),base_indices=data['base_indices'],**records)
 out={'joint_order':int(G.order()),'joint_derived_order':int(D.order()),'cases':cases,'passing_pairs':sum(x['commonword']for x in cases),'elapsed_seconds':time.monotonic()-start,'scope':'Exact three-evaluation ordinary Fprime image; other freegentle substitutions remain additional. F_V uniqueness is a separate lemma under investigation.'}
 (W/'records/hurwitz_three_pair_commonword.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='cases'},indent=2))
if __name__=='__main__':run()
