"""G038: actual polarization blocks; SYT and Young-permutation characters."""
from pathlib import Path
from functools import lru_cache
from itertools import permutations
from fractions import Fraction
from collections import Counter
from math import factorial, comb
import sys, json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"root"))
import stable_second_row_positive as target


@lru_cache(None)
def partitions(n,cap=None):
    if n==0:return ((),)
    return tuple((i,)+tail for i in range(min(n,cap or n),0,-1)
                 for tail in partitions(n-i,i))


def compositions(n,d):
    if d==1:
        yield (n,)
        return
    for first in range(n+1):
        for tail in compositions(n-first,d-1):
            yield (first,)+tail


def rank(columns):
    pivots={}
    for column in columns:
        column={i:Fraction(v) for i,v in column.items() if v}
        while column:
            i=min(column)
            if i not in pivots:
                scale=column[i]
                pivots[i]={j:v/scale for j,v in column.items()}
                break
            scale=column[i]
            for j,v in pivots[i].items():
                column[j]=column.get(j,0)-scale*v
                if not column[j]:del column[j]
    return len(pivots)


def schur_dimension(shape,d):
    answer=Fraction(1)
    for i,width in enumerate(shape):
        for j in range(width):
            hook=width-j+sum(v>j for v in shape[i+1:])
            answer*=Fraction(d+j-i,hook)
    assert answer.denominator==1
    return int(answer)


def polarization_dimensions(d,D):
    kernel=cokernel=blocks=0
    for beta in compositions(D,d):
        support=[i for i,v in enumerate(beta) if v]
        columns=[]
        for i in support:
            if beta[i]>=2:columns.append({i:2})
            for j in support:
                if i<j:columns.append({i:1,j:1})
        r=rank(columns)
        kernel+=len(columns)-r
        cokernel+=len(support)-r
        blocks+=1
    return kernel,cokernel,blocks


@lru_cache(None)
def tableaux(shape):
    if not shape:return ((),)
    result=[]
    for i,width in enumerate(shape):
        if i+1<len(shape) and shape[i+1]==width:continue
        smaller=list(shape);smaller[i]-=1
        while smaller and smaller[-1]==0:smaller.pop()
        result.extend(T+((i+1,width),) for T in tableaux(tuple(smaller)))
    return tuple(result)


@lru_cache(None)
def fake(shape):
    m=sum(shape);out=[0]*(m*(m-1)//2+1)
    for T in tableaux(shape):
        degree=sum(m-j for j in range(1,m) if T[j][0]>T[j-1][0])
        out[degree]+=1
    return tuple(out)


@lru_cache(None)
def jacobi_trudi_terms(shape):
    length=len(shape);out=Counter()
    for p in permutations(range(length)):
        degrees=tuple(shape[i]-i+p[i] for i in range(length))
        if min(degrees)<0:continue
        sign=(-1)**sum(p[i]>p[j] for i in range(length) for j in range(i+1,length))
        out[tuple(sorted((d for d in degrees if d),reverse=True))]+=sign
    return tuple((shape,c) for shape,c in out.items() if c)


@lru_cache(None)
def permutation_character(block_sizes,cycles):
    """Fixed ordered set partitions, by assigning each literal cycle to a block."""
    if not cycles:return int(not any(block_sizes))
    length=cycles[0]
    return sum(permutation_character(block_sizes[:i]+(size-length,)+block_sizes[i+1:],
                                     cycles[1:])
               for i,size in enumerate(block_sizes) if size>=length)


@lru_cache(None)
def character(shape,cycles):
    return sum(c*permutation_character(alpha,cycles)
               for alpha,c in jacobi_trudi_terms(shape))


def centralizer(cycles):
    value=1
    for length,count in Counter(cycles).items():
        value*=length**count*factorial(count)
    return value


def tensor_multiplicity(nu,alpha,cycles,pair):
    result=Fraction()
    for rho in cycles:
        fixed=(comb(rho.count(1),2)+rho.count(2)) if pair else rho.count(1)-1
        result+=Fraction(character(nu,rho)*character(alpha,rho)*fixed,centralizer(rho))
    assert result.denominator==1 and result>=0
    return int(result)


def independent_free(nu):
    m=sum(nu);N=m*(m-1)//2;shapes=partitions(m);out=[0]*(N+3)
    for alpha in shapes:
        pair=tensor_multiplicity(nu,alpha,shapes,True)
        std=tensor_multiplicity(nu,alpha,shapes,False)
        f=fake(alpha)
        for j,v in enumerate(f):
            out[j+2]+=pair*v
            out[j+1]-=std*v
    d=1 if nu==(m-1,1) else 2 if nu==(m-2,1,1) else 0
    if d:
        out[d]+=1
        for i in range(2,m+1):out[d+i]-=1
    while len(out)>1 and not out[-1]:out.pop()
    assert all(v>=0 for v in out)
    return tuple(out),d


def main():
    counts=Counter()
    polarization=[]
    for d in range(2,7):
        for D in range(1,10):
            kernel,cokernel,blocks=polarization_dimensions(d,D)
            want=schur_dimension((D-2,2),d) if D>=4 else 0
            assert kernel==want,(d,D,kernel,want)
            assert cokernel==(d if D==1 else comb(d,2) if D==2 else 0)
            counts["actual_polarization_degree_cases"]+=1
            counts["exact_multidegree_blocks"]+=blocks
            polarization.append(dict(dimension=d,total_degree=D,kernel=kernel,cokernel=cokernel))
    for m in range(3,8):
        shapes=partitions(m)
        for nu in shapes:
            assert character(nu,(1,)*m)==len(tableaux(nu))
            norm=sum((Fraction(character(nu,rho)**2,centralizer(rho)) for rho in shapes),Fraction())
            assert norm==1
            got=independent_free(nu)
            assert got==target.free_numerator(nu),(nu,got,target.free_numerator(nu))
            counts["independent_free_numerators"]+=1
            counts["standard_tableaux"]+=len(tableaux(nu))
        # Complete row orthogonality also checks the permutation-character implementation.
        for i,nu in enumerate(shapes):
            for alpha in shapes[:i]:
                assert sum((Fraction(character(nu,rho)*character(alpha,rho),centralizer(rho))
                            for rho in shapes),Fraction())==0
                counts["character_row_orthogonality_checks"]+=1
    out={
        "statement":"G038 independent quadratic-polarization and free-numerator audit",
        "status":"PASS",
        "methods":[
            "literal multidegree polarization columns and exact rational elimination",
            "removable-corner standard tableaux and direct comajor exponents",
            "Young-permutation fixed ordered set partitions and Jacobi-Trudi",
            "unordered-pair fixed points and literal tensor character averages"
        ],
        **dict(counts),
        "polarization_cases":polarization,
        "root_cycle_MN_or_hook_quotient_code":"not imported",
        "target_import":"positive evaluator under verification only"
    }
    (HERE/"STABLE_SECOND_ROW_INDEPENDENT_RECEIPT.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items() if k!="polarization_cases"},indent=2))


if __name__=="__main__":main()
