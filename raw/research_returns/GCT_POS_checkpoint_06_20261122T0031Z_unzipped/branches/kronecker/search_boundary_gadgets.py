"""Exploratory nonuniform-margin incidence-basis search.

A gadget has local size q.  Vertex0 in each part has margin r, the
remaining q-1 vertices have margin1.  Replacing an edge of mass r in
a previously balanced support by this gadget adds q-1 dimensions.
Every reported solution is checked by integer arithmetic.  Search is
not exhaustive, and only nondegenerate vertices are traversed.
"""
import argparse,itertools,json,math,time
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser()
p.add_argument('--q',type=int,default=4)
p.add_argument('--den',type=int,default=16)
p.add_argument('--steps',type=int,default=100000)
p.add_argument('--seed',type=int,default=20261121)
p.add_argument('--out',required=True)
a=p.parse_args();q=a.q;rank=3*q-2;D=a.den
edges=list(itertools.product(range(q),repeat=3));edge_index={e:i for i,e in enumerate(edges)}
full=np.zeros((3*q,q**3),dtype=np.int64)
for j,e in enumerate(edges):
    for h,v in enumerate(e):full[h*q+v,j]=1
rows=list(range(q))+list(range(q,2*q-1))+list(range(2*q,3*q-1))
A=full[rows]
initial=sorted(edge_index[e] for i in range(q-1) for e in [(i,i,i+1),(i,i+1,i),(i+1,i,i)])+[edge_index[(q-1,)*3]]
rng=np.random.default_rng(a.seed);basis=initial.copy();seen=set();best=-1;records=[]
start=time.time();numerator=1
def save(done):
    Path(a.out).write_text(json.dumps({'scope':'Nonexhaustive nonuniform-margin basis search; reported integer identities exact',
       'q':q,'parameter_denominator':D,'steps':done,'records':records,'elapsed':time.time()-start},indent=2))
for step in range(a.steps):
    if step%250==0:
        numerator=int(rng.choice(list(range(1,D,2))));basis=initial.copy();seen.clear()
    rhsfull=np.array([numerator if i%q==0 else D for i in range(3*q)],dtype=np.int64)
    rhs=rhsfull[rows]
    inv=np.linalg.inv(A[:,basis]);det=round(np.linalg.det(A[:,basis]));x=inv@rhs
    if min(x)<1e-8:
        basis=initial.copy();continue
    U=inv@A
    ratios=np.divide(x[:,None],U,out=np.full(U.shape,np.inf),where=U>1e-9)
    leaving=np.argmin(ratios,axis=0);theta=ratios[leaving,np.arange(q**3)]
    choices=[]
    for j in range(q**3):
        if j in basis:continue
        i=leaving[j];dd=round(det*U[i,j])
        if not dd:continue
        y=x-theta[j]*U[:,j];y[i]=theta[j]
        if min(y)<1e-8:continue
        nb=basis.copy();nb[i]=j;key=tuple(sorted(nb))
        if key in seen:continue
        den=abs(dd)*D
        nums=np.rint(y*abs(dd)).astype(np.int64)
        if not np.array_equal(full[:,nb]@nums,rhsfull*abs(dd)):continue
        gcd=math.gcd(den,*list(map(int,nums)));d=den//gcd
        v=(d&-d).bit_length()-1
        score=v+float(rng.gumbel())*0.8
        choices.append((score,key,d,v))
    if not choices:
        basis=initial.copy();seen.clear();continue
    _,key,d,v=max(choices,key=lambda z:z[0]);basis=list(key);seen.add(key)
    if v>best:
        x=np.linalg.solve(A[:,basis],rhs)
        nums=np.rint(x*d/D).astype(np.int64)
        assert np.array_equal(full[:,basis]@nums,rhsfull*d//D) and np.all(nums>0)
        es=[edges[j] for j in basis]
        free=all(len(set((e[i],e[j]) for e in es))==len(es) for i,j in [(0,1),(0,2),(1,2)])
        best=v;record={'step':step,'parameter':[numerator,D],'denominator':d,'v2':v,
           'amplification_v2':v-(D&-D).bit_length()+1,'support':es,'numerators':list(map(int,nums)),
           'basis_determinant':round(np.linalg.det(A[:,basis])),'free':free}
        records.append(record);print(json.dumps(record),flush=True);save(step+1)
        if v>(D&-D).bit_length()-1+q-1:
            print('POTENTIAL SUPERDOUBLING GADGET',flush=True);break
    if step%10000==9999:print(json.dumps({'progress':step+1,'best_v2':best,'seconds':time.time()-start}),flush=True)
save(step+1)
