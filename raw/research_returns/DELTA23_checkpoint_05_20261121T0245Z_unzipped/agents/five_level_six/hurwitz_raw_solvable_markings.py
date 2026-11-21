#!/usr/bin/env python3
from pathlib import Path
import numpy as np,json,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def join(gs,ts):
 n=len(gs[0]);return pg([np.r_[g,n+t] for g,t in zip(gs,ts)])
def main():
 start=time.monotonic();g=np.load(HERE/'hurwitz_raw_block_solvable.npz')['generators'];old=np.load(HERE/'hurwitz_block_correlations.npz')['signed_generators'];G=pg(g);O=pg(old)
 go=int(G.order());oo=int(O.order());jo=int(join(g,old).order());gd=int(G.derived_subgroup().order());od=int(O.derived_subgroup().order());print('globalorders',go,oo,jo,gd,od,flush=True);assert go==jo==331776 and oo==110592 and gd==55296 and od==18432
 A,B,C=g;r=A[B];z=r[r[r]];a,b,c=old;rr=a[b];zz=rr[rr[rr]];first=[A[A],B[B]];mixed=[C[C],z];oldfirst=[a[a],b[b]];oldmixed=[c[c],zz]
 target=json.load(open(PENT/'cubic_detector_216.json'))
 def aff(a):return np.array([3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)])
 cubic=[aff(target[k]) for k in ['x','y']];harmonic=[np.array([1,2,0,3]),np.array([1,2,3,0])]
 records={'first_order':int(pg(first).order()),'first_join_signed':int(join(first,oldfirst).order()),'first_join_cubic216':int(join(first,cubic).order()),'mixed_order':int(pg(mixed).order()),'mixed_join_signed':int(join(mixed,oldmixed).order()),'mixed_join_harmonicS4':int(join(mixed,harmonic).order())}
 assert records=={'first_order':192,'first_join_signed':192,'first_join_cubic216':3456,'mixed_order':144,'mixed_join_signed':144,'mixed_join_harmonicS4':144}
 # All five literal pentagon pair images and marked old joins.
 X=[A[A],B[B],C[C],z,(B[C])[(B[C])[(B[C])]]]
 Y=[a[a],b[b],c[c],zz,(b[c])[(b[c])[(b[c])]]]
 pairs=[]
 for i,j in [(0,1),(1,2),(2,3),(3,4),(4,0)]:
  h=[X[i],X[j]];o=[Y[i],Y[j]]
  pairs.append({'pair':str(i+1)+str(j+1),'raw_order':int(pg(h).order()),'old_order':int(pg(o).order()),'joint_order':int(join(h,o).order())})
 T=G
 for _ in range(4):T=T.derived_subgroup()
 assert T.order()==768
 kernel=None
 for h in T.generate_schreier_sims():
  k=h**256
  if not k.is_identity:kernel=np.array(k.array_form);break
 assert kernel is not None and pg([kernel]).order()==3
 central=all(np.array_equal(kernel[a],a[kernel]) for a in g)
 d=A[B[C]];full=d[d[d[d]]];od0=a[b[c]];ofull=od0[od0[od0[od0]]]
 assert np.array_equal(ofull,np.arange(24))
 assert np.array_equal(full,kernel) or np.array_equal(full,kernel[kernel])
 out={'global_order':go,'old_signed_order':oo,'joint_order':jo,'global_derived_order':gd,'old_signed_derived_order':od,'projection_kernel_order':3,'kernel_is_central':central,'full_twist_generates_kernel':True,**records,'five_pair_orders':pairs,'elapsed_seconds':time.monotonic()-start,'result':'PASS','scope':'Exact marked projection and individual pair quotients; no global commutator-isomorphism assertion.'}
 (HERE/'hurwitz_raw_solvable_markings.json').write_text(json.dumps(out,indent=2)+'\n')
 np.savez_compressed(HERE/'hurwitz_raw_solvable_markings.npz',central_kernel_generator=kernel)
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
