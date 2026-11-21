"""Exact integral reflections killing every full-rank survivor boundary face.

Uses only hard-coded integer data and the Python standard library.
This proves the localized chains are cycles, not that they are nonboundaries.
"""
from fractions import Fraction
from pathlib import Path
import json

vectors=[[int(i==j) for i in range(9)] for j in range(9)]+[
 [-1,-1,0,-1,-1,-2,-2,-2,-3],
 [-1,0,-1,-1,-1,-1,-2,-2,-3],
 [0,-1,-1,-1,-2,-2,-2,-3,-3],
]
# Each row: removed index, swapped indices, common sign, integral functional.
# Vector indices in this table are one based.
table=[
 (1,4,12,1,[-1,0,0,1,0,0,0,0,0]),
 (2,3,5,1,[0,1,1,0,-1,0,0,0,0]),
 (3,2,5,1,[0,1,1,0,-1,0,0,0,0]),
 (4,1,5,-1,[1,0,0,-2,1,0,0,0,0]),
 (5,1,7,1,[1,0,0,0,1,0,-1,0,0]),
 (6,2,4,-1,[0,1,0,1,0,-1,0,0,0]),
 (7,1,5,-1,[1,0,0,0,1,0,-1,0,0]),
 (8,1,9,1,[1,0,0,0,0,0,0,1,-1]),
 (9,1,8,-1,[1,0,0,0,0,0,0,1,-1]),
 (10,1,11,1,[1,0,0,0,0,0,0,0,0]),
 (11,1,10,1,[1,0,0,0,0,0,0,0,0]),
 (12,1,4,1,[1,0,0,-1,0,0,0,0,0]),
]

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def rank(rows):
    a=[[Fraction(x) for x in row] for row in rows];k=0
    for j in range(len(a[0])):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None:continue
        a[p],a[k]=a[k],a[p]
        s=a[k][j];a[k]=[x/s for x in a[k]]
        for i in range(k+1,len(a)):
            s=a[i][j]
            a[i]=[x-s*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

verified=[]
for removed,j,k,eps,phi in table:
    r,j0,k0=removed-1,j-1,k-1
    assert len({r,j0,k0})==3
    keep=[v for i,v in enumerate(vectors) if i!=r]
    assert rank(keep)==9
    u=[eps*x-y for x,y in zip(vectors[k0],vectors[j0])]
    assert dot(phi,vectors[j0])==1 and dot(phi,vectors[k0])==-eps
    assert all(dot(phi,v)==0 for i,v in enumerate(vectors) if i not in {r,j0,k0})
    assert dot(phi,u)==-2
    g=[[int(a==b)+u[a]*phi[b] for b in range(9)] for a in range(9)]
    assert all(sum(g[a][c]*g[c][b] for c in range(9))==int(a==b) for a in range(9) for b in range(9))
    for i,v in enumerate(vectors):
        if i==r:continue
        expected=[eps*x for x in vectors[k0 if i==j0 else j0]] if i in {j0,k0} else v
        assert [dot(row,v) for row in g]==expected
    verified.append({'removed_one_based':removed,'swap_one_based':[j,k],'vector_sign':eps,'functional':phi,'integral_involution':g,'quadratic_ray_sign':-1})
result={
 'date':'2026-11-21','scope':'Every full-rank facet has an explicit integral odd ray permutation; localized chains are cycles. No claim that either is a nonboundary.',
 'rank9_cycle_projective_degree':11,'rank10_cycle_projective_degree':12,
 'verified_full_rank_facets':verified,
 'rank10_additional_facet':'Deleting the orthogonal last vector gives rank9 in ambient rank10 and lies in the relative boundary.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'verified_facets':len(verified),'all_integral_involutions':True,'all_ray_signs':-1,'rank9_is_localized_cycle':True,'rank10_is_localized_cycle':True,'nonboundary_claim':False},indent=2))
