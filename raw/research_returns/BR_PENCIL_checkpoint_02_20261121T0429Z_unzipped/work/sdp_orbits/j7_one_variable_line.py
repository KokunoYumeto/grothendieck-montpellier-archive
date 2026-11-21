"""Refine four-weight extensions with one parameter line by exact arrangements."""
from pathlib import Path
import sys,json,time
from collections import defaultdict,Counter
from functools import lru_cache
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_typeB_line_conditions import primitive,canonical_rows
from j7_actual_line_rank_probe import prepare
from j7_joint_line_arrangements import arrangements


def go(S,sign=1):
 base=Path(__file__).parent;stem=('det_' if sign==-1 else '')+'_'.join(map(str,S))
 arr=json.load(open(base/('j7_joint_line_'+stem+'.json')))
 previous=json.load(open(base/('j7_actual_line_rank_'+stem+'.json')))
 maps=prepare(S,arr,sign);counts=Counter();remaining=[];witnesses=[]
 for rec in previous['remaining']:
  if rec.get('multiplicity_case'):remaining.append(rec);continue
  states=[]
  for case in rec['joint_states']:
   inds=rec['indices'];choices=case['states'];dims=case['dimensions']
   free=[(i,j) for i,j,d in zip(inds,choices,dims) if d>1]
   if len(free)!=1:states.append(case);counts['multiple_parameter_lines']+=1;continue
   i,j=free[0];st=arr['line_arrangements'][str(i)]['states'][j];K=Matrix.hstack(*(Matrix(v) for v in st['kernel']));d=K.cols
   fixed=tuple((h,s) for h,s,dim in zip(inds,choices,dims) if dim==1)
   conds=[];oldconds=[];actualfixed={}
   for ori in ['A','B']:
    fixedcolumns=defaultdict(list)
    for c in fixed:
     for w,v in maps[ori]['fixed_vectors'][c]:
      if any(v):fixedcolumns[w].append(v)
    actualfixed[ori]=sum(Matrix.hstack(*(Matrix(v) for v in vs)).rank() for vs in fixedcolumns.values())
    for w,Q0 in maps[ori]['line_maps'][i]:
     Q=Matrix(Q0)*K if Q0 else Matrix.zeros(0,d)
     oldconds.append(Q)
     if not Q.rows:conds.append({'equations':[]});continue
     F=Matrix.hstack(*(Matrix(v) for v in fixedcolumns[w])) if fixedcolumns[w] else Matrix.zeros(Q.rows,0)
     null=F.T.nullspace();H=Matrix([primitive(list(v)) for v in null]) if null else Matrix.zeros(0,Q.rows)
     R=H*Q
     raw=[primitive(list(R.row(k))) for k in range(R.rows)];eq=canonical_rows([row for row in raw if row],d)
     conds.append({'equations':eq})
   allowed={'A':16-actualfixed['A'],'B':24-actualfixed['B']}
   if min(allowed.values())<0:counts['fixed_exact_rank_excludes']+=1;continue
   surviving=[]
   for new in arrangements(conds,d):
    zeros=set(new['zero_columns']);activeA=7-sum(z<7 for z in zeros);activeB=9-sum(z>=7 for z in zeros)
    if activeA>allowed['A'] or activeB>allowed['B']:continue
    KP=Matrix.hstack(*(Matrix(v) for v in new['kernel']))
    # The original arrangement stratum required every old nonzero column
    # to remain nonzero. A finite union of proper linear subspaces cannot
    # cover KP over an infinite field, so this is the precise compatibility.
    oldzero=set(st['zero_columns'])
    if any(z not in oldzero and oldconds[z]*KP==Matrix.zeros(oldconds[z].rows,KP.cols) for z in range(16)):
     continue
    surviving.append({'new_kernel':new['kernel'],'new_dimension':new['dimension'],'actual_increment_A':actualfixed['A']+activeA,'actual_increment_B':actualfixed['B']+activeB})
   if surviving:
    states.append({**case,'refined':surviving});counts['one_parameter_line_survives']+=1
   else:counts['one_parameter_line_excludes']+=1
  if states:remaining.append({**rec,'joint_states':states})
 result={'subset':S,'sign':sign,'counts':dict(counts),'remaining':remaining}
 (base/('j7_one_variable_'+stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
 print(S,'sign',sign,dict(counts),'remaining supports',len(remaining),flush=True)
 return result

if __name__=='__main__':
 st=time.time();go([0,1,3,6,7,9,18],-1);print('seconds',time.time()-st)
