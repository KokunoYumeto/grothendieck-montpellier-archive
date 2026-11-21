"""Exact small boundary characters and deterministic Reynolds seeds."""
from pathlib import Path
from functools import lru_cache
from itertools import permutations,combinations
from collections import defaultdict
from random import Random
from math import comb
import csv
HERE=Path(__file__).resolve().parent
@lru_cache(None)
def compositions(n,r):
    if r==1:return ((n,),)
    return tuple((i,)+tail for i in range(n+1) for tail in compositions(n-i,r-1))
def partitions(n,r,cap=None):
    if not r:
        if not n:yield ()
        return
    if cap is None:cap=n
    for i in range(min(cap,n),-1,-1):
        if i*r<n:break
        for tail in partitions(n-i,r-1,i):yield (i,)+tail
def schur(outer,inner,rank):
    N=outer*inner;base=N+1
    place=[base**j for j in range(rank-1)]
    weights=[sum(w[j]*place[j] for j in range(rank-1)) for w in compositions(inner,rank)]
    h=[{0:1}]
    for i in range(1,outer+1):
        d=defaultdict(int)
        for k in range(1,i+1):
            kw=[k*w for w in weights]
            for x,c in h[i-k].items():
                for w in kw:d[x+w]+=c
        assert all(v%i==0 for v in d.values())
        h.append({x:v//i for x,v in d.items()})
    perms=[(p,(-1)**sum(p[i]>p[j] for i in range(rank) for j in range(i+1,rank)))
           for p in permutations(range(rank))]
    answer={}
    for lam in partitions(N,rank):
        m=0
        for p,sg in perms:
            w=tuple(lam[i]+p[i]-i for i in range(rank))
            if min(w)<0 or max(w)>N:continue
            m+=sg*h[-1].get(sum(w[j]*place[j] for j in range(rank-1)),0)
        assert m>=0
        if m:answer[lam]=m
    den=1
    for i in range(rank):
        for j in range(i+1,rank):den*=j-i
    def dim(lam):
        num=1
        for i in range(rank):
            for j in range(i+1,rank):num*=lam[i]-lam[j]+j-i
        assert num%den==0
        return num//den
    expected=comb(comb(inner+rank-1,rank-1)+outer-1,outer)
    assert sum(m*dim(lam) for lam,m in answer.items())==sum(h[-1].values())==expected
    return answer,expected
def make_case(r,L,b):
    source,dimension=schur(r,b,r);target,_=schur(r,b-L,r)
    minors=[I for h in range(1,r+1) for I in combinations(range(r),h)]
    index={I:z for z,I in enumerate(minors)}
    @lru_cache(None)
    def pred(lam,j):
        out=[]
        def visit(i,left,mu):
            if i==r:
                if not left:out.append(tuple(mu))
                return
            low=lam[i+1] if i+1<r else 0
            high=lam[i] if i<j-1 else 0
            for x in range(min(high,left),low-1,-1):visit(i+1,left-x,mu+(x,))
        visit(0,(j-1)*b,())
        return tuple(out)
    @lru_cache(None)
    def number(lam,j):
        if j==0:return int(not any(lam))
        return sum(number(mu,j-1) for mu in pred(lam,j))
    def seed(lam,idx):
        shapes=[None]*(r+1);shapes[r]=lam
        for j in range(r,0,-1):
            for mu in pred(shapes[j],j):
                k=number(mu,j-1)
                if idx>=k:idx-=k
                else:shapes[j-1]=mu;break
            else:raise AssertionError('overflow')
        rows=[]
        for i in range(r):
            row=[]
            for j in range(1,r+1):row += [j-1]*(shapes[j][i]-shapes[j-1][i])
            rows.append(row)
        counts=[0]*len(minors)
        for c in range(lam[0]):
            I=tuple(rows[i][c] for i in range(r) if c<len(rows[i]))
            assert I==tuple(sorted(set(I)))
            counts[index[I]]+=1
        return counts
    output=HERE/f'POLARIZATION_R{r}_L{L}_B{b}'
    records=[]
    with Path(str(output)+'.seeds').open('w') as f:
        print(r,L,b,len(source),file=f)
        for lam,m in source.items():
            tm=sum(v for mu,v in target.items()
                   if all(lam[i]>=mu[i]>=(lam[i+1] if i+1<r else 0) for i in range(r)))
            K=number(lam,r);cap=K
            rng=Random(20261121+sum((i+1)*v*100**i for i,v in enumerate(lam)))
            ids=rng.sample(range(K),cap)
            print(*lam,m,K,cap,file=f)
            for idx in ids:print(*seed(lam,idx),file=f)
            records.append(dict(partition=','.join(map(str,lam)),source_multiplicity=m,
                                target_multiplicity=tm,forced_kernel=max(0,m-tm),
                                tableau_dimension=K,seeds=cap))
    with Path(str(output)+'_SOURCE.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]),delimiter='\t');w.writeheader();w.writerows(records)
    print('CASE',r,L,b,'constituents',len(source),'HWsum',sum(source.values()),
          'maxmult',max(source.values()),'dimension',dimension,'forced_kernel',
          [(z['partition'],z['forced_kernel']) for z in records if z['forced_kernel']],flush=True)
if __name__=='__main__':
    for case in [(3,2,5),(3,3,8),(5,1,4)]:make_case(*case)
