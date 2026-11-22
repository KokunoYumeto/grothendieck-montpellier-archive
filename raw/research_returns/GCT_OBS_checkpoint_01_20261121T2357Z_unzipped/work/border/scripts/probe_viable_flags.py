#!/usr/bin/env python3
"""Exact Borel viable-flag tests for fixed extension spaces.
Uses CHL Proposition 2.4: a border-r span admits a Borel-invariant flag whose
j-dimensional tautological tensor has border rank <=j. OPEN parameter families
are retained explicitly, never sampled.
"""
import argparse,json,time
from collections import Counter
from itertools import combinations
from br_linear import Space,add
from borel_quiver import module,ab_module,successors,extension_vectors
from probe_coupled_borel import enumerate_ab


def lower_bound(F,a,b,target,M):
 usedA={i for v in F for i,j in v};usedB={j for v in F for i,j in v}
 lower=max(len(F),len(usedA),len(usedB))
 if lower>target:return lower,'support'
 # Koszul tests on the original two matrix factors.
 from probe_extension_koszul import koszul
 for factor in (1,2):
  for p in (1,2):
   if p>= (a if factor==1 else b):continue
   t=koszul(F,M,factor,0,p)
   if t['lower']>target:return t['lower'],'factor_'+str(factor)+'_p'+str(p)
 # Koszul along the flag-label factor; matrix columns indexed by B.
 n=len(F)
 for p in range(1,min(3,(n-1)//2)+1):
  import math
  cost=math.comb(n-1,p);R=Space(1000003)
  for I in combinations(range(n),p):
   for c in usedB:
    out={}
    for h,v in enumerate(F):
     if h in I:continue
     for (z,k),x in v.items():
      if k==c:out[tuple(sorted(I+(h,))),z]=(x.numerator*pow(x.denominator,-1,1000003)%1000003)*((-1)**sum(i<h for i in I))
    R.append(out)
  value=(R.rank()+cost-1)//cost
  if value>target:return value,'koszul_'+str(p)
 return lower,'inconclusive'


def check(E,AM,maxlevel=17):
 a=len(AM['subset']);b=len(AM['support']);wt=lambda ab:add(AM['aw'][ab[0]],AM['bw'][ab[1]])
 M=module([],E,wt,AM['actions']);states={tuple(() for _ in M['blocks'])};branches=[];history=[]
 for j in range(1,min(len(E),maxlevel)+1):
  nxt=set()
  for F in states:
   rigid,params=successors(M,F);nxt.update(rigid)
   branches.extend((j,F,i,K) for i,K in params)
  states=set();counts=Counter()
  for F in nxt:
   vectors=extension_vectors(M,F);lower,kind=lower_bound(vectors,a,b,j,AM)
   if lower>j:counts[kind]+=1
   else:states.add(F)
  history.append({'level':j,'candidates':len(nxt),'survivors':len(states),'excluded':dict(counts),'parameter_branches':len(branches)})
  print(history[-1],flush=True)
  if not states:break
 return {'history':history,'survivors':len(states),'parameter_branches':len(branches),'status':'EXCLUDED' if not states and not branches else 'OPEN'}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+',default=[0,1,2,3,4,5,6,7,8,12]);ap.add_argument('--candidate',type=int);ap.add_argument('--maxlevel',type=int,default=17);ap.add_argument('--output');args=ap.parse_args()
 t=time.time();M=ab_module(args.subset);Es,fams,hist=enumerate_ab(M,17);results=[]
 for i,E in enumerate(Es):
  if args.candidate is not None and args.candidate!=i:continue
  print('CANDIDATE',i,flush=True);r=check(E,M,args.maxlevel);r['candidate']=i;results.append(r)
 out={'subset':args.subset,'AB_families':len(fams),'AB_history':hist,'results':results,'seconds':time.time()-t}
 if args.output:open(args.output,'w').write(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out))
