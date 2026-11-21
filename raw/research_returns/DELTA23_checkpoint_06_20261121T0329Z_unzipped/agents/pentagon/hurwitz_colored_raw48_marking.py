#!/usr/bin/env python3
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;start=time.monotonic()
def group(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def join(a,b):return np.array([np.r_[x,len(x)+y]for x,y in zip(a,b)])
raw=np.load(HERE/'hurwitz_colored_raw_mixed_projection.npz')['raw_generators_9'];RH=group(raw);order=int(RH.order());print('raw order',order,'derived',[int(g.order())for g in RH.derived_series()], 'genorders',[int(Permutation(g.tolist()).order())for g in raw],flush=True)
a,b=np.load(HERE/'hurwitz_cubic216_four_13_pair34_component9.npz')['generators'];c=np.argsort(a[b]);pairs=[(a,b),(b,c),(c,a),(b,a),(c,b),(a,c)];rows=[]
for i,pair in enumerate(pairs):
 gs=np.array(pair);G=group(gs);o=int(G.order());J=group(join(gs,raw));jo=int(J.order());r={'source':'original_mixed72','orientation':i,'source_order':o,'joined_order':jo,'kernel_over_source':jo//o};rows.append(r);print(r,flush=True)
# The compact signed Burau quotient retains the harmonic information.
q=np.load(HERE.parent/'five_level_six/hurwitz_block_correlations.npz')['signed_generators'];A,B,C=q;s=A[B[A]]
for name,gs in [('signed_first',np.array([A[A],B[B]])),('signed_mixed',np.array([C[C],s[s]]))]:
 G=group(gs);o=int(G.order());J=group(join(gs,raw));jo=int(J.order());r={'source':name,'source_order':o,'joined_order':jo,'kernel_over_source':jo//o};rows.append(r);print(r,flush=True)
(HERE/'hurwitz_colored_raw48_marking.json').write_text(json.dumps({'raw_order':order,'cases':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
