"""Exact checks prompted by the six Codex transcripts, SA07 part 3.

Finite evaluations below certify displayed examples or arithmetic identities,
not general theorems. General arguments are in root_computations.md.
"""
import json
from fractions import Fraction
from math import prod, gcd
import sympy as s

out = {}
x, t, M, mu, q = s.symbols('x t M mu q', positive=True)

# K15-01 scan 46: cyclotomic quotient falsely identified with a field.
a, b = x**3+x+1, x**3+x**2+1
phi = s.cyclotomic_poly(7, x)
assert s.Poly(a*b-phi, x, modulus=2).is_zero
assert all(int(f.subs(x,r)) % 2 for f in (a,b) for r in (0,1))
out['cyclotomic_quotient'] = {
    'p':2,'n':3,'Phi7':str(phi),'factors_mod2':[str(a),str(b)],
    'coprime':str(s.gcd(s.Poly(a,x,modulus=2),s.Poly(b,x,modulus=2)).as_expr()),
    'irreducible_reason':'Both cubics have no F2 root.',
    'quotient':'F8 x F8, cardinality 64, not F8.'}

# B15-03 scan 49: the quadratic majorant really solves the reduced equation.
aa=q*mu*(1+q*M*mu)
bb=M*(1/(1-mu*t)-1)
v=(1-s.sqrt(1-4*aa*bb))/(2*aa)
residual=s.simplify(v-aa*v**2-bb)
assert residual == 0
out['implicit_majorant']={'quadratic':'v - q*mu*(1+q*M*mu)*v^2 = M*(1/(1-mu*t)-1)',
    'substituted_residual':str(residual),'branch_at_origin':'v(0)=0'}

# K15-02 scan 79: the literal central-binomial square-root formula fails.
N=8
bad=1-s.Add(*(s.binomial(2*n,n)*x**n for n in range(1,N+1)))
good=1-s.Add(*(s.binomial(2*n,n)*x**n/s.Integer(2*n-1) for n in range(1,N+1)))
bad_res=s.series(bad**2-(1-4*x),x,0,6)
good_res=s.series(good**2-(1-4*x),x,0,N+1)
assert s.expand(bad**2-(1-4*x)).coeff(x,2)==-8
assert all(s.expand(good**2-(1-4*x)).coeff(x,n)==0 for n in range(N+1))
out['square_root_display']={'literal_residual':str(bad_res),
    'candidate_corrected_residual':str(good_res),
    'corrected_coefficient':'binomial(2*n,n)/(2*n-1)',
    'scope':'Formal check through degree 8; generalized binomial theorem proves all degrees.'}

# B15-03 scan 51: the factor r^-2 is required in the displayed estimate.
r=Fraction(1,4); w=Fraction(1,16); bound_M=r*r
full_geometric_sum=1/(1-Fraction(1,2))/(1-w/r)
out['missing_scale_factor']={'f':'z^2','u':0,'r':str(r),'w':str(w),
    'M':str(bound_M),'actual_quadratic_term':str(w*w),
    'literal_single_term_bound':str(bound_M*w*w),
    'full_geometric_sum':str(full_geometric_sum),
    'literal_full_sum_bound':str(bound_M*w*w*full_geometric_sum),
    'repaired_single_term_bound':str(bound_M*w*w/r**2)}
assert w*w > bound_M*w*w
assert w*w > bound_M*w*w*full_geometric_sum

# B15-02 scan 33: a linear interpolation must reach its right endpoint.
z=s.symbols('z')
out['interpolation']={'literal_interval_0_1':'z/(1-z)',
    'literal_right_limit':str(s.limit(z/(1-z),z,1,dir='-')),
    'candidate_repair':'z/(1-0)','repaired_right_value':1}

# B15-01 scan 82: nonflat base change of R-linear Hom.
# R=Z[T]/(T(T-2)); X=Z with T=0; Y=Z with T=2.
out['R_action_base_change']={'integer_equation':'2*c=0 over Z, hence c=0',
    'integer_kernel_rank':len(s.Matrix([[2]]).nullspace()),
    'mod2_equation':'0*c=0 over F2', 'mod2_kernel_dimension':1,
    'R_finite_free_rank_over_Z':2,
    'claim':'Hom_R(X,Y) tensor F2 = 0 but Hom_(R tensor F2)(X tensor F2,Y tensor F2)=F2'}

# B15-01 scan 171: exact finite classical-group orders.
sp6=2**9*prod(2**(2*i)-1 for i in range(1,4))
so5=3**4*prod(3**(2*i)-1 for i in range(1,3))
out['root_group_orders']={'Sp6_F2':sp6,'W_E7':2*sp6,
    'SO5_F3':so5,'Omega5_F3':so5//2,'O5_F3':2*so5,'W_E6':so5}
assert sp6==1451520 and so5//2==25920

# K15-01 scan 40 and K15-02 scan 77: finite residue checks.
square_data={}
for pp,nn in [(3,2),(5,2),(7,2),(2,3),(2,5)]:
    mod=pp**nn
    units={u for u in range(mod) if gcd(u,pp)==1}
    squares={u*u%mod for u in units}
    square_data[f'{pp}^{nn}']={'units':len(units),'squares':len(squares),
        'index':len(units)//len(squares),'minus_one_square':mod-1 in squares}
out['unit_square_quotients_examples']=square_data

# B15-02 scan 47: explicit local invertibility without global injectivity.
out['power_map_example']={'n':13,'domain':'|z-1|<1/2',
    'points':'1 and exp(2*pi*i/13)', 'common_image':1,
    'distance_bound':'2*sin(pi/13) < 2*pi/13 < 44/91 < 1/2',
    'derivative':'13*z^12, nonzero on domain'}
assert Fraction(44,91)<Fraction(1,2)

# K15-02 scan 71: ordinary real majorants omit p-adic division factors.
def vp_integer(n,p):
    v=0
    while n%p==0:
        n//=p;v+=1
    return v
out['padic_majorant_failure']={'equation':"y'=1+y, y(0)=0",
    'coefficient_x2':'1/2','2_adic_absolute_value':2,
    'ordinary_real_majorant_coefficient':str(Fraction(1,2)),
    'required_divisor_factor':'|1/m|_p rather than real 1/m'}

# B15-02 scan 47: a locally analytic non-Archimedean uniqueness counterexample.
out['locally_analytic_ODE']={'field':'Q3','domain':'Z3','rhs':0,'initial':0,
    'nonzero_solution':'v(x)=3^N if x in 1+3Z3; v(x)=0 otherwise (N>=1)',
    'residue_table_mod3':{'0':0,'1':'3^N','2':0},
    'derivative_everywhere':0,
    'reason':'Each of the three residue classes is open and closed; v is constant locally.',
    'all_smaller_neighbourhoods':'Use 3^m+3^(m+1)Z3 inside 3^m Z3, with amplitude in V.'}

# B15-03 scan 53: boundary convergence is not stable under polynomial weights.
out['boundary_convergence']={'a_n':'1/(n+1)^2','radius':1,'beta':1,
    'unweighted_sum':'pi^2/6 (convergent)',
    'weighted_terms':'(n+1)*a_n=1/(n+1)',
    'weighted_sum':'divergent',
    'repair':'At every strictly smaller radius rho<r, polynomial weights are absorbed by (rho/r)^n.'}

# K15-02 scan 69: universal chain-rule cancellation behind Frobenius.
# For each fixed k,j, symbolic independent U_ih, partials, deltas and w_kh.
pdim=2; qdim=2
d=s.symbols('d0:2'); UU=s.symbols('U0:4'); DY=s.symbols('Y0:8'); DX=s.symbols('X0:8'); ww=s.symbols('w0:2')
U=lambda i,h: UU[i*qdim+h]
Y=lambda i,j,h: DY[(i*qdim+j)*qdim+h]
X=lambda i,j,k: DX[(i*qdim+j)*pdim+k]
k=0;j=1
partial_v=[ww[h]+t*U(k,h) for h in range(qdim)]
dv_partial=U(k,j)+t*sum(d[i]*X(i,j,k) for i in range(pdim))+sum(d[i]*Y(i,j,h)*partial_v[h] for i in range(pdim) for h in range(qdim))
dtU=U(k,j)+t*sum(d[i]*X(k,j,i) for i in range(pdim))+t*sum(d[i]*Y(k,j,h)*U(i,h) for i in range(pdim) for h in range(qdim))
linear=sum(d[i]*Y(i,j,h)*ww[h] for i in range(pdim) for h in range(qdim))
curvature=t*sum(d[i]*(X(i,j,k)-X(k,j,i)+sum(Y(i,j,h)*U(k,h)-Y(k,j,h)*U(i,h) for h in range(qdim))) for i in range(pdim))
assert s.expand(dv_partial-dtU-linear-curvature)==0
out['Frobenius_chain_rule']={'symbolic_residual':0,
    'identity':"w'_kj - sum_(i,h) delta_i (partial_yh U_ij) w_kh = t sum_i delta_i F_ki,j",
    'scope':'Generic two-by-two indeterminates verify signs/index contractions; written indexed derivation applies to arbitrary p,q.'}

print(json.dumps(out,indent=2,ensure_ascii=False))
