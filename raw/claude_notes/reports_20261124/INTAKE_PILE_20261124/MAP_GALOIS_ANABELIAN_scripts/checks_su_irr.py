from fractions import Fraction
from math import comb
import itertools, random
# 1) j-invariant of Legendre curve and p-adic integrality <-> lambda in U(Z_p) for odd p
def vp(x, p):
    x = Fraction(x)
    if x == 0: return 10**9
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0: n//=p; v+=1
    while d % p == 0: d//=p; v-=1
    return v
def j(l):
    l = Fraction(l)
    return 256*(l*l-l+1)**3/(l*l*(1-l)**2)
random.seed(1)
bad = 0
for _ in range(20000):
    a = random.randint(-500,500); b = random.randint(1,500)
    l = Fraction(a,b)
    if l in (0,1): continue
    for p in (3,5,7,11,13):
        inU = vp(l,p)==0 and vp(1-l,p)==0
        jint = vp(j(l),p) >= 0
        if inU != jint: bad += 1
print("j-integrality <-> lambda in U(Z_p) (odd p) mismatches:", bad)
# 2) U(Z[1/2]) and U(Z[1/6]) by brute force over S-units with bounded exponents
def sunits(primes, E):
    out=set()
    for exps in itertools.product(range(-E,E+1), repeat=len(primes)):
        v=Fraction(1)
        for p,e in zip(primes,exps): v*=Fraction(p)**e
        out.add(v); out.add(-v)
    return out
for primes in ([2],[2,3]):
    U=sunits(primes, 12)
    sols=sorted(l for l in U if (1-l) in U and l not in (0,1))
    print(primes, len(sols), [str(s) for s in sols][:40])
    print("  j values:", sorted(set(str(j(s)) for s in sols))[:12])
# 3) Bernoulli numbers and irregular pairs (l, k), l < 200
def bernoulli(N):
    B=[Fraction(0)]*(N+1); B[0]=Fraction(1)
    for m in range(1,N+1):
        B[m] = -sum(comb(m+1,k)*B[k] for k in range(m))/Fraction(m+1)
    return B
B=bernoulli(200)
def isprime(n): return n>1 and all(n%q for q in range(2,int(n**0.5)+1))
pairs=[]
for l in range(3,200):
    if not isprime(l): continue
    for k in range(2,l-2,2):
        if B[k].numerator % l == 0: pairs.append((l,k))
print("irregular pairs l<200:", pairs)
print("=> class r = k-1 (mod l-1) where the SECTION_GHOSTS B.25 obstruction group H^2(G_{Q,{l,inf}},Z_l(r+1)) = K_{2r}(Z)_l can be nonzero:")
print([(l, k-1) for (l,k) in pairs])
