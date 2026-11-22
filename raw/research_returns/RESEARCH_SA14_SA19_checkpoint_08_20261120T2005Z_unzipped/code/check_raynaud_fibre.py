"""Finite semigroup check accompanying the uniform fibre non-immersion proof.

Scope: no construction or nonvanishing theorem is numerically certified here.
We enumerate the possible pole exponents for the explicitly stated cuspidal
fibre k[u^p,u^ell], for primes through 19 and 2<=ell<=80 coprime to p.
For a<ell every allowable positive exponent is divisible by p. Thus sections
of O(a infinity) cannot give a generically immersive map on that fibre.
"""
from pathlib import Path
import json,time,math
start=time.monotonic()
primes=[2,3,5,7,11,13,17,19]
checks=[]
for p in primes:
    for ell in range(2,81):
        if math.gcd(p,ell)!=1: continue
        a=ell-1
        exponents=sorted({i*p+j*ell for i in range(a//p+1) for j in range(a//ell+1) if i*p+j*ell<=a})
        expected=list(range(0,a+1,p))
        assert exponents==expected
        checks.append({'p':p,'ell':ell,'a':a,'pole_exponents':exponents})
result={'scope':__doc__,'checked_pairs':len(checks),'all_passed':True,
        'examples':[c for c in checks if (c['p'],c['ell']) in [(2,3),(3,4),(5,6),(5,11),(7,8)]],
        'seconds':round(time.monotonic()-start,6)}
out=Path(__file__).with_name('check_raynaud_fibre_output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
