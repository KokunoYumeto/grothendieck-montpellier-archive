"""Exact Weyl and Coxeter orbit certificates, using fundamental-weight coordinates.

Each reflection word is recorded in application order. No floating point data
or representation-dimension table is used.
"""
from collections import deque, Counter
import json

def compute(r, index, h):
    edges=[(0,2),(1,3),(2,3),(3,4),(4,5)]
    if r==7:edges.append((5,6))
    A=[[2*int(i==j) for j in range(r)] for i in range(r)]
    for i,j in edges:A[i][j]=A[j][i]=-1
    lam=tuple(int(i==index-1) for i in range(r))
    def s(v,j):
        return tuple(v[i]-v[j]*A[j][i] for i in range(r))
    def c(v):
        for j in reversed(range(r)):v=s(v,j)
        return v
    basis=[tuple(int(i==j) for i in range(r)) for j in range(r)]
    images=basis
    matrix_order=None
    for exponent in range(1,h+1):
        images=[c(v) for v in images]
        if images==basis:
            matrix_order=exponent
            break
    assert matrix_order==h
    words={lam:[]}; todo=deque([lam])
    while todo:
        v=todo.popleft()
        for j in range(r):
            w=s(v,j)
            if w not in words:words[w]=words[v]+[j+1];todo.append(w)
    seen=set(); cycles=[]
    for v in words:
        if v in seen:continue
        cyc=[];w=v
        while w not in seen:
            seen.add(w);cyc.append(w);w=c(w)
        assert w==v
        cycles.append(cyc)
    small=min((v for cyc in cycles if len(cyc)<h for v in cyc),
              key=lambda v:(len(words[v]),v))
    cyc=[small];w=c(small)
    while w!=small:cyc.append(w);w=c(w)
    w=lam
    for j in words[small]:w=s(w,j-1)
    assert w==small
    assert [len(words),sorted(map(len,cycles))]=={
        6:[27,[3,12,12]],7:[56,[2,18,18,18]]
    }[r]
    return dict(type=f"E{r}",cartan=A,highest_weight=lam,coxeter_h=h,
                checked_matrix_order=matrix_order,
                orbit_size=len(words),coxeter_cycle_lengths=sorted(map(len,cycles)),
                short_weight=small,word_from_highest=words[small],
                short_cycle=cyc,short_period=len(cyc))

if __name__=="__main__":
    for r,index,h in [(6,1,12),(7,7,18)]:
        print(json.dumps(compute(r,index,h),sort_keys=True))
