#!/usr/bin/env python3
"""D23.P21: exact first-pair lifts on the four orthogonal detector blocks.

Finite group enumeration plus duality; the final block11 index is the
separately proved D23.H4 condition, not an additional assumption on f.
"""
from pathlib import Path
import numpy as np,json,itertools,time
from sympy.combinatorics import Permutation,PermutationGroup
H=Path(__file__).resolve().parent;R=H.parents[1];F=H.parent/'five_level_six'
d=np.load(H/'hurwitz_cubic216_four_13.npz');bs=np.load(H/'hurwitz_cubic216_four_13_block0.npz');bm=bs['block_map'];sub=np.flatnonzero(np.isin(bm,[7,8,10,11]));idx={int(v):i for i,v in enumerate(sub)}
a,b=[np.array([idx[int(g[v])]for v in sub])for g in d['generators'][:2]];one=np.arange(448);s=a[b[a]];delta=a[b];z=delta[delta[delta]]
assert not np.array_equal(z,one) and np.array_equal(z[z[z]],one)
assert np.array_equal(z[a],a[z]) and np.array_equal(z[b],b[z])
x,y=a[a],b[b]
B448=PermutationGroup([Permutation(g.tolist())for g in[a,b]])
B36=PermutationGroup([Permutation(g.tolist())for g in d['detector_generators']])
assert B448.order()==11664 and B36.order()==3888
G=PermutationGroup([Permutation(g.tolist())for g in[x,y]]);D=G.derived_subgroup();print('orders',G.order(),D.order(),flush=True)
assert G.order()==5832 and D.order()==1944
assert D.contains(Permutation(z.tolist()))
assert np.array_equal(s[x][np.argsort(s)],y) and np.array_equal(s[y][np.argsort(s)],x)
det={int(v):int(w)for v,w in zip(d['detector_subset'],d['detector_map'])};reps=[next(idx[v]for v,w in det.items()if w==j)for j in range(36)]
def down(p):return np.array([det[int(sub[p[v]])]for v in reps])
assert np.array_equal(down(a),d['detector_generators'][0]);assert np.array_equal(down(b),d['detector_generators'][1]);assert np.array_equal(down(z),np.arange(36))
rows=json.loads((R/'records/hurwitz36_gt_stability.json').read_text())['candidates'];targets={tuple(row['label']):np.array(row['f'])for row in rows if row['simultaneous_conjugators']==1}
candidates={key:[]for key in targets}
for p in D.generate_schreier_sims():
 f=np.array(p.array_form);fd=down(f)
 for key,target in targets.items():
  if np.array_equal(fd,target):candidates[key].append(f)
selected={}
for key,cs in candidates.items():
 assert len(cs)==3
 assert {tuple(f)for f in cs}=={tuple(cs[0]),tuple(cs[0][z]),tuple(cs[0][z[z]])}
 keep=[f for f in cs if np.array_equal(s[f][np.argsort(s)],np.argsort(f))]
 print('first',key,'lifts',len(cs),'duality',len(keep),flush=True)
 assert len(keep)==1;selected[key]=keep[0]
 assert np.array_equal(delta[delta[keep[0]]][np.argsort(delta[delta])][delta[keep[0]][np.argsort(delta)]][keep[0]],one)
trans=np.load(F/'hurwitz_block_correlations.npz')['transversals'];base=np.load(F/'hurwitz_block_stabilizer.npz')['base'];lifts=np.load(R/'records/hurwitz_h1_orthogonal_lifts.npz');known=[7,8,10,11]
outputs=[];saved={'subset':sub,'generators':np.array([a,b])}
for bit in[0,1]:
 f=selected[(0,bit)];saved[f'first_f_{bit}']=f
 passes=[]
 for i,j in itertools.product(range(3),repeat=2):
  v=np.full(448,-1,dtype=int)
  for block,k in zip(known,[i,i,i,j]):
   local=lifts[f'case_{bit}_{block}_permutations'][k]
   points=trans[block][base]
   v[[idx[int(w)]for w in points]]=[idx[int(w)]for w in points[local]]
  assert np.all(v>=0) and np.array_equal(v[a],a[v])
  first=np.array_equal(v[b][np.argsort(v)],np.argsort(f)[b[f]])
  if first:passes.append((i,j));saved[f'V_{bit}_{i}_{j}']=v
 print('bit',bit,'Bcovariance passes',passes,flush=True)
 outputs.append({'a3':bit,'B_covariance_passes':passes,'after_R11_constraint':[p for p in passes if p[1]==(0 if bit==0 else 2)]})
np.savez_compressed(H/'hurwitz_first_four_block_lifts.npz',**saved)
out={'statement':'D23.P21','B448_order':int(B448.order()),'B36_order':int(B36.order()),'group_order':int(G.order()),'derived_order':int(D.order()),'central_kernel_order':3,'central_generator':'(AB)^3','kernel_is_contained_in_derived':True,'swap_conjugation_checked':True,'all_six_have_three_lifts_and_one_duality_lift':True,'all_six_selected_lifts_pass_cyclic_norm':True,'cases':outputs,'scope':'Actual-source necessary values from H1 and two-cycle; final unique quadruple also uses H4. No actual mixed lift is asserted.','result':'PASS'}
(H/'hurwitz_first_four_block_lifts.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
