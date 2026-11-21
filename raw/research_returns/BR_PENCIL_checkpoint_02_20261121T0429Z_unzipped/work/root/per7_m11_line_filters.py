"""Exact-modular finite line-increment bounds for the per7 support11 cases."""
from pathlib import Path
from itertools import combinations
import sys,json,time
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pencil'))
from det7_prolongation import data,quad_weight,var_weight,rank
from det7_typeB_line_conditions import conditions

def main():
 source=json.loads(Path(__file__).with_name('per7_small_prolongation.json').read_text())['records']
 results=[];start=time.time()
 for old in source:
  if len(old['support'])!=11:continue
  S=old['subset'];variables,T,blocks,image=data(S,1);used=sorted({i for pair in old['remaining'] for i in pair})
  assert all(len(pair)==2 for pair in old['remaining'])
  aw=[tuple(-v for v in quad_weight(q)) for q in S];bw=[var_weight(v) for v in variables]
  info={}
  for bi in used:
   w,coords,dim=blocks[bi];ci={}
   for F,fw in [('A',aw),('B',bw)]:
    d=len(fw);cond=conditions(T,variables,w,coords,F,S,w in image)
    maxzeros=0
    for nz in range(d,-1,-1):
     found=False
     for zero in combinations(range(d),nz):
      eq=[row for c in zero for row in cond[c]['equations']]
      M=np.array(eq,dtype=np.int64).reshape((len(eq),dim))
      rr,_,_=rank(M)
      if rr<dim:found=True;break
     if found:maxzeros=nz;break
    ci[F]={'minimum_increment':d-maxzeros,'conditions':cond,'weights':[tuple(x+y for x,y in zip(w,f)) for f in fw]}
   info[str(bi)]={'quotient_dimension':dim,'factors':ci}
  remaining=[];excluded=[]
  for pair in old['remaining']:
   i,j=pair;proofs=[]
   for F,d in [('A',7),('B',11)]:
    left=info[str(i)]['factors'][F];right=info[str(j)]['factors'][F]
    overlap=len(set(left['weights'])&set(right['weights']))
    inc=left['minimum_increment']+right['minimum_increment']-overlap
    if old['baseline'][F]+inc>(d-1)*13:
     proofs.append({'factor':F,'increment':inc,'overlap':overlap})
   if proofs:excluded.append({'pair':pair,'proofs':proofs})
   else:remaining.append(pair)
  rec={'subset':S,'baseline':old['baseline'],'block_info':info,'excluded':excluded,'remaining':remaining}
  results.append(rec)
  print(S,'pairs',len(old['remaining']),'excluded',len(excluded),'remaining',len(remaining),'dims',[(pair,[blocks[i][2] for i in pair]) for pair in remaining],flush=True)
  Path(__file__).with_name('per7_m11_line_filters.json').write_text(json.dumps(results,indent=2)+'\n')
 print('DONE',time.time()-start,flush=True)
if __name__=='__main__':main()
