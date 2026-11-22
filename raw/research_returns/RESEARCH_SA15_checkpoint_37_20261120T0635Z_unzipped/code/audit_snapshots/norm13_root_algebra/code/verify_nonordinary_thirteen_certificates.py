"""Reconstruct the generic and exceptional norm-thirteen certificates.

Generic resultants are rebuilt by a binary-polynomial Bareiss determinant,
independently of the discovery resultant call.  The exceptional affine
certificate is checked as an explicit polynomial Bezout identity, not by
assuming a specialization theorem for a generic gcd.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,traceback,signal
from post_CP27_binary_coefficient_ring import cmul,square,divmodp,gcdp,factor_power
sys.path.insert(0,'/tmp/research_sa15_flint')
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
start=time.perf_counter();agent=Path(__file__).resolve().parents[1]
out={'status':'RUNNING','checks':[]}
def timeout(*unused):raise TimeoutError('Norm-thirteen reconstruction exceeded120seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(120)
def load(stem):return json.loads((agent/'outputs'/f'{stem}.json').read_text())
def check(name,condition=True):
    assert condition,name;out['checks'].append(name)
try:
    generic=load('post_CP28_thirteen_parameter_probe')
    def exact(a,b):
        q,r=divmodp(a,b);assert r==0;return q
    def resultant(f,g):
        n,m=len(f)-1,len(g)-1;N=n+m
        mat=[[0]*N for _ in range(N)]
        for i in range(m):mat[i][i:i+n+1]=list(reversed(f))
        for i in range(n):mat[m+i][i:i+m+1]=list(reversed(g))
        previous=1
        for k in range(N-1):
            if mat[k][k]==0:
                j=next(j for j in range(k+1,N) if mat[j][k]);mat[k],mat[j]=mat[j],mat[k]
            pivot=mat[k][k]
            for i in range(k+1,N):
                for j in range(k+1,N):mat[i][j]=exact(cmul(pivot,mat[i][j])^cmul(mat[i][k],mat[k][j]),previous)
                mat[i][k]=0
            previous=pivot
        return mat[-1][-1]
    coeff=lambda name:[int(h,16) for h in generic[name]['numerator_L_coefficients_v_binary_hex']]
    r1=resultant(coeff('P1'),coeff('P2'));r2=resultant(coeff('A'),coeff('T'))
    check('binary_Bareiss_generic_resultant',r1==int(generic['stages'][0]['polynomial_hex'],16))
    check('binary_Bareiss_A_zero_resultant',r2==int(generic['stages'][1]['polynomial_hex'],16))
    factors=set()
    for row,actual in zip(generic['stages'][:2],[r1,r2]):
        product=1
        for f in row['factorization']:
            v=int(f['factor_hex'],16);factors.add(v);product=cmul(product,factor_power(v,f['exponent']))
        check('binary_factor_product_'+row['stage'],product==actual)
    Bz=cmul(2,3)
    for f in sorted(factors):
        if divmodp(Bz,f)[1]:Bz=cmul(Bz,f)
    check('bad_parameter_product',Bz==int(generic['bad_z_polynomial_hex'],16))
    r=6;num=square(r)^1;den=factor_power(r,3);power=1;B=1
    for i in range(Bz.bit_length()-2,-1,-1):
        power=cmul(power,den);B=cmul(B,num)^(power if (Bz>>i)&1 else 0)
    H4=(1<<4)|(1<<1)
    while True:
        g=gcdp(B,H4)
        if g==1:break
        B=exact(B,g)
    check('homogeneous_parameter_pullback',B==int(generic['pulled_bad_polynomial_hex'],16))
    translated=real=imag=0
    for i in range(B.bit_length()):
        if not (B>>i)&1:continue
        j=i
        while True:
            translated^=1<<j
            if not j:break
            j=(j-1)&i
        if i%3 in (0,2):real^=1<<i
        if i%3 in (1,2):imag^=1<<i
    reciprocal=int(bin(B)[2:][::-1],2)
    polys=[B,translated,reciprocal,real,imag]
    def xgcd(a,b):
        x0,x1,y0,y1=1,0,0,1
        while b:
            q,r=divmodp(a,b);a,b=b,r;x0,x1=x1,x0^cmul(q,x1);y0,y1=y1,y0^cmul(q,y1)
        return a,x0,y0
    G=polys[0];weights=[1]
    for f in polys[1:]:
        G,u,v=xgcd(G,f);weights=[cmul(u,w) for w in weights]+[v]
    D12=(1<<12)|(1<<9)|(1<<6)|(1<<3)|1
    target=factor_power(D12,5)^factor_power(H4,12)
    check('five_parameter_gcd',G==target==int(generic['stages'][2]['gcd_hex'],16))
    combination=0
    for u,f in zip(weights,polys):combination^=cmul(u,f)
    check('explicit_five_parameter_Bezout',combination==target)
    out['generic_certificate']={'resultants_binary_hex':[hex(r1),hex(r2)],'bad_z_binary_hex':hex(Bz),
       'pulled_bad_binary_hex':hex(B),'five_polynomials_binary_hex':[hex(f) for f in polys],
       'bezout_binary_hex':[hex(f) for f in weights],'gcd_binary_hex':hex(target)}

    source=load('post_CP28_thirteen_three_anticommuting_probe')
    coords=load('post_CP28_thirteen_three_unit_coordinates')
    poles=load('post_CP28_thirteen_pole_fibres')
    linear=load('post_CP28_thirteen_linear_subresultants')['pairs'][0]
    modulus=sum(int(c)<<i for i,c in enumerate(coords['field_modulus']))
    def powmod(a,n,mod):
        b=1
        while n:
            if n&1:b=divmodp(cmul(a,b),mod)[1]
            a=divmodp(square(a),mod)[1];n>>=1
        return b
    check('finite_field_modulus_irreducible',powmod(2,1<<12,modulus)==2 and
          gcdp(powmod(2,1<<6,modulus)^2,modulus)==1 and gcdp(powmod(2,1<<4,modulus)^2,modulus)==1)
    K=fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)(coords['field_modulus']));R=fq_default_poly_ctx(K);p=R.gen()
    val=lambda n:K([(n>>i)&1 for i in range(12)])
    enc=lambda c:sum(int(v)<<i for i,v in enumerate(c.to_list()))
    dec=lambda a:R([val(x) for x in a]);serial=lambda f:[enc(c) for c in f.coeffs()]
    zero,one=R.zero(),R.one();z=val(source['parameter_z']);a=z*z;b=a+z+1
    check('exceptional_modulus',z**3+z*z+1==K(0) and b**5==z**6)
    autos=[list(map(val,row)) for row in source['automorphisms_encoded']]
    for i,(s,u,v,beta) in enumerate(autos):
        check(f'automorphism_{i}',u*u==a*s and v*v+u==b*s and v==a*s**4+b*s*s and beta*beta+beta==a*s**5+b*s**3)
        check(f'order_four_{i}',u*s*s+v*s==K(1))
    for i in range(3):
        for j in range(i):
            s,u,v,_=autos[i];t,U,V,_=autos[j]
            check(f'anticommutation_{i}_{j}',u*t*t+v*t+U*s*s+V*s==K(1))
    check('translation_independence',len({enc(sum((autos[i][0] for i in range(3) if m>>i&1),K(0))) for m in range(8)})==8)
    shifts=[row[0] for row in autos];ys=[p*p*u+p*v+R([beta]) for s,u,v,beta in autos]
    derivatives=[(p+R([s]))**4*a+(p+R([s]))**2*b for s in shifts]
    ell=lambda cs,s:cs[0]+cs[1]*s+cs[2]*s*s
    def interpolation(cs):
        F=[cs[1]*Y+ell(cs,s)*D for s,Y,D in zip(shifts,ys,derivatives)]
        s,t=shifts[:2];c3=(F[0]+F[1])*(1/(s*s+t*t));c1=F[0]+c3*s*s
        V1=ell(cs,s)*ys[0]+c1*s+c3*s**3;V2=ell(cs,t)*ys[1]+c1*t+c3*t**3
        c4=(V2*s*s+V1*t*t)*(1/(s*s*t**4+s**4*t*t));c2=(V1+c4*s**4)*(1/(s*s))
        return F,[c1,c2,c3,c4]
    rows=[[],[]]
    for j in range(3):
        cs=[one if i==j else zero for i in range(3)];F,bs=interpolation(cs);c1,c2,c3,c4=bs;s=shifts[2]
        rows[0].append(F[2]+c1+c3*s*s)
        rows[1].append(ell(cs,s)*ys[2]+c1*s+c2*s*s+c3*s**3+c4*s**4)
    r,s=rows;cs=[r[1]*s[2]+r[2]*s[1],r[2]*s[0]+r[0]*s[2],r[0]*s[1]+r[1]*s[0]]
    F,bs=interpolation(cs);coefficients=cs+bs
    def sparse(rows):
        f=zero
        for (ex,ep),c in rows:assert ex==0;f+=p**ep*val(c)
        return f
    expected=[sparse(row) for row in source['coefficients']]
    check('independent_interpolation_reconstruction',coefficients==expected)
    def xgcd_field(a,b):
        x0,x1,y0,y1=one,zero,zero,one
        while not b.is_zero():
            q,r=divmod(a,b);a,b=b,r;x0,x1=x1,x0+q*x1;y0,y1=y1,y0+q*y1
        scale=1/a.coeffs()[-1];return a*scale,x0*scale,y0*scale
    G,u,v=xgcd_field(cs[0],cs[1]);G,w,t=xgcd_field(G,cs[2]);rank_weights=[w*u,w*v,t]
    check('every_finite_interpolation_rank_two',sum((c*x for c,x in zip(rank_weights,cs)),zero)==one)
    def trim(v):
        v=list(v)
        while v and v[-1].is_zero():v.pop()
        return v
    def qadd(x,y):return trim([(x[i] if i<len(x) else zero)+(y[i] if i<len(y) else zero) for i in range(max(len(x),len(y)))])
    def qmul(x,y):
        if not x or not y:return []
        z=[zero]*(len(x)+len(y)-1)
        for i,u in enumerate(x):
            for j,v in enumerate(y):z[i+j]+=u*v
        return trim(z)
    c1,c2,c3,c4=bs;polynomial=[zero,c1,c2,c3,c4];d1=p**4*a+p*p*b
    difference=[zero,d1,p*b,R([b]),p*a,R([a])]
    norm=qadd(qadd(qmul(polynomial,polynomial),qmul(cs,polynomial)),qmul(qmul(cs,cs),difference))
    prescribed=[zero,one]
    for s in shifts:prescribed=qmul(prescribed,[R([s*s]),zero,one])
    A,B,C=map(sparse,source['residual_coefficients'])
    check('independent_norm_factorization',norm==qmul(prescribed,[C,B,A]) and A==cs[2]*cs[2]*a)
    Ln,Ld=map(dec,[coords['coordinates']['L']['numerator'],coords['coordinates']['L']['denominator']])
    Mn,Md=map(dec,[coords['coordinates']['M']['numerator'],coords['coordinates']['M']['denominator']])
    check('residual_rational_coordinates',Ln*A==B*Ld and Mn*A==(p*p*A+p*B+C)*Md)
    l2=cs[2];monic_l2=l2*(1/l2.coeffs()[-1])
    def offdiag(n,d):
        nc,dc=n.coeffs(),d.coeffs();f=trim([d*(nc[i] if i<len(nc) else K(0))+n*(dc[i] if i<len(dc) else K(0)) for i in range(max(len(nc),len(dc)))])
        q=[zero]*(len(f)-1);q[-1]=f[-1]
        for i in range(len(f)-2,0,-1):q[i-1]=f[i]+p*q[i]
        assert f[0]+p*q[0]==zero
        return q
    EL,EM=offdiag(Ln,Ld),offdiag(Mn,Md)
    U,V=[[dec(row) for row in linear[name]] for name in ['bezout_first','bezout_second']]
    S=[dec(row) for row in linear['linear_coefficients']]
    check('full_polynomial_Bezout_identity',qadd(qmul(U,EL),qmul(V,EM))==S)
    G,u,v=xgcd_field(S[0],S[1]);check('only_pole_zeros_of_linear_coefficients',G==monic_l2**44)
    check('linear_coefficient_Bezout',u*S[0]+v*S[1]==monic_l2**44)
    check('squarefree_pole_scheme',l2.degree()==8 and l2.gcd(l2.derivative()).degree()==0)
    check('simple_pole_chart',l2.gcd(c4).degree()==0 and (B+c4*c4)%l2==zero)
    gb,ib,_=xgcd_field(B,l2);check('pole_middle_unit',gb==one)
    value=(p+C*ib)%l2;check('recorded_pole_value',value==dec(poles['pole_value']))
    minimal=dec(poles['minimal_polynomial']);check('separable_pole_value_polynomial',minimal.degree()==8 and minimal.gcd(minimal.derivative()).degree()==0)
    powers=[one]
    for i in range(8):powers.append(powers[-1]*value%l2)
    evaluated=zero
    for c in reversed(minimal.coeffs()):evaluated=(evaluated*value+R([c]))%l2
    check('pole_value_polynomial_identity',evaluated==zero)
    mat=[[powers[j][i] for j in range(8)] for i in range(8)]
    for j in range(8):
        pivot=next(i for i in range(j,8) if mat[i][j]!=K(0));mat[j],mat[pivot]=mat[pivot],mat[j]
        scalar=1/mat[j][j];mat[j]=[x*scalar for x in mat[j]]
        for i in range(8):
            if i!=j:
                scalar=mat[i][j];mat[i]=[x+scalar*y for x,y in zip(mat[i],mat[j])]
    check('pole_value_generates_degree_eight_algebra',all(mat[i][j]==K(int(i==j)) for i in range(8) for j in range(8)))
    out.update({'status':'PASS_COMPLETE_THIRTEEN_CERTIFICATE_RECONSTRUCTION','exceptional_field_modulus_hex':hex(modulus),
       'interpolation_rank_Bezout':[serial(f) for f in rank_weights],
       'linear_coefficient_Bezout':[serial(u),serial(v)],'linear_coefficient_gcd':serial(G),
       'scope':'Exact reconstruction of the coefficient inputs, generic resultants, parameter Bezout identity, exceptional automorphisms, interpolation/norm, affine linear combination and all pole-fibre algebra. The accompanying written proof supplies the geometric implications.'})
except Exception:out.update({'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()})
finally:
    signal.alarm(0);out['actual_utc']=datetime.now(timezone.utc).isoformat();out['runtime_seconds']=time.perf_counter()-start
    (agent/'outputs/verify_nonordinary_thirteen_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':len(out['checks']),'actual_utc':out['actual_utc'],'runtime_seconds':out['runtime_seconds'],'traceback':out.get('traceback')},indent=2))
