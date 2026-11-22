#!/usr/bin/env python3
"""Exact exploratory test of the stronger standard two-factor bound."""
from collections import Counter
from itertools import combinations_with_replacement
from math import lcm
from pathlib import Path
import argparse,datetime,json,time

parser=argparse.ArgumentParser();parser.add_argument('--min-n',type=int,default=15);parser.add_argument('--max-n',type=int,default=20)
args=parser.parse_args();start=time.perf_counter()
def parts(n,maximum=None):
    if not n:yield ();return
    if maximum is None:maximum=n
    for k in range(min(n,maximum),0,-1):
        for p in parts(n-k,k):yield (k,)+p
def spec(p):
    L=lcm(*p);s=Counter()
    for k in p:
        for j in range(k):s[j*(L//k)]+=1
    s[0]-=1
    return L,+s
out=[];all_count=0
for n in range(args.min_n,args.max_n+1):
    entries=[(p,*spec(p)) for p in parts(n)]
    fails=[];count=0;minimum=None;witness=None
    for (p,L,S),(q,M,T) in combinations_with_replacement(entries,2):
        K=2*n-len(p)-len(q)
        if not K:continue
        N=lcm(L,M);prod=Counter()
        for x,v in S.items():
            for y,w in T.items():prod[(x*(N//L)+y*(N//M))%N]+=v*w
        a=n-1;e=a*a;nu=e-max(prod.values())
        gap=2*nu-((n-3)*K+n)
        if minimum is None or gap<minimum:minimum=gap;witness=[p,q,nu,K,N,[z for z,v in prod.items() if v==max(prod.values())]]
        if gap<0 and len(fails)<25:fails.append({'p':p,'q':q,'nu':nu,'K':K,'gap_numerator':gap,'denominator':2,'largest_targets':[[z,N] for z,v in prod.items() if v==max(prod.values())]})
        count+=1
    out.append({'n':n,'partitions':len(entries),'unordered_pairs':count,'minimum_gap_numerator':minimum,'minimum_witness':witness,'failures_first25':fails})
    all_count+=count
    print(json.dumps(out[-1]),flush=True)
result={'status':'REFUTED' if any(x['failures_first25'] for x in out) else 'FINITE PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'seconds':time.perf_counter()-start,
 'range':[args.min_n,args.max_n],'total_unordered_pairs':all_count,'results':out,
 'scope':'All exact scalar eigenspaces for these finite partition pairs only; no universal theorem inferred.'}
path=Path(__file__).with_name('standard_strong_index_test_%s_%s.json'%(args.min_n,args.max_n));path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))
