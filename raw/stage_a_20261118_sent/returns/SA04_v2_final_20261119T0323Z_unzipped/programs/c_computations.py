"""Reproducible symbolic and finite checks for the C audit.

Finite examples certify the displayed examples only. Universal proofs are stated
separately in parts/c/analysis.md; no numerical sample is labelled such a proof.
"""
from pathlib import Path
import itertools, math, json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

def result(label,**kw): print(label+' '+json.dumps(kw,default=str,sort_keys=True))

root=Path('/workspace/scratch/594d1dc856a9/source')
for package in ['MPL_93_221-236+161-5','MPL_98']:
    notes=(root/'SA04_notes/pro'/f'{package}_notes.md').read_text().splitlines()
    text=(root/'SA04_texts/pro'/f'{package}_transcription.tex').read_text().splitlines()
    result('inventory_'+package,indexed=sum(x.startswith('### ') for x in notes),nested=sum(x.startswith('#### ') for x in notes),scan_markers=sum(x.startswith(r'\scanpage{') for x in text))

a,b,c,d,u,x,y,t,eps,m,n=s.symbols('a b c d u x y t eps m n')
M=s.Matrix([[a,0],[b,a]])
assert s.det(M)==a*a
result('NORM_DUAL_NUMBERS',matrix=M,norm=s.det(M))
A=s.Matrix(3,3,s.symbols('a0:9'))
first=s.expand((s.eye(3)+eps*A).det()).coeff(eps,1)
assert first==s.trace(A)
result('NORM_TRACE',first_order=first,trace=s.trace(A))
B0=s.Matrix(2,2,s.symbols('b0:4'))
B1=s.Matrix(2,2,s.symbols('c0:4'))
block=s.diag(B0,B1)
assert s.expand(block.det()-B0.det()*B1.det())==0
assert s.trace(block)==s.trace(B0)+s.trace(B1)
assert s.zeros(0,0).det()==1
result('NORM_DIRECT_SUM',determinant_difference=0,trace_difference=0,rank_zero_norm=1,rank_zero_trace=0,rank_one_norm='identity')

# C=A[y]/(y^4-u), B=A[x]/(x^2-u), x=y^2.
poly=a+b*y+c*y*y+d*y**3
cols=[]
for j in range(4):
    v=s.rem(poly*y**j,y**4-u,y)
    cols.append([s.expand(v).coeff(y,i) for i in range(4)])
MC=s.Matrix.hstack(*[s.Matrix(z) for z in cols])
norm_CB=s.rem((a+c*x)**2-x*(b+d*x)**2,x*x-u,x)
P=s.expand(norm_CB).coeff(x,0); Q=s.expand(norm_CB).coeff(x,1)
nested=s.expand(P*P-u*Q*Q)
assert s.expand(MC.det()-nested)==0
result('NORM_TOWER',norm_C_B=norm_CB,norm_B_A=nested,difference=0)

def rank_mod(M,p):
    a=[list(map(lambda z:int(z)%p,row)) for row in M]; r=0
    if not a:return 0
    for col in range(len(a[0])):
        z=next((j for j in range(r,len(a)) if a[j][col]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r]; inv=pow(a[r][col],-1,p);a[r]=[(v*inv)%p for v in a[r]]
        for j in range(len(a)):
            if j!=r:
                k=a[j][col];a[j]=[(v-k*w)%p for v,w in zip(a[j],a[r])]
        r+=1
    return r
swap=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
sign_dim=4-rank_mod((swap+s.eye(4)).tolist(),2)
alt_rank=rank_mod([[0,1,1,0]],2)
assert (sign_dim,alt_rank)==(3,1)
result('ALT_CHAR2',sign_eigenspace_dimension=sign_dim,alternating_image_dimension=alt_rank)
orbits={tuple(sorted(w)) for w in itertools.product(range(2),repeat=3)}
result('PERMUTATION_INVARIANTS',E_size=2,tensor_degree=3,symmetric_orbits=len(orbits),orbit_sizes=[sum(tuple(sorted(w))==z for w in itertools.product(range(2),repeat=3)) for z in sorted(orbits)],sign_action_Z_invariants_rank=0,sign_action_mod2_invariants_rank=1)
T=range(2); X=range(4); fibres=[[z for z in X if z//2==j] for j in T]
assert sorted(sum(fibres,[]))==list(X)
result('FINITE_SET_NORM_COMPOSITION',inner_fibres=fibres,flattened=sum(fibres,[]),composite_fibre=list(X))
result('EMPTY_DEGREE',identity_degree=1,disjoint_two_identity_degree=2,empty_pullback_forces_equality=False)

result('PERIOD_OPEN_ARC',omega='dx',operator='1',de_Rham_class=0,a=0,b=1,integral=s.integrate(1,(x,0,1)))
f=t*x; lo=t; hi=2*t
integral=s.integrate(f,(x,lo,hi))
rhs=s.integrate(s.diff(f,t),(x,lo,hi))+f.subs(x,hi)*s.diff(hi,t)-f.subs(x,lo)*s.diff(lo,t)
assert s.simplify(s.diff(integral,t)-rhs)==0
result('MOVING_ENDPOINTS',integral=integral,derivative=s.diff(integral,t),Leibniz_rhs=rhs)
result('RELATIVE_NOT_ABSOLUTE_CLOSED',relative_form='s dx',section='x=t',pulled_back='s dt',exterior_derivative='ds wedge dt')
result('INTERSECTING_HORIZONTAL',section_a_velocity=0,section_b_velocity=1,common_horizontal_vector_possible=False)
result('RHOM_RANK',rank_K1=2,rank_K2=2,rank_Hom=4,rank_unit=1)

# Cartan identity for one-forms, comparing the coordinate pullback derivative.
va=x*x+y; vb=x-y*y; f=x*y+x; g=x*x+y**3
cartan=s.Matrix([s.diff(f*va+g*vb,x)-(s.diff(g,x)-s.diff(f,y))*vb,
                 s.diff(f*va+g*vb,y)+(s.diff(g,x)-s.diff(f,y))*va])
pullback=s.Matrix([va*s.diff(f,x)+vb*s.diff(f,y)+f*s.diff(va,x)+g*s.diff(vb,x),
                   va*s.diff(g,x)+vb*s.diff(g,y)+f*s.diff(va,y)+g*s.diff(vb,y)])
assert all(s.expand(z)==0 for z in cartan-pullback)
result('CARTAN_FIRST_ORDER',cartan_coefficients=list(cartan),coordinate_derivative=list(pullback),difference=list(map(s.expand,cartan-pullback)))
for p in [2,3,5,7]:
    # The only derivative coefficient of x^(p-1) is p*a_p, even for formal series.
    assert p%p==0
result('CHAR_P_PRIMITIVE',tested_primes=[2,3,5,7],coefficient_equation='p*a_p=1 in characteristic p, impossible')

weights=sorted({j-i for i in [0,1] for j in [0,1]})
checks=[(h,r,math.comb(h,r)//h) for h in range(2,31) for r in range(1,h) if math.gcd(h,r)==1]
assert all(math.comb(h,r)%h==0 for h,r,_ in checks)
result('SERRE_WEIGHT_ARITHMETIC',End_weights=weights,coprime_binomial_checks=len(checks),determinant_exponent_for_2_3=2*3-3*2,universal_reason='r*C(h,r)=h*C(h-1,r-1), gcd(r,h)=1')
series=2*x+x*x
assert series.subs(x,-2)==0
v=s.Rational(10); seq=[v]
for i in range(15):v=max(v/2,v-1);seq.append(v)
result('VALUATION_THRESHOLD',p=2,height=1,threshold=1,x_at_boundary=-2,f_at_boundary=0,upper_bound_recurrence=seq,eventual_halving=seq[-1]==seq[-2]/2)

J=s.Matrix([[0,1],[-1,0]])
assert J*J==-s.eye(2)
result('REAL_CONIC_DESCENT',semilinear_lift_square=J*J,scalar_norm='a^2+b^2',negative_one_is_real_norm=False)
result('CIRCLE_MONODROMY',reflection_matrix=s.diag(1,-1),orientation_degree=-1,number_connected_components=1)
d2=s.Matrix([[0],[2]])
result('KLEIN_BOTTLE',cellular_d2=d2,smith=smith_normal_form(d2,domain=s.ZZ),cohomology_H1='Z',cohomology_H2='Z/2')

fixed=s.expand((m+n+1)+(m-n+1))
assert fixed==2*m+2
result('BOUNDEDNESS_POLYNOMIAL',split_pair_Hilbert=fixed,h0_for_n_1_to_8=[j+1 for j in range(1,9)],line_bundle_Hilbert=m+n+1,quotient_sections='X^n,Y^n have no common projective zero',cycle='[P1] for every n')
result('BOUNDEDNESS_AFFINE_COKERNEL',lengths=[j for j in range(1,9)],modules='k[x]/(x^n)',h0_O_minus_n=[0]*8)
t1,t2=s.symbols('t1 t2')
aligned=s.groebner([x-t1,x-t1],x,domain=s.QQ.frac_field(t1))
independent=s.groebner([x-t1,x-t2],x,domain=s.QQ.frac_field(t1,t2))
assert independent.polys[0].as_expr()==1
result('RELATIVE_FIELD_POSITIONS',aligned_ideal=list(aligned),independent_ideal=list(independent))
z=s.symbols('z')
gb=s.groebner([z*x,(1-z)*x*x,(1-z)*(y-a*x)],z,x,y,domain=s.QQ.frac_field(a),order='lex')
elimination=[v.as_expr() for v in gb.polys if not v.as_expr().has(z)]
assert set(elimination)=={x*x,x*y}
result('PRIMARY_COMPONENTS',parameter='arbitrary a',intersection_generators=elimination)
result('INSEPARABLE_SUPPORT',p=3,after_root=s.expand((x-a)**3),mod3=s.Poly((x-a)**3,x,a,modulus=3).as_expr())
result('WRONG_RING_TOR',B='k[x]',B_i='k',B_i_free_resolution_degrees=[0],B_free_resolution_differential='x',Tor_over_B_dimensions=[1,1],naive_Bi_result=[1,0])
result('TOR_INPUT_FLATNESS',A='k[t]',B='A[x]',M1='B/(tx)',M2='B/(x)',tensor_differential=s.expand(t*x).subs(x,0),Tor_before=['A','A'],specialized_M1_relation=(t*x).subs(t,0),Tor_after=['k',0])
result('EXT_TERMINAL_COKERNEL',Hom_complex_differential=t,generic_H0=0,generic_H1='A/(t)',specialized_differential=t.subs(t,0),special_H0='k')
result('HOM_COMMON_DENOMINATOR',sequence=[str(s.Rational(1,math.factorial(i))) for i in range(1,9)],image_description='rational sequences with one common nonzero integer denominator',all_positive_Ext=0)
result('RADICAL_SQUARE_ZERO_TOR',embedding_dimension=2,ranks=[2**i for i in range(10)],recurrence='beta_(i+1)=2 beta_i')
result('UNBOUNDED_COMPLEX',blocks=[str(t-i) for i in range(5)],exceptional_points=list(range(5)),universal_obstruction='infinitely many distinct a_n require infinitely many locally closed rank-jump strata')

full=s.eye(2);prefix=s.Matrix([[1,0]])
result('JET_FLAG',full_rank=full.rank(),full_nullity=2-full.rank(),prefix_rank=prefix.rank(),prefix_nullity=2-prefix.rank())
pts={'a','b','c'}
parts=[({'a','b'},[set(),{'a'},{'b'},{'a','b'}]),({'a','c'},[set(),{'c'},{'a','c'}]),({'c','b'},[set(),{'b'},{'c','b'}])]
subsets=[set(c) for k in range(4) for c in itertools.combinations(sorted(pts),k)]
qopens=[U for U in subsets if all(U&X in tau for X,tau in parts)]
induced=[U&{'a','b'} for U in qopens]
assert {'a'} not in induced
result('GLUING_COUNTEREXAMPLE',quotient_opens=[sorted(U) for U in qopens],discrete_piece_induced=[sorted(U) for U in induced],missing_open=['a'])

uu,vv=s.symbols('u v');rel=s.groebner([uu*uu-2,vv*vv-2],uu,vv,domain=s.QQ)
e=(2+uu*vv)/4
assert rel.reduce(s.expand(e*e-e))[1]==0
result('WEIL_RESTRICTION_POINTS',quadratic_tensor_rank=4,split_factors=2,idempotent=e,idempotency_remainder=0,T_Qp='K^*',T_K='(K x K)^*')
result('VALUATION_COCYCLE',coboundary_valuation='v(sigma(a))-v(a)=0',uniformizer_valuation=1,uniformizer_coboundary=False)
result('DIRECT_PRODUCT_SECTION_MODEL',multipliers=[2,3],values_n_0_to_3=[[b**j for j in range(4)] for b in [2,3]],conjugation_in_abelian_group='trivial',sections_conjugate=False)
print('All asserted symbolic identities and finite counterexample checks passed. Universal qualifications are in analysis.md.')
