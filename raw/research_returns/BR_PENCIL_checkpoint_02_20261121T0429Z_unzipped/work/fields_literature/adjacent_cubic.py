#!/usr/bin/env python3
"""Exact tensor/Koszul experiments for two adjacent row-cubic slices."""
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import json

DIMS=(2,4,4,4)

def entries(sign):
    out={}
    for a,last in enumerate((2,3)):
        base=(0,1,last)
        for p in permutations(range(3)):
            inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
            out[(a,)+tuple(base[i] for i in p)] = sign**inv
    return out

def wedge(I, x):
    if x in I:return None
    return tuple(sorted(I+(x,))),(-1)**sum(i<x for i in I)

def multi_matrix(sign,wedges,ps,contract,output):
    ws=[list(combinations(range(DIMS[i]),p)) for i,p in zip(wedges,ps)]
    wd=[list(combinations(range(DIMS[i]),p+1)) for i,p in zip(wedges,ps)]
    cols=list(product(*ws,range(DIMS[contract])))
    rows=list(product(*wd,range(DIMS[output])))
    ri={x:i for i,x in enumerate(rows)}
    M=[[0]*len(cols) for _ in rows]
    for c,src in enumerate(cols):
        for ix,v in entries(sign).items():
            if ix[contract]!=src[-1]:continue
            dest=[];value=v
            for h,i in enumerate(wedges):
                w=wedge(src[h],ix[i])
                if w is None:break
                I,s=w;dest.append(I);value*=s
            else:
                r=ri[tuple(dest)+(ix[output],)]
                M[r][c]+=value
    cost=1
    for i,p in zip(wedges,ps):cost*=comb(DIMS[i]-1,p)
    return M,cost

def modular_pivots(M,prime=1000003):
    a=[[x%prime for x in row] for row in M]
    labels=list(range(len(a)));r=0;rows=[];cols=[]
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];labels[r],labels[pivot]=labels[pivot],labels[r]
        rows.append(labels[r]);cols.append(c)
        inv=pow(a[r][c],-1,prime)
        a[r]=[x*inv%prime for x in a[r]]
        for i in range(r+1,len(a)):
            fac=a[i][c]
            if fac:a[i]=[(x-fac*y)%prime for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return rows,cols

def main():
    results=[]
    # The last three factors are equivalent up to a sign, so two shapes suffice.
    for wedges,contract,output in [((0,1),2,3),((1,2),0,3),((1,2),3,0)]:
        for ps in product(*(range(1,DIMS[i]) for i in wedges)):
            rec={'wedges':wedges,'ps':ps,'contract':contract,'output':output,'families':{}}
            for label,sgn in [('det',-1),('per',1)]:
                M,cost=multi_matrix(sgn,wedges,ps,contract,output)
                rows,cols=modular_pivots(M)
                rec['families'][label]={'shape':[len(M),len(M[0])],'cost':cost,'rank_mod':len(rows),'bound':(len(rows)+cost-1)//cost,'rows':rows,'cols':cols}
            results.append(rec)
            print({k:v for k,v in rec.items() if k!='families'}, {f:(v['shape'],v['cost'],v['rank_mod'],v['bound']) for f,v in rec['families'].items()},flush=True)
    Path(__file__).with_name('adjacent_cubic_koszul_search.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
