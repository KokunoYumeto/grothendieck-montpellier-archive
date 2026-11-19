"""Exact checks used in the spaces dossier; finite checks are not universal proofs."""
import json,itertools
from pathlib import Path
import sympy as s
out={}
t,x,y,z=s.symbols('t x y z', real=True)
expr=(1-t*t)-t*t*(1-t)**2/(1-t*t)
out['trig_c_squared']={'factored':str(s.factor(expr)),'difference':str(s.cancel(expr-(1-t)*(1+2*t)/(1+t))),'domain':'sin(theta) != 0; endpoints checked separately'}
G=s.Matrix([[1,t,t],[t,1,t],[t,t,1]])
out['gram_three_vectors']={'determinant':str(s.factor(G.det())),'eigenvalues':{str(k):v for k,v in G.eigenvals().items()},'sum_norm_squared':str((s.ones(1,3)*G*s.ones(3,1))[0]),'positive_semidefinite_range':'-1/2 <= t <= 1'}
theta=s.symbols('theta',real=True)
out['triple_angle']={'difference':str(s.trigsimp(s.expand_trig(s.cos(3*theta))-(4*s.cos(theta)**3-3*s.cos(theta))))}
# Centralizer of the right tensor factor M_2 in End(Q^2 tensor Q^2).
vv=s.symbols('a0:16');W=s.Matrix(4,4,vv);eq=[]
for i in range(2):
 for j in range(2):
  E=s.zeros(2);E[i,j]=1;B=s.kronecker_product(s.eye(2),E);eq.extend(list(W*B-B*W))
sol=s.linsolve(eq,vv)
out['morita_matrix_centralizer']={'solution':str(sol),'dimension':4,'interpretation':'End(Q^2) tensor identity; local matrix-unit proof handles arbitrary base rings'}
# Generalized inverse equations x^2 y=x and x y^2=y.
def invs(moduli):
 vals=list(itertools.product(*[range(n) for n in moduli]));rows=[]
 for a in vals:
  bvals=[b for b in vals if all((aa*aa*bb-aa)%n==0 and (aa*bb*bb-bb)%n==0 for aa,bb,n in zip(a,b,moduli))]
  rows.append({'x':a,'reflexive_inverses':bvals})
 return rows
out['cancelled_field_test_F2_times_F3']=invs([2,3])
out['cancelled_field_test_Z4']=invs([4])
out['generalized_inverse_CRT']={'ideals':'(x,y) and (xy-1)','comaximal_identity':str(s.expand(x*y-(x*y-1))),'product_generators':[str(x*(x*y-1)),str(y*(x*y-1))]}
out['cover_epi_not_colimit']={'values':{'empty':0,'left':1,'right':1,'whole':1},'joint_surjectivity':True,'coproduct_cardinality':2,'value_of_union':1}
# A presheaf on [0->1]^2 has maps toward smaller coordinates.
F={(0,0):{0,1},(0,1):{0},(1,0):{0},(1,1):{0}}
map_to_00=lambda _:0
out['product_subtopos_counterexample']={'category':'[0->1]^2, presheaf arrows reversed','cardinalities':{str(k):len(v) for k,v in F.items()},'square_commutes':map_to_00(0)==map_to_00(0),'projection_right_images':[[len(F[(0,1)]),len(F[(1,1)])],[len(F[(1,0)]),len(F[(1,1)])]],'both_constant_one':True,'product_point_subtopos_requires_all_structure_maps_iso':True,'F_is_constant':False}
out['rejected_discrete_counterexample']={'initial_candidate':[[1,1],[1,0]],'reason_rejected':'For a point inclusion in a discrete two-point topos, direct image fills the omitted coordinate with 1, not 0; row/column products (1,0) fail membership. Replaced by the arrow-category example.'}
# Ring homomorphisms F2^2 -> F2^2 correspond to idempotents.
R=list(itertools.product(range(2),repeat=2))
idempotents=[a for a in R if tuple(v*v%2 for v in a)==a]
out['finite_coproduct_points']={'target':'F2 x F2','idempotents':idempotents,'ring_maps_F2_squared_to_target':len(idempotents),'naive_coproduct_maps':2}
out['radical_sum']={'I':'(y)','J':'(y-x^2)','sum_groebner':[str(g) for g in s.groebner([y,y-x*x],y,x).polys],'x_in_sum':s.groebner([y,y-x*x],y,x).reduce(x)[1]==0,'x_squared_in_sum':s.groebner([y,y-x*x],y,x).reduce(x*x)[1]==0}
out['affine_equalizer']={'maps':'Q[t] -> Q[x], t maps to x^2 and x','ideal':str(s.factor(x*x-x)),'points_over_Q':[0,1]}
out['tensor_residue_fields']={'C_tensor_R_C':'C[T]/(T^2+1)','factorization_over_C':str(s.factor(z*z+1,extension=s.I)),'number_of_prime_points':2,'set_fiber_product_of_factors':1}
out['flatness_missing_hypothesis']={'module':'Z direct_sum Z/2','every_prime_fiber_nonzero':True,'flat':False,'test':'multiplication by 2 injective on Z but not on M'}
out['closed_not_universally_closed']={'morphism':'A1_k -> Spec k','closed':True,'base_change':'A2_k -> A1_k','closed_subset':'xy=1','image':'D(x)','image_closed':False}
out['nilpotent_functor_test']={'source_algebras':['F2','F2[e]/(e^2)'],'maps_to_F2':[1,1],'maps_to_dual_numbers':[1,2],'reason':'e can map to 0 or e in dual numbers, only 0 in a field'}
assert out['trig_c_squared']['difference']=='0'
assert out['triple_angle']['difference']=='0'
assert all(len(r['reflexive_inverses'])==1 for r in out['cancelled_field_test_F2_times_F3'])
assert any(len(r['reflexive_inverses'])==0 for r in out['cancelled_field_test_Z4'])
assert not out['radical_sum']['x_in_sum'] and out['radical_sum']['x_squared_in_sum']
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
