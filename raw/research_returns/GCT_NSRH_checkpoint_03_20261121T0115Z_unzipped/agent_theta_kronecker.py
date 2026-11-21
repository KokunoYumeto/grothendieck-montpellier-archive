from functools import lru_cache
from collections import Counter
from fractions import Fraction
from math import factorial

@lru_cache(None)
def parts(n, bound=None):
    if n==0:return ((),)
    if bound is None:bound=n
    return tuple((j,)+p for j in range(min(n,bound),0,-1) for p in parts(n-j,j))

@lru_cache(None)
def rim_removals(lam,k):
    out=[]
    for mu in parts(sum(lam)-k):
        if len(mu)>len(lam) or any(mu[i]>lam[i] for i in range(len(mu))):continue
        cells={(i,j) for i,v in enumerate(lam) for j in range(mu[i] if i<len(mu) else 0,v)}
        if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}<=cells for i,j in cells):continue
        if not cells:continue
        reached={next(iter(cells))};front=list(reached)
        while front:
            i,j=front.pop()
            for a in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if a in cells and a not in reached:reached.add(a);front.append(a)
        if reached!=cells:continue
        out.append((mu,(-1)**(len({i for i,j in cells})-1)))
    return tuple(out)

@lru_cache(None)
def character(lam,rho):
    if not rho:return int(not lam)
    return sum(sign*character(mu,rho[1:]) for mu,sign in rim_removals(lam,rho[0]))

def centralizer(rho):
    z=1
    for k,m in Counter(rho).items():z*=k**m*factorial(m)
    return z

def kron(lam,mu,nu):
    return sum(Fraction(character(lam,rho)*character(mu,rho)*character(nu,rho),centralizer(rho)) for rho in parts(sum(lam)))

if __name__=='__main__':
    for n in (4,9):
        ps=parts(n)
        for a in ps:
            for b in ps:
                inner=sum(Fraction(character(a,rho)*character(b,rho),centralizer(rho)) for rho in ps)
                assert inner==int(a==b),(n,a,b,inner)
        print('character orthogonality checked for n=',n)
        mu=(2,2) if n==4 else (3,3,3)
        for lam in ps:
            g=kron(lam,mu,mu)
            assert g.denominator==1 and g>=0
            if g>1: print(lam,mu,mu,g)
