#!/usr/bin/env python3
"""Recursive Borel-coordinate border substitution with Koszul leaves.
False means the selected tests did not prove the bound; never an upper bound.
"""
import argparse,json,math,time
from itertools import combinations
from functools import lru_cache
from collections import Counter
from br_linear import tensor,Space,add


def run(S,target=18,maxstates=30000):
 support,U,aw,bw,blocks=tensor(S,-1);weights=[aw,bw,bw]
 entries={(a,b,c):x for c,v in enumerate(U) for (a,b),x in v.items()}
 a=len(S);m=len(support);stats=Counter();start=time.time();proof={}
 from br_linear import RECTS
 belowA=lambda i,j:all(x<=y for I,J in zip(RECTS[S[i]],RECTS[S[j]]) for x,y in zip(I,J))
 belowB=lambda i,j:support[i]//4<=support[j]//4 and support[i]%4<=support[j]%4
 orders=[belowA,belowB,belowB]
 def clean(state):
  E={v:x for v,x in entries.items() if all(v[i] in state[i] for i in range(3))}
  return tuple(tuple(sorted({v[i] for v in E})) for i in range(3)),E
 def koszul(E,state,f,source,p):
  third=3-f-source;space=Space(1000003);vals={c:[] for c in state[source]}
  for v,x in E.items():vals[v[source]].append((v[f],v[third],x))
  for I in combinations(state[f],p):
   iset=set(I)
   for c in state[source]:
    col={}
    for z,o,x in vals[c]:
     if z not in iset:col[tuple(sorted(I+(z,))),o]=(-1)**sum(i<z for i in I)*x
    space.append(col)
  return space.rank(),math.comb(len(state[f])-1,p)
 @lru_cache(None)
 def prove(state,r):
  state,E=clean(state)
  stats['states']+=1
  if stats['states']>maxstates:raise RuntimeError('state budget reached')
  dims=tuple(len(s) for s in state)
  if max(dims,default=0)>=r:return True
  if r<=0:return True
  if not E:return False
  # Untruncated seven-or-more-minor image: inherited exact mu7 propagation.
  if len(state[0])>=7:
   used={b for a,b,c in entries if a in state[0]}
   if used<=set(state[1]) and used<=set(state[2]) and len(state[0])+7>=r:return True
  # Try economical Koszul maps, both orientations.
  candidates=[]
  for f in range(3):
   n=dims[f]
   for source in range(3):
    if f==source:continue
    third=3-f-source
    for p in range(1,min(4,(n-1)//2)+1):
     cost=math.comb(n-1,p)
     nr=math.comb(n,p+1)*dims[third];nc=math.comb(n,p)*dims[source]
     if min(nr,nc)>(r-1)*cost:candidates.append((nc+nr,f,source,p))
  for size,f,source,p in sorted(candidates):
   if size>14000:continue
   rho,cost=koszul(E,state,f,source,p);stats['koszul']+=1
   if rho>(r-1)*cost:
    stats['koszul_success']+=1;proof[str((state,r))]={'type':'koszul','factor':f,'source':source,'p':p,'rank':rho,'cost':cost};return True
  for f in sorted(range(3),key=lambda z:dims[z]):
   if dims[f]<=1:continue
   o=orders[f]
   removable=[i for i in state[f] if not any(i!=j and (o(i,j) if f==0 else o(j,i)) for j in state[f])]
   passed=True
   for i in removable:
    new=list(state);new[f]=tuple(j for j in state[f] if j!=i)
    if not prove(tuple(new),r-1):passed=False;break
   if passed:
    stats['substitution_success']+=1;proof[str((state,r))]={'type':'substitution','factor':f,'removed':removable};return True
  return False
 state=(tuple(range(a)),tuple(range(m)),tuple(range(m)))
 try:ok=prove(state,target);status='PROVED' if ok else 'INCONCLUSIVE'
 except RuntimeError:ok=False;status='BUDGET'
 return {'subset':S,'target':target,'status':status,'stats':dict(stats),'cache':str(prove.cache_info()),'seconds':time.time()-start,'proof_nodes':proof}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+',default=[0,1,2,3,4,5,6,7,8,12]);ap.add_argument('--target',type=int,default=18);ap.add_argument('--maxstates',type=int,default=30000);ap.add_argument('--output');args=ap.parse_args()
 r=run(args.subset,args.target,args.maxstates)
 if args.output:open(args.output,'w').write(json.dumps(r,indent=2)+'\n')
 print(json.dumps({k:v for k,v in r.items() if k!='proof_nodes'}))
