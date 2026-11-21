#!/usr/bin/env python3
"""Necessary finite surjectivity tests, independent of GT-kernel rigidity."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from krammer_f9_probe import to3
from krammer_first_pair import inv,mul

ROOT=Path(__file__).parent
def action(gs):
 d=len(gs[0]);vs=[tuple(v) for v in np.eye(d,dtype=np.int16)];idx={v:j for j,v in enumerate(vs)}
 for v in vs:
  for g in gs:
   w=tuple(map(int,g@v%3))
   if w not in idx:idx[w]=len(vs);vs.append(w)
 arr=np.array(vs,dtype=np.int16).T
 def perm(g):return Permutation([idx[tuple(map(int,v))] for v in (g@arr%3).T])
 return perm, len(vs)

def run():
 st=time.monotonic();d=json.loads((ROOT.parent/'characters/records/krammer_mixed_correlation.json').read_text())
 raw=lambda a:to3(np.array(a)).astype(np.int16)
 C=raw(d['C_full']);Ci=inv(C);Q=raw(d['Q_full']);Qi=inv(Q)
 targets=[]
 for record in d['pairs']:
  B=raw(record['splitting_basis']);Bi=inv(B);parts=[]
  for name in ['solvable','unitary']:
   gs=list(map(raw,record[name+'_generators']));perm,degree=action(gs)
   order=int(PermutationGroup([perm(g) for g in gs]).order());expected=108 if name=='solvable' else 24192;assert order==expected
   parts.append((name,gs,perm,degree,expected))
  targets.append((record['pair'],B,Bi,parts))
 sol=np.load(ROOT/'krammer_pentagon_solutions.npz');rows=[];cache={};counts={}
 for index,(R,label) in enumerate(zip(sol['R'],sol['labels'])):
  R=R.astype(np.int16);r=mul(mul(Ci,R),C);F45=mul(mul(mul(Qi,r),Q),inv(r));checks=[]
  for value,(pair,B,Bi,parts) in zip([R,F45],targets):
   block=mul(mul(Bi,value),B)
   for j,(name,gs,perm,degree,expected) in enumerate(parts):
    f=block[6*j:6*j+6,6*j:6*j+6];key=(tuple(pair),name,f.astype(np.int8).tobytes())
    if key not in cache:
     changed=mul(mul(inv(f),gs[1]),f);order=int(PermutationGroup([perm(gs[0]),perm(changed)]).order());cache[key]=order
    order=cache[key];checks.append({'pair':pair,'block':name,'order':order,'expected':expected,'pass':order==expected})
  passed=all(c['pass'] for c in checks);lab=str(tuple(map(int,label)));counts.setdefault(lab,[0,0]);counts[lab][int(passed)]+=1
  rows.append({'index':index,'label':list(map(int,label)),'pass':passed,'checks':checks})
 out={'statement':'D23.P14 generation component','scope':'Necessary q∘Φ surjectivity for actual gentle Φ; no invariance of kerq or representation rigidity assumed.','counts_fail_pass':counts,'distinct_group_order_checks':len(cache),'rows':rows,'elapsed_seconds':time.monotonic()-st}
 (ROOT/'krammer_gentle_generation.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

if __name__=='__main__':run()
