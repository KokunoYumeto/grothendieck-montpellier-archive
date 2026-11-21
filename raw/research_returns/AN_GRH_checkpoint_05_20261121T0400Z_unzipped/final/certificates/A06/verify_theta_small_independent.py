"""Independent elementary arithmetic check of the finite part of finding A06."""
from collections import defaultdict
from math import gcd, isqrt

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def order(a,p):
    x=1
    for e in range(1,p):
        x=x*a%p
        if x==1:return e
    raise AssertionError((a,p))

candidate=[p for p in range(3,705) if prime(p) and (p-1)%19==0]
assert candidate==[191,229,419,457,571,647]
orders=[order(2,p) for p in candidate]
assert orders==[95,76,418,76,114,323]
survivors=[]
for p in candidate:
    if order(2,p)!=p-1:continue
    g=pow(2,19,p)
    H={pow(g,e,p) for e in range(order(g,p))}
    assert len(H)==(p-1)//gcd(p-1,19)
    differences=defaultdict(list)
    for a in H|{0}:
        for b in H|{0}:
            if a!=b:differences[(a-b)%p].append((a,b))
    assert all((a,b) in differences[2] for a,b in [(1,418),(71,69),(350,348)])
    assert len(differences[2])>=3
    print({'p':p,'generator':g,'H_order':len(H),'difference_2_pairs':sorted(differences[2])})
    survivors.append(p)
assert survivors==[419]
print({'candidate_primes':candidate,'orders_of_2':orders,'finite_A06_obstruction':'PASS'})
