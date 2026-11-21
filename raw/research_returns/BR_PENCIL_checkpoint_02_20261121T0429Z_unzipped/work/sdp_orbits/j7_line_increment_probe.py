"""Exploratory small exact linear-arrangement bounds on four weight lines."""
from pathlib import Path
import sys,json,time
from itertools import combinations,product
from functools import lru_cache
import numpy as np
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
import per5_prolongation_certificate as p
from det7_typeB_line_conditions import conditions,rank
from det7_prolongation import data,quad_weight,var_weight


def go(S, sign=1):
 prefix="det_" if sign==-1 else ""
 inp=Path(__file__).with_name('j7_saturation_'+prefix+('_'.join(map(str,S)))+'.json')
 sat=json.load(open(inp));variables,T,blocks,image=data(S,sign)
 # data's ordering is different from saturation file. Work by weight.
 byweight={tuple(w):(block,dim) for w,block,dim in blocks}
 Aweights=[tuple(-x for x in quad_weight(q)) for q in S];Bweights=[var_weight(v) for v in variables]
 info={}
 for i,record in enumerate(sat['weights']):
  w0=record['weight'];w=tuple(w0[:3]+[0]+w0[3:]+[0]);block,dim=byweight[w]
  info[i]={'A':{},'B':{}}
  for ori,fw in [('A',Aweights),('B',Bweights)]:
   cond=conditions(T,variables,w,block,ori,S=S,image_character=w in image)
   patterns=[]
   for count in range(len(fw),-1,-1):
    for zeros in combinations(range(len(fw)),count):
     if any(set(zeros)<set(z) for z in patterns):continue
     eq=[row for j in zeros for row in cond[j]['equations']]
     if rank(eq,dim)<dim:patterns.append(zeros)
   info[i][ori]={'mininc':len(fw)-max(map(len,patterns)),'zero_sets':patterns,'weights':[tuple(a+b for a,b in zip(w,u)) for u in fw]}
 print('minincrements',[ (i,d['A']['mininc'],d['B']['mininc']) for i,d in info.items()],flush=True)
 base={o:rank(p.prolongation_matrix([T[:,:,c] for c in range(T.shape[2])],o).tolist(),0) for o in ['A','B']}
 limits={o:(len(fw)-1)*13-base[o] for o,fw in [('A',Aweights),('B',Bweights)]}
 print('base',base,'limits',limits,flush=True)
 # Distinct-weight lines are the 4-support cases. Multiplicity cases deferred.
 remain=[];ex=0
 for rec in sat['remaining']:
  inds=rec['indices']
  if len(inds)!=4:remain.append(rec);continue
  failed=False
  bounds={}
  for ori in ['A','B']:
   allweights=[w for i in inds for w in info[i][ori]['weights']]
   overlap=len(allweights)-len(set(allweights))
   lower=sum(info[i][ori]['mininc'] for i in inds)-overlap
   bounds[ori]=lower
   if lower>limits[ori]:failed=True;break
  if failed:ex+=1
  else:remain.append({**rec,'simple_increment_bounds':bounds})
 print('excluded',ex,'remaining',len(remain),flush=True)
 out={'subset':S,'base':base,'increment_limits':limits,'line_info':info,'excluded':ex,'remaining':remain}
 Path(__file__).with_name('j7_line_increment_'+prefix+('_'.join(map(str,S)))+'.json').write_text(json.dumps(out,indent=2)+'\n')
 return out

if __name__=='__main__':
 for S in [[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]]:go(S)
