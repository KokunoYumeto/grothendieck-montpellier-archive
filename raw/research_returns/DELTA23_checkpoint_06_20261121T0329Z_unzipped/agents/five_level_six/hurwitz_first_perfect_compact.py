#!/usr/bin/env python3
from pathlib import Path
import pickle,json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent

def compact(G,level):
 if len(G.generators)<=6:return G
 target=G.order();arr=np.array([g.array_form for g in G.generators],dtype=np.int16);rng=np.random.default_rng(20261121+level);n=G.degree;gs=[]
 for k in range(20):
  w=np.arange(n)
  for i in rng.integers(0,len(arr),size=int(rng.integers(1,4*len(arr)+1))):w=arr[i][w]
  gs.append(Permutation(w.tolist()))
  if len(gs)<4:continue
  H=PermutationGroup(gs);ho=H.order();print('compact',level,len(gs),'order',ho,'target',target,flush=True)
  if ho==target:return H
 raise RuntimeError('failed to compact')

def main():
 start=time.monotonic();states=pickle.load(open(HERE/'hurwitz_first_groups_state.pkl','rb'));args,st=states[1];G=PermutationGroup(args);G.__dict__.update(st);series=[1567283281920000];counts=[2]
 for level in range(1,12):
  G=compact(G,level);o=G.order();series.append(int(o));counts.append(len(G.generators));print('Pderived level',level,'order',o,'generators',len(G.generators),flush=True)
  with (HERE/f'hurwitz_first_derived_{level}_state.pkl').open('wb') as f:pickle.dump((list(G.args),G.__dict__),f)
  D=G.derived_subgroup();do=D.order()
  if do==o:
   print('PERFECT',o,flush=True);break
  G=D
 else:raise RuntimeError('no stabilization')
 with (HERE/'hurwitz_first_perfect_state.pkl').open('wb') as f:pickle.dump((list(G.args),G.__dict__),f)
 np.savez_compressed(HERE/'hurwitz_first_perfect_residual.npz',generators=np.array([g.array_form for g in G.generators],dtype=np.int16))
 out={'P_derived_series':series,'generator_counts':counts,'perfect_residual_order':int(G.order()),'solvable_P_quotient_order':int(series[0]//G.order()),'solvable_Pderived_quotient_order':int(series[1]//G.order()),'elapsed_seconds':time.monotonic()-start,'compaction':'Each replacement generator is an explicit product in the previous generator list; equality certified by exact order.'}
 (HERE/'hurwitz_first_perfect_residual.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
