"""Exact exploratory refinement of the A=0 norm-thirteen obstruction.

The new necessary obstruction uses the residual ordinate slope.  This file
does not promote the geometric interpretation or claim a uniform theorem.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
from post_CP27_binary_coefficient_ring import E
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_mpoly_ctx,nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING'}
try:
    z,L=E(2),E([0,1]);a=z*z;delta=z+1;b=a+z+1;e=(delta*delta).inverse_constant()
    j=a*L+delta*delta;k=delta**4
    A=a*a*L**7+(a*a+1)*L**3+(a+1)*L+a
    H=a*a*L**6+(a*a+1)*L*L+(a+1)
    J=a*a*L**4+(a*a+1)
    b2=J*e*e+a*a*e**4*j*j
    b1=1+H*e+a*a*e**4*k
    P2=b2*b2*j*j+b1*b1+L*A*b2
    P1=b2*b2*k+L*A*b1+A*A*e
    T=b1**3+j*j*b1*b2*b2+k*b2**3
    change=a*L**4+b*L*L+L*(a*L**4+delta*delta*L*L+delta*L)
    ctx=nmod_mpoly_ctx.get(('L','z'),2,'lex')
    def poly(f):
        data={}
        for i,v in enumerate(f.p):
            while v:
                bit=v&-v;data[(i,bit.bit_length()-1)]=1;v^=bit
        return ctx.from_dict(data)
    def uni(f):
        data=f.to_dict();assert all(i==0 for i,j in data)
        deg=max((int(j) for i,j in data),default=-1)
        return nmod_poly([int(data.get((0,j),0)) for j in range(deg+1)],2)
    enc=lambda p:hex(sum(int(c)<<i for i,c in enumerate(p.coeffs())))
    res=lambda f,g:uni(poly(f).resultant(poly(g),'L'))
    generic=res(P1,P2); rt=res(A,T); rd=res(A,change)
    rb1=res(A,b1);rb2=res(A,b2)
    # Z=delta is excluded only in the A=0 sector; it forces L=delta/a.
    ell=delta*a.inverse_constant()
    special=a*a*ell**7+(a*a+1)*ell**3+(a+1)*ell+a
    assert len(special.p)==1
    make=lambda h:nmod_poly([(h>>i)&1 for i in range(h.bit_length())],2)
    rspecial=make(special.p[0])
    necessary=[generic,rt.gcd(rd),rb1.gcd(rb2),rspecial]
    assert all(necessary)
    x=nmod_poly([0,1],2);B=x*(x+1)
    data=[]
    for name,p in zip(['generic','nonconstant_B_A_zero','constant_B_A_zero','ordinate_denominator_A_zero'],necessary):
        fac=[{'factor_hex':enc(f),'degree':int(f.degree()),'exponent':int(n)} for f,n in p.factor()[1]]
        data.append({'name':name,'polynomial_hex':enc(p),'degree':int(p.degree()),'factorization':fac})
        for row in fac:
            f=make(int(row['factor_hex'],16))
            if B%f:B*=f
    r=x*x+x;num=r*r+1;den=r**3
    co=B.coeffs();pull=nmod_poly([int(co[-1])],2);power=nmod_poly([1],2)
    for i in range(len(co)-2,-1,-1):
        power*=den;pull=pull*num+int(co[i])*power
    h=x**4+x
    while True:
        g=pull.gcd(h)
        if g==1:break
        pull=pull//g
    real=nmod_poly([int(c) if i%3 in (0,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    imag=nmod_poly([int(c) if i%3 in (1,2) else 0 for i,c in enumerate(pull.coeffs())],2)
    orbit=pull.gcd(pull.compose(x+1)).gcd(nmod_poly(list(reversed(pull.coeffs())),2)).gcd(real).gcd(imag)
    out.update({'status':'PASS_EXPLORATORY_REFINED_RESULTANTS','A':A.serial(),'slope_change':change.serial(),
      'special_A_numerator_hex':hex(special.p[0]),'special_A_denominator':special.d,
      'resultants':data,'raw_resultants':{'A_T':enc(rt),'A_slope_change':enc(rd),'A_b1':enc(rb1),'A_b2':enc(rb2)},
      'bad_z_hex':enc(B),'bad_z_degree':int(B.degree()),'pulled_bad_hex':enc(pull),'pulled_bad_degree':int(pull.degree()),
      'five_parameter_gcd_hex':enc(orbit),'five_parameter_gcd_degree':int(orbit.degree()),
      'scope':'Exact exploratory arithmetic only. The residual-ordinate separation argument and all geometric fibre cases still require a full written proof and independent audit.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP28_thirteen_ordinate_parameter_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
