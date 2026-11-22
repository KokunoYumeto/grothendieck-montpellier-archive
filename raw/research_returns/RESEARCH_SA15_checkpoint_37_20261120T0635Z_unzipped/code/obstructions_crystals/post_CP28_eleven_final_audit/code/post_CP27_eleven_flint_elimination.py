"""Bounded exact FLINT discovery of norm-eleven parameter obstructions.

Requires python-flint0.9.0. Discovery only: every exceptional factor and
geometric special fibre still needs an independently checkable certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys, json, time, subprocess, traceback

agent=Path(__file__).resolve().parents[1]
output=agent/'outputs/post_CP27_eleven_flint_elimination.json'

if '--worker' not in sys.argv:
    start=time.perf_counter()
    try:
        proc=subprocess.run([sys.executable,__file__,'--worker'],capture_output=True,text=True,timeout=60)
        stdout,stderr=proc.stdout,proc.stderr
        if proc.returncode:
            payload={'status':'EXPLORATORY_FAILURE','returncode':proc.returncode,'stderr':stderr}
        else:
            payload=json.loads(output.read_text())
    except subprocess.TimeoutExpired as exc:
        stdout=exc.stdout or b'';stderr=exc.stderr or b''
        if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
        if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
        payload={'status':'EXPLORATORY_TIMEOUT','timeout_seconds':60,
                 'partial':json.loads(output.read_text()) if output.exists() else None}
    payload['actual_utc']=datetime.now(timezone.utc).isoformat()
    payload['total_runtime_seconds']=time.perf_counter()-start
    output.write_text(json.dumps(payload,indent=2)+'\n')
    (agent/'outputs/post_CP27_eleven_flint_elimination.stdout.txt').write_text(stdout)
    (agent/'outputs/post_CP27_eleven_flint_elimination.stderr.txt').write_text(stderr)
    print(stdout)
    print(json.dumps({k:payload[k] for k in ['status','actual_utc','total_runtime_seconds']}))
    raise SystemExit

sys.path.insert(0,'/tmp/research_sa15_flint')
import flint
from flint import nmod_mpoly_ctx,nmod_poly

start=time.perf_counter()
payload={'status':'RUNNING','python_flint_version':flint.__version__,'stages':[],
         'scope':'Exact elimination discovery only; not a fibre-exclusion or nodality proof.'}
ctx=nmod_mpoly_ctx.get(('L','v'),2,'lex')
L,v=ctx.gens()

def retain(stage,**kw):
    row={'stage':stage,'seconds':time.perf_counter()-start,**kw}
    payload['stages'].append(row)
    output.write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({k:row[k] for k in row if k not in ('factorization','polynomial_hex')}),flush=True)

def decode(item):
    terms={}
    for i,co in enumerate(item['numerator_L_coefficients_v_binary_hex']):
        p=int(co,16)
        while p:
            bit=p&-p;j=bit.bit_length()-1;terms[(i,j)]=1;p^=bit
    return ctx.from_dict(terms)

def univariate(poly):
    data=poly.to_dict();assert all(i==0 for i,j in data)
    degree=max((j for i,j in data),default=-1)
    return nmod_poly([int(data.get((0,j),0)) for j in range(degree+1)],2)

def encode_uni(poly):
    return hex(sum(int(c)<<i for i,c in enumerate(poly.coeffs())))

raw=json.loads((agent/'outputs/post_CP27_eleven_rational_quintic.json').read_text())
assert raw['status']=='PASS_UNIVERSAL_QUINTIC_IDENTITIES_ONLY'
f,g,c3,c2,e=map(decode,raw['triple_conditions'])
A=decode(raw['A'])
retain('decoded',degrees=[tuple(map(int,p.degrees())) for p in (f,g,c3,c2,e,A)])
d=f.gcd(g)
retain('generic_bivariate_gcd',gcd=str(d),degrees=tuple(map(int,d.degrees())))
ex=c3.resultant(c2,'L')
exu=univariate(ex)
exf=exu.factor()
retain('exceptional_c3_c2_resultant',degree=int(exu.degree()),polynomial_hex=encode_uni(exu),
       factorization=[{'factor_hex':encode_uni(p),'degree':int(p.degree()),'exponent':int(e)} for p,e in exf[1]])
res=f.resultant(g,'L')
ru=univariate(res)
retain('generic_resultant',degree=int(ru.degree()),polynomial_hex=encode_uni(ru))
fac=ru.factor()
retain('generic_resultant_factorization',factor_count=len(fac[1]),
       factorization=[{'factor_hex':encode_uni(p),'degree':int(p.degree()),'exponent':int(e)} for p,e in fac[1]])
payload['status']='PASS_EXACT_ELIMINATION_DISCOVERY_ONLY'
payload['runtime_seconds']=time.perf_counter()-start
output.write_text(json.dumps(payload,indent=2)+'\n')
