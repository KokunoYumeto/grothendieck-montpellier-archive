"""G032 independent exhaustive reconstruction from normal monomials and Weyl shifts.

No root Python module is imported. Arithmetic in trace products, character sums,
and successive finite differences uses Python unbounded integers (object arrays).
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations, product
from math import factorial
from pathlib import Path
import hashlib
import json
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "root"
CLASSES = ((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
PARTITIONS = ((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
LABELS = tuple("".join(map(str,p)) for p in PARTITIONS)
DELTA = (2,1,0)
PERMS = tuple(permutations(range(3)))
EPS = {p: (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in PERMS}
NORMALS = ((),(1,),(1,1),(2,),(1,1,1),(2,1),(3,))

def class_size(cycles):
    z = 1
    for length,count in Counter(cycles).items():
        z *= length**count * factorial(count)
    return factorial(5)//z

SIZES = tuple(class_size(c) for c in CLASSES)

def frobenius_characters(cycles):
    polynomial = {(0,)*5:1}
    for length in cycles:
        following = defaultdict(int)
        for powers,value in polynomial.items():
            for slot in range(5):
                new = list(powers);new[slot] += length
                following[tuple(new)] += value
        polynomial = following
    delta = (4,3,2,1,0)
    answer = []
    for shape in PARTITIONS:
        lam = shape+(0,)*(5-len(shape));value = 0
        for p in permutations(range(5)):
            sign = (-1)**sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))
            powers = tuple(lam[i]+delta[i]-delta[p[i]] for i in range(5))
            value += sign*polynomial.get(powers,0)
        answer.append(value)
    return tuple(answer)

CHARS = tuple(zip(*(frobenius_characters(c) for c in CLASSES)))
assert all(sum(SIZES[g]*CHARS[i][g]*CHARS[j][g] for g in range(7))
           == (120 if i==j else 0) for i in range(7) for j in range(7))

def complete(cycles, indices):
    """Closed traces for every standard module of complement size 2..5."""
    cycles = tuple(sorted(cycles,reverse=True))
    n = np.maximum(np.asarray(indices,dtype=np.int64),0)
    if cycles==(1,1): ans=np.ones_like(n)
    elif cycles==(2,): ans=np.where(n%2==0,1,-1)
    elif cycles==(1,1,1): ans=n+1
    elif cycles==(2,1): ans=(n%2==0).astype(np.int64)
    elif cycles==(3,): ans=np.asarray((1,-1,0),dtype=np.int64)[n%3]
    elif cycles==(1,1,1,1): ans=(n+1)*(n+2)//2
    elif cycles==(2,1,1): ans=n//2+1
    elif cycles==(2,2): ans=np.where(n%2==0,1,-1)*(n//2+1)
    elif cycles==(3,1): ans=(n%3==0).astype(np.int64)
    elif cycles==(4,): ans=np.asarray((1,-1,0,0),dtype=np.int64)[n%4]
    elif cycles==(1,1,1,1,1): ans=(n+1)*(n+2)*(n+3)//6
    elif cycles==(2,1,1,1): ans=(n//2+1)*((n+1)//2+1)
    elif cycles==(2,2,1): ans=np.where(n%2==0,n//2+1,0)
    elif cycles==(3,1,1): ans=n//3+1
    elif cycles==(3,2): ans=np.asarray((1,-1,1,0,0,0),dtype=np.int64)[n%6]
    elif cycles==(4,1): ans=(n%4==0).astype(np.int64)
    elif cycles==(5,): ans=np.asarray((1,-1,0,0,0),dtype=np.int64)[n%5]
    else: raise AssertionError(cycles)
    # Only the closed formulas above use bounded integers: indices in this
    # exhaustive run are at most 550, so their largest intermediate is <553^3.
    assert int(np.max(n)) < 10000
    return np.where(np.asarray(indices)>=0,ans,0).astype(object)

@lru_cache(None)
def normal_polynomial(cycles):
    polynomial={(0,0,0):1}
    for length in cycles:
        factor=[]
        for degree in range(3):
            for i in range(degree+1):
                for j in range(degree-i+1):
                    factor.append((length*i,length*j,length*(degree-i-j)))
        following=defaultdict(int)
        for old,value in polynomial.items():
            for monomial in factor:
                following[tuple(old[i]+monomial[i] for i in range(3))]+=value
        polynomial=dict(following)
    return polynomial

@lru_cache(None)
def tableau_polynomial(shape):
    cells=[(r,c) for r,row in enumerate(shape) for c in range(row)]
    entries={};answer=defaultdict(int)
    def visit(index,weight):
        if index==len(cells):
            answer[weight]+=1;return
        r,c=cells[index]
        lower=max(entries.get((r,c-1),1),entries.get((r-1,c),0)+1)
        for letter in range(lower,4):
            entries[r,c]=letter
            nxt=list(weight);nxt[letter-1]+=1
            visit(index+1,tuple(nxt))
        entries.pop((r,c),None)
    visit(0,(0,0,0))
    return dict(answer)

@lru_cache(None)
def compressed_terms(class_index,c):
    cycles=CLASSES[class_index]
    answer=defaultdict(int)
    # Literal stable subsets are unions of the actual cycles. Equal-length
    # cycles remain distinct here, which recovers their exact multiplicities.
    for choices in product((False,True),repeat=len(cycles)):
        selected=tuple(cycles[i] for i in range(len(cycles)) if choices[i])
        if sum(selected)>3:continue
        complement=tuple(cycles[i] for i in range(len(cycles)) if not choices[i])
        orientation=(-1)**len(selected)
        for monomial,value in normal_polynomial(selected).items():
            for p in PERMS:
                shifts=tuple(DELTA[i]-DELTA[p[i]]-monomial[i] for i in range(3))
                last=int(complete(complement,c+shifts[2]))
                if last:
                    answer[complement,shifts[0],shifts[1]]+=orientation*EPS[p]*value*last
    return tuple((key,value) for key,value in sorted(answer.items()) if value)

def independent_grid(xs,bs,c):
    xs=tuple(xs);bs=tuple(bs)
    X=np.asarray(xs,dtype=np.int64)[:,None]
    B=np.asarray(bs,dtype=np.int64)[None,:]
    traces=[]
    for g in range(7):
        total=np.zeros((len(xs),len(bs)),dtype=object)
        first={};second={}
        for (cycles,s0,s1),coefficient in compressed_terms(g,c):
            key=(cycles,s0)
            if key not in first:first[key]=complete(cycles,X+B+c+s0)
            key2=(cycles,s1)
            if key2 not in second:second[key2]=complete(cycles,B+c+s1)
            total += coefficient*first[key]*second[key2]
        traces.append(total)
    values=[]
    for row in CHARS:
        numerator=np.zeros_like(traces[0])
        for size,chi,trace in zip(SIZES,row,traces):
            numerator += size*chi*trace
        assert not np.any(numerator%120)
        values.append(numerator//120)
    return np.asarray(values,dtype=object),max(int(np.max(np.abs(t))) for t in traces)

def successive_differences(array,axis):
    levels=[];current=array
    for degree in range(array.shape[axis]):
        levels.append(np.take(current,0,axis=axis))
        if degree+1<array.shape[axis]:
            current=np.diff(current,axis=axis)
    return np.stack(levels,axis=axis)

def check_stats(raw,axes,expected,bulk):
    input_max=int(np.max(np.abs(raw)))
    assert input_max==expected["input_max"],(input_max,expected["input_max"])
    table=raw
    for axis in axes:table=successive_differences(table,axis)
    assert int(np.min(table))>=0
    assert table.size==expected["count"]
    hashes={}
    for i,label in enumerate(LABELS):
        values=table[i]
        low=int(values.min());high=int(values.max())
        assert 0<=low<=high<2**63
        digest=hashlib.sha256(np.ascontiguousarray(values,dtype="<i8").tobytes()).hexdigest()
        assert dict(min=low,max=high,sha256=digest)==expected["labels"][label],(label,low,high,digest)
        hashes[label]=digest
    if bulk:
        active=[(i,j) for i in range(4) for j in range(5) if np.any(table[:,:,:,i,j])]
        assert [list(v) for v in active]==expected["active_orders"]
        minima={f"{i},{j}":int(table[:,:,:,i,j].min()) for i,j in active}
        zeros={label:[[int(x),int(b)] for x,b in np.argwhere(table[i,:,:,0,0]==0)]
               for i,label in enumerate(LABELS)}
        assert minima==expected["minimum_by_order"]
        assert zeros==expected["zero_pairs"]
    else:
        active=list(range(4))
        minima={str(i):int(table[:,:,i].min()) for i in active}
        zeros={label:[int(x) for x in np.flatnonzero(table[i,:,0]==0)] for i,label in enumerate(LABELS)}
        assert minima==expected["minimum_by_order"]
        assert zeros==expected["zero_residues"]
    return {"count":int(table.size),"hashes":hashes,"minimum_by_order":minima,
            "zeros":zeros,"max":int(table.max())}

def main():
    start=time.monotonic()
    source=ROOT/"THIRD_POWER_FIXED_TWIST_CERTIFICATE.json"
    expected=json.loads(source.read_text())
    normal_checks=0
    for cycles in NORMALS:
        key=",".join(map(str,cycles));expansion=defaultdict(int)
        for shape,value in expected["normal_schur"][key]:
            for monomial,coefficient in tableau_polynomial(tuple(shape)).items():
                expansion[monomial]+=value*coefficient
        expansion={m:v for m,v in expansion.items() if v}
        assert expansion==normal_polynomial(cycles),cycles
        normal_checks+=1
    answer={"statement":"G032 independent exhaustive fixed-constant reconstruction",
            "status":"PASS","method":"unexpanded truncated normal monomials; six Weyl shifts; explicit closed complete traces; fresh Frobenius character rows; Python-integer successive differences",
            "input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "normal_tableau_expansion_checks":normal_checks,"character_rows":CHARS,
            "twists":{},"all_trace_arithmetic":"unbounded Python integers"}
    total=0;maximum_trace=0
    for c in range(3):
        raw,trace_max=independent_grid(range(240),range(8,308),c)
        maximum_trace=max(maximum_trace,trace_max)
        shaped=raw.reshape(7,4,60,5,60).transpose(0,2,4,1,3)
        data={"bulk_b8":check_stats(shaped,(3,4),expected["twists"][str(c)]["bulk_b8"],True),"boundaries":{}}
        total+=data["bulk_b8"]["count"]
        print("twist",c,"bulk PASS",504000,"constants",flush=True)
        for b in range(8):
            shift=max(0,15-3*c-2*b)
            reference=expected["twists"][str(c)]["boundaries"][str(b)]
            assert reference["x_shift"]==shift
            raw,trace_max=independent_grid(range(shift,shift+240),(b,),c)
            maximum_trace=max(maximum_trace,trace_max)
            shaped=raw[:,:,0].reshape(7,4,60).transpose(0,2,1)
            result=check_stats(shaped,(2,),reference,False)
            result["x_shift"]=shift;data["boundaries"][str(b)]=result
            total+=result["count"]
        answer["twists"][str(c)]=data
        print("twist",c,"all eight boundaries PASS",13440,"constants",flush=True)
    assert total==expected["total_constants"]==1552320
    answer.update(total_constants=total,maximum_absolute_trace=maximum_trace,
                  elapsed_seconds=time.monotonic()-start,
                  compressed_term_counts={str(c):[len(compressed_terms(g,c)) for g in range(7)] for c in range(3)})
    target=HERE/"THIRD_POWER_FIXED_TWIST_INDEPENDENT_RECEIPT.json"
    target.write_text(json.dumps(answer,indent=2)+"\n")
    print("PASS",total,"constants;",normal_checks,"normal identities;",target.name,flush=True)

if __name__=="__main__":
    main()

