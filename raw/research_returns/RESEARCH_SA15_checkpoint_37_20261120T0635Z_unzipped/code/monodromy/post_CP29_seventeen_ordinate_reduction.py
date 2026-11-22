"""Exact ordinate refinement for the norm17 quartic; no nodality claim."""
from pathlib import Path
from datetime import datetime, timezone
import json, signal, time, traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start=time.perf_counter()
agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING','stages':[]}
def timeout(*unused):raise TimeoutError('Norm17 ordinate reduction exceeded60seconds')
def stage(name):
    row={'stage':name,'seconds':time.perf_counter()-start}
    result['stages'].append(row);print(json.dumps(row),flush=True)
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    zz=symbols('z');base=GF(2).frac_field(zz);z=base.gens[0]
    R,p,T,V,L,beta=ring('p,T,V,L,beta',base);con=R.ground_new
    a,b=con(z*z),con(z*z+z+1)
    e=1/(b*b);j=a*L
    relp=p*p+L*p+V+e*(T*T+T)
    relT=T**4+T**3+j*T*T+b**4
    red=lambda f:f.div([relp,relT])[1]
    def coefficient(f,index,degree):
        out={}
        for monomial,value in f.items():
            if monomial[index]==degree:
                m=list(monomial);m[index]=0;out[tuple(m)]=value
        return R(out)
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    Zexplicit=a*a*p**8+(a*a+1)*p**4+(a+1)*p*p+a*p+beta
    Bfull=red(Zexplicit+T+b+A*p)
    Bpositive=Bfull-coefficient(Bfull,1,0)
    Q=red(Bpositive*Bpositive+L*A*Bpositive+A*A*e*(T*T+T))
    r=[coefficient(Q,1,i) for i in (1,2,3)]
    c=T+b
    inverseT=(T**3+T*T+j*T)/(b**4)
    assert not red(T*inverseT+1)
    K=red(L+c*c*inverseT*inverseT+b/a)
    d1=a*p**4+b*p*p;d2=d1*d1+b*p
    q=T*d2+c*b
    P1=c*d1+(T*d1+c*d2)*L+q*(L*L+K)
    P0=(T*d1+c*d2)*K+q*L*K
    D=red(c*c+T*c*L+T*T*K)
    N=red(c*P1+T*P0)
    assert not red(a*T*D+b*c**4)
    k0=b*b*(b+j)
    inverse_c4_numerator=red((c**3+c*c+(b+j)*c+b*b)**4)
    assert not red(c**4*inverse_c4_numerator+k0**4)
    inner=red(c*L*L+(c+T*L)*K)
    Nv=red(k0**4*(d1+L*d2)+a*T*c*inner*inverse_c4_numerator)
    assert not red(D*Nv+N*k0**4)
    coefficient_p=coefficient(Nv,0,1)
    assert coefficient_p.degree(T)<=0 and Nv.degree(p)<=1
    corrected=red(A*(Nv+coefficient_p*p)+coefficient_p*Bfull)
    ordinate=[coefficient(corrected,1,i) for i in (1,2,3)]
    assert all(f.degree(p)<=0 and f.degree(V)<=0 and f.degree(beta)<=0 for f in ordinate)
    minors={'N12':r[0]*ordinate[1]+r[1]*ordinate[0],
            'N13':r[0]*ordinate[2]+r[2]*ordinate[0],
            'N23':r[1]*ordinate[2]+r[2]*ordinate[1]}
    stage('rational_ordinate_and_positive_coefficients')
    def serialize(f):
        coeffs=[coefficient(f,3,i).get((0,0,0,0,0),base.zero) for i in range(max(0,f.degree(L))+1)]
        enc=lambda poly:sum((int(v)%2)<<m[0] for m,v in poly.items())
        return [[enc(c.numer),enc(c.denom)] for c in coeffs]
    result.update({'status':'PASS_EXACT_ORDINATE_REFINEMENT_ONLY',
                   'degrees_L':{name:f.degree(L) for name,f in minors.items()},
                   'polynomials':{name:serialize(f) for name,f in minors.items()},
                   'ordinate_positive_coefficients':[str(f) for f in ordinate],
                   'scope':'When b*A*(b+aL) is nonzero, three equal residual divisors force the three positive-coefficient cross minors to vanish in addition to F=G=0. Exact ordinate algebra only; special L, A=0 and modulus exceptions remain untreated.'})
except Exception:result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_ordinate_reduction.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('polynomials','ordinate_positive_coefficients')},indent=2))
