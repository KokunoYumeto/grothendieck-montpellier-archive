"""Exact finite supplement for B59.

Checks conditional ramification arithmetic, three-slope tie order, arbitrary
2-plane additive root polynomials, and scalar/Frobenius incompatibility.
No formal group, ramified extension, or congruent pair is constructed.
"""
from pathlib import Path
from datetime import datetime, timezone
import itertools, math, time, json
started=time.perf_counter()
counts={'single_break_cases':0,'two_break_cases':0,'three_slope_cases':0,
        'additive_planes':0,'additive_polynomial_coefficient_checks':0,
        'additive_polynomial_root_checks':0,'nonzero_middle_coefficient_planes':0,
        'scalar_Frobenius_cases':0}
primes=[p for p in range(5,44) if all(p%d for d in range(2,math.isqrt(p)+1))]
p5_patterns=[]
for p in primes:
    q=p*p;N=q-1;A=q*(p-1);b0=N*(p-1);target=q*A
    for b in range(N//2,b0,N):
        if b%p==0:continue
        K=A+N*b;Jmin=A+(q-p)*b;c=target-K
        assert A<K<target and K%p and c>b0 and c>b
        assert Jmin%p==0 and Jmin%q!=0
        assert K+c==target
        assert Jmin+p*c-(K+c)==(p-1)*(c-b)>0
        assert A+q*c-(K+c)==N*(c-b)>0
        assert b*q+c-b==b0*q
        counts['single_break_cases']+=1
    for b1 in range(N//2,b0,N):
        if b1%p==0:continue
        J=A+(q-p)*b1
        # c>b2 is equivalent to p*b2<q*b0-(q-p)*b1.
        bound=(q*b0-(q-p)*b1-1)//p
        for b2 in range(b1+N,bound+1,N):
            if b2%p==0:continue
            K=J+(p-1)*b2;c=target-K
            assert b1<b2<c and c>b0
            assert J%p==0 and J%q!=0 and K%p and A<J<K<target
            assert A+q*b1==J+p*b1<K+b1 and A+q*b1<target
            assert J+p*b2==K+b2<A+q*b2 and J+p*b2<target
            assert K+c==target<J+p*c and target<A+q*c
            assert J+p*c-(K+c)==(p-1)*(c-b2)
            # Exact three-step Herbrand function, without floats.
            assert b1*q+(b2-b1)*p+c-b2==b0*q
            assert c%N==0
            counts['two_break_cases']+=1
            if p==5:p5_patterns.append([b1,b2,c,J,K])
    # Exhaustive small-break, small-intercept three-slope combinatorics.
    # These checks impose the needed tie/cap conditions, not geometric existence.
    for b1 in range(1,9):
        for b2 in range(b1+1,10):
            for c in range(b2+1,11):
                # One final term must hit target; enumerate the other intercept
                # near each possible tie as well as a strictly later value.
                Js={target-p*c,A+(q-p)*b1,A+(q-p)*b2,target-p*c+1}
                Ks={target-c,A+N*b1,A+N*b2,target-c+1}
                for J,K in itertools.product(Js,Ks):
                    if J<=A or K<=A or min(J+p*c,K+c)!=target:continue
                    if A+q*c<=target:continue
                    d1=[A+q*b1,J+p*b1,K+b1]
                    d2=[A+q*b2,J+p*b2,K+b2]
                    if min(d1)>=target or min(d2)>=target:continue
                    if d1.count(min(d1))<2 or d2.count(min(d2))<2:continue
                    assert d1[0]==d1[1]<d1[2]
                    assert d2[1]==d2[2]<d2[0]
                    assert J==A+(q-p)*b1 and K==J+(p-1)*b2
                    counts['three_slope_cases']+=1

# General 2-dimensional Fp subspaces in F_(p^3), whose root polynomial
# ordinarily has a NONZERO X^p coefficient. This deliberately avoids
# restricting the anti-Cartan leading space to a scalar copy of F_(p^2).
for p in [5,7,11]:
    cubic=next((c0,c1,c2) for c0 in range(1,p) for c1 in range(p) for c2 in range(p)
               if all((x**3+c2*x*x+c1*x+c0)%p for x in range(p)))
    c0,c1,c2=cubic;zero=(0,0,0);one=(1,0,0)
    els=list(itertools.product(range(p),repeat=3))
    def add(a,b):return tuple((a[i]+b[i])%p for i in range(3))
    def neg(a):return tuple(-v%p for v in a)
    def sub(a,b):return add(a,neg(b))
    def scalar(n,a):return tuple(n*v%p for v in a)
    def mul(a,b):
        v=[0]*5
        for i in range(3):
            for j in range(3):v[i+j]=(v[i+j]+a[i]*b[j])%p
        for j in [4,3]:
            t=v[j]
            for k,ck in enumerate(cubic):v[j-3+k]=(v[j-3+k]-t*ck)%p
        return tuple(v[:3])
    def power(a,n):
        out=one
        while n:
            if n&1:out=mul(out,a)
            a=mul(a,a);n//=2
        return out
    xp={x:power(x,p) for x in els};xq={x:xp[xp[x]] for x in els}
    normals=[v for v in els[1:] if next(x for x in v if x)==1]
    assert len(normals)==p*p+p+1
    for normal in normals:
        D=[x for x in els if sum(normal[i]*x[i] for i in range(3))%p==0]
        assert len(D)==p*p
        a=next(x for x in D if x!=zero)
        aline={scalar(n,a) for n in range(p)}
        b=next(x for x in D if x not in aline)
        ap=power(a,p-1);yb=sub(xp[b],mul(ap,b));yp=power(yb,p-1)
        assert yb!=zero and yp!=zero
        s=neg(add(power(ap,p),yp));t=mul(yp,ap)
        assert t!=zero
        if s!=zero:counts['nonzero_middle_coefficient_planes']+=1
        # Direct multiplication of every (X-d), independent of the displayed
        # additive-polynomial formula, on all F_(5^3) planes.
        if p==5:
            coeff=[one]
            for d in D:
                out=[zero]*(len(coeff)+1)
                for j,v in enumerate(coeff):
                    out[j]=sub(out[j],mul(d,v));out[j+1]=add(out[j+1],v)
                coeff=out
            expected=[zero]*(p*p+1);expected[1]=t;expected[p]=s;expected[p*p]=one
            assert coeff==expected
            counts['additive_polynomial_coefficient_checks']+=len(coeff)
        Dset=set(D)
        for x in els:
            value=add(xq[x],add(mul(s,xp[x]),mul(t,x)))
            assert (value==zero)==(x in Dset)
            counts['additive_polynomial_root_checks']+=1
        counts['additive_planes']+=1

# A full quadratic leading Cartan space cannot identify Frobenius with
# one scalar. Test all scalar candidates for several quadratic fields.
for p in [5,7,11,13]:
    ns=next(n for n in range(2,p) if pow(n,(p-1)//2,p)==p-1)
    for a,b in itertools.product(range(p),repeat=2):
        # At 1 the candidate must be1; at sqrt(ns), Frobenius is its negative.
        agree_one=(a,b)==(1,0)
        agree_root=(b*ns%p,a)==(0,p-1)
        assert not(agree_one and agree_root)
        counts['scalar_Frobenius_cases']+=1
assert counts['nonzero_middle_coefficient_planes']>0
result={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,**counts,
        'p5_conditional_two_break_patterns':p5_patterns,
        'scope':'Finite conditional arithmetic, exact additive-polynomial identities and finite leading spaces only. No BT group, ramified extension, or congruent pair constructed.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='p5_conditional_two_break_patterns'},indent=2))
