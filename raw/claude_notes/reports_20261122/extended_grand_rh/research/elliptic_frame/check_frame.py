"""Exact polynomial arithmetic checks for 269a1, with no external dependencies."""
from collections import Counter
from itertools import combinations, product
from math import isqrt


def trim(f):
    f = list(f)
    while f and not f[-1]:
        f.pop()
    return tuple(f)


def subtract(f, g, p):
    out = list(f) + [0] * max(0, len(g) - len(f))
    for i, a in enumerate(g):
        out[i] -= a
    return trim(a % p for a in out)


def remainder(f, modulus, p):
    f = trim(a % p for a in f)
    inverse = pow(modulus[-1], -1, p)
    while len(f) >= len(modulus):
        shift = len(f) - len(modulus)
        lead = f[-1] * inverse
        f = subtract(f, (0,) * shift + tuple(lead * a for a in modulus), p)
    return f


def gcd(f, g, p):
    f = trim(a % p for a in f)
    g = trim(a % p for a in g)
    while g:
        f, g = g, remainder(f, g, p)
    return trim((a * pow(f[-1], -1, p)) % p for a in f)


def multiply(f, g, modulus, p):
    if not f or not g:
        return ()
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i+j] += a*b
    return remainder(out, modulus, p)


def power(f, exponent, modulus, p):
    result = (1,)
    f = remainder(f, modulus, p)
    while exponent:
        if exponent & 1:
            result = multiply(result, f, modulus, p)
        f = multiply(f, f, modulus, p)
        exponent //= 2
    return result


X = (0,1)
quartic = (-4,-9,-12,0,3)
sextic = (-27,0,64,0,-24,0,3)
cubic = (-269,0,0,1)
ysquare = (-3,-8,0,4)  # (2y+1)^2 for the curve


def rational_roots(modulus, p, k):
    return gcd(modulus, subtract(power(X, p**k, modulus, p), X, p), p)


def torsion_size(p, k):
    # The four distinct x-coordinates solve quartic; at each rational x
    # exactly two y occur iff 4x^3-8x-3 is a square in the extension.
    assert p % 2 and p not in (3,269)
    xs = rational_roots(quartic,p,k)
    ytest = subtract(power(ysquare, (p**k - 1)//2, quartic,p), (1,),p)
    return 1+2*(len(gcd(xs,ytest,p))-1)


def partitions():
    return [frozenset((frozenset((0,j)),frozenset(set(range(4))-{0,j}))) for j in range(1,4)]


def matrix_mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % 3
                 for i,j in product(range(2),repeat=2))


def matrix_pow(a,n):
    z=(1,0,0,1)
    for _ in range(n):
        z=matrix_mul(z,a)
    return z


def act(a,v):
    return ((a[0]*v[0]+a[1]*v[1])%3,(a[2]*v[0]+a[3]*v[1])%3)


def line(v):
    return min(v,tuple(-b % 3 for b in v))


def check_group():
    vs=list(product(range(3),repeat=2))
    ls=sorted(set(line(v) for v in vs if v!=(0,0)))
    ps=partitions()
    actions=set()
    kernel=[]
    rows=Counter()
    for a in product(range(3),repeat=4):
        det=(a[0]*a[3]-a[1]*a[2])%3
        if not det:
            continue
        perm=tuple(ls.index(line(act(a,v))) for v in ls)
        img=tuple(ps.index(frozenset(frozenset(perm[i] for i in pair) for pair in part)) for part in ps)
        actions.add(img)
        t=sum(i==j for i,j in enumerate(img))-1
        if t==2:
            kernel.append(a)
        pairs=tuple(combinations(range(4),2))
        fixed_pairs=sum(frozenset((perm[i],perm[j]))==frozenset((i,j)) for i,j in pairs)
        assert t == fixed_pairs - sum(i==j for i,j in enumerate(perm))
        t2=sum(act(matrix_pow(a,2),v)==v for v in vs)
        t4=sum(act(matrix_pow(a,4),v)==v for v in vs)
        if det==1:
            assert t==(t4-5)//2 and t==3*({1:0,3:1,9:2}[t2]-1)**2-1
        else:
            assert t==0
        rows[det,t,t2,t4]+=1
    assert len(kernel)==8 and len(actions)==6 and sum(rows.values())==48
    print("GL2(F3) det, trace, torsion over quadratic and quartic fields, frequency")
    for key,num in sorted(rows.items()):
        print(*key,num)


def check_primes(limit):
    tested=Counter()
    examples={}
    for p in range(2,limit+1):
        if p in (3,269) or any(p%i==0 for i in range(2,isqrt(p)+1)):
            continue
        t=0 if p%3==2 else (2 if pow(269,(p-1)//3,p)==1 else -1)
        d1,d2=(len(rational_roots(quartic,p,k))-1 for k in [1,2])
        assert d1*d1-4*d1+d2==2*t
        if p!=2:
            u=torsion_size(p,2)
            v=torsion_size(p,4)
            if p%3==1:
                assert t==3*({1:0,3:1,9:2}[u]-1)**2-1 and t==(v-5)//2
                examples.setdefault((t,u,v),(p,d1,d2))
            for j in range(1,7):
                fixed=lambda poly: len(rational_roots(poly,p,j))-1
                assert fixed(sextic)-fixed(quartic)==fixed(cubic)-1
        tested[t]+=1
    print("Prime tests through",limit,"by trace:",sorted(tested.items()))
    print("Trace, quadratic torsion, quartic torsion -> p, quartic root counts:",sorted(examples.items()))


if __name__=="__main__":
    fp=tuple(a%5 for a in quartic)
    rem=subtract(power(X,25,fp,5),X,5)
    assert rem==(0,4,3,4) and gcd(fp,rem,5)==(1,)
    check_group()
    check_primes(1000)
