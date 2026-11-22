"""Exact B58 arithmetic and finite linear-algebra supplement.

No formal group, division extension, or congruent pair is constructed.
"""
from pathlib import Path
from datetime import datetime, timezone
import time, math, itertools, json
started=time.perf_counter()
primes=[n for n in range(5,102) if all(n%d for d in range(2,math.isqrt(n)+1))]
valuation_cases=0;low_break_cases=0;type_cases=0;order_two_pairs={}
for p in primes:
    q=p*p;N=q-1;A=q*(p-1);b0=N*(p-1)
    # Exact ramification/point-field indices and the cyclotomic point.
    assert A//q==p-1 and q*A//q==q*(p-1)
    assert (q*(p-1))-(p-1)==b0 and p*N-N==b0
    assert N*q*A>q*A and pow(p,4,N)==1
    valuation_cases+=1
    for b in range(1,b0):
        if b%p==0:continue
        K=A+N*b;c=q*b0-N*b
        assert K%p and A<K<q*A and K+c==q*A
        assert c>b0 and c>b and c%N==0
        # First possible degree with exact p-valuation one above the strict bound.
        J=((A+(q-p)*b)//p+1)*p
        if J%q==0:J+=p
        assert J%p==0 and J%q!=0 and J>A+(q-p)*b
        if J<q*A:assert J+p*c>K+c
        assert A+q*c-(K+c)==N*(c-b)>0
        assert J+p*c-(K+c)>(p-1)*(c-b)>0
        # Actual two-break Herbrand function: W has orderq² and finalZ orderq.
        assert (b*q+c-b)==b0*q
        low_break_cases+=1
    pairs=set()
    for c1 in range(1,N,p-1):
        r=c1+p-1;h=(p+1)//math.gcd(p+1,r)
        if h==1:continue
        c2=(p*c1+(p-1)**2)%N
        o1=tuple(sorted({c1,p*c1%N}));o2=tuple(sorted({c2,p*c2%N}))
        if o1==o2:continue
        type_cases+=1
        if h==2:
            assert p%4==1 and (c2-c1)%N==N//2
            pairs.add(tuple(sorted((o1,o2))))
    assert len(pairs)==(1 if p%4==1 else 0)
    order_two_pairs[str(p)]=sorted(pairs)
assert order_two_pairs['5']==[((1,5),(13,17))]

polynomial_cases=0;scalar_cases=0;evaluation_cases=0;centralizer_cases=0
for p in [5,7,11,13]:
    ns=next(a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1)
    els=list(itertools.product(range(p),repeat=2))
    def add(x,y):return((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(x,y):return((x[0]*y[0]+ns*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def frob(x):return(x[0],-x[1]%p)
    basis=[(1,0),(0,1)]
    for a,b in itertools.product(els,repeat=2):
        vals=[add(mul(a,frob(x)),mul(b,x)) for x in basis]
        assert (vals==[(0,0),(0,0)])==(a==(0,0) and b==(0,0))
        # X^q+aX^p+bX vanishes on Fq iff a=0,b=-1.
        vals_q=[add(x,v) for x,v in zip(basis,vals)]
        assert (vals_q==[(0,0),(0,0)])==(a==(0,0) and b==((-1)%p,0))
        polynomial_cases+=2
    for a in els:
        assert any(mul(a,x)!=frob(x) for x in basis)
        scalar_cases+=1
    if p>7:continue
    matrices=list(itertools.product(range(p),repeat=4))
    def apply(B,v):return((B[0]*v[0]+B[1]*v[1])%p,(B[2]*v[0]+B[3]*v[1])%p)
    for v in els[1:]:
        kernels=sum(apply(B,v)==(0,0) for B in matrices)
        assert kernels==p*p
        assert len({mul(a,v) for a in els})==p*p
        evaluation_cases+=len(matrices)
    for B in matrices:
        # Centralizer of multiplication by sqrt(ns) is the nonsplit Cartan.
        lhs=((B[1])%p,(B[0]*ns)%p,B[3]%p,(B[2]*ns)%p)
        rhs=((ns*B[2])%p,(ns*B[3])%p,B[0]%p,B[1]%p)
        assert (lhs==rhs)==(B[0]==B[3] and B[1]==ns*B[2]%p)
        centralizer_cases+=1
result={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-started,'valuation_cases':valuation_cases,
 'low_break_inequality_cases':low_break_cases,'different_type_cases':type_cases,
 'additive_polynomial_cases':polynomial_cases,'scalar_Frobenius_cases':scalar_cases,
 'primitive_point_stabilizer_cases':evaluation_cases,'centralizer_cases':centralizer_cases,
 'projective_order_two_pairs':order_two_pairs,
 'scope':'Exact arithmetic, additive-polynomial coefficients and finite matrix spaces only; no formal group or division field instantiated.'}
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_b58_exact_arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='projective_order_two_pairs'},indent=2))
