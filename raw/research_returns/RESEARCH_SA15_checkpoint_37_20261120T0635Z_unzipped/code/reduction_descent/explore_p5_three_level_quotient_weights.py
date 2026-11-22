"""Exploratory finite p5 exact coefficient bounds, not a promoted result."""
from itertools import product
from pathlib import Path
from datetime import datetime,timezone
import json,time
st=time.perf_counter()
p=5;N=24;types={'A':(1,5),'B':(9,21),'C':(13,17)}
monomials=[v for v in product(range(5),repeat=3) if 1<=sum(v)<=4]
rows=[]
for name1,name2 in [('A','B'),('A','C'),('B','C')]:
 for c in types[name1]:
  for d in types[name2]:
   weights=(5*c%24,5*d%24,c)
   for e in (8,12,16,20,24):
    a=e*N; qs=[(1,1,1)]
    for _ in range(2):
     old=qs[-1]; new=[]
     for target in weights:
      candidates=[(a+min(old),'p-divisible',None),(25*min(old),'high-degree',None)]
      for beta in monomials:
       residue=(target-p*sum(x*y for x,y in zip(beta,weights)))%N
       value=(residue or N)+p*sum(x*y for x,y in zip(beta,old))
       candidates.append((value,'p-multiple',beta))
      new.append(min(candidates,key=lambda x:x[0])[0])
     qs.append(tuple(new))
    rows.append({'types':[name1,name2],'c':c,'d':d,'e':e,'tangent_weights':weights,'q':qs,'minimum_q2':min(qs[2]),'threshold':a//4,'excludes_by_bound':min(qs[2])>=a//4})
out={'status':'EXPLORATORY_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-st,'rows':rows,'scope':'Finite lower bounds for actual-target coefficient weights. No promoted group exclusion is inferred before full proof audit.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
for pair in [('A','B'),('A','C'),('B','C')]:
 print(pair,sorted(set((r['minimum_q2'],r['e'],r['excludes_by_bound']) for r in rows if r['types']==list(pair))))
