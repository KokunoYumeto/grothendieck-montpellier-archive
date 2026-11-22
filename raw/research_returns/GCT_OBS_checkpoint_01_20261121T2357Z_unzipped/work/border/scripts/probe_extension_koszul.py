#!/usr/bin/env python3
"""Higher Koszul equations for the limiting rank-r AB extension itself."""
import argparse,json,math,time
from collections import defaultdict
from itertools import combinations
from br_linear import Space,neg,add
from borel_quiver import ab_module
from probe_coupled_borel import enumerate_ab


def koszul(E,M,f,source,p):
 prime=1000003;a=len(M['subset']);b=len(M['support']);ew=[];T={}
 for h,v in enumerate(E):
  x=next(iter(v));w=add(M['aw'][x[0]],M['bw'][x[1]]);assert all(add(M['aw'][i],M['bw'][j])==w for i,j in v)
  ew.append(neg(w))
  for (i,j),v0 in v.items():T[h,i,j]=v0.numerator*pow(v0.denominator,-1,prime)%prime if hasattr(v0,'denominator') else v0
 weights=[ew,M['aw'],M['bw']];dims=[len(E),a,b];third=3-f-source
 vals=defaultdict(list)
 for v,x in T.items():vals[v[source]].append((v[f],v[third],x))
 spaces=defaultdict(lambda:Space(prime))
 for I in combinations(range(dims[f]),p):
  iset=set(I);wI=tuple(sum(weights[f][i][z] for i in I) for z in range(8))
  for c in range(dims[source]):
   w=tuple(x-y for x,y in zip(wI,weights[source][c]));col={}
   for z,o,x in vals[c]:
    if z not in iset:col[tuple(sorted(I+(z,))),o]=x*((-1)**sum(i<z for i in I))
   spaces[w].append(col)
 r=sum(s.rank() for s in spaces.values());cost=math.comb(dims[f]-1,p)
 return {'factor':f,'source':source,'p':p,'rank':r,'cost':cost,'lower':(r+cost-1)//cost}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+',default=[0,1,2,3,4,5,6,7,8,12]);ap.add_argument('--output');args=ap.parse_args()
 start=time.time();M=ab_module(args.subset);Es,fams,hist=enumerate_ab(M,17);results=[]
 for i,E in enumerate(Es):
  tests=[];done=False
  for f in (1,2):
   for p in range(1,(len(M['subset']) if f==1 else len(M['support']))//2):
    for source in (0,3-f):
     t=koszul(E,M,f,source,p);tests.append(t);print('E',i,t,flush=True)
     if t['lower']>17:done=True;break
    if done:break
   if done:break
  results.append({'candidate':i,'excluded':done,'tests':tests})
 out={'subset':args.subset,'AB_history':hist,'AB_families':len(fams),'results':results,'seconds':time.time()-start}
 if args.output:open(args.output,'w').write(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out),flush=True)
