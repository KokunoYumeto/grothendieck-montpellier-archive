"""Independent exact certificate for the two C20 reductions.

This uses enumeration of the entire squaring map over F_37 and F_37^2,
not the norm/Legendre point-count implementation in the root script.
Polynomial arithmetic and irreducibility tests use only the standard library.
"""
from collections import Counter
from math import gcd, isqrt


def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a


def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)


def neg(a):return [-x for x in a]
def scale(a,k):return trim([k*x for x in a])


def mul(a,b):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)


def ppow(a,n):
    b=[1]
    while n:
        if n&1:b=mul(a,b)
        a=mul(a,a);n//=2
    return b


def modpoly(a,f,p):
    a=trim([x%p for x in a])
    inv=pow(f[-1],-1,p)
    while len(a)>=len(f):
        d=len(a)-len(f);v=a[-1]*inv%p
        for i,c in enumerate(f):a[i+d]=(a[i+d]-v*c)%p
        a=trim(a)
    return a


def gpoly(a,b,p):
    while b:a,b=b,modpoly(a,b,p)
    return [x*pow(a[-1],-1,p)%p for x in a] if a else []


def powmod(a,n,f,p):
    b=[1]
    while n:
        if n&1:b=modpoly(mul(a,b),f,p)
        a=modpoly(mul(a,a),f,p);n//=2
    return b


def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def determinant_bareiss(rows):
    a=[row[:] for row in rows];n=len(a);sign=1;previous=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next(j for j in range(k+1,n) if a[j][k])
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%previous==0
                a[i][j]=numerator//previous
        for i in range(k+1,n):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]


def quartic_discriminant(f):
    assert len(f)==5 and f[-1]==1
    g=[i*f[i] for i in range(1,5)]
    F=list(reversed(f));G=list(reversed(g))
    sylvester=[]
    for j in range(3):sylvester.append([0]*j+F+[0]*(2-j))
    for j in range(4):sylvester.append([0]*j+G+[0]*(3-j))
    return determinant_bareiss(sylvester)


def irreducibility_certificate(f,p):
    n=len(f)-1
    if f[-1]%p==0:return None
    prime_divisors=[r for r in range(2,n+1) if n%r==0 and isprime(r)]
    x=[0,1];h=x;remainders={};gcds={}
    for k in range(1,n+1):
        h=powmod(h,p,f,p)
        if k in [n//r for r in prime_divisors]:
            rem=modpoly(add(h,neg(x)),f,p)
            g=gpoly(f,rem,p)
            remainders[k]=h;gcds[k]=g
            if len(g)!=1:return None
    if h!=x:return None
    return {'prime':p,'degree':n,'final_remainder':h,
            'intermediate_remainders':remainders,'gcds':gcds}


# Rebuild the odd division polynomial from the integral elliptic recurrences.
A=-30;B=-25
c=[B,A,0,1]
psi3=[-A*A,12*B,6*A,0,3]
f4=[-8*B*B-A**3,-4*A*B,-5*A*A,20*B,5*A,0,1]
psi5=add(scale(mul(ppow(c,2),f4),32),neg(ppow(psi3,3)))
psi7=add(mul(psi5,ppow(psi3,3)),neg(scale(mul(ppow(c,2),ppow(f4,3)),128)))
content=0
for x in psi7:content=gcd(content,x)
assert len(psi7)==25 and psi7[-1]==7 and content==1
print('psi7 ascending coefficients:',psi7)
cert=None
for p in range(11,1000):
    if isprime(p):
        cert=irreducibility_certificate(psi7,p)
        if cert:break
assert cert is not None
print('psi7 modular irreducibility certificate:',cert)


p=37
assert pow(2,(p-1)//2,p)==p-1


def ffadd(x,y):return ((x%p+y%p)%p)+p*((x//p+y//p)%p)


def ffmul(x,y):
    a,b=x%p,x//p;c,d=y%p,y//p
    return (a*c+2*b*d)%p+p*((a*d+b*c)%p)


def ffeval(coeffs,x):
    ans=0
    for c in reversed(coeffs):ans=ffadd(ffmul(ans,x),c%p)
    return ans


square_counts=Counter(ffmul(y,y) for y in range(p*p))
base_square_counts=Counter(y*y%p for y in range(p))
assert sum(square_counts.values())==p*p and len(square_counts)==(p*p+1)//2
phi=[-300,-100,-60,0,1]
roots=[a for a in range(p) if sum(c*pow(a,i,p) for i,c in enumerate(psi7))%p==0]
assert roots==[7,20,35]
psi7der=[i*psi7[i] for i in range(1,len(psi7))]
assert all(sum(c*pow(a,i,p) for i,c in enumerate(psi7der))%p for a in roots)
print('Simple psi7 roots mod37:',roots)


for a,expected in [(7,(35,1297)),(20,(37,1361))]:
    f=mul([-a,1],phi)
    n1=1+sum(base_square_counts[sum(c*pow(x,i,p) for i,c in enumerate(f))%p] for x in range(p))
    n2=1+sum(square_counts[ffeval(f,x)] for x in range(p*p))
    assert (n1,n2)==expected
    deriv=[i*f[i] for i in range(1,len(f))]
    assert len(gpoly(f,deriv,p))==1
    trace=p+1-n1
    middle=(n2-p*p-1+trace*trace)//2
    frob=[p*p,-p*trace,middle,-trace,1]
    delta=trace*trace-4*(middle-2*p)
    print('a=',a,'counts=',(n1,n2),'Frob ascending=',frob,'real discriminant=',delta)
    disc=quartic_discriminant(frob)
    assert disc==({7:110882494512,20:637336153872}[a])
    assert isqrt(disc)**2!=disc
    print('Quartic discriminant by integer Sylvester determinant:',disc,'nonsquare')
    c=None
    for ell in range(2,100):
        if isprime(ell):
            c=irreducibility_certificate(frob,ell)
            if c:break
    assert c is not None
    print('Frob irreducibility certificate:',c)
    assert middle%p
    assert not any([trace==0,trace*trace==p+middle,
                    trace*trace==2*middle,trace*trace==3*middle-3*p])
print('All two-reduction point counts, smoothness, ordinarity, and exception checks passed.')
