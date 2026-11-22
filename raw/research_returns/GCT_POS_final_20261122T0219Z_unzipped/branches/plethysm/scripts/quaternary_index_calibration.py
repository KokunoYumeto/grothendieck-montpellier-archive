"""Exact finite calibration from Salmon's quaternary-cubic Hilbert series.
This does not extrapolate to larger n. All arithmetic uses Fraction.
"""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json
L=120; degree=4; weights=[2,4,6,8,10]; nmax=8*L
coeff=[0]*(nmax+1);coeff[0]=1
for a in weights:
 for s in range(a,nmax+1):coeff[s]+=coeff[s-a]
values=[coeff[s]+(coeff[s-25] if s>=25 else 0) for s in range(nmax+1)]
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):r[i+j]+=a*b
 return r
def add(p,q):
 r=[F(0)]*max(len(p),len(q))
 for i,a in enumerate(p):r[i]+=a
 for i,b in enumerate(q):r[i]+=b
 return r
def evaluate(p,x):
 r=F(0)
 for a in reversed(p):r=r*x+a
 return r
def shift(p,u):return [sum(p[j]*comb(j,i)*u**(j-i) for j in range(i,len(p))) for i in range(len(p))]
polys=[]
for r in range(L):
 vals=[F(values[r+j*L]) for j in range(degree+1)]
 p=[F(0)];basis=[F(1)]
 for j in range(degree+1):
  p=add(p,[b*vals[0]/factorial(j)/L**j for b in basis])
  vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
  basis=mul(basis,[F(-r-j*L),F(1)])
 polys.append(p)
for s in range(nmax+1):assert evaluate(polys[s%L],s)==values[s]
# Global-QP justification: numerator over (1-t^L)^5 has degree595<600.
for p in range(500):
 if all(all(c>=0 for c in shift(poly,p)) for poly in polys):break
else:raise RuntimeError('No positivity shift within calibration range')
bad=[]
for x in range(1,p+1):
 for r,poly in enumerate(polys):
  if evaluate(poly,x)<=0:bad.append((x,r,str(evaluate(poly,x))))
s=max([x for x,r,v in bad],default=0)
prev=[(r,j,str(c)) for r,poly in enumerate(polys) for j,c in enumerate(shift(poly,p-1)) if c<0] if p else []
record={'period_used':L,'degree':degree,'positivity_index':p,'strict_saturation_index':s,'previous_shift_negative_coefficients':prev,'last_nonpositive_constituent_values':[a for a in bad if a[0]==s],'largest_realized_hole':max(x for x in range(nmax+1) if values[x]==0),'polynomials_low_to_high':[[str(a) for a in poly] for poly in polys]}
(Path(__file__).resolve().parent.parent/'certificates/quaternary_index_calibration.json').write_text(json.dumps(record,indent=2))
print({k:v for k,v in record.items() if k!='polynomials_low_to_high'})
