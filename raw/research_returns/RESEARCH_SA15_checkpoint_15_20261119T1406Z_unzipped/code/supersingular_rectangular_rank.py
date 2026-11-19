#!/usr/bin/env python3
"""Exact discovery for the first inseparable rectangular polarization.

All finite searches and complete matrices are retained. The geometric proof
of the generic upper bound and the all-degree extension is separate.
"""
from pathlib import Path
import itertools,json,random,time

started=time.perf_counter()
w=Path(__file__).resolve().parents[1]

def basis(n):
    result=[(a,0) for a in range(n//2+1)]
    result += [(a,1) for a in range((n-3)//2+1)] if n>=3 else []
    assert len(result)==n
    return result

def one_factor(n):
    B=basis(n);index={v:i for i,v in enumerate(B)}
    out=[]
    for a in B:
        row=[]
        for b in B:
            x,y=a[0]+b[0],a[1]+b[1]
            terms=[(x,y)] if y<2 else [(x,1),(x+3,0)]
            targets=set()
            for i,j in terms:
                target=((i//2,1) if i%2 else (i//2+1,0)) if j else ((i//2,0) if i%2 else None)
                if target is not None:
                    k=index[target]
                    if k in targets:targets.remove(k)
                    else:targets.add(k)
            row.append(sorted(targets))
        out.append(row)
    return B,out

def rank(columns):
    piv={}
    for column in columns:
        while column:
            p=column.bit_length()-1
            if p in piv:column^=piv[p]
            else:piv[p]=column;break
    return len(piv)

def apply(columns,vector):
    out=0
    while vector:
        bit=vector&-vector;vector^=bit
        out^=columns[bit.bit_length()-1]
    return out

def discover(n,m,target,budget=10000):
    B,L=one_factor(n);D,R=one_factor(m)
    pairs=list(itertools.product(range(n),range(m)))
    elementary=[]
    for a,b in pairs:
        elementary.append([sum(1<<(m*i+j) for i,j in itertools.product(L[a][u],R[b][v])) for u,v in pairs])
    rng=random.Random(202611191110+n*101+m)
    trials=[];witness=None
    for attempt in range(1,budget+1):
        s=rng.getrandbits(n*m);C=[0]*(n*m)
        for i in range(n*m):
            if s>>i&1:C=[a^b for a,b in zip(C,elementary[i])]
        r1=rank(C);C2=[apply(C,v) for v in C];r2=rank(C2)
        trials.append([s,r1,r2])
        if r1==r2==target:
            assert apply(C,s)==0
            witness=dict(section_bits=s,columns=C,rank_C=r1,rank_C2=r2)
            break
    return dict(degrees=[n,m],basis_first=B,basis_second=D,
                tensor_index=f'{m}*i+j',seed=202611191110+n*101+m,
                target=target,budget=budget,attempts=attempt,
                complete_trials=trials,witness=witness)

case=discover(6,3,16)
out=dict(status='PASS' if case['witness'] else 'NO_WITNESS_IN_BOUNDED_SEARCH',
         curve='y^2+y=x^3 over F2',case=case,
         matrix_convention='Root-removed Cartier on H0(O(6O) external O(3O)); coherent Frobenius is its transpose.',
         scope='One exact base-rank witness; no all-degree or full-monodromy inference from sampling.',
         elapsed_seconds=time.perf_counter()-started)
(w/'outputs/supersingular_rectangular_rank.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
