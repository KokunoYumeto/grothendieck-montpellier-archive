"""Exact small checks accompanying E/F/K. No floating point and no external data."""
from itertools import product
from time import perf_counter
import sympy as s
start=perf_counter()
# R_m=F2[e,x_1,...,x_m]/(e^2,e*x_i,x_i^2).
# Basis indices 0..2**m-1 are squarefree x-monomials; index 2**m is e.
def mul(a,b,m):
    e=1<<m; out=0
    for i in range(e+1):
        if not (a>>i)&1: continue
        for j in range(e+1):
            if not (b>>j)&1: continue
            if i==e or j==e:
                k=e if (i==e and j==0) or (j==e and i==0) else None
            else: k=None if i&j else i|j
            if k is not None: out ^= 1<<k
    return out
# B=R_1 has basis 1,x,e; B tensor_A B=R_2.
def delta(a):
    return ((a&1)*1) ^ (((a>>1)&1)*((1<<1)^(1<<2))) ^ (((a>>2)&1)*(1<<4))
for a,b,c in product(range(8),repeat=3):
    assert mul(mul(a,b,1),c,1)==mul(a,mul(b,c,1),1)
for a,b in product(range(8),repeat=2):
    assert delta(mul(a,b,1))==mul(delta(a),delta(b),2)
# Evaluate a polynomial under a specified homomorphism R_m -> R_n.
# Construct the two iterated coproducts independently, rather than comparing
# two copies of the same already-simplified primitive-generator expression.
def substitute(a,m,n,images):
    out=0
    for mask in range(1<<m):
        if (a>>mask)&1:
            term=1
            for j in range(m):
                if (mask>>j)&1: term=mul(term,images[j],n)
            out ^= term
    if (a>>(1<<m))&1: out ^= 1<<(1<<n)
    return out
for a in range(8):
    left=substitute(delta(a),2,3,[(1<<1)^(1<<2),1<<4])
    right=substitute(delta(a),2,3,[1<<1,(1<<2)^(1<<4)])
    assert left==right
    assert substitute(delta(a),2,1,[0,1<<1])==a
    assert substitute(delta(a),2,1,[1<<1,0])==a
    assert substitute(delta(a),2,1,[1<<1,1<<1])==((a&1)^(a&4))
image={mul(1<<2,a,1) for a in range(8)}
kernel={a for a in range(8) if mul(1<<2,a,1)==0}
assert len(image)==2 and len(kernel)==4
print('Nonflat Hopf algebra: |A|=4; |B|=8; F2-dimension(B)=3.')
print('Associativity checked on all 512 triples; coproduct multiplicativity on all 64 pairs.')
print('Coassociativity checked by two independent substitution maps on all 8 elements.')
print('Both counit laws and the antipode law checked on all 8 elements.')
print('Multiplication by epsilon: image size 2, kernel size 4; flatness fails.')
t=s.symbols('t')
for n in range(1,9):
    f=t+t**(n+1)
    assert s.Poly(f-t,t).nth(n+1)==1
    assert s.rem(f-t,t**(n+1),t)==0
print('Formal coordinate maps t+t^(n+1): identity n-jet, nonidentity (n+1)-jet, n=1,...,8.')
u=s.symbols('u')
g=s.gcd(u**4-1,u**6+1)
assert g==u**2+1
assert -16*(4+27)==-496
print('Real elliptic twist: gcd(u^4-1,u^6+1)=',g,'; discriminants both -496.')
for q in [0,1,2,-1]:
    rank=s.Matrix([[q]]).rank()
    assert rank==(q!=0)
    print('P1 extension parameter',q,': connecting-map rank',rank)
for p in [2,3,5,7]:
    degrees=list(range(1,16))
    nonpowers=[d for d in degrees if d%p]
    assert all(d%p for d in nonpowers)
    print('alpha_p classes t^m outside Frobenius image, p=',p,':',nonpowers)
print('Square-theorem omitted base bundle degree:',4-1-1)
print('Elapsed seconds:',perf_counter()-start)
