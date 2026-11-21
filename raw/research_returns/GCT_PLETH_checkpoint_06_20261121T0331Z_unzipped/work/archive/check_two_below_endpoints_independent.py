"""T050 independent endpoint certificates: ambient Schur minus jets plus pair induction."""
from pathlib import Path
from itertools import combinations
from math import comb
import sys,json,hashlib
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character,z
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
WEIGHTS=[[120//z(c)*character(mu,c) for c in CLASSES] for mu in LABELS]
BRANCHES=((2,True,2,0),(2,False,1,2),(2,False,0,4),
          (3,True,2,0),(3,False,1,1),(3,False,0,3),
          (4,True,1,0),(4,False,0,2))
NAMES=("k2_bge2","k2_b1","k2_b0","k3_bge2","k3_b1","k3_b0","k4_bge1","k4_b0")
path=HERE.parent/"theta/outer5/TWO_BELOW_ENDPOINTS_SUMMARY.json"
target=json.loads(path.read_text())

def complete(cycles,limit=600):
    raw=[1]+[0]*limit
    for ell in cycles:
        for n in range(ell,limit+1):raw[n]+=raw[n-ell]
    return np.array([raw[n]-(raw[n-1] if n else 0) for n in range(limit+1)],dtype=object)

HS=[complete(cyc) for cyc in CLASSES]
def H(g,n):
    idx=np.asarray(n,dtype=np.int64)
    return np.where(idx<0,0,HS[g][np.maximum(0,idx)])

def perm(cycles):
    out=[];start=0
    for ell in cycles:
        out.extend(start+(i+1)%ell for i in range(ell));start+=ell
    return out

def subcycles(p,subset):
    remaining=set(subset);result=[]
    while remaining:
        x=min(remaining);q=p[x];length=1;remaining.remove(x)
        while q!=x:remaining.remove(q);q=p[q];length+=1
        result.append(length)
    return tuple(sorted(result,reverse=True))

PAIR=[]
for cyc in CLASSES:
    p=perm(cyc);terms=[]
    for pair in combinations(range(5),2):
        if set(p[i] for i in pair)!=set(pair):continue
        rest=set(range(5))-set(pair)
        pair_sign=1 if all(p[i]==i for i in pair) else -1
        rc=subcycles(p,rest);rs=(-1)**(3-len(rc))
        terms.append((pair_sign,rs,complete(rc)))
    PAIR.append(terms)

def traces(g,x,b,k):
    a=b+x;c=2*k-2
    ambient=(H(g,a+c)*(H(g,b+c)*H(g,c)-H(g,b+c+1)*H(g,c-1))
             -H(g,a+c+1)*(H(g,b+c-1)*H(g,c)-H(g,b+c+1)*H(g,c-2))
             +H(g,a+c+2)*(H(g,b+c-1)*H(g,c-1)-H(g,b+c)*H(g,c-2)))
    fiber=((H(g,a)-H(g,a-1))*(H(g,b)-H(g,b-1))
           -(H(g,a+1)-H(g,a))*(H(g,b-1)-H(g,b-2)))
    jet=CLASSES[g].count(1)*int(HS[g][k-1])*fiber
    pair=np.zeros(np.broadcast_shapes(x.shape,b.shape),dtype=object)
    for ps,rs,h in PAIR[g]:
        twist=np.ones(b.shape,dtype=object) if rs==1 else 1-2*(b%2)
        pair+=ps*twist*h[x]
    return ambient-jet+pair

verified=0;hashes={};minimum=None;maximum=0;zeros=[];largest_abs_trace=0
for name,(k,variable,bshift,xshift) in zip(NAMES,BRANCHES):
    X=np.arange(240,dtype=np.int64).reshape(-1,1)
    B=np.arange(300 if variable else 1,dtype=np.int64).reshape(1,-1)
    x=X+xshift;b=B+bshift
    arrays=[traces(g,x,b,k) for g in range(7)]
    largest_abs_trace=max(largest_abs_trace,max(int(max(map(abs,a.flat))) for a in arrays))
    for mu,weights in zip(LABELS,WEIGHTS):
        key=",".join(map(str,mu));record=target["branches"][name]["labels"][key]
        vals=sum(w*a for w,a in zip(weights,arrays))
        assert np.all(vals%120==0)
        vals//=120
        assert min(vals.flat)>=0
        blocks=vals.reshape(4,60,5 if variable else 1,60 if variable else 1).transpose(1,3,0,2)
        digest=hashlib.sha256();active=[]
        for i in range(4):
            for j in range(5 if variable else 1):
                v=np.diff(np.diff(blocks,n=i,axis=2),n=j,axis=3)[:,:,0,0]
                lo=int(min(v.flat));hi=int(max(v.flat))
                slot=f"{i},{j}"
                assert lo==record["minima"][slot] and hi==record["maxima"][slot]
                assert lo>=0 and hi<2**63
                if hi:
                    active.append([i,j])
                    if i+j:minimum=lo if minimum is None else min(minimum,lo)
                maximum=max(maximum,hi)
                if not(i or j):
                    found=[list(map(int,p)) for p in np.argwhere(v==0)]
                    assert found==record["zero_residues"]
                    for rx,rb in found:zeros.append(dict(label=key,k=k,x=rx+xshift,b=rb+bshift))
                digest.update(v.astype("<i8").tobytes(order="C"))
                verified+=v.size
        assert active==record["active_orders"]
        assert digest.hexdigest()==record["sha256"]
        hashes[name+"|"+key]=digest.hexdigest()
    print("PASS",name,"cumulative constants",verified,flush=True)
assert verified==1520400 and minimum==1957 and maximum==3227506200 and len(zeros)==18
receipt=dict(statement="T050 complete endpoint constants independently reconstructed",
 status="PASS",verified_entries=verified,matched_branch_label_hashes=len(hashes),
 minimum_positive_active_order=minimum,maximum_constant=maximum,
 largest_absolute_evaluated_trace=largest_abs_trace,
 arithmetic="Python unbounded integers throughout character and successive-difference computations; int64 used only after final exact bounds for hash serialization",
 method="ambient3x3 Jacobi-Trudi minus full point jets plus literal fixed-pair induction, standard traces from cycle denominators; successive quotient-index differences",
 zero_exceptions=zeros,hashes=hashes,input_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
(HERE/"TWO_BELOW_ENDPOINTS_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({k:v for k,v in receipt.items() if k not in ("hashes","zero_exceptions")},indent=2))
