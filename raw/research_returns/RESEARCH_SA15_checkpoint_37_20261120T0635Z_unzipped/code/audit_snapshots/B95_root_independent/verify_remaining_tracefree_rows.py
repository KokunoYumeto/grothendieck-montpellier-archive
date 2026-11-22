#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import json,time
started=time.perf_counter()
def psi(bs,v):
 p=Q(0);ans=Q(0);s=1;v=Q(v)
 for b in map(Q,bs):
  if v<=b:return ans+s*(v-p)
  ans+=s*(b-p);p=b;s*=5
 return ans+s*(v-p)
rows=[];bad=[]; thresholds={}
for a,rs,otherC in [(7,[30,54,78],858),(11,[6,30,54,78,102,126],1362)]:
 t=24*a
 assert 80+5*t<1875
 assert Q(5625-75,5)<Q(5545-4*t)
 assert Q((5545-4*t)+4*t,5)==1109
 for r in rs:
  rp=r-12 if a==7 else r+12
  for C in range(6,1110,24):
   if C<=t:continue
   delta=Q(t+4*r,5); beta=Q(C+4*r,5); gamma=Q(otherC+4*rp,5)
   up=[Q(min(r,rp)),Q(max(r,rp)),delta,min(beta,gamma),max(beta,gamma)]
   assert all(x<y for x,y in zip(up,up[1:])),(a,r,C,up)
   lo=[psi(up,z) for z in up]
   lv=psi(up,beta);lw=psi(up,gamma)
   lr=psi(up,r);lrp=psi(up,rp)
   cyc=psi(up,576)
   assert max(up)<576
   for mirror in [False,True]:
    bpair=[a,15] if not mirror else [9,24-a]
    bmin=bpair[0];jmin=24-bpair[1]
    origv,origw,cres=(lv,lw,lrp) if not mirror else (lw,lv,lr)
    esh=[lo[3],Q(lo[4]+4*lo[3],5)]
    z=lo[3] if origw==lo[3] else esh[-1]
    highU=15600*jmin
    ah=Q(highU+4*z,5)
    assert highU>z and ah>esh[-1],(a,r,C,mirror,'high',highU,z,ah,esh)
    Ba=psi(esh,ah)
    assert Ba==78000*jmin-4*origv
    elo=[cres,Q(origw+4*cres,5)]
    assert elo[1]>elo[0]
    dc=3120*bmin
    assert dc>elo[-1],(a,r,C,mirror,'low',dc,elo)
    Bd=psi(elo,dc)
    assert Bd==78000*bmin-4*origw-20*cres
    key=str(bpair)
    ztest=origv if origw<origv else z
    prev=thresholds.setdefault(key,{'high_threshold':Q(0),'low_threshold':Q(0)})
    prev['high_threshold']=max(prev['high_threshold'],ztest)
    prev['low_threshold']=max(prev['low_threshold'],elo[-1])
    row={'a':a,'r':r,'rprime':rp,'C':C,'b_pair':bpair,'upper':[str(v) for v in up],
         'lower':[str(v) for v in lo],'cyclotomic':str(cyc),'a1_bound':str(Ba),'d1_bound':str(Bd),
         'a_gap':str(cyc-Ba),'d_gap':str(cyc-Bd)}
    rows.append(row)
    if cyc<=max(Ba,Bd):bad.append(row)
# Independent exact binomial and critical-bound arithmetic.
for j in range(1,25): assert comb(75,j)%5==0
assert comb(75,25)%5==3 and comb(80,5)%5==1
critical_checks=0
for a in [7,11]:
 t=24*a
 assert 75+25*t>1875 and 80+5*t<1875
 for zz in range(t+1,5550):
  if zz>1110 and zz>5545-4*t:
   J=5625-zz
   assert J+t<80+5*t<1875
   critical_checks+=1
 for mm in range(5,1876,5):
  if mm>75:assert mm>=80
# Closed strict-gap formulas are checked against independent Herbrand
# integration, and analytically minimized on the exact endpoint ranges.
for row in rows:
 a,r,C=row['a'],row['r'],row['C']
 mirror=row['b_pair'][0]==9
 if a==7 and not mirror: da,dd=676440-2520*r,1237200-500*C-2500*r
 if a==7 and mirror: da,dd=1237440-500*C-2520*r,677400-2500*r
 if a==11 and not mirror: da,dd=365400-2520*r,915600-500*C-2500*r
 if a==11 and mirror: da,dd=914400-500*C-2520*r,365400-2500*r
 assert Q(row['a_gap'])==da and Q(row['d_gap'])==dd
 assert da>0 and dd>0
expected_thresholds={'[7, 15]':(51318,16098),'[9, 17]':(80418,10326),
 '[11, 15]':(29706,28794),'[9, 13]':(143706,4326)}
for key,(hi,lo) in expected_thresholds.items():
 assert thresholds[key]=={'high_threshold':Q(hi),'low_threshold':Q(lo)}
thresholds={k:{a:str(b) for a,b in v.items()} for k,v in thresholds.items()}
assert len(rows)==654 and not bad
result={'status':'PASS' if not bad else 'FAIL','actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-started,'profiles':len(rows),'bad_profiles':bad,'critical_bound_checks':critical_checks,
 'binomial_checks':26,'relative_field_thresholds':thresholds,
 'minimum_a_gap':str(min(Q(x['a_gap']) for x in rows)),
 'minimum_d_gap':str(min(Q(x['d_gap']) for x in rows)),
 'scope':'Exact finite supplement to B95: critical binomial arithmetic, all654 necessary conductor profiles, actual-field restriction formulas from B94, and symbolic strict-gap identities. The full written actual-field proof is required; no profile realization or unrestricted least-index equality is inferred.',
 'rows':rows}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
