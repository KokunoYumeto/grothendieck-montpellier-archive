#!/usr/bin/env python3
"""Exact checks for B.021--023. All arithmetic is finite-field/polynomial arithmetic."""
from itertools import product


def node_valuation_difference(i, j, q, Q, m):
    assert i != j
    if i % q != j % q:
        return 0
    i //= q
    j //= q
    v = m
    while i % Q == j % Q:
        i //= Q
        j //= Q
        v += 1
    return v


def w(n,q,Q,m):
    total=m*(n//q)
    divisor=q*Q
    while divisor<=n:
        total+=n//divisor
        divisor*=Q
    return total


count=0
lower_count=0
for q,Q in [(2,2),(3,3),(4,4),(2,4),(2,8),(3,9),(4,16)]:
    for m in range(1,5):
        for n in range(1,101):
            actual=sum(node_valuation_difference(n,i,q,Q,m) for i in range(n))
            assert actual==w(n,q,Q,m),(q,Q,m,n,actual,w(n,q,Q,m))
            count+=1
        for n in range(1,21):
            for j in range(q*Q*Q):
                if j<n: # The product is exactly zero at an earlier interpolation node.
                    continue
                actual=sum(node_valuation_difference(j,i,q,Q,m) for i in range(n))
                assert actual>=w(n,q,Q,m),(q,Q,m,n,j)
                lower_count+=1
    print(f'Newton nodes q={q}, Q={Q}, m=1..4: exact denominator n<=100 and '
          'all three-digit nodes for n<=20: PASS')
print(f'Newton totals: {count} denominator identities, {lower_count} lower-bound cases.')


# Polynomials over F2 are bit masks. No truncation is used until explicit reduction.
def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        a<<=1;b>>=1
    return c


def madd(a,b):
    return [[x^y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def mmul(a,b):
    rows,inner,cols=len(a),len(b),len(b[0])
    c=[[0]*cols for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            for j in range(cols):c[i][j]^=pmul(a[i][k],b[k][j])
    return c


def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def reduce_mat(a,mask):
    return [[x&mask for x in row] for row in a]


def scalar_inverse(a,modulus):
    mask=modulus-1
    return next(b for b in range(modulus) if pmul(a,b)&mask==1)


def blocks(a,b,c,d):
    return [ar+br for ar,br in zip(a,b)]+[cr+dr for cr,dr in zip(c,d)]


I2=identity(2);O2=[[0,0],[0,0]];I4=identity(4)
J=blocks(O2,I2,I2,O2) # -1=1 in characteristic two.
patch_count=0
for m in [1,2,3]:
    modulus=1<<m; mask=modulus-1; found=0
    for entries in product(range(modulus),repeat=4):
        a=[[entries[0],entries[1]],[entries[2],entries[3]]]
        det=pmul(a[0][0],a[1][1])^pmul(a[0][1],a[1][0])
        if not det&1:continue
        dinv=scalar_inverse(det&mask,modulus)
        ai=reduce_mat([[pmul(dinv,a[1][1]),pmul(dinv,a[0][1])],
                       [pmul(dinv,a[1][0]),pmul(dinv,a[0][0])]],mask)
        assert reduce_mat(mmul(a,ai),mask)==I2
        e1=blocks(I2,a,O2,I2)
        e2=blocks(I2,O2,ai,I2)
        gamma=mmul(mmul(mmul(e1,e2),e1),J)
        # Each elementary shear is its own inverse over F2[t].
        inverse=mmul(mmul(mmul(J,e1),e2),e1)
        assert mmul(gamma,inverse)==I4
        assert mmul(inverse,gamma)==I4
        assert reduce_mat(gamma,mask)==blocks(a,O2,O2,ai)
        found+=1
    assert found==6*(2**(4*(m-1)))
    patch_count+=found
    print(f'Block lifting over F2[t]/t^{m}: all {found} invertible 2x2 matrices; '
          'lift and inverse checked exactly in F2[t]: PASS')
print(f'Patching total: {patch_count} complete matrix cases.')


class FiniteField:
    def __init__(self,p,modulus):
        self.p=p;self.mod=modulus;self.e=len(modulus)-1;self.Q=p**self.e
    def coeffs(self,a):
        c=[]
        for _ in range(self.e):c.append(a%self.p);a//=self.p
        return c
    def encode(self,a):
        return sum((x%self.p)*(self.p**i) for i,x in enumerate(a))
    def mul(self,a,b):
        ac,bc=self.coeffs(a),self.coeffs(b)
        c=[0]*(2*self.e-1)
        for i,x in enumerate(ac):
            for j,y in enumerate(bc):c[i+j]=(c[i+j]+x*y)%self.p
        for degree in range(len(c)-1,self.e-1,-1):
            z=c[degree]
            for j in range(self.e):c[degree-self.e+j]=(c[degree-self.e+j]-z*self.mod[j])%self.p
        return self.encode(c[:self.e])
    def power(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r


for p,modulus,q in [(2,[1,1,1],2),(2,[1,1,0,1],2),
                    (3,[1,0,1],3),(2,[1,1,0,0,1],4)]:
    F=FiniteField(p,modulus);Q=F.Q
    assert all(F.power(a,Q)==a for a in range(Q))
    assert all(F.power(a,Q-1)==1 for a in range(1,Q))
    fixed=[a for a in range(Q) if F.power(a,q)==a]
    assert len(fixed)==q
    for r in [1,2,3]:
        fixed_tuples=0
        for values in product(range(Q),repeat=r):
            powered=tuple(F.power(a,q) for a in values)
            if powered==values:fixed_tuples+=1
        assert fixed_tuples==q**r
        # Coordinate idempotents are fixed and give an l-basis after scalar extension.
        idempotents=[tuple(int(i==j) for i in range(r)) for j in range(r)]
        assert all(tuple(F.power(a,q) for a in e)==e for e in idempotents)
    print(f'Finite-field descent q={q}, Q={Q}: all functions on up to3 points; '
          'fixed ring has q^r elements and fixed idempotents span after extension: PASS')


# A concrete cusp correction: a=(X^2+X)/t^2, b=(a^2+a)/t,
# G=b^2 and F=a+tG are in Int(F2+t^2F2[[t]]); a=F+tG.
count=0
for x in range(1<<12):
    if x&2:continue
    anum=pmul(x,x)^x
    assert anum&3==0
    a=anum>>2
    bnum=pmul(a,a)^a
    assert bnum&1==0
    b=bnum>>1
    G=pmul(b,b)
    F=a^(G<<1)
    assert not G&2 and not F&2
    assert F^(G<<1)==a
    count+=1
print(f'Cusp correction: all {count} elements of R modulo t^12: PASS')
print('ALL B.021--023 EXACT CHECKS PASSED.')
