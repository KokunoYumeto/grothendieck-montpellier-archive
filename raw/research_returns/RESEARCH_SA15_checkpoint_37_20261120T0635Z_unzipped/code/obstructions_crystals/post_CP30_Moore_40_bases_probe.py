"""Exact finite F4 probe of 40 stabilizer-basis necessary Moore conditions.

This does not identify the actual Cartier parameter surface.  An equality
of finite point sets is not used as a geometric classification theorem.
For selected exceptional parameters the determinant is expanded as an
actual polynomial in all nine indeterminates, not sampled in x.
"""
from pathlib import Path
from itertools import product, permutations
from datetime import datetime, timezone
import json, time
import numpy as np

start=time.perf_counter()
mul=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
inv=[0,1,3,2]
zeta=[1,2,3]
points=list(product(range(3),repeat=2))
index={v:i for i,v in enumerate(points)}
def add(u,v): return tuple((a+b)%3 for a,b in zip(u,v))
def neg(u): return tuple(-a%3 for a in u)
def scale(t,u): return tuple(t*a%3 for a in u)
def dot(u,v): return sum(a*b for a,b in zip(u,v))%3
def normalize(row):
    row=tuple(int(v) for v in row)
    if not any(row): return None
    first=next(v for v in row if v)
    return tuple(int(mul[inv[first],v]) for v in row)
def pack(row): return sum(int(v)<<(2*i) for i,v in enumerate(row))
def rank(rows):
    work=[list(map(int,r)) for r in rows]
    lead=0
    for j in range(9):
        pivot=next((i for i in range(lead,len(work)) if work[i][j]),None)
        if pivot is None: continue
        work[lead],work[pivot]=work[pivot],work[lead]
        factor=inv[work[lead][j]]
        work[lead]=[int(mul[factor,x]) for x in work[lead]]
        for i in range(len(work)):
            if i!=lead and work[i][j]:
                f=work[i][j]
                work[i]=[x^int(mul[f,y]) for x,y in zip(work[i],work[lead])]
        lead+=1
        if lead==len(work): break
    return lead

# Computational basis, 27 full-support quadratic bases, 12 affine-line bases.
bases=[('coordinate',np.eye(9,dtype=np.uint8))]
for quad in product(range(3),repeat=3):
    rows=[]
    for lin in points:
        rows.append([zeta[(quad[0]*a*a+quad[1]*a*b+quad[2]*b*b+dot(lin,(a,b)))%3]
                     for a,b in points])
    bases.append(('quadratic_'+''.join(map(str,quad)),np.array(rows,dtype=np.uint8)))
directions=[(1,0),(0,1),(1,1),(1,2)]
for u in directions:
    remaining=set(points);cosets=[]
    while remaining:
        origin=min(remaining)
        coset=[add(origin,scale(t,u)) for t in range(3)]
        cosets.append(coset);remaining.difference_update(coset)
    for q in range(3):
        rows=[]
        for coset in cosets:
            for lin in range(3):
                row=[0]*9
                for t,a in enumerate(coset): row[index[a]]=zeta[(q*t*t+lin*t)%3]
                rows.append(row)
        bases.append(('line_'+''.join(map(str,u))+'_'+str(q),np.array(rows,dtype=np.uint8)))
assert len(bases)==40
assert all(rank(rows)==9 for _,rows in bases)
normalized_bases={tuple(sorted(pack(normalize(r)) for r in rows)) for _,rows in bases}
assert len(normalized_bases)==40

vectors=[]
for first in range(9):
    for tail in product(range(4),repeat=8-first):
        vectors.append((0,)*first+(1,)+tail)
all_vectors=np.array(vectors,dtype=np.uint8)
assert len(vectors)==(4**9-1)//3
remaining=all_vectors
steps=[]
for name,basis in bases:
    values=np.zeros((len(remaining),9),dtype=np.uint8)
    for j in range(9):
        values ^= mul[remaining[:,j,None],basis[None,:,j]]
    remaining=remaining[np.any(values==0,axis=1)]
    steps.append({'basis':name,'remaining_projective_F4_points':len(remaining)})
necessary={pack(v):tuple(map(int,v)) for v in remaining}

# The 81 translated phased alternating four-dimensional vector subspaces.
known=set();plane_sizes=[];plane_rows=[]
for center,phase in product(points,repeat=2):
    plane=set()
    for values in product(range(4),repeat=4):
        row=[0]*9
        for u,value in zip(directions,values):
            row[index[add(center,neg(u))]]=value
            row[index[add(center,u)]]=int(mul[zeta[dot(phase,u)],value])
        normalized=normalize(row)
        if normalized is not None: plane.add(pack(normalized))
    assert len(plane)==(4**4-1)//3
    known.update(plane);plane_sizes.append(len(plane))
    plane_rows.append({'center':center,'phase':phase,'projective_points':sorted(plane)})
outside=sorted(set(necessary)-known)
missing=sorted(known-set(necessary))

plus=[[index[add(a,b)] for b in points] for a in points]
minus=[[index[add(a,neg(b))] for b in points] for a in points]
def exact_det(c):
    coefficients={}
    nonzero_terms=0
    for perm in permutations(range(9)):
        coeff=1;monomial=0
        for i,j in enumerate(perm):
            coeff=int(mul[coeff,c[minus[i][j]]])
            if coeff==0: break
            monomial += 1<<(4*plus[i][j])
        if coeff:
            nonzero_terms+=1
            coefficient=coefficients.get(monomial,0)^coeff
            if coefficient: coefficients[monomial]=coefficient
            else: coefficients.pop(monomial,None)
    return coefficients,nonzero_terms

selected=[]
for code in outside[:3]:
    c=necessary[code]
    coefficients,terms=exact_det(c)
    selected.append({'parameter':c,'packed':code,
                     'determinant_identically_zero':not coefficients,
                     'uncancelled_monomials':len(coefficients),
                     'nonzero_permutation_terms':terms,
                     'coefficients':{hex(m):v for m,v in sorted(coefficients.items())}})
known_code=min(known)
known_parameter=tuple((known_code>>(2*j))&3 for j in range(9))
known_det,known_terms=exact_det(known_parameter)
assert not known_det
out={
    'status':'EXACT_FINITE_PROBE_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-start,
    'projective_F4_parameters':len(vectors),'distinct_invertible_bases':len(bases),
    'basis_steps':steps,'necessary_F4_points':len(necessary),
    'known_alternating_union_F4_points':len(known),
    'outside_known_union':len(outside),'known_missing_necessary':len(missing),
    'selected_exact_polynomial_determinants':selected,
    'known_polynomial_check':{'parameter':known_parameter,'identically_zero':True,
                              'nonzero_permutation_terms':known_terms},
    'remaining_parameters':[{ 'packed':code,'parameter':v} for code,v in sorted(necessary.items())],
    'known_planes':plane_rows,
    'scope':'The 40 invertible F4 stabilizer bases and their finite projective zero sets are computed exactly. For selected outside points all 9! determinant permutation terms are collected as a polynomial in nine independent x variables. Finite point equality, if any, is not a geometric classification; Clifford covariance and the actual Cartier theta-parameter identification still require separate proofs. No fixed-surface or monodromy conclusion.'
}
path=Path(__file__).with_suffix('.output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','projective_F4_parameters',
      'distinct_invertible_bases','necessary_F4_points','known_alternating_union_F4_points',
      'outside_known_union','known_missing_necessary')}))
print(json.dumps([{'parameter':r['parameter'],'zero':r['determinant_identically_zero'],
                   'monomials':r['uncancelled_monomials']} for r in selected]))
