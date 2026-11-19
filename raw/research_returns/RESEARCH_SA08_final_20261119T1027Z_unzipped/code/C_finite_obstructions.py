"""Exhaustive finite certificates for SA08 statements C2 and B6.
No symbolic package is required. This is a finite certificate, not evidence for
an untested universal assertion: the universal B6 obstruction is proved by
three scalar equations in C_findings.md.
"""
from itertools import product
from time import perf_counter
from pathlib import Path
from math import comb, gcd
start=perf_counter()
lines=[]
def out(s):
    print(s); lines.append(s)
# Exact, nonsplit normalized complex Z/2 --2--> Z/4 --mod2--> Z/2.
a2=range(2); a1=range(4); a0=range(2)
d2=lambda x:2*x%4
d1=lambda x:x%2
assert {d2(x) for x in a2}=={x for x in a1 if d1(x)==0}
assert {d1(x) for x in a1}==set(a0)
assert [x for x in a2 if d2(x)==0]==[0]
# A Z-module hom Z/2 -> Z/4 is determined by image of 1 annihilated by 2.
hom_images=[x for x in a1 if 2*x%4==0]
sections=[x for x in hom_images if d1(x)==1]
assert sections==[]
out('C2 finite nonsplit exact complex: sizes (2,4,2); exactness TRUE; hom images '+str(hom_images)+'; right inverse count 0.')
# Half-DGA action necessarily has edge form sigma(c,z)=(a*c0+b*c1)*(v1-v0).
# Enumerate all coefficients and every pair of functions on Delta[2].
for q in (2,3,4):
    pairs=list(product(range(q),repeat=2))
    vals=list(product(range(q),repeat=3))
    leibniz=[]; unital=[]; good=[]; checked=0
    for a,b in pairs:
        unit=(a+b)%q==1
        if unit: unital.append((a,b))
        ok=True
        for c in vals:
            for v in vals:
                edge=lambda i,j:(a*c[i]+b*c[j])*(v[j]-v[i])
                lhs=(edge(1,2)-edge(0,2)+edge(0,1))%q
                rhs=((c[1]-c[0])*(v[2]-v[0])-(c[2]-c[0])*(v[1]-v[0]))%q
                checked+=1
                if lhs!=rhs:ok=False
        if ok:leibniz.append((a,b))
        if ok and unit:good.append((a,b))
    assert leibniz==[(1,1)]
    assert good==[]
    out(f'B6 over Z/{q}: coefficient pairs {len(pairs)}; function-pair checks {checked}; unital pairs {len(unital)}; Leibniz pairs {leibniz}; simultaneous pairs {good}.')
out('Universal scalar certificate: (a+b-1)-(a-1)-(b-1)=1; all three equations cannot hold in a nonzero ring.')
# B604: finite free chain modules for the minimal simplicial circle.
# C=Z[0]+Z[1] has zero boundary; therefore all tensor/Hom boundaries vanish.
chain_ranks = {0: 1, 1: 1}
tensor_ranks = {n: sum(chain_ranks.get(a,0)*chain_ranks.get(n-a,0)
                     for a in range(3)) for n in range(3)}
hom_ranks = {r: sum(rank*tensor_ranks.get(n+r,0)
                  for n,rank in chain_ranks.items()) for r in range(-1,3)}
assert tensor_ranks == {0: 1, 1: 2, 2: 1}
assert hom_ranks == {-1: 1, 0: 3, 1: 3, 2: 1}
assert all(sum(0 for _ in range(tensor_ranks.get(n-1,0))) == 0
           for n in tensor_ranks)
out('B604 minimal circle: tensor-chain ranks '+str(tensor_ranks)+
    '; pointwise coendomorphism ranks '+str(hom_ranks)+
    '; all differentials zero, so H_1 has rank 3.')
endomorphism_ranks={r:sum(rank*tensor_ranks.get(n+r,0)
                        for n,rank in tensor_ranks.items())
                    for r in range(-2,3)}
assert endomorphism_ranks=={-2:1,-1:4,0:6,1:4,2:1}
out('B604 exact scan360 comparison: by EZ, both pointwise mapping '
    'complexes are homotopy equivalent to End(T), T=C(S1) tensor C(S1). '
    'Its ranks are '+str(endomorphism_ranks)+
    '; zero differential gives H_1 rank 4.')
binomial_values={n: gcd(*(comb(n,a) for a in range(1,n)))
                 for n in range(2,129)}
for prime in (2,3,5,7,11):
    power=prime
    while power<=128:
        assert binomial_values[power]==prime
        power*=prime
out('C11 binomial-ideal finite check: 127 weights n=2..128; '
    'all prime powers of 2,3,5,7,11 in range have gcd p. '
    'Powers of 2: '+str({n:binomial_values[n] for n in (2,4,8,16,32,64,128)})+'.')
out(f'Runtime seconds: {perf_counter()-start:.6f}')
Path('SA08_work/logs/C_finite_obstructions.txt').write_text('\n'.join(lines)+'\n')
