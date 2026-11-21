"""G025: independent Jacobi--Trudi base traces and all minimal seeds.

Single cycles use a literal small integer determinant. The 22 and 32
base traces use Jacobi--Trudi over F61 and finite interpolation, avoiding
the signed residue and Laurent formulas in the root implementation.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import defaultdict
from fractions import Fraction
from math import comb
import json,sys,hashlib

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character,partitions,z

CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
PRIME=61
assert all(PRIME%d for d in range(2,8))
counts={"single_cycle_determinants":0,"two_cycle_interpolations":0}


def trim(lam):
    return tuple(v for v in lam if v)


def determinant(matrix,modulus=None):
    a=[list(map(Fraction,row)) for row in matrix] if modulus is None else [row[:] for row in matrix]
    out=1
    for i in range(len(a)):
        pivot=next((j for j in range(i,len(a)) if a[j][i]),None)
        if pivot is None:return 0
        if pivot!=i:
            a[i],a[pivot]=a[pivot],a[i]
            out=-out
        p=a[i][i]
        out*=p
        if modulus:
            out%=modulus
            inv=pow(p,-1,modulus)
        else:
            inv=1/p
        for j in range(i+1,len(a)):
            mult=a[j][i]*inv
            for q in range(i+1,len(a)):
                a[j][q]-=mult*a[i][q]
                if modulus:a[j][q]%=modulus
            a[j][i]=0
    if modulus:return out%modulus
    assert out.denominator==1
    return int(out)


@lru_cache(None)
def single(lam,length):
    counts["single_cycle_determinants"]+=1
    padded=lam+(0,)*(length-len(lam))
    H=lambda j:int(j>=0 and j%length==0)
    result=determinant([[H(padded[i]-i+j) for j in range(length)]
                        for i in range(length)])
    assert result in (-1,0,1)
    return result


def coefficient_by_interpolation(values,index):
    current=values[:]
    basis=[1]
    answer=0
    for j in range(len(values)):
        if index<len(basis):
            answer+=current[0]*basis[index]
        current=[(b-a)%PRIME for a,b in zip(current,current[1:])]
        new=[0]*(len(basis)+1)
        inverse=pow(j+1,-1,PRIME)
        for power,value in enumerate(basis):
            new[power]=(new[power]-j*value*inverse)%PRIME
            new[power+1]=(new[power+1]+value*inverse)%PRIME
        basis=new
    return answer%PRIME


@lru_cache(None)
def two_cycles(lam,n,cycle):
    counts["two_cycle_interpolations"]+=1
    length=sum(cycle)
    padded=lam+(0,)*(length-len(lam))
    degree=sum(lam)//cycle[0]
    assert degree+1<PRIME
    largest=max(padded[i]-i+length-1 for i in range(length))
    values=[]
    for parameter in range(degree+1):
        denominator=[1]
        for ell,weight in zip(cycle,(parameter,1)):
            new=[0]*(len(denominator)+ell)
            for i,value in enumerate(denominator):
                new[i]=(new[i]+value)%PRIME
                new[i+ell]=(new[i+ell]-weight*value)%PRIME
            denominator=new
        complete=[1]
        for j in range(1,largest+1):
            complete.append(-sum(denominator[q]*complete[j-q]
                                  for q in range(1,min(j,len(denominator)-1)+1))%PRIME)
        H=lambda j:complete[j] if j>=0 else 0
        matrix=[[H(padded[i]-i+j) for j in range(length)] for i in range(length)]
        values.append(determinant(matrix,PRIME))
    residue=coefficient_by_interpolation(values,n)
    answer=residue if residue<=PRIME//2 else residue-PRIME
    # The proved alternant bounds make signed reconstruction exact.
    bound=n+1 if cycle==(2,2) else 10
    assert 2*bound<PRIME and abs(answer)<=bound
    return answer


@lru_cache(None)
def strips(lam,n,rank):
    padded=lam+(0,)*(rank+1-len(lam))
    required=sum(lam)-n
    lower=padded[1:]
    upper=padded[:-1]
    results=[]
    def visit(i,left,chosen):
        if i==rank:
            if left==0:results.append(trim(chosen))
            return
        lo=max(lower[i],left-sum(upper[i+1:]))
        hi=min(upper[i],left-sum(lower[i+1:]))
        for value in range(lo,hi+1):
            visit(i+1,left-value,chosen+(value,))
    visit(0,required,())
    return tuple(results)


@lru_cache(None)
def trace(lam,n,cycle):
    lam=trim(lam)
    if sum(lam)!=n*sum(cycle) or len(lam)>sum(cycle):return 0
    if len(cycle)==1:return single(lam,cycle[0])
    if cycle[-1]==1:
        return sum(trace(beta,n,cycle[:-1]) for beta in strips(lam,n,sum(cycle)-1))
    return two_cycles(lam,n,cycle)


def compositions_at_most(bound,length):
    if length==0:
        yield ()
    else:
        for first in range(bound+1):
            for rest in compositions_at_most(bound-first,length-1):
                yield (first,)+rest


target=json.loads((ROOT/"FIVE_ROW_GAP2_SEEDS.json").read_text())["seeds"]
by_key={(tuple(row["parity"]),tuple(row["increment"])):row for row in target}
all_u=list(compositions_at_most(4,4))
assert len(all_u)==70
seeds=[]
for parity in product(range(2),repeat=4):
    base=tuple(2+p for p in parity)
    for u in all_u:
        if sum((i+1)*(base[i]+2*u[i]) for i in range(4))%5:continue
        smaller=[v for v in product(*(range(a+1) for a in u)) if v!=u]
        if any(sum((i+1)*(base[i]+2*v[i]) for i in range(4))%5==0 for v in smaller):
            continue
        gaps=tuple(base[i]+2*u[i] for i in range(4))
        lam=tuple(sum(gaps[i:]) for i in range(4))
        n=sum(lam)//5
        values=tuple(trace(lam,n,cycle) for cycle in CLASSES)
        mult=[]
        for mu in LABELS:
            numerator=sum((120//z(cycle))*character(mu,cycle)*value
                          for cycle,value in zip(CLASSES,values))
            assert numerator%120==0
            mult.append(numerator//120)
        row=by_key[parity,u]
        assert tuple(row["gaps"])==gaps
        assert tuple(row["traces"])==values,(parity,u,values,row["traces"])
        assert row["multiplicities"]==mult and min(mult)>=2
        seeds.append((parity,u))
assert len(seeds)==len(set(seeds))==76 and set(seeds)==set(by_key)


def actual_symmetric(m,n,lam):
    total=defaultdict(Fraction)
    for alpha in partitions(m):
        terms={():Fraction(1,z(alpha))}
        for ell in alpha:
            new=defaultdict(Fraction)
            for old,coefficient in terms.items():
                for beta in partitions(n):
                    cycle=tuple(sorted(old+tuple(ell*b for b in beta),reverse=True))
                    new[cycle]+=coefficient/z(beta)
            terms=new
        for cycle,coefficient in terms.items():total[cycle]+=coefficient
    return sum(coefficient*character(lam,cycle) for cycle,coefficient in total.items())


source=actual_symmetric(4,5,(8,6,4,2))
target_n4=actual_symmetric(5,4,(8,6,4,2))
assert (source,target_n4)==(1,3)
receipt={
    "statement":"G025 independent complete minimal-seed reconstruction","status":"PASS",
    "minimal_seeds":76,"class_traces_compared":76*7,
    "irreducible_multiplicities_compared":76*7,
    "minimum_multiplicity":2,"largest_inner_degree":12,
    "method":"interlacing strips; literal integer single-cycle JT determinants; two-cycle JT interpolation over F61",
    "finite_field_exactness":"degree<61; 22 trace bound n+1<=13, 32 trace bound10; centered residues unique",
    "base_computations":counts,"n4_source_multiplicity":int(source),
    "n4_target_multiplicity":int(target_n4),
    "compared_seed_file_sha256":hashlib.sha256((ROOT/"FIVE_ROW_GAP2_SEEDS.json").read_bytes()).hexdigest(),
}
(HERE/"GAP2_SEEDS_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
