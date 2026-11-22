"""Exact bounded discovery of the exceptional A=0 repeated-B obstruction."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,subprocess
agent=Path(__file__).resolve().parents[1]
out=agent/'outputs/post_CP27_eleven_A_zero_elimination.json'
if '--worker' not in sys.argv:
    start=time.perf_counter()
    try:
        p=subprocess.run([sys.executable,__file__,'--worker'],capture_output=True,text=True,timeout=60)
        stdout,stderr=p.stdout,p.stderr
        result=json.loads(out.read_text()) if p.returncode==0 else {'status':'EXPLORATORY_FAILURE','returncode':p.returncode,'stderr':stderr}
    except subprocess.TimeoutExpired as e:
        stdout=e.stdout or b'';stderr=e.stderr or b''
        if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
        if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
        result={'status':'EXPLORATORY_TIMEOUT','partial':json.loads(out.read_text()) if out.exists() else None}
    result['actual_utc']=datetime.now(timezone.utc).isoformat();result['total_runtime_seconds']=time.perf_counter()-start
    out.write_text(json.dumps(result,indent=2)+'\n')
    (agent/'outputs/post_CP27_eleven_A_zero_elimination.stdout.txt').write_text(stdout)
    (agent/'outputs/post_CP27_eleven_A_zero_elimination.stderr.txt').write_text(stderr)
    print(stdout);print(json.dumps({k:result[k] for k in ['status','actual_utc','total_runtime_seconds']}))
    raise SystemExit
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx,nmod_poly
start=time.perf_counter();result={'status':'RUNNING','stages':[]}
ctx=nmod_mpoly_ctx.get(('T','L','v'),2,'lex');T,L,v=ctx.gens()
ctx2=nmod_mpoly_ctx.get(('L','v'),2,'lex')
def stage(name,**kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw};result['stages'].append(row)
    out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:row[k] for k in row if k not in ['factorization','polynomial_hex','polynomial_terms']}),flush=True)
def decode(item):
    data={}
    for i,c in enumerate(item['numerator_L_coefficients_v_binary_hex']):
        p=int(c,16)
        while p:
            x=p&-p;j=x.bit_length()-1;data[(0,i,j)]=1;p^=x
    return ctx.from_dict(data)
raw=json.loads((agent/'outputs/post_CP27_eleven_rational_quintic.json').read_text())
cb=raw['charpoly_B']
den=[max(f['denominator_exponents_v_vplus1_G'][i] for f in cb) for i in range(3)]
G=v**10+v**7+v**5+v**3+1
F=T-T;der=T-T
for i,item in enumerate(cb):
    a,b,c=(x-y for x,y in zip(den,item['denominator_exponents_v_vplus1_G']))
    coeff=decode(item)*v**a*(v+1)**b*G**c
    F+=coeff*T**(5-i)
    if (5-i)%2:der+=coeff*T**(4-i)
stage('cleared_characteristic',degrees=list(map(int,F.degrees())),denominator_exponents=den)
disc=F.resultant(der,'T')
assert disc.degrees()[0]<=0
disc2=disc.project_to_context(ctx2)
A=decode(raw['A']).project_to_context(ctx2)
stage('B_value_discriminant',degrees=list(map(int,disc2.degrees())),
      polynomial_terms=[[list(map(int,k)),int(c)] for k,c in disc2.to_dict().items()])
res=A.resultant(disc2,'L')
data=res.to_dict();assert all(i==0 for i,j in data)
degree=max((int(j) for i,j in data),default=-1)
poly=nmod_poly([int(data.get((0,j),0)) for j in range(degree+1)],2)
enc=lambda f:hex(sum(int(c)<<i for i,c in enumerate(f.coeffs())))
fac=poly.factor()
stage('A_zero_repeated_B_resultant',degree=degree,polynomial_hex=enc(poly),
      factorization=[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in fac[1]])
result['status']='PASS_A_ZERO_ELIMINATION_DISCOVERY_ONLY';result['runtime_seconds']=time.perf_counter()-start
result['scope']='Exact denominator-cleared discriminant and A-resultant only. Geometric special cases and an independently checked final certificate remain required.'
out.write_text(json.dumps(result,indent=2)+'\n')
