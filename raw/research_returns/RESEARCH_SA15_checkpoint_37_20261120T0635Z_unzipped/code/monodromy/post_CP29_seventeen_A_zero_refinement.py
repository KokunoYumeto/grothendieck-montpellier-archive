"""Exploratory exact A-zero ordinate separation for norm17."""
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
    AA=polynomial(A)
    Fresult=uni(AA.resultant(polynomial(FB),'L'))
    Gresult=uni(AA.resultant(polynomial(GB),'L'))
    Kresult=uni(AA.resultant(polynomial(K),'L'))
    special=uni(AA.resultant(polynomial(b+j),'L'))
    generic=Fresult.gcd(Gresult)
    result['diagnostic_degrees']={'F':int(Fresult.degree()),'G':int(Gresult.degree()),'generic':int(generic.degree()),'K':int(Kresult.degree()),'special':int(special.degree())}
    result['zero_resultant_gcds']={'K':str(AA.gcd(polynomial(K))),'special':str(AA.gcd(polynomial(b+j)))}
    assert generic and Kresult and special, 'A universal exceptional branch persists; no nonzero bad polynomial asserted.'
    bad=generic*Kresult*special
    result.update({'status':'PASS_A_ZERO_NECESSARY_CONDITIONS_ONLY',
                   'degrees':{'F_resultant':int(Fresult.degree()),'G_resultant':int(Gresult.degree()),'joint_generic':int(generic.degree()),'ordinate_p_slope':int(Kresult.degree()),'special_denominator':int(special.degree())},
                   'bad_z_polynomial_hex':enc(bad),
                   'factorization':[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(e)} for f,e in bad.factor()[1]],
                   'scope':'At A=0, K*(b+aL)!=0, equal ordinate determines at most one p for each T, so triple fibres require three equal B-values and FB=GB=0. The K=0 and b+aL=0 loci are added as overestimates. No complete norm17 proof.'})
except Exception:result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP29_seventeen_A_zero_refinement.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('bad_z_polynomial_hex','factorization')},indent=2))
