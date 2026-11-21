#!/usr/bin/env python3
"""Exhaust exact raw mixed34 lift fibers and their local C² covariance."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_marked_raw_lift import MarkedRawLift
HERE=Path(__file__).resolve().parent;start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];x=C[C];N=len(x);I=np.arange(N)
lifts=np.load(HERE/'hurwitz_colored_last_gentle.npz');liftmeta=json.loads((HERE/'hurwitz_colored_last_gentle.json').read_text());V=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')['base_V']
Ws={aid:6*V[I//6]+(I%6+lifts[f'potential_{aid}'][I//6])%6 for aid in liftmeta['passing_assemblies']}
targets={aid:W[x[np.argsort(W)]]for aid,W in Ws.items()}
parts=np.load(HERE/'hurwitz_colored_raw_mixed_projection.npz');states=pickle.loads((HERE/'hurwitz_colored_raw_mixed_projection_state.pkl').read_bytes())
baseparts=np.load(HERE/'hurwitz_colored_inverse_12_mixed.npz');inventory=json.loads((HERE/'hurwitz_colored_raw_mixed_projection.json').read_text())['cases']
sph=np.load(HERE/'hurwitz_spherical_five_orbit.npz');co=np.load(HERE/'hurwitz_order5_cochains.npz');j=next(i for i,label in enumerate(co['labels'])if np.array_equal(label,[1,0]));rho=sph['rho'];F=co['f12'][j];Rfull=np.argsort(rho)[F[rho]];R=Rfull[1344:]-1344
rows=[];saved={};kernelsaved={}
for item in sorted(inventory,key=lambda r:(r['raw_order'],r['raw_preimage_degree'])):
 k=item['component'];sub=parts[f'raw_subset_{k}'];gs=parts[f'raw_generators_{k}'];n=len(sub);basub=baseparts[f'orbit_{k}'];bgens=baseparts[f'pair_{k}'];d=len(basub)
 loc=np.full(N,-1,dtype=int);loc[sub]=np.arange(n)
 baseloc=np.full(5376,-1,dtype=int);baseloc[basub]=np.arange(d);rb=baseloc[R[basub]];assert min(rb)>=0
 G=PermutationGroup(states[k][0]);G.__dict__.update(states[k][1]);BG=PermutationGroup([Permutation(g.tolist())for g in bgens]);assert BG.order()==item['base_order']
 row={'component':k,'kernel_order':item['kernel_order'],'cases':{}};localtargets={}
 for aid in Ws:
  t=loc[targets[aid][sub]];preserves=min(t)>=0
  member=preserves and G.contains(Permutation(t.tolist()))
  row['cases'][str(aid)]={'target_preserves_preimage':bool(preserves),'new_x_in_raw_group':bool(member)}
  if member:localtargets[aid]=t
 if not localtargets:
  rows.append(row);print(row,flush=True);continue
 lift=MarkedRawLift((BG.args,BG.__dict__),gs);r0=lift.lift(rb)
 # Add the literal base action and stabilize a base of that action.
 jgens=np.array([np.r_[g,n+b]for g,b in zip(gs,bgens)])
 J=PermutationGroup([Permutation(g.tolist())for g in jgens]);points=[n+v for v in BG.base]
 jb,jsg=J.schreier_sims_incremental(base=points)
 kg=[np.array(g.array_form[:n])for g in jsg if all(g(v)==v for v in points)]
 if not kg:kg=[np.arange(n)]
 K=PermutationGroup([Permutation(g.tolist())for g in kg]);assert K.order()==item['kernel_order']
 kk=np.array([g.array_form for g in K.generate_schreier_sims()]);assert all(np.array_equal(g[::6]//6,np.arange(d))for g in kk)
 kernelsaved[k]=(K.args,K.__dict__);saved[f'kernel_{k}']=kk;saved[f'section_R_{k}']=r0
 for aid,t in localtargets.items():
  good=[]
  for h in kk:
   r=h[r0]
   if np.array_equal(r[gs[0][np.argsort(r)]],t):good.append(r)
  row['cases'][str(aid)]['allowed_R_lifts']=len(good)
  saved[f'R_{aid}_{k}']=np.array(good,dtype=int).reshape(-1,n)
 rows.append(row);print(row,flush=True)
 (HERE/'hurwitz_colored_raw_mixed_local.json').write_text(json.dumps({'status':'IN_PROGRESS','cases':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
np.savez_compressed(HERE/'hurwitz_colored_raw_mixed_local.npz',**saved)
(HERE/'hurwitz_colored_raw_mixed_kernels_state.pkl').write_bytes(pickle.dumps(kernelsaved))
passing=[aid for aid in Ws if all(r['cases'][str(aid)].get('allowed_R_lifts',0)>0 for r in rows)]
out={'status':'PASS','passing_assemblies':passing,'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Complete local raw R lift fibers over the known baseR and C² covariance. Derived membership, global commonword and full C covariance remain additional.'}
(HERE/'hurwitz_colored_raw_mixed_local.json').write_text(json.dumps(out,indent=2)+'\n');print('passing',passing,flush=True)
