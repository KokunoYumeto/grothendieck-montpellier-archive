"""Universal exact interpolation for 3+g+h of Rosati norm eleven.

No theta nodality or monodromy statement is inferred by this program.
"""
from pathlib import Path
import datetime,json,signal,time,traceback
from itertools import permutations
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start=time.perf_counter();root=Path(__file__).resolve().parent.parent
def timeout(*unused):raise TimeoutError('Norm-eleven interpolation exceeded 60 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
result={'status':'RUNNING'}
try:
    rr=symbols('r');base=GF(2).frac_field(rr);r=base.gens[0]
    R,p,w,beta,t,X=ring('p,w,beta,t,X',base)
    con=R.ground_new;D=con(r*r);z=con((r*r+1)/r**3);a=z*z;b=a+z+1
    gt=t*t+t+D;ft=(a*t**5+b*t**3).div([gt])[1]
    relations=[w*w+w+ft,beta*beta+beta+z+1,gt]
    red=lambda f:f.div(relations)[1]
    u=z*(t+con(r));v=z*t*t+t+con(1/r**2)
    F=lambda x:a*x**5+b*x**3
    gp=z*p*p+(z+1)*p+beta;hp=u*p*p+v*p+w
    d1=a*p**4+b*p*p;d2=d1*d1+b*p
    Y=red(hp+t*t*gp+D*d1)
    C=red(t*Y);Z=red(Y+t*D*(gp+d1+d2))
    A1=red(C*d1);A2=red(Z*d1+C*d2)
    A3=red(Z*(gp+d1)+C*(gp+d1+d2))
    poly=A1*X+A2*X*X+A3*X**3
    linear=Z*X+C
    checks=[]
    def check(name,f):
        q=red(f);assert not q,(name,str(q));checks.append(name)
    check('third_order_zero_at_P_linear',A1+C*d1)
    check('third_order_zero_at_P_quadratic',A2+Z*d1+C*d2)
    check('zero_at_gP',(Z+C)*gp+A1+A2+A3)
    check('zero_at_hP',(Z*t+C)*hp+A1*t+A2*t*t+A3*t**3)
    norm=red(poly*poly+linear*poly+linear*linear*(F(p+X)+F(p)))
    prescribed=X**3*(X+1)*(X+t)
    rb=red(A3*A3+a*(p+t+1)*Z*Z)
    rc=red((b+a*((t+1)*p+(t+1)**2+t))*Z*Z+a*C*C+(t+1)*A3*A3)
    residual=a*Z*Z*X*X+rb*X+rc
    check('norm_factorization',norm+prescribed*residual)
    E=red(t*gp+hp)
    check('cubic_coefficient_simplification',t*t*D*Z*A3+t*t*Z*Z*E+C*C*Z)
    Q=red(ft+t*t*(z+1))
    check('Y_E_relation',E*E+a*p*D*D+Y+Q)
    alpha=t/D
    gamma=con((r**6+r**5+r+1)/r**4)*t+con((r**3+r+1)/r**2)
    A4=a*D;A2=con((r**6+r**2+1)/r**4);A1star=a*D*D
    Y0=w+t*t*beta
    check('Y_quartic',Y+A4*p**4+A2*p*p+A1star*p+Y0)
    check('Z_quadratic_in_Y',Z+alpha*Y*Y+(alpha+1)*Y+gamma)
    check('arbitrary_section_last_row_L',t*hp+t*t*d1+t**3*(gp+d1)+t*Y)
    check('arbitrary_section_last_row_C',hp+t*d1+t*t*d2+t**3*(gp+d1+d2)+Z)
    check('A3_reduced_formula',D*A3+Z*E+Y*Y)
    check('linear_residual_coefficient',D*D*rb+(a*D*D*(t+1)+Y+Q)*Z*Z+Y**4)
    Mnum=a*Z*Z*p*p+rb*p+rc
    check('constant_residual_coefficient',Mnum+(t+1)*rb+(a*t+b)*Z*Z+a*Z*Z*p*p+rb*p+a*t*t*Y*Y)
    result={'status':'PASS_UNIVERSAL_INTERPOLATION_IDENTITIES_ONLY','checks':checks,
      'Y':str(Y),'Z':str(Z),'gamma':str(gamma),'Q':str(Q),
      'scope':'All universal interpolation rows and both residual-coordinate identities. Parameter elimination and the full geometric proof are separate.'}
except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0);result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/post_CP27_eleven_verified_interpolation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
