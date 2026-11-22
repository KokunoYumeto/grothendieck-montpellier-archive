"""Finite prototype of a three-fibre obstruction in the cubic Z-algebra.

Only the open A(ell)!=0 is tested. No universal geometric claim is made.
"""
from pathlib import Path
import datetime,hashlib,json,signal,time,traceback
from sympy.polys.rings import ring
from sympy.polys.groebnertools import groebner
from gf16_exact_domain import K16,F16,verify_field

start=time.perf_counter();root=Path(__file__).resolve().parent.parent
result={'status':'RUNNING'}
def timeout(*unused):raise TimeoutError('Cubic-algebra prototype exceeded 60 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    field=verify_field()
    source=root/'outputs/probe_seven_finite_mumford.json';data=json.loads(source.read_text())
    r,z,t,beta,w=map(F16,data['choice_r_z_t_beta_w'])
    D=r*r;a=z*z;b=a+z+1;cg=z*D+t;c=D*cg
    Z0=w+t*t*beta+t*cg;E0=w+t*beta+(t+1)*cg;q0=(E0*E0+Z0)/(D*D)
    kappa=(b+a*(D+1))/a
    R,x,l,d=ring('x,l,d',K16,order='lex')
    j=a*D*D*l+D*D*q0;k=D*D*cg**4
    cubic=x**3+j*x**2+k
    red=lambda f:f.div([cubic])[1]
    invx=(x*x+j*x)/k
    assert red(x*invx)==1
    u=red(d+kappa+c*c*invx**2)
    A4=a*D;A2=a*D*(D+1)+1;A1=a*D*D
    A=A4*l**3+A2*l+A1
    B=red(x+Z0+A4*(l*l*u+u*u)+A2*u)
    obstruction=red(B*B+l*A*B+u*A*A)
    def xcoeff(f,i):
        return R.from_dict({(0,el,ed):co for (ex,el,ed),co in f.items() if ex==i})
    equations=[xcoeff(obstruction,i) for i in range(3)]
    # Reduce the stored numerator of nu modulo p^2+ell*p+u.
    nrows=data['sparse_integer_coordinates']['nu']['numerator']
    pn=[(R.zero,R.one)]
    for n in range(1,max(row[0] for row in nrows)+1):
        aa,bb=pn[-1];pn.append((red(l*aa+bb),red(u*aa)))
    an=sum((pn[n][0]*F16(co) for n,co in nrows),R.zero)
    bn=sum((pn[n][1]*F16(co) for n,co in nrows),R.zero)
    # Check the exact denominator really is a scalar multiple of Z(p)^3.
    Rp,p=ring('p',K16)
    build=lambda rows:sum((p**e*F16(co) for e,co in rows),Rp.zero)
    sc=data['sparse_integer_coordinates'];Z=build(sc['Z']['numerator'])/F16(sc['Z']['denominator'][0][1])
    quotient,remainder=build(sc['nu']['denominator']).div([Z**3])
    assert not remainder and quotient[0].degree(p)==0
    denominator_scalar=quotient[0][(0,)]
    nu_times_A=red(invx**3*red(an*B+bn*A))/denominator_scalar
    equations.extend(xcoeff(nu_times_A,i) for i in (1,2))
    print(json.dumps({'stage':'equations','degrees':[max(map(sum,f.keys()),default=-1) for f in equations],'terms':[len(f) for f in equations]}),flush=True)
    S,s,L,dd=ring('s,l,d',K16,order='lex')
    convert=lambda f:S.from_dict({(0,el,ed):co for (ex,el,ed),co in f.items() if not ex})
    assert all(f.degree(x)<=0 for f in equations)
    G=groebner([convert(f) for f in equations]+[s*convert(A)+1],S,method='f5b')
    result={'status':'COMPLETED_FINITE_CUBIC_ALGEBRA','basis':[str(g) for g in G],
      'unit_ideal':len(G)==1 and G[0]==1,'equations':[str(f) for f in equations],
      'open_denominator_A':str(A),'nu_denominator_scalar':int(denominator_scalar),
      'field_checks':field,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'scope':'One finite parameter and the open A(ell)!=0 only; no complete or universal triple-fibre conclusion.'}
except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0)
    result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/probe_seven_cubic_algebra.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
