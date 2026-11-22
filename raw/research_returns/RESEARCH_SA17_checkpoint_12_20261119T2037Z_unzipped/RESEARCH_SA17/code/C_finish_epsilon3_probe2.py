#!/usr/bin/env python3
"""Adaptive integral extension probe; only found explicit sequences certify relations."""
from pathlib import Path
exec(Path('code/C_finish_epsilon3_probe.py').read_text().split('\ncandidates=valid=classified=0;relations={}')[0])

def blocks(ta0,tb0,rhs):
 a,b=rhs.shape;free=[];base=np.zeros((a,b),dtype=np.int64)
 for i,j in product(range(a),range(b)):
  coef=ta0[i,i]+tb0[j,j]
  if coef:
   if rhs[i,j]%coef:return
   base[i,j]=rhs[i,j]//coef
  elif rhs[i,j]:return
  else:free.append((i,j))
 for vals in product((-1,0,1),repeat=len(free)):
  ans=base.copy()
  for ij,v in zip(free,vals):ans[ij]=v
  yield ans

candidates=valid=classified=0;relations={}
for na,ta,ea in ob:
 for nb,tb,eb in ob:
  a,b=len(ta[0]),len(tb[0]);z=np.zeros((b,a),dtype=np.int64)
  for x0 in blocks(ta[0],tb[0],np.zeros((a,b),dtype=np.int64)):
   for x1 in blocks(ta[0],tb[0],-ta[1]@x0-x0@tb[1]):
    for x2 in blocks(ta[0],tb[0],-ta[1]@x1-ta[2]@x0-x0@tb[2]-x1@tb[1]):
     candidates+=1;xs=[x0,x1,x2]
     t=[np.block([[ta[r],xs[r]],[z,tb[r]]]) for r in range(3)]
     assert np.array_equal(t[0]@t[0],np.eye(a+b,dtype=np.int64))
     assert not np.any(t[0]@t[1]+t[1]@t[0])
     assert not np.any(t[0]@t[2]+t[2]@t[0]+t[1]@t[1])
     valid+=1;can=canonical(t)
     if can is None:continue
     classified+=1
     rel=tuple(ea[i]+eb[i]-can['extra'][i] for i in range(3))
     if rel!=(0,0,0) and rel not in relations:
      relations[rel]={'A':na,'B':nb,'X':[x.tolist() for x in xs],'quotient':can}
report={'scope':'free opposite-sign coefficients -1,0,1; same-sign coefficients solved integrally; endpoints plus/minus/M22/M12/M21','admissible':valid,'classified_after_regular_removal':classified,'relations':[{'vector':r,**v} for r,v in relations.items()],'runtime':perf_counter()-START}
Path('logs/C_finish_epsilon3_probe2.json').write_text(json.dumps(report,indent=2,default=str)+'\n')
print(json.dumps(report,indent=2,default=str))
