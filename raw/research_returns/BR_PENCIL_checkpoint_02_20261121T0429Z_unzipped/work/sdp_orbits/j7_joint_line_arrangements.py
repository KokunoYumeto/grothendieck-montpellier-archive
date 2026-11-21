"""Exploratory exact rational arrangements for four distinct extension weights."""
from pathlib import Path
import sys,json,time
from itertools import product
from functools import lru_cache
from collections import Counter
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_typeB_line_conditions import conditions,primitive
from det7_prolongation import data,quad_weight,var_weight

@lru_cache(None)
def span(rows,d):
 if not rows:return ()
 R,piv=Matrix(rows).rref()
 return tuple(tuple(primitive(list(R.row(i)))) for i in range(len(piv)))

def arrangements(conds,d):
 states={()}
 for col in conds:
  more=set()
  for E in states:
   Q=span(E+tuple(tuple(r) for r in col['equations']),d)
   if len(Q)<d:more.add(Q)
  states.update(more)
 out=[]
 for E in sorted(states):
  zeros=[j for j,col in enumerate(conds) if len(span(E+tuple(tuple(r) for r in col['equations']),d))==len(E)]
  K=Matrix(E).nullspace() if E else [Matrix.eye(d)[:,i] for i in range(d)]
  out.append({'equations':E,'zero_columns':zeros,'dimension':d-len(E),'kernel':[primitive(list(v)) for v in K]})
 return out

def go(S, sign=1):
 base=Path(__file__).parent;stem=('det_' if sign==-1 else '')+'_'.join(map(str,S))
 sat=json.load(open(base/('j7_saturation_'+stem+'.json')))
 previous=json.load(open(base/('j7_line_increment_'+stem+'.json')))
 variables,T,blocks,image=data(S,sign);byweight={tuple(w):(block,dim) for w,block,dim in blocks}
 info={};Aw=set();Bw=set()
 for i,r in enumerate(sat['weights']):
  w0=r['weight'];w=tuple(w0[:3]+[0]+w0[3:]+[0]);block,dim=byweight[w]
  A=conditions(T,variables,w,block,'A',S=S,image_character=w in image)
  B=conditions(T,variables,w,block,'B',S=S,image_character=w in image)
  states=arrangements(A+B,dim)
  for state in states:
   state['A_active']=[tuple(col['target_weight']) for j,col in enumerate(A) if j not in state['zero_columns']]
   state['B_active']=[tuple(col['target_weight']) for j,col in enumerate(B) if j+7 not in state['zero_columns']]
   Aw.update(state['A_active']);Bw.update(state['B_active'])
  info[i]={'states':states,'block':block,'quotient_dimension':dim,'weight':w}
 Aids={w:i for i,w in enumerate(sorted(Aw))};Bids={w:i for i,w in enumerate(sorted(Bw))}
 for inf in info.values():
  for state in inf['states']:
   state['A_mask']=sum(1<<Aids[w] for w in state['A_active']);state['B_mask']=sum(1<<Bids[w] for w in state['B_active'])
 print('arrangements',S,Counter(len(i['states']) for i in info.values()),flush=True)
 remain=[];ex=0;poss=0;dimensions=Counter()
 for rec in previous['remaining']:
  inds=rec['indices']
  if len(inds)!=4:remain.append({**rec,'multiplicity_case':True});continue
  survivors=[]
  for choices in product(*(range(len(info[i]['states'])) for i in inds)):
   A=B=0
   for i,j in zip(inds,choices):
    st=info[i]['states'][j];A|=st['A_mask'];B|=st['B_mask']
   if A.bit_count()>16 or B.bit_count()>24:continue
   dims=[info[i]['states'][j]['dimension'] for i,j in zip(inds,choices)]
   survivors.append({'states':choices,'dimensions':dims,'A_weight_count':A.bit_count(),'B_weight_count':B.bit_count()});dimensions[tuple(sorted(dims))]+=1
  if survivors:remain.append({**rec,'joint_states':survivors});poss+=len(survivors)
  else:ex+=1
 print('excluded',ex,'remaining supports',len(remain),'joint states',poss,'dimensions',dimensions,flush=True)
 out={'subset':S,'line_arrangements':info,'excluded_supports':ex,'joint_states_count':poss,'remaining':remain}
 (base/('j7_joint_line_'+stem+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 return out

if __name__=='__main__':
 st=time.time()
 for S in [[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]]:go(S)
 print('seconds',time.time()-st)
