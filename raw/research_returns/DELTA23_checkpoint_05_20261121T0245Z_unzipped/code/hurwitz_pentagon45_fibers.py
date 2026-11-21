"""Exhaust the H7 common-word fibers at the remaining pentagon pair.

This is a finite necessary test, not an existence result for actual GT.
"""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'work';PENT=W/'agents/pentagon';FIVE=W/'agents/five_level_six';CHAR=W/'agents/characters'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist())for g in gs])
def run():
 start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 J=A[B[C[A[B[A]]]]];ji=np.argsort(J)
 state=pickle.loads((W/'private/hurwitz_mixed45_state.pkl').read_bytes());M,D=[PermutationGroup(a)for a,s in state]
 for g,(a,s)in zip([M,D],state):g.__dict__.update(s)
 assert M.order()==13374150672384 and D.order()==557256278016
 cc=np.load(CHAR/'records/hurwitz_commonword_centralizer216.npz')['elements'];assert len(cc)==216
 Fs=np.load(FIVE/'hurwitz_first_pair_covariance.npz');Rdata=np.load(W/'records/hurwitz_solvable_fiber_filter.npz')
 out=[];accepted={}
 for idx,base in zip(Rdata['base_indices'],Rdata['R_witnesses']):
  F=Fs[f'F_1_{idx}'];fi=np.argsort(F);Rlist=[];Hlist=[];cs=[]
  for j,c in enumerate(cc):
   R=base[c];FR=F[R];H=J[FR[ji[np.argsort(FR)]]]
   if D.contains(Permutation(H.tolist())):
    assert np.array_equal(R[J[np.argsort(R)[ji]][J[fi[ji]][H[F]]]],np.arange(1344))
    Rlist.append(R);Hlist.append(H);cs.append(j)
  accepted[f'R_{idx}']=np.array(Rlist,dtype=np.int16);accepted[f'H_{idx}']=np.array(Hlist,dtype=np.int16);accepted[f'centralizer_indices_{idx}']=np.array(cs)
  row={'candidate_index':int(idx),'passing_count':len(cs),'centralizer_indices':cs};out.append(row);print('V',int(idx),'H45derived count',len(cs),flush=True)
 np.savez_compressed(W/'records/hurwitz_pentagon45_fibers.npz',base_indices=Rdata['base_indices'],**accepted)
 result={'cases':out,'candidate_count':len(out),'surviving_candidates':sum(x['passing_count']>0 for x in out),'elapsed_seconds':time.monotonic()-start,'scope':'Complete216 H7 fibers; membership in fullM45derived is necessary only. Does not yet test all gentle or mixed triple common-word correlations.'}
 (W/'records/hurwitz_pentagon45_fibers.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='cases'},indent=2))
if __name__=='__main__':run()
