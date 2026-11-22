"""Finite-parameter norm-eleven quintic fibre diagnostic.

No geometric or uniform conclusion is drawn from this exploration.
"""
from pathlib import Path
import datetime,json,signal,time,traceback
from sympy.polys.rings import ring
from sympy.polys.matrices import DomainMatrix
from gf16_exact_domain import K16,F16,verify_field

start=time.perf_counter();root=Path(__file__).resolve().parent.parent
def timeout(*unused):raise TimeoutError('Norm-eleven finite quintic exceeded 60 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
result={'status':'RUNNING'}
try:
    verify_field();r,z,t,beta,w=map(F16,[2,6,8,4,4])
    a=z*z;b=a+z+1;D=r*r
    Rp,p=ring('p',K16)
    gp=z*p*p+(z+1)*p+beta
    hp=z*(t+r)*p*p+(z*t*t+t+1/D)*p+w
    d1=a*p**4+b*p*p;d2=d1*d1+b*p
    Y=hp+t*t*gp+D*d1
    Z=Y+t*D*(gp+d1+d2)
    alpha=t/D
    quotient,remainder=(Z+alpha*Y*Y).div([Y])
    assert quotient[0].degree(p)==0 and remainder.degree(p)==0
    bb=quotient[0][(0,)];cc=remainder[(0,)]
    assert cc
    Q=a*t**5+b*t**3+t*t*(z+1)
    A4=a*D;A2=Y[(2,)];A1=Y[(1,)]
    RL,L=ring('L',K16);FF=RL.to_field();l=FF.gens[0];K=FF.to_domain()
    R,v=ring('v',K)
    con=lambda c:R.ground_new(FF(c))
    ll=R.ground_new(l)
    L0=a*D*D*(l+t+1)+Q
    A=A4*l**3+A2*l+A1
    theta=con(alpha)+con(bb)*v+con(cc)*v*v
    C=(R.ground_new(L0)*v+1)*theta**2+v
    red=lambda f:f.div([C])[1]
    invv=(C+C[(0,)]).exquo(v)/C[(0,)]
    assert red(v*invv)==1
    u=con(t*t)*v+R.ground_new(t*t*L0)*v*v
    B=red(invv+con(A4)*(ll*ll*u+u*u)+con(A2)*u)
    P=red(B*B+R.ground_new(l*A)*B+R.ground_new(A*A)*u)
    def characteristic(f):
        columns=[red(f*v**i) for i in range(5)]
        matrix=[[column.get((j,),K.zero) for column in columns] for j in range(5)]
        return DomainMatrix.from_list(matrix,K).charpoly_berk()
    cp=characteristic(P)
    one,c4,c3,c2,c1,c0=cp
    # Triple-root criteria for T^5+c4T^4+c3T^3+c2T^2+c1T+c0.
    cond1=c2**4+c3**3*c2**2+c1*c3**4
    cond2=c2**5+c4*c2**4*c3+c3**3*c2**3+c2**3*c3**3+c1*c2*c3**4+c0*c3**5
    # The two middle terms cancel in characteristic two; retain explicit source.
    def gcd_many(polys):
        nonzero=[f for f in polys if f]
        if not nonzero:return RL.zero
        out=nonzero[0]
        for f in nonzero[1:]:out=out.gcd(f)
        return out
    generic_gcd=gcd_many([cond1.numer,cond2.numer])
    exceptional_gcd=gcd_many([c3.numer,c2.numer,(c0+c4*c1).numer])
    print(json.dumps({'stage':'generic_triple','cp_degrees':[[f.numer.degree(),f.denom.degree()] for f in cp],'generic_gcd':str(generic_gcd),'exceptional_gcd':str(exceptional_gcd)}),flush=True)
    cb=characteristic(B)
    # Discriminant of the five B-values; A=0 only needs it to be nonzero.
    RT,T=ring('T',K)
    ch=sum((T**(5-i)*co for i,co in enumerate(cb)),RT.zero)
    disc=ch.resultant(ch.diff(T))
    discriminant_A_gcd=A.numer.gcd(disc.numer) if disc else A.numer
    result={'status':'COMPLETED_FINITE_QUINTIC_DIAGNOSTIC',
      'choice_r_z_t_beta_w':[2,6,8,4,4],
      'Z_as_quadratic_in_Y':{'alpha':int(alpha),'beta':int(bb),'gamma':int(cc)},
      'charpoly_P':[str(f) for f in cp],
      'triple_generic_gcd':str(generic_gcd),
      'triple_exceptional_gcd':str(exceptional_gcd),
      'A_zero_discriminant_gcd':str(discriminant_A_gcd),
      'A':str(A),'L0':str(L0),
      'scope':'A fixed finite-parameter diagnostic; leading-coefficient, denominator and special-coordinate cases remain to be proved separately.'}
except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0);result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/probe_eleven_finite_quintic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
