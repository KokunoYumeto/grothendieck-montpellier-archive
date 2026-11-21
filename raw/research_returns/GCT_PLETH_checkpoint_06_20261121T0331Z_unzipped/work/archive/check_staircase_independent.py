"""Independent monomial convolution for G022/G023 cycle trace polytopes."""
from pathlib import Path
from itertools import combinations
from math import comb,gcd
import hashlib,json,sys
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character,z

CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
NAMES=("5","41","32","311","221","2111","11111")
SIZES=tuple(120//z(cycle) for cycle in CLASSES)
CHARS=tuple(tuple(character(label,cycle) for cycle in CLASSES) for label in LABELS)


def trace_by_convolution(lengths,r):
    if any(gcd(r+1,ell)>1 for ell in lengths):
        return 0
    sign=1
    for ell in lengths:
        perm=[((r+1)*j)%ell for j in range(ell)]
        sign*=(-1)**sum(perm[i]>perm[j] for i in range(ell) for j in range(i+1,ell))
    if len(lengths)==1:
        return sign
    targets=[r*(5-ell)//2 for ell in lengths[:-1]]
    assert all(r*(5-ell)%2==0 for ell in lengths)
    shape=tuple(target+1 for target in targets)
    array=np.zeros(shape,dtype=np.int64)
    array[(0,)*len(targets)]=1
    edge_count=sum(gcd(a,b) for a,b in combinations(lengths,2))
    assert (r+1)**edge_count < 2**63
    for i,j in combinations(range(len(lengths)),2):
        g=gcd(lengths[i],lengths[j])
        for repetition in range(g):
            result=np.zeros_like(array)
            for u in range(r+1):
                increments=[0]*len(targets)
                increments[i]=(r-u)*lengths[j]//g
                if j<len(targets):
                    increments[j]=u*lengths[i]//g
                if any(value>target for value,target in zip(increments,targets)):
                    continue
                source=tuple(slice(0,size-value) for size,value in zip(shape,increments))
                dest=tuple(slice(value,size) for size,value in zip(shape,increments))
                result[dest]+=array[source]
            array=result
    return sign*int(array[tuple(targets)])


initial=[trace_by_convolution(CLASSES[0],r) for r in range(7)]
newton=[sum((-1)**(j-i)*comb(j,i)*initial[i] for i in range(j+1))
        for j in range(7)]
assert initial==[1,24,219,1136,4175,12216,30429]
assert newton==[1,23,172,550,850,630,180]


def closed(g,r):
    if g==0:
        return sum(value*comb(r,j) for j,value in enumerate(newton))
    if g==1:
        return 0 if r%2 else (r//2+1)**3+(r//2)**3
    if g==2:
        return 0 if r%2 else 3*(r//2)**2+3*(r//2)+1
    if g==3:
        q,s=divmod(r,3)
        return (q+1,-q,0)[s]
    if g==4:
        return (1,0,0,0,-1,0)[r%6]
    if g==5:
        return (1,0,-1,0)[r%4]
    return (1,-1,-1,1,0)[r%5]


sample_count=0
for g,lengths in enumerate(CLASSES):
    for r in range(10 if g==0 else 16):
        value=trace_by_convolution(lengths,r)
        assert value==closed(g,r),(lengths,r,value,closed(g,r))
        sample_count+=1
print("independent monomial convolutions",sample_count,flush=True)

target=json.loads((ROOT/"STAIRCASE_FIVE_CERTIFICATE.json").read_text())
checked=0
minimum=None
digest=hashlib.sha256()
zeros={}
for name,row in zip(NAMES,CHARS):
    zeros[name]=[]
    for s in range(60):
        for j in range(7):
            numerator=sum(size*ch*sum((-1)**(j-i)*comb(j,i)*closed(g,s+60*i)
                                     for i in range(j+1))
                          for g,(size,ch) in enumerate(zip(SIZES,row)))
            value,remainder=divmod(numerator,120)
            assert remainder==0 and value>=0
            if j:
                assert value>0
                minimum=value if minimum is None else min(minimum,value)
            elif value==0:
                zeros[name].append(s)
            assert value==target["table"][name][s][j],(name,s,j,value)
            digest.update((str(value)+"\n").encode())
            checked+=1
assert zeros==target["zero_parameters"]
assert minimum==107377819
receipt={
    "statement":"G022/G023 independent cycle-trace reconstruction","status":"PASS",
    "algorithm":"edge-by-edge monomial convolution, with the first c-1 exponents retained",
    "independent_trace_counts":sample_count,"identity_initial":initial,
    "identity_newton":newton,"fixed_Newton_constants_compared":checked,
    "minimum_positive_order_constant":minimum,"zero_parameters":zeros,
    "constant_stream_sha256":digest.hexdigest(),
    "character_table":"independent Murnaghan-Nakayama evaluation in S5",
    "int64_bound":"each intermediate coefficient <= (r+1)^number_of_parallel_edges < 2^63",
}
(HERE/"STAIRCASE_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
