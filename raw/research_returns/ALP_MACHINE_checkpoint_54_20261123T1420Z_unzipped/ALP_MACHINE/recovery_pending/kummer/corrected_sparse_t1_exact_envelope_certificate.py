#!/usr/bin/env python3
"""Corrected independent sparse-column envelope: actual zero-target coarea, t1.

AM-DO-070-C1 adds the exact factor2 for the active type-III place.
The original script and result are preserved; this is a separate correction copy.

This is an arithmetic diagnostic. It does not establish whole-profile removal,
replay an old error list, or substitute for the accompanying geometric proof.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb,isqrt
from datetime import datetime,timezone
import argparse,json,hashlib

ap=argparse.ArgumentParser()
ap.add_argument('--output',required=True,type=Path)
args=ap.parse_args()
p=Path('/tmp/alpa66/work/recovery_pending').resolve()
if p not in args.output.resolve().parents:raise ValueError('pending-only output')
checks=[]
def ck(b,n):
 if not b:raise AssertionError(n)
 checks.append(n)
def ceil_log2_ratio(n,d):
 assert n>0 and d>0
 e=n.bit_length()-d.bit_length()
 def above(e):
  return n<=d*(1<<e) if e>=0 else n*(1<<(-e))<=d
 while not above(e):e+=1
 while above(e-1):e-=1
 ck(above(e) and not above(e-1),'exact_two_sided_log_ceiling')
 return e
f=168;m=164;s=11;c=F(2250,7)
D0=7**140*29**144*5**84*13**84
ck(60**168<2**995 and 2**996<61**168,'actual_T_root_between60and61')
ck(c==F(72*1500,336),'scalar_fractional_cover_constant')
# Actual position count binom(m,k) is in each rational volume below.
C=(1+9850+1945+5022+168+22+668
 +F(669*f,4)*F(113,16)-F(281,4)*335*167
 +f*(F(9,2)-F(959,4)))
# Actual zero-target weighted fibre correction: 2^t with t=1.
C += 1
rows=[]
for k in range(1,m+1):
 qpow=(F(665,4)-k)*f
 ck(qpow.denominator==1 and qpow>0,'positive_sparse_monotone_exponent')
 if k<=60:
  scale=1<<24
  rnum=isqrt((k*scale*scale)//60)
  if rnum*rnum*60<k*scale*scale:rnum+=1
  rr=F(rnum,scale)
  ck(rr*rr>=F(k,60),'small_branch_upper_radius')
  rad=1+c*rr
  Tpower=F(343*s)-F(335,2)+k
  weighted_den=1
  branch='uncapped_y_R'
 else:
  rad=1+c
  Tpower=F(343*s)-F(5,4)
  weighted_den=k**int(qpow)
  branch='sparsity_cap'
  ck(F(343*s)-F(335,2)+k+F(qpow,f)==Tpower,
     'active_cap_exact_T_cancellation')
 n=(528*rad.numerator**2)**(f*k)*comb(m,k)
 d=(rad.denominator**2)**(f*k)*factorial(f*k)*D0**k*weighted_den
 L=ceil_log2_ratio(n,d)
 E=C+996*Tpower+L
 rows.append(dict(k=k,branch=branch,radius_upper=str(rad),T_power=str(Tpower),
  weighted_volume_log_ceiling=L,exponent_upper=str(E),
  positive_exponent_means_bound_failure_only=E>=0))
passing=[r for r in rows if F(r['exponent_upper'])<-4096]
negative=[r for r in rows if F(r['exponent_upper'])<0]
maxrow=max(rows,key=lambda r:F(r['exponent_upper']))
maxnegative=max(negative,key=lambda r:F(r['exponent_upper']))
ck([r['k'] for r in negative]==list(range(1,108)),'complete_negative_sector_1through107')
ck(F(maxnegative['exponent_upper'])==F(-6761,8)<-845,'negative_sector_maximum')
ck(F(rows[107]['exponent_upper'])==F(3999,8),'adjacent_k108_failed_envelope')
ck(len(negative)==107<2**7,'negative_sector_union_charge838')
# This comparison is a diagnostic of this explicit envelope, not a lower
# bound on the actual signed or absolute matrix contribution.
ck(F(maxrow['exponent_upper'])>0,'whole_profile_estimate_does_not_close')
ck(maxrow['k']==164,'largest_retained_envelope_at_dense_endpoint')
result=dict(finding='independent_sparse_t1_envelope_zero_target_corrected',status='PASS',
 time_utc=datetime.now(timezone.utc).isoformat(),assertions=len(checks),
 constant=str(C),rows=rows,
 k_with_upper_below_minus4096=[r['k'] for r in passing],
 k_with_negative_upper=[r['k'] for r in negative],
 maximum=maxrow,
 union_charge_for_below4096_sector=4088,
 negative_sector_maximum=maxnegative,
 union_charge_for_negative_sector=838,
 zero_target_correction='Exact weighted factor2 at the one type-III place; no independent CM-partner multiplicity.',
 scope='Corrected exact arithmetic for a conservative per-k envelope, all-top s11 t1 only. Sum over164 cells costs less than8bits. Geometry and main-ledger promotion are separate; positive envelope is no actual lower bound.',
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','time_utc','assertions','constant','maximum','k_with_upper_below_minus4096','k_with_negative_upper']},indent=2))
