from pathlib import Path
import numpy as np,json,pickle,time
from sympy.combinatorics import Permutation,PermutationGroup
H=Path(__file__).resolve().parent;R=H.parents[1]
raw=np.load(R/'records/hurwitz_product_fixed_cover.npz');base=np.load(H/'hurwitz_cubic216_four_13.npz')
def args(gens):
 a,b,c=gens;s=a[b[a]];t=c[b[c]];return s[s],t[t]
def group(gens):return PermutationGroup([Permutation(p.tolist())for p in gens])
saved={};out={}
for label,data in [('base',base),('raw',raw)]:
 gs=args(data['generators']);G=group(gs);start=time.monotonic();n=G.order();print(label,'order',n,'seconds',time.monotonic()-start,flush=True)
 D=G.derived_subgroup();dn=D.order();print(label,'derived',dn,'seconds',time.monotonic()-start,flush=True)
 with(H/f'hurwitz_pair45_{label}_state.pkl').open('wb')as f:pickle.dump([(list(g.args),g.__dict__)for g in[G,D]],f)
 out[label]={'order':int(n),'derived_order':int(dn),'elapsed_seconds':time.monotonic()-start}
 values=np.load(H/'hurwitz_required_f45.npz');hs=values[f'{label}_H'];membership=[]
 for idx,h in zip(values['candidate_indices'],hs):membership.append({'candidate':int(idx),'in_derived':bool(D.contains(Permutation(h.tolist())))})
 out[label]['recorded_witness_membership']=membership
 saved[f'{label}_generators']=gs
 (H/'hurwitz_raw_pair45.json').write_text(json.dumps(out,indent=2)+'\n')
print('kernel orders',out['raw']['order']//out['base']['order'],out['raw']['derived_order']//out['base']['derived_order'],flush=True)
out['projection_kernel_order']=out['raw']['order']//out['base']['order'];out['derived_projection_kernel_order']=out['raw']['derived_order']//out['base']['derived_order']
(H/'hurwitz_raw_pair45.json').write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(H/'hurwitz_raw_pair45.npz',**saved)
print(out,flush=True)
