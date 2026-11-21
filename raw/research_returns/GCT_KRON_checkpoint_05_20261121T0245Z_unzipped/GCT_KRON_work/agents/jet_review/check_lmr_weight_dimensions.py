"""Feasibility counts for the LMR degree12 multiplicity-six module."""
from itertools import product
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,time
source=Path(__file__).with_name('check_hessian_bracket_plethysm.py');ns={'__file__':str(source)}
exec(source.read_text().split('start=time.time()')[0],ns)

def weight_dimension(target,d=12,n=3):
 caps=target[1:];coords=list(product(*(range(c+1) for c in caps)));loc={a:i for i,a in enumerate(coords)};S=len(coords)
 dp=[[0]*S for _ in range(d+1)];dp[0][loc[(0,)*len(caps)]]=1;sums=[sum(a) for a in coords]
 generators=[a for a in product(range(n+1),repeat=len(caps)) if sum(a)<=n and all(a[i]<=caps[i] for i in range(len(caps)))]
 for g in generators:
  pairs=[]
  for idx,a in enumerate(coords):
   if all(x>=y for x,y in zip(a,g)):pairs.append((idx,loc[tuple(x-y for x,y in zip(a,g))]))
  for degree in range(1,d+1):
   current,previous=dp[degree],dp[degree-1]
   for dest,src in pairs:
    if n*degree-sums[dest]<=target[0]:current[dest]+=previous[src]
 return dp[d][loc[caps]],len(generators),S*(d+1)

lam=(19,7,2,2,2,2,2);shapes=[lam]
for i in range(6):
 q=list(lam);q[i]+=1;q[i+1]-=1;shapes.append(tuple(q))
records=[];done={};start=time.time()
for target in shapes:
 canonical=tuple(sorted(target,reverse=True))
 if canonical not in done:done[canonical]=weight_dimension(canonical)
 dim,gens,states=done[canonical]
 records.append({'weight':target,'canonical_weight':canonical,'weight_space_dimension':dim,'admissible_cubic_generators':gens,'DP_grid_states':states})
 print(json.dumps(records[-1]),flush=True)
chi=ns['character'];powers=ns['plethysm_power'](12)
a=sum((coef*chi(lam,cyc) for cyc,coef in powers.items()),Fraction(0))
assert a.denominator==1 and a==6
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','source':'Landsberg-Manivel-Ressayre, section3.2 p476; requested lambda12omega1+5omega2+2omega7=(19,7,2^5)','status':'PASS','method':'Exact unbounded monomial-knapsack counts in Sym12 Sym3 C7, each cubic generator processed once; all six adjacent raising targets counted. Ambient multiplicity independently evaluated by exact wreath cycleindex and Murnaghan-Nakayama.','ambient_multiplicity':int(a),'cycle_index_types':len(powers),'records':records,'elapsed_seconds':time.time()-start}
p=Path(__file__).with_name('lmr_weight_dimensions_certificate.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'ambient_multiplicity':int(a),'elapsed_seconds':time.time()-start,'certificate':str(p)}),flush=True)
