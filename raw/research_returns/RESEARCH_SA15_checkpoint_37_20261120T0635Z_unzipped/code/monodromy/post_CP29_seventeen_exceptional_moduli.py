"""Reconstruct the modulus polynomial of the norm17 orbit overestimate."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
source=json.loads((agent/'outputs/post_CP29_seventeen_full_orbit_probe.json').read_text())
assert source['status']=='PASS_EXACT_ORBIT_INTERSECTION_ONLY'
n=int(source['final_polynomial_hex'],16)
f=nmod_poly([(n>>i)&1 for i in range(n.bit_length())],2)
x=nmod_poly([0,1],2)
D=x**12+x**9+x**6+x**3+1
H=x**4+x
g,rem=divmod(f,D);assert not rem
remaining=g;chosen=[]
for i in range(9,-1,-1):
    term=D**(5*i)*H**(12*(9-i))
    if remaining.degree()==term.degree():
        chosen.append(i);remaining+=term
assert not remaining
modulus=nmod_poly([int(i in chosen) for i in range(10)],2)
guess_matches=(modulus*(x+1)==(x**7+1)*(x**3+1))
out={'status':'PASS_EXACT_EXCEPTIONAL_MODULUS_IDENTITY',
     'actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
     'previous_field_union_guess_matches':bool(guess_matches),
     'modulus_coefficients_ascending':[int(c) for c in modulus.coeffs()],
     'factorization':[{'coefficients_ascending':[int(c) for c in fac.coeffs()],'degree':int(fac.degree()),'exponent':int(e)} for fac,e in modulus.factor()[1]],
     'identity':'F(x)=D12(x)*H4(x)^108*f(D12(x)^5/H4(x)^12), f is the exact degree-nine binary polynomial listed in this output.',
     'scope':'The current sufficient-good-parameter argument leaves only mu=0 or mu^5 a root of the displayed degree-nine polynomial. This is an overestimate, not a bad-fibre assertion. Finite exceptional nodality remains unproved.'}
(agent/'outputs/post_CP29_seventeen_exceptional_moduli.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
