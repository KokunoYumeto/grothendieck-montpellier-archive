"""Full4096-coordinate integral verifier for the18-term crown/triangles cover.

Uses only Python integer arithmetic and the explicit port schema in the input.
No numerical solver, symbolic algebra package or source checker is required.
"""
from itertools import product
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'inputs/pg_cauchy_r3_integral_cover.json'
D=json.loads(P.read_text())

def flatten(out):
 n=0
 for x in out:n=4*n+x
 return n

def slot(i,j):
 return [k for k in range(3) if k!=i].index(j)

def target():
 v=[0]*4096
 edges=[(side+i,side+j) for side in (0,3) for i in range(3) for j in range(i+1,3)]
 for bits in product((0,1),repeat=6):
  out=[0]*6;sgn=1
  for (a,b),bit in zip(edges,bits):
   out[a]|=bit<<slot(a%3,b%3)
   out[b]|=(1-bit)<<slot(b%3,a%3)
   if bit:sgn=-sgn
  v[flatten(out)]+=sgn
 return v

def crown(sigma,mask):
 assert sorted(sigma)==[0,1,2] and 0<=mask<64
 v=[0]*4096
 edges=[(i,l) for i in range(3) for l in range(3) if i!=l]
 for bits in product((0,1),repeat=6):
  out=[0]*6;sgn=1
  for (i,l),bit in zip(edges,bits):
   j=sigma[l]
   out[i]|=bit<<slot(i,l)
   out[3+j]|=(1-bit)<<slot(j,sigma[i])
   if bit:sgn=-sgn
  for i in range(6):
   if mask>>i&1:out[i]=(out[i]>>1)|((out[i]&1)<<1)
  v[flatten(out)]+=sgn
 return v

H=target();total=[0]*4096;term_checks=[]
assert len(D['terms'])==18
for t in D['terms']:
 assert t['coefficient'] in (-1,1)
 v=crown(t['sigma'],t['swap_mask'])
 assert sum(x!=0 for x in v)==64
 total=[x+t['coefficient']*y for x,y in zip(total,v)]
 term_checks.append({'sigma':t['sigma'],'swap_mask':t['swap_mask'],'coefficient':t['coefficient'],'nonzero_coordinates':64})
assert total==H
out={'status':'PASS exact integral18-term identity, valid over every field',
 'checked_coordinates':4096,'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'target_nonzero_coordinates':sum(x!=0 for x in H),'term_count':18,
 'source_per_term':'K3,3 minus a perfect matching; six binary wires',
 'full_source':'K3,3, with omitted matching wires projected to basis0',
 'selector_dimension':18,'binary_selector_bits_sufficient':5,
 'coefficients':term_checks,'target_coefficients':[[i,x] for i,x in enumerate(H) if x],
 'scope':'r3,q2 finitecover only; no generalr or subquadratic asymptotic-selector claim'}
O=ROOT/'outputs/pg_cauchy_r3_integral_verification.json';O.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('coefficients','target_coefficients')},indent=2))
