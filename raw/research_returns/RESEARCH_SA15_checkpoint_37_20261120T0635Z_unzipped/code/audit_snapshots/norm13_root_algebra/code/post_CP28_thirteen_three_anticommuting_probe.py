"""Seven-point interpolation using three independent anticommuting units.

The finite-field identities are exploratory.  No nodality is inferred.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,traceback,signal
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','stages':[]}
def timeout(*unused):raise TimeoutError('Three-unit interpolation exceeded60seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
def stage(name,**kw):
    row={'stage':name,'seconds':time.perf_counter()-start,**kw};out['stages'].append(row);print(json.dumps(row),flush=True)
try:
    modulus=(1<<12)|(1<<7)|(1<<6)|(1<<5)|(1<<3)|(1<<1)|1
    def mul(x,y):
        r=0
        while y:
            if y&1:r^=x
            y>>=1;x<<=1
            if x>>12:x^=modulus
        return r
    def power(x,n):
        r=1
        while n:
            if n&1:r=mul(r,x)
            x=mul(x,x);n>>=1
        return r
    zi=next(x for x in range(2,4096) if power(x,3)^power(x,2)^1==0)
    ai=mul(zi,zi);bi=ai^zi^1
    AS={}
    for x in range(4096):AS.setdefault(mul(x,x)^x,x)
    auto_int=[]
    for shift in range(1,4096):
        v=mul(ai,power(shift,4))^mul(bi,power(shift,2));u=mul(v,v)^mul(bi,shift)
        if mul(u,u)!=mul(ai,shift):continue
        c=mul(ai,power(shift,5))^mul(bi,power(shift,3))
        if c not in AS:continue
        if mul(u,power(shift,2))^mul(v,shift)==1:auto_int.append((shift,u,v,AS[c]))
    def comm_int(g,h):
        s,u,v,_=g;t,U,V,_=h
        return mul(u,mul(t,t))^mul(v,t)^mul(U,mul(s,s))^mul(V,s)
    triple_int=[]
    for g in auto_int:
        if g[0]!=1:continue
        for h in auto_int:
            if comm_int(g,h)!=1:continue
            for j in auto_int:
                if j[0] in [0,g[0],h[0],g[0]^h[0]]:continue
                if comm_int(g,j)==comm_int(h,j)==1:triple_int.append((g,h,j))
    assert triple_int
    cc=symbols('c');K=MonogenicFiniteExtension(Poly(cc**12+cc**7+cc**6+cc**5+cc**3+cc+1,cc,modulus=2))
    K.gcd=lambda x,y:K.one if x or y else K.zero;K.quo=K.exquo=lambda x,y:x/y
    powers=[K.generator**i for i in range(12)]
    convert=lambda n:sum((powers[i] for i in range(12) if n>>i&1),K.zero)
    def encode(v):
        coeff=v.rep.to_list();return sum(int(c)<<i for i,c in enumerate(reversed(coeff)))
    z=convert(zi);a=z*z;b=a+z+1
    autos=[tuple(convert(x) for x in g) for g in auto_int]
    triples=[tuple(tuple(convert(x) for x in g) for g in row) for row in triple_int]
    selected=triples[0]
    stage('three_units',order_four_translation_count=len(autos),triple_count=len(triples),automorphisms=[[encode(x) for x in g] for g in selected])
    R,X,p=ring('X,p',K);cv=lambda v:R.ground_new(v)
    shifts=[g[0] for g in selected]
    ys=[p*p*g[1]+p*g[2]+cv(g[3]) for g in selected]
    derivs=[(p+cv(s))**4*a+(p+cv(s))**2*b for s in shifts]
    def ell(cs,s):return cs[0]+cs[1]*s+cs[2]*s*s
    def coefficients(cs):
        F=[cs[1]*Y+ell(cs,s)*D for s,Y,D in zip(shifts,ys,derivs)]
        s,t=shifts[:2]
        c3=(F[0]+F[1])/(s*s+t*t);c1=F[0]+c3*s*s
        V1=ell(cs,s)*ys[0]+c1*s+c3*s**3
        V2=ell(cs,t)*ys[1]+c1*t+c3*t**3
        c4=(V2*s*s+V1*t*t)/(s*s*t**4+s**4*t*t)
        c2=(V1+c4*s**4)/(s*s)
        return F,[c1,c2,c3,c4]
    rows=[[],[]]
    for j in range(3):
        cs=[R.one if i==j else R.zero for i in range(3)]
        F,bs=coefficients(cs);c1,c2,c3,c4=bs;s=shifts[2]
        rows[0].append(F[2]+c1+c3*s*s)
        rows[1].append(ell(cs,s)*ys[2]+c1*s+c2*s*s+c3*s**3+c4*s**4)
    rr,ss=rows
    cs=[rr[1]*ss[2]+rr[2]*ss[1],rr[2]*ss[0]+rr[0]*ss[2],rr[0]*ss[1]+rr[1]*ss[0]]
    assert any(cs)
    _,bs=coefficients(cs);allcoeff=cs+bs
    common=next(f for f in allcoeff if f)
    for f in allcoeff:
        if f:common=common.gcd(f)
    allcoeff=[f.exquo(common) for f in allcoeff]
    cs=allcoeff[:3];c1,c2,c3,c4=allcoeff[3:]
    linear=cs[0]+cs[1]*X+cs[2]*X*X
    polynomial=c1*X+c2*X*X+c3*X**3+c4*X**4
    for s,Y,D in zip(shifts,ys,derivs):
        assert not (linear.compose(X,cv(s))*Y+polynomial.compose(X,cv(s)))
        assert not (cs[1]*Y+linear.compose(X,cv(s))*D+c1+c3*s*s)
    fun=lambda x:x**5*a+x**3*b
    norm=polynomial**2+linear*polynomial+linear**2*(fun(p+X)+fun(p))
    prescribed=X
    for s in shifts:prescribed*=(X+cv(s))**2
    quotient,remainder=norm.div(prescribed)
    assert not remainder and quotient.degree(X)==2
    extract=lambda i:R.from_dict({(0,ep):v for (ex,ep),v in quotient.items() if ex==i})
    residual=[extract(i) for i in [2,1,0]]
    assert residual[0]==cs[2]**2*a
    def serial(f):return [[list(e),encode(c)] for e,c in f.terms()]
    stage('interpolation',common_degree=common.degree(p),kernel_degrees=[f.degree(p) for f in cs],residual_degrees=[f.degree(p) for f in residual])
    out.update({'status':'PASS_THREE_UNIT_INTERPOLATION_ONLY','field_modulus':'c^12+c^7+c^6+c^5+c^3+c+1','parameter_z':zi,
      'automorphisms_encoded':[[encode(x) for x in g] for g in selected],
      'common_factor':serial(common),'coefficients':[serial(f) for f in allcoeff],
      'residual_coefficients':[serial(f) for f in residual],
      'scope':'Exact finite-parameter interpolation and norm factorization. The possible interpolation rank drops and all theta fibres remain unclassified.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_three_anticommuting_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],'traceback':out.get('traceback')},indent=2))
