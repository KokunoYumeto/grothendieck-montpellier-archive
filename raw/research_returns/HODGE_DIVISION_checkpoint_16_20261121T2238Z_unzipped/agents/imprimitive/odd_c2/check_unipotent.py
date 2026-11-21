#!/usr/bin/env python3
"""All-q corrected unipotent bounds, with exact coefficient certificates."""
from pathlib import Path
import hashlib,json,time
import sympy as s
from unipotent_data import symbolic,ROWS

B=Path(__file__).resolve().parent
start=time.monotonic();q,t,basis,rows=symbolic();x=s.symbols('x')
assert len(rows)==44
def nonnegative(poly):
 p=s.Poly(s.expand(poly),x);assert all(c>=0 for c in p.all_coeffs());return [str(c) for c in reversed(p.all_coeffs())]
def abs_shift(poly):
 p=s.Poly(s.expand(poly.subs(q,7+x)),x)
 return sum(abs(c)*x**m[0] for m,c in p.terms())
cert=[];checks=0
for name,row in rows.items():
 if name=='1':continue
 d=row[0];assert s.diff(d,t)==0
 degree_floor=nonnegative((d-(q*q-1)/2).subs(q,7+x))
 if name not in ['theta3','theta4','theta7','theta8']:
  nonnegative((d-q*(q-1)**2/2).subs(q,7+x))
 entry_certs=[]
 for v in row[1:]:
  assert s.Poly(v,t).degree()<=1
  a=s.expand(v).coeff(t,0);b=s.expand(v).coeff(t,1)
  # sqrt(q)<=(q-1)/2 for q>=7; q^2-6q+1 has positive
  # coefficients at q=7+x, proving that auxiliary inequality.
  upper=abs_shift(a)+abs_shift(b)*(3+x/2)
  diff=s.expand(d.subs(q,7+x)/2-upper)
  entry_certs.append(nonnegative(diff));checks+=1
 cert.append({'name':name,'degree':str(d),'degree_floor':degree_floor,'half_bound_coefficients':entry_certs})
nonnegative(((q-1)**2-4*q).subs(q,7+x))
# The printed averaging identities also determine the positions of the
# zero entries in the two sparse basis rows unambiguously.
weights=[1,(q*q-1)/2,(q*q-1)/2,q*(q-1)*(3*q+1)/2,q*(q-1)**2/2,q*q*(q-1)**2/2,q*q*(q-1)**2/2]
expected=[1,1,1,0,1,0,0]
for v,ans in zip(basis,expected):assert s.expand(sum(a*b for a,b in zip(v,weights))-ans*q**4)==0
out={'status':'PASS','source_transcription_sha256':hashlib.sha256((B/'unipotent_data.py').read_bytes()).hexdigest(),
     'nontrivial_types':len(rows)-1,'unipotent_entries':checks,'threshold':7,
     'character_ratio_bound':'1/2','minimum_degree':'(q^2-1)/2',
     'four_exceptional_degree_types':['theta3','theta4','theta7','theta8'],
     'other_degree_floor':'q*(q-1)^2/2','certificate':cert,'seconds':round(time.monotonic()-start,6)}
(B/'unipotent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='certificate'},indent=2))
