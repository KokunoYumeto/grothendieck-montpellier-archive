"""Exact modular block ranks for fixed four-line extensions; exploratory."""
from pathlib import Path
import sys,json,time
from itertools import combinations
from collections import defaultdict,Counter
from functools import lru_cache
import numpy as np
from sympy import Matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
from det7_prolongation import data,quad_weight,var_weight,prolong
from det7_typeB_line_conditions import primitive
from j7_weight_saturation import rank


def prepare(S,arr,sign=1):
 variables,T,blocks,image=data(S,sign);byweight={tuple(w):(block,dim) for w,block,dim in blocks}
 basis=[T[:,:,c] for c in range(T.shape[2])];basisweights=[tuple(-x for x in var_weight(v)) for v in variables]
 starts={}
 for key,inf in arr['line_arrangements'].items():
  i=int(key);w=tuple(inf['weight']);block,dim=byweight[w]
  params=block[:-1] if w in image else block;starts[i]=len(basis)
  for q,v in params:
   M=np.zeros(T.shape[:2],dtype=np.int64);M[q,v]=1;basis.append(M);basisweights.append(w)
 result={}
 for ori,fw in [('A',[tuple(-x for x in quad_weight(q)) for q in S]),('B',[var_weight(v) for v in variables])]:
  nf=len(fw);M=prolong(basis,ori);groups=defaultdict(list)
  for b,w in enumerate(basisweights):
   for j,v in enumerate(fw):groups[tuple(a+c for a,c in zip(w,v))].append(b*nf+j)
  quotient={};base_rank=0
  for weight,cols in groups.items():
   rows=np.flatnonzero(np.any(M[:,cols],axis=1));basecols=[c for c in cols if c//nf<len(variables)]
   B=Matrix(M[np.ix_(rows,basecols)].tolist()) if basecols else Matrix.zeros(len(rows),0)
   null=B.T.nullspace();base_rank+=B.rank()
   H=Matrix([primitive(list(v)) for v in null]) if null else Matrix.zeros(0,len(rows))
   quotient[weight]=(rows,H)
  line_maps={}
  fixed_vectors={}
  for key,inf in arr['line_arrangements'].items():
   i=int(key);w=tuple(inf['weight']);d=inf['quotient_dimension'];line_maps[i]=[]
   for j,v in enumerate(fw):
    weight=tuple(a+c for a,c in zip(w,v));rows,H=quotient[weight]
    C=Matrix(M[np.ix_(rows,[(starts[i]+k)*nf+j for k in range(d)])].tolist())
    Q=H*C
    line_maps[i].append((weight,[[int(x) for x in Q.row(k)] for k in range(Q.rows)]))
   for s,st in enumerate(inf['states']):
    if st['dimension']!=1:continue
    vec=st['kernel'][0]
    fixed_vectors[i,s]=[(weight,tuple(sum(a*b for a,b in zip(row,vec)) for row in Q)) for weight,Q in line_maps[i]]
  @lru_cache(None)
  def increment(choices,fixed_vectors=fixed_vectors):
   byweight=defaultdict(list)
   for choice in choices:
    for w,v in fixed_vectors[choice]:
     if any(v):byweight[w].append(v)
   total=0
   for w,cols in byweight.items():
    total+=rank(list(zip(*cols)))
   return total
  result[ori]={'base_rank':base_rank,'increment':increment,'fixed_vectors':fixed_vectors,'line_maps':line_maps}
 return result


def go(S, sign=1):
 stem=('det_' if sign==-1 else '')+'_'.join(map(str,S));base=Path(__file__).parent
 arr=json.load(open(base/('j7_joint_line_'+stem+'.json')));maps=prepare(S,arr,sign)
 remain=[];counts=Counter();n=0
 for rec in arr['remaining']:
  if rec.get('multiplicity_case'):remain.append(rec);continue
  states=[]
  for case in rec['joint_states']:
   inds=rec['indices'];choices=case['states'];fixed=tuple((i,j) for i,j,d in zip(inds,choices,case['dimensions']) if d==1)
   incA=maps['A']['increment'](fixed);incB=maps['B']['increment'](fixed)
   if incA>16 or incB>24:counts['fixed_rank_excludes']+=1;continue
   if len(fixed)==4:
    counts['fixed_survives']+=1;states.append({**case,'actual_increment_A':incA,'actual_increment_B':incB});continue
   counts['with_parameters_survives']+=1;states.append({**case,'fixed_increment_A':incA,'fixed_increment_B':incB})
  if states:remain.append({**rec,'joint_states':states})
 out={'subset':S,'counts':dict(counts),'remaining':remain}
 (base/('j7_actual_line_rank_'+stem+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(S,dict(counts),'remaining supports',len(remain),flush=True)
 return out

if __name__=='__main__':
 st=time.time()
 for S in [[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]]:go(S)
 print('seconds',time.time()-st)
