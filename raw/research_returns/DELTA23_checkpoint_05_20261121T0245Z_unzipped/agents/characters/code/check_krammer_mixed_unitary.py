#!/usr/bin/env python3
"""Exact invariant spaces and unitary groups for two mixed Krammer pairs."""
import json
import itertools
from pathlib import Path
import numpy as np
from sympy.combinatorics import PermutationGroup
import krammer_mixed_structure as k


def rref3(a):
    a=np.array(a,dtype=np.int64,copy=True)%3
    r=0;p=[]
    for j in range(a.shape[1]):
        i=next((i for i in range(r,len(a)) if a[i,j]),None)
        if i is None:continue
        a[[r,i]]=a[[i,r]]
        a[r]=a[r]*pow(int(a[r,j]),-1,3)%3
        for i in range(len(a)):
            if i!=r and a[i,j]:a[i]=(a[i]-a[i,j]*a[r])%3
        p.append(j);r+=1
        if r==len(a):break
    return a,p


def null3(a):
    a,p=rref3(a);out=[]
    for j in range(a.shape[1]):
        if j in p:continue
        v=np.zeros(a.shape[1],dtype=np.int64);v[j]=1
        for i,c in enumerate(p):v[c]=-a[i,j]%3
        out.append(v)
    return out


def conj(a):
    a=np.asarray(a);return a%3+3*(-(a//3)%3)


def hermitian_basis(n):
    out=[]
    for i in range(n):
        b=np.zeros((n,n),dtype=np.int64);b[i,i]=1;out.append(b)
    for i in range(n):
        for j in range(i+1,n):
            b=np.zeros((n,n),dtype=np.int64);b[i,j]=b[j,i]=1;out.append(b)
            b=np.zeros((n,n),dtype=np.int64);b[i,j]=3;b[j,i]=6;out.append(b)
    return out


def invariant_hermitian(gs):
    n=len(gs[0]);bs=hermitian_basis(n);columns=[]
    for b in bs:
        col=[]
        for g in gs:
            diff=k.A[k.mm(k.mm(conj(g).T,b),g),k.N[b]]
            col.extend(diff.flatten()%3);col.extend(diff.flatten()//3)
        columns.append(col)
    ns=null3(np.array(columns).T)
    forms=[]
    for coeff in ns:
        form=np.zeros((n,n),dtype=np.int64)
        for c,b in zip(coeff,bs):form=k.A[form,k.M[c,b]]
        forms.append(form)
    return forms


def det3(a):
    result=0
    for i,j,l,s in [(0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,2),(2,1,0,2),(1,0,2,2)]:
        term=k.M[s,k.M[a[0,i],k.M[a[1,j],a[2,l]]]]
        result=k.A[result,term]
    return int(result)


root=Path(__file__).resolve().parents[1]
data=json.loads((root/"records"/"krammer_mixed_structure.json").read_text())
raw=k.kp.matrices(4,3,6)
out={"field":"F3[i], i²=-1, encoding a+3b","pairs":[]}
for row in data["pairs"]:
    module=row["proper_cyclic_submodules"][3]
    w=np.array(module["basis"],dtype=np.int64)
    gs=[np.array(g,dtype=np.int64)[:3,:3] for g in module["adapted_generators"]]
    forms=invariant_hermitian(gs)
    assert len(forms)==1
    form=forms[0]
    assert k.rank(form)==3
    assert np.array_equal(form,conj(form).T)
    assert all(np.array_equal(k.mm(k.mm(conj(g).T,form),g),form) for g in gs)
    norm_one_vectors=0
    for entries in itertools.product(range(9),repeat=3):
        vec=np.array(entries,dtype=np.int64)[:,None]
        norm_value=int(k.mm(k.mm(conj(vec).T,form),vec)[0,0])
        norm_one_vectors += norm_value==1
    assert norm_one_vectors==252
    ps,degree=k.kp.orbit_perm(list(map(k.kp.to3,gs)),np.eye(6,dtype=np.int64),limit=1000)
    group=PermutationGroup(ps);ds=group.derived_series()
    orders=[int(h.order()) for h in ds]
    assert orders==[24192,6048]
    assert int(group.derived_subgroup().derived_subgroup().order())==6048
    dets=[det3(g) for g in gs]
    # U(3,3) has order 3^3(3+1)(3^2-1)(3^3+1)=24192.
    # SU(3,3) has index4; containment plus exact orders proves equality.
    unitary_order=3**3*(3+1)*(3**2-1)*(3**3+1)
    assert int(group.order())==unitary_order
    result={"pair":row["label"],"invariant_space_basis":w.tolist(),
            "restricted_generators":[g.tolist() for g in gs],
            "hermitian_form":form.tolist(),"form_rank":3,
            "form_determinant":det3(form),"generator_determinants":dets,
            "norm_one_vector_count":norm_one_vectors,
            "generator_orders":[int(g.order()) for g in ps],
            "group_order":int(group.order()),"derived_orders":orders,
            "faithful_F3_vector_orbit_degree":degree,
            "original_braid_generator_closure_ranks":[k.rank(np.concatenate([w,k.mm(g,w)],axis=1)) for g in raw],
            "identification":"U(3,3), with perfect derived subgroup SU(3,3)",
            "result":"PASS"}
    out["pairs"].append(result)
    print(json.dumps(result),flush=True)
(root/"records"/"krammer_mixed_unitary.json").write_text(json.dumps(out,indent=2)+"\n")
