"""G027: literal signed restriction terms, Weyl extraction and balanced-cycle checks."""
from pathlib import Path
from itertools import product,permutations
from functools import lru_cache
from collections import defaultdict
from fractions import Fraction
from math import factorial
import hashlib,json,sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import partitions,character,z,sign
sys.path.insert(0,str(HERE.parent/"root"))
from five_row_cycle_trace import cycle_trace

@lru_cache(None)
def compositions(n,r):
    if r==0:return ((),) if n==0 else ()
    return tuple((a,)+rest for a in range(n+1) for rest in compositions(n-a,r-1))

@lru_cache(None)
def standard_h(cycles,n):
    if n<0:return 0
    raw=[1]+[0]*n
    for ell in cycles:
        for j in range(ell,n+1):raw[j]+=raw[j-ell]
    return raw[n]-(raw[n-1] if n else 0)

@lru_cache(None)
def truncated_cycle_product(selected,k,r):
    poly={(0,)*r:1}
    for ell in selected:
        factor=[tuple(ell*q for q in comp) for t in range(k) for comp in compositions(t,r)]
        out=defaultdict(int)
        for old,coefficient in poly.items():
            for term in factor:out[tuple(a+b for a,b in zip(old,term))]+=coefficient
        poly=dict(out)
    return tuple(poly.items())

@lru_cache(None)
def monomial_term(selected,remaining,k,beta):
    if any(q<0 for q in beta):return 0
    answer=0
    for exponent,coefficient in truncated_cycle_product(selected,k,len(beta)):
        value=coefficient
        for q,e in zip(beta,exponent):
            value*=standard_h(remaining,q-e)
            if not value:break
        answer+=value
    return answer

@lru_cache(None)
def schur_term(selected,remaining,k,alpha):
    r=len(alpha);delta=tuple(range(r-1,-1,-1));answer=0
    for perm in permutations(range(r)):
        beta=tuple(alpha[i]+delta[i]-delta[perm[i]] for i in range(r))
        answer+=sign(perm)*monomial_term(selected,remaining,k,beta)
    return answer

@lru_cache(None)
def arrangement_trace(m,k,alpha,cycles):
    if not k:
        return schur_term((),cycles,1,alpha)
    assert sum(alpha)>=m*k
    grouped=defaultdict(int)
    for mask in range(1<<len(cycles)):
        selected=tuple(cycles[j] for j in range(len(cycles)) if mask>>j&1)
        if sum(selected)>m-2:continue
        remaining=tuple(cycles[j] for j in range(len(cycles)) if not(mask>>j&1))
        # Euler sign times the actual orientation character.
        grouped[(selected,remaining)]+=(-1)**len(selected)
    return sum(coefficient*schur_term(selected,remaining,k,alpha)
               for (selected,remaining),coefficient in grouped.items())

def actual_cycle_index(lam,n,cycles):
    poly={():Fraction(1)}
    for ell in cycles:
        out=defaultdict(Fraction)
        for old,value in poly.items():
            for part in partitions(n):
                out[tuple(sorted(old+tuple(ell*q for q in part),reverse=True))]+=value/z(part)
        poly=out
    value=sum(coefficient*character(lam,cycle) for cycle,coefficient in poly.items())
    assert value.denominator==1
    return int(value)

totals={};rows=[];mn_checks=0;hashers={m:hashlib.sha256() for m in (3,4,5)}
for m,maxn in ((3,8),(4,6),(5,4)):
    cases=traces=multiplicities=positive=0;maxk=maxN=0
    allcycles=partitions(m);outer=partitions(m)
    for n in range(maxn+1):
        for lam in partitions(m*n):
            if len(lam)>m:continue
            padded=lam+(0,)*(m-len(lam))
            alpha=tuple(padded[1]-padded[m-1-i] for i in range(m-2))
            k=max(0,padded[1]-n)
            values=[]
            for cyc in allcycles:
                expected=cycle_trace(lam,n,cyc)
                got=(-1)**((m-len(cyc))*padded[1])*arrangement_trace(m,k,alpha,cyc)
                assert got==expected,(m,n,lam,alpha,k,cyc,got,expected)
                if n<=2:
                    independent=actual_cycle_index(lam,n,cyc)
                    assert got==independent
                    mn_checks+=1
                values.append(got);traces+=1
            for mu in outer:
                value=sum(Fraction(character(mu,cyc)*tr,z(cyc)) for cyc,tr in zip(allcycles,values))
                assert value.denominator==1 and value>=0
                multiplicities+=1
            cases+=1;positive+=int(k>0);maxk=max(maxk,k);maxN=max(maxN,sum(alpha))
            hashers[m].update(json.dumps([n,lam,k,alpha,values],separators=(",",":")).encode()+b"\n")
    totals[m]=dict(partition_cases=cases,positive_k_cases=positive,class_trace_checks=traces,
                   multiplicity_checks=multiplicities,max_inner_degree=maxn,max_k=maxk,max_alpha_size=maxN,
                   sha256=hashers[m].hexdigest())
    print("m",m,totals[m],flush=True)

receipt=dict(statement="G027 independent exact signed-restriction character checks",status="PASS",
    by_outer_degree=totals,literal_cycle_index_MN_checks=mn_checks,
    method="FA17 selected-cycle truncations, exact orientation/Euler signs, complementary standard trace, Weyl-denominator extraction; comparison with balanced cycle engine and small literal MN cycle index",
    all_class_checks=sum(row["class_trace_checks"] for row in totals.values()),
    all_partition_cases=sum(row["partition_cases"] for row in totals.values()))
(HERE/"FAT_ARRANGEMENT_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({k:v for k,v in receipt.items() if k!="by_outer_degree"},indent=2),flush=True)

