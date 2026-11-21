#!/usr/bin/env python3
"""Complete missing mixed-pair component orders and derived series."""
from pathlib import Path
import json,time
import numpy as np
from sympy import factorint
from hurwitz_block_stabilizer import group,compact

HERE=Path(__file__).parent;PENT=HERE.parent/'pentagon'
def run():
 start=time.monotonic();rows=[]
 A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators']
 x1=A[A];x3=C[C];s=A[B[A]];x4=s[s];t=C[B[C]];x5=t[t]
 reversal=A[B[C[A[B[A]]]]]
 rev_i=np.argsort(reversal)
 assert np.array_equal(reversal[x3[rev_i]],x1)
 assert np.array_equal(reversal[x4[rev_i]],x5)
 for pair,indices in [('34',range(16)),('45',range(30))]:
  full=[x3,x4] if pair=='34' else [x4,x5]
  seen=set();orbits=[]
  for v in range(1344):
   if v in seen:continue
   todo=[v];seen.add(v)
   for w in todo:
    for p in full:
     u=int(p[w])
     if u not in seen:seen.add(u);todo.append(u)
   orbits.append(todo)
  orbits=sorted(orbits,key=len)
  assert len(orbits)==len(indices) and sum(map(len,orbits))==1344
  for i in indices:
   d=np.load(PENT/f'hurwitz_cubic216_four_13_pair{pair}_component{i}.npz')
   orbit=orbits[i];loc={v:j for j,v in enumerate(orbit)}
   rebuilt=np.array([[loc[int(p[v])] for v in orbit] for p in full])
   gs=d['generators'];assert np.array_equal(gs,rebuilt)
   G=group(gs);order=G.order()
   row={'pair':pair,'component':i,'degree':len(gs[0]),'order':int(order),
        'order_factorization':{str(k):int(v) for k,v in factorint(order).items()},'derived_orders':[int(order)]}
   cur=G
   while cur.order()!=1:
    D=cur.derived_subgroup();n=D.order();row['derived_orders'].append(int(n))
    if n==cur.order():break
    cur,_=compact([np.array(p.array_form,dtype=np.int16) for p in D.generators])
   rows.append(row)
   print(pair,i,len(gs[0]),row['derived_orders'],flush=True)
   out={'rows':rows,'full_component_reconstruction':'PASS',
        'reversal_to_pair51':'PASS','elapsed_seconds':time.monotonic()-start}
   (HERE/'hurwitz_mixed_large_components.json').write_text(json.dumps(out,indent=2)+'\n')
 assert all(r['derived_orders'][-1]==1 and len(r['derived_orders'])<=7 for r in rows)
 print(json.dumps({'component_count':len(rows),'maximum_derived_length':max(len(r['derived_orders'])-1 for r in rows),
                   'full_component_reconstruction':'PASS','reversal_to_pair51':'PASS',
                   'elapsed_seconds':time.monotonic()-start},indent=2))
if __name__=='__main__':run()
