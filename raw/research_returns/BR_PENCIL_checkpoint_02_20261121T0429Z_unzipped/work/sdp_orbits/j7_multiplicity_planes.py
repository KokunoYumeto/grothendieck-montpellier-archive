"""Exact rational projective arrangements for multiplicity (2,1,1)."""
from pathlib import Path
import sys,json,time
from collections import defaultdict,Counter
from itertools import product
from functools import lru_cache
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_typeB_line_conditions import primitive,canonical_rows
from j7_actual_line_rank_probe import prepare
from j7_joint_line_arrangements import arrangements


def rows_integer(M):
 return [r for r in (primitive(list(M.row(i))) for i in range(M.rows)) if r]


def condition(Q,d,m):
 """rank(Q|E) = baseline - drop*1_{C parameter=0}."""
 Q=Matrix(Q) if Q else Matrix.zeros(0,d);r=Q.rank()
 if m==1:
  return (int(r>0),int(r>0),rows_integer(Q))
 assert m==2 and d==3
 if r==0:return 0,0,[]
 if r==3:return 2,0,Matrix.eye(3).tolist()
 if r==2:
  return 2,1,[primitive(list(v)) for v in Q.nullspace()]
 # E=ker(Q) precisely when its dual normal lies in row(Q).
 row=next(Q.row(i) for i in range(Q.rows) if any(Q.row(i)))
 C=Matrix([primitive(list(v)) for v in Matrix(row).nullspace()])
 return 1,1,C.tolist()


def make_components(maps,arr):
 Aweights=sorted({w for rows in maps['A']['line_maps'].values() for w,Q in rows});Bweights=sorted({w for rows in maps['B']['line_maps'].values() for w,Q in rows})
 ids={'A':{w:i for i,w in enumerate(Aweights)},'B':{w:i for i,w in enumerate(Bweights)}}
 components={}
 for key,inf in arr['line_arrangements'].items():
  i=int(key);d=inf['quotient_dimension']
  for m in range(1,min(2,d)+1):
   raw=list(maps['A']['line_maps'][i])+list(maps['B']['line_maps'][i])
   if m==d:
    # The whole quotient block is a fixed component.
    E=Matrix.eye(d);states=[{'parameter_dimension':0,'basis':E.tolist(),'ranks':[Matrix(Q).rank() if Q else 0 for w,Q in raw]}];conds=[];bd=[]
   else:
    bd=[];conds=[]
    for w,Q in raw:
     base,drop,C=condition(Q,d,m);bd.append((base,drop));conds.append({'equations':C})
    states=[]
    for a in arrangements(conds,d):
     zeros=set(a['zero_columns']);ranks=[base-drop*int(j in zeros) for j,(base,drop) in enumerate(bd)]
     st={**a,'parameter_dimension':a['dimension'],'ranks':ranks}
     if a['dimension']==1:
      v=a['kernel'][0]
      E=Matrix(v) if m==1 else Matrix.hstack(*(Matrix(u) for u in Matrix([v]).nullspace()))
      st['basis']=E.tolist()
     states.append(st)
   for st in states:
    for ori,offset,number in [('A',0,7),('B',7,9)]:
     st[ori+'_mask1']=sum(1<<ids[ori][raw[offset+j][0]] for j in range(number) if st['ranks'][offset+j]>=1)
     st[ori+'_mask2']=sum(1<<ids[ori][raw[offset+j][0]] for j in range(number) if st['ranks'][offset+j]>=2)
   components[i,m]={'weight_index':i,'dimension':d,'multiplicity':m,'states':states,'conditions':conds,'base_drop':bd}
 return components


def refine_one(maps,components,choices):
 """choices tuples (weight,multiplicity,state_index); None denotes exclusion."""
 free=[choice for choice in choices if 'basis' not in components[choice[:2]]['states'][choice[2]]]
 assert len(free)==1
 i,m,s=free[0];comp=components[i,m];old=comp['states'][s];d=comp['dimension']
 K=Matrix.hstack(*(Matrix(v) for v in old['kernel']));kd=K.cols
 new_conditions=[];new_base_drop=[];fixedinc={}
 for ori in ['A','B']:
  columns=defaultdict(list)
  for h,mh,sh in choices:
   if (h,mh,sh)==free[0]:continue
   E=Matrix(components[h,mh]['states'][sh]['basis'])
   for w,Q in maps[ori]['line_maps'][h]:
    V=Matrix(Q)*E if Q else Matrix.zeros(0,E.cols)
    columns[w].extend(list(V.columnspace()))
  fixedinc[ori]=sum(Matrix.hstack(*vs).rank() for vs in columns.values() if vs)
  for w,Q0 in maps[ori]['line_maps'][i]:
   Q=Matrix(Q0) if Q0 else Matrix.zeros(0,d)
   if columns[w]:
    F=Matrix.hstack(*columns[w]);H=Matrix([primitive(list(v)) for v in F.T.nullspace()])
    if H.rows==0:H=Matrix.zeros(0,Q.rows)
    Q=H*Q
   base,drop,C=condition(Q.tolist(),d,m)
   C=Matrix(C)*K if C else Matrix.zeros(0,kd)
   new_conditions.append({'equations':rows_integer(C)});new_base_drop.append((base,drop))
 limits={'A':16-fixedinc['A'],'B':24-fixedinc['B']}
 if min(limits.values())<0:return None
 result=[]
 for new in arrangements(new_conditions,kd):
  zeros=set(new['zero_columns']);ranks=[b-dd*int(j in zeros) for j,(b,dd) in enumerate(new_base_drop)]
  if sum(ranks[:7])>limits['A'] or sum(ranks[7:])>limits['B']:continue
  KP=Matrix.hstack(*(Matrix(v) for v in new['kernel']));P=K*KP
  oldzero=set(old['zero_columns'])
  compatible=True
  for j,cc in enumerate(comp['conditions']):
   if j in oldzero:continue
   C=Matrix(cc['equations']) if cc['equations'] else Matrix.zeros(0,d)
   if C*P==Matrix.zeros(C.rows,P.cols):compatible=False;break
  if compatible:result.append({'parameter_basis':P.tolist(),'dimension':P.cols,'increment_A':fixedinc['A']+sum(ranks[:7]),'increment_B':fixedinc['B']+sum(ranks[7:])})
 return result or None


def actual_fixed(maps,components,choices):
 result={}
 for ori in ['A','B']:
  columns=defaultdict(list)
  for i,m,s in choices:
   E=Matrix(components[i,m]['states'][s]['basis'])
   for w,Q in maps[ori]['line_maps'][i]:
    V=Matrix(Q)*E if Q else Matrix.zeros(0,E.cols)
    columns[w].extend(list(V.columnspace()))
  result[ori]=sum(Matrix.hstack(*vs).rank() for vs in columns.values() if vs)
 return result


def go(S,sign=-1):
 base=Path(__file__).parent;stem=('det_' if sign==-1 else '')+'_'.join(map(str,S))
 arr=json.load(open(base/('j7_joint_line_'+stem+'.json')));sat=json.load(open(base/('j7_saturation_'+stem+'.json')))
 maps=prepare(S,arr,sign);components=make_components(maps,arr)
 records=[];counts=Counter();survivors=[]
 for rec in sat['remaining']:
  inds=rec['indices']
  if len(inds)!=3:continue
  for double in inds:
   if (double,2) not in components:continue
   keys=[(i,2 if i==double else 1) for i in inds]
   for ss in product(*(range(len(components[key]['states'])) for key in keys)):
    choices=tuple((i,m,s) for (i,m),s in zip(keys,ss));counts['states_tested']+=1
    masks=[0,0,0,0]
    for (i,m),s in zip(keys,ss):
     state=components[i,m]['states'][s]
     for j,k in enumerate(['A_mask1','A_mask2','B_mask1','B_mask2']):masks[j]|=state[k]
    if masks[0].bit_count()+masks[1].bit_count()>16 or masks[2].bit_count()+masks[3].bit_count()>24:
     counts['weight_rank_excludes']+=1;continue
    free=sum('basis' not in components[i,m]['states'][s] for i,m,s in choices)
    if free==0:
     ranks=actual_fixed(maps,components,choices)
     if ranks['A']>16 or ranks['B']>24:counts['fixed_rank_excludes']+=1;continue
     counts['fixed_survives']+=1;survivors.append({'choices':choices,'increments':ranks});continue
    if free==1:
     refined=refine_one(maps,components,choices)
     if not refined:counts['one_parameter_excludes']+=1;continue
     counts['one_parameter_survives']+=1;survivors.append({'choices':choices,'refined':refined});continue
    counts['multiple_parameters_remain']+=1;survivors.append({'choices':choices,'free_components':free})
 print(S,'sign',sign,dict(counts),'survivors',len(survivors),flush=True)
 out={'subset':S,'sign':sign,'components':{str(k):v for k,v in components.items()},'counts':dict(counts),'survivors':survivors}
 (base/('j7_multiplicity_'+stem+'.json')).write_text(json.dumps(out,indent=2,default=lambda x:int(x) if getattr(x,'is_Integer',False) else str(x))+'\n')
 return out

if __name__=='__main__':
 st=time.time();go([0,1,3,6,7,9,18],-1);print('seconds',time.time()-st)
