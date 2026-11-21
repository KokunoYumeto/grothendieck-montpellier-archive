"""Exact standalone certificate: the explicit orientation survivors are boundaries.

Uses only hard-coded integer data and Python's standard library. The proof
that these exact cells bound in the localized Voronoi complex is in
k12_survivor_coface_section.tex. This does not compute either whole homology
group or K12. No numerical discovery output is an input to this verifier.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

def gram_value(q,v):
    return sum(q[i][j]*v[i]*v[j] for i in range(len(v)) for j in range(len(v)))

def matrix_rank(rows):
    a=[[F(x) for x in row] for row in rows]
    k=0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[k]=a[k],a[i]
        p=a[k][j];a[k]=[x/p for x in a[k]]
        for i in range(k+1,len(a)):
            p=a[i][j]
            if p:a[i]=[x-p*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k

def ldl(q):
    n=len(q);lower=[[F(i==j) for j in range(n)] for i in range(n)];diagonal=[]
    for i in range(n):
        d=q[i][i]-sum(lower[i][k]**2*diagonal[k] for k in range(i))
        assert d>0
        diagonal.append(d)
        for j in range(i+1,n):
            lower[j][i]=(q[j][i]-sum(lower[j][k]*lower[i][k]*diagonal[k] for k in range(i)))/d
    assert all(q[i][j]==sum(lower[i][k]*diagonal[k]*lower[j][k] for k in range(n)) for i in range(n) for j in range(n))
    return lower,diagonal

def exact_short_vectors(q,bound):
    lower,diagonal=ldl(q)
    n=len(q);z=[0]*n;found=[];nodes=0
    def visit(i,partial):
        nonlocal nodes
        nodes+=1
        if i<0:
            if any(z):
                assert gram_value(q,z)==partial
                found.append(tuple(z))
            return
        remaining=bound-partial
        if remaining<0:return
        shift=sum(lower[j][i]*z[j] for j in range(i+1,n))
        a,b=shift.numerator,shift.denominator
        squared_radius=(remaining/diagonal[i])*b*b
        radius=isqrt(squared_radius.numerator//squared_radius.denominator)
        low=-((radius+a)//b)
        high=(radius-a)//b
        # low=ceil((-radius-a)/b), high=floor((radius-a)/b).
        for value in range(low,high+1):
            z[i]=value
            term=diagonal[i]*(F(value)+shift)**2
            assert term<=remaining
            visit(i-1,partial+term)
    visit(n-1,F(0))
    return sorted(found),nodes,diagonal

INTEGER_GRAM = [[720, 138, 140, 40, 140, 0, -180, 0, -180], [138, 720, 98, 0, 0, -220, 0, -199, 80], [140, 98, 720, 67, -140, 0, 0, -140, -53], [40, 0, 67, 720, 0, 0, -240, 0, -93], [140, 0, -140, 0, 720, -48, -43, -220, -61], [0, -220, 0, 0, -48, 720, 34, -56, -300], [-180, 0, 0, -240, -43, 34, 720, -66, -264], [0, -199, -140, 0, -220, -56, -66, 720, -360], [-180, 80, -53, -93, -61, -300, -264, -360, 720]]
DENOMINATOR = 720
VECTORS = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, -1, 0, -1, -1, -2, -2, -2, -3], [-1, 0, -1, -1, -1, -1, -2, -2, -3], [0, -1, -1, -1, -2, -2, -2, -3, -3]]
NEW_VECTOR = [0, 0, 0, 0, 0, 0, 0, 1, 1]
REFLECTION_TABLE = [(1, 4, 12, 1, [-1, 0, 0, 1, 0, 0, 0, 0, 0]), (2, 3, 5, 1, [0, 1, 1, 0, -1, 0, 0, 0, 0]), (3, 2, 5, 1, [0, 1, 1, 0, -1, 0, 0, 0, 0]), (4, 1, 5, -1, [1, 0, 0, -2, 1, 0, 0, 0, 0]), (5, 1, 7, 1, [1, 0, 0, 0, 1, 0, -1, 0, 0]), (6, 2, 4, -1, [0, 1, 0, 1, 0, -1, 0, 0, 0]), (7, 1, 5, -1, [1, 0, 0, 0, 1, 0, -1, 0, 0]), (8, 1, 9, 1, [1, 0, 0, 0, 0, 0, 0, 1, -1]), (9, 1, 8, -1, [1, 0, 0, 0, 0, 0, 0, 1, -1]), (10, 1, 11, 1, [1, 0, 0, 0, 0, 0, 0, 0, 0]), (11, 1, 10, 1, [1, 0, 0, 0, 0, 0, 0, 0, 0]), (12, 1, 4, 1, [1, 0, 0, -1, 0, 0, 0, 0, 0])]

q=[[F(x,DENOMINATOR)for x in row]for row in INTEGER_GRAM]
assert all(q[i][j]==q[j][i]for i in range(9)for j in range(9))
target=VECTORS+[NEW_VECTOR]
assert all(gram_value(q,v)==1 for v in target)
short,nodes,diag=exact_short_vectors(q,F(1))
signed={tuple(v)for v in target}|{tuple(-x for x in v)for v in target}
assert set(short)==signed and len(short)==26
qrank=matrix_rank([[v[i]*v[j]for i in range(9)for j in range(i,9)]for v in target])
assert qrank==13
assert matrix_rank(VECTORS)==9

def dot(a,b):return sum(x*y for x,y in zip(a,b))
witnesses=[]
for removed,j,k,eps,phi in REFLECTION_TABLE:
 r,j0,k0=removed-1,j-1,k-1
 assert dot(phi,NEW_VECTOR)==0
 u=[eps*x-y for x,y in zip(VECTORS[k0],VECTORS[j0])]
 assert dot(phi,u)==-2
 g=[[int(a==b)+u[a]*phi[b]for b in range(9)]for a in range(9)]
 assert all(sum(g[a][c]*g[c][b]for c in range(9))==int(a==b)for a in range(9)for b in range(9))
 facet=[v for i,v in enumerate(target)if i!=r]
 assert matrix_rank(facet)==9
 assert matrix_rank([[v[a]*v[b]for a in range(9)for b in range(a,9)]for v in facet])==12
 for i,v in enumerate(target):
  if i==r:continue
  expected=[eps*x for x in VECTORS[k0 if i==j0 else j0]]if i in {j0,k0}else v
  assert [dot(row,v)for row in g]==expected
 witnesses.append({'removed_original_index_one_based':removed,'swap_indices_one_based':[j,k],'sign':eps,'functional':phi,'integral_involution':g,'fixes_new_vector':True,'facet_vector_rank':9,'facet_quadratic_rank':12,'ray_permutation_sign':-1})
# With rays ordered (v1,...,v12,w), deleting w has incidence +1
# in DEKM equations(1)-(2), using the original ordered rays for tau.
# No other face is equivalent to tau, because each has an odd stabilizer.
result={
 'scope':'Exact minimum, dimension and facet-reflection certificate for the two explicit boundary cells; no whole-homology vanishing claim.',
 'integer_gram':INTEGER_GRAM,'denominator':DENOMINATOR,'target_vectors':target,
 'positive_LDL_diagonal':[str(x)for x in diag],
 'norm_le_one_signed_vectors':short,'enumeration_node_count':nodes,
 'quadratic_rank':qrank,'projective_degree':12,
 'odd_facet_witnesses':witnesses,
 'unique_remaining_facet':'tau, obtained by deleting the new vector',
 'rank9_boundary_coefficient':1,
 'rank10_extension':{'gram':'Q orthogonal-sum [1]','minimum_pairs':14,'quadratic_rank':14,'projective_degree':13,'unique_surviving_full_rank_facet':'sigma','relative_boundary_facet':'delete e10','boundary_coefficient_after_orientation_choice':1}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'positive_definite':True,'minimum_pairs':13,'enumeration_nodes':nodes,'quadratic_rank':qrank,'odd_other_facets':len(witnesses),'all_fix_w':True,'unique_remaining_boundary_coefficient':1,'rank10_extension_boundary_coefficient':1,'whole_homology_claim':False},indent=2))
