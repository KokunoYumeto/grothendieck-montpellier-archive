"""AM-K033: finite exact Frobenius/trace/weighted-pairing certificate.

This checks coefficient matrices and arithmetic, not the infinite display,
theta-image or selected asymptotic theorem. Those are proved in the report.
"""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
from enlarged_host_ranks_characters_alpha_certificate import parameter_check

p=11
n=29


def canon(f):
    f=list(f)
    return tuple((x-f[-1])%p for x in f[:-1])+(0,)


zero=(0,)*n
one=(1,)+(0,)*(n-1)


def add(x,y):
    return canon([(a+b)%p for a,b in zip(x,y)])


def scale(x,a):
    return canon([a*b for b in x])


def mul(x,y):
    ans=[0]*n
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:
                    ans[(i+j)%n]=(ans[(i+j)%n]+a*b)%p
    return canon(ans)


def power(x,k):
    ans=one
    while k:
        if k&1:
            ans=mul(ans,x)
        x=mul(x,x)
        k//=2
    return ans


def aut(x,a):
    ans=[0]*n
    for j,c in enumerate(x):
        ans[j*a%n]=(ans[j*a%n]+c)%p
    return canon(ans)


def sm(xs):
    ans=zero
    for x in xs:
        ans=add(ans,x)
    return ans


def fqadd(x,y):
    return ((x[0]+y[0])%p,(x[1]+y[1])%p)


def fqneg(x):
    return ((-x[0])%p,(-x[1])%p)


def fqmul(x,y):
    return ((x[0]*y[0]+2*x[1]*y[1])%p,
            (x[0]*y[1]+x[1]*y[0])%p)


fqzero=(0,0)
fqone=(1,0)


def fqpow(x,k):
    out=fqone
    while k:
        if k&1:out=fqmul(out,x)
        x=fqmul(x,x)
        k//=2
    return out


def fqinv(x):
    assert x!=fqzero
    ans=fqpow(x,119)
    assert fqmul(x,ans)==fqone
    return ans


def fqsum(xs):
    out=fqzero
    for x in xs:out=fqadd(out,x)
    return out


def transpose(A):
    return list(map(list,zip(*A)))


def fqmm(A,B):
    return [[fqsum(fqmul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def fqinverse2(A):
    det=fqadd(fqmul(A[0][0],A[1][1]),fqneg(fqmul(A[0][1],A[1][0])))
    di=fqinv(det)
    ans=[[fqmul(di,A[1][1]),fqmul(di,fqneg(A[0][1]))],
         [fqmul(di,fqneg(A[1][0])),fqmul(di,A[0][0])]]
    assert fqmm(A,ans)==[[fqone,fqzero],[fqzero,fqone]]
    return ans


def vfac(k):
    out=0
    while k:
        k//=11
        out+=k
    return out


def digits(k):
    out=0
    while k:
        out+=1
        k//=11
    return out


def main():
    H={1,12,17,28}
    cosets=[{pow(2,l,29)*h%29 for h in H} for l in range(7)]
    assert 11 in cosets[4] and 121%29 in cosets[1]
    periods=[canon([int(j in C) for j in range(29)]) for C in cosets]
    a=[-8,-4,-2,-5,-2,-4,-4]
    e0=scale(sm(scale(periods[i],a[i]) for i in range(7)),pow(29,-1,11))
    es=[aut(e0,pow(2,j,29)) for j in range(7)]
    U=[[aut(es[j],pow(2,l,29)) for j in range(7)] for l in range(7)]
    for k in range(7):
        for l in range(7):
            assert sm(mul(U[j][k],U[j][l]) for j in range(7))==(one if k==l else zero)
            assert sm(mul(U[k][j],U[l][j]) for j in range(7))==(one if k==l else zero)
            assert power(U[k][l],121)==U[(k+1)%7][l]
    pairs=[]
    for k in range(7):
        for l in range(7):
            c=sm(mul(U[k][j],power(U[l][j],121)) for j in range(7))
            assert c==(one if k==(l+1)%7 else zero)
            if c!=zero:pairs.append((k,l))
    pi=add(scale(one,4),add(scale(periods[0],-2),periods[4]))
    pis=[aut(pi,pow(2,l,29)) for l in range(7)]
    invpis=[power(x,11**7-2) for x in pis]
    for l in range(7):
        k=(l+1)%7
        assert mul(pis[l],invpis[l])==one
        assert power(pis[l],121)==pis[k]
        assert mul(power(invpis[k],3),power(power(invpis[l],3),121))==power(invpis[k],6)
    half=(6,0)
    ii=(0,4)  # in F_11[t]/(t^2-2), i=4t and i^2=-1.
    assert fqmul(ii,ii)==(10,0)
    C=[[fqone,ii],[fqone,fqneg(ii)]]
    Ci=fqinverse2(C)
    assert all(fqpow(x,121)==x for row in Ci for x in row)
    sign_pair=fqmm(transpose(Ci),Ci)
    assert sign_pair==[[fqzero,half],[half,fqzero]]
    quadratics=[]
    deltas=[]
    for aa,ss in [(1,(4,0)),(3,(0,1))]:
        dd=aa*aa+4
        assert fqmul(ss,ss)==(dd%11,0)
        up=fqmul(half,fqadd((aa,0),ss))
        um=fqmul(half,fqadd((aa,0),fqneg(ss)))
        dp=fqmul(fqinv(up),fqinv(ss))
        dm=fqmul(fqinv(um),fqinv(fqneg(ss)))
        V=[[fqone,up],[fqone,um]]
        Vi=fqinverse2(V)
        assert all(fqpow(x,121)==x for row in Vi for x in row)
        pairing=fqmm(transpose(Vi),Vi)
        assert pairing==[[dp,fqzero],[fqzero,dm]]
        assert fqmm(fqmm(transpose(V),[[dp,fqzero],[fqzero,dm]]),V)==[
            [fqone,fqzero],[fqzero,fqone]]
        deltas.append([dp,dm])
        quadratics.append(dict(a=aa,d=dd,V=V,inverse_pairing=pairing))
    combined_delta=[fqmul(x,y) for x in deltas[0] for y in deltas[1]]
    assert all(x!=fqzero for x in combined_delta)
    explicit_pairs={}
    for h in (1,4):
        support=[dict(tau3=[3,sign,(l+1)%7,rho],
                      tau2=[2,-sign,l,rho])
                 for sign in (1,-1) for l in range(7) for rho in range(h)]
        assert len(support)==14*h
        assert len({tuple(x['tau3']+x['tau2']) for x in support})==14*h
        explicit_pairs[str(h)]=support
    s,w=Fraction(1,10),Fraction(121,1220)
    assert 122*w-12==s and s-w==Fraction(1,1220)
    samples=[]
    for r in range(16):
        A,B=11**r,11**(r+2)
        coefficient=s-w*(A+B)
        predicted=Fraction(11**r-1,10)
        assert coefficient+vfac(A)+vfac(B)==predicted
        assert coefficient==Fraction(-(121*11**r-1),10)
        assert predicted.denominator==1
        samples.append(dict(r=r,A=A,B=B,coefficient_valuation=str(coefficient),
                            factorial_valuation=vfac(A)+vfac(B),
                            derivative_valuation=int(predicted)))
    baselines=[]
    for f,k,t in [(42,42,1759),(168,168,1633)]:
        par=parameter_check(k=k,f=f,m=2,t=t)
        part=par['nu0']
        D0=f*sum(part)
        c0=f*sum(vfac(n) for n in part)
        Kbound=k*f*sum(digits(n) for n in part)
        lower_offset=-Fraction(1,5)-Kbound
        upper_offset=c0-Fraction(1,10)-Fraction(D0,1220)
        assert lower_offset<=upper_offset
        r=0
        while 122*11**r<D0:r+=1
        baselines.append(dict(f=f,k=k,t=t,D0=D0,c0=c0,K0_upper=Kbound,
                              lower_offset_bound=str(lower_offset),
                              upper_offset_exact=str(upper_offset),
                              first_r_growing_degree_at_least_D0=r))
    result=dict(result='PASS',checked_at=datetime.now(timezone.utc).isoformat(),
        scope='Exact mod11 cyclotomic Frobenius and all49 trace-pair entries, plus/minus and weighted quadratic inverse pairings, standard-lattice unit factors, explicit enlarged-CM support pairs, Legendre and source-baseline arithmetic. No infinite-series, actual theta derivative or automorphic-image computation is claimed.',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256=hashlib.sha256(Path(__file__).with_name(
            'enlarged_host_ranks_characters_alpha_certificate.py').read_bytes()).hexdigest(),
        Frobenius11_coset=4,Frobenius121_coset=1,B_pair_support=pairs,
        sign_pairing=sign_pair,quadratic_pairings=quadratics,
        combined_delta_units=combined_delta,explicit_pairs=explicit_pairs,
        Legendre_samples=samples,actual_first_edge_baselines=baselines)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in [
        'result','checked_at','script_sha256','Frobenius11_coset',
        'Frobenius121_coset','B_pair_support','sign_pairing',
        'quadratic_pairings','combined_delta_units','actual_first_edge_baselines']},indent=2))


if __name__=='__main__':
    main()
