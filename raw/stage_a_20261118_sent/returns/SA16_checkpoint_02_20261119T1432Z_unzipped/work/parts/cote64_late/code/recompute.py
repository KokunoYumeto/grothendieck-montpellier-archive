"""Exact computations independently rerun for late cote64.
No manuscript reading is altered. Symbolic certificates prove rational/polynomial
identities on their declared domains; finite-field examples are only examples.
"""
import sympy as s, itertools, json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'outputs'
records=[]
def emit(key, result, scope):
 print('\n### '+key+'\n'+str(result)+'\nScope: '+scope)
 records.append(dict(key=key,result=str(result),scope=scope))
def zero(e):
 q=s.factor(e); assert q==0,q; return q
x,y,z,t,l,a1,a2,a3,b,r,u,v,m=s.symbols('x y z t l a1 a2 a3 b r u v m')
# 78: a comparison example, explicitly not an equation on the page.
i=s.I; si=1-i
emit('Q0_example', {'s_i^4':s.expand(si**4),'quotient':s.expand(-si**2/2),'s_minus_i / s_i':s.simplify((1+i)/si)},'Own/earlier-run comparison over Z[1/2,i], not manuscript polynomial.')
# 80 tensor powers, basic degree certificate.
emit('tensor_degree_counterexample', {'deg_M':1,'deg_Msharp_squared':2,'deg_Mb':1},'Trivial torsors on P1_C, M=O(1); different degrees prohibit isomorphism.')
# 90--92 finite group with multiplication C3 semidirect C4.
G=list(itertools.product(range(3),range(4))); one=(0,0)
def mul(g,h):return ((g[0]+(-1)**g[1]*h[0])%3,(g[1]+h[1])%4)
def inv(g):return next(h for h in G if mul(g,h)==one and mul(h,g)==one)
def order(g):
 q=one
 for n in range(1,13):
  q=mul(q,g)
  if q==one:return n
comm={mul(mul(mul(g,h),inv(g)),inv(h)) for g in G for h in G}
centre=[g for g in G if all(mul(g,h)==mul(h,g) for h in G)]
emit('D3prime',{'order':len(G),'commutators':sorted(comm),'centre':centre,'odd_lift_orders':sorted(set(order(g) for g in G if g[1]%2)),'quotient_C4':all(mul(g,h)[1]==(g[1]+h[1])%4 for g in G for h in G)},'Exact enumeration of defining 12-element group; every transposition lift has order4, so no splitting over S3.')
emit('line_characters',[(par,k,(par*(-1)**k), ((-1)**k)*par) for par in (1,-1) for k in range(4) if par==(-1)**k],'Pairs satisfying D3prime fibre product have scalar lambda² sign(g)=1.')
# Branch-coordinate conversions and exceptional points.
X=(1-t)*z/(z-t); X2=t*(z-1)/(z-t)
emit('branch_coordinates',{'first_at_0_1_inf':[s.simplify(X.subs(z,0)),s.simplify(X.subs(z,1)),s.limit(X,z,s.oo)],'second_at_0_1_inf':[s.simplify(X2.subs(z,0)),s.simplify(X2.subs(z,1)),s.limit(X2,z,s.oo)]},'t not0,1; both send z=t to infinity. Branch labels must be retained.')
j=256*(1-l+l*l)**3/(l*l*(1-l)**2)
emit('special_parameters',{'C3_fixed_numerator':s.factor(1-(1-l)*l),'j_harmonic':[s.simplify(j.subs(l,q)) for q in [-1,2,s.Rational(1,2)]],'char3_fixed':str(s.Poly(l*l-l+1,l,modulus=3).as_expr()),'char3_repeat':s.Poly((l+1)**2-(l*l-l+1),l,modulus=3).as_expr()},'Explicit standard Legendre comparison; not the manuscript branch-order convention.')
# 103: pole derivative, normalization.
n,c=s.symbols('n c')
emit('principal_parts',{'D(t^-n)':s.diff(t**(-n),t),'canonical_factor':-n,'multiplicative_rescaling_factor':-n*c,'c=-1/2':n/2},'Invariant vector has leading d/dt, pp_n is canonical; formula exact leading order.')
def basis(N):return [(j,0) for j in range(N//2+1)]+[(j,1) for j in range((N-3)//2+1)]
def rank_mod(A,p):
 A=[list(map(lambda q:int(q)%p,row)) for row in A]; rank=0
 for j in range(len(A[0]) if A else 0):
  k=next((k for k in range(rank,len(A)) if A[k][j]),None)
  if k is None:continue
  A[rank],A[k]=A[k],A[rank]; z=pow(A[rank][j],-1,p);A[rank]=[(z*q)%p for q in A[rank]]
  for k in range(len(A)):
   if k!=rank:
    z=A[k][j];A[k]=[(q-z*w)%p for q,w in zip(A[k],A[rank])]
  rank+=1
 return rank
checks=[]
for p in [3,5,7,11]:
 for N in range(0,4*p+3):
  src=basis(N); dst=basis(N+1); A=[[0 for _ in src] for _ in dst]
  for col,(j,k) in enumerate(src):
   # D x=y, D y=(3x²-1)/2 in y²=x³-x.
   terms={(j-1,1):j} if k==0 and j else {}
   if k:terms={(j+2,0):(2*j+3)*pow(2,-1,p),(j,0):-(2*j+1)*pow(2,-1,p)}
   for mon,coef in terms.items():
    if coef%p:A[dst.index(mon)][col]+=coef
  dim=len(src)-rank_mod(A,p); expected=max(1,N//p);assert dim==expected,(p,N,dim,expected)
  if N in (2*p-1,2*p,2*p+1):checks.append((p,N,dim))
emit('filtered_kernel_examples',checks,'Exact modular linear algebra on smooth y²=x³-x; universal proof is separate, not inferred from these samples.')
emit('basis_dimensions',[(N,len(basis(N)),sum(1 for j,k in basis(N) if not k),sum(1 for j,k in basis(N) if k)) for N in range(0,13)],'Weights x=2,y=3; coefficients and parity independent of generic cubic relation.')
# 105 ordinary and monic normalizations.
emit('leading_cubic',{'ordinary_x_lead':1,'ordinary_y_lead':-2,'ordinary_cubic_lead':4,'rescaled_x_lead':4,'rescaled_y_lead':-8,'rescaled_y²/x³':1},'delta identified with a unit parameter tangent; ε_n=(-1/2)^n pp_n permits monic equation.')
f=x**3+a1*x*x+a2*x+a3
new=s.Poly(s.expand(f.subs(x,x-b)),x)
emit('translated_cubic',new.all_coeffs(),'x_new=x_old+b; a1 changes by-3b, so tracezero unique only if3 invertible.')
wrong=x**3+a1*x*x+a2*x*x+a3
res=s.expand(2*y*s.diff(f,x)/2-s.diff(wrong,x)*y)
emit('cubic_derivation_residual',s.factor(res),'DP=y, Dy=fprime/2; a2*x² alternative is incompatible unless residual vanishes specially.')
vals=[-1/t,1/(1-t),0]; V=s.Matrix([[1,q,q*q] for q in vals])
emit('Vandermonde',s.factor(V.det()),'t not0,1; also injectivity of span{1,x} on three distinct branch images.')
roots=(x-r)*(x-u)*(x-v)
emit('root_coefficients',s.Poly(s.expand(roots),x).all_coeffs(),'Fixes signs of a1,a2,a3; final a3=-ruv.')
# Secant third intersection: factor on line y=m x+n0.
n0=s.symbols('n0'); third=m*m-a1-u-v
poly=s.expand(f-(m*x+n0)**2)
coeff=s.Poly(poly,x).all_coeffs()
emit('secant_coefficients',{'coefficients':coeff,'sum_roots':m*m-a1,'third_x':third,'third_y':s.expand(m*third+n0)},'u != v, line through both points. Third point is negative of sum; multiplicities permitted for third intersection.')
emit('determinant_repeated_counterexample',{'det':s.Matrix([[1,0,0],[1,1,0],[1,0,0]]).det(),'sum':'(0,0)+(1,0)+(0,0)=(1,0), not O'},'All points on smooth y²=x³-x over Q; repeated-point counterexample excluded by author correction.')
# Mobius deck transformation and fourth division.
A=(r-u)*(r-v); sig=r+A/(x-r); MM=s.Matrix([[r,A-r*r],[1,-r]])
zero(s.factor((sig-r)**2-A).subs(x,r+s.sqrt(A)))
assert (MM*MM-A*s.eye(2)).applyfunc(s.factor)==s.zeros(2)
zero(s.together(roots.subs(x,sig)-A*A*roots/(x-r)**4))
a1r=-(r+u+v);a2r=r*u+r*v+u*v
correct=-(a1r*r+2*a2r-3*u*v); wrong=-(a1r*r+2*a2r+3*u*v)
zero(correct-A)
emit('Mobius_and_fourth_division',{'matrix_square':MM*MM,'fixed_polynomial':s.expand((x-r)**2-A),'correct_radical':s.factor(correct),'wrong_minus_correct':s.factor(wrong-correct),'r1u2v3_correct':correct.subs({r:1,u:2,v:3}),'r1u2v3_wrong':wrong.subs({r:1,u:2,v:3})},'Pairwise distinct roots; M²=A I and f(sigma x)=A² f(x)/(x-r)^4. Four halves per nonzero2-torsion point,12 total.')
# Cyclic differences.
z1,z2,z3=s.symbols('z1 z2 z3'); zs=[z1,z2,z3]
vv=s.Matrix([z2-z3,z3-z1,z1-z2]); ker=s.Matrix([[1,1,1],zs])*vv
assert ker.applyfunc(s.factor)==s.zeros(2,1)
delta=(z1-z2)*(z2-z3)*(z3-z1); f1v=vv/delta;f2v=-s.diag(z1,z2,z3)*vv/delta
rhs=[s.Matrix([0,1,-1])/(z2-z3),s.Matrix([-1,0,1])/(z3-z1),s.Matrix([1,-1,0])/(z1-z2)]
for zi,rr in zip(zs,rhs):assert (zi*f1v+f2v-rr).applyfunc(s.factor)==s.zeros(3,1)
emit('cyclic_difference_basis',{'kernel':ker,'Delta*f1':vv,'-Delta*f2':s.diag(*zs)*vv},'Three distinct roots; exact vector identities underlie123/125/126, not missing square normalization.')
# Complex structures and modular transformations.
xx,yy=s.symbols('xx yy',real=True,nonzero=True); JJ=s.Matrix([[-xx,xx*xx+yy*yy],[-1,xx]])/yy
assert (JJ*JJ+s.eye(2)).applyfunc(s.factor)==s.zeros(2)
emit('orientation_matrix',{'J':JJ,'J²':JJ*JJ,'det(e1,J e1)':JJ[1,0]},'Conjugate transport from C(z,1), yy>0; orientation is negative, as author later notes.')
aa,bb,cc,dd,ee,ff,gg,hh=s.symbols('a b c d e f g h'); Gm=s.Matrix([[aa,bb],[cc,dd]]);Hm=s.Matrix([[ee,ff],[gg,hh]])
# sigma uses adjugate, determinants=1; adjugates reverse multiplication identically.
def sigma(M):return s.diag(-1,1)*M.adjugate()*s.diag(-1,1)
assert (sigma(Gm*Hm)-sigma(Hm)*sigma(Gm)).applyfunc(s.factor)==s.zeros(2)
hT=(ee*t+ff)/(gg*t+hh); jprod=(cc*hT+dd)*(gg*t+hh); jgh=(Gm*Hm)[1,0]*t+(Gm*Hm)[1,1]
zero(jprod-jgh)
rho=lambda M:s.diag(1,-1)*M*s.diag(1,-1)
assert (rho(Gm*Hm)-rho(Gm)*rho(Hm)).applyfunc(s.factor)==s.zeros(2)
emit('modular_cocycles',{'sigma(g)':sigma(Gm),'rho(g)':rho(Gm),'cocycle_residual':s.factor(jprod-jgh)},'Universal polynomial adjugate/cocycle identities; modular actions additionally impose det=1.')
S=s.Matrix([[0,-1],[1,0]]);T=s.Matrix([[1,1],[0,1]])
emit('modular_matrices',{'S²':S*S,'(ST)³':(S*T)**3,'S T Sinv':S*T*S.inv(),'full_twist_image':(S*T)**3},'Conventions recorded; braid central full twist maps-I, kernel generator its square.')
# Free words, explicit lifts supplied by earlier run.
def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return tuple(out)
def winv(w):return tuple(-a for a in reversed(w))
def subst(w,A):
 out=()
 for a in w:out=red(out+(A[a] if a>0 else winv(A[-a])))
 return out
def comp(A,B):return {j:subst(B[j],A) for j in (1,2)}
def power(A,n):
 R={1:(1,),2:(2,)}
 for _ in range(n):R=comp(A,R)
 return R
Sa={1:(2,),2:(-1,)};Ta={1:(1,),2:(1,2)};ST3=power(comp(Sa,Ta),3);S2=power(Sa,2)
cword=(2,-1)
inner={j:red(cword+(j,)+winv(cword)) for j in (1,2)}
assert ST3==comp(inner,S2),(ST3,comp(inner,S2))
commword=(1,2,-1,-2)
emit('free_group_lifts',{'S4':power(Sa,4),'ST3':ST3,'Inn(yx^-1)S2':comp(inner,S2),'S_commutator':subst(commword,Sa),'T_commutator':subst(commword,Ta)},'Exact free reduction; relation is modulo inner automorphisms, not an equality of the naive lifts in Aut(F2).')
emit('frame_stabilizer',{'lambda':-1,'g':-s.eye(2),'action_on_period_pair':'(-1)^(-1) * (-I) = I','action_on_fibre':'z -> -z','fixed_points':'E[2], cardinality4 over C;3 nonzero'},'Refutes combined freeness already crossed out by author; separate factors free on frame base.')
# Quadratic algebra calculations.
alpha,beta,pi,h,rr,SS,uu=s.symbols('alpha beta pi h rr SS uu')
zero(s.expand((t+alpha)**2-(alpha*alpha-b)-(t*t+2*alpha*t+b)))
change=s.expand((alpha+pi*beta)**2-alpha*alpha)
emit('dyadic_obstruction',{'lift_change':change,'divided_by_pi':s.expand(change/pi),'after_b=pi²h_normalized_relation':'v²+(2alpha/pi)v+h=0, v=(S-alpha)/pi'},'2 in(pi); change in(pi²), so b modm² independent of lift. Missing integral generator proves nonnormality.')
P=rr*rr+4*h
zero(s.expand((2*uu-rr)**2-P-4*(uu*uu-rr*uu-h)))
emit('normalization_generator',{'identity':s.factor((2*uu-rr)**2-P),'discriminant':s.discriminant(uu*uu-rr*uu-h,uu),'derivative_square_mod_relation':s.rem((2*uu-rr)**2,s.Poly(uu*uu-rr*uu-h,uu).as_expr(),uu)},'u=(S+r)/2; discriminantP, derivative²=P in quotient, hence etale onD(P). Global normality proved separately.')
# All linear squares mod4 suffice for degree2 primitive polynomial; higher-degree terms of a root reduce away.
mod4=[]
for lam in range(8):
 roots4=[]
 for aa0,aa1 in itertools.product(range(4),repeat=2):
  pol=s.Poly((aa1*x+aa0)**2-x*(x-lam),x)
  if all(int(co)%4==0 for co in pol.all_coeffs()):roots4.append((aa0,aa1))
 mod4.append((lam,roots4))
emit('T_Tlambda_mod4',mod4,'Explicit residues; general proof coefficient comparison: root mod2 isT, every lift square≡T² mod4.')
zero(s.expand((1-4*m*x)-(2*uu-1)**2+4*(uu*uu-uu+m*x)))
emit('infinity_chart',{'S²/T²':s.simplify((t*(t-l))/t**2).subs(t,1/x),'normal_equation':uu*uu-uu+m*x,'infinity_fibre':uu*(uu-1),'wrong_sign_at_lambda4_x0':-1,'mod2_equation':'u²+u+(m mod2)x'},'lambda4m; correct radicand1-lambda*x, wrong one givesQ(i) atx0 and ramificationat2.')
emit('tangent_cone',{'general':'X²+bar(2alpha/pi)XY+bar(b/pi²)Y²','unramified_dyadic':'cross coefficient nonzero, separable binary quadratic','equal_characteristic2_cusp':'T²+pi³, tangent T²','ramified_mixed_char':'A=Z2[sqrt2],alpha1,a5,b=-4,pi=sqrt2: coneT²'},'Ordinary-node assertion requiresv(2)=1; no blanket quadratic-ordinary conclusion.')
# Separate earlier-run bridge: Picard--Fuchs exact identity.
F=x*(x-1)*(x-l)
# Divide all differential expressions bydx/y. Parameter derivative of1/y is-F_l/(2F)/y.
q1=-s.diff(F,l)/(2*F);q2=s.diff(q1,l)+q1*q1
Lratio=l*(1-l)*q2+(1-2*l)*q1-s.Rational(1,4)
B=x*(x-1)/(2*(x-l))
exactratio=s.diff(B,x)-B*s.diff(F,x)/(2*F)
zero(s.together(Lratio-exactratio))
p=(1-2*l)/(l*(1-l));q=-1/(4*l*(1-l))
sch=s.factor(2*q-s.diff(p,l)-p*p/2)
emit('Picard_Fuchs_bridge',{'exact_residual':s.factor(Lratio-exactratio),'Schwarzian':sch},'Independent calculation for characteristic0 standard Legendre; not a manuscript assertion.')
Hchecks=[]
for pp in [3,5,7,11,13]:
 mm=(pp-1)//2;H=sum(s.binomial(mm,k)**2*l**k for k in range(mm+1))
 LH=l*(1-l)*s.diff(H,l,2)+(1-2*l)*s.diff(H,l)-s.Rational(1,4)*H
 num=s.together(LH).as_numer_denom()[0]
 assert s.Poly(num,l,modulus=pp).is_zero
 coeff=s.Poly(s.expand(F**mm),x).coeff_monomial(x**(pp-1))
 assert s.Poly(coeff-(-1)**mm*H,l,modulus=pp).is_zero
 Hchecks.append((pp,str(s.Poly(H,l,modulus=pp).as_expr())))
emit('Hasse_bridge',Hchecks,'Exact tested odd primes; binomial formula and hypergeometric recurrence give allp, proof in proof_notes.md.')
def modrat(e,pp):
 nn,dd=s.cancel(e).as_numer_denom();return s.cancel(s.Poly(nn,l,modulus=pp).as_expr()/s.Poly(dd,l,modulus=pp).as_expr())
AA=s.Matrix([[0,1],[1/(4*l*(1-l)),-(1-2*l)/(l*(1-l))]])
BB=s.eye(2)
for k in range(3):BB=(BB.diff(l)-AA*BB).applyfunc(lambda e:modrat(e,3))
expected=s.Matrix([[-(l+1),(l+1)**2],[-1,l+1]])/(l*l*(l-1)**2)
assert (BB-expected).applyfunc(lambda e:modrat(e,3))==s.zeros(2),(BB,expected)
assert (BB*BB).applyfunc(lambda e:modrat(e,3))==s.zeros(2)
emit('p_curvature_bridge',{'matrix':BB,'at_supersingular_minus1':BB.subs(l,-1).applyfunc(lambda e:modrat(e,3)),'square':(BB*BB).applyfunc(lambda e:modrat(e,3))},'ExactF3(lambda) computation of(∂-A)^3 since∂^[3]=0; nonzero squarezero, also atlambda=-1.')
OUT.joinpath('computation_records.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
print('\nALL EXACT ASSERTIONS PASSED. '+str(len(records))+' computation groups.')
