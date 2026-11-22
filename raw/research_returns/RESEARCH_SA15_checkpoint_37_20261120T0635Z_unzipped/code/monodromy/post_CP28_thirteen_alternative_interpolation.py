"""Bounded exact interpolation for 1+2g+2h+2gh at the exceptional surface.

This exploratory program checks identities over a specified finite field
and retains all rational coordinates.  It asserts no nodality theorem.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,traceback,signal
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','stages':[]}
def timeout(*unused):raise TimeoutError('Alternative norm-thirteen interpolation exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
def stage(name,**kw):
    d={'stage':name,'seconds':time.perf_counter()-start,**kw};out['stages'].append(d);print(json.dumps(d),flush=True)
try:
    cc=symbols('c')
    K=MonogenicFiniteExtension(Poly(cc**6+cc+1,cc,modulus=2))
    K.gcd=lambda x,y:K.one if x or y else K.zero
    K.quo=K.exquo=lambda x,y:x/y
    generator=K.generator;vals=[sum((generator**i for i in range(6) if n>>i&1),K.zero) for n in range(64)]
    encode={str(v):n for n,v in enumerate(vals)}
    AS={}
    for v in vals:AS.setdefault(str(v*v+v),v)
    choices=[]
    for xi in vals:
        if xi**4==xi:continue
        r=xi**2+xi;t=xi**2;z=(r*r+1)/r**3;a=z*z;b=a+z+1
        if str(z+1) in AS and str(a*t**5+b*t**3) in AS:
            choices.append((xi,r,t,z,a,b,AS[str(z+1)],AS[str(a*t**5+b*t**3)]))
    assert choices,'No complete quaternion presentation over the chosen field.'
    xi,r,t,z,a,b,beta,w=choices[0]
    cg=z*t*t+(z+1)*t
    assert (z*z+z+1)**5==z**6
    stage('parameters',xi_r_t_z_beta_w=[encode[str(v)] for v in [xi,r,t,z,beta,w]])
    R,X,p=ring('X,p',K);one=R.one
    cv=lambda v:R.ground_new(v)
    G=p*p*z+p*(z+1)+cv(beta)
    H=p*p*(z*(t+r))+p*(z*t*t+t+1/(r*r))+cv(w)
    shifts=[K.one,t,t+1];ys=[G,H,G+H+cv(cg)]
    derivs=[(p+cv(s))**4*a+(p+cv(s))**2*b for s in shifts]
    def ell(cs,s):return cs[0]+cs[1]*s+cs[2]*s*s
    def derivative_coefficients(cs):
        F=[cs[1]*y+ell(cs,s)*v for s,y,v in zip(shifts,ys,derivs)]
        c3=(F[0]+F[1])/(1+t*t);c1=F[0]+c3
        return F,c1,c3
    rows=[[],[]]
    for j in range(3):
        cs=[one if i==j else R.zero for i in range(3)]
        F,c1,c3=derivative_coefficients(cs)
        rows[0].append(F[2]+c1+c3*(t+1)**2)
        rows[1].append(sum((ell(cs,s)*y for s,y in zip(shifts,ys)),R.zero)+c3*(t*t+t))
    rr,ss=rows
    cs=[rr[1]*ss[2]+rr[2]*ss[1],rr[2]*ss[0]+rr[0]*ss[2],rr[0]*ss[1]+rr[1]*ss[0]]
    assert any(cs)
    for row in rows:assert not sum((x*y for x,y in zip(row,cs)),R.zero)
    stage('two_row_kernel',row_degrees=[[f.degree(p) for f in row] for row in rows],kernel_degrees=[f.degree(p) for f in cs])
    F,c1,c3=derivative_coefficients(cs)
    V1=ell(cs,K.one)*ys[0]+c1+c3
    Vt=ell(cs,t)*ys[1]+c1*t+c3*t**3
    c4=(Vt+V1*t*t)/(t**4+t*t);c2=V1+c4
    allcoeff=cs+[c1,c2,c3,c4]
    common=next(f for f in allcoeff if f)
    for f in allcoeff:
        if f:common=common.gcd(f)
    allcoeff=[f.exquo(common) for f in allcoeff]
    cs=allcoeff[:3];c1,c2,c3,c4=allcoeff[3:]
    linear=cs[0]+cs[1]*X+cs[2]*X*X
    polynomial=c1*X+c2*X*X+c3*X**3+c4*X**4
    for s,Y,D in zip(shifts,ys,derivs):
        assert not ((linear.compose(X,cv(s)))*Y+polynomial.compose(X,cv(s)))
        assert not (cs[1]*Y+linear.compose(X,cv(s))*D+c1+c3*s*s)
    fun=lambda x:x**5*a+x**3*b
    norm=polynomial**2+linear*polynomial+linear**2*(fun(p+X)+fun(p))
    prescribed=X
    for s in shifts:prescribed*= (X+cv(s))**2
    quotient,remainder=norm.div(prescribed)
    assert not remainder and quotient.degree(X)==2
    extract=lambda i:R.from_dict({(0,ep):v for (ex,ep),v in quotient.items() if ex==i})
    lead=extract(2);middle=extract(1);constant=extract(0)
    assert lead==cs[2]**2*a
    def serial(f):return [[list(e),encode[str(c)]] for e,c in f.terms()]
    stage('primitive_norm',common_degree=common.degree(p),coefficient_degrees=[f.degree(p) for f in allcoeff],residual_degrees=[f.degree(p) for f in [lead,middle,constant]])
    out.update({'status':'PASS_FINITE_PARAMETER_INTERPOLATION_ONLY','field_modulus':'c^6+c+1',
      'parameters_encoded':{name:encode[str(v)] for name,v in [('xi',xi),('r',r),('t',t),('z',z),('beta',beta),('w',w)]},
      'common_factor':serial(common),'coefficient_names':['l0','l1','l2','c1','c2','c3','c4'],
      'coefficients':[serial(f) for f in allcoeff],'residual_coefficients':[serial(f) for f in [lead,middle,constant]],
      'scope':'Exact identities for a fixed parameter on mu^5=1 only. No all-fibre classification, theta nodality or norm-thirteen full group is asserted.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_alternative_interpolation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],'traceback':out.get('traceback')},indent=2))
