"""Exploratory exact interpolation for 3+g+h of Rosati norm eleven.

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
    # Common roots of Y,Z are exactly the failure of the interpolation line.
    A4=a*D;monicY=Y.mul_ground(r**4/(r**4+1))
    reduceY=lambda f:red(f.div([monicY])[1])
    zr=reduceY(Z)
    columns=[reduceY(zr*p**i) for i in range(4)]
    def coeff_p(f,i):return R.from_dict({(0,ew,eb,et,ex):co for (ep,ew,eb,et,ex),co in f.items() if ep==i})
    matrix=[[coeff_p(columns[jj],ii) for jj in range(4)] for ii in range(4)]
    det=R.zero
    for permutation in permutations(range(4)):
        term=R.one
        for ii in range(4):term=red(term*matrix[ii][permutation[ii]])
        det=red(det+term)
    normw=red(det*red(det.compose(w,w+1)))
    normb=red(normw*red(normw.compose(beta,beta+1)))
    assert normb.degree(w)<=0 and normb.degree(beta)<=0
    normt=red(normb*red(normb.compose(t,t+1)))
    assert normt.degree(t)<=0
    outnorm='0' if not normt else {'numerator':str(normt[(0,0,0,0,0)].numer.factor_list()),'denominator':str(normt[(0,0,0,0,0)].denom.factor_list())}
    result={'status':'PASS_INTERPOLATION_IDENTITIES_ONLY','checks':checks,
      'Y':str(Y),'Z':str(Z),'C':str(C),'Z_mod_Y':str(zr),
      'kernel_theta_resultant':str(det),'kernel_theta_resultant_norm':outnorm,
      'scope':'Exact interpolation and kernel-theta obstruction for a proposed norm-eleven map only. No triple-fibre or nodality inference.'}
except Exception:result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0);result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/nonordinary_eleven_q8_interpolation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
