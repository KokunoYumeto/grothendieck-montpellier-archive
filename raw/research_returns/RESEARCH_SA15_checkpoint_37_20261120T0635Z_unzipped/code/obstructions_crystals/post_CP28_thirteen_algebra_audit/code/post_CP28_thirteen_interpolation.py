"""Exploratory universal interpolation for 3+2g of Rosati norm thirteen."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,signal,traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING'}
def timeout(*unused):raise TimeoutError('Norm-thirteen interpolation exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    zz=symbols('z');base=GF(2).frac_field(zz);z=base.gens[0]
    R,p,beta,X,l,c=ring('p,beta,X,l,c',base);con=R.ground_new
    a=con(z*z);b=con(z*z+z+1);delta=con(z+1)
    relation=beta*beta+beta+delta
    red=lambda f:f.div([relation])[1]
    G=con(z)*p*p+delta*p+beta
    d1=a*p**4+b*p*p;d2=d1*d1+b*p
    F=G+d1;Z=red(delta+G+d1+d2)
    A3=red((Z+delta)*F+delta*d2)
    A1=delta*d1;A2=Z*d1+delta*d2
    checks=[]
    def check(name,q):
        v=red(q);assert not v,(name,str(v));checks.append(name)
    arbitrary_k=(l+c)*F+c*d2
    derivative_at_g=l*G+(l+c)*(d1+delta)+c*d1+arbitrary_k
    check('arbitrary_section_derivative_row',derivative_at_g+delta*l+Z*c)
    check('F_squared_relation',F*F+Z+a*p)
    check('cubic_coefficient',A3+Z*(F+delta)+delta*delta)
    check('Z_additive_polynomial',Z+a*a*p**8+(a*a+1)*p**4+(a+1)*p*p+a*p+beta+delta)
    linear=Z*X+delta;poly=A1*X+A2*X*X+A3*X**3
    fun=lambda x:a*x**5+b*x**3
    norm=red(poly*poly+linear*poly+linear*linear*(fun(p+X)+fun(p)))
    Rb=A3*A3+a*p*Z*Z;Rc=delta*Z*Z+a*delta*delta
    check('norm_factorization',norm+X**3*(X+1)**2*(a*Z*Z*X*X+Rb*X+Rc))
    check('linear_residual_coefficient',Rb+Z**3+delta*delta*Z*Z+delta**4)

    S,p,Z,U,L,beta=ring('p,Z,U,L,beta',base);con=S.ground_new
    a=con(z*z);delta=con(z+1);e=1/(delta*delta)
    j=a*L+delta*delta;k=delta**4
    relp=p*p+L*p+U+e*Z;relZ=Z**3+j*Z*Z+k
    reduce=lambda f:f.div([relp,relZ])[1]
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    H=a*a*L**6+(a*a+1)*L*L+(a+1)
    J=a*a*L**4+(a*a+1)
    b2=J*e*e+a*a*e**4*j*j
    b1=1+H*e+a*a*e**4*k
    b0=H*U+J*U*U+a*a*U**4+beta+delta+a*a*e**4*j*k
    Zexpression=a*a*p**8+(a*a+1)*p**4+(a+1)*p*p+a*p+beta+delta
    assert not reduce(Zexpression+Z+A*p+b2*Z*Z+b1*Z+b0)
    checks.append('eighth_degree_reduction')
    P2=b2*b2*j*j+b1*b1+L*A*b2
    P1=b2*b2*k+L*A*b1+A*A*e
    B=b2*Z*Z+b1*Z
    assert not reduce(B*B+L*A*B+A*A*e*Z+P2*Z*Z+P1*Z+b2*b2*j*k)
    checks.append('generic_triple_coefficients')
    # Collision of the three quadratic B-values: remaining root j+b1/b2.
    T=b1**3+j*j*b1*b2*b2+k*b2**3
    assert not ((j*b2+b1)**3+j*(j*b2+b1)**2*b2+k*b2**3+T)
    checks.append('A_zero_collision_polynomial')
    result.update({'status':'PASS_UNIVERSAL_INTERPOLATION_AND_CUBIC_REDUCTION_ONLY',
        'checks':checks,'A':str(A),'P1':str(P1),'P2':str(P2),'T':str(T),
        'scope':'Universal identities only. A uniform good-parameter and complete exceptional-fibre proof are not yet supplied.'})
except Exception:result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_interpolation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in result if k not in ['A','P1','P2','T']},indent=2))
