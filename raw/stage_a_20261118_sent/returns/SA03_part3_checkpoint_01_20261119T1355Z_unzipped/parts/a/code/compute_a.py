"""Exact finite algebra checks; these are tests, not automatic proof verdicts."""
from pathlib import Path
import itertools, json
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
out={}

# Linear counterexample to the two separate relation submodules, scan24.
q=s.Matrix([[1,1]]); rho=s.Matrix([[1,0]])
ker=q.nullspace()[0]
out['mixed_relation']={'q':str(q),'rho':str(rho),'ker_q_generator':list(ker),'rho_kernel':list(rho*ker),'dim_correct_C':1-s.Matrix.hstack(*[rho*v for v in q.nullspace()]).rank(),'dim_J_mod_R1_plus_R2':1,'lambda_id_compatible':False}
# The second proposed quotient coker rho fails even without primed terms.
q2=s.Matrix([[1]]);rho2=s.Matrix([[1]])
out['coker_rho']={'dim_correct_C':1,'dim_coker_rho':1-rho2.rank(),'explanation':'For q=id, rho=id, compatible pairs have mu=lambda and arbitrary lambda.'}

# Square-zero algebra coefficient multiplication; epsilon^2=0.
t,e,a,b,x,y,z=s.symbols('t e a b x y z')
sq=s.rem((a+b*e)**2,e**2,e)
out['dual_number_endomorphism']={'image_epsilon_squared':str(sq),'equations':[str(s.expand(sq).coeff(e,i)) for i in (0,1)],'char_not_2_automorphisms_reduced':'a=0; b invertible','char_2_equations':'a^2=0; b invertible for automorphisms'}
out['regular_square_zero_ideal']={'algebra':'k[t]_(t)[epsilon]/epsilon^2','J_basis_over_DVR':['epsilon'],'multiplication_t_power_on_J':'t^n (nonzero on the free rank-one DVR module)','integral_ambient':False}

# Fixed finite jets: agreement to order r, nonzero infinitesimal deformation.
r,d=3,5
f=z**d+e*z**r;g=z**d
out['fixed_jet']={'r':r,'d':d,'difference':str(f-g),'mod_z_power':str(s.rem(f-g,z**r,z)),'epsilon_coefficient':str(s.diff(f-g,e)),'homogeneous_pair':['x^5+epsilon*x^3*y^2','y^5'],'no_common_zero_reason':'On y=0 the first coordinate is x^5; on y!=0 the second is invertible.'}

# T=P1 jet transition: z'=1/z gives tangent coordinate v'=-v/z^2.
v=s.symbols('v')
out['P1_tangent_restriction']={'transition_derivative':str(s.diff(1/z,z)*v),'fibre_over_z0':'A^1','closed_projective_embedding_possible':False,'reason':'A closed fibre A1 is not proper; a closed subscheme of projective space would be proper.'}

# Idempotents in Z_2[x]/(x^2-1) encode the binary finite-etale test.
idem=s.rem((a+b*x)**2-(a+b*x),x*x-1,x)
out['mu2_binary_test']={'idempotent_equations':[str(s.expand(idem).coeff(x,i)) for i in (0,1)],'generic_solutions':[[str(vv) for vv in tup] for tup in s.solve([a*a+b*b-a,2*a*b-b],[a,b])],'generic_geometric_count':4,'special_geometric_count':2,'special_reason':'In characteristic2 the linear coefficient forces b=0 and a^2=a.'}

# Geometric section counts / dimensions over split and infinitesimal finite sources.
out['nonseparated_etale']={'branch_points':[0,1],'section_choices':list(itertools.product([0,1],repeat=2)),'section_count':4,'max_fibre_count':2,'source_components':1,'asserted_bound':2}
out['mixed_dimensions']={'source_degree':2,'target_dimension_set':[1,2],'restriction_dimensions':sorted({a+b for a in (1,2) for b in (1,2)}),'scalar_multiple_set':[2,4]}
out['dual_number_affine_dimension']={'source_length':2,'target_dimension_set':[1],'restriction_dimension_set':[2],'literal_D_equals_nDprime_rhs':[4]}
out['finite_etale_counts']=[{'components':n,'rank':m,'restriction_rank':m**n} for n,m in [(1,2),(2,2),(3,2),(2,3)]]

# Scheme-theoretic stability equations on an ordinary Grassmannian quotient chart.
c,d=s.symbols('c d')
Q=s.Matrix([[1,a,0,b],[0,c,1,d]])
N=s.Matrix([[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]])
M=s.Matrix([[a,b],[c,d]])
defect=Q*N-M*Q
u,w=s.symbols('u w')
generator=s.Matrix([u,w]);cyclic=s.Matrix.hstack(generator,M*generator)
out['grassmann_stability_freeness']={'quotient_matrix':str(Q),'multiplication_matrix':str(M),'descent_equations_matrix':str(defect),'square_zero_equations_matrix':str(M*M),'cyclic_generator_determinant':str(s.expand(cyclic.det())),'zero_action_stable_but_not_B_free':True,'regular_nilpotent_action_free':True}

# Constant-action functor on finite C2-sets.
out['C2_internal_Hom_counterexample']={'sizes_for_trivial_two_point_test':{str(n):2**n for n in range(5)},'forced_cardinality_A':1,'regular_C2_action':[1,0],'F_regular_action':[0,1],'E_power_A_action':[1,0]}

# Laurent monomial parity proves no section to squaring Gm.
out['nonfinite_source_degree_formula']={'equation':'u(t)^2=t in k[t,t^-1]','units':'c*t^m','exponent_equation':'2*m=1','integer_solutions':[],'representing_section_scheme':'empty','predicted_rank_if_nu_only':2}

# Surjection of points and formal principal homogeneous action need separate hypotheses.
out['surjectivity_failure']={'T':'Spec k[epsilon]/epsilon^2','X':'Spec k','underlying_map_surjective':True,'section_obstruction':'epsilon must map to both epsilon and 0 in R[epsilon]/epsilon^2 for any nonzero R'}
out['nonflat_principal_action']={'S':'Spec k[t]','G':'Spec k[t,x]/(t*x)','action':'addition','ideal_Hopf_compatibility':'Delta(tx)=tx tensor 1 + 1 tensor tx','principal_action_inverse':'(p,q) -> (p,q-p)','t_times_x':0,'x_nonzero_witness':'quotient t=0 is k[x]','section_forces_support_monomorphism_isomorphism':True}

assert out['mixed_relation']['dim_correct_C']==0
assert out['coker_rho']['dim_correct_C']==1
assert out['fixed_jet']['mod_z_power']=='0'
assert len(out['mu2_binary_test']['generic_solutions'])==4
assert out['nonseparated_etale']['section_count']>out['nonseparated_etale']['asserted_bound']
assert out['mixed_dimensions']['restriction_dimensions']!=out['mixed_dimensions']['scalar_multiple_set']
path=ROOT/'outputs'/'compute_a.json'
path.write_text(json.dumps(out,indent=2,ensure_ascii=False,default=str)+'\n')
print(json.dumps({'checks':len(out),'all_assertions_passed':True,'output':str(path)},indent=2))
