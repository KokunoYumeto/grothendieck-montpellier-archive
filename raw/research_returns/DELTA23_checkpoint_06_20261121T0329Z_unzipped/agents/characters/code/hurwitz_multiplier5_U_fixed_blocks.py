#!/usr/bin/env python3
"""Necessary U-centralization and mixed C covariance on fixed blocks9,11."""
from pathlib import Path
import pickle,json
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_multiplier5_global_seeds import HERE,PENT,FIVE,A,B,C,Z,bm,points,loc,local
from hurwitz_multiplier5_detector import power

def run():
 with (FIVE/'hurwitz_full_mixed_groups_state.pkl').open('rb')as f:states=pickle.load(f)
 args,st=states[1];MD=PermutationGroup(args);MD.__dict__.update(st)
 gs=[]
 for g in MD.generators:
  p=np.array(g.array_form);gs.append(np.r_[local(p,9),112+local(p,11)])
 G=PermutationGroup([Permutation(p.tolist())for p in gs]);print('joint9/11',G.order(),flush=True)
 elements=np.array([p.array_form for p in G.generate_schreier_sims()]);e9=elements[:,:112];e11=elements[:,112:]-112
 print('local9',len({p.tobytes()for p in e9}),'local11',len({p.tobytes()for p in e11}),flush=True)
 gp=np.load(HERE/'records/hurwitz_multiplier5_global_probe.npz');sub0=gp['partial_subset_0'];p0=gp['partial_maps_0'];labels=gp['partial_labels_0']
 mixed=np.load(HERE/'records/hurwitz_multiplier5_U_probe.npz');u9=local(mixed['U'],9);c9=local(C,9)
 lf=np.load(HERE/'records/hurwitz_multiplier5_U_local.npz');meta=json.loads((HERE/'records/hurwitz_multiplier5_U_local.json').read_text())
 rows=[];saved={}
 for case in meta['cases']:
  if not any(r['C_covariance']for r in case['R11_candidates']):continue
  no,wi=case['detector'],case['lift'];rr11=lf[f'R_{no}_0']
  eligible=np.flatnonzero(np.all(e11==rr11,axis=1));goodseeds=[];counts=[]
  for ix,(target,localix)in enumerate(labels):
   if target!=0:continue
   W=np.full(1344,-1,dtype=int);W[sub0]=p0[ix];w9=loc[9,W[points[9]]]
   tc=w9[power(c9,-1)[np.argsort(w9)]] # overwritten below with literal C target
   tc=w9[c9[np.argsort(w9)]]
   tu=w9[u9[np.argsort(w9)]]
   allowed=[]
   for k in eligible:
    r=e9[k];ri=np.argsort(r)
    if np.array_equal(r[power(c9,5)[ri]],tc)and np.array_equal(r[u9[ri]],tu):allowed.append(int(k))
   if allowed:goodseeds.append(ix)
   counts.append(len(allowed));saved[f'allowed_{no}_{wi}_{ix}']=np.array(allowed)
  row={'detector':no,'four_block_lift':wi,'joint_R11_fiber':len(eligible),'block0_seed_count':36,'passing_block0_seeds':len(goodseeds),'witness_counts':counts}
  rows.append(row);print(row,flush=True)
 saved['joint9_11_elements']=elements;saved['joint9_11_generators']=np.array(gs)
 np.savez_compressed(HERE/'records/hurwitz_multiplier5_U_fixed_blocks.npz',**saved)
 out={'joint9_11_order':int(G.order()),'cases':rows,'scope':'Necessary projection of full Mprime to blocks9/11, with exact first36-determined R11. Tests simultaneous C covariance and Ustar conjugation; other blocks and common first36/R9 word constraints remain separate.'}
 (HERE/'records/hurwitz_multiplier5_U_fixed_blocks.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
