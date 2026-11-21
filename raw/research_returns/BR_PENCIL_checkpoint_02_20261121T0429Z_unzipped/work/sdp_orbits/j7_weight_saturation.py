"""Exploratory exact finite-field torus saturation tests; no final theorem claim."""
from pathlib import Path
import sys,json,time
from itertools import combinations
from collections import defaultdict
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pencil'))
import per5_prolongation_certificate as p
from functools import lru_cache

def rank(M, prime=1000003):
 A=[list(map(lambda x:int(x)%prime,row)) for row in M]
 if not A:return 0
 r=0
 for c in range(len(A[0])):
  rr=next((i for i in range(r,len(A)) if A[i][c]),None)
  if rr is None:continue
  A[r],A[rr]=A[rr],A[r];v=pow(A[r][c],-1,prime)
  A[r]=[(x*v)%prime for x in A[r]]
  for i in range(r+1,len(A)):
   if A[i][c]:
    v=A[i][c];A[i]=[(x-v*y)%prime for x,y in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def go(S, sign=1):
 prefix="det_" if sign==-1 else ""
 pairs=list(combinations(range(4),2));p.A_DIM=7
 p.RECTANGLES=[(pairs[z//6],pairs[z%6]) for z in S]
 T=p.tensor()
 if sign==-1:
  for q,((r,s),(c,d)) in enumerate(p.RECTANGLES):
   x,y=3*r+d,3*s+c;T[q,x,y]=T[q,y,x]=-1
 classes,image=p.weights()
 weights=[(w,b) for w,b in classes.items() if len(b)-(w in image)>0]
 caps=[len(b)-(w in image) for w,b in weights]
 basis=[T[:,:,c] for c in range(9)]; bw=[tuple(-x for x in p.weight_var(*v)) for v in p.VARIABLES]; owner=[-1]*9
 for wi,(w,b) in enumerate(weights):
  if w in image:
   vec=T[:,:,image[w]];pivot=next((q,v) for q,v in b if vec[q,v])
  else:pivot=None
  for q,v in b:
   if (q,v)==pivot:continue
   M=np.zeros((7,9),dtype=np.int64);M[q,v]=1
   basis.append(M);bw.append(w);owner.append(wi)
 assert len(basis)==63
 evaluators={};stats={}
 for ori in ['A','B']:
  fw=[tuple(-x for x in p.weight_quad(*rect)) for rect in p.RECTANGLES] if ori=='A' else [p.weight_var(*v) for v in p.VARIABLES]
  n=len(fw);M=p.prolongation_matrix(basis,ori)
  cg=defaultdict(list)
  for j,w in enumerate(bw):
   for i,u in enumerate(fw):cg[tuple(a+b for a,b in zip(w,u))].append(j*n+i)
  blocks=[]
  for w,cols in cg.items():
   rows=np.flatnonzero(np.any(M[:,cols],axis=1));B=M[np.ix_(rows,cols)]
   own=[owner[c//n] for c in cols];optional=sorted(set(own)-{-1});bitpositions={a:i for i,a in enumerate(optional)}
   ownerslocal=[-1 if o==-1 else bitpositions[o] for o in own]
   lookup={}
   # Precompute only local patterns of at most four selected global weights.
   for size in range(min(4,len(optional))+1):
    for chosen in combinations(range(len(optional)),size):
     mask=sum(1<<j for j in chosen);C=[j for j,o in enumerate(ownerslocal) if o<0 or mask>>o&1]
     lookup[mask]=len(C)-rank(B[:,C])
   blocks.append((optional,lookup))
  def evaluator(mask,blocks=blocks):
   total=0
   for optional,lookup in blocks:
    local=sum(((mask>>j)&1)<<i for i,j in enumerate(optional));total+=lookup[local]
   return total
  evaluators[ori]=evaluator;stats[ori]={'blocks':len(blocks),'patterns':sum(len(d) for _,d in blocks),'max_optional':max(len(a) for a,_ in blocks)}
 print('prepared',S,stats,flush=True)
 remain=[];count=0;by_size={}
 for size in range(1,5):
  nrem=0
  for inds in combinations(range(len(weights)),size):
   if sum(caps[i] for i in inds)<4:continue
   count+=1;mask=sum(1<<i for i in inds)
   da=evaluators['A'](mask)
   if da<13:continue
   db=evaluators['B'](mask)
   if db<13:continue
   remain.append({'indices':inds,'maxdim':9+sum(caps[i] for i in inds),'dimA':da,'dimB':db});nrem+=1
  by_size[size]=nrem;print('size',size,'remaining',nrem,flush=True)
 result={'subset':S,'weights':[{'weight':w,'block':b,'capacity':cap} for (w,b),cap in zip(weights,caps)],'count':count,'remaining':remain,'by_size':by_size,'blocks':stats}
 Path(__file__).with_name('j7_saturation_'+prefix+('_'.join(map(str,S)))+'.json').write_text(json.dumps(result,indent=2)+'\n')
 print('done',S,count,len(remain),flush=True)
 return result

if __name__=='__main__':
 st=time.time()
 for S in [[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]]:go(S)
 print('seconds',time.time()-st)
