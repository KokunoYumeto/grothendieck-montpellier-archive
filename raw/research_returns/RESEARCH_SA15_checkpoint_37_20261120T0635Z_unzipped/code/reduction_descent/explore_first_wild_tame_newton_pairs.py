"""Exploratory p5/e20 Newton rows; conditional constraints, not a theorem."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
from itertools import product
st=time.perf_counter();p=5;N=24;e=20
cs=[c for c in range(N) if c%4==1]
rows=[];raw=0
for B1,B2 in product(range(5,100,10),repeat=2):
 if B1>B2:continue
 b1,b2=B1//p,B2//p
 for c1,c2 in product(cs,repeat=2):
  if (B1-c1)%6 or (B2-c2)%6:continue
  S1=sorted({c1,5*c1%24});S2=sorted({c2,5*c2%24})
  if S1==S2:continue
  h1=(c1-B1)%24;l1=(5*c1+B1)%24
  h2=(c2-B2)%24;l2=(5*c2+B2)%24
  assert h1%6==l1%6==h2%6==l2%6==0
  assert h1!=l1 and h2!=l2
  if sorted([h1,l1])!=sorted([h2,l2]):continue
  raw+=1;aligned=(h1==h2)
  if b1%5 and b2%5:continue
  if b1%5 or b2%5:
   prime,div=(b1,b2) if b1%5 else (b2,b1)
   if not aligned or div<prime:continue
  rows.append(dict(B=[B1,B2],b=[b1,b2],c=[c1,c2],special=[S1,S2],high_aligned=aligned,
                   high_quotient=[5*B1 if B1<20 else 120-B1,5*B2 if B2<20 else 120-B2]))
keys=sorted(set((tuple(r['B']),r['high_aligned']) for r in rows))
assert keys==[((25,75),False),((35,75),True),((55,75),True)]
one=[]
for c1,c2 in product(cs,repeat=2):
 if c1>=c2:continue
 S1=sorted({c1,5*c1%24});S2=sorted({c2,5*c2%24})
 a1=(c1+20)%24;a2=(c2+20)%24
 if S1!=S2 and sorted({a1,5*a1%24})==sorted({a2,5*a2%24}):
  one.append(dict(c=[c1,c2],special=[S1,S2],residual=sorted({a1,5*a1%24})))
out=dict(status='EXPLORATORY_COMPLETE',actual_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-st,
         raw_tame_character_rows=raw,retained_rows=rows,parameter_flag_keys=keys,one_slope_rows=one,
         scope='Finite arithmetic after conditional common-point-field inequalities proposed in the research notes. Does not establish actual formal-group existence, prove the imported arbitrary-e extension, or exclude residual-wild cases. No promotion from these rows.')
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
