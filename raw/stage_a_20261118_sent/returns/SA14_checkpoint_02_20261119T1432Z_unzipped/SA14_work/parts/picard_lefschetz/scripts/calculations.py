"""Exact symbolic/finite calculations supporting the Picard/Lefschetz audit.
Mathematical interpretations and hypotheses are in outputs/proof_checks.md.
These finite tests illustrate formulas; only symbolic identities are certificates.
"""
import json,itertools
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parents[1]
O={}
# 58:23: geometrically disconnected generic fibre, split closed fibre.
t=S.symbols('t')
O['split_special_fibre']={'polynomial':'t^2+1','irreducible_over_Q':bool(S.Poly(t*t+1,t,domain=S.QQ).is_irreducible),'roots_mod_5':[a for a in range(5) if (a*a+1)%5==0],'factorization_mod_5':str(S.factor(t*t+1,modulus=5)),'derivative_nonzero_at_roots':[2*a%5 for a in [2,3]],'generic_components_over_Q':1,'special_components_over_F5':2}
# 58:41: automorphism defect in all nontrivial Artinian thickenings.
O['automorphism_faithfulness']=[{'N':N,'inverse_mod_tN':str(sum((-t)**j for j in range(N))),'product_mod_tN':str(S.rem((1+t)*sum((-t)**j for j in range(N)),t**N,t)),'restrictions_of_1_and_1_plus_t':'both 1 mod t','distinct_mod_tN':N>=2} for N in range(2,7)]
# 58:58: skyscraper graded pieces, positive module k[x0].
O['skyscraper_twists']={'model':'P^2, Y=(x0=0), p=[1:0:0], U=X, F=k(p)','H0_F_twist_dimensions':{str(m):1 for m in range(-8,9)},'H0_formal_completion':0,'positive_module':'k[x0,x1,x2]/(x1,x2)=k[x0]','positive_generator_degrees':[0],'hyperplane_equation_on_F':'invertible; hence F-regular','Z':'empty; any condition only near Z is vacuous'}
# 57:295: two-dimensional quadratic algebra identities.
d,x,y,u,v=S.symbols('delta xi eta xi_prime eta_prime')
I=S.eye(2);J=S.Matrix([[0,d],[1,0]])
X=x*I+y*J;Y=u*I+v*J
prod=X*Y
norm=lambda a,b:a*a-d*b*b
O['diangles']={'S_square_minus_delta_I':str(J*J-d*I),'product':str(prod),'expected_difference':str(prod-((x*u+d*y*v)*I+(x*v+y*u)*J)),'norm_product_residual':str(S.expand(norm(x*u+d*y*v,x*v+y*u)-norm(x,y)*norm(u,v))),'rotation_square':str(X*X),'order_two_off_diagonal':'2*xi*eta','tau_composition':'(tau+tau_prime)/(1+delta*tau*tau_prime), denominators nonzero'}
# 57:292: lattice tests; invariant factors illustrate nonzero-H criterion.
O['tate_lattice_tests']=[]
for p in [2,3,5]:
 for a in [0,1,2,3]:
  for b in [0,1,2,3]:
   # Multiplication by p^a on Z/p^b; b=0 is zero H.
   N=p**b
   kernel=[z for z in range(N) if (p**a*z)%N==0]
   O['tate_lattice_tests'].append({'p':p,'lattice_map':f'multiplication by {p}^{a}','H_order':N,'tensor_map_kernel_size':len(kernel),'split_lattice_injection':a==0,'nonzero_H':b>0,'mod_p_injective':a==0})
O['tate_isogeny_test']={'map':'multiplication by p on Qp/Zp','kernel_order':'p','cokernel_order':1,'isomorphism_mod_finite':True,'integral_Tate_map':'multiplication by p on Zp, not invertible','rational_Tate_map':'multiplication by p on Qp, invertible'}
# 57:289: impossibility of the literal equality for nonzero rank-p subgroup.
O['p_subgroup_equality']=[{'p':p,'pF':[p*x%p for x in range(p)],'G':list(range(p)),'pF_equals_G':set(p*x%p for x in range(p))==set(range(p))} for p in [2,3,5,7]]
# 57:285,287: derivative of inversion and fixed tangent dimensions.
O['igusa_tangent_control']=[{'char':p,'dim_A':a,'dim_B':b,'fixed_tangent_dim_Aprime':a if p==2 else 0,'fixed_cotangent_dim_A':a if p==2 else 0,'h01':b+(a if p==2 else 0),'h10':b+(a if p==2 else 0),'A_prime_2_rank':2**(2*a),'Pic_tau_relative_dim':b,'flat_kernel':'finite flat A_prime[2]'} for p in [2,3,5] for a,b in [(1,1),(2,1),(2,3)]]
# 57:298,300: solve equality of polynomial and inverse-polynomial restrictions.
O['glued_curve_restrictions']=[]
for N in range(1,9):
 c=S.symbols('c0:'+str(N+1));e=S.symbols('e0:'+str(N+1))
 equations=[c[0]-e[0]]+list(c[1:])+list(e[1:])
 M,_=S.linear_eq_to_matrix(equations,list(c)+list(e))
 O['glued_curve_restrictions'].append({'max_degree':N,'unknowns':2*N+2,'constraint_rank':M.rank(),'solution_dimension':2*N+2-M.rank(),'solutions':'c0=e0, all positive-degree coefficients zero'})
# 57:302: degree and independent Pic^0 generator determine zero Pic classes.
# L1 degree3 and L2=L1 tensor P, P of infinite order.
M=S.Matrix([[3,3],[0,1]])
O['elliptic_gluing_pic']={'map_Z2_to_degree_and_P':str(M),'integer_kernel':[], 'determinant':int(M.det()),'Pic_kernel_on_components':0,'unit_map':'(a,b) -> a/b from k* x k* to k*, surjective','Pic_pushout':0,'ample_bundle_exists':False,'normalization':'P2 disjoint union P2, projective'}
# 57:304 and 58:66: normalization/graph contributions.
graphs={'tree3':(3,[(0,1),(1,2)]),'cycle3':(3,[(0,1),(1,2),(2,0)]),'two_vertices_two_edges':(2,[(0,1),(0,1)]),'one_vertex_one_loop':(1,[(0,0)])}
O['nodal_graph_genus']=[]
for name,(nv,edges) in graphs.items():
 inc=S.zeros(nv,len(edges))
 for j,(a,b) in enumerate(edges):inc[a,j]-=1;inc[b,j]+=1
 rank=inc.rank();b1=len(edges)-rank
 O['nodal_graph_genus'].append({'graph':name,'vertices':nv,'nodes':len(edges),'incidence_rank':rank,'b1':b1,'genus_if_all_components_rational':len(edges)-nv+1,'torus_rank':b1})
# 58:53 Jacobi cofactor identity as a polynomial identity; conventional signed minors.
entries=S.symbols('a0:9');A=S.Matrix(3,3,entries)
i,j,h,k=0,1,0,1
cof=A.cofactor_matrix();complement=A.minor_submatrix(i,h).minor_submatrix(j-1,k-1).det()
signed_complement=(-1)**(i+j+h+k)*complement
jacobi=S.expand(cof[i,h]*cof[j,k]-cof[i,k]*cof[j,h]-A.det()*signed_complement)
O['jacobi_cofactor']={'size':3,'rows_deleted':[1,2],'columns_deleted':[1,2],'signed_complement':str(signed_complement),'polynomial_residual':str(jacobi),'certificate':'residual exactly zero in Z[a0,...,a8]'}
# 58:51: rank = largest nonzero minor on representative exact matrices.
O['rank_minor_checks']=[]
for A in [S.Matrix([[1,2,3],[2,4,6]]),S.Matrix([[1,0,2],[0,1,3]]),S.zeros(2,3),S.Matrix([[1,2],[3,6]])]:
 largest=0
 for size in range(1,min(A.rows,A.cols)+1):
  if any(A.extract(r,c).det()!=0 for r in itertools.combinations(range(A.rows),size) for c in itertools.combinations(range(A.cols),size)):largest=size
 O['rank_minor_checks'].append({'matrix':str(A),'rank':A.rank(),'largest_nonzero_minor':largest})
# Pole growth obstruction in 58:46. Table is illustration; proof is analytic algebra.
O['formal_pole_growth']={'series':'sum z^(-n^2) x^n','pole_orders':[n*n for n in range(13)],'successive_increments':[2*n+1 for n in range(12)],'rational_fraction_bound':'if g0 has z-order e and g*f=h with g,h in k[[z]][[x]], then pole_order(f_n) <= (n+1)e; quadratic growth violates every such bound'}
# Exact sequence direction 58:56: boundary image = kernel alpha.
O['localization_direction']={'sequence':'A -> B -> C --alpha--> D','coker_A_to_B':'ker(alpha)','restriction_A_to_B_surjective_iff':'alpha injective','alpha_surjective_alone':'does not imply ker(alpha)=0'}
# Connection dimension arithmetic only, not a geometric proof.
O['cutting_dimension']=[{'n':n,'h':h,'K':n+h,'K_minus_n':h} for n in range(1,5) for h in range(4)]
(P/'outputs'/'calculations.json').write_text(json.dumps(O,ensure_ascii=False,indent=2)+'\n')
print('Exact calculations completed:',len(O),'named sections')
print('Split-special-fibre polynomial:',O['split_special_fibre'])
print('Jacobi residual:',jacobi)
print('Diangle norm residual:',O['diangles']['norm_product_residual'])
print('Gluing restriction solution dimensions:',[r['solution_dimension'] for r in O['glued_curve_restrictions']])
print('Graph cycle/genus checks:',O['nodal_graph_genus'])
print('No numeric test certifies a missing geometric construction; see proof_checks.md.')
