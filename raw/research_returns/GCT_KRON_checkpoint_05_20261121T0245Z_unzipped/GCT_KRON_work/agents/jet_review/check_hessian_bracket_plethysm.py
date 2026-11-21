"""Exact h_d[h_3] coefficient at (R+4,3,2^(R-2))."""
from pathlib import Path
from functools import lru_cache
from collections import Counter,defaultdict
from fractions import Fraction
from math import factorial
from datetime import datetime,timezone
import json,importlib.util,time
src=Path(__file__).parents[2]/'computations/independent_characters.py'
spec=importlib.util.spec_from_file_location('oldchar',src);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
partitions=old.partitions;z_type=old.z_type

@lru_cache(None)
def beta_removals(lam,k):
 L=len(lam);beads={v+L-i-1 for i,v in enumerate(lam)};out=[]
 for b in beads:
  to=b-k
  if to<0 or to in beads:continue
  sign=(-1)**sum(to<c<b for c in beads)
  nb=sorted((beads-{b})|{to},reverse=True)
  nu=tuple(v-(L-i-1) for i,v in enumerate(nb) if v-(L-i-1)>0)
  assert sum(nu)==sum(lam)-k
  out.append((nu,sign))
 return tuple(out)

@lru_cache(None)
def character(lam,cyc):
 if not cyc:return int(not lam)
 if sum(lam)!=sum(cyc):return 0
 return sum(s*character(nu,cyc[1:]) for nu,s in beta_removals(lam,cyc[0]))

@lru_cache(None)
def local_power(i,m):
 ans=[]
 for a in range(m+1):
  for b in range(m-a+1):
   c=m-a-b
   coeff=Fraction(factorial(m)*3**b*2**c,factorial(a)*factorial(b)*factorial(c)*6**m)
   cyc=tuple(sorted((i,)*(3*a+b)+(2*i,)*b+(3*i,)*c,reverse=True))
   ans.append((cyc,coeff))
 return tuple(ans)

@lru_cache(None)
def plethysm_power(d):
 total=defaultdict(Fraction)
 for outer in partitions(d):
  expansion={():Fraction(1,z_type(outer))}
  for i,m in Counter(outer).items():
   nxt=defaultdict(Fraction)
   for a,c0 in expansion.items():
    for b,c1 in local_power(i,m):
     nxt[tuple(sorted(a+b,reverse=True))]+=c0*c1
   expansion=nxt
  for cyc,coef in expansion.items():total[cyc]+=coef
 return dict(total)

start=time.time();cross=0
for n in range(0,9):
 for lam in partitions(n):
  for cyc in partitions(n):
   assert character(lam,cyc)==old.character(lam,cyc),(lam,cyc)
   cross+=1
print(json.dumps({'character_crosschecks':cross}),flush=True)
records=[]
for R in range(2,13):
 d=R+1;lam=(R+4,3)+(2,)*(R-2);power=plethysm_power(d)
 value=sum((coef*character(lam,cyc) for cyc,coef in power.items()),Fraction(0))
 assert value.denominator==1 and value>=0
 # Pairing with the one-row character checks that each wreath cycle index has total mass1.
 assert sum(power.values(),Fraction(0))==1
 record={'R':R,'outer_degree':d,'inner_degree':3,'partition':lam,'ambient_multiplicity':int(value),'power_sum_cycle_types':len(power)}
 records.append(record);print(json.dumps(record),flush=True)
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'PASS','method':'Exact cycle-index h_d[h3] with p_i[h3]=(p_i^3+3p_i p_2i+2p_3i)/6; exact Murnaghan-Nakayama beta-bead removals crosschecked against connected-border-strip engine for all shapes and cycle types at size0..8. Rational arithmetic only.','character_crosschecks':cross,'records':records,'elapsed_seconds':time.time()-start}
p=Path(__file__).with_name('hessian_bracket_plethysm_certificate.json');p.write_text(json.dumps(result,indent=2)+'\n');print(str(p),flush=True)
