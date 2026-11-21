#!/usr/bin/env python3
"""Compress the fixed-coset frame detector when only parity is needed."""
from collections import deque
import json
from pathlib import Path
import numpy as np


def canon(a):
    a=tuple(x%12 for x in a);return min(a,tuple(-x%12 for x in a))
def mm(a,b):
    return canon((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                  a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def mmn(a,b,n):
    return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)
def span(vs,p):
    bs={}
    for raw in vs:
        v=raw.copy()%p
        for j,b in sorted(bs.items()):
            if v[j]:v=(v-v[j]*b)%p
        nz=np.flatnonzero(v)
        if len(nz):
            j=int(nz[0]);bs[j]=v*pow(int(v[j]),-1,p)%p
    return bs


one=canon((1,0,0,1));s=canon((0,1,-1,0));r=canon((0,-1,1,-1))
group=[one];idx={one:0};parents={0:None};todo=deque([0])
while todo:
    i=todo.popleft()
    for j,g in enumerate([s,r]):
        v=mm(group[i],g)
        if v not in idx:
            idx[v]=len(group);group.append(v);parents[idx[v]]=(i,j);todo.append(idx[v])
assert len(group)==576
C2=[g for g in group if mm(g,s)==mm(s,g)]
C3=[g for g in group if mm(g,r)==mm(r,g)]
assert (len(C2),len(C3))==(16,18)


def eta2(g):
    # At3 C(S)=<S>, odd exponent iff the off-diagonal entry is nonzero.
    # At4 the parity of that entry records the image in C(S mod2)=C2.
    return (int(g[1]%3!=0)+g[1]%2)%2


sign_tables={}
for n in [3,4]:
    ident=(1,0,0,1);R=(0,(-1)%n,1,(-1)%n);t=ident;table={}
    for j in range(3):
        for sign in [0,1]:table[tuple(((-1)**sign)*x%n for x in t)]=sign
        t=mmn(t,R,n)
    assert len(table)==6
    sign_tables[n]=table
def eta3(g):
    return (sign_tables[3][tuple(x%3 for x in g)]+sign_tables[4][tuple(x%4 for x in g)])%2


out={"statement":"D23.C13","Q_order":576,"detectors":[]}
for p,C,eta,generator in [(2,C2,eta2,s),(3,C3,eta3,r)]:
    assert all(eta(mm(a,b))==(eta(a)+eta(b))%2 for a in C for b in C)
    assert eta(generator)==0 and {eta(a) for a in C}=={0,1}
    H=[a for a in C if eta(a)==0]
    expected=8 if p==2 else 9
    assert len(H)==expected
    cosets=sorted({tuple(sorted(idx[mm(g,h)] for h in H)) for g in group})
    ci={v:i for i,v in enumerate(cosets)};c_of={a:i for i,v in enumerate(cosets) for a in v}
    dim=len(cosets);assert dim==(72 if p==2 else 64)
    def perm(g):return np.array([c_of[idx[mm(g,group[c[0]])]] for c in cosets],dtype=np.int64)
    perms=[perm(g) for g in group]
    def act(i,v):
        ans=np.zeros(dim,dtype=np.int16);ans[perms[i]]=v;return ans
    e=np.zeros(dim,dtype=np.int16);e[c_of[0]]=1
    ts=e if p==2 else np.zeros(dim,dtype=np.int16)
    tr=e if p==3 else np.zeros(dim,dtype=np.int16)
    cocycles=[np.zeros(dim,dtype=np.int16) for _ in group]
    for i in range(1,len(group)):
        parent,j=parents[i];cocycles[i]=(cocycles[parent]+act(parent,[ts,tr][j]))%p
    schreier=[]
    for i,g in enumerate(group):
        for j,h in enumerate([s,r]):
            target=idx[mm(g,h)]
            schreier.append((cocycles[i]+act(i,[ts,tr][j])-cocycles[target])%p)
    image=span(schreier,p)
    # The fixed-coset obstruction distinguishes exactly eta=1 among
    # centralizer residues, independently of the actual image of Gamma.
    pg=perms[idx[generator]]
    fixed=[j for j in range(dim) if int(pg[j])==j]
    bad=[]
    for g in C:
        rhs=(e-act(idx[g],e))%p
        if eta(g):
            assert np.count_nonzero(rhs[fixed])==2
            bad.append(idx[g])
        else:
            assert not np.any(rhs)
    result={"prime":p,"centralizer_order":len(C),"H_order":len(H),
            "H_matrices":H,"permutation_module_dimension":dim,
            "actual_U_image_rank":len(image),
            "actual_extension_order_expression":f"576 * {p}^{len(image)}",
            "excluded_odd_centralizer_residues":len(bad),
            "base_coset_index":c_of[0],"S_permutation":perms[idx[s]].tolist(),
            "R_permutation":perms[idx[r]].tolist(),
            "result":"PASS"}
    out["detectors"].append(result)
    print(json.dumps({k:result[k] for k in ["prime","H_order","permutation_module_dimension","actual_U_image_rank","excluded_odd_centralizer_residues","result"]}),flush=True)

out["original_FP23_image_ranks"]={}
for p,generator in [(2,s),(3,r)]:
    H=[one];cur=one
    for _ in range(1,p):cur=mm(cur,generator);H.append(cur)
    cosets=sorted({tuple(sorted(idx[mm(g,h)] for h in H)) for g in group})
    ci={a:i for i,c in enumerate(cosets) for a in c};d=len(cosets)
    perms=[np.array([ci[idx[mm(g,group[c[0]])]] for c in cosets]) for g in group]
    def act0(i,v):
        ans=np.zeros(d,dtype=np.int16);ans[perms[i]]=v;return ans
    e=np.zeros(d,dtype=np.int16);e[ci[0]]=1;zero=np.zeros(d,dtype=np.int16)
    ts,tr=(e,zero) if p==2 else (zero,e)
    cs=[zero.copy() for _ in group]
    for i in range(1,len(group)):
        par,j=parents[i];cs[i]=(cs[par]+act0(par,[ts,tr][j]))%p
    vs=[]
    for i,g in enumerate(group):
        for j,h in enumerate([s,r]):vs.append((cs[i]+act0(i,[ts,tr][j])-cs[idx[mm(g,h)]])%p)
    rank=len(span(vs,p));assert rank==(97 if p==2 else 96)
    out["original_FP23_image_ranks"][str(p)]=rank
path=Path(__file__).resolve().parents[1]/"records"/"compressed_parity_detector.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print('certificate:',path,flush=True)
