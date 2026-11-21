#!/usr/bin/env python3
"""Exact Schreier generators on a 112-point block of the new Hurwitz action."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).parent
PENT=HERE.parent/'pentagon'
def compose(a,b):return a[b]
def inverse(a):return np.argsort(a)
def group(gs):return PermutationGroup([Permutation(g.tolist()) for g in gs])
def compact(gs):
 out=[];current=PermutationGroup([Permutation(list(range(len(gs[0]))))])
 for g in gs:
  p=Permutation(g.tolist())
  if not current.contains(p):
   out.append(g);current=group(out);current.schreier_sims()
 return current,out
def run():
 start=time.monotonic()
 raw=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 bd=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')
 small,block=bd['generators'],bd['block_map']
 n=len(raw[0]);I=np.arange(n);J=np.arange(len(small[0]))
 base=np.flatnonzero(block==0);loc={int(v):i for i,v in enumerate(base)}
 assert len(base)==112
 assert all(np.array_equal(block[g],q[block]) for g,q in zip(raw,small))
 def restrict(g):
  assert set(map(int,g[base]))==set(loc)
  return np.array([loc[int(v)] for v in g[base]],dtype=np.int16)
 # A Schreier transversal for the twelve blocks.
 trans={0:I};word={0:[]};todo=[0]
 for b in todo:
  for j,(g,q) in enumerate(zip(raw,small)):
   c=int(q[b])
   if c not in trans:
    trans[c]=g[trans[b]];word[c]=[j+1]+word[b];todo.append(c)
 assert len(todo)==12
 hfull=[];h=[];hwords=[];seen=set()
 for b in todo:
  for j,(g,q) in enumerate(zip(raw,small)):
   c=int(q[b]);z=inverse(trans[c])[g[trans[b]]];p=restrict(z)
   if p.tobytes() not in seen and not np.array_equal(p,np.arange(112)):
    seen.add(p.tobytes());h.append(p);hfull.append(z)
    hwords.append(list(-v for v in word[c][::-1])+[j+1]+word[b])
 H,hshort=compact(h);ho=H.order();print('block stabilizer order',ho,'generators',len(hshort),flush=True)
 # A Schreier transversal for the kernel of the action on twelve blocks.
 qt=[J];lifts=[I];qw=[[]];index={J.tobytes():0}
 for p,t,w in zip(qt,lifts,qw):
  for j,(g,q) in enumerate(zip(raw,small)):
   p1=q[p];key=p1.tobytes()
   if key not in index:
    index[key]=len(qt);qt.append(p1);lifts.append(g[t]);qw.append([j+1]+w)
 assert len(qt)==216
 k=[];kfull=[];kwords=[];seen=set()
 for p,t,w in zip(qt,lifts,qw):
  for j,(g,q) in enumerate(zip(raw,small)):
   v=index[q[p].tobytes()];z=inverse(lifts[v])[g[t]]
   assert np.array_equal(block[z],block)
   rz=restrict(z)
   # Do not deduplicate by one block restriction: two such equal
   # restrictions can have different actions on the other eleven blocks.
   if z.tobytes() not in seen and not np.array_equal(z,I):
    seen.add(z.tobytes());k.append(rz);kfull.append(z)
    kwords.append(list(-a for a in qw[v][::-1])+[j+1]+w)
 K,kshort=compact(k);ko=K.order();print('block kernel projection order',ko,'generators',len(kshort),flush=True)
 np.savez_compressed(HERE/'hurwitz_block_stabilizer.npz',base=base,
                     stabilizer=np.array(h),stabilizer_full=np.array(hfull),
                     kernel=np.array(k),kernel_full=np.array(kfull),
                     stabilizer_compact=np.array(hshort),kernel_compact=np.array(kshort))
 print('point-stabilizer orbits',sorted(map(len,H.stabilizer(0).orbits())),flush=True)
 ds=[]
 cur=H
 while True:
  o=cur.order();ds.append(int(o));nxt=cur.derived_subgroup()
  print('derived step',o,nxt.order(),flush=True)
  if nxt.order()==o:break
  cur,_=compact([np.array(p.array_form,dtype=np.int16) for p in nxt.generators])
 print('stabilizer derived orders',ds,flush=True)
 assert all(H.contains(p) for p in K.generators) and ho==ko
 ks=ds.copy()
 print('kernel derived orders',ks,flush=True)
 out={'degree':1344,'block_count':12,'block_size':112,
      'block_quotient_order':216,'stabilizer_schreier_generators':len(h),
      'stabilizer_order':int(ho),'stabilizer_derived_orders':ds,
      'kernel_schreier_generators':len(k),'kernel_projection_order':int(ko),
      'kernel_derived_orders':ks,'stabilizer_transitive':H.is_transitive(),
      'kernel_transitive':K.is_transitive(),'stabilizer_words':hwords,
      'point_stabilizer_orbit_sizes':sorted(map(len,H.stabilizer(0).orbits())),
      'kernel_words':kwords,'elapsed_seconds':time.monotonic()-start,
      'scope':'Exact Schreier image computations; no abstract simple-group identification yet.'}
 (HERE/'hurwitz_block_stabilizer.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({key:val for key,val in out.items() if not key.endswith('_words')},indent=2),flush=True)
if __name__=='__main__':run()
