from pathlib import Path
import ast,json
base=Path(__file__).parent
r=json.loads((base/'k12_trimodular_extremal_check.json').read_text())['results']
e=json.loads((base/'k12_trimodular_exact_certificate.json').read_text())['record1']
v=json.loads((base/'k12_survivor_certificate.json').read_text())['vectors']
s=(base/'k12_trimodular_extremal_check.py').read_text();tree=ast.parse(s)
needed={'dot','cross','detcols','canonical','facets','parity','matvec'}
functions='\n\n'.join(ast.get_source_segment(s,n)for n in tree.body if isinstance(n,ast.FunctionDef)and n.name in needed)
s2=(base/'k12_survivor_certificate.py').read_text();tree2=ast.parse(s2)
functions+='\n\n'+'\n\n'.join(ast.get_source_segment(s2,n)for n in tree2.body if isinstance(n,ast.FunctionDef)and n.name in {'reconstruct_dual','det3'})
head='''"""Exact checks of the three published trimodular extremal templates.

The published values h(3,3)=25 and number of extremal equivalence classes3
are external coverage inputs, not re-enumerated by this program. This
standalone verifier checks each displayed record, the first obstruction,
the second identification and the third odd symmetry exactly.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json

'''
const='\n\nVERTEX_RECORDS = '+repr([x['vertices']for x in r])+'\nGALE_RECORDS = '+repr([x['rays']for x in r])+'\nOUTSIDE_VECTORS = '+repr(e['outside_vectors'])+'\nTAU_VECTORS = '+repr(v)+'\nODD_MATRIX = '+repr(r[2]['odd_ray_symmetry']['matrix'])+'\n'
body='''
results=[]
for vertices0,rays0 in zip(VERTEX_RECORDS,GALE_RECORDS):
 vertices=[tuple(v)for v in vertices0];rays=[tuple(v)for v in rays0]
 ineq=facets(vertices)
 box=[range(min(v[i]for v in vertices),max(v[i]for v in vertices)+1)for i in range(3)]
 points={z for z in product(*box)if all(dot(f[:3],z)<=f[3]for f in ineq)}
 expected={(0,0,0)}|set(rays)|{tuple(-x for x in z)for z in rays}
 assert points==expected and len(points)==25 and len(rays)==12
 assert all(canonical(z)==z for z in rays) and len(set(rays))==12
 minors=[abs(detcols(*a))for a in combinations(rays,3)]
 assert max(minors)==3 and 1 in minors
 results.append({'lattice_points':25,'signed_nonzero_pairs':12,'maximal_minor':3,'unit_minor_exists':True})
V1,_,_=reconstruct_dual(GALE_RECORDS[0]);V2,_,_=reconstruct_dual(GALE_RECORDS[1])
assert V2==[tuple(z)for z in TAU_VECTORS]
assert len(OUTSIDE_VECTORS)==6
S={canonical(z)for z in V1}
assert all(any(z)and canonical(z)not in S for z in OUTSIDE_VECTORS)
assert len({canonical(z)for z in OUTSIDE_VECTORS})==6
# sum outside quadratic forms = first five coordinate rays + twelfth ray.
right=[V1[i]for i in [0,1,2,3,4,11]]
assert all(sum(z[i]*z[j]for z in OUTSIDE_VECTORS)==sum(z[i]*z[j]for z in right)for i in range(9)for j in range(9))
rays=[tuple(z)for z in GALE_RECORDS[2]];lookup={z:i for i,z in enumerate(rays)}
images=[matvec(ODD_MATRIX,z)for z in rays]
assert all(canonical(z)in lookup for z in images)
perm=[lookup[canonical(z)]for z in images]
assert perm==[10,1,8,3,6,5,4,7,2,9,0,11] and parity(perm)==1
assert abs(detcols(*(tuple(row[j]for row in ODD_MATRIX)for j in range(3))))==1
out={'scope':'Per-record exact checks only; published extremal coverage is an explicit external input. No assertion that all target cells have index at most3 or generate their ambient lattice.',
 'published_parameters':{'h_3_3':25,'extremal_class_count':3,'source':'Averkov-Schymura 2024 section5.2 Tables1,3 p85'},
 'records':results,'first_dual_vectors':V1,'first_outside_vectors':OUTSIDE_VECTORS,'first_quadratic_identity_indices_one_based':[1,2,3,4,5,12],
 'first_template_complete_minimum_impossible':True,'second_dual_is_tau':True,
 'third_odd_matrix':ODD_MATRIX,'third_pair_permutation_zero_based':perm,
 'third_swaps_one_based':[[1,11],[3,9],[5,7]],'consequence':'Under ambient minimum generation and maximal index<=3, each rank10 degree12 orientation generator is zero or the previously certified boundary sigma.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\\n')
print(json.dumps({'records_checked':3,'first_impossible':True,'second_is_tau':True,'third_odd':True,'classification_coverage_recomputed':False},indent=2))
'''
(base/'k12_trimodular_classification_certificate.py').write_text(head+functions+const+body)
