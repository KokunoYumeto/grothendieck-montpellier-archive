"""Finite certificates for SA27-C236 and SA27-C241.

Pure Python; no external algebra library. Both examples and their hypotheses are
specified independently in proof_checks.md. Output is evidence, not a substitute
for those arguments. The tetrahedron certificate is over Q and F_2; the integral
homotopy type uses the explicit barycentric-subdivision identification.
"""
from itertools import combinations
from fractions import Fraction
import json
from pathlib import Path

def rank(rows,p=None):
    if not rows: return 0
    a=[[x%p if p else Fraction(x) for x in row] for row in rows]
    nr,nc=len(a),len(a[0]); k=0
    for j in range(nc):
        piv=next((i for i in range(k,nr) if a[i][j]),None)
        if piv is None: continue
        a[k],a[piv]=a[piv],a[k]
        inv=pow(int(a[k][j]),-1,p) if p else 1/a[k][j]
        a[k]=[(x*inv)%p if p else x*inv for x in a[k]]
        for i in range(nr):
            if i==k or not a[i][j]: continue
            q=a[i][j]
            a[i]=[(x-q*y)%p if p else x-q*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==nr: break
    return k

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

# C_2 regular representation in basis (1,g), with trivial one-dimensional ends.
g=[[0,1],[1,0]]; inject=[[1],[1]]; augment=[[1,1]]
assert matmul(g,inject)==inject
assert matmul(augment,g)==augment
assert all(x%2==0 for row in matmul(augment,inject) for x in row)
# Coinvariant quotient q=k[C_2] -> k sends both basis vectors to 1.
q=[[1,1]]
induced_inject=[[sum(row)%2] for row in matmul(q,inject)]
assert induced_inject==[[0]]
induced_augment=[[1]]
orig_ranks=[rank(inject,2),rank(augment,2)]
coinv_ranks=[rank(induced_inject,2),rank(induced_augment,2)]
coinv={
 'claim':'SA27-C236','field':'F_2','group':'C_2','indexing_functor':'B C_2 -> terminal category',
 'original_dimensions':[1,2,1], 'original_differentials':[inject,augment],
 'maps_are_C2_equivariant':True, 'd_squared_zero':True, 'original_ranks':orig_ranks,
 'original_homology_dimensions':[1-orig_ranks[0],2-sum(orig_ranks),1-orig_ranks[1]],
 'coinvariant_dimensions':[1,1,1],'coinvariant_differentials':[induced_inject,induced_augment],
 'coinvariant_ranks':coinv_ranks,
 'coinvariant_homology_dimensions':[1-coinv_ranks[0],1-sum(coinv_ranks),1-coinv_ranks[1]],
 'conclusion':'A monomorphism becomes zero; an acyclic three-term complex becomes nonacyclic.'}

# Face poset of boundary of a tetrahedron: nonempty proper subsets of {0,1,2,3}.
faces=[frozenset(c) for k in (1,2,3) for c in combinations(range(4),k)]
chains={0:[(f,) for f in faces]}
for k in (1,2):
    chains[k]=[c+(f,) for c in chains[k-1] for f in faces if c[-1]<f]
def boundary(k):
    if k==0:return []
    ids={c:i for i,c in enumerate(chains[k-1])}
    m=[[0]*len(chains[k]) for _ in chains[k-1]]
    for j,c in enumerate(chains[k]):
        for t in range(k+1):m[ids[c[:t]+c[t+1:]]][j]+=(-1)**t
    return m
d1,d2=boundary(1),boundary(2)
assert not any(x for r in matmul(d1,d2) for x in r)
def homology(p):
    r1,r2=rank(d1,p),rank(d2,p)
    return {'boundary_ranks':[r1,r2],'betti_numbers':[len(chains[0])-r1,len(chains[1])-r1-r2,len(chains[2])-r2]}
poset={'claim':'SA27-C241','objects':[sorted(f) for f in faces],
 'nerve_nondegenerate_simplex_counts':[len(chains[i]) for i in range(3)],
 'morphism_count_including_identities':len(faces)+len(chains[1]),
 'chain_complex_condition':True,'rational_homology':homology(None),'F2_homology':homology(2),
 'topological_identification':'The order complex is the barycentric subdivision of the boundary of the standard tetrahedron, hence S^2.',
 'limit_of_certificate':'Homology ranks do not prove simple connectivity. The displayed triangulation identification proves it and the integral H^2=Z statement used in proof_checks.md.'}
out={'coinvariants':coinv,'tetrahedron_face_poset':poset}
assert coinv['original_homology_dimensions']==[0,0,0]
assert coinv['coinvariant_homology_dimensions']==[1,0,0]
assert poset['rational_homology']['betti_numbers']==[1,0,1]
assert poset['F2_homology']['betti_numbers']==[1,0,1]
base=Path(__file__).resolve().parent
(base/'computation_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
