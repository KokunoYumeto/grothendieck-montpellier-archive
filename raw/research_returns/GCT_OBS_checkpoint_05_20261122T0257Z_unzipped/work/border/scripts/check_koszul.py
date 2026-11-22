#!/usr/bin/env python3
"""Exact ranks of residual Koszul maps, independently reconstructed.
The input file supplies only subsets and the choice of factor/exterior degree.
All selected old minors are ignored. All arithmetic is stdlib Q or F_p.
"""
import argparse,json,math,time
from collections import defaultdict,Counter
from itertools import combinations
from br_linear import tensor,Space,varwt,quadwt,neg,NONUNIT_PIVOTS


def koszul(S,sign,along,p,prime):
 support,U,aw,bw,blocks=tensor(S,sign);a=len(S);m=len(support)
 fw=aw if along=='A' else bw;dims=len(fw);spaces=defaultdict(lambda:Space(prime));cols=0
 for I in combinations(range(dims),p):
  iw=tuple(sum(fw[i][k] for i in I) for k in range(8));iset=set(I)
  for c,v in enumerate(U):
   w=tuple(x-y for x,y in zip(iw,bw[c]));out={}
   for (h,b),value in v.items():
    z,other=(h,b) if along=='A' else (b,h)
    if z in iset:continue
    J=tuple(sorted(I+(z,)));sgn=(-1)**sum(i<z for i in I)
    out[J,other]=sgn*value
   spaces[w].append(out);cols+=1
 return sum(s.rank() for s in spaces.values()),len(spaces),math.comb(dims-1,p)


def ideals(size):
 from br_linear import RECTS
 lower=[{q for q in range(36) if q!=z and all(x<=y for I,J in zip(RECTS[q],RECTS[z]) for x,y in zip(I,J))} for z in range(36)]
 layer={frozenset()}
 for _ in range(size):layer={s|{z} for s in layer for z in range(36) if z not in s and lower[z]<=s}
 return sorted(tuple(sorted(s)) for s in layer)


def run(path,prime,mode):
 data=json.load(open(path));sign=-1 if mode=='det' else 1;results=[];start=time.time()
 for no,rec in enumerate(data['records']):
  kind=rec['type'];S=rec['subset']
  if kind not in ('A_koszul','B_koszul','support'):continue
  support,U,aw,bw,blocks=tensor(S,sign)
  if kind=='support':r=len(support);cost=1;num=0
  else:r,num,cost=koszul(S,sign,kind[0],rec['p'],prime)
  result={'subset':S,'type':kind,'p':rec.get('p'),'rank':r,'pure_cost':cost,'lower_bound':(r+cost-1)//cost,'weight_blocks':num}
  results.append(result)
  if len(results)%100==0:print(json.dumps({'done':len(results),'elapsed':round(time.time()-start,1)}),flush=True)
 out={'family':mode,'prime':prime,'results':results,'nonunit_pivots':sorted(NONUNIT_PIVOTS),
      'status':'PASS' if all(r['lower_bound']>=14 for r in results) else 'OPEN','seconds':time.time()-start}
 print(json.dumps({k:v for k,v in out.items() if k!='results'}),flush=True)
 return out


def main():
 ap=argparse.ArgumentParser();ap.add_argument('certificate');ap.add_argument('--prime',type=int,default=0);ap.add_argument('--family',choices=['det','per'],required=True);ap.add_argument('--output');args=ap.parse_args()
 if args.prime:assert args.prime>=2 and all(args.prime%d for d in range(2,int(args.prime**.5)+1))
 result=run(args.certificate,args.prime,args.family)
 if args.output:
  with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
if __name__=='__main__':main()
