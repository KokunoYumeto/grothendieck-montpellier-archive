#!/usr/bin/env python3
"""Exact finite quotient checks for B.037; no external libraries or randomness."""
from itertools import product

# D=F2[x,y]/(x,y)^2, basis (1,x,y).
def dbasis(i,j):
    if i==0:return j
    if j==0:return i
    return None

def dmul(a,b):
    c=0
    for i in range(3):
        if a>>i&1:
            for j in range(3):
                if b>>j&1:
                    k=dbasis(i,j)
                    if k is not None:c^=1<<k
    return c

# D tensor D, ordered basis i tensor j with index 3*i+j.
table=[[0]*9 for _ in range(9)]
for i,j,k,l in product(range(3),repeat=4):
    a,c=dbasis(i,k),dbasis(j,l)
    if a is not None and c is not None:table[3*i+j][3*k+l]=1<<(3*a+c)

def tmul(a,b):
    ans=0
    while a:
        abit=a&-a;i=abit.bit_length()-1;a^=abit
        bb=b
        while bb:
            bbit=bb&-bb;j=bbit.bit_length()-1;bb^=bbit
            ans^=table[i][j]
    return ans

def diagonal(a):
    ans=0
    for i,j in product(range(3),repeat=2):
        if a>>(3*i+j)&1:
            k=dbasis(i,j)
            if k is not None:ans^=1<<k
    return ans

image={diagonal(a) for a in range(512)}
kernel=[a for a in range(512) if diagonal(a)==0]
assert len(image)==8 and len(kernel)==64
witness=(1<<3)^(1<<1)
assert witness!=0 and diagonal(witness)==0
for a,b in product(range(512),repeat=2):
    assert diagonal(a^b)==diagonal(a)^diagonal(b)
    assert diagonal(tmul(a,b))==dmul(diagonal(a),diagonal(b))
print('D tensor D: all512 elements and262144 pairs checked; dimension9; image8; kernel64; x tensor1 - 1 tensorx is nonzero and maps to zero: PASS')

# T/(x,y)^4 and R=F2+(x,y)^2T within this finite quotient.
mons=[(i,n-i) for n in range(4) for i in range(n+1)]
idx={m:i for i,m in enumerate(mons)}
mt=[[0]*10 for _ in range(10)]
for i,(a,b) in enumerate(mons):
    for j,(c,d) in enumerate(mons):
        if a+b+c+d<4:mt[i][j]=1<<idx[a+c,b+d]

def mul4(a,b):
    ans=0
    while a:
        abit=a&-a;i=abit.bit_length()-1;a^=abit
        bb=b
        while bb:
            bbit=bb&-bb;j=bbit.bit_length()-1;bb^=bbit
            ans^=mt[i][j]
    return ans

linear=(1<<idx[1,0])|(1<<idx[0,1])
R=[a for a in range(1024) if a&linear==0]
assert len(R)==256
count=0
for r in R:
    q=mul4(r,r)^r
    assert q&7==0
    for coeff in range(1024):
        val=mul4(coeff,q)
        assert val&linear==0 and val&1==0
        count+=1
print(f'Finite truncation T/(x,y)^4: all{len(R)} R-inputs and{count} coefficient/input pairs verify q(R)T subset (x,y)^2T: PASS')
print('ALL B.037 HIGHER-DIMENSIONAL EXACT CHECKS PASSED.')
