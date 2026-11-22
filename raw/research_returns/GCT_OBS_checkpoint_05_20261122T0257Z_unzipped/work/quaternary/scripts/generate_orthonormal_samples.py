#!/usr/bin/env python3
"""Centered determinant or padded-nonic samples with normalized second tensor I3.

Pure standard-library arithmetic modulo101. Determinant samples are obtained
by an explicit congruence of the trace Gram matrix. Padded samples have the
exact integer-lift definition F=(x0+l)Q8, with F0=1,F1=0,F2=36 sum xi^2.
All normalized tensor coordinates of orders2 through9 are retained.
"""
import argparse
import hashlib
import json
from time import monotonic
from centered_det9_sampler import (Generator, determinant, dense_coefficients,
                                  pencil_at, polynomial_at, polynomial_product,
                                  tensor_normalization)


P=101
ROOTS={}
for _r in range(P):ROOTS.setdefault(_r*_r%P,_r)
COORDINATES=[(j,a,b,j-a-b) for j in range(2,10)
             for a in range(j+1) for b in range(j-a+1)]


def inner(q,u,v):
    return sum(u[i]*q[i][j]*v[j] for i in range(3) for j in range(3))%P


def trace_gram(matrices):
    inverse=pow(72,P-2,P)
    return [[-inverse*sum(matrices[i][a][b]*matrices[j][b][a]
                         for a in range(9) for b in range(9))%P
             for j in range(3)] for i in range(3)]


def orthonormalizer(q):
    """Return h with h^T q h=I if q is nonsingular with square determinant."""
    discriminant=determinant(q,P)
    if not discriminant or discriminant not in ROOTS:return None
    vectors=[[int(i==j) for i in range(3)] for j in range(3)]
    diagonal=[]
    for k in range(3):
        pivot=next((i for i in range(k,3) if inner(q,vectors[i],vectors[i])),None)
        if pivot is None:
            pair=next((i,j) for i in range(k,3) for j in range(i+1,3)
                      if inner(q,vectors[i],vectors[j]))
            i,j=pair;vectors[i]=[(x+y)%P for x,y in zip(vectors[i],vectors[j])]
            pivot=i
        vectors[k],vectors[pivot]=vectors[pivot],vectors[k]
        d=inner(q,vectors[k],vectors[k]);assert d
        diagonal.append(d);inverse=pow(d,P-2,P)
        for i in range(k+1,3):
            scalar=inner(q,vectors[k],vectors[i])*inverse%P
            vectors[i]=[(a-scalar*b)%P for a,b in zip(vectors[i],vectors[k])]
    nonsquares=[i for i,d in enumerate(diagonal) if d not in ROOTS]
    assert len(nonsquares) in (0,2)
    normalized=[None]*3
    for i,d in enumerate(diagonal):
        if d in ROOTS:
            inverse=pow(ROOTS[d],P-2,P)
            normalized[i]=[inverse*x%P for x in vectors[i]]
    if nonsquares:
        i,j=nonsquares;a,b=diagonal[i],diagonal[j];inverse_a=pow(a,P-2,P)
        for y in range(P):
            rhs=(1-b*y*y)*inverse_a%P
            if rhs in ROOTS:
                x=ROOTS[rhs];break
        else:raise AssertionError('nondegenerate binary form represents1')
        inverse_root=pow(ROOTS[a*b%P],P-2,P)
        normalized[i]=[(x*u+y*v)%P for u,v in zip(vectors[i],vectors[j])]
        normalized[j]=[(-b*y*u+a*x*v)*inverse_root%P
                       for u,v in zip(vectors[i],vectors[j])]
    h=[[normalized[j][i] for j in range(3)] for i in range(3)]
    assert all(inner(q,normalized[i],normalized[j])==int(i==j)
               for i in range(3) for j in range(3))
    assert determinant(h,P)
    return h


def transform(matrices,h):
    out=[]
    for j in range(3):
        a=[[sum(h[k][j]*matrices[k][r][c] for k in range(3))%P
            for c in range(9)] for r in range(9)]
        a[-1][-1]=-sum(a[i][i] for i in range(8))
        out.append(a)
    assert all(sum(a[i][i] for i in range(9))==0 for a in out)
    return out


def check_identity_second(tensors):
    assert all(v==int(max(alpha)==2) for alpha,v in tensors[2].items())


def determinant_sample(generator):
    rejected=0
    while True:
        state=generator.state
        matrices=[generator.traceless(9) for _ in range(3)]
        q=trace_gram(matrices);h=orthonormalizer(q)
        if h is not None:break
        rejected+=1
    transformed=transform(matrices,h)
    assert trace_gram(transformed)==[[int(i==j) for j in range(3)] for i in range(3)]
    coefficients=dense_coefficients(transformed,P)
    assert coefficients[(0,0,0)]==1
    assert all(coefficients.get(alpha,0)==0 for alpha in ((1,0,0),(0,1,0),(0,0,1)))
    tensors=tensor_normalization(coefficients,P,9);check_identity_second(tensors)
    probes=Generator(state^0x9e3779b9,P);checks=[]
    for _ in range(3):
        point=tuple(probes.next() for _ in range(3))
        direct=determinant(pencil_at(transformed,point,P),P)
        reconstructed=polynomial_at(coefficients,point,P)
        assert direct==reconstructed
        checks.append(list(point)+[direct])
    source=dict(matrices=transformed,raw_gram=q,change_of_basis=h)
    return tensors,source,checks,state,rejected


def padded_sample(generator):
    state=generator.state
    linear=[generator.next() for _ in range(3)]
    l={(1,0,0):linear[0],(0,1,0):linear[1],(0,0,1):linear[2]}
    forms={0:{(0,0,0):1},1:{},2:{(2,0,0):36,(0,2,0):36,(0,0,2):36}}
    for j in range(3,9):
        forms[j]={(a,b,j-a-b):generator.next() for a in range(j+1) for b in range(j-a+1)}
    powers=[{(0,0,0):1}]
    for _ in range(9):powers.append(polynomial_product(powers[-1],l,P))
    last=dict(powers[9])
    for j in range(2,9):
        sign=(-1)**j
        for alpha,c in polynomial_product(powers[9-j],forms[j],P).items():
            last[alpha]=(last.get(alpha,0)+sign*c)%P
    forms[9]=last
    coefficients={alpha:c for form in forms.values() for alpha,c in form.items()}
    tensors=tensor_normalization(coefficients,P,9);check_identity_second(tensors)
    probes=Generator(state^0x9e3779b9,P);checks=[]
    for _ in range(3):
        point=tuple(probes.next() for _ in range(3));x0=probes.next()
        lv=sum(x*y for x,y in zip(linear,point))%P
        fj=[polynomial_at(forms[j],point,P) for j in range(10)]
        remainder=sum(fj[j]*pow(-lv,9-j,P) for j in range(10))%P
        assert remainder==0
        quotient=[1]
        for j in range(1,9):quotient.append((fj[j]-lv*quotient[-1])%P)
        direct=sum(fj[j]*pow(x0,9-j,P) for j in range(10))%P
        factored=(x0+lv)*sum(quotient[j]*pow(x0,8-j,P) for j in range(9))%P
        assert direct==factored
        checks.append([x0,*point,direct,factored,remainder])
    source=dict(linear=linear,ordinary_forms={str(j):[[list(a),c] for a,c in forms[j].items()]
                                             for j in range(2,9)},
                exact_last_form='F9=l^9+sum(j=2..8)(-1)^j l^(9-j)Fj overZ')
    return tensors,source,checks,state,0


def generate(kind,samples,seed,path):
    started=monotonic();generator=Generator(seed,P)
    function=determinant_sample if kind=='determinant' else padded_sample
    rows=[];checks=[];states=[];rejections=0;source_hash=hashlib.sha256();first=None
    for i in range(samples):
        tensors,source,sanity,state,rejected=function(generator)
        rows.append([tensors[j][(a,b,c)] for j,a,b,c in COORDINATES])
        checks.append(sanity);states.append(state);rejections+=rejected
        source_hash.update((json.dumps(source,separators=(',',':'))+'\n').encode())
        if first is None:first=source
    tensor_hash=hashlib.sha256(bytes(v for row in rows for v in row)).hexdigest()
    data=dict(prime=P,kind=kind,seed=seed,samples=samples,coordinates=COORDINATES,
              normalized_tensors=rows,second_tensor='identity3x3 exactly modulo101',
              normalization='T_alpha=ordinary coefficient*(9-j)! alpha!/9! mod101',
              generator='s<-1664525s+1013904223 mod2^32; value=(s>>16) mod101',
              accepted_generator_states=states,rejected_source_pencils=rejections,
              source_sha256=source_hash.hexdigest(),normalized_tensors_sha256=tensor_hash,
              sanity=checks,first_source=first)
    encoded=(json.dumps(data,separators=(',',':'))+'\n').encode()
    with open(path,'wb') as f:f.write(encoded)
    manifest=dict(file=path,file_sha256=hashlib.sha256(encoded).hexdigest(),kind=kind,
                  samples=samples,coordinates=len(COORDINATES),sanity_checks=3*samples,
                  source_sha256=source_hash.hexdigest(),normalized_tensors_sha256=tensor_hash,
                  rejected_source_pencils=rejections,seconds=round(monotonic()-started,3))
    with open(path+'.manifest.json','w') as f:json.dump(manifest,f,indent=2);f.write('\n')
    return manifest


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind',choices=('determinant','padded'),required=True)
    parser.add_argument('--samples',type=int,required=True)
    parser.add_argument('--seed',type=int,default=20261122)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    print(json.dumps(generate(args.kind,args.samples,args.seed,args.output)),flush=True)
