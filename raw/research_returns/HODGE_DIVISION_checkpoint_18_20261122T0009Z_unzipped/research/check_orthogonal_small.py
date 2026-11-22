"""Complete small-orthogonal spectra using previously reviewed Ramanujan arithmetic.

The GAP probe is a different computation. This checker independently
selects extension rows, validates fusions, and checks Schur indicators.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from functools import lru_cache
import hashlib,json,sys,time
import sympy as sp
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(R/'agents/g34_eightfolds/bireflection'))
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square,ramanujan

@lru_cache(None)
def mean(z):
 if isinstance(z,int): return F(z)
 n,c=z
 return F(sum(a*ramanujan(n,k) for k,a in enumerate(c)),int(sp.totient(n)))

def main():
 start=time.perf_counter();raw=(B/'orthogonal_small_inputs.json').read_bytes()
 digest=hashlib.sha256(raw).hexdigest()
 assert digest=='5236207618c2564af7ed4871c0f92a667664255d2e60be87f037257356669b79'
 D=json.loads(raw);ts={t['name']:t for t in D['tables']}
 expected={
  '6.O7(3)':('2/9',27),'6.O7(3).2':('11/39',78),
  'O8-(2)':('16/51',34),'O8-(2).2':('7/34',34),
  '2^2.O8+(3)':('28/65',260),'2.O8-(3)':('52/123',246),
  '2.O9(3)':('13/41',780),
  'O10+(2)':('32/93',155),'O10+(2).2':('7/31',155),
  'O10-(2)':('64/187',154),'O10-(2).2':('5/22',154),
  'O12+(2)':('128/357',651),'O12+(2).2':('5/21',651),
  'O12-(2)':('256/715',650),'O12-(2).2':('31/130',650)}
 assert set(ts)==set(expected)
 chars={n:[[encode(z) for z in row] for row in t['characters']] for n,t in ts.items()}
 out={'status':'PASS','input_sha256':digest,'rows':0,'spectra':0,'normal_fusions':0,
      'indicators_checked':0,'tables':[]}
 for name,t in ts.items():
  cc=chars[name];n=len(cc)
  assert n==len(t['orders'])==len(t['sizes'])==len(t['indicators'])
  assert all(len(row)==n for row in cc)
  assert sum(row[0]**2 for row in cc)==sum(t['sizes'])==t['order']
  assert t['full_row_orthogonality_checked'] is True
  pm={z['prime']:z['map'] for z in t['power_maps']}
  for prime,mp in pm.items():
   assert len(mp)==n and all(1<=j<=n for j in mp)
   assert all(t['orders'][j-1]==o//gcd(o,prime) for j,o in zip(mp,t['orders']))
  for row,indicator in zip(cc,t['indicators']):
   v=sum(size*mean(row[j-1]) for size,j in zip(t['sizes'],pm[2]))/t['order']
   assert v==indicator and v in (-1,0,1)
   out['indicators_checked']+=1
  if 'core' in t:
   u=ts[t['core']];fusion=t['fusion'];assert t['order']==2*u['order']
   assert len(fusion)==len(u['orders']) and [i for i,j in enumerate(fusion) if j==1]==[0]
   assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
   assert all(sum(size for size,j in zip(u['sizes'],fusion) if j==k)==t['sizes'][k-1] for k in set(fusion))
   for p in u['power_maps']:
    assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
   out['normal_fusions']+=1
  rr={'name':name,'rows':[],'spectra':0}
  for i,row in enumerate(cc):
   a=row[0]
   if a<=1:continue
   core_row=i+1
   if 'core' in t:
    norm=sum(size*rational_mean_abs_square(row[j-1]) for size,j in zip(u['sizes'],fusion))/u['order']
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
   rr['rows'].append({'row':i+1,'core_row':core_row,'degree':a,'min_nu':nu,
                     'min_class':at,'ratio':str(F(nu,a)),'indicator':t['indicators'][i]})
  rr['min_ratio']=str(min(F(x['min_nu'],x['degree']) for x in rr['rows']))
  rr['min_degree']=min(x['degree'] for x in rr['rows'])
  assert (rr['min_ratio'],rr['min_degree'])==expected[name],name
  print(json.dumps({k:v for k,v in rr.items() if k!='rows'}),flush=True)
  out['rows']+=len(rr['rows']);out['spectra']+=rr['spectra'];out['tables'].append(rr)
 assert (out['rows'],out['spectra'],out['normal_fusions'])==(2938,778260,6)
 o9=next(t for t in out['tables'] if t['name']=='2.O9(3)')
 nonreal=[r for r in o9['rows'] if r['indicator']==0]
 assert [(r['row'],r['degree'],r['ratio']) for r in nonreal]==[(224,838656,'1/2'),(225,838656,'1/2')]
 assert all(r['indicator']==1 for r in o9['rows'] if r['indicator']!=0)
 assert min(F(28,65),F(52,123))/2>F(1,5)
 assert min(F(2,9),F(7,34),F(7,31),F(5,22),F(5,21),F(31,130))>F(1,5)
 assert 6/(12*F(1,5)-2)==15<27
 assert 6/(10*F(13,82)-1)==F(41,4)<780
 out['O9_nonselfdual_rows']=nonreal
 out['seconds']=time.perf_counter()-start
 (B/'orthogonal_small_checked.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='tables'}),flush=True)
if __name__=='__main__':main()
