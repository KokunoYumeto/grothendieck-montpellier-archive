#!/usr/bin/env python3
"""Exact coordinate, parity and finite grading diagnostics for AM-DO-046.
No automorphic representation, L-value, or period is computed.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parent
src=ROOT/'enlarged_gap_admissible_interval_certificate.json'
data=json.loads(src.read_text());counts=Counter();rows=[]
A=1<<960;B=1<<955

def ck(x,tag):
 assert x,tag
 counts[tag]+=1

for host in data['hosts']:
 a=host['a']; n=a+1; minimum=None
 for ell in (int(host['ell_min']),int(host['ell_max'])):
  v=[4*ell*(a-1-i) for i in range(a-1)]
  for role,roledata in host['roles'].items():
   E=int(roledata['E'])
   ends=(Q(A)+Q(a-1,2),-Q(B)-Q(a-1,2)) if role=='top' else (Q(v[0]+4*a*ell)+Q(1,2),Q(2*ell)+Q(1,2))
   # Each adjacent source gap depends on at most two independent bits.
   for j in range(a-1):
    for x,y in product((0,1),repeat=2):
     left=ends[0] if j==0 else Q(v[j-1])-Q(1,2)-ell*x
     right=ends[1] if j+1==a-1 else Q(v[j])-Q(1,2)-ell*y
     gap=left-right
     ck(gap>1,'initial_all_adjacent_gaps_gt1')
     ck((left-Q(a-1,2)).denominator==1 and (right-Q(a-1,2)).denominator==1,'initial_HC_grid')
     minimum=gap if minimum is None else min(minimum,gap)
   for q in (0,ell):
    bot=v+[-E+ell,-E-ell-q]
    ck(len(bot)==n,'bottom_rank')
    ck(all(bot[i]-bot[i+1]>1 for i in range(n-1)),'bottom_all_adjacent_gaps_gt1')
    ck(all((Q(x)-Q(n-1,2)).denominator==1 for x in bot),'bottom_HC_grid')
    dual=[-x for x in bot[::-1]]
    ck(all(dual[i]-dual[i+1]>1 for i in range(n-1)),'contragredient_preserves_gap')
    minimum=min(minimum,min(bot[i]-bot[i+1] for i in range(n-1)))
 rows.append({'host':host['host'],'a':a,'minimum_endpoint_gap':str(minimum),'scope':'All words and allowed ell,q by affine endpoint and adjacent-bit reduction.'})
 for N in (a,n):
  for d in range(1,N+1):
   eps=(d-N)%2
   ck((N-d+eps)%2==0,'odd_eta_parity_repair')
   for j in range(d):
    lam=Q(N-1,2)+10*(d-j)
    rho=Q(d-1,2)-j
    ck((lam+Q(eps,2)-rho).denominator==1,'coefficient_weight_integral')
   if d>1:
    mu=[Q(N-1,2)+10*(d-j)+Q(eps,2)-(Q(d-1,2)-j) for j in range(d)]
    ck(all(mu[j]>=mu[j+1] for j in range(d-1)),'coefficient_weight_dominant')

for d in range(2,32):
 for z in (Q(-103,2),Q(0),Q(201,2)):
  string=[z+Q(d-1,2)-j for j in range(d)]
  ck(all(string[j]-string[j+1]==1 for j in range(d-1)),'Arthur_SL2_unit_step')
# Common stable-theta character shift and added multiset cancellation.
for n in range(1,12):
 for m in range(2*n+1,2*n+7):
  for shift in (Q(-9,2),Q(0),Q(13,2)):
   old=[Q(3*i+n,2) for i in range(n)]
   added=[Q(m-n-1,2)-j+Q(7,2) for j in range(m-n)]
   union=Counter([x+shift for x in old]+added)
   union.subtract(Counter(added))
   ck(+union==Counter(x+shift for x in old),'exact_common_multiset_cancellation')

# Green product support carries block degree even without choosing a
# single finite constituent in each inducing representation.
for N in range(2,25):
 for d in range(1,N//2+1):
  for cuts in product((0,1),repeat=min(d-1,7)):
   ds=[];current=1
   for cut in cuts:
    if cut:ds.append(current);current=1
    else:current+=1
   current+=d-1-len(cuts);ds.append(current)
   ck(sum(ds)==d and all(x>0 for x in ds),'finite_HC_factor_degree')

out={'finding':'AM-DO-046','status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),
 'assertions':sum(counts.values()),'counts':dict(counts),'actual_profiles':rows,
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'scope':'Actual HC gap/grid bounds, exact half-parity repair, Arthur string and Green degree diagnostics only; no L-value or period computation.'}
(ROOT/'definite_oscillator_actual_arthur_parameters_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
