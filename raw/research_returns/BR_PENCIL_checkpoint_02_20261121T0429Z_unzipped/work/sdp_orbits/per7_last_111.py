"""Exact AB/AC degree111 intersection test for eight candidate extensions."""
from pathlib import Path
import json,sys,time
from collections import defaultdict,Counter
import numpy as np
from sympy import Matrix
from per7_last_joint import setup,S
from check_support9_sevenplanes import rank_q
from det7_prolongation import var_weight,quad_weight


def extension(v,U0):
 X=np.zeros(U0[0].shape,dtype=np.int64);X[2,v]=1
 return U0+[X]


def tensor_columns(E,orientation):
 cols=[]
 for M in E:
  for j in range(11):
   V=np.zeros((7,11,11),dtype=np.int64)
   if orientation=='AB':V[:,:,j]=M
   else:V[:,j,:]=M
   cols.append(V.reshape(-1))
 return np.stack(cols,axis=1)


def main():
 variables,T,blocks,image,U,U0,coordinate=setup();vs=[1,2,3,5,6,7,9,10];aw=[tuple(-x for x in quad_weight(q)) for q in S];bw=[var_weight(v) for v in variables]
 baselineweights=[tuple(-x for x in b) for b in bw]+[tuple(x+y for x,y in zip(aw[2],bw[8]))]
 columns={};weights={}
 for v in vs:
  E=extension(v,U0);ew=baselineweights+[tuple(x+y for x,y in zip(aw[2],bw[v]))]
  cw=[tuple(x+y for x,y in zip(w,b)) for w in ew for b in bw]
  weights[v]=cw
  for ori in ['AB','AC']:columns[v,ori]=tensor_columns(E,ori)
 records=[];counts=Counter()
 for v in vs:
  for w in vs:
   M=np.hstack([columns[v,'AB'],columns[w,'AC']]);cg=defaultdict(list)
   for j,weight in enumerate(weights[v]+weights[w]):cg[weight].append(j)
   r=0
   for target,cs in cg.items():
    rs=np.flatnonzero(np.any(M[:,cs],axis=1));r+=rank_q(M[np.ix_(rs,cs)].tolist())
   dim=286-r;counts[dim]+=1;rec={'AB_extra_variable':v,'AC_extra_variable':w,'intersection_dimension':dim};records.append(rec)
   if dim>=13:print('SURVIVES',rec,flush=True)
 print('intersection dimensions',dict(counts),flush=True)
 Path(__file__).with_name('per7_last_111.json').write_text(json.dumps({'subset':S,'records':records,'dimension_counts':dict(counts)},indent=2)+'\n')

if __name__=='__main__':
 st=time.time();main();print('seconds',time.time()-st)
