"""Refine two free extension lines modulo their fixed complement."""
from pathlib import Path
import sys,json,time
from collections import defaultdict,Counter
from itertools import product
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_typeB_line_conditions import primitive,canonical_rows
from j7_actual_line_rank_probe import prepare
from j7_joint_line_arrangements import arrangements


def go(S,sign=-1):
 base=Path(__file__).parent;stem=('det_' if sign==-1 else '')+'_'.join(map(str,S))
 arr=json.load(open(base/('j7_joint_line_'+stem+'.json')));previous=json.load(open(base/('j7_one_variable_'+stem+'.json')))
 maps=prepare(S,arr,sign);result=[];counts=Counter()
 for rec in previous['remaining']:
  if rec.get('multiplicity_case'):continue
  for case in rec['joint_states']:
   inds=rec['indices'];choices=case['states'];dims=case['dimensions'];free=[(i,j) for i,j,d in zip(inds,choices,dims) if d>1]
   assert len(free)==2
   fixed=tuple((h,s) for h,s,dim in zip(inds,choices,dims) if dim==1)
   fixedcolumns={};fixedinc={}
   for ori in ['A','B']:
    col=defaultdict(list)
    for c in fixed:
     for w,v in maps[ori]['fixed_vectors'][c]:
      if any(v):col[w].append(v)
    fixedinc[ori]=sum(Matrix.hstack(*(Matrix(v) for v in vs)).rank() for vs in col.values());fixedcolumns[ori]=col
   limits={'A':16-fixedinc['A'],'B':24-fixedinc['B']}
   linestates=[]
   for i,j in free:
    old=arr['line_arrangements'][str(i)]['states'][j];K=Matrix.hstack(*(Matrix(v) for v in old['kernel']));d=K.cols
    conds=[];oldconds=[];qcols=[]
    for ori in ['A','B']:
     for w,Q0 in maps[ori]['line_maps'][i]:
      Q=Matrix(Q0)*K if Q0 else Matrix.zeros(0,d);oldconds.append(Q)
      vs=fixedcolumns[ori][w]
      if vs:
       F=Matrix.hstack(*(Matrix(v) for v in vs));N=F.T.nullspace();H=Matrix([primitive(list(v)) for v in N]) if N else Matrix.zeros(0,Q.rows);Q=H*Q
      qcols.append((ori,w,Q));rows=[primitive(list(Q.row(k))) for k in range(Q.rows)];conds.append({'equations':canonical_rows([r for r in rows if r],d)})
    states=[]
    for new in arrangements(conds,d):
     KP=Matrix.hstack(*(Matrix(v) for v in new['kernel']));oldzero=set(old['zero_columns'])
     if any(z not in oldzero and oldconds[z]*KP==Matrix.zeros(oldconds[z].rows,KP.cols) for z in range(16)):continue
     active={'A':set(),'B':set()};vectors={};zero=set(new['zero_columns'])
     for z,(ori,w,Q) in enumerate(qcols):
      if z not in zero:active[ori].add(w)
      vectors[ori,w]=Q*KP
     states.append({'dimension':KP.cols,'basis':K*KP,'active':active,'vectors':vectors})
    linestates.append(states)
   survivors=[]
   for s,t in product(range(len(linestates[0])),range(len(linestates[1]))):
    X,Y=linestates[0][s],linestates[1][t]
    lower={o:len(X['active'][o]|Y['active'][o]) for o in ['A','B']}
    if any(lower[o]>limits[o] for o in ['A','B']):counts['new_weight_union_excludes']+=1;continue
    if X['dimension']==Y['dimension']==1:
     ranks={}
     for o in ['A','B']:
      ranks[o]=0
      for w in X['active'][o]|Y['active'][o]:
       columns=[D['vectors'][o,w] for D in (X,Y) if (o,w) in D['vectors']]
       ranks[o]+=Matrix.hstack(*columns).rank()
     if any(ranks[o]>limits[o] for o in ['A','B']):counts['new_fixed_rank_excludes']+=1;continue
    survivors.append({'state_pair':[s,t],'dimensions':[X['dimension'],Y['dimension']],'lower':lower,'parameter_bases':[X['basis'].tolist(),Y['basis'].tolist()]});counts['survives']+=1
   out={'indices':inds,'states':choices,'free':free,'limits':limits,'new_line_states':[len(x) for x in linestates],'survivors':survivors};result.append(out)
   print(inds,'states',[len(x) for x in linestates],'survivors',len(survivors),flush=True)
 out={'subset':S,'sign':sign,'counts':dict(counts),'records':result}
 (base/('j7_two_variable_'+stem+'.json')).write_text(json.dumps(out,indent=2)+'\n');print('counts',dict(counts),flush=True);return out

if __name__=='__main__':
 st=time.time();go([0,1,3,6,7,9,18],-1);print('seconds',time.time()-st)
