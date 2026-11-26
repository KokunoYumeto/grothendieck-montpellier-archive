"""Original exact-rational nonvanishing certificate for Jac(v^2+v=u^5).
No floating point arithmetic is used anywhere in the certificate.
The mathematical inputs are stated in the companion proof note.
"""
from fractions import Fraction as F
from math import isqrt, factorial

SCALE = 10**6

def sqrt_bounds(q):
    assert q >= 0
    a = isqrt(q.numerator*SCALE*SCALE//q.denominator)
    lo,hi=F(a,SCALE),F(a+1,SCALE)
    assert lo*lo <= q < hi*hi
    return lo,hi

def atan_bounds(q, m=50):
    assert 0 < q < 1
    s=sum(((-1)**j)*q**(2*j+1)/F(2*j+1) for j in range(m))
    nxt=((-1)**m)*q**(2*m+1)/F(2*m+1)
    return min(s,s+nxt),max(s,s+nxt)

a,b=atan_bounds(F(1,5)); c,d=atan_bounds(F(1,239))
pilo,pihi=16*a-4*d,16*b-4*c # Machin's formula
assert pilo>F(314159,100000) and pihi<F(314160,100000)
pilo,pihi=F(314159,100000),F(314160,100000)
root_floor=isqrt(isqrt(3125*SCALE**4))
rootlo,roothi=F(root_floor,SCALE),F(root_floor+1,SCALE)
assert rootlo**4<=3125<roothi**4
klo,khi=4*pilo/roothi,4*pihi/rootlo
assert klo>F(16807,10000) and khi<F(16808,10000)
klo,khi=F(16807,10000),F(16808,10000)
assert klo>F(5,3)
assert pihi*khi/2<4

def expminus_upper(q,m=100):
    assert q>=0
    s=t=F(1)
    for j in range(1,m+1):
        t*=q/F(j); s+=t
    return 1/s

def expminus_lower(q,m=80):
    assert q>=0 and q<m+2
    s=t=F(1)
    for j in range(1,m+1):
        t*=q/F(j); s+=t
    nxt=t*q/F(m+1)
    # For j>=m+1 all consecutive ratios are at most q/(m+2).
    tail=nxt/(1-q/F(m+2))
    return 1/(s+tail)

def d4(n):
    ans,p=1,2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e+=1
        ans*=((e+1)*(e+2)*(e+3))//6
        p+=1
    if n>1:ans*=4
    return ans

leadrootlo,_=sqrt_bounds(pilo*klo/2)
lead_lower=2*leadrootlo*expminus_lower(khi)*(1+F(3,8)/khi-F(15,128)/(klo*klo))
assert lead_lower>F(7,10)
finite_upper=F(0)
for n in range(11,401):
    snlo,snhi=sqrt_bounds(F(n))
    zlo,zhi=klo*snlo,khi*snhi
    zlo=F(zlo.numerator*10000//zlo.denominator,10000)
    zhi=F(zhi.numerator*10000//zhi.denominator+1,10000)
    _,prefhi=sqrt_bounds(pihi*zhi/2)
    finite_upper+=2*F(d4(n))/snlo*prefhi*expminus_upper(zlo)*(1+F(3,8)/zlo)
# Integral bound for n>400: term <= 8 n^2 exp(-5 sqrt(n)/3).
# Integral from 400 to infinity equals this explicit rational times exp(-100/3).
poly=sum(F(factorial(5),factorial(5-j))*20**(5-j)*F(3,5)**(j+1) for j in range(6))
tail_upper=16*poly*expminus_upper(F(100,3))
assert finite_upper+tail_upper<F(13,20)
assert lead_lower-finite_upper-tail_upper>F(1,20)

def rational_decimal(q,digits=12):
    s=10**digits
    a=q.numerator*s//q.denominator
    return f'{a//s}.{a%s:0{digits}d}'
print('Exact-rational assertions passed.')
print('Leading-term lower bound > 7/10; computed lower bound begins',rational_decimal(lead_lower))
print('Absolute tail upper bound < 13/20; computed upper bound begins',rational_decimal(finite_upper+tail_upper))
print('L(A,1) > 1/20.')
