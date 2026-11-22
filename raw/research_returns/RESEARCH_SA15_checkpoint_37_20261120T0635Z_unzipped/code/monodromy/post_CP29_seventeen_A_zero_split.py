"""Exact split A-zero ordinate necessary conditions for norm17, exploratory."""
from pathlib import Path
from datetime import datetime, timezone
import json, sys, time, traceback
from sympy import symbols
from sympy.polys.domains import GF
from sympy.polys.rings import ring
from post_CP27_binary_coefficient_ring import cmul, divmodp, gcdp
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx, nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING'}
try:
    zz=symbols('z');base=GF(2).frac_field(zz);z=base.gens[0]
    R,p,T,V,L,beta=ring('p,T,V,L,beta',base);con=R.ground_new
    a,b=con(z*z),con(z*z+z+1);e=1/(b*b);j=a*L
    relp=p*p+L*p+V+e*(T*T+T)
    relT=T**4+T**3+j*T*T+b**4
    red=lambda f:f.div([relp,relT])[1]
    def coeff(f,index,degree):
        out={}
        for m,c in f.items():
            if m[index]==degree:
                n=list(m);n[index]=0;out[tuple(n)]=c
        return R(out)
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    Z=a*a*p**8+(a*a+1)*p**4+(a+1)*p*p+a*p+beta
    B=red(Z+T+b+A*p)
    b1,b2,b3=[coeff(B,1,i) for i in (1,2,3)]
    FB=b1*b3+j*b3*b3+b2*b3+b2*b2
    GB=b**4*b3**3+(b3+b2)**2*b1
    K=a*a*L**8+b*b*L**4+a*L**3
    d1=a*p**4+b*p*p;d2=d1*d1+b*p
    assert coeff(red(d1+L*d2),0,1)==K
    ctx=nmod_mpoly_ctx.get(('L','z'),2,'lex')
    enc=lambda pol:hex(sum(int(c)<<i for i,c in enumerate(pol.coeffs())))
    def polynomial(f):
        data=[coeff(f,3,i).get((0,0,0,0,0),base.zero) for i in range(max(0,f.degree(L))+1)]
        binary=lambda pol:sum((int(c)%2)<<m[0] for m,c in pol.items())
        ds=[binary(c.denom) for c in data];den=1
        for d in ds:den=cmul(den,divmodp(d,gcdp(den,d))[0])
        terms={}
        for i,(c,d) in enumerate(zip(data,ds)):
            mult,rem=divmodp(den,d);assert not rem
            v=cmul(binary(c.numer),mult)
            while v:
                bit=v&-v;terms[(i,bit.bit_length()-1)]=1;v^=bit
        return ctx.from_dict(terms)
    def uni(f):
        data=f.to_dict();assert all(i==0 for i,j in data)
        degree=max((int(j) for i,j in data),default=-1)
        return nmod_poly([int(data.get((0,j),0)) for j in range(degree+1)],2)
    Q=a*L**3+a*L*L+(a+1)*L+a
    S=a*L**4+a*L**3+L*L+1
    R2=a*L*L+a*L+1
    assert A==Q*S and K==L**3*Q*R2
    AA,QQ,SS=polynomial(A),polynomial(Q),polynomial(S)
    Fresult=uni(SS.resultant(polynomial(FB),'L'))
    Gresult=uni(SS.resultant(polynomial(GB),'L'))
    Kresult=uni(SS.resultant(polynomial(R2),'L'))
    special=uni(AA.resultant(polynomial(b+j),'L'))
    generic=Fresult.gcd(Gresult)
    old=json.loads((agent/'outputs/post_CP29_seventeen_quartic_reduction.json').read_text())
    def decode_binary(n):
        out=base.zero
        while n:
            bit=n&-n;out+=z**(bit.bit_length()-1);n^=bit
        return out
    HH=R.zero
    for degree,(num,den) in enumerate(old['polynomials']['H']):
        HH+=con(decode_binary(num)/decode_binary(den))*L**degree
    collision=uni(QQ.resultant(polynomial(HH),'L'))
    result['diagnostic_degrees']={'F':int(Fresult.degree()),'G':int(Gresult.degree()),'generic':int(generic.degree()),'K_complement':int(Kresult.degree()),'special':int(special.degree()),'Q_collision':int(collision.degree())}
    assert generic and Kresult and special and collision
    bad=generic*Kresult*special*collision
    result.update({'status':'PASS_A_ZERO_NECESSARY_CONDITIONS_ONLY',
                   'degrees':{'F_resultant':int(Fresult.degree()),'G_resultant':int(Gresult.degree()),'joint_generic':int(generic.degree()),'ordinate_p_slope':int(Kresult.degree()),'special_denominator':int(special.degree())},
                   'bad_z_polynomial_hex':enc(bad),
                   'factorization':[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in bad.factor()[1]],
                   'scope':'The universal common cubic Q is separated: use the collision discriminant on Q=0, and three equal B-values on S=0 when the ordinate slope and its denominator are nonzero. Their remaining exceptional resultants are added. Exact necessary conditions, not a full norm17 theorem.'})
except Exception:result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_A_zero_split.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('bad_z_polynomial_hex','factorization')},indent=2))
