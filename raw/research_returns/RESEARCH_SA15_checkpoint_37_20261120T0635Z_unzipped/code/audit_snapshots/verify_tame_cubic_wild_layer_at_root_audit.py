"""B56 exact finite supplement; no formal group or congruent pair is built."""
from pathlib import Path
import datetime, json, math, time
start=time.perf_counter()
primes=[p for p in range(5,102) if all(p%d for d in range(2,math.isqrt(p)+1))]
monomial_checks=0
break_checks=0
weight_checks=0
conjugacy_checks=0
cardinality_fields=0
cardinality_nonzero_values=0
p5=[]
for p in [5,7]:
    q,N=p*p,p*p-1
    A=p*(p-1);b0=N*(p-1)
    exponents=[]
    for j in range(A,q*A+1):
        s=1
        while j%(s*p)==0:s*=p
        assert math.comb(j,s)%p==(j//s)%p
        assert all(math.comb(j,r)%p==0 for r in range(1,s))
        exponents.append((j,s));monomial_checks+=1
    divisible=[(j,s) for j,s in exponents if s>1]
    for b in range(1,(q-1)*A):
        assert min(j+s*b for j,s in divisible)==A+p*b
        if b<b0:
            target=A+p*b;j0=target-b
            assert A<j0<q*A
            matches=[j for j,s in exponents if s==1 and j+b==target]
            assert matches==([j0] if j0%p else [])
        elif b>b0:
            assert A+p*b>q*A
            j0=q*A-b
            assert A<j0<q*A
            matches=[j for j,s in exponents if s==1 and j+b==q*A]
            assert matches==([j0] if j0%p else [])
        break_checks+=1
for p in primes:
    q,N=p*p,p*p-1
    assert p**3%N==p
    assert (p*p*(p-1))%N==p-1
    for c1 in range(1,N,p-1):
        c2=(p*c1+(p-1)**2)%N
        r=(c1+p-1)%N
        if r%(p+1)==0:continue
        assert (c2+p-1)%N==p*r%N
        h=N//math.gcd(N,(p-1)*r)
        for b in {p*(p-1)*r%N,(-p*(p-1)*r)%N}:
            assert (p*b)%N in {(p-1)*r%N,(-(p-1)*r)%N}
            if h>2:
                assert b%(p+1)!=0
            else:
                assert h==2 and b%(p+1)==0
            weight_checks+=1
        if p==5:
            names={frozenset([1,5]):'A',frozenset([9,21]):'B',frozenset([13,17]):'C'}
            t1=names[frozenset([c1,p*c1%N])];t2=names[frozenset([c2,p*c2%N])]
            assert (h==2)==({t1,t2}=={'A','C'})
            p5.append({'tangent_exponents':[c1,c2],'types':[t1,t2],'projective_order':h,'necessary_wild_orders':[625] if h>2 else [125,625]})
# Independent explicit Fp² composition check of c sigma conjugation on beta sigma.
for p in [5,7,11,13]:
    ns=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    def mul(x,y):return ((x[0]*y[0]+ns*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def power(x,n):
        y=(1,0)
        while n:
            if n&1:y=mul(y,x)
            x=mul(x,x);n//=2
        return y
    def sig(x):return (x[0],-x[1]%p)
    els=[(a,b) for a in range(p) for b in range(p)]
    for c in els[1:]:
        inv=power(c,p*p-2)
        factor=mul(c,sig(inv))
        for beta in els:
            target=mul(factor,sig(beta))
            for z in [(1,0),(0,1)]:
                # A=c sigma, A^-1=sigma(c^-1) sigma.
                x=mul(sig(inv),sig(z))
                x=mul(beta,sig(x))
                x=mul(c,sig(x))
                assert x==mul(target,sig(z))
            conjugacy_checks+=1
    values={power(z,p-1) for z in els if z!=(0,0)}
    assert len(values)==p+1>1
    cardinality_fields+=1;cardinality_nonzero_values+=p*p-1
    for scalar in els:
        z=(1,0) if scalar!=(1,0) else (0,1)
        assert mul(scalar,z)!=sig(z)
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Finite binomial, lower-break arithmetic, tame weights and explicit anti-Cartan conjugacy only; no formal group or pair existence inferred.',
        'monomial_first_terms':monomial_checks,'lower_break_cases':break_checks,'tame_weight_cases':weight_checks,
        'anti_Cartan_conjugacy_cases':conjugacy_checks,'low_break_cardinality_fields':cardinality_fields,'low_break_nonzero_values':cardinality_nonzero_values,'p5_oriented_cases':p5,
        'runtime_seconds':time.perf_counter()-start}
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_b56_exact_arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
