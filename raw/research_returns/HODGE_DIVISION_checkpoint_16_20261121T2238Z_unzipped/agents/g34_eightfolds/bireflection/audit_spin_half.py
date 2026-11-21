#!/usr/bin/env python3
"""Independent all-eigenspace half bound on the complete faithful2.A6 input."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from audit_sporadic_input import encode,fourier_via_rational_trace
P=Path(__file__).resolve().parent
src=P.parent.parent/'imprimitive/sporadic/alternating_cover_inputs.json'
raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c'
t=next(t for t in json.loads(raw)['tables'] if t['name']=='2.A6')
chars=[[encode(z) for z in c] for c in t['characters']]
z=next(j for j,(s,o) in enumerate(zip(t['sizes'],t['orders'])) if s==1 and o==2)
rows=[i for i,c in enumerate(chars) if c[z]==-c[0]]
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
     'method':'independent Ramanujan-sum exact Fourier reconstruction',
     'rows':[],'total_entries':0}
for i in rows:
 c=chars[i];e=c[0];record={'row':i+1,'degree':e,'spectra':[]}
 for j,s in enumerate(t['sizes']):
  if s==1:continue
  m=fourier_via_rational_trace(t,c,j);nu=e-max(m)
  assert 2*nu>=e
  record['spectra'].append({'class':j+1,'order':len(m),'multiplicities':m,'nu':nu})
 record['minimum_nu_over_degree']=str(min(F(x['nu'],e) for x in record['spectra']))
 assert record['minimum_nu_over_degree']=='1/2'
 out['total_entries']+=len(record['spectra']);out['rows'].append(record)
assert out['total_entries']==66 and len(out['rows'])==6
(P/'audit_spin_half.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','rows':6,'entries':66,'all_minimum_nu_over_degree':'1/2'}))
