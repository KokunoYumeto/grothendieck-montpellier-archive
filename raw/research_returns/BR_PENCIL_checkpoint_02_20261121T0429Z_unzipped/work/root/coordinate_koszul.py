"""Exact modular Koszul certificates for coordinate 2x2 minor subspaces.

The matrix entries are integers. A nonzero minor modulo the explicit prime
certifies that minor is nonzero over Q. This is not floating-point evidence.
"""
from __future__ import annotations
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import argparse, json, math, time
import numpy as np

N = 4
PAIRS = list(combinations(range(N), 2))
RECTS = [(a, b) for a in PAIRS for b in PAIRS]
INDEX = {x: i for i, x in enumerate(RECTS)}
SUPPORTS = [frozenset(N*r+c for r in a for c in b) for a,b in RECTS]

def group_maps():
    result = []
    for r in permutations(range(N)):
        for c in permutations(range(N)):
            mapping = tuple(INDEX[(tuple(sorted(r[i] for i in a)),tuple(sorted(c[i] for i in b)))] for a,b in RECTS)
            result.append(mapping)
            result.append(tuple((x % 6)*6 + x//6 for x in mapping))
    return result

def orbit_reps(j):
    maps = group_maps()
    seen = set()
    for s in combinations(range(36),j):
        if s in seen: continue
        orb = {tuple(sorted(mp[i] for i in s)) for mp in maps}
        seen.update(orb)
        yield s, len(orb)

def slices(s, sign):
    support = sorted(set().union(*(SUPPORTS[i] for i in s)))
    ix = {v:i for i,v in enumerate(support)}
    m = len(support)
    mats=[]
    for z in s:
        (r0,r1),(c0,c1)=RECTS[z]
        a,b,c,d = [ix[N*r+col] for r,col in [(r0,c0),(r0,c1),(r1,c0),(r1,c1)]]
        mat=np.zeros((m,m),dtype=np.int64)
        mat[a,d]=mat[d,a]=1
        mat[b,c]=mat[c,b]=sign
        mats.append(mat)
    return support,mats

def koszul(mats,p):
    j=len(mats)
    nr,nc=mats[0].shape
    src=list(combinations(range(j),p))
    dst=list(combinations(range(j),p+1))
    di={x:i for i,x in enumerate(dst)}
    out=np.zeros((len(dst)*nr,len(src)*nc),dtype=np.int64)
    for ci,I in enumerate(src):
        for a,M in enumerate(mats):
            if a in I: continue
            J=tuple(sorted((a,)+I))
            ri=di[J]
            sg=(-1)**sum(i<a for i in I)
            out[ri*nr:(ri+1)*nr,ci*nc:(ci+1)*nc]=sg*M
    return out

def modular_rank(a,prime=1000003):
    """Return rank and original row/column sets of a certified pivot minor."""
    a=np.array(a,dtype=np.int64,copy=True)%prime
    nr,nc=a.shape
    rowids=list(range(nr))
    pivrows=[];pivcols=[];pivvals=[]
    r=0
    for c in range(nc):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz): continue
        k=r+int(nz[0])
        if k!=r:
            a[[r,k]]=a[[k,r]]
            rowids[r],rowids[k]=rowids[k],rowids[r]
        v=int(a[r,c]); inv=pow(v,-1,prime)
        pivrows.append(rowids[r]);pivcols.append(c);pivvals.append(v)
        a[r,c:]=(a[r,c:]*inv)%prime
        inds=np.flatnonzero(a[r+1:,c])+r+1
        if len(inds):
            a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[r,c:])%prime
        r+=1
        if r==nr: break
    return {"rank_mod_p":r,"prime":prime,"rows":pivrows,"cols":pivcols,"pivot_product_mod_p":math.prod(pivvals)%prime}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--j',type=int,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--target',type=int,default=0,help='Skip Koszul if ordinary support already attains this lower bound.')
    args=parser.parse_args()
    start=time.time(); records=[]
    ps=range(1,(args.j-1)//2+1) if args.j>2 else [1]
    for s,count in orbit_reps(args.j):
        support,dmats=slices(s,-1)
        rec={"subset":list(s),"rectangles":[RECTS[i] for i in s],"orbit_size":count,"support":support,"support_bound":len(support),"families":{}}
        for name,sgn in [('det',-1),('per',1)]:
            bound=max(len(support),args.j)
            cert=[]
            if not args.target or bound<args.target:
                _,mats=slices(s,sgn)
                for p in ps:
                    mat=koszul(mats,p)
                    c=modular_rank(mat)
                    c.update({"p":p,"shape":list(mat.shape),"pure_cost":math.comb(args.j-1,p)})
                    c['bound']=(c['rank_mod_p']+c['pure_cost']-1)//c['pure_cost']
                    bound=max(bound,c['bound']);cert.append(c)
                    if args.target and bound>=args.target: break
            rec['families'][name]={"lower_bound":bound,"koszul":cert}
        records.append(rec)
    data={"j":args.j,"n":4,"b":2,"number_of_subsets":math.comb(36,args.j),"number_of_orbits":len(records),"orbit_sum":sum(r['orbit_size'] for r in records),"target":args.target,"support_counts":dict(Counter({m:sum(r['orbit_size'] for r in records if r['support_bound']==m) for m in sorted({r['support_bound'] for r in records})})),"minimum_certified":{f:min(r['families'][f]['lower_bound'] for r in records) for f in ['det','per']},"seconds":time.time()-start,"records":records}
    assert data['orbit_sum']==data['number_of_subsets']
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))
    for fam in ['det','per']:
        m=data['minimum_certified'][fam]
        print(fam,'minimizers',[r['subset'] for r in records if r['families'][fam]['lower_bound']==m][:40])

if __name__=='__main__':main()
