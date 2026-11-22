#!/usr/bin/env python3
"""Independent integral projections in A followed by middle Koszul maps.
Discovery uses seeded stdlib random; certificates retain the full matrix.
"""
import random,json,time,math
from itertools import combinations
from br_linear import tensor,Space
from check_koszul import ideals

def projected_rank(S,P,p,prime=1000003):
 support,U,aw,bw,blocks=tensor(S,-1);d=len(P);out=Space(prime)
 for I in combinations(range(d),p):
  si=set(I)
  for v in U:
   col={}
   for (h,b),x in v.items():
    for z in range(d):
     if z in si or not P[z][h]:continue
     key=(tuple(sorted(I+(z,))),b)
     col[key]=col.get(key,0)+x*P[z][h]*(-1)**sum(i<z for i in I)
   out.append(col)
 return out.rank()

def main():
 start=time.time();out=[]
 for S in ideals(10):
  if S>tuple(sorted(q%6*6+q//6 for q in S)):continue
  best=0;cert=None
  for d in (3,5):
   p=(d-1)//2;cost=math.comb(d-1,p)
   for seed in range(3):
    rng=random.Random(20261122+sum(1<<q for q in S)+seed*97+d)
    P=[[rng.randrange(-3,4) for q in S] for i in range(d)]
    r=projected_rank(S,P,p);lo=(r+cost-1)//cost;best=max(best,lo)
    if lo>=18:cert={'subset':list(S),'projection':P,'p':p,'rank':r,'cost':cost,'lower':lo,'prime':1000003};break
   if cert:break
  row={'subset':list(S),'best':best,'certificate':cert};out.append(row);print(json.dumps({'subset':list(S),'best':best}),flush=True)
  with open('certificates/det10_projected_koszul.json','w') as f:json.dump({'results':out,'seconds':time.time()-start},f,indent=2)

if __name__=='__main__':main()
