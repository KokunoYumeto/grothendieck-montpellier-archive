#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,time
started=time.perf_counter()
def psi(bs,v):
 p=Q(0);ans=Q(0);s=1;v=Q(v)
 for b in map(Q,bs):
  if v<=b:return ans+s*(v-p)
  ans+=s*(b-p);p=b;s*=5
 return ans+s*(v-p)
rows=[];bad=[]
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
    row={'a':a,'r':r,'rprime':rp,'C':C,'b_pair':bpair,'upper':[str(v) for v in up],
         'lower':[str(v) for v in lo],'cyclotomic':str(cyc),'a1_bound':str(Ba),'d1_bound':str(Bd),
         'a_gap':str(cyc-Ba),'d_gap':str(cyc-Bd)}
    rows.append(row)
    if cyc<=max(Ba,Bd):bad.append(row)
result={'status':'PASS' if not bad else 'FAIL','actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-started,'profiles':len(rows),'bad_profiles':bad,
 'minimum_a_gap':str(min(Q(x['a_gap']) for x in rows)),
 'minimum_d_gap':str(min(Q(x['d_gap']) for x in rows)),
 'scope':'Exploratory finite conductor arithmetic only; full critical-coefficient and actual-field proof still required. No theorem promotion.',
 'rows':rows}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
