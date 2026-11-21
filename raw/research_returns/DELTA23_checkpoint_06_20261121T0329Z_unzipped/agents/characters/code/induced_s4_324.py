#!/usr/bin/env python3
"""Induce F->S4 to B=C2*C3, retaining the literal source marking."""
from collections import deque
from pathlib import Path
import itertools
import json
import math
from sympy.combinatorics import Permutation, PermutationGroup


def wm(a,b):
    out=list(a)
    for g in b:
        if out and (out[-1]==0)==(g==0):
            h=out.pop()
            if g:
                if (h+g)%3:out.append((h+g)%3)
        else:out.append(g)
    return tuple(out)


def wi(a):return tuple(0 if x==0 else 3-x for x in a[::-1])
def wp(a,n):
    if n<0:return wp(wi(a),-n)
    out=()
    for _ in range(n):out=wm(out,a)
    return out


def pm(a,b):return tuple(b[a[i]] for i in range(len(a)))
def pi(a):return tuple(a.index(i) for i in range(len(a)))
def pp(a,n):
    if n<0:return pp(pi(a),-n)
    out=tuple(range(len(a)))
    for _ in range(n):out=pm(out,a)
    return out


s=(0,);r=(1,);tau=wm(s,r)
x=wp(tau,-2);y=wm(wm(s,x),s)
u=wi(tau);v=wm(s,(2,))
assert wm(wm(u,v),u)==s and wm(u,v)==r
sd=(1,0,2);rd=(1,2,0)
def deck(w):
    out=(0,1,2)
    for g in w:out=pm(out,sd if g==0 else pp(rd,g))
    return out


reps=[(),s,r,(2,),wm(s,r),wm(s,(2,))]
didx={deck(t):i for i,t in enumerate(reps)}
assert len(didx)==6
edges=[];need=set()
for t in reps:
    row=[]
    for g in [s,r]:
        target=didx[deck(wm(t,g))]
        h=wm(wm(t,g),wi(reps[target]));need.add(h);row.append((target,h))
    edges.append(row)


# Schreier cocycles are short words in the fixed x,y.  Exhaustion in the free
# product B provides an exact rewriting certificate, with no word guessing.
fgens=[x,y,wi(x),wi(y)]
rewrites={():()};todo=deque([()])
while not need.issubset(rewrites):
    old=todo.popleft()
    for j,g in enumerate(fgens):
        new=wm(old,g)
        if new not in rewrites:
            rewrites[new]=rewrites[old]+(j,);todo.append(new)
            if len(rewrites)>100000:raise RuntimeError('Schreier rewrite limit')


p=(1,2,0,3);t=(3,1,2,0);fgimages=[p,t,pi(p),pi(t)]
def rho(w):
    out=(0,1,2,3)
    for j in rewrites[w]:out=pm(out,fgimages[j])
    return out


sg=[];rg=[]
for j,out in [(0,sg),(1,rg)]:
    for row in edges:
        target,h=row[j];himage=rho(h)
        out.extend(4*target+himage[k] for k in range(4))
sg,rg=tuple(sg),tuple(rg)
assert pp(sg,2)==tuple(range(24)) and pp(rg,3)==tuple(range(24))
ug=pi(pm(sg,rg));vg=pm(sg,pp(rg,2))
xg,yg=pp(ug,2),pp(vg,2)
assert tuple(xg[:4])==p and tuple(yg[:4])==t
group=PermutationGroup([Permutation(sg),Permutation(rg)])
pure=PermutationGroup([Permutation(xg),Permutation(yg)])
record={"field":"permutations on 24 induced sheets", "source":"F=ker(B->S3), x=(sr)^-2,y=sxs; x->(123), y->(14)",
        "s":sg,"r":rg,"u":ug,"v":vg,"x":xg,"y":yg,
        "schreier_representatives":reps,
        "schreier_cocycles":[[{"target":i,"Bword":h,"Fword":rewrites[h]} for i,h in row] for row in edges],
        "B_image_order":int(group.order()),"F_image_order":int(pure.order()),
        "F_derived_orders":[int(g.order()) for g in pure.derived_series()]}
path=Path(__file__).resolve().parents[1]/"records"/"induced_s4_324.json"
path.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:record[k] for k in ["B_image_order","F_image_order","F_derived_orders"]}),flush=True)


