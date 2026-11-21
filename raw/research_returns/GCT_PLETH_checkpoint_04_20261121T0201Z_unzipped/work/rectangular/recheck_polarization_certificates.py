#!/usr/bin/env python3
"""Recompute every selected minor entry in the two requested finite cases.

Uses a separate Python/NumPy multivariate Taylor evaluator and recursive
Laplace determinants; never calls the C++ evaluator.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import numpy as np
import sys
from math import isqrt

P=1000003
HERE=Path(__file__).resolve().parent
MINORS=[I for h in range(1,5) for I in combinations(range(4),h)]
MINOR_INDEX={I:i for i,I in enumerate(MINORS)}
assert all(P%d for d in range(2,isqrt(P)+1))

def check_symmetric(orbit):
    raw={counts:c for c,counts in orbit}
    for adjacent in range(3):
        p=list(range(4))
        p[adjacent],p[adjacent+1]=p[adjacent+1],p[adjacent]
        transformed={}
        for counts,c in raw.items():
            nc=[0]*15
            sg=1
            for z,I in enumerate(MINORS):
                J=tuple(p[i] for i in I)
                inversions=sum(J[u]>J[v] for u in range(len(J))
                               for v in range(u+1,len(J)))
                nc[MINOR_INDEX[tuple(sorted(J))]]+=counts[z]
                sg*=(-1)**(inversions*counts[z])
            transformed[tuple(nc)]=c*sg
        assert transformed==raw

def det(A):
    if not A: return 1
    return sum((-1)**j*A[0][j]*det(tuple(tuple(row[k] for k in range(len(A)) if k!=j)
                                        for row in A[1:])) for j in range(len(A)))%P

def parse(stem):
    ints=iter(map(int,(HERE/(stem+".input")).read_text().split()))
    L,b,n=next(ints),next(ints),next(ints)
    blocks={}
    for _ in range(n):
        lam=tuple(next(ints) for _ in range(4))
        m,nc=next(ints),next(ints)
        cand=[]
        for _ in range(nc):
            nt=next(ints)
            orbit=[]
            for _ in range(nt):
                c=next(ints);counts=tuple(next(ints) for _ in range(15))
                assert tuple(sum(counts[z] for z,I in enumerate(MINORS) if len(I)>i)
                             for i in range(4))==lam
                assert all(sum(counts[z] for z,I in enumerate(MINORS) if i in I)==b
                           for i in range(4))
                orbit.append((c,counts))
            cand.append(orbit)
        blocks[lam]=(m,cand)
    lines=iter((HERE/(stem+"_CERTIFICATES.txt")).read_text().splitlines())
    assert next(lines)=="prime 1000003"
    next(lines)
    points={}
    certs=[]
    for line in lines:
        ss=line.split()
        if ss[0]=="point":
            points[int(ss[1])]=tuple(map(int,ss[2:]))
        elif ss[0]=="partition":
            lam=tuple(map(int,ss[1].split(",")));m=int(ss[3]);rank=int(ss[5])
            chosen=tuple(map(int,next(lines).split()[1:]))
            rows=tuple(map(int,next(lines).split()[1:]))
            matrix=[tuple(map(int,next(lines).split())) for _ in range(rank)]
            d=int(next(lines).split()[1])
            assert rank==m==blocks[lam][0]
            certs.append((lam,chosen,rows,matrix,d))
    assert len(certs)==len(blocks)
    assert {c[0] for c in certs}==set(blocks)
    return L,b,blocks,points,certs

def run(stem):
    L,b,blocks,points,certs=parse(stem)
    @lru_cache(None)
    def forms(point):
        data=points[point]
        X=tuple(tuple(data[4*i+j] for j in range(4)) for i in range(4))
        x=data[16:]
        ans=[]
        for I in MINORS:
            h=len(I)
            A=tuple(tuple(X[i][j] for j in I) for i in range(h))
            linear=[0]*4
            for k,j in enumerate(I):
                B=tuple(tuple(x[i] if q==k else A[i][q] for q in range(h)) for i in range(h))
                linear[j]=det(B)
            ans.append((det(A),tuple(linear)))
        return tuple(ans)
    @lru_cache(None)
    def coefficient(counts,point):
        dp=np.zeros((L+1,)*4,dtype=np.int64)
        dp[(0,)*4]=1
        fs=forms(point)
        for z,m in enumerate(counts):
            c,linear=fs[z]
            for _ in range(m):
                nd=dp*c
                for j in MINORS[z]:
                    to=[slice(None)]*4;fr=to.copy()
                    to[j]=slice(1,None);fr[j]=slice(None,-1)
                    nd[tuple(to)]+=dp[tuple(fr)]*linear[j]
                dp=nd%P
        return int(dp[(L,)*4])
    cells=0
    for lam,chosen,rows,matrix,d in certs:
        cand=blocks[lam][1]
        for candidate in chosen:
            check_symmetric(cand[candidate])
        for i,point in enumerate(rows):
            for j,candidate in enumerate(chosen):
                val=sum(c*coefficient(counts,point) for c,counts in cand[candidate])%P
                assert val==matrix[i][j],(lam,i,j,val,matrix[i][j])
                cells+=1
        assert det(tuple(matrix))==d!=0,(lam,d)
    msg=f"{stem}: PASS; {len(certs)} blocks; {cells} independently recomputed entries; {coefficient.cache_info().currsize} Taylor evaluations"
    print(msg)
    return msg

if __name__=="__main__":
    stems=sys.argv[1:] or ["POLARIZATION_R4_L1_B3","POLARIZATION_R4_L2_B7"]
    msgs=[run(s) for s in stems]
    (HERE/"POLARIZATION_INDEPENDENT_RECHECK.txt").write_text("\n".join(msgs)+"\n")
