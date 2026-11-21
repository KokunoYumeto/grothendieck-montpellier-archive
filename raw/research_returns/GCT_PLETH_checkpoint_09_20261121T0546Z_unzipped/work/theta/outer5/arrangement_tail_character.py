"""T049: rank-five characters from literal bounded-table counts.

The computational path is the factored tail product, followed by the
six Weyl shifts and eight exterior shifts.  It does not enumerate the
signed subset complex and does not call a plethysm library.
"""
from functools import lru_cache
from itertools import permutations, product
from math import factorial
import argparse
import json
import numpy as np

CLASSES = ((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES = (1,10,15,20,20,30,24)
LABELS = ((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
CHAR = (
    (1,1,1,1,1,1,1),
    (4,2,0,1,-1,0,-1),
    (5,1,1,-1,1,-1,0),
    (6,0,-2,0,0,0,1),
    (5,-1,1,-1,-1,1,0),
    (4,-2,0,1,1,0,-1),
    (1,-1,1,1,-1,-1,1),
)
RHO = (2,1,0)


def permutation_sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


WEYL_SHIFTS = tuple((tuple(RHO[p[i]] for i in range(3)),permutation_sign(p))
                    for p in permutations(range(3)))


@lru_cache(None)
def table_polynomial(cycles, k, cap):
    """Coefficients of the product of tails in a bounded exponent box.

Each step first convolves with all nonnegative triples of multiples
of the cycle length, using three exact prefix sums.  It then removes
the triples of total row degree <k.  All array entries are Python
integers; there is no fixed-width overflow assumption.
"""
    assert k>=0 and cap>=0
    shape=(cap+1,)*3
    arr=np.zeros(shape,dtype=object);arr[0,0,0]=1
    for c in cycles:
        full=arr.copy()
        for axis in range(3):
            for j in range(c,cap+1):
                dst=[slice(None)]*3;src=[slice(None)]*3
                dst[axis]=j;src[axis]=j-c
                full[tuple(dst)]+=full[tuple(src)]
        for u in range(min(k-1,cap//c)+1):
            for v in range(min(k-1-u,cap//c)+1):
                for w in range(min(k-1-u-v,cap//c)+1):
                    du,dv,dw=c*u,c*v,c*w
                    full[du:,dv:,dw:]-=arr[:cap+1-du,:cap+1-dv,:cap+1-dw]
        assert all(v>=0 for v in full.flat)
        arr=full
    arr.flags.writeable=False
    return arr


def trace_alpha(cycles,k,alpha,cap=None):
    alpha=tuple(alpha)
    assert len(alpha)==3 and alpha[0]>=alpha[1]>=alpha[2]>=0
    target=tuple(alpha[i]+RHO[i] for i in range(3))
    cap=max(target) if cap is None else cap
    assert cap>=max(target)
    poly=table_polynomial(tuple(cycles),k,cap)
    total=0
    for wrho,sgn in WEYL_SHIFTS:
        for delta in product((0,1),repeat=3):
            beta=tuple(target[i]-wrho[i]-delta[i] for i in range(3))
            if min(beta)>=0:
                total+=sgn*(-1)**sum(delta)*int(poly[beta])
    return total


def balanced_traces(n,lam,cap=None):
    lam=tuple(lam)+(0,)*(5-len(lam))
    if len(lam)!=5 or tuple(sorted(lam,reverse=True))!=lam or min(lam)<0 or sum(lam)!=5*n:
        raise ValueError('output must be a partition of 5n with at most five rows')
    k=max(0,lam[1]-n)
    alpha=(lam[1]-lam[4],lam[1]-lam[3],lam[1]-lam[2])
    return tuple((-1)**((5-len(c))*lam[1])*trace_alpha(c,k,alpha,cap)
                 for c in CLASSES)


def multiplicities(n,lam,cap=None):
    tr=balanced_traces(n,lam,cap)
    ans=[]
    for row in CHAR:
        value=sum(size*chi*t for size,chi,t in zip(SIZES,row,tr))
        assert value%120==0 and value>=0,(n,lam,row,tr,value)
        ans.append(value//120)
    return tuple(ans)


def table_polytope(cycles,k,beta):
    """Literal matrices for the bounded-table term DP.11."""
    v=len(cycles);nvar=3*v
    Aeq=[]
    for a in range(3):
        row=[0]*nvar
        for j,c in enumerate(cycles):row[3*j+a]=c
        Aeq.append(row)
    Aub=[];bub=[]
    for i in range(nvar):
        row=[0]*nvar;row[i]=-1;Aub.append(row);bub.append(0)
    for j in range(v):
        row=[0]*nvar
        for a in range(3):row[3*j+a]=-1
        Aub.append(row);bub.append(-k)
    return dict(A_eq=Aeq,b_eq=list(beta),A_ub=Aub,b_ub=bub,
                variables=[f'z_{j+1}_{a+1}' for j in range(v) for a in range(3)])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--n',type=int,required=True)
    p.add_argument('--output',required=True,help='comma-separated output partition')
    args=p.parse_args();lam=tuple(map(int,args.output.split(',')))
    values=multiplicities(args.n,lam)
    print(json.dumps({'statement':'T-049','n':args.n,'output':lam,
        'class_order':CLASSES,'balanced_traces':balanced_traces(args.n,lam),
        'coefficients':[{"outer":mu,"value":v} for mu,v in zip(LABELS,values)]},indent=2))


if __name__=='__main__':main()
