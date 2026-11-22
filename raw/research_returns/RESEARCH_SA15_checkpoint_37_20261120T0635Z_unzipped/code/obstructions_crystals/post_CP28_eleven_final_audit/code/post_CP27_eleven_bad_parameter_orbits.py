"""Exact PGL2(F4)-orbit obstruction test for retained norm-eleven factors.

The input includes the A=0 repeated-B obstruction. This exact algebraic
calculation still requires the complete geometric fibre interpretation.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING'}
try:
    raw=json.loads((agent/'outputs/post_CP27_eleven_flint_elimination.json').read_text())
    assert raw['status']=='PASS_EXACT_ELIMINATION_DISCOVERY_ONLY'
    v=nmod_poly([0,1],2)
    make=lambda x:nmod_poly([(x>>i)&1 for i in range(x.bit_length())],2)
    encode=lambda p:hex(sum(int(c)<<i for i,c in enumerate(p.coeffs())))
    extra=json.loads((agent/'outputs/post_CP27_eleven_A_zero_elimination.json').read_text())
    assert extra['status']=='PASS_A_ZERO_ELIMINATION_DISCOVERY_ONLY'
    factors={f['factor_hex'] for source in (raw,extra) for row in source['stages'] for f in row.get('factorization',[])}
    B=nmod_poly([1],2)
    for f in sorted(factors):B*=make(int(f,16))
    H=v**4+v
    B=B//B.gcd(H)
    D=v**12+v**9+v**6+v**3+1
    assert D*H==v**16+v
    assert H.compose(v+1)==H
    assert D.compose(v+1)==D
    assert nmod_poly(list(reversed(D.coeffs())),2)==D
    iterations=[]
    original=B
    while True:
        trans=B.compose(v+1)
        inv=nmod_poly(list(reversed(B.coeffs())),2)
        co=B.coeffs()
        real=nmod_poly([int(c) if i%3 in (0,2) else 0 for i,c in enumerate(co)],2)
        imag=nmod_poly([int(c) if i%3 in (1,2) else 0 for i,c in enumerate(co)],2)
        nxt=B.gcd(trans).gcd(inv).gcd(real).gcd(imag)
        iterations.append({'before_degree':int(B.degree()),'after_degree':int(nxt.degree()),'result_hex':encode(nxt)})
        if nxt==B:break
        B=nxt
    factorization=B.factor()
    result.update({'status':'PASS_ALL_RETAINED_BAD_FACTOR_ORBIT_TEST',
      'initial_radical_degree':int(original.degree()),'iterations':iterations,
      'stable_bad_orbit_polynomial_hex':encode(B),
      'stable_factors':[{'factor_hex':encode(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in factorization[1]],
      'modulus_zero_gcd_hex':encode(B.gcd(D)),
      'stable_polynomial_divides_D':bool(not (D%B)),
      'scope':'Exact maximum invariant root subset for all generic, exceptional and A-zero repeated-B factors. The complete interpolation and geometric fibre proof require independent audit before any nodality or monodromy assertion.'})
except Exception:
    result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP27_eleven_bad_parameter_orbits.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
