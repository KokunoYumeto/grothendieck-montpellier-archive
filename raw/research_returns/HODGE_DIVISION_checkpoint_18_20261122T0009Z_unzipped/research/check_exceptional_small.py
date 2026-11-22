"""Exact spectra from complete exceptional inputs, separately from GAP.

Reuses the already reviewed Ramanujan Fourier arithmetic; this is a new
complete data application, not a new implementation of that arithmetic.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import hashlib,json,sys,time
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(R/'agents/g34_eightfolds/bireflection'))
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square

def main():
 start=time.perf_counter();raw=(B/'exceptional_small_inputs.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()=='625618617ad0b6268b8898cc39e7e04afb6ae55f8639686347a0b9cf8d244a21'
 d=json.loads(raw);ts={t['name']:t for t in d['tables']}
 assert set(ts)=={'2.F4(2)','2.F4(2).2','F4(3)','E6(2)','(2^2x3).2E6(2)'}
 chars={n:[[encode(z) for z in r] for r in t['characters']] for n,t in ts.items()}
 out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'rows':0,'spectra':0,'tables':[]}
 for name,t in ts.items():
  cc=chars[name];n=len(cc)
  assert n==len(t['orders'])==len(t['sizes'])
  assert all(len(r)==n for r in cc)
  assert sum(r[0]**2 for r in cc)==sum(t['sizes'])==t['order']
  assert len(t['indicators'])==n and all(x in (-1,0,1) for x in t['indicators'])
  for pm in t['power_maps']:
   assert len(pm['map'])==n
   assert all(1<=j<=n for j in pm['map'])
   assert all(t['orders'][j-1]==o//gcd(o,pm['prime']) for o,j in zip(t['orders'],pm['map']))
  if 'core' in t:
   u=ts[t['core']];fusion=t['fusion'];assert t['order']==2*u['order']
   assert len(fusion)==len(u['orders']) and [i for i,j in enumerate(fusion) if j==1]==[0]
   assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
   assert all(sum(s for s,j in zip(u['sizes'],fusion) if j==k)==t['sizes'][k-1] for k in set(fusion))
   pm={z['prime']:z['map'] for z in t['power_maps']}
   for p in u['power_maps']:
    assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
  rr={'name':name,'rows':[],'spectra':0}
  for i,row in enumerate(cc):
   a=row[0]
   if a<=1:continue
   core_row=i+1
   if 'core' in t:
    norm=sum(s*rational_mean_abs_square(row[j-1]) for s,j in zip(u['sizes'],fusion))/u['order']
    assert norm.denominator==1
    if norm!=1:continue
    matches=[j+1 for j,c in enumerate(chars[t['core']]) if c==[row[k-1] for k in fusion]]
    assert len(matches)==1;core_row=matches[0]
   nu=a;at=0
   for j,z in enumerate(row):
    if abs_square(z)[1]==(a*a,):continue
    ev=spectrum(t,row,j);v=a-max(ev)
    if v<nu:nu=v;at=j+1
    rr['spectra']+=1
   rr['rows'].append({'row':i+1,'core_row':core_row,'degree':a,'min_nu':nu,'min_class':at,
                      'ratio':str(F(nu,a)),'indicator':t['indicators'][i]})
  rr['min_ratio']=str(min(F(x['min_nu'],x['degree']) for x in rr['rows']))
  rr['min_degree']=min(x['degree'] for x in rr['rows'])
  print(json.dumps({k:v for k,v in rr.items() if k!='rows'}),flush=True)
  out['rows']+=len(rr['rows']);out['spectra']+=rr['spectra'];out['tables'].append(rr)
 out['seconds']=time.perf_counter()-start
 (B/'exceptional_small_checked.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='tables'}),flush=True)
if __name__=='__main__':main()
