#!/usr/bin/env python3
"""Independent path-matching and block-Toeplitz check of the R27 finite core.

No author matrix builder, continuant recurrence, or elimination routine is
imported. The uniform insertion and projection-support proof is separate.
"""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import numpy as np

BASE=Path(__file__).resolve().parents[2]
ROOT=BASE/'work/rectangular/border_ternary'
record=json.loads((ROOT/'jacobi_boundary_repair_m17.json').read_text())
stored=np.load(ROOT/'jacobi_boundary_repair_m17.npz')
prime=101
m=17
L=m-1
alpha=record['alpha']
cut=record['cut_edge']
assert cut==8
d0=record['delta_with_zero_cut']
d1=d0[:]
d1[cut]=1
slope=record['change']
assert slope==[[0,1,2],[3,0,4],[0,5,6],[7,8,0]]
units=[(1,0,0,0),(0,1,0,0),(0,0,1,0)]
base_forms=[0,1,0,2]
forms=[]
for b,row in zip(base_forms,slope):
    form={units[b]:1}
    for variable,c in enumerate(row):
        if c:
            exponent=list(units[variable]);exponent[3]=1
            form[tuple(exponent)]=c
    forms.append(form)

def product_polynomials(a,b):
    result={}
    for e,c in a.items():
        for f,d in b.items():
            g=tuple(x+y for x,y in zip(e,f))
            result[g]=(result.get(g,0)+c*d)%prime
    return {e:c for e,c in result.items() if c}

u0,uL,v0,vL=forms
tv0=product_polynomials(product_polynomials(v0,vL),u0)
tvL=product_polynomials(product_polynomials(v0,vL),uL)
tu0=product_polynomials(product_polynomials(u0,uL),v0)
tuL=product_polynomials(product_polynomials(u0,uL),vL)
monomials=[(a,b,m+1-a-b) for a in range(m+1,-1,-1)
           for b in range(m+1-a,-1,-1)]
lookup={v:i for i,v in enumerate(monomials)}
assert monomials==[tuple(x) for x in np.load(ROOT/'jacobi_repair_m17.npz')['monomials'].tolist()]

def build_by_matchings(delta):
    @lru_cache(None)
    def interval(a,b):
        result={}
        if b<a:
            return {(0,0,0,0):1}
        def visit(start,edges):
            occupied={v for e in edges for v in (e,e+1)}
            coefficient=1
            for e in edges:
                coefficient=coefficient*delta[e]%prime
            for v in range(a,b+1):
                if v not in occupied:
                    coefficient=coefficient*alpha[v]%prime
            k=len(edges)
            exponent=(b-a+1-2*k,k,k,0)
            result[exponent]=(result.get(exponent,0)+coefficient)%prime
            for e in range(start,b):
                visit(e+2,edges+(e,))
        visit(a,())
        return {e:c for e,c in result.items() if c}

    matrices=np.zeros((4,len(monomials),8*m+3),dtype=np.int64)
    def add(column,a,b,shift,form,scalar=1):
        polynomial=product_polynomials(interval(a,b),form)
        for exponent,coefficient in polynomial.items():
            mon=tuple(exponent[k]+shift[k] for k in range(3))
            matrices[exponent[3],lookup[mon],column]=(matrices[exponent[3],lookup[mon],column]+scalar*coefficient)%prime
    def edge_product(a,b):
        value=1
        for e in range(a,b):
            value=value*delta[e]%prime
        return value
    for variable in range(3):
        add(variable,0,L,units[variable][:3],{(0,0,0,0):1})
    for i in range(m):
        prefix=edge_product(0,i)
        suffix=edge_product(i,L)
        for variable,unit in enumerate(units):
            x,y,z=unit[:3]
            add(3+3*i+variable,i+1,L,(x,y+i,z),v0)
            add(3+3*i+variable,0,i-1,(x,y,z+L-i),vL,suffix)
            add(3+3*m+3*i+variable,i+1,L,(x,y,z+i),u0,prefix)
            add(3+3*m+3*i+variable,0,i-1,(x,y+L-i,z),uL)
        if i:
            add(6*m+3+i,1,i-1,(0,0,L-i),tv0,2*suffix)
            add(7*m+3+i,1,i-1,(0,L-i,0),tu0,2)
        if i<L:
            add(6*m+3+i,i+1,L-1,(0,i,0),tvL,2)
            add(7*m+3+i,i+1,L-1,(0,0,i),tuL,2*prefix)
    return matrices

zero=build_by_matchings(d0)
one=build_by_matchings(d1)
delta_product=1
for d in d1:
    delta_product=delta_product*d%prime
inverse=pow(delta_product,-1,prime)
negative=[i for i,(a,b,c) in enumerate(monomials) if -m-5<=b-c<=-m+5]
zero[:,negative,:]=one[:,negative,:]*inverse%prime
rows=record['rows'];columns=record['columns']
allowed=set(range(6))|set(range(m-5,m))
assert rows==[i for i,(a,b,c) in enumerate(monomials) if (b-c)%m in allowed]

def column_character(column):
    if column<3:
        return [0,1,-1][column]%m
    if column<3+3*m:
        index,variable=divmod(column-3,3)
        return (index+[0,1,-1][variable])%m
    if column<3+6*m:
        index,variable=divmod(column-3-3*m,3)
        return (-index+[0,1,-1][variable])%m
    if column<3+7*m:
        return (column-3-6*m)%m
    return -(column-3-7*m)%m
assert columns==[j for j in range(8*m+3) if column_character(j) in allowed]
jets=zero[:,rows,:][:,:,columns]
for k in range(3):
    assert np.array_equal(jets[k],stored[f'C{k}']), ('coefficient mismatch',k)

def echelon_rank(matrix):
    a=matrix.copy()%prime
    row_order=list(range(a.shape[0]))
    rank=0
    pivot_rows=[]
    pivot_columns=[]
    pivots=[]
    for j in range(a.shape[1]):
        choices=np.flatnonzero(a[rank:,j])
        if not len(choices):
            continue
        i=rank+int(choices[0])
        if i!=rank:
            a[[i,rank]]=a[[rank,i]]
            row_order[i],row_order[rank]=row_order[rank],row_order[i]
        pivot=int(a[rank,j])
        pivots.append(pivot)
        pivot_rows.append(row_order[rank]);pivot_columns.append(j)
        # Eliminate below without normalizing the pivot row.
        multipliers=a[rank+1:,j]*pow(pivot,-1,prime)%prime
        a[rank+1:,j:]=(a[rank+1:,j:]-multipliers[:,None]*a[rank,j:][None,:])%prime
        rank+=1
        if rank==a.shape[0]:
            break
    residue=1
    for value in pivots:
        residue=residue*value%prime
    return {'rank':rank,'pivot_rows_in_order':pivot_rows,
            'pivot_columns':pivot_columns,'selected_minor_mod101':residue}

checks=[]
height,width=jets[0].shape
for order in range(3):
    toeplitz=np.zeros(((order+1)*height,(order+1)*width),dtype=np.int64)
    for i in range(order+1):
        for j in range(i+1):
            toeplitz[i*height:(i+1)*height,j*width:(j+1)*width]=jets[i-j]
    result=echelon_rank(toeplitz)
    result.update({'order':order,'shape':list(toeplitz.shape),
                   'matrix_sha256':hashlib.sha256(toeplitz.astype('uint8').tobytes()).hexdigest()})
    checks.append(result)
assert [c['rank'] for c in checks]==[84,172,262]
result={'checked_utc':datetime.now(timezone.utc).isoformat(),
        'who':'GPT-6 Astra Pro; root; effort not exposed; CUE_GCT_20261121_R1',
        'status':'PASS','coefficient_method':'Independent direct enumeration of path matchings with unmatched alpha weights, and polynomial multiplication including epsilon as an explicit fourth exponent',
        'all_three_jet_matrices_match':True,'each_jet_shape':[height,width],
        'jet_entry_count':3*height*width,
        'jet_sha256':[hashlib.sha256(jets[k].astype('uint8').tobytes()).hexdigest() for k in range(3)],
        'toeplitz_checks':checks,'valuation_counts_through_order_two':[84,4,2],
        'scope':'Exact finite core only. Uniform insertion, full-column projection support and the border induction are separately read mathematical proofs.'}
(BASE/'work/root/r27_boundary_jet_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='toeplitz_checks'}))
