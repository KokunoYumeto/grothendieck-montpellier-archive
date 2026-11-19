#!/usr/bin/env python3
"""Exact, reproducible checks of manuscript formulas and specified counterexamples.

No finite sample is labelled a proof of a general theorem. Symbolic identities,
exhaustive finite examples, and integer root-lattice calculations are separated.
"""
import json,itertools,math,datetime
from pathlib import Path
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'parts/root'
out={};x,t,p,a,M,D=s.symbols('x t p a M D',nonzero=True)

f=s.cyclotomic_poly(7,x);fac=s.factor_list(f,modulus=2)
out['cyclotomic_F2_n3']={'polynomial':str(f),'factors':[(str(g),n) for g,n in fac[1]],'cubic_root_sets':[[r for r in (0,1) if int(g.subs(x,r))%2==0] for g,n in fac[1]],'conclusion':'two irreducible cubics, hence F8×F8; not F8'}
assert len(fac[1])==2 and all(s.degree(g,x)==3 for g,n in fac[1])

prime=7;pts=[(xx,yy) for xx in range(prime) for yy in range(prime) if (yy*yy-xx**3-xx)%prime==0]
tworoots=[xx for xx in range(prime) if (xx**3+xx)%prime==0]
out['maximal_order_p7']={'curve':'y²=x³+x over F7','affine_points':pts,'points_including_infinity':len(pts)+1,'trace':prime+1-(len(pts)+1),'discriminant_mod_7':(-64)%7,'rational_nonzero_two_torsion_x':tworoots,'deduction':'F²+7=0; if (1+F)/2 were an integral endomorphism, F would fix every geometric2torsion point. It does not: only one nonzero2torsion point is rational. Thus the Z[F] action need not extend to Z[(1+√−7)/2].'}
assert len(pts)+1==8 and tworoots==[0] and (-64)%7!=0

out['unit_square_classes']={str(mod):{'unit_count':sum(math.gcd(z,mod)==1 for z in range(mod)),'unit_squares':sorted({z*z%mod for z in range(mod) if math.gcd(z,mod)==1}),'quotient_size':sum(math.gcd(z,mod)==1 for z in range(mod))//len({z*z%mod for z in range(mod) if math.gcd(z,mod)==1})} for mod in [8,9,25,49]}
out['unit_square_classes']['scope']='The mod8 dyadic and odd prime-power checks illustrate the counts; the p-adic assertions use Hensel lifting, proved in root_proofs.md.'
F=s.Matrix([[0,-p],[1,0]]);V=-F
out['slope_half_rank2']={'F':str(F),'F_squared':str(F*F),'det_F':str(F.det()),'FV':str(F*V),'tensor_FV':str(s.kronecker_product(F,F)*s.kronecker_product(V,V)),'scope':'linear model over a field where Frobenius on coefficients is trivial; semilinear identities require the indicated coefficient twists'}
assert F*F==-p*s.eye(2) and F*V==p*s.eye(2)

At=s.Matrix([[1,-2*t],[0,-1]]);g=s.Matrix([[1,t],[0,1]])
out['involutions_GL2']={'A_t':str(At),'square':str(At**2),'conjugate':str(g*s.diag(1,-1)*g.inv()),'conclusion':'infinitely many homomorphisms μ2→GL2 in one conjugacy orbit; this does not show all are admissible polarizations'}
assert At**2==s.eye(2) and g*s.diag(1,-1)*g.inv()==At
out['torus_mu2']={'rank_counts':{str(r):2**r for r in range(7)},'opposite_cocharacters':'n=1 and n=−1 have equal reduction modulo2 and opposite signed rays'}
out['effectivity_dual_test']={'q':3,'n':1,'tate_eigenvalue':'3','dual_eigenvalue':'1/3','dual_is_algebraic_integer':False,'scope':'refutes unrestricted every-representation integrality in a rigid category containing a nontrivial Tate object; does not refute a correctly restricted effective-category criterion'}

vec=list(itertools.product((0,1),repeat=3))
plus=lambda v,w:tuple(vi^wi for vi,wi in zip(v,w))
b=lambda v,w:(v[0]*w[1]+v[1]*w[0])%2
perm=lambda v:(v[0],v[2],v[1])
alpha=lambda v,w:v[0]*(w[1]+w[2])%2
count=0
for u,v,w in itertools.product(vec,repeat=3):
 assert b(u,plus(v,w))==(b(u,v)+b(u,w))%2
 assert b(plus(u,v),w)==(b(u,w)+b(v,w))%2
 assert (alpha(v,w)+alpha(u,plus(v,w))-alpha(u,v)-alpha(plus(u,v),w))%2==0
 count+=1
for v,w in itertools.product(vec,repeat=2):
 assert b(v,w)==b(w,v) and b(v,v)==0
 assert (b(perm(v),perm(w))-b(v,w))%2==(alpha(v,w)+alpha(w,v))%2
out['Picard_counterexample']={'objects':'F2³','automorphisms_at_each_object':'F2','commutor':'b(x,y)=x1*y2+x2*y1','functor':'swap coordinates2and3; initially zero tensorator','witness':{'x':[1,0,0],'y':[0,1,0],'original_b':b((1,0,0),(0,1,0)),'transported_b':b(perm((1,0,0)),perm((0,1,0)))},'triple_checks':count,'pair_checks':64,'repair':'alpha(x,y)=x1*(y2+y3) is normalized bilinear2cocycle; corrected tensorator makes the underlying functor symmetric','scope':'literal broad autoisomorphism reading only; Codex auto-intérieurs alternative is not refuted'}

rad=1+2*p*M/D*s.log(1-a*t)
wrong=p*a*(1-s.sqrt(rad));right=(1-s.sqrt(rad))/(p*a)
out['ODE_initial_derivative']={'printed_derivative':str(s.diff(wrong,t).subs(t,0)),'required_derivative':str(M/D),'corrected_derivative':str(s.diff(right,t).subs(t,0)),'ratio_printed_to_required':str(s.simplify(s.diff(wrong,t).subs(t,0)/(M/D))),'corrected_symbolic_residual':str(s.simplify(s.diff(right,t)-M/((1-a*t)*(1-p*a*right)*D)))}
assert s.simplify(s.diff(right,t)-M/((1-a*t)*(1-p*a*right)*D))==0
bad=1-sum(s.binomial(2*n,n)*x**n for n in range(1,7));good=1-sum(s.binomial(2*n,n)*x**n/s.Integer(2*n-1) for n in range(1,7))
out['binomial_identity']={'printed_square_through_x5':str(s.series(bad*bad,x,0,6)),'corrected_square_through_x5':str(s.series(good*good,x,0,6)),'coefficient_x2_printed':int(s.expand(bad*bad).coeff(x,2))}
assert s.expand(bad*bad).coeff(x,2)==-8 and s.series(good*good,x,0,6).removeO()==1-4*x
out['majorant_direction']={'alpha':1,'beta':2,'M':10,'first_failing_degree':next(n for n in range(100) if 2**n>10),'general_proof':'if beta/alpha>1, (beta/alpha)^n is unbounded, so no finiteM works for alln'}
out['Legendre_minus1']=[{'prime':q,'minus1_is_square':any(z*z%q==q-1 for z in range(q)),'p_mod4':q%4} for q in [3,5,7,11,13,17,19,23,29,31]]
assert all(row['minus1_is_square']==(row['p_mod4']==1) for row in out['Legendre_minus1'])

jcases=[]
for q in [5,7,11,13,17,19,23,29,31,37,41,43]:
 h0=int(s.Poly((x**3+1)**((q-1)//2),x).coeff_monomial(x**(q-1)))%q
 h1728=int(s.Poly((x**3+x)**((q-1)//2),x).coeff_monomial(x**(q-1)))%q
 assert (h0==0)==(q%3==2)
 assert (h1728==0)==(q%4==3)
 jcases.append({'p':q,'Hasse_j0':h0,'Hasse_j1728':h1728})
out['exceptional_j']={'automorphism_orders_over_algebraic_closure_char_not_2_3':{'j0':6,'j1728':4},'equations':'(x,y)↦(u²x,u³y); j0 requiresu^6=1,j1728 requiresu^4=1','hasse_checks':jcases,'scope':'finite arithmetic checks support, but do not replace, the general Hasse-coefficient proof recorded separately'}

def cartan(n):
 C=2*s.eye(n)
 for i in range(n-2):C[i,i+1]=C[i+1,i]=-1
 C[2,n-1]=C[n-1,2]=-1
 return C
def roots(C):
 n=C.rows;seen=set();todo=[]
 for i in range(n):
  r=tuple(int(i==j) for j in range(n));todo.append(r);seen.add(r)
 while todo:
  r=todo.pop();v=s.Matrix(r);cv=C*v
  for j in range(n):
   rr=list(r);rr[j]-=int(cv[j]);rr=tuple(rr)
   if rr not in seen:seen.add(rr);todo.append(rr)
 return seen
rootout={}
for n,ell in [(6,3),(7,2)]:
 C=cartan(n);R=roots(C)
 images={tuple(int(y)%ell for y in C*s.Matrix(r)) for r in R}
 QPindex=ell**n//int(C.det())
 assert all((s.Matrix(r).T*C*s.Matrix(r))[0]==2 for r in R)
 assert all(z.q==1 for z in ell*C.inv())
 rootout[f'E{n}']={'Cartan_matrix':[list(map(int,C.row(j))) for j in range(n)],'determinant':int(C.det()),'root_count':len(R),'index_Q_over_ellP':QPindex,'distinct_root_images_Cr_mod_ell':len(images),'all_root_norms':2}
assert rootout['E6']['root_count']==72 and rootout['E6']['distinct_root_images_Cr_mod_ell']==72
assert rootout['E7']['root_count']==126 and rootout['E7']['distinct_root_images_Cr_mod_ell']==63
sp6=2**9*math.prod(2**(2*i)-1 for i in range(1,4))
so5=3**4*(3**2-1)*(3**4-1)
rootout['orders']={'Sp6_F2':sp6,'W_E7':2*sp6,'SO5_F3':so5,'O5_F3':2*so5,'Omega5_F3':so5//2,'W_E6':math.prod([2,5,6,8,9,12])}
assert sp6==1451520 and so5==51840
out['exceptional_root_lattices']=rootout

e=s.Matrix([[0,1],[0,0]]);f=s.Matrix([[0,0],[1,0]]);h=s.diag(1,-1)
br=lambda u,v:u*v-v*u
K=lambda u,v:4*s.trace(u*v)
out['sl2_orthogonals']={'basis':'e,h,f','Killing_Gram':str(s.Matrix([[K(u,v) for v in [e,h,f]] for u in [e,h,f]])),'e_perp_basis':'e,h = b+','f_perp_basis':'h,f = b−','printed_crossed_borel_formula':'false in sl2; candidate swap the signs','brackets':{'[h,e]':str(br(h,e)),'[h,f]':str(br(h,f)),'[e,f]':str(br(e,f))}}
assert K(e,e)==K(e,h)==0 and K(e,f)!=0
mod2=lambda B:B.applyfunc(lambda z:int(z)%2)
out['sl2_char2']={'h_mod2':str(mod2(h)),'[e,f]':str(mod2(br(e,f))),'[h,e]':str(mod2(br(h,e))),'[h,f]':str(mod2(br(h,f))),'lower_central_series_dimensions':[3,1,0],'scope':'matrix Lie algebra sl2 over characteristic2; nilpotent of class2, so characteristic0 statements require their hypothesis'}
out['norm_character_lattices']={'Res_Qi_Gm_rational_cocharacters':'(n,n), n∈Z','norm_composite':'2n','section_of_norm_exists':False,'weight_two_lift':'n=1','relative_norm_vs_absolute':'N_L/K rho=epsilon implies N_L/Q rho=epsilon^[K:Q]','real_factor_relation':'2*rho=epsilon in character notation; absolute trace contributes degree multiplicity','disconnected_density_example':'T[3] for T=ker(N_Q(i)/Q); Q(i) has no primitive cube root, so T[3](Q)={1} although T[3] is nontrivial'}
out['real_comparison_involutions']={'setup':'c:VB⊗C→VdR⊗C; cbar=τ_dR c τ_B where τ_B,τ_dR are scalar conjugations; real structure gives c τ_geom=τ_dR c τ_B','transported_product':'τ_geom = τ_B (c^-1 τ_dR c) = (c^-1 τ_dR c) τ_B if real comparison equivariance holds','one_Tate_period':'c=2πi, so transported deRham conjugation=−ordinary conjugation and product=−1','scope':'algebraic consequence of equivariant comparison; the manuscript’s two labels and degree conventions must be matched before applying it'}
out['timestamp']=datetime.datetime.now(datetime.timezone.utc).isoformat()
(OUT/'root_computations_output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'groups':len(out)-1,'checks':'all exact assertions passed','output':str(OUT/'root_computations_output.json')},indent=2))
