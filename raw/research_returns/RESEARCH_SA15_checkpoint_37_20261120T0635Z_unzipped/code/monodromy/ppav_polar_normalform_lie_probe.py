#!/usr/bin/env python3
"""Exact Lie-stabilizer probes for polar tensors. No full theorem inference."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,itertools
start=time.perf_counter()
base=Path(__file__).resolve().parents[1]
prior=json.loads((base/'outputs/ppav_polar_normalform_probe.json').read_text())
trips=list(itertools.combinations(range(9),3));idx={t:i for i,t in enumerate(trips)}
def rank(rows):
 piv={}
 for r in rows:
  while r:
   j=r.bit_length()-1
   if j in piv:r^=piv[j]
   else:piv[j]=r;break
 return len(piv)
result=[]
for old in prior['rows']:
 B={tuple(i-1 for i in t) for t in old['polar_terms']};cols=[]
 for a in range(9):
  for b in range(9):
   v=0
   for t in B:
    if b not in t:continue
    tt=[a if c==b else c for c in t]
    if len(set(tt))<3:continue
    v^=1<<idx[tuple(sorted(tt))]
   if a==b:v^=1<<84
   cols.append(v)
 rr=rank(cols)
 result.append({'parameters':old['parameters'],'Lie_sl9_stabilizer_dimension':81-rr,'matrix_rank_including_trace':rr})
out={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'rows':result,'scope':'Exact infinitesimal stabilizer dimensions; no actual-Cartier identification or stability theorem inferred here.'}
(base/'outputs/ppav_polar_normalform_lie_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
