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


p=(1,2,0,3);t=(1,2,3,0);fgimages=[p,t,pi(p),pi(t)]
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
record={"field":"permutations on 24 induced sheets", "source":"F=ker(B->S3), x=(sr)^-2,y=sxs; x->(123), y->(1234)",
        "s":sg,"r":rg,"u":ug,"v":vg,"x":xg,"y":yg,
        "schreier_representatives":reps,
        "schreier_cocycles":[[{"target":i,"Bword":h,"Fword":rewrites[h]} for i,h in row] for row in edges],
        "B_image_order":int(group.order()),"F_image_order":int(pure.order()),
        "F_derived_orders":[int(g.order()) for g in pure.derived_series()]}
path=Path(__file__).resolve().parents[1]/"records"/"induced_s4_harmonic.json"
path.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps({k:record[k] for k in ["B_image_order","F_image_order","F_derived_orders"]}),flush=True)


if __name__=="__main__":
    # The projective signed modulus-12 quotient on primitive row vectors.
    # Row action uses the same right-composition convention as the induction.
    def normvec(vec):return min(tuple(vec),tuple(-a%12 for a in vec))
    vectors=sorted({normvec((a,b)) for a,b in itertools.product(range(12),repeat=2) if math.gcd(a,b,12)==1})
    vindex={v:i for i,v in enumerate(vectors)}
    def matperm(mat):
        a,b,c,d=mat
        return tuple(vindex[normvec(((x*a+y*c)%12,(x*b+y*d)%12))] for x,y in vectors)
    uq=matperm((1,1,0,1));vq=matperm((1,0,11,1))
    sq=pm(pm(uq,vq),uq);rq=pm(uq,vq)
    def join(a,b):return tuple(a)+tuple(len(a)+j for j in b)
    sj,rj=join(sg,sq),join(rg,rq)
    uj,vj=join(ug,uq),join(vg,vq)
    full=PermutationGroup([Permutation(sj),Permutation(rj)])
    purejoint=PermutationGroup([Permutation(pp(uj,2)),Permutation(pp(vj,2))])
    print('joint B',full.order(),'joint pure',purejoint.order(),flush=True)
    central=purejoint.centralizer(Permutation(sj))
    print('pure s-centralizer',central.order(),flush=True)
    # Exact CRT classes with beta4=I and beta3=+S or -S.
    def crt(a4,a3):return next(a for a in range(12) if a%4==a4%4 and a%3==a3%3)
    oddmats=[]
    for sign in [1,2]:
        m4=(1,0,0,1);m3=(0,sign,(-sign)%3,0)
        oddmats.append(tuple(crt(a,b) for a,b in zip(m4,m3)))
    oddperms={matperm(m):m for m in oddmats}
    witness=None
    for elem in central.generate_schreier_sims():
        qpart=tuple(elem(24+j)-24 for j in range(48))
        if qpart in oddperms:
            witness={"matrix_mod12":oddperms[qpart],"joint_permutation":list(elem.array_form)}
            break
    record.update({"joint_Q12_B_order":int(full.order()),"joint_Q12_F_order":int(purejoint.order()),
                   "joint_pure_s_centralizer_order":int(central.order()),
                   "odd_harmonic_pure_centralizer_witness":witness})
    purederived=purejoint.derived_subgroup()
    derivedcentral=purederived.centralizer(Permutation(sj))
    dwitness=None
    for elem in derivedcentral.generate_schreier_sims():
        qpart=tuple(elem(24+j)-24 for j in range(48))
        if qpart in oddperms:
            dwitness={"matrix_mod12":oddperms[qpart],"joint_permutation":list(elem.array_form)}
            break
    record.update({"joint_Fderived_order":int(purederived.order()),
                   "joint_Fderived_s_centralizer_order":int(derivedcentral.order()),
                   "odd_harmonic_Fderived_centralizer_witness":dwitness})
    path.write_text(json.dumps(record,indent=2)+"\n")
    print('odd harmonic pure centralizer survives:',witness is not None,flush=True)
    print('F-derived order',purederived.order(),'s-centralizer',derivedcentral.order(),
          'odd harmonic survives:',dwitness is not None,flush=True)
