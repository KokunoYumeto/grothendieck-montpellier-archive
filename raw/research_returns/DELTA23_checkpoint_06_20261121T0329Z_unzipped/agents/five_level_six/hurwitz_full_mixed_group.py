#!/usr/bin/env python3
from pathlib import Path
import numpy as np,json,pickle,time
from sympy import factorint
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def perm(a):return Permutation(np.asarray(a).tolist())
def main():
 start=time.monotonic();A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];r=A[B];z=r[r[r]];x=C[C]
 M=PermutationGroup([perm(x),perm(z)]);mo=M.order();print('fullmixedorder',mo,'factorization',factorint(mo),flush=True)
 MD=M.derived_subgroup();md=MD.order();print('fullmixedderivedorder',md,'factorization',factorint(md),flush=True)
 with (HERE/'hurwitz_full_mixed_groups_state.pkl').open('wb') as f:pickle.dump([(list(G.args),G.__dict__) for G in [M,MD]],f)
 ca=np.load(PENT/'hurwitz_global_conjugators.npz');first=json.load(open(HERE/'hurwitz_global_firstpair.json'))['survivors'];rows=[];surv={}
 for bit in [0,1]:
  vs=ca[f'mixed72_V_{bit}'];keep=[]
  for j in first[str(bit)]:
   V=vs[j];assert np.array_equal(V[z],z[V]);xx=V[x[np.argsort(V)]];yes=M.contains(perm(xx))
   if yes:keep.append(j)
   rows.append({'a3':bit,'candidate':j,'normalizes_fullmixed':bool(yes)})
  surv[str(bit)]=keep;print('bit',bit,'fullmixednormalizer',len(keep),flush=True)
 out={'mixed_order':int(mo),'mixed_derived_order':int(md),'mixed_abelianization_order':int(mo//md),'rows':rows,'survivors':surv,'elapsed_seconds':time.monotonic()-start}
 (HERE/'hurwitz_full_mixed_group.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
