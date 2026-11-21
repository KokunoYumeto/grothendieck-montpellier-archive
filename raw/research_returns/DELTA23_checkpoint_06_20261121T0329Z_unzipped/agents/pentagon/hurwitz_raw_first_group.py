from pathlib import Path
import numpy as np,json,time,pickle
from sympy.combinatorics import Permutation,PermutationGroup
H=Path(__file__).resolve().parent;R=H.parents[1]
d=np.load(R/'records/hurwitz_product_fixed_cover.npz');A,B=d['generators'][:2]
seen=set();orbs=[]
for i in range(8064):
 if i in seen:continue
 todo=[i];seen.add(i)
 for v in todo:
  for p in[A,B]:
   w=int(p[v])
   if w not in seen:seen.add(w);todo.append(w)
 orbs.append(todo)
print('rawB3 orbit degrees',sorted(map(len,orbs)),flush=True)
start=time.monotonic();G=PermutationGroup([Permutation(A.tolist()),Permutation(B.tolist())]);n=G.order();print('rawB3 order',n,'elapsed',time.monotonic()-start,flush=True)
with(H/'hurwitz_raw_first_group.pkl').open('wb')as f:pickle.dump({'group':G,'cache':G.__dict__},f)
out={'raw_B3_order':int(n),'raw_B3_orbit_degrees':sorted(map(len,orbs)),'elapsed_seconds':time.monotonic()-start}
(H/'hurwitz_raw_first_group.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
