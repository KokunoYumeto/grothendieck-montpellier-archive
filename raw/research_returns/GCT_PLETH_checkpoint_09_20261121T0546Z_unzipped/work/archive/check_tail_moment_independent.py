"""R046: independent three-coordinate normalized split-moment check."""
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import comb,factorial
from fractions import Fraction
from collections import defaultdict
import json

def compositions(d):
    for p in range(d+1):
        for q in range(d-p+1):yield (p,q,d-p-q)

counts=0
for d in range(2,7):
  for n in (d,d+1):
    rows=[((i*i+1)%7-3,(2*i*i+i)%9-4,(i*i*i+3)%11-5) for i in range(n-1)]
    rows.append(tuple(-sum(v[j] for v in rows) for j in range(3)))
    polynomial={(0,0,0):1}
    for v in rows:
        nxt=defaultdict(int)
        for exp,c in polynomial.items():
            nxt[exp]+=c
            for j in range(3):
                target=list(exp);target[j]+=1;nxt[tuple(target)]+=c*v[j]
        polynomial=dict(nxt)
    @lru_cache(None)
    def moment(exp):return sum(product_value(v,exp) for v in rows)
    def product_value(v,exp):
        z=1
        for x,e in zip(v,exp):z*=x**e
        return z
    @lru_cache(None)
    def distinct(exp):
        if not sum(exp):return 1
        first=next(i for i,v in enumerate(exp) if v)
        remaining=list(exp);remaining[first]-=1;answer=0
        for chosen in product(*(range(v+1) for v in remaining)):
            block=list(chosen);block[first]+=1;size=sum(block)
            coefficient=(-1)**(size-1)*factorial(size-1)
            for c,k in zip(remaining,chosen):coefficient*=comb(c,k)
            rest=tuple(c-k for c,k in zip(remaining,chosen))
            answer+=coefficient*moment(tuple(block))*distinct(rest)
        return answer
    for exp in compositions(d):
        normal=Fraction(factorial(n-d),factorial(n))
        lhs=normal*distinct(exp)
        rhs=normal*polynomial.get(exp,0)
        for e in exp:rhs*=factorial(e)
        assert lhs==rhs,(d,n,exp,lhs,rhs)
        counts+=1
out={'statement':'R046 independent normalized split-moment audit','status':'PASS',
     'method':'three-coordinate product-form expansion versus submultiset first-block Mobius recursion; exact fractions; no source imports',
     'degrees':[2,6],'row_counts':'d and d+1','normalized_entries':counts}
(Path(__file__).resolve().parent/'TAIL_MOMENT_NORMALIZATION_INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
