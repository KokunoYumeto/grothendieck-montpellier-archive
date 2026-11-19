#!/usr/bin/env python3
"""Bounded search for one sparse template across doubling rectangular sizes.

Every rejected template and tested rank is retained. Finite success would
only suggest a uniform proof, never establish one.
"""
from pathlib import Path
import itertools,json,random,time
started=time.perf_counter();w=Path(__file__).resolve().parents[1]
def basis(n):
 return [(i,0) for i in range(n//2+1)]+[(i,1) for i in range((n-3)//2+1)]
def cartier_product(a,b,index):
 i,j=a[0]+b[0],a[1]+b[1]
 terms=[(i,j)] if j<2 else [(i,1),(i+3,0)]
 out=set()
 for i,j in terms:
  q=((i//2,1) if i%2 else (i//2+1,0)) if j else ((i//2,0) if i%2 else None)
  if q is not None:
   k=index[q]
   if k in out:out.remove(k)
   else:out.add(k)
 return out
def rank(columns):
 piv={}
 for v in columns:
  while v:
   j=v.bit_length()-1
   if j in piv:v^=piv[j]
   else:piv[j]=v;break
 return len(piv)
def apply(columns,v):
 out=0
 while v:
  bit=v&-v;v^=bit;out^=columns[bit.bit_length()-1]
 return out
def elementary(m):
 n=2*m;B=basis(n);D=basis(3);ix={a:i for i,a in enumerate(B)};iy={a:i for i,a in enumerate(D)}
 template=[(0,0),(1,0),(m-1,0),(m,0),(m-3,1),(m-2,1)]
 matrices=[]
 for a,b in itertools.product(template,D):
  columns=[]
  for u,v in itertools.product(B,D):
   col=0
   for i,j in itertools.product(cartier_product(a,u,ix),cartier_product(b,v,iy)):col^=1<<(3*i+j)
   columns.append(col)
  matrices.append(columns)
 return dict(m=m,n=n,basis=B,template=template,matrices=matrices)
sizes=[3,6,12,24,48,96]
systems={m:elementary(m) for m in sizes}
rng=random.Random(202611191201);budget=2000;trials=[];success=None
for attempt in range(budget):
 pattern=74594 if attempt==0 else rng.getrandbits(18)
 rec={'pattern':pattern,'tested':[]};good=True;certificates=[]
 for m in sizes:
  system=systems[m];N=6*m;C=[0]*N
  for j in range(18):
   if pattern>>j&1:C=[a^b for a,b in zip(C,system['matrices'][j])]
  r1=rank(C);r2=rank([apply(C,v) for v in C]) if r1==N-2 else None
  rec['tested'].append({'m':m,'rank_C':r1,'rank_C2':r2,'target':N-2})
  if r1!=N-2 or r2!=N-2:good=False;break
  certificates.append({'m':m,'degrees':[2*m,3],'template':system['template'],'columns':C,'rank_C':r1,'rank_C2':r2})
 trials.append(rec)
 if good:success={'pattern':pattern,'certificates':certificates};break
out={'status':'COMMON_FINITE_TEMPLATE_FOUND' if success else 'NO_COMMON_TEMPLATE_IN_BUDGET',
 'scope':'Finite bounded evidence only; no uniform or geometric inference',
 'seed':202611191201,'budget':budget,'sizes_half_first_degree':sizes,
 'template':'(1,x,x^(m-1),x^m,y*x^(m-3),y*x^(m-2)) tensor (1,x,y)',
 'complete_trials':trials,'successful_template':success,'elapsed_seconds':time.perf_counter()-started}
(w/'outputs/ss_rectangular_sparse_templates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'trials':len(trials),'pattern':None if success is None else success['pattern'],
 'elapsed_seconds':out['elapsed_seconds'],'output':'outputs/ss_rectangular_sparse_templates.json'},indent=2))
