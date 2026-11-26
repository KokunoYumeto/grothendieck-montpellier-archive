"""Exact expansion of13 local-product terms into the certified18-term identity."""
from pathlib import Path
from itertools import product
from collections import defaultdict
import json,hashlib
B=Path(__file__).resolve().parents[1]
P=B/'inputs/pg_cauchy_r3_dense_cover.json'
D=json.loads(P.read_text())
E=json.loads((B/'inputs/pg_cauchy_r3_integral_cover.json').read_text())
a=defaultdict(int); b=defaultdict(int)
for t in E['terms']:a[tuple(t['sigma']),t['swap_mask']]+=t['coefficient']
for t in D['terms']:
 assert len(t['local_I_swap_coefficients'])==6
 for bits in product((0,1),repeat=6):
  c=t['coefficient']
  for v,bit in enumerate(bits):c*=t['local_I_swap_coefficients'][v][bit]
  b[tuple(t['sigma']),sum(bit<<v for v,bit in enumerate(bits))]+=c
a={k:v for k,v in a.items() if v};b={k:v for k,v in b.items() if v}
assert a==b and len(D['terms'])==13
out={'status':'PASS exact integral13-term local-product cover','expanded_nonzero_terms':len(b),'selector_dimension':13,'binary_selector_bits_sufficient':4,'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'scope':'Each term uses a crown graph and party-local I,SWAP,I-SWAP,SWAP-I. Valid over every field. No general-r or asymptotic claim.'}
p=B/'outputs/pg_cauchy_r3_dense_verification.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(p)
print(json.dumps(out,indent=2))
