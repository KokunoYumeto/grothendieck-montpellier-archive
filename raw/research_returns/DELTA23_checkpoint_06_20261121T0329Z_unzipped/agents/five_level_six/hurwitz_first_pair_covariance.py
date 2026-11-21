#!/usr/bin/env python3
"""D23.F34. Complete first-B3 subgroup and explicit associator-value checks."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def pp(g):return Permutation(np.asarray(g).tolist())
def main():
 start=time.monotonic()
 A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];n=len(A);I=np.arange(n)
 r=A[B];s=r[A];z=r[r[r]]
 assert np.array_equal(s[s],z)
 G=pg([A,B]);P=pg([A[A],B[B]]);PD=P.derived_subgroup()
 orders=[int(g.order()) for g in [G,P,PD]]
 assert orders==[3134566563840000,1567283281920000,261213880320000]
 assert orders[1]//orders[2]==6
 power=I.copy();b2order=None
 for k in range(1,7):
  power=B[B[power]]
  if PD.contains(pp(power)):
   b2order=k;break
 assert b2order==6
 print('first group, pure, derived orders',orders,flush=True)
 ca=np.load(PENT/'hurwitz_global_conjugators.npz');known=np.load(PENT/'hurwitz_first_four_block_lifts.npz');sub=known['subset'];back=np.full(n,-1);back[sub]=np.arange(len(sub))
 rows=[];surv={};saved={'subset448':sub}
 for bit in [0,1]:
  vs=ca[f'mixed72_V_{bit}'];labels=ca[f'mixed72_labels_{bit}'];assert vs.shape==(72,n)
  keep=[]
  for j,V in enumerate(vs):
   vi=np.argsort(V)
   assert np.array_equal(V[A],A[V]) and np.array_equal(V[z],z[V])
   Bnew=V[B[vi]];yes=G.contains(pp(Bnew))
   row={'a3':bit,'candidate':j,'labels':labels[j].tolist(),'normalizes_first_B3':bool(yes)}
   if yes:
    keep.append(j);F=r[V[np.argsort(r)[vi]]]
    # F V centralizes B; every test uses literal full1344 permutations.
    assert np.array_equal(F[Bnew[np.argsort(F)]],B)
    assert PD.contains(pp(F))
    assert np.array_equal(back[F[sub]],known[f'first_f_{bit}'])
    assert np.array_equal(s[F[np.argsort(s)]],np.argsort(F))
    r2=r[r]
    assert np.array_equal(r2[F[np.argsort(r2)]][r[F[np.argsort(r)]][F]],I)
    row.update({'F_in_Pderived':True,'exact_P21_restriction':True,'two_cycle':True,'three_cycle':True,'B_covariance':True})
    saved[f'F_{bit}_{j}']=F
   rows.append(row)
  assert len(keep)==36;surv[str(bit)]=keep
  print('a3',bit,'survivors',keep,flush=True)
 out={'statement':'D23.F34','first_B3_order':orders[0],'pure_pair_order':orders[1],'pure_derived_order':orders[2],'B2_order_in_Pabelianization':b2order,'rows':rows,'survivors':surv,'elapsed_seconds':time.monotonic()-start,'scope':'Necessary finite actual-source tests only. All retained candidates admit explicit first-pair values; no common-word compatibility with mixed values or actual GT lift is asserted.','result':'PASS'}
 (HERE/'hurwitz_first_pair_covariance.json').write_text(json.dumps(out,indent=2)+'\n')
 np.savez_compressed(HERE/'hurwitz_first_pair_covariance.npz',**saved)
if __name__=='__main__':main()
