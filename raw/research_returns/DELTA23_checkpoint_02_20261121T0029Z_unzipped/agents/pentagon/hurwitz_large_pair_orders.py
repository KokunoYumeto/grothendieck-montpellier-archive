#!/usr/bin/env python3
"""Complete the previously bounded large-component order inventory.

The only intended use is a prime-support certificate for common-quotient
arguments. A timed-out component remains unknown, never counted as passed.
"""
import json,pathlib,time,signal,multiprocessing as mp
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent

def job(arg):
 pair,oi,pp=arg;st=time.monotonic()
 def alarm(*unused):raise TimeoutError
 signal.signal(signal.SIGALRM,alarm);signal.alarm(20)
 try:
  g=PermutationGroup([Permutation(list(p)) for p in pp]);order=int(g.order());rest=order
  for prime in [2,3]:
   while rest%prime==0:rest//=prime
  out={'pair':pair,'component':oi,'degree':len(pp[0]),'order':order,'prime_to_six_part':rest,'status':'EXACT'}
 except TimeoutError:out={'pair':pair,'component':oi,'degree':len(pp[0]),'status':'TIMEOUT_NO_CONCLUSION'}
 finally:signal.alarm(0)
 out['seconds']=time.monotonic()-st;return out

def run():
 st=time.monotonic();ps=np.load(ROOT/'hurwitz_cubic_ssrr.npz')['generators'];co=lambda a,b:a[b];x=[co(a,a) for a in ps]
 for a in [co(co(ps[0],ps[1]),ps[0]),co(co(ps[2],ps[1]),ps[2])]:x.append(co(a,a))
 jobs=[]
 for i,j in [(0,1),(2,3),(3,4)]:
  seen=set();orbs=[]
  for a in range(len(x[0])):
   if a in seen:continue
   orb=[a];seen.add(a)
   for v in orb:
    for g in (x[i],x[j]):
     w=int(g[v])
     if w not in seen:seen.add(w);orb.append(w)
   orbs.append(orb)
  for oi,orb in enumerate(sorted(orbs,key=len)):
   if len(orb)<=216:continue
   vi={v:k for k,v in enumerate(orb)};pp=tuple(tuple(vi[int(g[v])] for v in orb) for g in (x[i],x[j]))
   jobs.append(([i+1,j+1],oi,pp))
 rows=[];log=ROOT/'hurwitz_cubic_large_pair_orders.jsonl';log.write_text('')
 with mp.Pool(4) as pool:
  for row in pool.imap_unordered(job,jobs):
   rows.append(row)
   with log.open('a') as f:f.write(json.dumps(row)+'\n')
   print(json.dumps(row),flush=True)
 out={'input':'hurwitz_cubic_ssrr.npz','large_component_count':len(jobs),'components':sorted(rows,key=lambda r:(r['pair'],r['component'])),'all_exact_six_primary':all(r['status']=='EXACT' and r['prime_to_six_part']==1 for r in rows),'elapsed_seconds':time.monotonic()-st}
 (ROOT/'hurwitz_cubic_large_pair_orders.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='components'}),flush=True)

if __name__=='__main__':run()
