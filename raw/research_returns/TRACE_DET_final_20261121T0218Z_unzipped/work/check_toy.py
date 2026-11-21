"""Exact finite checks supporting, but not proving, TRACE_DET's toy findings."""
from itertools import product
from fractions import Fraction
import json

def weighted_count(q,t,k):
    total=0
    for xs in product(range(q),repeat=k):
        if sum(xs[j]*xs[j+1] for j in range(k-1))%q==0:
            w=1
            for x in xs:w*=t[x]
            total+=w
    return total

records=[]
cases=0
for q in (2,3):
    for t in product((0,1,2),repeat=q):
        for k in range(2,6):
            n=weighted_count(q,t,k)
            r=q*n-sum(t)**k
            rhs2=(q-1)**2*q**(k-1)*sum(x*x for x in t)**2*max(t)**(2*k-4)
            assert r*r<=rhs2,(q,t,k,r,rhs2)
            cases+=1
records.append({'check':'prime-modulus inequality by exact squared arithmetic','cases':cases,'outcome':'all passed'})
q=4;t=(1,)*q;k=3
n=weighted_count(q,t,k);r=q*n-sum(t)**k
records.append({'check':'composite counterexample','q':q,'t':t,'k':k,'N':n,'R':r,'claimed_bound':(q-1)*q*sum(x*x for x in t)})
assert (n,r)==(32,64)
q=2;t=(2,1);k=1
n=weighted_count(q,t,k);r=q*n-sum(t)
records.append({'check':'k=1 counterexample','q':q,'t':t,'N':n,'R':r,'claimed_bound':str(Fraction(sum(x*x for x in t),max(t)))})
assert r>Fraction(sum(x*x for x in t),max(t))
print(json.dumps(records,indent=2))
