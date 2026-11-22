"""Exact iterative PGL2(F4)-orbit intersection for the norm17 bad set."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time, traceback
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','steps':[]}
try:
    data=json.loads((agent/'outputs/post_CP29_seventeen_split_parameter_probe.json').read_text())
    assert data['status']=='PASS_RESULTANT_DISCOVERY_ONLY'
    n=int(data['pulled_bad_polynomial_hex'],16)
    f=nmod_poly([(n>>i)&1 for i in range(n.bit_length())],2)
    x=nmod_poly([0,1],2)
    enc=lambda p:hex(sum(int(c)<<i for i,c in enumerate(p.coeffs())))
    while True:
        coeffs=f.coeffs()
        real=nmod_poly([int(c) if i%3 in (0,2) else 0 for i,c in enumerate(coeffs)],2)
        imag=nmod_poly([int(c) if i%3 in (1,2) else 0 for i,c in enumerate(coeffs)],2)
        nxt=f.gcd(f.compose(x+1)).gcd(nmod_poly(list(reversed(coeffs)),2)).gcd(real).gcd(imag)
        out['steps'].append({'input_degree':int(f.degree()),'output_degree':int(nxt.degree()),'polynomial_hex':enc(nxt)})
        if nxt==f:break
        f=nxt
    out.update({'status':'PASS_EXACT_ORBIT_INTERSECTION_ONLY','final_degree':int(f.degree()),'final_polynomial_hex':enc(f),
                'factorization':[{'factor_hex':enc(g),'degree':int(g.degree()),'exponent':int(e)} for g,e in f.factor()[1]],
                'scope':'Iterated exact generator intersection of the retained overestimated bad locus. The generators preserve normalized modulus, but no complete exceptional-fibre or norm17 theorem is asserted.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_full_orbit_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
