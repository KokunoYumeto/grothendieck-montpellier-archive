"""Exact finite Newton/arc arithmetic for B63; no field is instantiated."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import time, json

started=time.perf_counter()
primes=(5,7,11,13,17,19)
newton_cases=chain_cases=arc_cases=weight_cases=index_cases=0
examples=[]

def inverses(p,b,Z):
    q=p*p
    if b>=Z*F(p-1,p):return {Z/q}
    return {(Z-b)/p,F(b,p*(p-1))}

for p in primes:
    q=p*p; N=q-1
    for a in range(1,401):
        if a%p==0:continue
        for b in range(1,a+2):
            newton_cases+=1
            if b>=F(a*p,p+1): values={F(a,N)}
            else: values={F(a-b,p-1),F(b,p*(p-1))}
            values={z for z in values if z.denominator==1 and z>0}
            for n in range(2,5):
                new=set()
                for z in values:
                    assert 0<z<a
                    for w in inverses(p,b,z):
                        assert 0<w<z
                        if w.denominator==1:new.add(w)
                values=new; chain_cases+=1
                if values:assert a>N*p**(2*n-3)
    for n in range(2,7):
        Q=q**(n-1); threshold=p**(2*n-3)
        # Near the threshold, across the former upper bound, and at large
        # indices where the excluded A multiple genuinely arises.
        candidates=set()
        for center in (threshold,Q,3*Q,N*Q,(N+1)*Q,10*N*Q):
            for j in range(-20,21):
                e=((center+j)//(p-1))*(p-1)
                if e>threshold:candidates.add(e)
        for e in sorted(candidates):
            A=e//Q+1
            adjusted=A%N==0
            if adjusted:A+=1
            assert F(e,Q)<A<F(e,p**(2*n-3)) and A%N
            d=N*e; b=d-(p-1)*A*Q
            assert b>(q-p)*A*q**(n-2)>0
            assert A*Q<d<N*A*Q
            assert b%N==(-(p-1)*A)%N
            assert F(d-b,p-1)==A*Q
            assert b<F(d*p,p+1)
            z=F(A*Q)
            for j in range(n-1,0,-1):
                assert inverses(p,b,z)=={F(A*q**(j-1))}
                z/=q
                weight_cases+=1
            assert z==A
            for j in range(n-1):
                w=A*q**j
                assert b+p*w>q*w
                assert d>q*w
                weight_cases+=1
            assert b+(p-1)*A*Q==d<N*A*Q
            arc_cases+=1
            if adjusted and len(examples)<12:
                examples.append(dict(p=p,n=n,e=e,A=A,d=d,b=b,adjusted=True))
    for e in range(p-1,20001,p-1):
        L=0; power=p
        while power<=e-1:L+=1;power*=p
        bound=(L+3)//2
        n=1
        while p**(2*(n+1)-3)<e:n+=1
        assert bound==n
        index_cases+=1

out=dict(status='PASS',actual_utc=datetime.now(timezone.utc).isoformat(),
         runtime_seconds=time.perf_counter()-started,
         counts=dict(newton_cases=newton_cases,chain_cases=chain_cases,
                     arc_cases=arc_cases,weight_cases=weight_cases,
                     index_cases=index_cases),
         adjusted_arc_examples=examples,
         scope='Six primes; a<=400 exact rational Newton chains at levels2--4; selected arc indices through level6; all permitted e<=20000 for integer formula. No existence theorem or infinite-field construction inferred from finite tests.')
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
