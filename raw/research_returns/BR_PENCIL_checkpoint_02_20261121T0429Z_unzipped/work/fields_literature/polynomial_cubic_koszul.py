#!/usr/bin/env python3
"""Weight-block Koszul calculations for the adjacent polynomial cubic pencil.

Exact modular ranks are exploratory lower certificates until independently
checked. No floating-point operations occur.
"""
from itertools import combinations, permutations
from pathlib import Path
from collections import defaultdict
from math import comb
import json,sys,time
import numpy as np

HERE=Path(__file__).resolve().parent
P=1000003
EW=[tuple(int(i==r) for i in range(3))+tuple(int(i==c) for i in range(4))
    for r in range(3) for c in range(4)]
AW=[(-1,-1,-1,-1,-1,-int(a==0),-int(a==1)) for a in range(2)]

def add(*weights):return tuple(sum(x) for x in zip(*weights))
def neg(w):return tuple(-x for x in w)
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def tensor(sign):
    vals=[]
    for a,last in enumerate((2,3)):
        labels=(0,1,last)
        for r in permutations(range(3)):
            for c in permutations(range(3)):
                word=tuple(4*r[i]+labels[c[i]] for i in range(3))
                value=parity(r)*parity(c) if sign==-1 else 1
                vals.append((a,*word,value))
    return vals

def pivots(M):
    a=np.array(M,dtype=np.int64)%P
    labels=list(range(a.shape[0]));rows=[];cols=[];r=0
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        h=r+int(nz[0]);a[[r,h]]=a[[h,r]];labels[r],labels[h]=labels[h],labels[r]
        rows.append(labels[r]);cols.append(c)
        a[r,c:]=a[r,c:]*pow(int(a[r,c]),-1,P)%P
        inds=np.flatnonzero(a[r+1:,c])+r+1
        if len(inds):a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[r,c:])%P
        r+=1
        if r==len(a):break
    return rows,cols

def build(p,sign):
    source_wedges=list(combinations(range(12),p))
    target_wedges=list(combinations(range(12),p+1))
    wedge_target_index={v:i for i,v in enumerate(target_wedges)}
    target_weight={}
    row_blocks=defaultdict(list)
    for h,J in enumerate(target_wedges):
        jw=add(AW[0],AW[1],*(EW[j] for j in J))
        for l in range(12):
            row=h*12+l;w=add(jw,EW[l]);target_weight[row]=w;row_blocks[w].append(row)
    col_blocks=defaultdict(list);sparse={}
    by_ak=defaultdict(list)
    for a,j,k,l,v in tensor(sign):by_ak[a,k].append((j,l,v))
    for alpha in range(2):
        a=1-alpha
        for h,I in enumerate(source_wedges):
            iw=add(AW[alpha],*(EW[j] for j in I))
            for k in range(12):
                col=(alpha*len(source_wedges)+h)*12+k
                w=add(iw,neg(EW[k]));col_blocks[w].append(col)
                vals=[]
                for j,l,v in by_ak[a,k]:
                    if j in I:continue
                    J=tuple(sorted(I+(j,)))
                    row=wedge_target_index[J]*12+l
                    value=v*(-1)**a*(-1)**sum(i<j for i in I)
                    assert target_weight[row]==w
                    vals.append((row,value))
                sparse[col]=vals
    result=[];total=0;largest=0
    for w,cols in col_blocks.items():
        rows=row_blocks.get(w,[])
        if not rows:continue
        ri={r:i for i,r in enumerate(rows)}
        M=np.zeros((len(rows),len(cols)),dtype=np.int64)
        for c,col in enumerate(cols):
            for row,v in sparse[col]:M[ri[row],c]+=v
        rr,cc=pivots(M);total+=len(rr);largest=max(largest,len(rows)*len(cols))
        result.append({'weight':list(w),'shape':list(M.shape),'rank':len(rr),
                       'minor_rows':[rows[i] for i in rr],'minor_cols':[cols[i] for i in cc]})
    cost=comb(11,p)
    return {'family':'det' if sign==-1 else 'per','p':p,'shape':[len(target_wedges)*12,2*len(source_wedges)*12],
            'prime':P,'rank_mod':total,'pure_cost':cost,'lower_bound':(total+cost-1)//cost,
            'nonempty_blocks':len(result),'largest_block_area':largest,'blocks':result}

def main():
    ps=[int(s) for s in sys.argv[1:]] or [1,2,3,4]
    start=time.time();records=[]
    for p in ps:
        for sign in (-1,1):
            record=build(p,sign);records.append(record)
            print({k:v for k,v in record.items() if k!='blocks'},'seconds',time.time()-start,flush=True)
            (HERE/'polynomial_cubic_koszul_results.json').write_text(json.dumps(records,indent=2)+'\n')

if __name__=='__main__':main()
