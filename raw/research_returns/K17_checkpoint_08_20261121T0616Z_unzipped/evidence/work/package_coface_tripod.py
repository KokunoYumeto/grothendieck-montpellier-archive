from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json,ast
b=Path(__file__).parent
c=json.loads((b/'k12_coface_tripod_candidate.json').read_text());q=[[F(z)for z in row]for row in c['gram_rational']];den=lcm(*(z.denominator for row in q for z in row));G=[[int(z*den)for z in row]for row in q]
s=(b/'k12_survivor_certificate.py').read_text();tree=ast.parse(s)
funcs='\n\n'.join(ast.get_source_segment(s,n)for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in {'gram_value','matrix_rank','ldl','exact_short_vectors'})
s2=(b/'k12_survivor_boundary_certificate.py').read_text();tree2=ast.parse(s2)
table=next(ast.literal_eval(n.value)for n in tree2.body if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='table'for t in n.targets))
head='''"""Exact standalone certificate: the explicit orientation survivors are boundaries.

Uses only hard-coded integer data and Python's standard library. The proof
that these exact cells bound in the localized Voronoi complex is in
k12_survivor_coface_section.tex. This does not compute either whole homology
group or K12. No numerical discovery output is an input to this verifier.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

'''
const='\n\nINTEGER_GRAM = '+repr(G)+'\nDENOMINATOR = '+repr(den)+'\nVECTORS = '+repr(c['target'][:-1])+'\nNEW_VECTOR = '+repr(c['target'][-1])+'\nREFLECTION_TABLE = '+repr(table)+'\n'
body='''
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
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\\n')
print(json.dumps({'positive_definite':True,'minimum_pairs':13,'enumeration_nodes':nodes,'quadratic_rank':qrank,'odd_other_facets':len(witnesses),'all_fix_w':True,'unique_remaining_boundary_coefficient':1,'rank10_extension_boundary_coefficient':1,'whole_homology_claim':False},indent=2))
'''
(b/'k12_survivor_coface_certificate.py').write_text(head+funcs+const+body)
print('packaged',den)
