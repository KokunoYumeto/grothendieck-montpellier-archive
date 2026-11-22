"""Exact reconstruction of retained norm-eleven parameter certificates.

Checks resultant factor-products and the orbit Bezout identity with independent
binary-polynomial arithmetic, and checks u*Z^2=t^2*Y^2 without inverting Y.
The resultants themselves are defined by their retained Sylvester inputs and
are recomputed in the separate FLINT elimination programs.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback
from post_CP27_binary_coefficient_ring import E,G,cmul,square,divmodp,gcdp,factor_power
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import nmod_poly

start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
result={'status':'RUNNING'}
try:
    raw=json.loads((agent/'outputs/post_CP27_eleven_rational_quintic.json').read_text())
    generic=json.loads((agent/'outputs/post_CP27_eleven_flint_elimination.json').read_text())
    azero=json.loads((agent/'outputs/post_CP27_eleven_A_zero_elimination.json').read_text())
    factors=set();checks=[]
    generic_R1=next(x for x in generic['stages'] if x['stage']=='generic_resultant')['polynomial_hex']
    for source in (generic,azero):
        for row in source['stages']:
            if 'factorization' not in row:continue
            p=1
            for f in row['factorization']:
                value=int(f['factor_hex'],16);factors.add(value)
                p=cmul(p,factor_power(value,f['exponent']))
            expected=int(row.get('polynomial_hex',generic_R1),16)
            assert p==expected,row['stage']
            checks.append({'stage':row['stage'],'degree':p.bit_length()-1,'factor_product_exact':True})
    factors.add(G)
    B=1
    for f in sorted(factors):B=cmul(B,f)
    H=(1<<4)|(1<<1)
    while True:
        g=gcdp(B,H)
        if g==1:break
        B,rem=divmodp(B,g);assert not rem
    assert B.bit_length()-1==3354
    assert divmodp(B,G)[1]==0
    make=lambda p:nmod_poly([(p>>i)&1 for i in range(p.bit_length())],2)
    enc=lambda p:sum(int(c)<<i for i,c in enumerate(p.coeffs()))
    V=nmod_poly([0,1],2)
    bf=make(B)
    translation=enc(bf.compose(V+1))
    inverse=int(bin(B)[2:][::-1],2)
    real=imag=0
    for i in range(B.bit_length()):
        if not ((B>>i)&1):continue
        if i%3 in (0,2):real^=1<<i
        if i%3 in (1,2):imag^=1<<i
    polynomials=[B,translation,inverse,real,imag]
    bezout=[make(1)];g=make(B)
    for p in polynomials[1:]:
        new,s,t=g.xgcd(make(p))
        assert new==s*g+t*make(p)
        bezout=[b*s for b in bezout]+[t]
        g=new
    assert g==1
    bez=[enc(x) for x in bezout]
    value=0
    for a,b in zip(bez,polynomials):value^=cmul(a,b)
    assert value==1

    decode=lambda f:E([int(x,16) for x in f['numerator_L_coefficients_v_binary_hex']],tuple(f['denominator_exponents_v_vplus1_G']))
    C=[decode(x) for x in raw['quintic_coefficients_ascending']]
    u=[decode(x) for x in raw['u_coefficients_ascending']]
    zero,one=E(),E(1);v=E(2);t=v*v
    alpha=E(1,(0,2,0));beta=alpha+1;gamma=E(G,(0,4,0))
    def trim(p):
        while p and not p[-1]:p.pop()
        return p
    def mult(p,q):
        ans=[zero]*(len(p)+len(q)-1)
        for i,x in enumerate(p):
            for j,y in enumerate(q):ans[i+j]=ans[i+j]+x*y
        while len(ans)>5:
            shift=len(ans)-6;lead=ans[-1]
            for i,x in enumerate(C):ans[shift+i]=ans[shift+i]+lead*x
            trim(ans)
        return ans
    Z=[gamma,beta,alpha]
    uz2=mult(u,mult(Z,Z))
    target=[zero,zero,t*t]
    assert trim([ (uz2[i] if i<len(uz2) else zero)+(target[i] if i<len(target) else zero)
                 for i in range(max(len(uz2),len(target)))])==[]
    result.update({'status':'PASS_EXACT_FACTOR_BEZOUT_AND_REGULAR_U_CERTIFICATE',
       'factor_product_checks':checks,
       'B_degree':3354,'B_hex':hex(B),
       'five_polynomials_hex':[hex(x) for x in polynomials],
       'bezout_coefficients_hex':[hex(x) for x in bez],
       'bezout_sum_checked_with_binary_arithmetic':True,
       'u_Z_squared_identity_without_Y_inversion':True,
       'scope':'Exact factor-product, univariate Bezout and regular-u identities; the three resultant computations and complete geometric interpretation remain separate audited inputs.'})
except Exception:
    result.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    result['actual_utc']=datetime.now(timezone.utc).isoformat();result['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/post_CP27_eleven_certificate_reconstruction.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in result if k not in ['B_hex','five_polynomials_hex','bezout_coefficients_hex']},indent=2))
