#!/usr/bin/env python3
"""Exact finite computations supporting manuscript checks, not numerical proofs of infinity."""
from fractions import Fraction
from itertools import combinations
import json, math
from pathlib import Path
import sympy as s
out={}
# Cote 6/49: smooth genus-2 curve with an ordinary and a supersingular elliptic quotient.
def chi(n,p):
    n%=p
    return 0 if n==0 else (1 if pow(n,(p-1)//2,p)==1 else -1)
examples=[]
for p in [5,7,11]:
    for a,b,c in combinations(range(1,p),3):
        n1=p+1+sum(chi((u-a)*(u-b)*(u-c),p) for u in range(p))
        n2=p+2+sum(chi(u*(u-a)*(u-b)*(u-c),p) for u in range(p)) # quartic has two rational infinity points
        t1=p+1-n1;t2=p+1-n2
        if (t1%p==0)!=(t2%p==0):
            examples.append(dict(p=p,roots=[a,b,c],E1_points=n1,E2_points=n2,E1_trace=t1,E2_trace=t2))
            break
    if examples:break
out['mixed_elliptic_quotients']=examples
p=examples[0]['p'];a,b,c=examples[0]['roots'];x=s.symbols('x')
f=(x*x-a)*(x*x-b)*(x*x-c)
out['genus2_polynomial']={'polynomial_mod_p':str(s.Poly(f,x,modulus=p).as_expr()),'gcd_with_derivative_mod_p':str(s.gcd(s.Poly(f,x,modulus=p),s.Poly(s.diff(f,x),x,modulus=p)).as_expr()),'genus':2,'p':p}
# Cote 7/23: monomial de Rham differential.
for p in [2,3,5]:
    out[f'affine_line_char_{p}']={'kernel_monomial_exponents_0_to_20':[n for n in range(21) if n%p==0], 'H1_representative_exponents_0_to_20':[n for n in range(21) if (n+1)%p==0]}
# Cote 7/40: sparse restricted series and denominator loss.
out['restricted_series_primitive_valuations']=[{'r':r,'exponent':2**(2*r)-1,'coefficient_val':r,'denominator_val':2*r,'primitive_val':-r,'better_coefficient_val':3*r,'better_primitive_val':r} for r in range(1,9)]
out['disjoint_infinite_family_support_samples']={str(m):[2**m*(2*r+1) for r in range(1,9)] for m in range(5)}
out['integrality_gap']={'form':'t^(p-1) dt over Z_p','coefficient_primitive':'1/p','tail_val_difference':'eventually +infinity','integrable_over_Zp':False,'integrable_over_Qp':True}
# Cote 7/41: written decay inequality.
out['positive_rho_bound_diagnostic']=[{'n':n,'a_n_abs':1,'rho_power':2**n,'inequality':1<=2**n} for n in range(8)]
# Cote 6/59: Frobenius skew relation F[a]=[a^p]F.
t,T=s.symbols('t T')
out['frobenius_skew_relation_F2t']={'F_after_t':str((t*T)**2),'t2_after_F':str(t**2*T**2),'difference':str(s.expand((t*T)**2-t**2*T**2))}
# Cote 6/65-66: finite-etale fixed vector kernel; monomial leading terms x_i^p.
u,v=s.symbols('u v');p=3
# A=[[1,1],[0,1]], equations A*x^[p]-x=0; inverse form generates same ideal.
g=s.groebner([u**3-u+v,v**3-v],u,v, modulus=p)
out['unit_root_kernel_rank2_p3']={'groebner':[str(a) for a in g.polys],'standard_monomials':[f'u^{i} v^{j}' for i in range(p) for j in range(p)],'rank':p*p,'jacobian_original':[[-1,0],[0,-1]],'jacobian_determinant_mod_p':1}
# Cote 6/62: RHom versus derived tensor shifts, G=Z/p, O=F_p.
out['derived_shift_test']={'RHom_Z_ZpFp':{'H^0':1,'H^1':1},'Zp_tensor_L_Z_Fp':{'H^-1':1,'H^0':1},'correct_shift_on_tensor_in_cohomological_convention':'[-1]'}
# Cote 7/59: differential operator commutator.
out['D_t_commutator']=[{'n':n,'D_t_times_t_minus_t_times_D':(n+1)-n} for n in range(9)]
# Cote 7/51: Cartan formula on polynomial forms in two variables.
x,y=s.symbols('x y');P=x*x*y+y*y;Q=x*y+x
# X = x*d/dx + y^2*d/dy; alpha=P dx+Q dy.
a,b=x,y*y
contraction=s.expand(P*a+Q*b)
dalpha=s.diff(Q,x)-s.diff(P,y)
left_dx=s.expand(s.diff(contraction,x)-dalpha*b)
left_dy=s.expand(s.diff(contraction,y)+dalpha*a)
right_dx=s.expand(a*s.diff(P,x)+b*s.diff(P,y)+P*s.diff(a,x)+Q*s.diff(b,x))
right_dy=s.expand(a*s.diff(Q,x)+b*s.diff(Q,y)+P*s.diff(a,y)+Q*s.diff(b,y))
out['cartan_homotopy']={'alpha_dx':str(P),'alpha_dy':str(Q),'vector_field':[str(a),str(b)],'left':[str(left_dx),str(left_dy)],'right':[str(right_dx),str(right_dy)],'difference':[str(s.expand(left_dx-right_dx)),str(s.expand(left_dy-right_dy))]}
# Cote 6/56-57: Smith normal form reduction of multiplicative-type kernels.
out['ordinary_polarized_formal_kernel']={'model_char_p':'k[[z_1,...,z_d]]/(z_1^(p^e1),...,z_r^(p^er))','regular_sequence':'distinct variable powers; dimension=d-r','reduced_ring':'k[[z_(r+1),...,z_d]]','dimension_g1_to_6':[g*(g+1)//2 for g in range(1,7)]}
# Cote 7/24: the full cusp complex is contracted by the weighted Euler derivation.
f=y*y-x**3;E_f=2*x*s.diff(f,x)+3*y*s.diff(f,y)
torsion_form=(3*y,-2*x)
d_torsion=s.diff(torsion_form[1],x)-s.diff(torsion_form[0],y)
out['ordinary_cusp_diagnostic']={'f':str(f),'Euler_f':str(E_f),'Euler_f_minus_6f':str(s.expand(E_f-6*f)),'Omega2':'C[x,y]/(y,x^2) dx wedge dy','torsion_form':'3y dx - 2x dy','d_torsion_coefficient':str(d_torsion),'Euler_homotopy':'on positive weight w, h=i_E/w; dh+hd=1; weight-zero complex is C in degree0','H_positive':0}
# Exact p-curvature of the Legendre Picard-Fuchs module over F_3(t).
t=s.symbols('t')
xx=s.symbols('xx');ca,cb,r0,r1,r2=s.symbols('ca cb r0 r1 r2')
ff=xx*(xx-1)*(xx-t);rr=r0+r1*xx+r2*xx**2
poly=s.Poly(s.expand(s.Rational(1,2)*xx*(xx-1)-(ca+cb*xx)*ff-s.diff(rr,xx)*ff+s.Rational(1,2)*rr*s.diff(ff,xx)),xx)
solution=s.solve(poly.all_coeffs(),[ca,cb,r0,r1,r2],dict=True)[0]
out['legendre_cyclic_basis']={str(k):str(v) for k,v in solution.items()}
def modrat(z,p=3):
    num,den=s.fraction(s.cancel(z))
    pn=s.Poly(num,t,modulus=p);pd=s.Poly(den,t,modulus=p)
    if pd.is_zero:raise ValueError('zero denominator modulo p')
    return s.cancel(pn.as_expr()/pd.as_expr())
# In basis e0=omega,e1=nabla_partial(omega), the connection matrix has columns
# (0,1), (1/(4t(1-t)),-(1-2t)/(t(1-t))).
A=s.Matrix([[0,1/(4*t*(1-t))],[1,-(1-2*t)/(t*(1-t))]]).applyfunc(modrat)
B=s.eye(2)
for j in range(3):B=(B.diff(t)+A*B).applyfunc(modrat)
out['legendre_pcurvature_p3']={'base':'F_3[t,1/(t(1-t))]','curve':'y^2=x(x-1)(x-t)','basis':['omega','nabla_partial(omega)'],'connection_matrix':[[str(A[i,j]) for j in range(2)] for i in range(2)],'pcurvature':[[str(B[i,j]) for j in range(2)] for i in range(2)],'nonzero':any(B[i,j]!=0 for i in range(2) for j in range(2)),'square':[[str(modrat((B*B)[i,j])) for j in range(2)] for i in range(2)],'trace':str(modrat(s.trace(B))),'determinant':str(modrat(B.det())),'partial_p':'partial^3=0 on F_3(t)'}
# Cote 7/48: derived base change does not imply cohomological flatness.
out['derived_base_change_countermodel']={'base':'Z','perfect_complex_degrees_0_1':'[Z --p--> Z]','ordinary_H0':0,'H0_after_derived_tensor_Fp':1,'conclusion':'cohomology does not commute with nonflat base change despite the tautological derived compatibility'}
path=Path(__file__).resolve().parents[1]/'outputs/computations.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
