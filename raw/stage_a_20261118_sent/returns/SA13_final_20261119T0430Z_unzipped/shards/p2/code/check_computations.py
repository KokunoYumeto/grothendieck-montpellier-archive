#!/usr/bin/env python3
"""Explicit certificates for the P2 dossier. Finite tests are labelled as such.
Run: python deliverable/shards/p2/code/check_computations.py
No test outcome is used to manufacture a note verdict.
"""
from fractions import Fraction
import itertools, json, math
import sympy as s

out={}
q=7
cubes=sorted({pow(x,3,q) for x in range(1,q)})
out['finite_field_global_ext']={'field':q,'coefficients':3,'nonzero_cubes':cubes,'quotient_order':(q-1)//len(cubes),'meaning':'Kummer gives H^1(F_7,mu_3)=F_7^*/F_7^{*3}, nonzero; dimension-zero global Ext bound 0 fails.'}
assert cubes==[1,6]

x,y,z,w,a,b=s.symbols('x y z w a b')
fermat=x**4+y**4+z**4+w**4
restriction=s.expand(fermat.subs({x:a*y,z:b*w}))
remainder=s.rem(s.Poly(restriction,a),s.Poly(a**4+1,a)).as_expr()
remainder=s.rem(s.Poly(remainder,b),s.Poly(b**4+1,b)).as_expr()
assert remainder==0
out['fermat_quartic']={'restriction':str(restriction),'remainder_mod_a4plus1_b4plus1':str(remainder),'gradient':[str(s.diff(fermat,t)) for t in (x,y,z,w)],'intersection_obstruction':'H.L=1; H^2=4, so L=mH would require m=1/4, impossible for integral m. Gradient zero only at origin in characteristic zero.'}

# In the arrow category Vec(F_2)^{0 -> 1}: E=(k --id--> k),
# A=(0 -> k), B=(k -> 0). A section B->E must have s_0=id
# and s_1=0; the arrow square would require id=0.
arrow_sections=[(u,v) for u,v in itertools.product(range(2),repeat=2) if u==1 and v==0 and u==0]
assert not arrow_sections
out['arrow_category_injective_stalks']={'splitting_sections':arrow_sections,'meaning':'All objectwise k-vector spaces are injective modules, but 0->A->E->B->0 is nonsplit as a sheaf on the finite Alexandrov arrow site.'}

out['tame_multiplication']=[{'n':n,'e':e,'kernel_size':sum((e*x)%n==0 for x in range(n)),'image_size':len({(e*x)%n for x in range(n)}),'predicted_kernel':math.gcd(e,n)} for n,e in [(9,3),(8,6),(5,6),(7,1)]]
assert all(t['kernel_size']==t['predicted_kernel'] for t in out['tame_multiplication'])
out['shift_convention']=[{'r':r,'degree_of_k_shift_r':-r,'degree_of_derived_dual':r} for r in [-2,-1,0,1,2]]

# Hilbert-space example: g_n=e_0+e_n/n, h_n=e_n/n for n>=1.
# Their span contains every e_n (n>=1) and e_0=g_n-h_n!  That
# tempting example is invalid; use g_n=e_0+e_n/n alone instead.
# e_0 is a norm limit of g_n, and e_n=n(g_n-e_0) lies in the closure;
# no finite linear combination of g_n equals e_0.
out['hilbert_dense_hyperplane_example']={'generators':'g_n=e_0+e_n/n only','squared_distance_gn_e0':[str(Fraction(1,n*n)) for n in range(1,7)],'proof':'Any finite sum sum a_n g_n=e_0 forces all a_n/n=0 in coordinates n>=1, then coefficient e_0=0. Thus e_0 not in G but closure G=H. Weak topology sigma(H,G) has continuous dual G, so unit ball has no supporting continuous hyperplane at e_0.'}

# Exact generic Gegenbauer integral formula with finite beta sums. The
# manuscript's w_p and missing n cannot be reconstructed from this alone.
t=s.symbols('t',positive=True)
gegen=[]
for lam in [s.Rational(1,2),s.Rational(3,2)]:
 for n in range(6):
  poly=s.expand(s.gegenbauer(n,lam,t))
  parity=s.simplify(poly.subs(t,-t)-(-1)**n*poly)
  assert parity==0
  I=0;J=0
  for (d,),co in s.Poly(poly,t).terms():
   aa=s.Rational(d+1,2);bb=lam+s.Rational(1,2)
   B=s.gamma(aa)*s.gamma(bb)/s.gamma(aa+bb)
   I+=co*B/2
   J+=co*B*(s.digamma(aa)-s.digamma(aa+bb))/4
  integrand=s.expand(poly*(1-t*t)**(lam-s.Rational(1,2)))
  direct_I=s.integrate(integrand,(t,0,1))
  direct_J=s.integrate(integrand*s.log(t),(t,0,1))
  assert s.simplify(I-direct_I)==0 and s.simplify(J-direct_J)==0
  gegen.append({'lambda':str(lam),'n':n,'C_n':str(poly),'I':str(s.simplify(I)),'J_log':str(s.simplify(J)),'C_n_at_1':str(poly.subs(t,1))})
out['gegenbauer_checks']=gegen

# Codex scan 25: V additive with C2 acting by -1. Every (a,-1)
# has order two and gives a distinct complement. All are conjugate.
def affine_mul(g,h): return (g[0]+g[1]*h[0],g[1]*h[1])
out['nonunique_splittings']=[{'a':a,'square':affine_mul((a,-1),(a,-1)),'conjugate_standard_by_a_over_2':affine_mul(affine_mul((Fraction(a,2),1),(0,-1)),(-Fraction(a,2),1))} for a in [0,1,2]]
assert all(r['square']==(0,1) for r in out['nonunique_splittings'])
out['unipotent_characteristic_polynomial']={'identity_2':str(s.eye(2).charpoly(t).as_expr()),'printed_alternative':str(t*t-1),'difference':str(s.expand((t-1)**2-(t*t-1)))}

# Trace need be an integer, not nonnegative: the C2-action -1 on
# H^1 of an elliptic curve has trace -2.
out['negative_inertia_trace']={'matrix':str(-s.eye(2)),'trace':int(s.trace(-s.eye(2))),'geometric_realization':'Quadratic twist over C((t)) of a constant elliptic curve; tame inertia involution acts by [-1].'}

# Elliptic CM twist: E:y^2=x^3-x, E_t:y^2=x^3-t^2*x.
# Over sqrt(t), x=tX,y=t*sqrt(t)Y gives E; v_t(discriminant)=6.
T,X,Y,u=s.symbols('T X Y u')
twisted=(u**3*Y)**2-(u**2*X)**3+u**4*(u**2*X)
assert s.expand(twisted-u**6*(Y*Y-X**3+X))==0
out['nonconstant_extension_needed']={'equation':'y^2=x^3-t^2*x over Q(t)','discriminant':'64*t^6','change_over_t_equal_u2':str(s.factor(twisted)),'obstruction':'t is not a square in k_prime(t) for any finite constant field extension k_prime/Q, since v_t(t)=1. Inertia at t=0 acts nontrivially on T_l for odd l. The constant abelian variety after descent has trivial geometric inertia; an isogeny would preserve rational Tate representations.'}

# Invariants versus coinvariants: two generators on a two-dimensional
# vector space can share an invariant covector but no invariant vector.
A=s.Matrix([[2,0],[0,1]]); B=s.Matrix([[1,1],[0,1]])
common_kernel=(A-s.eye(2)).col_join(B-s.eye(2)).nullspace()
span_images=(A-s.eye(2)).row_join(B-s.eye(2))
out['invariants_vs_coinvariants']={'matrices':[str(A),str(B)],'common_invariant_dimension':len(common_kernel),'coinvariant_dimension':2-span_images.rank(),'meaning':'Finite-generation alone does not identify invariants and coinvariants for a non-procyclic acting group. This is a linear-algebra example, not the manuscript local-field example.'}
assert len(common_kernel)==0 and 2-span_images.rank()==1

out['finite_kernel_cokernel']=[{'l':ell,'matrix':M,'kernel':sum(all(sum(M[i][j]*v[j] for j in range(2))%ell==0 for i in range(2)) for v in itertools.product(range(ell),repeat=2)),'cokernel':ell**2//len({tuple(sum(M[i][j]*v[j] for j in range(2))%ell for i in range(2)) for v in itertools.product(range(ell),repeat=2)})} for ell,M in [(2,[[0,0],[0,1]]),(3,[[1,1],[0,0]]),(5,[[1,0],[0,1]])]]
assert all(r['kernel']==r['cokernel'] for r in out['finite_kernel_cokernel'])
print(json.dumps(out,ensure_ascii=False,indent=2,default=str))
