"""Exact ordinate-refined resultant discovery for norm17; no geometric claim."""
from pathlib import Path
from datetime import datetime, timezone
import json, signal, sys, time, traceback
from post_CP27_binary_coefficient_ring import cmul, divmodp, gcdp
sys.path.insert(0, '/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx, nmod_poly

start = time.perf_counter()
agent = Path(__file__).resolve().parents[1]
result = {'status':'RUNNING','stages':[]}
def timeout(*unused):
    raise TimeoutError('Norm17 resultant probe exceeded60seconds')
def stage(name, **kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw}
    result['stages'].append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in ('polynomial_hex','factorization')},indent=2),flush=True)
signal.signal(signal.SIGALRM,timeout)
signal.alarm(60)
try:
    data=json.loads((agent/'outputs/post_CP29_seventeen_quartic_reduction.json').read_text())
    assert data['status']=='PASS_EXACT_QUARTIC_NECESSARY_CONDITIONS_ONLY'
    ctx=nmod_mpoly_ctx.get(('L','z'),2,'lex')
    def to_poly(coeffs):
        denominator=1
        for numerator,d in coeffs:
            denominator=cmul(denominator,divmodp(d,gcdp(denominator,d))[0])
        terms={}
        for i,(numerator,d) in enumerate(coeffs):
            multiplier,remainder=divmodp(denominator,d)
            assert remainder==0
            v=cmul(numerator,multiplier)
            while v:
                bit=v&-v
                terms[(i,bit.bit_length()-1)]=1
                v^=bit
        return ctx.from_dict(terms),denominator
    ordinate=json.loads((agent/'outputs/post_CP29_seventeen_ordinate_reduction.json').read_text())
    assert ordinate['status']=='PASS_EXACT_ORDINATE_REFINEMENT_ONLY'
    all_polynomials={**data['polynomials'],**ordinate['polynomials']}
    polynomials={name:to_poly(value)[0] for name,value in all_polynomials.items()}
    result['cleared_denominators']={name:hex(to_poly(value)[1]) for name,value in all_polynomials.items()}
    A,F,G,H=[polynomials[name] for name in ('A','F','G','H')]
    saturations=[]
    for name,poly in [('F',F),('G',G)]:
        iterations=0
        while True:
            g=poly.gcd(A)
            if g.is_constant():
                break
            poly=poly//g
            iterations+=1
        saturations.append({'name':name,'iterations':iterations,'degrees':[int(x) for x in poly.degrees()]})
        if name=='F':F=poly
        else:G=poly
    stage('saturation_by_A',saturations=saturations,common_F_G=str(F.gcd(G)))
    def uni(p):
        terms=p.to_dict()
        assert all(i==0 for i,j in terms)
        degree=max((int(j) for i,j in terms),default=-1)
        return nmod_poly([int(terms.get((0,j),0)) for j in range(degree+1)],2)
    enc=lambda p:hex(sum(int(c)<<i for i,c in enumerate(p.coeffs())))
    R1=uni(F.resultant(G,'L'))
    stage('initial_generic_resultant',degree=int(R1.degree()),polynomial_hex=enc(R1))
    for name in ('N12','N13','N23'):
        other=polynomials[name]
        test=uni(F.resultant(other,'L'))
        R1=R1.gcd(test)
        stage('refine_'+name,extra_degree=int(test.degree()),gcd_degree=int(R1.degree()),polynomial_hex=enc(R1))
    special=ctx.from_dict({(1,2):1,(0,2):1,(0,1):1,(0,0):1})
    special_bad=uni(F.resultant(special,'L')).gcd(uni(G.resultant(special,'L')))
    R1=(R1*special_bad)//R1.gcd(special_bad)
    stage('restore_special_ordinate_denominator',special_degree=int(special_bad.degree()),degree=int(R1.degree()),polynomial_hex=enc(R1))
    R2=uni(A.resultant(H,'L'))
    stage('A_zero_resultant',degree=int(R2.degree()),polynomial_hex=enc(R2))
    assert R1 and R2,'A resultant is identically zero: stronger fibre conditions are needed.'
    factors=set()
    for name,p in [('generic',R1),('A_zero',R2)]:
        fs=[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in p.factor()[1]]
        factors.update(row['factor_hex'] for row in fs)
        stage(name+'_factorization',factorization=fs)
    make=lambda h:nmod_poly([(h>>i)&1 for i in range(h.bit_length())],2)
    x=nmod_poly([0,1],2)
    B=x*(x+1)*(x*x+x+1)
    for f in sorted(factors):
        factor=make(int(f,16))
        if B%factor:B*=factor
    r=x*x+x
    num,den=r*r+1,r**3
    coefficients=B.coeffs()
    pull=nmod_poly([int(coefficients[-1])],2)
    power=nmod_poly([1],2)
    for i in range(len(coefficients)-2,-1,-1):
        power*=den
        pull=pull*num+int(coefficients[i])*power
    H4=x**4+x
    while True:
        g=pull.gcd(H4)
        if g==1:break
        pull=pull//g
    real=nmod_poly([int(c) if i%3 in (0,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    imag=nmod_poly([int(c) if i%3 in (1,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    orbit=pull.gcd(pull.compose(x+1)).gcd(nmod_poly(list(reversed(pull.coeffs())),2)).gcd(real).gcd(imag)
    stage('five_parameter_test',bad_z_degree=int(B.degree()),pull_degree=int(pull.degree()),gcd_degree=int(orbit.degree()),gcd_hex=enc(orbit),factorization=[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in orbit.factor()[1]])
    result.update({'status':'PASS_RESULTANT_DISCOVERY_ONLY','bad_z_polynomial_hex':enc(B),'pulled_bad_polynomial_hex':enc(pull),'scope':'Exact ordinate-refined resultants and five-transform gcd only. Special ordinate denominator is restored explicitly; A=0 uses the original overestimate. No norm17 theorem.'})
except Exception:
    result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0)
    result['actual_utc']=datetime.now(timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_ordinate_parameter_probe.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','actual_utc','runtime_seconds')},indent=2))
