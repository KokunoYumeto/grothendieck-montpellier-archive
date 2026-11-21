"""Exact finite supplement to HD-AST04--06; not a source-existence test."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from math import gcd
from datetime import datetime, timezone
import hashlib, json, time

start=time.perf_counter()
R=Path(__file__).resolve().parent
def prime_factors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out
def phi(n):
    a=n
    for p in prime_factors(n):a=a//p*(p-1)
    return a
def mobius(n):
    a=1
    for p in prime_factors(n):
        if n%(p*p)==0:return 0
        a=-a
    return a
def partitions(n,top=None):
    if n==0:
        yield ();return
    for v in range(min(n,top or n),1-1,-1):
        for tail in partitions(n-v,v):yield (v,)+tail
def spectrum(part):
    c=Counter(F(k,d) for d in part for k in range(d))
    c[F(0)]-=1
    return +c
def tensor(x,y):
    c=Counter()
    for a,m in x.items():
        for b,n in y.items():c[(a+b)%1]+=m*n
    return c
def swap(x):
    vals=list(x.elements());c=Counter(vals)
    for i,v in enumerate(vals):
        for w in vals[i+1:]:
            q=((v+w)/2)%1
            c[q]+=1;c[(q+F(1,2))%1]+=1
    return c
def rational_trace(c):
    by_order={}
    for x,m in c.items():
        d=x.denominator
        if d in by_order:assert by_order[d]==m
        else:by_order[d]=m
    for d,m in by_order.items():
        assert sum(v for x,v in c.items() if x.denominator==d)==phi(d)*m
    return sum(m*mobius(d) for d,m in by_order.items())
counts={'single_active_all_partitions':0,'selected_two_active_tensors':0,'selected_swaps':0,'generating_scalar_triples':0}
def check_spectrum(c,a):
    e=a*a
    assert sum(c.values())==e
    rational_trace(c)
    sq=Counter()
    for x,m in c.items():sq[(2*x)%1]+=m
    assert rational_trace(sq)>=-e//a
    for x,m in c.items():
        d=x.denominator
        assert phi(d)*m<=e
        if 6%d!=0:assert 4*a*m<=(a+1)*e
        if d%8==0:assert 4*m<=e
        for p in prime_factors(d):
            if p%2:assert (p-1)*m<=e

for n in range(15,21):
    a=n-1
    for part in partitions(n):
        c=Counter({x:m*a for x,m in spectrum(part).items()})
        check_spectrum(c,a)
        counts['single_active_all_partitions']+=1
for n in range(15,31):
    a=n-1
    patterns={(1,)*n,(2,)+(1,)*(n-2),(3,)+(1,)*(n-3)}
    for d in (2,3,4,5,7,8,11,13):
        if d<=n:patterns.add((d,)*(n//d)+(1,)*(n%d))
    spectra=[spectrum(p) for p in sorted(patterns)]
    for i,x in enumerate(spectra):
        check_spectrum(swap(x),a);counts['selected_swaps']+=1
        for y in spectra[i:]:
            check_spectrum(tensor(x,y),a)
            counts['selected_two_active_tensors']+=1

for M in (4,7,8,12,18,21,40,163):
    for x in range(M):
        for y in range(M):
            z=(-x-y)%M
            if gcd(gcd(x,y),M)!=1:continue
            ds=[M//gcd(v,M) for v in (x,y,z)]
            if 6%M:assert sum(6%d!=0 for d in ds)>=2
            for p in prime_factors(M):
                assert sum(v%p!=0 for v in (x,y,z))>=2
            if M%8==0:assert sum(d%8==0 for d in ds)>=2
            counts['generating_scalar_triples']+=1

non_eis=[]
for a in range(14,19):
    bound=F(12*a,19-a)
    assert a*a>bound
    non_eis.append({'n':a+1,'upper_degree':str(bound),'lower_degree':a*a})
dyadic=[]
for a in range(14,20):
    bound=F(12*a,20-a)
    assert a*a>bound
    dyadic.append({'n':a+1,'upper_degree':str(bound),'lower_degree':a*a})
prime_rows=[]
for p in (7,11,19,43,67,163):
    h=p-1
    assert 67*h-196>0 and 2*h-1>0
    for a in range(14,5*h):assert a*a>F(3*a*h,5*h-a)
    prime_rows.append({'p':p,'excluded_n_max':5*h,'remaining_n_min':5*h+1})
assert F(1,14)<=F(1,10)+F(3,5*196)
assert F(4*14+28,3*14)*196<=2*196+6
assert F(3*14+19,2*14)*196>2*196+6
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,
     'proof_sha256':hashlib.sha256((R/'alternating_standard_conductor_section.tex').read_bytes()).hexdigest(),
     'counts':counts,'non_eisenstein_endpoints':non_eis,'dyadic_endpoints':dyadic,
     'odd_prime_ranges':prime_rows,
     'strictness_witness':{'n':15,'t':2,'degree':196,'old_gates_satisfied':True,'new_gate_violated':True},
     'scope':'Exact finite spectra, cyclic quotient tuples and cutoff arithmetic supplement the universal proof. No source tuples or universal conductor theorem are verified computationally.'}
(R/'alternating_standard_conductor_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
