"""T053: literal standard-monomial tags against independent Koszul row characters."""
from pathlib import Path
from itertools import product
from functools import lru_cache
from collections import Counter
import json
HERE=Path(__file__).resolve().parent
@lru_cache(None)
def compositions(n,m):
    if m==0:return ((),) if n==0 else ()
    return tuple((i,)+tail for i in range(n+1) for tail in compositions(n-i,m-1))
@lru_cache(None)
def raw_count(m,eta,k):
    if any(x<0 for x in eta):return 0
    return sum(all(sum(row[i] for row in rows)>=k for i in range(m))
               for rows in product(*(compositions(x,m) for x in eta)))
def standard(m,eta,k):
    r=len(eta);tags=Counter()
    for rows in product(*(compositions(x,m) for x in eta)):
        v=tuple(sum(row[i] for row in rows)-k for i in range(m))
        if min(v)<0 or any(rows[a][a] and v[a] for a in range(r)):continue
        tag=tuple(a for a in range(r) if v[a]>0)
        assert all(rows[a][a]==0 and v[a]>=1 for a in tag)
        assert all(v[a]==0 for a in range(r) if a not in tag)
        assert all(0<=u<=eta[a] for a,row in enumerate(rows) for u in row)
        assert all(0<=q<=sum(eta) for q in v)
        tags[tag]+=1
    return tags
cases=points=empty=0;by_rank=[]
for r,m,limit,kmax in ((1,3,13,4),(1,4,11,3),(2,4,5,3),(2,5,4,2),(3,5,2,2)):
    here=0
    for eta in product(range(limit+1),repeat=r):
        for k in range(kmax+1):
            tags=standard(m,eta,k);actual=sum(tags.values())
            expected=0
            for bits in product((0,1),repeat=r):
                shifted=tuple(a-b for a,b in zip(eta,bits))
                expected+=(-1)**sum(bits)*raw_count(m,shifted,k)
            assert actual==expected>=0,(m,eta,k,actual,expected)
            assert len(tags)<=2**r
            if sum(eta)<m*k:assert actual==0;empty+=1
            if sum(eta)==0 and k==0:assert tags=={():1}
            cases+=1;here+=1;points+=actual
    by_rank.append(dict(r=r,m=m,maximum_row_weight=limit,maximum_charge=kmax,cases=here))
receipt=dict(statement='T053 charged incidence row polytopes',status='PASS',
 cases=cases,standard_monomial_points=points,forced_empty_cases=empty,by_rank=by_rank,
 method='literal row-composition matrices, forced Y exponents and disjoint standard tags, compared with the independent exterior Koszul alternating sum of truncated block counts',
 note='Includes smaller-row embeddings, zero weight/charge and impossible total-degree endpoints; no individual plethysm coefficient is identified with these whole row-weight counts.')
(HERE/'CHARGED_INCIDENCE_POLYTOPE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
