"""Verify the four marked prime classes and local norm fibres."""
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt


def marked(n, R, D):
    return [(u, v) for u in range(1, D+1) for v in range(1, D+1)
            if gcd(u, v) == gcd(u*v, 4*R) == 1
            and u % R == 1 and v % R == R-1 and (n+R) % (u*v) == 0]


def reduced_norm_sizes(m):
    return Counter(val for a in range(m) for b in range(m)
                   if gcd(val := (a*a-a*b+b*b) % m, m) == 1)


def local_checks():
    for q, exp in [(2,1),(2,5),(5,2),(11,1),(17,1),(269,1),
                   (7,1),(7,2),(13,1),(3,1),(3,2),(3,4)]:
        m = q**exp
        sizes = reduced_norm_sizes(m)
        if q == 3:
            assert max(sizes.values()) <= 2*m
            assert set(sizes.values()) == {2*m}
        else:
            exact = q**(exp-1)*(q+(1 if q%3 == 2 else -1))
            assert set(sizes.values())=={exact}
            assert len(sizes)==m-m//q


def main():
    local_checks()
    observed = set()
    for p in (26881,45361,63841,451921):
        assert not any(p%q==0 for q in range(2,isqrt(p)+1))
        assert p%9240 == 8401 and p%840 == 1 and (p+3)%11 == 0
        assert marked(p,3,11)==[(1,11)]
        v=pow(3,(p-1)//4,p)
        t=2 if pow(269,(p-1)//3,p)==1 else -1
        assert v in (1,p-1)
        pair=(1 if v==1 else -1,t)
        observed.add(pair)
        a,b,c=(p+3)//4,p*(p+3)//11,p*(p+3)
        assert Fraction(1,a)+Fraction(1,b)+Fraction(1,c)==Fraction(4,p)
        assert a%p and b%p==c%p==0
        print(p, pair, 'denominators',a,b,c)
    assert len(observed)==4
    count=0
    for R in (3,7,11,15):
        for p in range(R+1,1700):
            if p%12!=1 or any(p%q==0 for q in range(2,isqrt(p)+1)):continue
            a=(p+R)//4
            pairs=set()
            for u,v in marked(p,R,39):
                b,c=p*a*(u+v)//(R*v),p*a*(u+v)//(R*u)
                assert b%p==c%p==0 and Fraction(1,a)+Fraction(1,b)+Fraction(1,c)==Fraction(4,p)
                assert (b//gcd(b,c),c//gcd(b,c))==(u,v)
                pairs.add((b,c));count+=1
            assert len(pairs)==len(marked(p,R,39))
    print('additional ordered mark checks:',count)


if __name__=="__main__":
    main()
