#!/usr/bin/env python3
"""Exact finite checks for B.024--026, including mixed-characteristic indicators."""
from itertools import product


def digit_values(x,p,N,precision):
    values=[x]
    current=x
    for j in range(1,N):
        exp=precision+N-j
        modulus=p**(exp+1)
        current=((pow(current,p,modulus)-current)%modulus)//p
        values.append(current)
    return values


cases=0
for p in [2,3]:
    for N in [1,2,3]:
        for m in [1,2,3]:
            modulus=p**m
            for representative in range(p**N):
                target=[d%p for d in digit_values(representative,p,N,m)]
                for x in range(p**(N+m)):
                    digits=digit_values(x,p,N,m)
                    H=1
                    for d,c in zip(digits,target):
                        H=H*(1-pow((d-c)%modulus,p-1,modulus))%modulus
                    indicator=pow(H,p**m,modulus)
                    expected=int(x%(p**N)==representative)
                    assert indicator==expected,(p,N,m,representative,x,indicator)
                    cases+=1
    print(f'Mixed-characteristic indicator p={p}, N=1..3, m=1..3: '
          'all classes and all inputs modulo p^(N+m): PASS')
print(f'Indicator total: {cases} exact modular evaluations.')


# Split refinement R0^2 -> R0^5 over the nonfield ring Z/4Z.
parents=[0,0,1,1,1]
selected=[0,2]
for values in product(range(4),repeat=5):
    old=[values[i] for i in selected]
    kernel=[(values[i]-old[parents[i]])%4 for i in range(5)]
    assert all(kernel[i]==0 for i in selected)
    reconstructed=tuple((old[parents[i]]+kernel[i])%4 for i in range(5))
    assert reconstructed==values
print('Partition refinement over Z/4Z: all1024 vectors split as rank2 + rank3: PASS')


# B.025, a two-branch order with conductor exponent2, requiring r=3.
# T=F2[t] localized away from t(t+1), R=F2[m]+m^2 T, m=t(t+1).
def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c


def psquare(a):
    c=0;i=0
    while a:
        if a&1:c|=1<<(2*i)
        a>>=1;i+=1
    return c


def ppow(a,n):
    r=1
    while n:
        if n&1:r=pmul(r,a)
        a=psquare(a);n>>=1
    return r


def valuation_zero(a):
    assert a
    return (a&-a).bit_length()-1


def divide_linear_at_one(a):
    # Exact synthetic division by t+1 over F2, returning quotient and remainder.
    degree=a.bit_length()-1
    if degree<1:return 0,a
    q=0;carry=(a>>degree)&1
    q|=carry<<(degree-1)
    for i in range(degree-1,0,-1):
        carry=((a>>i)&1)^carry
        q|=carry<<(i-1)
    remainder=(a&1)^carry
    return q,remainder


def valuation_one(a):
    assert a
    result=0
    while True:
        q,r=divide_linear_at_one(a)
        if r:return result
        a=q;result+=1


def delta(a):
    num=psquare(a)^a
    assert not num&1
    return num>>1


m=0b110 # t(t+1)
a=psquare(m)
r=3
assert valuation_zero(a)==valuation_one(a)==2
for n in range(1,7):
    u=pmul(a,ppow(0b11,8*n))
    assert (u^a)&((1<<7)-1)==0
    assert valuation_one(u)==2+8*n
    x=ppow(u,r)
    digits=[]
    for j in range(7):
        digits.append(x)
        if j<6:x=delta(x)
    # The target a^3 has digit residues 0,0,0,0,0,0,1.
    assert [d&1 for d in digits]==[0,0,0,0,0,0,1]
    H=1
    for d in digits[:6]:H=pmul(H,d^1)
    H=pmul(H,digits[6])
    g=pmul(a,H)
    assert valuation_zero(g)==2<r
print('Two-branch conductor2 example: all n=1..6 give v0(g(u_n^3))=2<3: PASS')


# B.026 finite quotient: F2[tau,sigma]/(tau^2,sigma^2), basis1,tau,sigma,tau*sigma.
def tensor_mul(a,b):
    c=0
    exponents=[(0,0),(1,0),(0,1),(1,1)]
    for i,(ix,iy) in enumerate(exponents):
        if not(a>>i)&1:continue
        for j,(jx,jy) in enumerate(exponents):
            if (b>>j)&1 and ix+jx<2 and iy+jy<2:
                k=exponents.index((ix+jx,iy+jy))
                c^=1<<k
    return c


def diagonal(a):
    return (a&1)|((((a>>1)^(a>>2))&1)<<1)


def dual_mul(a,b):
    return ((a&1)*(b&1)) | (((((a>>1)&1)*(b&1)+(a&1)*((b>>1)&1))&1)<<1)


for a,b in product(range(16),repeat=2):
    assert diagonal(tensor_mul(a,b))==dual_mul(diagonal(a),diagonal(b))
    assert diagonal(a^b)==diagonal(a)^diagonal(b)
witness=0b0110
assert witness and diagonal(witness)==0
kernel=[a for a in range(16) if diagonal(a)==0]
assert len(kernel)==4
print('Intermediate-coefficient tensor quotient: all16 elements and256 pairs; '
      'kernel size4, tau-sigma witness nonzero: PASS')
print('ALL B.024--026 EXACT CHECKS PASSED.')
