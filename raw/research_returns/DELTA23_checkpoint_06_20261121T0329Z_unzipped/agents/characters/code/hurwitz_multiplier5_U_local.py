#!/usr/bin/env python3
"""Joint first-detector/mixed-block11 constraints for the multiplier-five U action."""
from pathlib import Path
import json,pickle,itertools
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_multiplier5_global_seeds import HERE,PENT,FIVE,A,B,C,Z,bm,points,loc,local
from hurwitz_multiplier5_detector import power

def run():
 inp=np.load(HERE/'records/hurwitz_multiplier5_detector.npz');a,b=inp['A'],inp['B'];Fs=inp['F']
 x,y=local(C[C],11),local(Z,11);c=local(C,11)
 J=PermutationGroup([Permutation(np.r_[a[a],36+x].tolist()),Permutation(np.r_[b[b],36+y].tolist())])
 D=J.derived_subgroup();print('joint',J.order(),'derived',D.order(),flush=True)
 choices={i:[]for i in range(len(Fs))};lookup={f.tobytes():i for i,f in enumerate(Fs)}
 for elt in D.generate_schreier_sims():
  e=np.array(elt.array_form);first=e[:36].astype(Fs.dtype)
  if first.tobytes()in lookup:choices[lookup[first.tobytes()]].append(e[36:]-36)
 print('fiber counts',[len(choices[i])for i in choices],flush=True)
 g=np.load(HERE/'records/hurwitz_multiplier5_global_probe.npz');subset=g['known_subset']
 mixed=np.load(HERE/'records/hurwitz_multiplier5_U_probe.npz');u=local(mixed['U'],11)
 out=[];saved={'mixed11_x':x,'mixed11_y':y,'mixed11_C':c,'mixed11_U':u}
 for label,wvalues in zip(g['known_labels'],g['known_maps']):
  no,wi,det,mu=map(int,label);W=np.full(1344,-1,dtype=int);W[subset]=wvalues
  ww=loc[11,W[points[11]]]
  rows=[]
  for ri,r in enumerate(choices[no]):
   U=np.argsort(r)[ww]
   cov=np.array_equal(ww[c],r[power(c,5)[np.argsort(r)[ww]]])
   central=np.array_equal(U[u],u[U])
   rows.append({'R11_index':ri,'C_covariance':bool(cov),'U_centralization':bool(central)})
   saved[f'R_{no}_{ri}']=r
  out.append({'detector':no,'lift':wi,'R11_candidates':rows})
  print(out[-1],flush=True)
 np.savez_compressed(HERE/'records/hurwitz_multiplier5_U_local.npz',**saved)
 result={'joint_order':int(J.order()),'joint_derived_order':int(D.order()),'mixed11_fiber_counts':[len(choices[i])for i in choices],
         'cases':out,'passing_C_and_U':sum(any(r['C_covariance']and r['U_centralization']for r in c['R11_candidates'])for c in out),
         'scope':'Actual source f must have joint first36/mixed11 derived value; tests C covariance and U centralization locally. No global R prescribed.'}
 (HERE/'records/hurwitz_multiplier5_U_local.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS_COUNT',result['passing_C_and_U'],flush=True)
if __name__=='__main__':run()
