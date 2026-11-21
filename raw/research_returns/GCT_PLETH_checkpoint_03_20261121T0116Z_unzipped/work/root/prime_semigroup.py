"""Explicit prime-block semigroups and canonical-image degree certificates."""
from __future__ import annotations
import csv, heapq, json, math
from pathlib import Path


def primes_upto(n):
    flags=bytearray(b'\1')*(n+1)
    flags[:2]=b'\0\0'
    for p in range(2,math.isqrt(n)+1):
        if flags[p]: flags[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if flags[p]]


def apery(gens):
    gens=sorted(set(gens)); g=gens[0]
    assert math.gcd(*gens)==1
    dist=[None]*g; prev=[None]*g; dist[0]=0
    queue=[(0,0)]
    while queue:
        d,r=heapq.heappop(queue)
        if d!=dist[r]: continue
        for h in gens:
            t=(r+h)%g; v=d+h
            if dist[t] is None or v<dist[t]:
                dist[t]=v; prev[t]=(r,h); heapq.heappush(queue,(v,t))
    assert all(v is not None for v in dist)
    witnesses=[]
    for r,w in enumerate(dist):
        coeff=[0]*len(gens); at=r
        while at:
            old,h=prev[at]; coeff[gens.index(h)]+=1; at=old
        assert sum(c*h for c,h in zip(coeff,gens))==w
        assert w%g==r
        witnesses.append(coeff)
    conductor=max(dist)-g+1
    # Independent Boolean DP verifies minimality and every gap through the conductor.
    bound=max(dist)+g+max(gens)
    reachable=[False]*(bound+1); reachable[0]=True
    for n in range(1,bound+1):
        reachable[n]=any(n>=h and reachable[n-h] for h in gens)
    assert all(reachable[n]==(n>=dist[n%g]) for n in range(bound+1))
    assert all(reachable[n] for n in range(conductor,bound+1))
    assert conductor==0 or not reachable[conductor-1]
    return {'generators':gens,'modulus':g,'apery':dist,'witnesses':witnesses,
            'conductor':conductor,'dp_bound':bound}


def main():
    out=Path(__file__).resolve().parent
    rows=[]; certificates={}
    all_primes=primes_upto(401)
    for a in range(2,101):
        minus_ps=[p for p in all_primes if a<p<=4*a+1 and p!=2]
        minus=apery([(p-1)//2 for p in minus_ps])
        seed_sources={}
        for p in all_primes:
            if p==2: continue
            for b in (p-1,p+1):
                if a<=b<=4*a:
                    seed_sources.setdefault(b,[]).append(p)
        widths=sorted(seed_sources)
        cert=apery([b//2 for b in widths])
        cert['widths']=widths; cert['rank']=a
        cert['seed_sources']={str(b):seed_sources[b] for b in widths}
        cert['minus_only']={'primes':minus_ps,**minus}
        # Omitted widths exceed 4a and hence their halves exceed 2a.
        # This verifies that the finite list generates ALL prime-adjacent widths.
        assert cert['conductor']<=2*a
        assert minus['conductor']<=2*a
        certificates[str(a)]=cert
        rows.append({'rank_a':a,'seed_widths':','.join(map(str,widths)),
                     'gcd_normalized':math.gcd(*cert['generators']),
                     'normalized_conductor':cert['conductor'],
                     'even_degree_from':2*cert['conductor'],
                     'minus_only_even_degree_from':2*minus['conductor'],
                     'full_surjectivity_source_bound':(a-1)**2,
                     'minimum_positive_semigroup_degree':widths[0],
                     'independent_dp_bound':cert['dp_bound'],
                     'all_prime_adjacent_widths_generated':'YES','outcome':'PASS'})
    with (out/'PRIME_SEMIGROUP_RANGES.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t');w.writeheader();w.writerows(rows)
    (out/'PRIME_SEMIGROUP_CERTIFICATES.json').write_text(json.dumps(certificates,indent=2)+'\n')
    for a in [2,3,4,5,6,7,8,9,10,12,16,20,26,32,50,64,100]:
        c=certificates[str(a)]
        print(a,2*c['conductor'],2*c['minus_only']['conductor'],(a-1)**2,c['modulus'],len(c['widths']))
    print('PASS: 198 finite seed sets; all Apéry witnesses and independent DP checks')

if __name__=='__main__': main()
