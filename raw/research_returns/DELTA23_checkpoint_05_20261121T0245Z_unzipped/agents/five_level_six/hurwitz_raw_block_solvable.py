#!/usr/bin/env python3
"""Raw8064 block stabilizer and its induced abelian-local quotient."""
from pathlib import Path
import numpy as np,json,pickle,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).parent;ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'
def pg(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def pp(g):return Permutation(np.asarray(g).tolist())
def compact(gs):
 current=pg([np.arange(len(gs[0]))]);out=[]
 for g in gs:
  if not current.contains(pp(g)):
   out.append(g);current=pg(out);current.order()
 return current,out

def main():
 start=time.monotonic();raw=np.load(ROOT/'records/hurwitz_product_fixed_cover.npz')['generators'];bd=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz');qgs=bd['generators'];bm=bd['block_map'][np.arange(8064)//6];base=np.flatnonzero(bm==0);assert len(base)==672
 I=np.arange(8064);local=np.full(8064,-1);local[base]=np.arange(672);trans={0:I};todo=[0]
 for i in todo:
  for g,q in zip(raw,qgs):
   j=int(q[i])
   if j not in trans:trans[j]=g[trans[i]];todo.append(j)
 assert len(todo)==12
 alltrans=np.array([trans[i] for i in range(12)]);invs=np.argsort(alltrans,axis=1);h=[];seen=set()
 for i in todo:
  for g,q in zip(raw,qgs):
   j=int(q[i]);w=invs[j][g[alltrans[i]]];a=local[w[base]];assert np.all(a>=0)
   if a.tobytes() not in seen and not np.array_equal(a,np.arange(672)):h.append(a);seen.add(a.tobytes())
 H,short=compact(h);ho=H.order();print('rawH',ho,'gens',len(h),len(short),flush=True)
 D=H.derived_subgroup();do=D.order();DD=D.derived_subgroup();ddo=DD.order();print('rawHderived',do,'second',ddo,flush=True)
 with (HERE/'hurwitz_raw_block_groups_state.pkl').open('wb') as f:pickle.dump([(list(G.args),G.__dict__) for G in [H,D]],f)
 # Explicit left regular cosets of D in H, normal because D=Hprime.
 reps=[np.arange(672)];repinv=[np.arange(672)]
 def identify(a):
  for k,inv in enumerate(repinv):
   if D.contains(pp(inv[a])):return k
  return None
 for a in reps:
  for g in short:
   b=g[a]
   if identify(b) is None:reps.append(b);repinv.append(np.argsort(b))
 assert len(reps)*do==ho;d=len(reps);print('abelianlocalquotient',d,flush=True)
 induced=[];local_trans=[]
 for g,q in zip(raw,qgs):
  out=np.full(12*d,-1);ls=[]
  for i in range(12):
   j=int(q[i]);w=invs[j][g[alltrans[i]]];a=local[w[base]];assert np.all(a>=0);ls.append(a)
   for k,t in enumerate(reps):
    v=identify(a[t]);assert v is not None;out[d*i+k]=d*j+v
  assert len(set(map(int,out)))==12*d;induced.append(out);local_trans.append(ls)
 Q=pg(induced);qo=Q.order();series=[];G=Q
 for level in range(12):
  o=G.order();series.append(int(o));print('rawsolv derived',level,o,flush=True)
  if o==1:break
  nxt=G.derived_subgroup();G,_=compact([np.array(g.array_form) for g in nxt.generators])
 else:raise RuntimeError('Induced quotient not provedsolvable')
 A,B,C=induced;r=A[B];z=r[r[r]];first=pg([A[A],B[B]]);mixed=pg([C[C],z]);fo=first.order();mo=mixed.order();print('rawsolv pairs',fo,mo,flush=True)
 np.savez_compressed(HERE/'hurwitz_raw_block_solvable.npz',base=base,transversals=alltrans,stabilizer_generators=np.array(h),stabilizer_compact=np.array(short),derived_generators=np.array([g.array_form for g in D.generators]),coset_representatives=np.array(reps),generators=np.array(induced),local_transitions=np.array(local_trans))
 out={'raw_degree':8064,'block_degree':672,'stabilizer_order':int(ho),'stabilizer_derived_order':int(do),'stabilizer_second_derived_order':int(ddo),'local_abelian_quotient_order':d,'induced_degree':12*d,'induced_order':int(qo),'induced_derived_series':series,'first_pair_order':int(fo),'mixed_pair_order':int(mo),'elapsed_seconds':time.monotonic()-start,'scope':'Exact finite stabilizer and induced local-abelian quotient; maximality and character retention not inferred from orders.'}
 (HERE/'hurwitz_raw_block_solvable.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
