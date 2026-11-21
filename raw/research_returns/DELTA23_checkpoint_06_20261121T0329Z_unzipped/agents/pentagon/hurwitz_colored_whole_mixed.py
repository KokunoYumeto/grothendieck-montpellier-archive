#!/usr/bin/env python3
"""Full marked mixed-pair/S4 join, without inferring from orbitwise tests."""
from pathlib import Path
import json,pickle,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
kind=sys.argv[1];no=int(sys.argv[2]);start=time.monotonic()
A,B,C=np.load(HERE/f'hurwitz_colored_{kind}_orbit_{no}.npz')['generators']
s=A[B[A]];pair=[C[C],s[s]];n=len(A)
M=PermutationGroup([Permutation(g.tolist())for g in pair])
order=int(M.order());print('full mixed order',order,'elapsed',time.monotonic()-start,flush=True)
with(HERE/f'hurwitz_colored_{kind}_{no}_whole_mixed_state.pkl').open('wb')as f:pickle.dump((M.args,M.__dict__),f)
target=[[1,2,0,3],[1,2,3,0]]
J=PermutationGroup([Permutation(np.r_[g,n+np.array(t)].tolist())for g,t in zip(pair,target)])
joined=int(J.order());assert joined%order==0
out={'kind':kind,'orbit':no,'degree':n,'full_mixed_order':order,'joined_markedS4_order':joined,
     'projection_kernel_order':joined//order,'retains_markedS4':joined==order,
     'elapsed_seconds':time.monotonic()-start,'scope':'Exact full marked group join, not orbitwise quotient inference.'}
(HERE/f'hurwitz_colored_{kind}_{no}_whole_mixed.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
