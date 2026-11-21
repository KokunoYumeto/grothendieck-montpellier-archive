#!/usr/bin/env python3
"""Actual first-B3 subgroup tests for the complete globalV candidate list."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy import factorint
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def run():
 start=time.monotonic()
 raw=np.load(PENT/'hurwitz_cubic216_four_13.npz');A,B,C=raw['generators']
 gs=[Permutation(g.tolist()) for g in [A,B]]
 G=PermutationGroup(gs);go=G.order()
 print('G3 order',go,'factorization',factorint(go),flush=True)
 with (HERE/'hurwitz_first_G3.pkl').open('wb') as f:pickle.dump(G,f)
 cand=np.load(PENT/'hurwitz_global_conjugators.npz')
 rows=[];surv={}
 for bit in [0,1]:
  vs=cand[f'mixed72_V_{bit}'];labels=cand[f'mixed72_labels_{bit}'];keep=[]
  for i,V in enumerate(vs):
   assert np.array_equal(V[A],A[V])
   Bi=V[B[np.argsort(V)]]
   yes=G.contains(Permutation(Bi.tolist()))
   rows.append({'a3':bit,'candidate':i,'labels':labels[i].tolist(),'normalizes_first_B3':bool(yes)})
   if yes:keep.append(i)
  surv[bit]=keep
  print('a3',bit,'firstB3normalizer survivors',len(keep),'of',len(vs),flush=True)
 out={'G3_order':int(go),'G3_order_factorization':{str(k):int(v) for k,v in factorint(go).items()},
      'rows':rows,'survivors':{str(k):v for k,v in surv.items()},
      'elapsed_seconds':time.monotonic()-start,
      'scope':'Necessary subgroup-normalization test; transporter and commonword constraints are separate.'}
 (HERE/'hurwitz_global_firstpair.json').write_text(json.dumps(out,indent=2)+'\n')
 if not any(surv.values()):return
 P=PermutationGroup([Permutation(A[A].tolist()),Permutation(B[B].tolist())]);po=P.order()
 print('pureP order',po,'factorization',factorint(po),flush=True)
 D=P.derived_subgroup();do=D.order();print('purederived order',do,flush=True)
 with (HERE/'hurwitz_first_P.pkl').open('wb') as f:pickle.dump(P,f)
 with (HERE/'hurwitz_first_Pderived.pkl').open('wb') as f:pickle.dump(D,f)
 out.update({'pure_order':int(po),'pure_derived_order':int(do),'elapsed_seconds':time.monotonic()-start})
 (HERE/'hurwitz_global_firstpair.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
