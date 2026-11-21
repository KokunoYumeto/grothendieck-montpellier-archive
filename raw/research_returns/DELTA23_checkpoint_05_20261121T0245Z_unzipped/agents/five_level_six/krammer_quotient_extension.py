#!/usr/bin/env python3
"""Exact analysis of the Krammer B3 restriction, DELTA23.

Uses the complete explicitly enumerated matrix group supplied by the pentagon
agent, but performs independent block, quotient, and extension checks.
F9 is encoded by a+3b, with i^2=-1; F3 matrices use doubled coordinates.
"""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
PENTAGON=HERE.parent/'pentagon'
data=np.load(PENTAGON/'krammer_first_pair.npz')
pure=data['pure'].astype(np.int16)
derived=data['derived'].astype(np.int16)
gens=data['generators'].astype(np.int16)
I=np.eye(12,dtype=np.int16)
IW=[0,1,2,3,6,7]
IQ=[4,5,8,9,10,11]
I6=np.eye(6,dtype=np.int16)

def mm(a,b):return a@b%3
def mp(a,n):
    out=np.eye(len(a),dtype=np.int16)
    while n:
        if n&1:out=mm(out,a)
        a=mm(a,a);n//=2
    return out
def inv(a):
    n=len(a);ar=np.concatenate([a.copy(),np.eye(n,dtype=np.int16)],axis=1)
    for j in range(n):
        p=next(k for k in range(j,n) if ar[k,j])
        ar[[j,p]]=ar[[p,j]];ar[j]=ar[j]*int(ar[j,j])%3
        for k in range(n):
            if k!=j and ar[k,j]:ar[k]=(ar[k]-ar[k,j]*ar[j])%3
    return ar[:,n:]
def block(a,inds):return a[np.ix_(inds,inds)]
def key(a):return a.astype(np.int8).tobytes()
def f9(a):
    n=len(a)//2;m=len(a[0])//2;out=[]
    for j in range(n):
        row=[]
        for k in range(m):
            u=int(a[2*j,2*k]);v=int(a[2*j+1,2*k])
            assert np.array_equal(a[2*j:2*j+2,2*k:2*k+2],[[u,-v%3],[v,u]])
            row.append(u+3*v)
        out.append(row)
    return out
def to3(a):
    out=np.zeros((2*len(a),2*len(a[0])),dtype=np.int16)
    for j,row in enumerate(a):
        for k,v in enumerate(row):
            u,b=int(v)%3,int(v)//3
            out[2*j:2*j+2,2*k:2*k+2]=[[u,-b%3],[b,u]]
    return out
def group(gs,limit=200000):
    unit=np.eye(len(gs[0]),dtype=np.int16);seen={key(unit)};els=[unit]
    for a in els:
        for g in gs:
            b=mm(a,g);k=key(b)
            if k not in seen:
                seen.add(k);els.append(b)
                if len(els)>limit:raise RuntimeError('group enumeration limit')
    return els

a,b,c=gens
literal_a=[[6,0,0,8,8,0],[0,0,0,3,0,0],[0,0,0,0,3,0],[0,1,0,7,0,0],[0,0,1,0,7,0],[0,0,0,0,0,1]]
literal_b=[[0,3,0,0,0,0],[1,7,0,0,0,0],[0,0,1,0,0,0],[0,7,0,6,0,8],[0,0,0,0,0,3],[0,0,0,0,1,7]]
assert np.array_equal(a,to3(literal_a)) and np.array_equal(b,to3(literal_b))
x,y=mp(a,2),mp(b,2)
# Rebuild the group from the two literal matrices rather than assuming that the
# imported array is an exhaustive enumeration or that it has no duplicates.
rebuilt=group([x,y])
assert len(rebuilt)==46656
assert {key(g) for g in rebuilt}=={key(g) for g in pure}
assert len({key(g) for g in pure})==len(pure)
qa,qb=block(a,IQ),block(b,IQ)
qx,qy=mp(qa,2),mp(qb,2)
Q=group([qa,qb]);Qpure=group([qx,qy])
assert len(Q)==96 and len(Qpure)==8
assert np.array_equal(mp(qx,2),I6) and np.array_equal(mp(qy,2),I6)
assert np.array_equal(mp(mm(qx,qy),4),I6)
assert not np.array_equal(mp(mm(qx,qy),2),I6)

wmats=pure[:,IW,:][:,:,IW]
qmats=pure[:,IQ,:][:,:,IQ]
wid=np.all(wmats==I6,axis=(1,2))
qid=np.all(qmats==I6,axis=(1,2))
kernel=pure[wid&qid]
assert len(kernel)==3
n=next(g for g in kernel if not np.array_equal(g,I))
assert np.array_equal(mp(n,3),I)
assert np.array_equal((n-I)@(n-I)%3,np.zeros_like(I))
z3=mp(mm(a,b),3)
assert np.array_equal(mp(z3,4),n)
assert np.array_equal(mp(z3,12),I)
assert not np.array_equal(mp(z3,6),I)
conjugation=[]
for g in [a,b,c,x,y]:
    v=mm(mm(g,n),inv(g))
    conjugation.append(next((j for j in [1,2] if np.array_equal(v,mp(n,j))),None))

diagonal_keys={key(np.concatenate([w,q],axis=0)) for w,q in zip(wmats,qmats)}
assert len(diagonal_keys)==1944*8
assert len({key(g) for g in wmats})==1944
assert len({key(g) for g in qmats})==8

filtered=np.load(PENTAGON/'krammer_exact_first_pair.npz')
candidates=filtered['candidates'].astype(np.int16)
labels=filtered['labels'].tolist()
assert len(candidates)==18
assert all(np.array_equal(block(g,IQ),I6) for g in candidates)
# Reconstruct the six W values from D23.P3, independently of the labels in the
# candidate file.  Frobenius contragredient over F9 becomes inverse transpose
# after restriction of scalars to F3.
P=to3([[7,7,2],[8,7,3],[2,8,1]])
Pi=inv(P)
def add9(u,v):return (u%3+v%3)%3+3*((u//3+v//3)%3)
def neg9(u):return (-u%3)%3+3*(-(u//3)%3)
def mul9(u,v):return ((u%3)*(v%3)-(u//3)*(v//3))%3+3*(((u%3)*(v//3)+(u//3)*(v%3))%3)
def inverse9(u):return next(v for v in range(1,9) if mul9(u,v)==1)
allowed_W={}
for rho in range(3):
    for a3 in range(2):
        eps=1 if a3==0 else 2
        d1=mul9((1-rho-eps)%3,inverse9(4))
        d2=mul9(add9(rho,3),d1)
        eta=to3([[1,rho,d1],[rho,(1+rho*rho)%3,d2],[0,0,1]])
        target=mm(mm(P,inv(eta).T),Pi)
        allowed_W[key(target)]=[rho,a3]
independent_candidates=[]
independent_labels=[]
for g,w,ok in zip(pure,wmats,qid):
    lab=allowed_W.get(key(w))
    if ok and lab is not None:
        independent_candidates.append(g);independent_labels.append(lab)
assert len(independent_candidates)==18
assert {key(g) for g in independent_candidates}=={key(g) for g in candidates}
for g,lab in zip(candidates,labels):assert allowed_W[key(block(g,IW))]==lab
rows=[]
two_cycle=[]
two_cycle_labels=[]
s=mm(mm(a,b),a)
for rho in range(3):
    for a3 in range(2):
        group_candidates=[g for g,l in zip(candidates,labels) if l==[rho,a3]]
        assert len(group_candidates)==3
        seed=group_candidates[0]
        assert {key(g) for g in group_candidates}=={key(mm(seed,mp(n,j))) for j in range(3)}
        good=[g for g in group_candidates if np.array_equal(mm(mm(mm(s,g),s),g),mm(s,s))]
        assert len(good)==1
        two_cycle.append(good[0]);two_cycle_labels.append([rho,a3])
        rows.append({'rho':rho,'a3':a3,'unique_two_cycle_matrix_F9':f9(good[0])})
np.savez_compressed(HERE/'krammer_six_first_pair.npz',candidates=np.array(two_cycle,dtype=np.int8),labels=np.array(two_cycle_labels,dtype=np.int8))

out={
    'field':'F3[i], i^2=-1, encoding a+3b',
    'quotient_generators_F9':[f9(qa),f9(qb)],
    'quotient_full_order':len(Q),'quotient_pure_order':len(Qpure),
    'quotient_pure_presentation':'<X,Y | X^2=Y^2=(XY)^4=1>, |XY|=4: dihedral order8',
    'diagonal_image_order':len(diagonal_keys),'full_pure_order':len(pure),
    'kernel_order':len(kernel),'kernel_generator_F9':f9(n),
    'kernel_generator_intrinsic':'((K1 K2)^3)^4; the B3 full twist has order12',
    'kernel_generator_minus_identity_F9':f9((n-I)%3),
    'kernel_conjugation_exponents_sigma1_sigma2_sigma3_X_Y':conjugation,
    'actual_gentle_necessary_candidates_before_two_cycle':18,
    'actual_gentle_necessary_candidates_after_two_cycle':6,
    'candidate_fibers':rows,
    'scope':'Exact finite matrix computations. Candidate lifts to profinite gentle elements are not asserted.'
}
dest=HERE/'krammer_quotient_extension.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='candidate_fibers'},indent=2))
