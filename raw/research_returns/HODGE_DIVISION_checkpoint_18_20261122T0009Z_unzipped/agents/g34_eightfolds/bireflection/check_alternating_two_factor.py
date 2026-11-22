#!/usr/bin/env python3
"""Exact supplements to D-ATT04--06; no tuple enumeration is claimed."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from math import lcm
import datetime,hashlib,json,re,time

t0=time.perf_counter();base=Path(__file__).resolve().parent
proof=base/'alternating_two_factor_section.tex';tex=proof.read_text()
assert tex.count(r'\[')==tex.count(r'\]')
assert re.findall(r'\\tag\{([^}]+)\}',tex)==['ATF.'+str(i) for i in range(1,13)]
def parts(n,m=1):
    if n==0:yield ()
    for k in range(m,n+1):
        for tail in parts(n-k,k):yield (k,)+tail
def spectra(p):
    L=lcm(*p);letter=Counter(j*(L//r) for r in p for j in range(r))
    u=list(letter.elements());u.remove(0)
    ex=Counter((x+y)%L for i,x in enumerate(u) for y in u[i+1:])
    up=Counter((x+y)%L for i,x in enumerate(u) for y in u[i:]);up.subtract(letter)
    assert min(up.values())>=0
    return L,+up,ex
def swap(S,L):
    ans=Counter();items=list(S.items())
    for i,(x,v) in enumerate(items):
        ans[2*x]+=v
        for j,(y,w) in enumerate(items[i:],i):
            mult=v*(v-1)//2 if i==j else v*w
            ans[(x+y)%(2*L)]+=mult;ans[(x+y+L)%(2*L)]+=mult
    return +ans

rows=0;swaprows=0;formulas=0
for n in range(15,27):
    A=F(n-5,2);B=F(n,4)
    for p in parts(n):
        L,up,ex=spectra(p);k=n-len(p)
        for S in (up,ex):
            a=sum(S.values());nu=a-max(S.values())
            if k:assert nu>=A*k+B
            if n<=20:
                Tw=swap(S,L);assert sum(Tw.values())==a*a
                pair=Counter()
                for x,v in S.items():
                    for y,w in S.items():pair[(x+y)%L]+=v*w
                diag=Counter({2*x:v for x,v in S.items()})
                for z in range(2*L):
                    twice=pair[z%L]+diag[z]-diag[(z+L)%(2*L)]
                    assert twice%2==0 and Tw[z]==twice//2
                    assert 2*Tw[z]<=a*(a-nu)+a
                    formulas+=1
                swaprows+=1
        rows+=1

arithmetic=[]
for n in range(15,1001):
    A=F(n-5,2);B=F(n,4)
    for kind in ('UP','EX'):
        a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
        d0=n-3 if kind=='UP' else n-2;b=1 if kind=='UP' else (n-1)//2
        assert a*(8*d0-2)>6
        assert a*(9*d0-F(b+1,2))>6
        assert B-1<=a
        expected=2*a+(5 if kind=='UP' else 3)
        assert A*(2*n-2)+12*B==expected
        excess=F(a,2)*(expected-2)-a*a
        assert excess==(F(3,2)*a if kind=='UP' else F(a,2)) and excess>6
        if n in (15,39,40,100,1000):arithmetic.append({'kind':kind,'n':n,'a':a,'final_excess':str(excess)})

# Actual imprimitive permutation index on two n-letter blocks: a swap
# with cycle product h has precisely the cycles of h, with lengths doubled.
index_cases=0
for n in range(3,15):
    for p in parts(n):
        perm=[];off=0
        for l in p:
            perm.extend([off+(j+1)%l for j in range(l)]);off+=l
        sw=list(range(n,2*n))+perm
        seen=set();cycles=0
        for i in range(2*n):
            if i in seen:continue
            cycles+=1;j=i
            while j not in seen:seen.add(j);j=sw[j]
        assert 2*n-cycles==n+(n-len(p));index_cases+=1
out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-t0,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'all_cycle_types_n15_26':rows,'weighted_swap_types_n15_20':swaprows,
 'exact_eigenspace_formula_checks':formulas,'actual_imprimitive_index_cases':index_cases,
 'finite_arithmetic_cases':2*(1000-15+1),'arithmetic_examples':arithmetic,
 'scope':'Exact finite common-index inequalities, weighted-swap formulas, actual imprimitive permutation indices and arithmetic. The universal source/generation and Riemann-Hurwitz argument is proved in TeX.'}
(base/'alternating_two_factor_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
