"""Exact residual-ordinate check over every nonpole exceptional factor for C0."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','factors':[]}
def timeout(*unused):raise TimeoutError('C0 norm17 exceptional gcd exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    data=json.loads((agent/'outputs/post_CP30_seventeen_four_unit_coordinates.json').read_text())
    model=next(row for row in data['models'] if row['name']=='zero_four_units')
    previous=json.loads((agent/'outputs/post_CP30_seventeen_four_unit_subresultants_zero_four_units.json').read_text())
    assert previous['status']=='PASS_LINEAR_COMBINATION_CERTIFICATES'
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(data['field_modulus']));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    enc=lambda c:sum(int(x)<<i for i,x in enumerate(c.to_list()))
    dec=lambda cs:R([val(c) for c in cs]);serial=lambda f:[enc(c) for c in f.coeffs()]
    zero,one=R.zero(),R.one()
    bad=dec(previous['nonpole_bad_polynomial'])
    def trim(a):
        a=list(a)
        while a and a[-1].is_zero():a.pop()
        return a
    def offdiagonal(coord):
        n,d=dec(coord['numerator']),dec(coord['denominator']);nc,dc=n.coeffs(),d.coeffs()
        coefficients=trim([d*(nc[i] if i<len(nc) else K(0))+n*(dc[i] if i<len(dc) else K(0)) for i in range(max(len(nc),len(dc)))])
        result=[zero]*(len(coefficients)-1);result[-1]=coefficients[-1]
        for i in range(len(coefficients)-2,0,-1):result[i-1]=coefficients[i]+p*result[i]
        assert coefficients[0]+p*result[0]==zero
        return result
    equations=[offdiagonal(model['coordinates'][name]) for name in ('L','M','nu')]
    factorization=bad.factor()[1]
    product=one
    for factor,exponent in factorization:product*=factor**exponent
    assert product*bad.coeffs()[-1]==bad
    for factor,exponent in factorization:
        def inverse(a):
            r0,r1=factor,a%factor;s0,s1=zero,one
            while not r1.is_zero():
                q,rem=divmod(r0,r1);r0,r1=r1,rem;s0,s1=s1,s0+q*s1
            assert r0.degree()==0
            return s0*(1/r0.coeffs()[0])%factor
        def add(a,b):return trim([((a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero))%factor for i in range(max(len(a),len(b)))])
        def scale(a,c):return trim([x*c%factor for x in a])
        def multiply(a,b):
            if not a or not b:return []
            result=[zero]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):result[i+j]=(result[i+j]+x*y)%factor
            return trim(result)
        def divide(a,b):
            a=trim(a);q=[zero]*max(0,len(a)-len(b)+1);inv=inverse(b[-1])
            while len(a)>=len(b):
                shift=len(a)-len(b);lead=a[-1]*inv%factor;q[shift]=lead
                a=add(a,[zero]*shift+scale(b,lead))
            return trim(q),a
        reduced=[trim([c%factor for c in equation]) for equation in equations]
        f=reduced[0];u=[[one],[],[]]
        for index in (1,2):
            g=reduced[index];v=[[],[],[]];v[index]=[one]
            while g:
                quotient,remainder=divide(f,g)
                w=[add(u[j],multiply(quotient,v[j])) for j in range(3)]
                f,g,u,v=g,remainder,v,w
            lead=inverse(f[-1]);f=scale(f,lead);u=[scale(x,lead) for x in u]
        reconstruction=[]
        for coefficient,equation in zip(u,reduced):reconstruction=add(reconstruction,multiply(coefficient,equation))
        assert reconstruction==f
        row={'factor':serial(factor),'factor_degree':int(factor.degree()),'exponent':int(exponent),'gcd_q_degree':len(f)-1,
             'gcd_q_coefficients':[serial(c) for c in f],'bezout_coefficients':[[serial(c) for c in polynomial] for polynomial in u]}
        out['factors'].append(row)
        print(json.dumps({'factor_degree':row['factor_degree'],'gcd_q_degree':row['gcd_q_degree'],'seconds':time.perf_counter()-start}),flush=True)
    out.update({'status':'PASS_EXACT_EXCEPTIONAL_GCDS','all_q_degrees_at_most_one':all(row['gcd_q_degree']<=1 for row in out['factors']),
                'scope':'Exact quotient-field polynomial Bezout identities on each retained exceptional irreducible factor. A gcd degree above1 is a genuine remaining fibre gate; no nodality is inferred in that case.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP30_seventeen_four_unit_exceptional_gcd.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='factors'},indent=2))
