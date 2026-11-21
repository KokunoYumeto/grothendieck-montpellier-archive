#!/usr/bin/env python3
"""Complete local ordinary A6 spectral certificate for HD-ALT-01.

Published CTblLib input, exact integer cyclotomic arithmetic. This is the
root's author certificate; an independent peer implementation is separate.
"""
from pathlib import Path
from functools import lru_cache
from math import gcd
import hashlib,json
import sympy as sp
from flint import fmpz_poly
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'agents/imprimitive/sporadic/alternating_cover_inputs.json'
raw=path.read_bytes(); table=json.loads(raw)['tables'][0]
assert table['name']=='2.A6'
X=sp.Symbol('X')
@lru_cache(None)
def phi(n):
 return fmpz_poly([int(a) for a in reversed(sp.Poly(sp.cyclotomic_poly(n,X),X).all_coeffs())])
def embed(value,n,automorphism=1):
 result=[0]*n
 if isinstance(value,int): result[0]=value;return result
 c,coeffs=value; assert n%c==0
 for j,a in enumerate(coeffs): result[(j*(n//c)*automorphism)%n]+=a
 return result
def power_class(j,d):
 for entry in table['power_maps']:
  p=entry['prime']
  while d>1 and d%p==0:
   j=entry['map'][j]-1;d//=p
 assert d==1
 return j
def multiplicities(chi,j):
 n=table['orders'][j];traces=[]
 for r in range(n):
  if r==0:traces.append(embed(chi[0],n));continue
  d=gcd(n,r)
  traces.append(embed(chi[power_class(j,d)],n,r//d))
 result=[]
 for k in range(n):
  numerator=[0]*n
  for r,trace in enumerate(traces):
   for b,a in enumerate(trace):numerator[(b-k*r)%n]+=a
  poly=fmpz_poly(numerator)%phi(n)
  assert poly.degree()<=0 and int(poly[0])%n==0
  m=int(poly[0])//n;assert m>=0;result.append(m)
 assert sum(result)==chi[0]
 return result
central=[j for j,s in enumerate(table['sizes']) if s==1]
assert len(central)==2
z=next(j for j in central if table['orders'][j]==2)
rows=[];count=0
for i,chi in enumerate(table['characters']):
 if chi[z]!=chi[0] or chi[0]==1:continue
 entries=[]
 for j in range(len(chi)):
  if j in central:continue
  mult=multiplicities(chi,j);nu=chi[0]-max(mult)
  assert 5*nu>=2*chi[0],(i+1,j+1,mult)
  entries.append({'class':j+1,'order':table['orders'][j],
                  'multiplicities_zero_first':mult,'moving_rank':nu})
  count+=1
 rows.append({'row':i+1,'degree':chi[0],'entries':entries})
assert [r['degree'] for r in rows]==[5,5,8,8,9,10]
assert count==66
out={'status':'PASS','table':'2.A6','input_sha256':hashlib.sha256(raw).hexdigest(),
     'scope':'all nontrivial center-positive rows and all noncentral classes; published group/table identification retained',
     'entries':count,'rows':rows,'universal_consequence':'nu(h)>=2dim/5 on nontrivial A6 constituents'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','rows':len(rows),'entries':count,'bound':'maximal eigenspace<=3dim/5'}))
