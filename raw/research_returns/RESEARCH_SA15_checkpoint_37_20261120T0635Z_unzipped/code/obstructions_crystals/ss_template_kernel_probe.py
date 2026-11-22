#!/usr/bin/env python3
from pathlib import Path
from time import perf_counter
import json
start=perf_counter()
source=Path('../../outputs/ss_rectangular_sparse_templates.json')
data=json.loads(source.read_text())
assert data['successful_template']['pattern']==62556

def basis(n):return [(i,0) for i in range(n//2+1)]+[(i,1) for i in range((n-3)//2+1)]
def nullspace(rows,N):
    a=rows[:];piv=[];r=0
    for j in range(N):
        k=next((k for k in range(r,len(a)) if (a[k]>>j)&1),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        for k in range(len(a)):
            if k!=r and (a[k]>>j)&1:a[k]^=a[r]
        piv.append(j);r+=1
    out=[]
    for f in range(N):
        if f in piv:continue
        v=1<<f
        for i,j in enumerate(piv):
            if (a[i]>>f)&1:v^=1<<j
        out.append(v)
    return out

def support(v,N):return [i for i in range(N) if(v>>i)&1]
rows=[]
for c in data['successful_template']['certificates']:
 q=c['m'];N=6*q;B=basis(2*q);ix={v:i for i,v in enumerate(B)}
 left=nullspace(c['columns'],N)
 assert len(left)==2
 s=0
 for i in range(18):
  if(62556>>i)&1:
   s^=1<<(3*ix[tuple(c['template'][i//3])]+i%3)
 ds=0
 for i,(a,b) in enumerate(B):
  for j in range(3):
   if not(s>>(3*i+j))&1:continue
   terms=[]
   if a%2:terms.append((a-1,b))
   if b:terms.append((a+2,0))
   for t in terms:ds^=1<<(3*ix[t]+j)
 pair=[[((v&w).bit_count()%2) for w in [s,ds]] for v in left]
 assert (pair[0][0]*pair[1][1]+pair[0][1]*pair[1][0])%2==1
 rows.append({'q':q,'left_kernel':left,'support':[support(v,N) for v in left],
              'support_size':[v.bit_count() for v in left], 'pairing_s_ds':pair})
out={'scope':'Finite left-kernel patterns, not a uniform proof','rows':rows,'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
