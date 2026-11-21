#!/usr/bin/env python3
"""Exact certificate for D23.F25--F26; no finite simple-group library used."""
from pathlib import Path
import json,sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'characters/code'))
import krammer_mixed_structure as k

def bar(a):
    a=np.asarray(a,dtype=np.int64)
    return a%3+3*(-(a//3)%3)

def null3(a):
    a=np.array(a,dtype=np.int64,copy=True)%3
    row=0;piv=[]
    for j in range(a.shape[1]):
        u=next((i for i in range(row,len(a)) if a[i,j]),None)
        if u is None:continue
        a[[row,u]]=a[[u,row]];a[row]=a[row]*pow(int(a[row,j]),-1,3)%3
        for i in range(len(a)):
            if i!=row and a[i,j]:a[i]=(a[i]-a[i,j]*a[row])%3
        piv.append(j);row+=1
        if row==len(a):break
    out=[]
    for j in range(a.shape[1]):
        if j in piv:continue
        v=np.zeros(a.shape[1],dtype=np.int64);v[j]=1
        for i,c in enumerate(piv):v[c]=-a[i,j]%3
        out.append(v)
    return out

def hermitian_forms(gs):
    n=len(gs[0]);bs=[]
    for i in range(n):
        b=np.zeros((n,n),dtype=np.int64);b[i,i]=1;bs.append(b)
    for i in range(n):
        for j in range(i+1,n):
            b=np.zeros((n,n),dtype=np.int64);b[i,j]=b[j,i]=1;bs.append(b)
            b=np.zeros((n,n),dtype=np.int64);b[i,j]=3;b[j,i]=6;bs.append(b)
    columns=[]
    for b in bs:
        col=[]
        for g in gs:
            d=k.A[k.mm(k.mm(bar(g).T,b),g),k.N[b]]
            col.extend(d.flatten()%3);col.extend(d.flatten()//3)
        columns.append(col)
    forms=[]
    for cs in null3(np.array(columns).T):
        f=np.zeros((n,n),dtype=np.int64)
        for c,b in zip(cs,bs):f=k.A[f,k.M[c,b]]
        forms.append(f)
    return forms

def determinant(a):
    a=np.array(a,copy=True);ans=1
    for j in range(len(a)):
        u=next((i for i in range(j,len(a)) if a[i,j]),None)
        if u is None:return 0
        if u!=j:a[[u,j]]=a[[j,u]];ans=k.N[ans]
        ans=k.M[ans,a[j,j]];a[j]=k.M[k.D[a[j,j]],a[j]]
        for i in range(j+1,len(a)):a[i]=k.A[a[i],k.N[k.M[a[i,j],a[j]]]]
    return int(ans)

def projective_normalize(v):
    v=np.asarray(v,dtype=np.int64)
    a=next(int(x) for x in v if x)
    return tuple(map(int,k.M[k.D[a],v]))

def orders(g,limit=100):
    h=np.eye(len(g),dtype=np.int64);eye=h.copy();po=None;scalar=None
    for n in range(1,limit+1):
        h=k.mm(h,g)
        if po is None and np.array_equal(h,k.M[h[0,0],eye]):po=n;scalar=int(h[0,0])
        if np.array_equal(h,eye):return n,po,scalar
    raise RuntimeError('order bound exceeded')

raw=k.kp.matrices(4,3,6);a,b,c=raw
x=k.mm(a,b);y=k.mp(c,2);z=k.inverse(k.mm(x,y));eye=np.eye(6,dtype=np.int64)
forms=hermitian_forms([x,y]);assert len(forms)==1
H=forms[0];assert k.rank(H)==6
assert np.array_equal(H,bar(H).T)
assert all(np.array_equal(k.mm(k.mm(bar(g).T,H),g),H) for g in raw)
assert [determinant(g) for g in raw]==[3,3,3]
assert [determinant(g) for g in [x,y,z]]==[2,2,1]

T=k.mp(y,2);N=k.A[T,k.N[eye]]
assert k.rank(N)==1 and not np.any(k.mm(N,N)) and np.array_equal(k.mp(T,3),eye)
seed=k.basiscols(N)[:,0]
vectors=[projective_normalize(seed)];seen={vectors[0]}
for v in vectors:
    for g in [x,y]:
        w=projective_normalize(k.mm(g,np.array(v)[:,None])[:,0])
        if w not in seen:seen.add(w);vectors.append(w)
assert len(vectors)==22204
assert all(not np.any(k.mm(k.mm(bar(np.array(v)[None,:]),H),np.array(v)[:,None])) for v in vectors)
norm_zero=1
for n in range(2,7):norm_zero=4*9**(n-1)-3*norm_zero
assert norm_zero==177633 and (norm_zero-1)//8==len(vectors)

local=[orders(g) for g in [x,y,z]]
assert local==[(36,36,1),(6,6,1),(6,3,2)]
pair_orders=[(36,6),(6,3),(3,36),(6,36),(3,6),(36,3)]
assert len(set(pair_orders))==6
assert np.array_equal(k.mp(k.mm(k.mm(a,b),c),4),2*eye%3)

uorder=3**15
for j in range(1,7):uorder*=3**j-(-1)**j
result={'statements':['D23.F25','D23.F26'],
 'field':'F3[i], i^2=-1, encoding a+3b',
 'Hermitian_form':H.tolist(),'Hermitian_space_dimension_F3':len(forms),'form_rank':6,
 'braid_determinants':[3,3,3],'orbital_determinants':[2,2,1],
 'transvection_word':'X3^2=K3^4','transvection':T.tolist(),'rank_T_minus_I':1,
 'isotropic_line_seed':list(map(int,seed)),'isotropic_line_orbit':len(vectors),
 'total_isotropic_lines':(norm_zero-1)//8,'all_orbit_lines_isotropic':True,
 'local_orders_projective_orders_scalars':local,'six_ordered_action_orders':pair_orders,
 'U6_order':uorder,'SU6_order':uorder//4,'orbital_group_order':uorder//2,
 'projective_special_unitary_order':uorder//8,
 'z4_minus_identity':True,
 'scope':'Exact matrix and exhaustive vector-orbit certificate. Generation, perfectness, simplicity and Goursat arguments are proved separately in the TeX proof.'}
(HERE/'krammer_orbital_unitary.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed(HERE/'krammer_orbital_isotropic_orbit.npz',vectors=np.array(vectors,dtype=np.uint8))
print(json.dumps({j:result[j] for j in ['isotropic_line_orbit','total_isotropic_lines','local_orders_projective_orders_scalars','U6_order','SU6_order','orbital_group_order']},indent=2),flush=True)
