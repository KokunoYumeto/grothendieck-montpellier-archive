"""Independent exact rational verification of all M=16 LP certificates.
Coverage is checked by matching every line of the separately generated spectral files.
No NumPy, SciPy, SymPy, or floating point is used here.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json,time
p=Path(__file__).resolve().parent;start=time.time()
for target in (8,16):
 lines=(p/f'm16_chi{target}_spectra.txt').read_text().splitlines()
 keys=[tuple(map(int,line.split())) for line in lines]
 assert len(set(keys))==len(keys)
 seen=set();positive=negative=0
 for line in (p/f'm16_chi{target}_certificates.jsonl').open():
  r=json.loads(line);W=r['W'];key=tuple(v for X in W for v in X)
  assert key not in seen;seen.add(key)
  sets=[sorted(set(X)) for X in W];mult=[Counter(X) for X in W]
  E=[e for e in product(*sets) if sum(e)%16==0]
  rows=[(j,v) for j in range(3) for v in sets[j]]
  assert sum(map(sum,W))%16==(2 if target==8 else 1)
  if 'y' in r:
   y=dict(zip(rows,map(Fraction,r['y'])))
   assert len(y)==len(rows)
   assert all(sum(y[j,e[j]] for j in range(3))>=0 for e in E)
   assert sum(y[j,v]*mult[j][v] for j,v in rows)<0
   negative+=1
  else:
   assert r['E']==[list(e) for e in E]
   x=list(map(Fraction,r['x']));assert len(x)==len(E)
   assert all(a>0 for a in x)
   assert all(sum(x[k] for k,e in enumerate(E) if e[j]==v)==mult[j][v] for j,v in rows)
   assert all(v%2==0 for X in W for v in X)
   positive+=1
 assert seen==set(keys)
 assert (positive,negative)==((4,31298) if target==8 else (0,56418))
 print(json.dumps({'target':target,'result':'PASS','positive':positive,'negative':negative,'coverage_matches_spectral_list':len(seen),'elapsed_seconds':round(time.time()-start,3)}),flush=True)
