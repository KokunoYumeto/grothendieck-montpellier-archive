#!/usr/bin/env python3
"""Joint first-solvable and FULL mixed cyclic/Nielsen core commonword test."""
from pathlib import Path
import numpy as np,json,pickle,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())
def main():
 start=time.monotonic();args,st=pickle.load(open(CHAR/'records/hurwitz_full_mixed_s3_compact_group_state.pkl','rb'));core=PermutationGroup(args);core.__dict__.update(st);assert core.degree==1476
 cgens=np.array([g.array_form for g in core.generators]);q=np.load(ROOT/'records/hurwitz_first_solvable_joint.npz')['generators'];gens=np.array([np.r_[a,472+b] for a,b in zip(q,cgens)])
 G=PermutationGroup([pp(g) for g in gens]);assert all(g.order()==12 for g in G.generators)
 print('constructing jointdegree',G.degree,'corebase',len(core.base),flush=True)
 G._schreier_sims(base=[472+i for i in core.base]);go=int(G.order());print('jointorder',go,'elapsed',time.monotonic()-start,flush=True)
 with (HERE/'hurwitz_first_full_cyclic_core_state.pkl').open('wb') as f:pickle.dump((list(G.args),G.__dict__),f)
 np.savez_compressed(HERE/'hurwitz_first_full_cyclic_core_group.npz',generators=gens,strong_generators=np.array([g.array_form for g in G.strong_gens],dtype=np.int16),base=np.array(G.base))
 # Recover only the original exponent vector of each SLP, never expand its word.
 memo={G.generators[0]:(1,0),G.generators[1]:(0,1),G.generators[0]**-1:(11,0),G.generators[1]**-1:(0,11)}
 def exp(p):
  if p.is_identity:return (0,0)
  if p in memo:return memo[p]
  if p**-1 in memo:return tuple((-v)%12 for v in memo[p**-1])
  if p in G._strong_gens_slp:fac=G._strong_gens_slp[p]
  elif p**-1 in G._strong_gens_slp:
   r0=tuple((-v)%12 for v in exp(p**-1));memo[p]=r0;return r0
  else:fac=G.generator_product(p,original=False)
  sums=[0,0]
  for f in fac:
   a,b=exp(f);sums[0]+=a;sums[1]+=b
  r0=(sums[0]%12,sums[1]%12);memo[p]=r0;return r0
 data=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz');f=np.load(PENT/'hurwitz_first_four_block_lifts.npz')['first_f_1'];ft=np.r_[f,448+np.arange(24)];rows=[];kept=[]
 for label,target in zip(data['passing_labels'],data['passing_tuples']):
  assert core.contains(pp(target));p=pp(np.r_[ft,472+target]);yes=bool(G.contains(p));ee=exp(p) if yes else None;derived=bool(yes and ee==(0,0))
  # A zero SLP exponent vector modulo12 certifies a commutator value because both generators have order12.
  row={'candidate':int(label[0]),'R_fiber_index':int(label[1]),'joint_membership':yes,'SLP_exponents_mod12':ee,'certified_derived_membership':derived};rows.append(row)
  if derived:kept.append(label.tolist())
  print(row,flush=True)
 out={'joint_order':go,'joint_degree':G.degree,'core_order':int(core.order()),'generator_orders':[12,12],'tested_pairs':len(rows),'surviving_pairs':len(kept),'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Exact fullmixedcycliccore+firstsolvable commutatorword test. Eachpassingderivedmembership has an originalgeneratorSLP withboth exponents0mod12; no actualGTlift asserted.','result':'PASS'}
 (HERE/'hurwitz_first_full_cyclic_core.json').write_text(json.dumps(out,indent=2)+'\n');np.savez_compressed(HERE/'hurwitz_first_full_cyclic_core.npz',passing_labels=np.array(kept,dtype=int))
 print(json.dumps({k:v for k,v in out.items() if k!='cases'},indent=2),flush=True)
if __name__=='__main__':main()
