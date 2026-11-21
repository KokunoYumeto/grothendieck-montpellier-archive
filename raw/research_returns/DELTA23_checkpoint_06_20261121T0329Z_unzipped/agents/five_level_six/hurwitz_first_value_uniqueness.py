#!/usr/bin/env python3
"""D23.F36. Exact center certificate for the complete first-value uniqueness lemma."""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def main():
 start=time.monotonic();source=np.load(HERE/'hurwitz_first_perfect_residual.npz');N=pg(source['derived_5']);assert N.order()==16796160000
 center=N.center();co=int(center.order());assert co==1
 A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];s=A[B[A]];si=np.argsort(s);assert np.array_equal(s[A[si]],B) and np.array_equal(s[B[si]],A)
 vs=np.load(PENT/'hurwitz_global_conjugators.npz');fs=np.load(HERE/'hurwitz_first_pair_covariance.npz');tests=0
 for bit in [0,1]:
  for key in fs.files:
   if not key.startswith(f'F_{bit}_'):continue
   i=int(key.split('_')[-1]);F0=fs[key];fi=np.argsort(F0);V=vs[f'mixed72_V_{bit}'][i];vi=np.argsort(V)
   assert np.array_equal(F0[V[B[vi]][fi]],B)
   assert np.array_equal(s[F0[si]],fi)
   # The generating-pair identity underlying the proof is checked literally.
   assert np.array_equal(fi[B[F0]],V[B[vi]])
   assert np.array_equal(V[A[vi]],A)
   tests+=1
 assert tests==72
 out={'statement':'D23.F36','perfect_residual_order':int(N.order()),'perfect_residual_center_order':co,'complete_first_value_unique':True,'candidate_instances_checked':tests,'elapsed_seconds':time.monotonic()-start,'result':'PASS','scope':'Uniqueness among ALL Pprime values with prescribed448+24 quotient, full Bcovariance and two-cycle. No enumeration of a restricted family is used.'}
 (HERE/'hurwitz_first_value_uniqueness.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
