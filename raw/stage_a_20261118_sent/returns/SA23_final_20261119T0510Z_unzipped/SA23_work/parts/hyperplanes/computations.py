#!/usr/bin/env python3
"""Exact checks of formulas/counterexamples already in the cote25 assessment.
Finite enumerations check examples only; unrestricted arguments are in proof_checks.md.
"""
import json, math
from pathlib import Path
import sympy as s
out={}
x,y,z,u,v,a,b,c,d,e,f,S1,S2=s.symbols('x y z u v a b c d e f S1 S2')
out['generic_combination_zero']=str(s.cancel((S1+S2*x).subs(x,-S1/S2)))
assert out['generic_combination_zero']=='0'
out['blowup_total_transform']=str(s.factor(a*x+b*x*u+c*x*v))
assert s.expand(a*x+b*x*u+c*x*v-x*(a+b*u+c*v))==0
out['quadric_tangent_section']=str((x*z-u*v).subs(z,0))
out['fixed_component_bertini']=str(s.factor(u*(a*x+b*y+c*z)))
q=x*z-y*y
out['char2_conic_gradient']=[str(s.Poly(s.diff(q,t),x,y,z,modulus=2).as_expr()) for t in [x,y,z]]
assert out['char2_conic_gradient']==['z','0','x']
# On P1 parametrized [s:t] -> [s²:st:t²], this is [t²:0:s²].
r,t=s.symbols('r t')
out['conic_pencil_ramification_numerator']=str(s.factor(s.together(s.diff((r*r+1)/r,r))))
out['conic_pencil_branch_values']=[s.simplify((r*r+1).subs(r,i)/i) for i in [-1,1]]
assert out['conic_pencil_branch_values']==[-2,2]
out['node_polar_matrix']=s.hessian(x*y,(x,y)).tolist()
out['cusp_quadratic_polar_matrix']=s.hessian(y*y,(x,y)).tolist()
assert s.det(s.hessian(x*y,(x,y)))==-1
assert s.det(s.hessian(y*y,(x,y)))==0
out['ambient_three_char2_quadric_partials']=[str(s.Poly(s.diff(x*x+y*z,t),x,y,z,modulus=2).as_expr()) for t in [x,y,z]]
# These vanish only at [1:0:0], where Q=1, so the projective quadric is smooth.
Q=a*x*x+b*y*y+c*z*z+d*x*y+e*x*z+f*y*z
det=s.factor(s.det(s.hessian(Q,(x,y,z))))
half=s.expand(det/2)
out['ternary_polar_determinant']=str(det); out['ternary_half_discriminant']=str(half)
assert all(coef.q==1 for coef in s.Poly(half,a,b,c,d,e,f).coeffs())
assert math.gcd(*map(int,s.Poly(det,a,b,c,d,e,f).coeffs()))==2
out['two_odd_ranks_sum']={'q1_half':str(a),'q2_half':str(b),'sum_even_discriminant':str(s.det(s.diag(2*a,2*b))),'required_factor':4}
assert s.det(s.diag(2*a,2*b))==4*a*b
standard=[]
for n in range(1,9):
 mat=s.zeros(n)
 for i in range(0,n-1,2): mat[i,i+1]=mat[i+1,i]=1
 if n%2: mat[n-1,n-1]=2
 val=mat.det(); expected=(-1)**(n//2)*(2 if n%2 else 1)
 assert val==expected
 standard.append({'rank':n,'polar_det':int(val),'corrected_discriminant':int(val/(2 if n%2 else 1))})
out['standard_forms']=standard
def bc(n,k): return math.comb(n,k) if n>=0 and 0<=k<=n else 0
hilbert=[]
for rank in range(2,7):
 for degree in range(0,9):
  exact=bc(degree+rank-1,rank-1)-bc(degree+rank-3,rank-1)
  cumulative=sum(bc(j+rank-1,rank-1)-bc(j+rank-3,rank-1) for j in range(degree+1))
  printed=bc(degree+rank,rank)-bc(degree+rank-2,rank)
  assert cumulative==printed
  if rank==2 and degree<5:hilbert.append({'rank':rank,'degree':degree,'graded_piece':exact,'printed_cumulative':printed})
out['hilbert_rank_alarm']=hilbert
out['schubert_dimension_checks']=[]
for R in range(2,10):
 for N in range(1,R+1):
  for M in range(1,N+1):
   for K in range(1,min(M,R-N)+1):
    lhs=K*(N-M+K)-(N-M)
    rhs=(K-1)*(N-M)+K*K
    assert lhs==rhs
    out['schubert_dimension_checks'].append([R,N,M,K,lhs])
out['schubert_checked_cases']=len(out.pop('schubert_dimension_checks'))
out['false_range_example']={'ambient_dimension':3,'X_dimension':3,'section_codimension':1,'claimed_first_stratum':'nonempty under k<=r-m','actual':'empty: every linear hyperplane in P3 is smooth'}
out['genus_two_no_plane_degree']=[{'degree':n,'smooth_plane_genus':(n-1)*(n-2)//2} for n in range(1,8)]
assert not any(v['smooth_plane_genus']==2 for v in out['genus_two_no_plane_degree'])
# General cofactor-ideal identity in the smallest nontrivial complementary-rank case.
A=s.Matrix([[1,0],[0,1],[a,b]])
B=s.Matrix([[1,0],[0,c],[d,1]])
normalA=s.Matrix(A[:,0]).cross(s.Matrix(A[:,1]))
normalB=s.Matrix(B[:,0]).cross(s.Matrix(B[:,1]))
intersection=normalA.cross(normalB)
mapA=s.Matrix([(normalB.dot(A[:,i])) for i in range(2)])
mapB=s.Matrix([(normalA.dot(B[:,i])) for i in range(2)])
cofA=s.simplify(A*s.Matrix([-mapA[1],mapA[0]]))
cofB=s.simplify(B*s.Matrix([-mapB[1],mapB[0]]))
assert s.simplify(cofA-intersection)==s.zeros(3,1)
assert s.simplify(cofB+intersection)==s.zeros(3,1)
out['cofactor_sign_example']={'P_section':list(map(str,cofA)),'Q_section':list(map(str,cofB)),'relation':'opposite signs; same ideal after inclusion in M'}
# Work in the free additive group of line-bundle characters (omega_X/Y, omega_Y/S, K).
# 0 -> Omega_X/Y tensor K -> P^1(K) -> K -> 0, with rank(Omega_X/Y)=d.
D=s.symbols('d',integer=True,positive=True)
omega_rel=s.Matrix([1,0,0]); omega_base=s.Matrix([0,1,0]); Kline=s.Matrix([0,0,1])
det_principal_parts=omega_rel+D*Kline+Kline
det_P=-det_principal_parts
det_Q=omega_base
det_M=omega_rel+omega_base
cofactor_line=s.simplify(det_P+det_Q-det_M)
discriminant_line=s.simplify(-Kline-cofactor_line) # Hom(L,K^-1)
assert cofactor_line==s.Matrix([-2,0,-D-1])
assert discriminant_line==s.Matrix([2,0,D])
out['line_bundle_determinant_exponents']={
 'character_basis':['omega_X/Y','omega_Y/S','K'],
 'det_principal_parts':[str(t) for t in det_principal_parts],
 'det_P':[str(t) for t in det_P],
 'cofactor_line':[str(t) for t in cofactor_line],
 'discriminant_line':[str(t) for t in discriminant_line],
 'derivation':'det P^1(K)=omega_X/Y*K^(d+1); L=det(P)*det(Q)*det(M)^-1; D is in Hom(L,K^-1).'}
# Universal polynomial dimension identities used throughout the incidence arguments.
R,N,M,H=s.symbols('r n m k',integer=True)
identities={
 'hyperplane_incidence_generic_dimension':(N+R-1)-R-(N-1),
 'higher_incidence_generic_dimension':N+M*(R-M)-M*(R-M+1)-(N-M),
 'grassmann_point_incidence_dimension':M*(R-M),
 'schubert_relative_codimension':s.expand(H*(N-M+H)-(N-M)-((H-1)*(N-M)+H**2)),
 'regular_sequence_codepth':(N-M)-(D-M)-(N-D),
 'first_jet_parameter_codimension':1+N,
 'projective_automorphism_dimension':(R+1)**2-1,
 'smooth_quadric_dimension':R-2,
}
for name in ['hyperplane_incidence_generic_dimension','higher_incidence_generic_dimension','schubert_relative_codimension','regular_sequence_codepth']:assert s.expand(identities[name])==0
out['universal_dimension_identities']={k:str(s.expand(v))for k,v in identities.items()}
# The Hessian on the critical-zero locus scales by the unit's constant term.
u0,u1,u2=s.symbols('u0 u1 u2'); F=a*x*x+b*x*y+c*y*y+d*x*x*y
unit=u0+u1*x+u2*y
HF=s.hessian(F,(x,y)).subs({x:0,y:0})
HUF=s.hessian(unit*F,(x,y)).subs({x:0,y:0})
assert HUF==u0*HF
assert s.factor(HUF.det()-u0**2*HF.det())==0
out['unit_hessian_scaling']={'Hessian_at_origin':[[str(v)for v in row]for row in HF.tolist()],'scaled_Hessian':[[str(v)for v in row]for row in HUF.tolist()],'determinant_difference':0,'scope':'Exact universal two-variable critical-zero example; general product-rule proof in proof_checks.md.'}
# Intersection of the two annihilator ideals in k[x,y]/(xy).
tt=s.symbols('tt')
gb=s.groebner([tt*y,(1-tt)*x],tt,x,y,order='lex')
elim=[g.as_expr() for g in gb.polys if not g.as_expr().has(tt)]
assert elim==[x*y]
out['node_conormal_annihilator']={'intersection_in_polynomial_ring':list(map(str,elim)),'quotient_relation':'x*y=0','fiber_of_generator_map':[0,0],'conclusion':'B→B², 1↦(y,x), is injective but its tensor with B/(x,y) is zero.'}
out['nilpotent_constant_fiber_rank']={'ring':'k[e]/(e²)','matrix':[['e']],'geometric_fiber_rank':0,'matrix_nonzero':True,'kernel':'(e), not a rank-one free direct summand','purpose':'Constant fiber rank alone does not force a matrix to be equivalent to diag(I_r,0) over a nonreduced base.'}
T=s.symbols('T')
assert s.cancel((1-T*T)/(1-T)**3-(1+T)/(1-T)**2)==0
out['quadric_hilbert_series_check']={'rank3_graded_series':str(s.cancel((1-T*T)/(1-T)**3)),'rank3_cumulative_series':str(s.cancel((1-T*T)/(1-T)**4)),'identity':'For rank r: h(T)=(1−T²)/(1−T)^r; cumulative series h(T)/(1−T).','general_proof':'One quadratic nonzerodivisor gives the degree-two shifted polynomial-ring exact sequence.'}
# A positive-dimensional linear base can force a singular pencil after Veronese.
q_fixed=a*x*x+b*y*y
p_fixed={x:0,y:0,z:1}
partials_fixed=[s.diff(q_fixed,t)for t in (x,y,z)]
assert q_fixed.subs(p_fixed)==0
assert all(t.subs(p_fixed)==0 for t in partials_fixed)
out['veronese_fixed_linear_space']={'field':'algebraically closed, characteristic0','source':'P²','embedding':'degree2 Veronese into P⁵','fixed_subspace':'C=V(U_x²,U_y²), isomorphic to P³','pencil':str(q_fixed),'point':[0,0,1],'partials':list(map(str,partials_fixed)),'values_at_point':[str(t.subs(p_fixed))for t in partials_fixed],'base_local_ideal':['x²','y²'],'base_length':4,'general_argument':'For every n≥2, (x^n,y^n) is contained in (x,y)²; the same first-jet obstruction persists. This general ideal inclusion, rather than a finite test, proves the all-degree statement.'}
out['checks_passed']=True
out['scope']='Exact symbolic identities and explicit examples; finite rank/degree lists do not prove universal statements.'
dest=Path(__file__).with_name('computations_output.json'); dest.write_text(json.dumps(out,default=str,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,default=str,ensure_ascii=False,indent=2))
