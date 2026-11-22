"""Exploratory exact norm-thirteen resultants and parameter-orbit test."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
from post_CP27_binary_coefficient_ring import E,cmul
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx,nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING','stages':[]}
def timeout(*unused):raise TimeoutError('Norm-thirteen parameter probe exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
def stage(name,**kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw};result['stages'].append(row)
    print(json.dumps({k:row[k] for k in row if k not in ['factorization','polynomial_hex']}),flush=True)
try:
    z,L=E(2),E([0,1]);a=z*z;delta=z+1;e=(delta*delta).inverse_constant()
    j=a*L+delta*delta;k=delta**4
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    H=a*a*L**6+(a*a+1)*L*L+(a+1)
    J=a*a*L**4+(a*a+1)
    b2=J*e*e+a*a*e**4*j*j
    b1=1+H*e+a*a*e**4*k
    P2=b2*b2*j*j+b1*b1+L*A*b2
    P1=b2*b2*k+L*A*b1+A*A*e
    T=b1**3+j*j*b1*b2*b2+k*b2**3
    ctx=nmod_mpoly_ctx.get(('L','z'),2,'lex')
    def poly(f):
        terms={}
        for i,v in enumerate(f.p):
            while v:
                bit=v&-v;terms[(i,bit.bit_length()-1)]=1;v^=bit
        return ctx.from_dict(terms)
    def uni(p):
        data=p.to_dict();assert all(i==0 for i,j in data)
        deg=max((int(j) for i,j in data),default=-1)
        return nmod_poly([int(data.get((0,j),0)) for j in range(deg+1)],2)
    enc=lambda p:hex(sum(int(c)<<i for i,c in enumerate(p.coeffs())))
    R1=uni(poly(P1).resultant(poly(P2),'L'))
    R2=uni(poly(A).resultant(poly(T),'L'))
    assert R1 and R2
    factorlists=[];factors=set()
    for name,p in [('generic',R1),('A_zero',R2)]:
        fac=[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in p.factor()[1]]
        factorlists.append(fac);factors.update(f['factor_hex'] for f in fac)
        stage(name,degree=int(p.degree()),polynomial_hex=enc(p),factorization=fac)
    make=lambda h:nmod_poly([(h>>i)&1 for i in range(h.bit_length())],2)
    x=nmod_poly([0,1],2)
    B=x*(x+1)
    for f in sorted(factors):
        q=make(int(f,16))
        if not (B%q):continue
        B*=q
    r=x*x+x;num=r*r+1;den=r**3
    co=B.coeffs();pull=nmod_poly([int(co[-1])],2);power=nmod_poly([1],2)
    for i in range(len(co)-2,-1,-1):
        power*=den;pull=pull*num+int(co[i])*power
    h=x**4+x
    while True:
        g=pull.gcd(h)
        if g==1:break
        pull= pull//g
    # Squarefree replacement is unnecessary for zero-set coverage.
    real=nmod_poly([int(c) if i%3 in (0,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    imag=nmod_poly([int(c) if i%3 in (1,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    orbitgcd=pull.gcd(pull.compose(x+1)).gcd(nmod_poly(list(reversed(pull.coeffs())),2)).gcd(real).gcd(imag)
    stage('five_parameter_test',bad_z_degree=int(B.degree()),pulled_degree=int(pull.degree()),gcd_degree=int(orbitgcd.degree()),gcd_hex=enc(orbitgcd))
    result.update({'status':'PASS_PARAMETER_DISCOVERY_ONLY','A':A.serial(),'P1':P1.serial(),'P2':P2.serial(),'T':T.serial(),
       'bad_z_polynomial_hex':enc(B),'pulled_bad_polynomial_hex':enc(pull),
       'scope':'Exact exploratory universal resultants and five-parameter gcd. Full fibre proof and independent certificate audits remain required; no norm-thirteen theorem asserted.'})
except Exception:result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_parameter_probe.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','actual_utc','runtime_seconds']},indent=2))
