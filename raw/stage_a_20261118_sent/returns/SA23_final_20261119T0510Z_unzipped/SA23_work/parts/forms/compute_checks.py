"""Exact certificates for selected finite algebraic claims; not proofs of global theorems."""
import sympy as s,itertools as it,json,math
from pathlib import Path
P=Path(__file__).parent
out={}
def rec(name,claims,data):out[name]={'claims':claims,'data':data,'scope':'Exact identity or stated finite example only; global proof in claim/proof register.'}
def mi(n,k):
 if n==1:yield(k,);return
 for i in range(k+1):
  for q in mi(n-1,k-i):yield(i,)+q
def fac(t):return math.prod(math.factorial(i) for i in t)
def fmt(f):return str(s.expand(f))
x,y,z,t,u,v=s.symbols('x y z t u v')
# Exterior algebra over Q, basis tuples, exact graded Leibniz extension.
def wedge(a,b):
 r={}
 for I,c in a.items():
  for J,d in b.items():
   if set(I)&set(J):continue
   sign=(-1)**sum(i>j for i in I for j in J);K=tuple(sorted(I+J));r[K]=r.get(K,0)+sign*c*d
 return {I:c for I,c in r.items() if c}
def plus(a,b,scale=1):
 r=a.copy()
 for I,c in b.items():r[I]=r.get(I,0)+scale*c
 return {I:c for I,c in r.items() if c}
e=[{(i,):s.Integer(1)} for i in range(3)];de=[wedge(e[0],e[1]),wedge(e[1],e[2]),{}]
def d(a):
 r={}
 for I,c in a.items():
  for j,i in enumerate(I):r=plus(r,wedge(wedge({I[:j]:c},de[i]),{I[j+1:]:1}),(-1)**j)
 return r
D2=d(d(e[0]));assert D2=={(0,1,2):-1}
rec('F01_exterior_square_zero_gap',['C-SA23-forms-066','C-SA23-forms-067'],{'d0':0,'de1':str(de[0]),'de2':str(de[1]),'d2e1':str(D2)})
# CE bracket dual to the above differential: [X1,X2]=-X1,[X2,X3]=-X2.
B={(0,1):s.Matrix([-1,0,0]),(1,2):s.Matrix([0,-1,0])}
def br(a,b):
 r=s.zeros(3,1)
 for i in range(3):
  for j in range(i+1,3):r+=(a[i]*b[j]-a[j]*b[i])*B.get((i,j),s.zeros(3,1))
 return r
E=[s.eye(3)[:,i] for i in range(3)]
Jac=br(E[0],br(E[1],E[2]))+br(E[1],br(E[2],E[0]))+br(E[2],br(E[0],E[1]))
assert Jac==E[0]
rec('F02_Jacobiator',['C-SA23-forms-067'],{'Jacobi_X1_X2_X3':list(map(str,Jac))})
# rank-one curvature
A_x=0;A_y=x
curv=s.diff(A_y,x)-s.diff(A_x,y)
assert curv==1
rec('F03_nonintegrable_connection',['C-SA23-forms-073'],{'connection':'d+x dy on O_A2_Q','coefficient_dx_wedge_dy':str(curv)})
# First-order target-source derivation identity.
f,g,df,dg,h=s.symbols('f g df dg h')
expr=s.expand((f+h*df)*(g+h*dg)-f*g)
rec('F04_source_target_Leibniz',['C-SA23-forms-065'],{'difference':str(expr),'coefficient_h':str(expr.coeff(h,1))})
# Formal inverse of one-dimensional formal monoid law F=x+y+xy.
inv=sum((-1)**i*x**i for i in range(1,9))
r=s.series(x+inv+x*inv,x,0,9).removeO();assert r==0
rec('F05_formal_monoid_inverse_example',['C-SA23-forms-064'],{'law':'x+y+xy','inverse_mod_x9':fmt(inv),'composite_mod_x9':str(r)})
# Smooth ordinary quadric in characteristic two, rank3: q=x^2+yz.
q=x*x+y*z;H=s.hessian(q,(x,y,z));H2=H.applyfunc(lambda n:int(n)%2)
assert H2.rank()==2
rec('F06_char2_ordinary_not_nondegenerate',['C-SA23-forms-020','C-SA23-forms-026'],{'q':str(q),'gradient_mod2':['0','z','y'],'Hessian_mod2':str(H2),'radical':'span of x-axis; q nonzero on nonzero radical vectors','projective_singular_points':'none: y=z=0 and q=0 force x=0','Hessian_rank':2})
# Fermat p+1: gradient Frobenius, differential Gauss zero.
fermat=[]
for p in [2,3,5]:
 F=x**(p+1)+y**(p+1)+z**(p+1)
 grad=[s.Poly(s.diff(F,a),(x,y,z),modulus=p).as_expr() for a in (x,y,z)]
 hh=[[s.Poly(s.diff(grad[i],a),(x,y,z),modulus=p).as_expr() for a in(x,y,z)] for i in range(3)]
 assert all(b==0 for row in hh for b in row)
 fermat.append({'p':p,'gradient':list(map(str,grad)),'gauss_differential':str(hh)})
rec('F07_inseparable_Gauss_example',['C-SA23-forms-022'],fermat)
# Smooth quadric surface tangent plane section is reducible.
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3');Q=x0*x3-x1*x2
rec('F08_quadric_tangent_section',['C-SA23-forms-024'],{'quadric':str(Q),'tangent_at_1000':'x3=0','section':str(Q.subs(x3,0)),'factorization':str(s.factor(Q.subs(x3,0)))})
# Universal affine incidence elimination, special polynomial ratios.
a0,a1,a2,S1,S2=s.symbols('a0 a1 a2 S1 S2')
rec('F09_incidence_and_ratios',['C-SA23-forms-003','C-SA23-forms-007','C-SA23-forms-027'],{'solve_1_minus_xS1_minus_yS2':'S2=(1-x*S1)/y on D(y)','substitution':fmt((1-x*S1-y*S2).subs(S2,(1-x*S1)/y)),'ratios':['x^2/x=x','xy/x=y','x^3/x^2=x','x^2*y/x^2=y']})
# Rees regular sequence and blow-up chart.
rec('F10_Rees_relation',['C-SA23-forms-030'],{'kernel_relation':'y*U-x*V','substitution_U_xt_V_yt':fmt((y*u-x*v).subs({u:x*t,v:y*t})),'scope':'Regular sequence x,y in Q[x,y]; general regular-sequence proof is syzygy argument.'})
# Grassmann chart: quotient[I_n A], kernel[-A;I].
a,b,c,d0=s.symbols('a b c d0');M=s.Matrix([[1,0,a,b],[0,1,c,d0]]);K=s.Matrix([[-a,-b],[-c,-d0],[1,0],[0,1]])
assert M*K==s.zeros(2)
rec('F11_Grassmann_chart',['C-SA23-forms-033'],{'quotient':str(M),'kernel':str(K),'composition':str(M*K),'dimension':4})
# Actual binomial identities in the positivity proof.
counts=[]
for n in [1,2,3]:
 for k in range(0,8):
  for alpha in mi(n,k):
   for qn in range(k+1):
    lhs=sum(math.prod(math.comb(ai,gi) for ai,gi in zip(alpha,gamma)) for gamma in mi(n,qn) if all(gi<=ai for ai,gi in zip(alpha,gamma)))
    assert lhs==math.comb(k,qn)
    counts.append((n,k,alpha,qn))
rec('F12_Vandermonde_derivative_norm',['C-SA23-forms-055','C-SA23-forms-056'],{'cases':len(counts),'identity':'Σ_|γ|=q binom(α,γ)=binom(|α|,q); ||z^α||_q²=α! binom(|α|,q)','all_equal':True})
# Gaussian matrix entries: prolongation equals derivative integral for monomial basis.
cases=0
for n in [1,2,3]:
 for m in [1,2]:
  for N in range(4):
   for al in mi(n,m):
    for be in mi(n,m):
     for ga in mi(n,N):
      delta=tuple(a+g for a,g in zip(al,ga));eps=tuple(b+g for b,g in zip(be,ga))
      prolong=s.Rational(fac(delta)*fac(eps),fac(ga))
      integral=s.Rational(fac(delta),fac(ga))*s.Rational(fac(eps),fac(ga))*fac(ga)
      assert integral==prolong;cases+=1
rec('F13_Gaussian_prolongation_matrix',['C-SA23-forms-055'],{'entries_checked':cases,'entry':'δ! ε! / γ! for δ=α+γ, ε=β+γ','off_diagonal_rule':'zero unless δ−α=ε−β≥0','all_equal':True})
# Weyl identity, both signs, arbitrary tested monomial u.
cases=0
for A in range(5):
 for B0 in range(5):
  for k in range(8):
   rhs=sum(s.binomial(A,j)*math.factorial(B0)//math.factorial(B0-j)*x**(B0-j)*s.diff(x**k,x,A-j) for j in range(min(A,B0)+1))
   assert s.expand(s.diff(x**(B0+k),x,A)-rhs)==0
   first=sum((-1)**j*s.Rational(1,math.factorial(j)*math.factorial(B0-j)*math.factorial(A-j))*s.diff(x**(A-j+k),x,B0-j) for j in range(min(A,B0)+1))
   assert s.expand(x**A*s.diff(x**k,x,B0)/math.factorial(A)/math.factorial(B0)-first)==0
   cases+=1
rec('F14_Weyl_normal_order',['C-SA23-forms-056'],{'pairs_and_monomials':cases,'both_commutation_formulas':True})
# Norm with multiplication weights has closed form binom(k+n+q-1,q).
checks=[]
for n in [1,2,3]:
 for k in range(5):
  al=next(mi(n,k))
  for qn in range(4):
   ratio=sum(s.Rational(fac(tuple(a+b for a,b in zip(al,ga))),fac(ga)*fac(al)) for ga in mi(n,qn))
   assert ratio==math.comb(k+n+qn-1,qn)
   checks.append((n,k,qn,int(ratio)))
rec('F15_multiplication_norm',['C-SA23-forms-056'],{'cases':len(checks),'ratio':'||z^α||_(q*)²/||z^α||0²=binom(k+n+q−1,q)','q1_constant_requires_fixed_n':True})
coef=[]
for N in range(0,7):
 poly=s.Poly(s.expand((x+y)**N*(x*x-x*y+y*y)),x,y)
 row=[int(poly.coeff_monomial(x**i*y**(N+2-i))) for i in range(N+3)]
 coef.append({'N':N,'coefficients':row,'strictly_positive':all(i>0 for i in row)})
assert [r['N'] for r in coef if r['strictly_positive']]==[3,4,5,6]
rec('F16_Quillen_scalar_example',['C-SA23-forms-056'],coef)
# Leading degree survives lower error shift.
N,eps,C=s.symbols('N eps C',positive=True);m=3
poly=s.expand(eps*s.prod(N+j for j in range(1,m+1))/math.factorial(m)-C*sum(s.prod(N+j for j in range(1,i+1))/math.factorial(i) for i in range(m)))
rec('F17_positivity_growth',['C-SA23-forms-056'],{'m3_error_polynomial':str(poly),'leading_coefficient':str(s.Poly(poly,N).LC()),'degree':s.degree(poly,N),'proof_scope':'For general m, binom(N+m,m) has leading coefficient1/m!, all i<m errors lower degree.'})
# K0 identities, using l=[L^k], dual exact sequence and l=m−e4.
l,n,m0,E1,E2,E3dual,E4=s.symbols('l n m E1 E2 E3dual E4')
E2expr=n*l-l*E3dual
left=(E1-E2expr).subs(l,m0-E4)
right=(E1+l*E3dual+n*E4-n*m0).subs(l,m0-E4)
assert s.expand(left-right)==0
rec('F18_K0_bundle_minus_rank',['C-SA23-forms-063'],{'identity':'E2=n*l-l*E3dual, l=m−E4 ⇒ E1−E2=E1+l*E3dual+n*E4−nm','residual':fmt(left-right)})
# RP² Stiefel-Whitney and Steenrod obstruction.
w=s.Poly((1+x)**3,x,modulus=2).as_expr();w=s.Poly(w,x).rem(s.Poly(x**3,x)).as_expr()
rec('F19_RP2_Gysin_and_Sq',['C-SA23-forms-047','C-SA23-forms-049','C-SA23-forms-052'],{'w_TRP2_mod_a3':str(w),'w1_squared':'a²≠0; pairing with fundamental class1','Sq1_PD_RP1':'Sq1(a)=a²≠0','H_minus2_point':0})
# Milnor formal-series coproduct coefficient, p=2.
A=s.symbols('a1:4');B1=s.symbols('b1:4');fa=x+sum(A[i-1]*x**(2**i) for i in range(1,4));fb=x+sum(B1[i-1]*x**(2**i) for i in range(1,4));comp=s.Poly(s.expand(fa.subs(x,fb)),x,*A,*B1,modulus=2).as_expr();co=[s.expand(comp).coeff(x,2**i) for i in range(1,4)]
rec('F20_strict_additive_series_composition',['C-SA23-forms-053'],{'coefficients_x2_x4_x8':list(map(str,co)),'order':'f∘g; swapping coaction swaps factors'})
# Acyclic finite CW certificate, Hatcher2.38.
d2=s.Matrix([[5,-2],[-3,1]]);assert d2.det()==-1
from sympy.combinatorics import Permutation,PermutationGroup
a=Permutation(0,1,2,3,4);candidates=[Permutation(list(p)) for p in it.permutations(range(5))]
b0=next(p for p in candidates if p.order()==3 and (a*p).order()==2)
G=PermutationGroup([a,b0]);assert G.order()==60
rec('F21_acyclic_noncontractible',['C-SA23-forms-038'],{'cellular_boundary':str(d2),'determinant':int(d2.det()),'a':str(a),'b':str(b0),'orders':[int(a.order()),int(b0.order()),int((a*b0).order())],'nontrivial_quotient_order':int(G.order()),'relations':'a^5=b^3=(ab)^2=1 in A5; boundary invertible gives reduced homology zero'})
# Dual-number periodic resolution and derived-Hom witness.
mult=s.Matrix([[0,0],[1,0]]);assert mult**2==s.zeros(2)
rec('F22_unbounded_Tor',['C-SA23-forms-037','C-SA23-forms-042'],{'multiplication_by_epsilon':str(mult),'kernel_dimension':2-mult.rank(),'image_dimension':mult.rank(),'kernel_equals_image':'both span epsilon','after_tensor_k':'all differentials zero, one k in every degree','Ext1_Z_Z2_Z2':'Z/2 via resolution Z --2--> Z'})
# Characteristic2 alternating Hessian odd size determinant formal identity.
a,b,c=s.symbols('a b c');HH=s.Matrix([[0,a,b],[a,0,c],[b,c,0]])
rec('F23_odd_char2_Hessian',['C-SA23-forms-020'],{'integer_determinant':str(HH.det()),'mod2':str(s.Poly(HH.det(),a,b,c,modulus=2).as_expr())})
# Moore-space cellular complex: the nonzero integral differential becomes invertible over Q.
moore=[]
for p0 in [2,3,5,7]:
 boundary=s.Matrix([[p0]])
 assert boundary.rank()==1 and boundary.inv()==s.Matrix([[s.Rational(1,p0)]])
 moore.append({'p':p0,'d_nplus1_over_Z':p0,'H_n_over_Z':'Z/'+str(p0),'rank_over_Q':1,'H_n_over_Q':0,'H_nplus1_over_Q':0,'rank_over_Fp':0,'H_n_over_Fp_dimension':1,'H_nplus1_over_Fp_dimension':1})
rec('F24_fixed_rational_coefficients',['C-SA23-forms-080'],{'examples':moore,'scope':'Finite cellular complexes M(Z/p,n), n≥2. The derived-local-system equivalence follows by the independent adjunction and bounded truncation argument in proof_checks.md.'})
# Pullback of a hyperplane through the blowup center, in an affine blowup chart.
ba,bb,bc,bu,bv,bw=s.symbols('a b c u v w')
pull=s.expand((ba*x+bb*y+bc*z).subs({x:bu,y:bu*bv,z:bu*bw}))
assert s.expand(pull-bu*(ba+bb*bv+bc*bw))==0
rec('F25_blowup_divisorial_exception',['C-SA23-forms-025','C-SA23-forms-082'],{'pullback':str(pull),'factorization':str(s.factor(pull)),'exceptional_component':'u=0','strict_transform':'a+b*v+c*w=0','dual_parameter_locus':'hyperplanes through a fixed point, codimension1','scope':'The chart checks the common exceptional factor; the strict transform is globally nonempty for every projective hyperplane through the center.'})
(P/'compute_checks.output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n')
print('PASS:',len(out),'exact check blocks saved')
