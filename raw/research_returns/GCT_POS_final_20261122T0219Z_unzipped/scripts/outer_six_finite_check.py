"""Complete n<=3 outer-six table by two distinct exact character methods.

Method A expands the power-sum plethysm and uses Murnaghan--Nakayama.
Method B expands weights of six-variable Sym^n and uses the Weyl
alternant to extract highest weights.  This is a finite validation
baseline, not the requested uniform positive Cox-ring evaluator.
"""
from symmetric_character import partitions, character, centralizer_size
from fractions import Fraction
from itertools import permutations
from collections import defaultdict
from math import factorial
from pathlib import Path
from time import monotonic
import json,csv

M=6; OUT=Path(__file__).resolve().parents[1]/'certificates'
LABELS=list(partitions(M)); CLASSES=LABELS
TABLE={mu:[character(mu,rho) for rho in CLASSES] for mu in LABELS}
for mu in LABELS:
    for nu in LABELS:
        assert sum(Fraction(a*b,centralizer_size(rho)) for a,b,rho in zip(TABLE[mu],TABLE[nu],CLASSES))==int(mu==nu)

def compositions(n,r):
    if r==1:
        yield (n,); return
    for a in range(n+1):
        for tail in compositions(n-a,r-1):
            yield (a,)+tail

def ps_product(n,rho):
    result={():Fraction(1)}
    inner=list(partitions(n))
    for r in rho:
        new=defaultdict(Fraction)
        for old,c in result.items():
            for tau in inner:
                key=tuple(sorted(old+tuple(r*t for t in tau),reverse=True))
                new[key]+=c/Fraction(centralizer_size(tau))
        result=new
    return result

def weight_products(n):
    base=list(compositions(n,M)); zero=(0,)*M
    cache={():{zero:1}}
    def get(rho):
        if rho in cache:return cache[rho]
        last=rho[-1]; smaller=get(rho[:-1]); new=defaultdict(int)
        multiples=[tuple(last*x for x in b) for b in base]
        for old,c in smaller.items():
            for b in multiples:
                new[tuple(x+y for x,y in zip(old,b))]+=c
        cache[rho]=dict(new);return cache[rho]
    return {rho:get(rho) for rho in CLASSES}

PERMS=[]
rho_shift=tuple(range(M-1,-1,-1))
for p in permutations(range(M)):
    sign=(-1)**sum(p[i]>p[j] for i in range(M) for j in range(i+1,M))
    shift=tuple(rho_shift[i]-rho_shift[p[i]] for i in range(M))
    PERMS.append((shift,sign))

rows=[]; stats=[]; start=monotonic()
for n in range(4):
    ps={rho:ps_product(n,rho) for rho in CLASSES}
    wp=weight_products(n)
    shapes=list(partitions(M*n))
    for mu in LABELS:
        expanded=defaultdict(Fraction)
        weights=defaultdict(int)
        for chi,rho in zip(TABLE[mu],CLASSES):
            if chi==0:continue
            factor=Fraction(chi,centralizer_size(rho))
            for tau,c in ps[rho].items():expanded[tau]+=factor*c
            integer_factor=chi*factorial(M)//centralizer_size(rho)
            for w,c in wp[rho].items():weights[w]+=integer_factor*c
        weights={w:c//factorial(M) for w,c in weights.items() if c}
        # A representation's actual weights have nonnegative integral multiplicity.
        for w in set().union(*(set(p) for p in wp.values())):
            numerator=sum(chi*factorial(M)//centralizer_size(rho)*wp[rho].get(w,0)
                          for chi,rho in zip(TABLE[mu],CLASSES))
            assert numerator%factorial(M)==0 and numerator>=0
        positive=0
        for lam in shapes:
            a=sum(c*character(lam,tau) for tau,c in expanded.items() if c)
            assert a.denominator==1 and a>=0
            if len(lam)>M:
                b=0
            else:
                padded=lam+(0,)*(M-len(lam)); b=0
                for shift,sign in PERMS:
                    key=tuple(x+y for x,y in zip(padded,shift))
                    if min(key)>=0:b+=sign*weights.get(key,0)
            assert a==b,(n,mu,lam,a,b)
            rows.append({'n':n,'outer':','.join(map(str,mu)),'output':','.join(map(str,lam)),
                         'power_sum_MN':int(a),'weight_alternant':b})
            positive+=int(a>0)
        stats.append({'n':n,'outer':mu,'partitions_checked':len(shapes),'nonzero':positive})
        print(json.dumps(stats[-1]),flush=True)
    with (OUT/'outer_six_n_le_3.tsv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    (OUT/'outer_six_n_le_3_summary.json').write_text(json.dumps({
        'status':'PASS through indicated degrees','rows':len(rows),'through_n':n,
        'methods':['power-sum plethysm and symmetric-group character inner product',
                   'six-variable weight expansion and Weyl alternant'],
        'scope':'finite reference table; not a positive all-n evaluator',
        'seconds':monotonic()-start,'details':stats},indent=2))
print(json.dumps({'result':'PASS','rows':len(rows),'seconds':monotonic()-start}),flush=True)
