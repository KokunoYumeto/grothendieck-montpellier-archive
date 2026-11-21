"""Exact derivative exploration for the CM curve y²=4x³−4x at p=7.

No asserted general theorem is inferred from finite calculations.
The even normalized translate at the nonzero two-torsion point x=0
satisfies theta_T(z)^2 = sigma(z)^2 wp(z), theta_T(0)=1.
"""
from fractions import Fraction as F
from math import factorial


def vpint(n,p):
    if not n:return float('inf')
    out=0
    while n%p==0:n//=p;out+=1
    return out


def vp(x,p):return vpint(x.numerator,p)-vpint(x.denominator,p)


M=110
W=[F(1),F(1,5)]
for k in range(2,M+1):
    W.append(6*sum(W[i]*W[k-i] for i in range(1,k))/((4*k-2)*(4*k-3)-12))
L=[F(0)]+[-W[k]/((4*k-1)*(4*k)) for k in range(1,M+1)]
logW=[F(0)]
for n in range(1,M+1):
    logW.append(W[n]-sum((k*logW[k]*W[n-k] for k in range(1,n)),F(0))/n)
LT=[L[k]+logW[k]/2 for k in range(M+1)]


def expseries(a):
    b=[F(1)]
    for n in range(1,len(a)):
        b.append(sum(k*a[k]*b[n-k] for k in range(1,n+1))/n)
    return b


sigma=expseries(L)
theta=expseries(LT)
assert sigma[:3]==[F(1),F(-1,60),F(-1,10080)]
assert theta[:3]==[F(1),F(1,12),F(-1,10080)]
for label,coeffs,offset in [('sigma',sigma,1),('theta_T',theta,0)]:
    failures=[]
    records=[]
    for m,a in enumerate(coeffs):
        n=4*m+offset
        if n==0:continue
        val=vp(a*factorial(n),7)
        bound=max(0,(7*n)//48-1)
        gap=F(7*n,48)-val
        if val<bound:failures.append((n,val,bound))
        if n in [8,9,48,49,96,97,144,145,192,193,240,241,288,289,320,321]:
            records.append((n,val,bound,gap))
    print(label,'first strong-loss1 failures:',failures[:16])
    print(label,'selected n, valuation, strong-loss1 bound, nslope-minus-valuation:',records)
for r in range(3):
    n=8*7**r
    derivative=theta[n//4]*factorial(n)
    assert vp(derivative,7)==(7**r-1)//6
    print('C22 exact subsequence check: n=',n,'valuation=',vp(derivative,7))
print('D16 theta_T(0)=',theta[4]*factorial(16))
