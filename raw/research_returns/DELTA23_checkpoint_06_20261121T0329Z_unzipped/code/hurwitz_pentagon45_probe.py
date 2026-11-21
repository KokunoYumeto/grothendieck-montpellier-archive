"""Full third mixed pair and the value required by the literal pentagon.

Working calculation, not a profinite realization assertion.
"""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'work';PENT=W/'agents/pentagon';FIVE=W/'agents/five_level_six'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist())for g in gs])
def run():
 start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 Z=A[B[A]];Z=Z[Z];T=C[B[C]];T=T[T]
 J=A[B[C[A[B[A]]]]];ji=np.argsort(J)
 assert np.array_equal(J[A[A][ji]],C[C])
 assert np.array_equal(J[Z[ji]],T)
 M=pg([Z,T]);print('M45 order',M.order(),flush=True)
 D=M.derived_subgroup();print('M45 derived',D.order(),flush=True)
 with (W/'private/hurwitz_mixed45_state.pkl').open('wb')as f:pickle.dump([(list(g.args),g.__dict__)for g in [M,D]],f)
 Fdata=np.load(FIVE/'hurwitz_first_pair_covariance.npz');RR=np.load(W/'records/hurwitz_solvable_fiber_filter.npz')
 passing=[];targets=[]
 for idx,R in zip(RR['base_indices'],RR['R_witnesses']):
  F=Fdata[f'F_1_{idx}'];R51=J[np.argsort(R)[ji]];F23=J[np.argsort(F)[ji]]
  # R34 R51 F23 H45 F12=1, with left composition a[b].
  left=R[R51[F23]];H=np.argsort(left)[np.argsort(F)]
  assert np.array_equal(left[H[F]],np.arange(1344))
  ok=D.contains(Permutation(H.tolist()));print('V',int(idx),'H45derived',ok,flush=True)
  if ok:passing.append(int(idx))
  targets.append(H)
 np.savez_compressed(W/'records/hurwitz_pentagon45_probe.npz',generators=np.array([Z,T]),derived_generators=np.array([p.array_form for p in D.generators]),base_indices=RR['base_indices'],required_H45=np.array(targets))
 out={'mixed45_order':int(M.order()),'mixed45_derived_order':int(D.order()),'passing_H7_witness_indices':passing,'elapsed_seconds':time.monotonic()-start,'scope':'One recorded R perV only; failed witness is not an excluded V. Full gentle and all common-word correlations remain.'}
 (W/'records/hurwitz_pentagon45_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
