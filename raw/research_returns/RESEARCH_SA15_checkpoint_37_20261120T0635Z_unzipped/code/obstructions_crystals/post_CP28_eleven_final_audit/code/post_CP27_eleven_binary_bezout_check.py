"""Independent binary-only reconstruction of the five parameter transforms."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import json,time
from post_CP27_binary_coefficient_ring import cmul,factor_power

@lru_cache(maxsize=None)
def translate_one(p):
    if p.bit_length()<=1:return p
    m=1<<((p.bit_length()-1).bit_length()-1)
    lo=p&((1<<m)-1);hi=p>>m
    b=translate_one(hi)
    return translate_one(lo)^b^(b<<m)

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
r=json.loads((agent/'outputs/post_CP27_eleven_certificate_reconstruction.json').read_text())
assert r['status']=='PASS_EXACT_FACTOR_BEZOUT_AND_REGULAR_U_CERTIFICATE'
B=int(r['B_hex'],16)
rev=sum(((B>>i)&1)<<(B.bit_length()-1-i) for i in range(B.bit_length()))
real=sum(((B>>i)&1)<<i for i in range(B.bit_length()) if i%3 in (0,2))
imag=sum(((B>>i)&1)<<i for i in range(B.bit_length()) if i%3 in (1,2))
polys=[B,translate_one(B),rev,real,imag]
assert polys==[int(p,16) for p in r['five_polynomials_hex']]
value=0
for p,b in zip(polys,r['bezout_coefficients_hex']):value^=cmul(p,int(b,16))
assert value==1
v=2;r0=(1<<2)|(1<<1)
N=factor_power(r0,6)^factor_power(r0,5)^factor_power(r0,4)^factor_power(r0,3)^1
D=(1<<12)|(1<<9)|(1<<6)|(1<<3)|1
H=(1<<4)|(1<<1)
assert N==D
assert cmul(factor_power(r0,12),factor_power(factor_power(r0,4)^1,3))==factor_power(H,12)
assert cmul(D,H)==(1<<16)|(1<<1)
assert translate_one(D)==D and translate_one(H)==H
assert sum(((D>>i)&1)<<(12-i) for i in range(13))==D
assert all(i%3==0 for i in range(D.bit_length()) if (D>>i)&1)
assert all(i%3==1 for i in range(H.bit_length()) if (H>>i)&1)
result={'status':'PASS_BINARY_ONLY_PARAMETER_BEZOUT_AND_MODULUS_IDENTITIES',
 'actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
 'B_degree':3354,'five_transform_polynomials_reconstructed':True,
 'bezout_sum':1,'modulus_Dickson_and_transform_identities':True,
 'scope':'No FLINT calls: the five transforms, full Bezout sum and modulus identities are reconstructed by binary polynomial arithmetic. Resultant inputs/recomputation and geometry remain separate.'}
(agent/'outputs/post_CP27_eleven_binary_bezout_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
