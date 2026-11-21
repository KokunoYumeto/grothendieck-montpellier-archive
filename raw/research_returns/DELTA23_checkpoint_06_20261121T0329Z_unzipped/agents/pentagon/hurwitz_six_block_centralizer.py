from pathlib import Path
import numpy as np,json,time
from sympy.combinatorics import Permutation,PermutationGroup
H=Path(__file__).resolve().parent;F=H.parent/'five_level_six'
d=np.load(H/'hurwitz_cubic216_four_13.npz');A,B,C=d['generators'];Z=A[B[A]];Z=Z[Z]
stab=np.load(F/'hurwitz_block_stabilizer.npz');base=stab['base'];loc={int(v):i for i,v in enumerate(base)}
t=np.load(F/'hurwitz_block_correlations.npz')['transversals'];group=PermutationGroup([Permutation(p.tolist())for p in stab['stabilizer']]);S=group.derived_subgroup();print('S',S.order(),flush=True)
def local(p,j):return np.array([loc[int(v)]for v in np.argsort(t[j])[p[t[j][base]]]])
def pg(ps):return PermutationGroup([Permutation(p.tolist())for p in ps])
outputs=[];saved={}
for j in[1]:
 a,z,c=[local(p,j)for p in[A[A[A]],Z[Z],A[A[A]]]];print('block',j,'orders',[Permutation(p.tolist()).order()for p in[a,z,c]],flush=True)
 K=S.centralizer(pg([a,z]));print('C_S(A,Z)',j,K.order(),flush=True)
 L=S.centralizer(pg([a,z,c]));print('C_S(A,Z,C)',j,L.order(),flush=True)
 M=pg([c[c],z]);print('mixed',j,M.order(),M.derived_subgroup().order(),flush=True)
 saved[f'a_{j}']=a;saved[f'z_{j}']=z;saved[f'c_{j}']=c;saved[f'centralizer_{j}']=np.array([p.array_form for p in K.generate_schreier_sims()],dtype=np.int16)
 outputs.append({'block':j,'A_order':int(Permutation(a.tolist()).order()),'Z_squared_order':int(Permutation(z.tolist()).order()),'C_order':int(Permutation(c.tolist()).order()),'AZ_centralizer_in_S':int(K.order()),'AZC_centralizer_in_S':int(L.order()),'pair_C_squared_Z_squared_order':int(M.order()),'pair_C_squared_Z_squared_derived':int(M.derived_subgroup().order())})
np.savez_compressed(H/'hurwitz_six_block_centralizer.npz',**saved)
(H/'hurwitz_six_block_centralizer.json').write_text(json.dumps(outputs,indent=2)+'\n')
print(json.dumps(outputs,indent=2))
