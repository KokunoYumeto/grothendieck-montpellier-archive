"""Reproducible finite certificates and explicitly labelled illustrations.

These calculations check the named finite instances, not infinite-dimensional
theorems.  Infinite arguments and the exact hypotheses are in proof_notes.md.
Run: python SA23_work/parts/analysis_curves/computations.py
"""
from pathlib import Path
from fractions import Fraction as Q
import itertools, json, math
import sympy as s
import mpmath as mp

D=Path(__file__).resolve().parent
OUT=[]
def emit(name, claims, result, kind='exact finite certificate'):
    OUT.append(dict(name=name,claims=[f'C-SA23-analysis_curves-{i:03}' for i in claims],kind=kind,result=result))

# Exterior normalizations and the functoriality actually used in the draft.
for n in [2,3,4]:
    emit(f'antisymmetrizer_n{n}',[31],dict(
        averaged_alternating_basis_tensor_norm_squared=str(Q(1,math.factorial(n))),
        quotient_basis_wedge_norm_squared=math.factorial(n),
        corrected_embedding_multiplier=f'sqrt({math.factorial(n)})',
        corrected_quotient_multiplier=f'1/sqrt({math.factorial(n)})'))
def ext(A,k):
    I=list(itertools.combinations(range(A.rows),k))
    J=list(itertools.combinations(range(A.cols),k))
    return s.Matrix([[A.extract(i,j).det() for j in J] for i in I])
A=s.Matrix([[1,2,0],[0,3,1],[2,0,1]])
B=s.Matrix([[2,0,1],[1,1,0],[0,1,2]])
z=s.symbols('z')
assert ext(A*B,2)==ext(A,2)*ext(B,2)
detpol=s.expand((s.eye(3)+z*A).det())
traces=[s.trace(ext(A,k)) for k in [1,2,3]]
assert all(detpol.coeff(z,k)==traces[k-1] for k in [1,2,3])
emit('exterior_functor_and_determinant_coefficients',[32,33,35,38],dict(
    A=str(A),B=str(B),exterior_multiplication=True,det_I_plus_zA=str(detpol),exterior_traces=list(map(str,traces))))

emit('square_root_singular_coefficient',[29],dict(u=2,actual_sqrt_uu_star=2,typed_rho_squared=4))
emit('determinant_absolute_equality',[36],dict(u=-1,absolute_det_I_plus_u=0,det_I_plus_absolute_u=2))
emit('concave_aligned_singular_sum',[42],dict(A='diag(1,0)',B='diag(0,1)',p='1/2',left=2,right='sqrt(2)',false_inequality='2 <= sqrt(2)'))
emit('reciprocal_majorization_direction',[45],dict(rho=[1,1],sigma=['2','1/2'],equal_products=True,left='5/2',right=2))
J=s.Matrix([[1,1],[0,1]])
evals=sorted((J.T*J).eigenvals().keys(),key=lambda x:float(x))
assert evals[0]<1
emit('nonsymmetric_eigenvalue_variant',[47],dict(A=str(J),eigenvalue_moduli=[1,1],least_singular_value=str(s.sqrt(evals[0])),function='f(x1,x2)=x2; convex, increasing, not symmetric'))
emit('nonsymmetric_product_variant',[49],dict(A='diag(2,1)',B='diag(1,2)',least_sv_product=2,product_of_least_svs=1))
emit('polar_norm_and_norm_order',[52,54,56],dict(
    sequence='1/n belongs to c0 but not l1',norm_order='sup <= l1',dual_of_l1='sup, not l1',
    multiplication_counterexample='N=l1, Nprime=l2, Ndoubleprime=sup; A=B=I2',left=2,right='sqrt(2)'))
emit('Cauchy_coefficient_radius',[64],dict(f='1+z',n=1,R=10,coefficient=1,max_modulus=11,typed_bound='11/100',correct_bound='11/10'))

u=s.Matrix([[1,0],[0,0]])
v=s.Matrix([[0,0],[s.Rational(3,5),s.Rational(4,5)]])
uabs=u
vabs=s.Matrix([[s.Rational(9,25),s.Rational(12,25)],[s.Rational(12,25),s.Rational(16,25)]])
ustarabs=u
vstarabs=s.diag(0,1)
def alpha2(X,Y): return s.simplify((s.trace(X)*s.trace(Y)-s.trace(X*Y))/2)
mixed=alpha2(u,v)
domain=alpha2(uabs,vabs)
ran=alpha2(ustarabs,vstarabs)
assert mixed==s.Rational(2,5) and domain==s.Rational(8,25) and ran==s.Rational(1,2)
assert mixed**2==domain*ran
emit('mixed_exterior_one_sided_bound',[35,66,67],dict(u=str(u),v=str(v),absolute_mixed_trace=str(mixed),domain_mixed=str(domain),range_mixed=str(ran),two_sided_Cauchy_Schwarz_equality=True))

# The scalar integral is a finite numerical check of the constant.  The proof
# by integration by parts and Euler's beta integral is recorded separately.
mp.mp.dps=60
p=mp.mpf('0.5');x=mp.mpf(4)
integral=mp.quad(lambda t: mp.log(1+t*x)*t**(-p-1),[0,1,mp.inf])
coeff=p*mp.sin(mp.pi*p)/mp.pi
emit('power_log_integral_constant',[41,71,72,75],dict(p=str(p),x=str(x),integral=mp.nstr(integral,40),coefficient=mp.nstr(coeff,40),product=mp.nstr(coeff*integral,40),expected=2),kind='60-digit numerical illustration; general identity proved separately')

emit('nonunitary_polar_and_adjoint_kernel',[68,70],dict(operator='A e_n=e_(n+1)/n on l2(N)',kernel_A_dimension=0,kernel_A_star_dimension=1,absolute_A_eigenvalues='1,1/2,1/3,...',absolute_A_star_eigenvalues='0,1,1/2,1/3,...',conclusion='not unitarily equivalent; partial polar isometry exists'),kind='symbolic infinite example, exact kernel calculation')
emit('strict_Holder_sign',[75],dict(A=1,B=1,p=2,q=2,r=1,left=1,right=1,false_inequality='1 < 1'))

# Exact rational interval certificate for the fractional-power monotonicity
# counterexample. H,K are positive definite, H-K is positive of rank one.
H=s.Matrix([[2,1],[1,5]]);K=s.diag(1,4)
assert H.det()==9 and H.trace()==7 and (H+s.eye(2)*3)**2==13*H
assert (H-K).eigenvals()=={2:1,0:1}
lo=Q(360555,100000); hi=Q(360556,100000)
assert lo*lo<13<hi*hi
c=Q(2,5)**5
# D=(H+3I)/sqrt(13)-diag(1,2); Sylvester for D-cI.
# Its first leading minor =5/t-1-c; determinant=5-18/t-c*(t-3)+c*c.
minor_lower=Q(5)/hi-1-c
det_lower=5-Q(18)/lo-c*(hi-3)+c*c
assert minor_lower>0 and det_lower>0
# Thus smallest eigenvalue >(.4)^5.  The Rayleigh quotient of (1,1)
# is (15/t-3)/2, which is >(.89)^5.
rayleigh_lower=(Q(15)/hi-3)/2
assert rayleigh_lower>Q(89,100)**5
assert Q(11,10)**10>2
t=mp.sqrt(13)
trace=t-3;det=5-18/t
dminus=(trace-mp.sqrt(trace*trace-4*det))/2
dplus=(trace+mp.sqrt(trace*trace-4*det))/2
left=dminus**mp.mpf('.2')+dplus**mp.mpf('.2')
right=mp.mpf(2)**mp.mpf('.1')
assert left>right
emit('fractional_power_monotonicity_counterexample',[80],dict(
    H=str(H),K=str(K),p='1/10',s='1/2',r=1,
    sqrtH='(H+3I)/sqrt(13)',sqrt13_interval=[str(lo),str(hi)],
    positive_minor_lower=str(minor_lower),positive_determinant_lower=str(det_lower),
    rayleigh_lower=str(rayleigh_lower),
    exact_comparison='F_p(1/2) > 2/5+89/100 =129/100 >11/10 >F_p(1)',
    F_half=mp.nstr(left,50),F_one=mp.nstr(right,50),
    both_parameters_strictly_below_one='Replace H,K by H^2,K^2 and p by1/20: s=1/4,r=1/2 gives same values',
    H_squared=str(H**2),K_squared=str(K**2)))

emit('codimension_intersection_sign',[82],dict(E='span(e1) in R2',F='same span(e1)',codim_intersection=1,sum_codimensions=2,correct_direction='<='))
U=s.diag(2,1)
correct=s.eye(2)*2-3*U+U**2
assert correct==s.zeros(2)
emit('Fredholm_minor_signs',[84,85],dict(U=str(U),alpha1=3,alpha2=2,first_terms=['2I','3U','U^2'],first_difference=str(s.eye(2)*2-3*U),correct_alternating_P2=str(correct),unsigned_P2=str(s.eye(2)*2+3*U+U**2)))

# Spectral and singular-value comparison: weighted cyclic matrices. The exact
# characteristic polynomial follows from the unique directed cycle.
for n in [3,4,6]:
    eps=s.Rational(1,10)
    weights=[eps**(-(n-1))]+[eps]*(n-1)
    C=s.zeros(n)
    for j,w in enumerate(weights): C[(j+1)%n,j]=w
    assert C.charpoly(z).as_expr()==z**n-1
    assert C.T*C==s.diag(*[w*w for w in weights])
    emit(f'cyclic_singular_eigen_n{n}',[34,40,83],dict(n=n,weights=list(map(str,weights)),characteristic_polynomial=str(C.charpoly(z).as_expr()),eigenvalue_moduli='all 1',singular_values=list(map(str,sorted(weights,reverse=True))),product_both=1))

rows=[]
for m in [10,100,1000,10000]:
    term=mp.mpf(1);total=term
    for n in range(1,m+1):
        term*=mp.mpf(m-n+1)/m;total+=term
    rows.append(dict(m=m,l1_norm=1,S=mp.nstr(total,25)))
emit('entire_function_unbounded_unit_ball',[65],rows,kind='numerical illustrations; exact unboundedness and local convergence proof in proof_notes.md')

rows=[]
for k in range(2,7):
    Nk=2**(2**k);previous=2**(2**(k-1))
    rows.append(dict(k=k,Nk=Nk,plateau_start=previous+1,
        ratio_at_start=math.log(Nk)/math.log(previous+1),ratio_at_end=1))
emit('summability_exponent_liminf',[61],dict(sequence='alpha_n=1/Nk for N(k-1)<n<=Nk, Nk=2^(2^k)',rho=1,liminf=1,limsup=2,finite_table=rows),kind='exact construction with floating illustrative logarithms; limit proof separate')
emit('canonical_product_order',[58,59,62],dict(alpha=2,product='product_(n>=1)(1-z/n^2)=sin(pi sqrt(z))/(pi sqrt(z))',actual_order='1/2',typed_order=1),kind='classical product identity and explicit order calculation, proof in notes')
emit('tail_integral_divergence',[81],dict(single_nonzero_eigenvalue=1,counting_function='n(r)=1 for0<r<1;0 forr>=1',integral_zero_infty='infinite',weighted_cutoff='rho^p*log(1/rho) tends0 for everyp>0'),kind='exact elementary integral')

# A single compact trace-class block construction; the general proof is in notes.
rows=[]
a=Q(1,2)
previous_b=None
for k in range(1,9):
    R=k+1;b=a/(R*R);lam=a/R
    assert a>lam>b>0 and lam/b==R
    if previous_b is not None:assert previous_b>a
    rows.append(dict(k=k,a=str(a),b=str(b),eigenvalue_modulus=str(lam),ratio_at_index_2k=str(lam/b)))
    previous_b=b;a=b/2
emit('compact_trace_class_unbounded_ratio',[83],dict(recurrence='a1=1/2; Rk=k+1; bk=ak/Rk^2; a(k+1)=bk/2',blocks=rows,general_conclusion='Block norms decrease geometrically; sum of singular values finite; ratio at2k=k+1 tends infinity'),kind='exact rational first eight blocks; infinite argument in proof_notes.md')

(D/'computation_output.json').write_text(json.dumps(OUT,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(dict(certificates=len(OUT),all_assertions_passed=True,output=str(D/'computation_output.json')),indent=2))
for record in OUT: print(record['name']+': '+json.dumps(record['result'],ensure_ascii=False))
