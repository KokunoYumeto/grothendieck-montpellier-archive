"""Independent Apéry optimality certificate check: potentials, not shortest paths."""
from pathlib import Path
from math import isqrt,gcd
import csv,json
HERE=Path(__file__).resolve().parent
DATA=HERE.parent/'root'/'PRIME_SEMIGROUP_CERTIFICATES.json'
def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def check(c):
    generators=c['generators'];g=c['modulus'];w=c['apery'];witnesses=c['witnesses']
    assert generators==sorted(set(generators))
    assert g==min(generators) and gcd(*generators)==1
    assert len(w)==len(witnesses)==g and w[0]==0
    for r,(value,coeff) in enumerate(zip(w,witnesses)):
        assert value>=0 and value%g==r
        assert len(coeff)==len(generators) and all(isinstance(x,int) and x>=0 for x in coeff)
        assert sum(x*h for x,h in zip(coeff,generators))==value
        # Along any path, these inequalities imply path length >= w(endpoint).
        # The printed witness realizes equality, proving exact minimality.
        for h in generators:assert w[(r+h)%g]<=value+h
    assert c['conductor']==max(w)-g+1>=0
    return lambda n:n>=w[n%g]
certs=json.loads(DATA.read_text());assert set(certs)==set(map(str,range(2,101)))
rows=[]
for a in range(2,101):
    c=certs[str(a)];member=check(c);minus=c['minus_only'];minusmember=check(minus)
    widths=[b for b in range(a,4*a+1) if b%2==0 and
            ((b-1>=3 and prime(b-1)) or (b+1>=3 and prime(b+1)))]
    assert c['widths']==widths and c['generators']==[b//2 for b in widths]
    for b in widths:
        sources=sorted(p for p in (b-1,b+1) if p>=3 and prime(p))
        assert sorted(c['seed_sources'][str(b)])==sources
    assert all(p>=3 and prime(p) and a<=p-1<=4*a for p in minus['primes'])
    assert minus['generators']==[(p-1)//2 for p in minus['primes']]
    # Also check every boundary generator, including p=4a+1.
    fullminus=[b//2 for b in range(a,4*a+1) if b%2==0 and prime(b+1)]
    assert all(minusmember(g) for g in fullminus)
    assert c['conductor']<=2*a and minus['conductor']<=2*a
    rows.append(dict(rank=a,both_even_conductor=2*c['conductor'],
                     minus_even_conductor=2*minus['conductor'],
                     all_Apery_edge_potentials_and_witnesses='PASS',
                     all_prime_adjacent_widths_through_4a='PASS',
                     entire_infinite_seed_semigroup='PASS'))
with (HERE/'PRIME_SEMIGROUP_INDEPENDENT_CHECK.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print('PASS 198 Apéry certificates by potential inequalities and explicit witnesses; trial-division seed enumeration; all boundary and omitted-width conditions')
