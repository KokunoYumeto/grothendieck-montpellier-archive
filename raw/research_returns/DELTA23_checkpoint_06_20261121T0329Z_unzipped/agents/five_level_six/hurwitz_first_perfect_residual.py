#!/usr/bin/env python3
"""D23.F35. Exact perfect residual and marked maximal solvable quotient."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def group(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def compact(G,level):
 if len(G.generators)<=6:return G
 target=G.order();arr=np.array([g.array_form for g in G.generators],dtype=np.int16);rng=np.random.default_rng(20261121+level);n=G.degree;gs=[]
 for k in range(24):
  w=np.arange(n)
  for i in rng.integers(0,len(arr),size=int(rng.integers(1,4*len(arr)+1))):w=arr[i][w]
  gs.append(Permutation(w.tolist()))
  if len(gs)<4:continue
  H=PermutationGroup(gs);ho=H.order()
  if ho==target:return H
 raise RuntimeError('No equal-order compact generating list found; no result is asserted.')
def main():
 start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];G=group([A[A],B[B]]);series=[];counts=[];allgens={}
 for level in range(12):
  G=compact(G,level);o=G.order();series.append(int(o));counts.append(len(G.generators));allgens[f'derived_{level}']=np.array([g.array_form for g in G.generators],dtype=np.int16)
  print('Pderived level',level,'order',o,'generators',len(G.generators),flush=True)
  D=G.derived_subgroup();do=D.order()
  if do==o:break
  G=D
 else:raise RuntimeError('No stabilization; no result is asserted.')
 expected=[1567283281920000,261213880320000,16325867520000,4081466880000,50388480000,16796160000]
 assert series==expected
 with (HERE/'hurwitz_first_perfect_state.pkl').open('wb') as f:pickle.dump((list(G.args),G.__dict__),f)
 small=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['generators'];signed=np.load(HERE/'hurwitz_block_correlations.npz')['signed_generators'];qgs=[]
 for a,b in zip(small,signed[:2]):qgs.append(np.concatenate((a[a],448+b[b])))
 # Compare the root's independently constructed literal marked quotient.
 qroot=HERE.parents[1]/'records/hurwitz_first_solvable_joint.npz'
 if qroot.exists():assert np.array_equal(np.array(qgs),np.load(qroot)['generators'])
 Q=group(qgs);qseries=[]
 for level in range(10):
  Q=compact(Q,20+level);qseries.append(int(Q.order()))
  if Q.order()==1:break
  Q=Q.derived_subgroup()
 assert qseries==[93312,15552,972,243,3,1]
 assert series[0]//series[-1]==qseries[0]
 np.savez_compressed(HERE/'hurwitz_first_perfect_residual.npz',**allgens,quotient_generators=np.array(qgs,dtype=np.int16))
 out={'statement':'D23.F35','P_derived_series':series,'generator_counts':counts,'perfect_residual_order':series[-1],'solvable_P_quotient_order':qseries[0],'solvable_Pderived_quotient_order':qseries[1],'marked_quotient_derived_series':qseries,'elapsed_seconds':time.monotonic()-start,'compaction':'Each replacement generator is a literal product of previous generators; equality follows from exact equal orders, not a probabilistic recognition.','scope':'Perfect residual order and maximal solvable quotient; no abstract alternating-group identification and no actual GT lift.','result':'PASS'}
 (HERE/'hurwitz_first_perfect_residual.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
