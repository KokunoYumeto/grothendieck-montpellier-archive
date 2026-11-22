#!/usr/bin/env python3
"""Recompute BR-004 from the signed 2x2 minor formulas, using only stdlib.

No inherited ranks, fixed spaces, or chosen minors are read.  Exact rational
arithmetic enumerates Borel-invariant flags in (A tensor B)/T(C*).  Higher
Koszul ranks are computed over F_1000003; a nonzero minor there is also
nonzero over Q, since every rational denominator is explicitly inverted.
Projective kernels of dimension >1 are exported in full and left OPEN.

Usage: python scripts/check_det10_gate.py --output certificates/det10_gate.json
"""
import argparse,json,time,math
from pathlib import Path
from collections import Counter,defaultdict
from br_linear import Space,rank
from borel_quiver import ab_module,successors,extension_vectors,linear_apply
from probe_coupled_borel import wedge_ranks
from probe_extension_koszul import koszul
from check_koszul import ideals
from probe_projected_koszul import projected_rank

PRIME=1000003
assert all(PRIME%d for d in range(2,math.isqrt(PRIME)+1))

def encode_vector(v):
 return [[list(i) if isinstance(i,tuple) else i,str(x)] for i,x in sorted(v.items())]

def encode_flag(F):
 return [{'weight_block':i,'rows':[encode_vector(dict(v)) for v in rows]}
         for i,rows in enumerate(F) if rows]

def verify_module(M):
 s=Space()
 for v in M['U']:s.append(v)
 assert s.rank()==len(M['support'])
 for v in M['U']:
  for action in M['actions']:
   assert not s.reduce(linear_apply(v,action)), 'T(C*) is not invariant'
 for w,basis in M['blocks']:
  assert all(v for v in basis)

def run(S,r=17):
 start=time.time();M=ab_module(S);verify_module(M)
 a=len(S);b=len(M['support']);q=r-b
 assert q>=0
 states={tuple(() for _ in M['blocks'])};families=[];history=[];exclusions=[]
 for level in range(1,q+1):
  nxt=set()
  for F in sorted(states):
   rigid,params=successors(M,F);nxt.update(rigid)
   for i,K in params:
    families.append({'level':level,'flag_before':encode_flag(F),'weight_block':i,
                     'weight':M['blocks'][i][0],'projective_dimension':len(K)-1,
                     'kernel_basis':[encode_vector(v) for v in K]})
  states=set();counts=Counter()
  for F in sorted(nxt):
   E=M['U']+extension_vectors(M,F);assert rank(E)==b+level
   rs=wedge_ranks(E,a,b)
   if rs['A']>(a-1)*r or rs['B']>(b-1)*r:
    counts['first_wedge']+=1
    exclusions.append({'level':level,'flag':encode_flag(F),'test':'first_wedge','ranks':rs})
    continue
   done=False
   for f,dim in ((2,b),(1,a)):
    for p in (2,3):
     if len(E)*dim<=r*(dim-p):continue
     t=koszul(E,M,f,0,p,PRIME)
     if t['lower']>r:
      done=True;counts['higher_koszul']+=1
      exclusions.append({'level':level,'flag':encode_flag(F),'test':'higher_koszul',**t})
      break
    if done:break
   if not done:states.add(F)
  history.append({'level':level,'generated':len(nxt),'remaining':len(states),
                  'excluded':dict(counts),'parameter_branches_so_far':len(families)})
  if not states:break
 out={'subset':list(S),'transpose':sorted(q%6*6+q//6 for q in S),
      'support':M['support'],'history':history,'prime':PRIME,
      'quotient_weight_blocks':[{'weight':w,'basis':[encode_vector(v) for v in B]} for w,B in M['blocks']],
      'surviving_flags':[encode_flag(F) for F in sorted(states)],
      'surviving_extensions':[[encode_vector(v) for v in extension_vectors(M,F)] for F in sorted(states)],
      'parameter_branches':families,'exclusions':exclusions,
      'status':'EXCLUDED' if not states and not families else 'OPEN','seconds':time.time()-start}
 print(json.dumps({'subset':list(S),'status':out['status'],'rigid_survivors':len(states),'parameter_branches':len(families)}),flush=True)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--subset',type=int,nargs='+');ap.add_argument('--output',default='certificates/det10_gate.json');args=ap.parse_args()
 allcases=ideals(10);assert len(allcases)==59
 cases=[tuple(args.subset)] if args.subset else [S for S in allcases if S<=tuple(sorted(q%6*6+q//6 for q in S))]
 results=[];start=time.time()
 for S in cases:
  results.append(run(S))
  with open(args.output,'w') as f:json.dump({'claim':'BR-004','scope':'characteristic zero','results':results},f,indent=2)
 excluded=set();open_cases=set()
 for row in results:
  dest=excluded if row['status']=='EXCLUDED' else open_cases
  dest.add(tuple(row['subset']));dest.add(tuple(row['transpose']))
 extension_excluded=set(excluded);projection_checks=[]
 if not args.subset:
  assert excluded.isdisjoint(open_cases)
  assert excluded|open_cases==set(allcases)
  assert (len(excluded),len(open_cases))==(32,27)
  inputs=json.loads((Path(__file__).resolve().parent.parent/'certificates/det10_projection_inputs.json').read_text())['records']
  for rec in inputs:
   S=rec['subset'];P=rec['projection'];p=rec['p'];rk=projected_rank(S,P,p,PRIME);cost=math.comb(len(P)-1,p)
   assert rk>17*cost
   projection_checks.append({**rec,'rank':rk,'pure_cost':cost,'prime':PRIME})
   for ss in (tuple(S),tuple(sorted(q%6*6+q//6 for q in S))):
    excluded.add(ss);open_cases.discard(ss)
  assert (len(excluded),len(open_cases))==(36,23)
 out={'claim':'BR-004','scope':'characteristic zero','prime':PRIME,
      'status':'PASS','extension_excluded_subsets':sorted(extension_excluded),
      'projected_koszul_checks':projection_checks,
      'excluded_subsets':sorted(excluded),'remaining_subsets':sorted(open_cases),
      'representatives':len(results),'results':results,'seconds':time.time()-start}
 with open(args.output,'w') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:v for k,v in out.items() if k!='results'}),flush=True)

if __name__=='__main__':main()
