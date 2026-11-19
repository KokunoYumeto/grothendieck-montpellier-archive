"""Exact finite/symbolic checks. Each output states its scope; bounded tests are not universal proofs."""
import itertools as it,json,math
import sympy as s
out={}
def add(a,b): return tuple(x^y for x,y in zip(a,b))
def mv(M,v): return tuple(sum(M[3*i+j]*v[j] for j in range(3))%2 for i in range(3))
E=[(1,0,0),(0,1,0),(0,0,1)]
def pgl_br(a,b): return (0,(a[0]*b[1]+a[1]*b[0])%2,(a[0]*b[2]+a[2]*b[0])%2)
def sl_br(a,b): return ((a[1]*b[2]+a[2]*b[1])%2,0,0)
def derivs(br):
    return [M for M in it.product(range(2),repeat=9) if all(mv(M,br(a,b))==add(br(mv(M,a),b),br(a,mv(M,b))) for a in E for b in E)]
def inners(br):
    return {tuple(br(v,E[j])[i] for i in range(3) for j in range(3)) for v in it.product(range(2),repeat=3)}
def normalizer(br,gens):
    span={(0,0,0)}
    for g in gens:span|={add(v,g) for v in list(span)}
    return [v for v in it.product(range(2),repeat=3) if all(br(v,w) in span for w in gens)]
for name,br in [('pgl2_F2',pgl_br),('sl2_F2',sl_br)]:
    D=derivs(br);I=inners(br)
    out[name]={'derivations':len(D),'inner_derivations':len(I),'dim_H1':int(math.log2(len(D)//len(I))), 'normalizer_H':normalizer(br,[E[0]]),'normalizer_Y':normalizer(br,[E[2]])}
D=(0,0,0,0,1,0,0,0,0)
out['pgl2_counterexample']={'D_matrix_rows':[[0,0,0],[0,1,0],[0,0,0]],'is_derivation':D in derivs(pgl_br),'is_inner':D in inners(pgl_br)}
perms=list(it.permutations(range(4)));unit=tuple(range(4))
def mul(a,b):return tuple(a[b[i]] for i in range(4))
def inv(a):return tuple(a.index(i) for i in range(4))
V4=[unit,(1,0,3,2),(2,3,0,1),(3,2,1,0)]
conj=lambda a,g:mul(mul(g,a),inv(g))
out['V4_into_S4_H1_R']={'V4_cocycles':[a for a in V4 if mul(a,a)==unit], 'S4_orbit_of_double_transposition':sorted({conj(V4[1],g) for g in perms}), 'neutral_fibre':[a for a in V4 if unit in {conj(a,g) for g in perms}],'V4_conjugation_trivial':all(conj(a,g)==a for a in V4 for g in V4)}
V2=list(it.product(range(2),repeat=2));V4v=list(it.product(range(2),repeat=4));mons=[(i,i) for i in range(4)]+list(it.combinations(range(4),2))
def qval(coeff,v):return sum(c*v[i]*v[j] for c,(i,j) in zip(coeff,mons))%2
def tensor(a,b):return (a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
qh=lambda a:a[0]*a[1]
cands=[c for c in it.product(range(2),repeat=10) if all(qval(c,tensor(a,b))==qh(a)*qh(b) for a in V2 for b in V2)]
swap=lambda v:(v[2],v[3],v[0],v[1])
out['quadratic_tensor_obstruction']={'tested_forms':2**10,'monomial_order':mons,'candidate_coefficients':cands,'number_candidates':len(cands),'swap_first_factor_exchanges_candidates':all(qval(cands[0],swap(v))==qval(cands[1],v) for v in V4v),'invariant_candidates':sum(all(qval(c,swap(v))==qval(c,v) for v in V4v) for c in cands)}
q0=lambda v:v[0]*v[1]%2
q1=lambda v:(v[0]+v[0]*v[1]+v[1])%2
polar=lambda q,a,b:(q(add(a,b))+q(a)+q(b))%2
out['same_polar_different_quadratic']={'q0_values':[q0(v) for v in V2],'q1_values':[q1(v) for v in V2],'equal_polars':all(polar(q0,a,b)==polar(q1,a,b) for a in V2 for b in V2),'nonzero_isotropic_q0':[v for v in V2[1:] if q0(v)==0],'nonzero_isotropic_q1':[v for v in V2[1:] if q1(v)==0]}
def dn_mul(a,b):return (a[0]*b[0]%2,(a[0]*b[1]+a[1]*b[0])%2)
out['dual_numbers']={'lambda':(1,1),'lambda_squared':dn_mul((1,1),(1,1)),'u':(0,1),'u_squared':dn_mul((0,1),(0,1))}
t1,t2=s.symbols('t1 t2')
det=s.det(s.Matrix([[1-t1*t1,2*t1],[1-t2*t2,2*t2]]))
out['ordered_ray_determinant']={'expanded':str(s.expand(det)),'factorised':str(s.factor(det)),'identity_remainder':str(s.expand(det-2*(t2-t1)*(1+t1*t2)))}
a,b,c=s.symbols('a b c')
out['exterior_gram_determinant']={'matrix':[['a','b'],['b','c']],'determinant':str(s.det(s.Matrix([[a,b],[b,c]])))}
x=s.symbols('x')
def binpoly(x,n):return s.prod(x-i for i in range(n))/math.factorial(n)
fail=[]
for p in range(7):
    for q in range(7):
        rhs=sum(s.Rational(math.factorial(n),math.factorial(n-p)*math.factorial(n-q)*math.factorial(p+q-n))*binpoly(x,n) for n in range(max(p,q),p+q+1))
        if s.expand(binpoly(x,p)*binpoly(x,q)-rhs)!=0:fail.append((p,q))
out['Dist_Gm_product']={'tested_p_q':'0 through6 inclusive (49 polynomial identities over Q)','failures':fail,'X1_square_minus_X1_minus_2X2':str(s.expand(x*x-x-2*binpoly(x,2))),'universal_reason':'Count pairs of subsets of a fixed n-element union: overlap p+q−n, first-only n−q, second-only n−p; polynomial identity then holds for every p,q and every integer-valued argument.'}
Phi=lambda z,w:z*s.conjugate(w)
im=lambda z,w:s.im(Phi(z,w))
val=Phi(s.Integer(1),s.Integer(1));minus=-im(1,s.I)+s.I*im(1,1);plus=im(1,s.I)+s.I*im(1,1)
out['hermitian_sign']={'Phi_1_1':str(val),'Im_Phi_1_i':str(im(1,s.I)),'formula8_minus_reconstruction':str(minus),'formula12_plus_reconstruction':str(plus),'minus_matches':s.simplify(val-minus)==0,'plus_matches':s.simplify(val-plus)==0}
lam=s.diag(1,2);alpha=s.Matrix([[0,1],[0,0]]);dagger=lam.inv()*alpha.T*lam
out['Rosati_not_integral']={'polarisation_matrix':str(lam),'endomorphism_alpha':str(alpha),'dagger':str(dagger),'integral':all(a.q==1 for a in dagger)}
n,c=s.symbols('n c');f=s.expand((n+c)**4)
out['characteristic_coefficients']={'example':'A=E², alpha=[c], degree(n+alpha)=(n+c)^4','polynomial':str(f),'sigma_degrees':{str(i):s.Poly(f,n).coeff_monomial(n**(4-i)).as_poly(c).degree() for i in range(1,5)},'universal_reason':'Homogeneity degree2g of ν gives σ_i(cα)=c^i σ_i(α), comparing ν(n+cα)=c^(2g)ν(n/c+α).'}
out['hyperelliptic_multiplication']=[{'genus':g,'domain_dim_symmetric':g*(g+1)//2,'image_basis_exponents':list(range(2*g-1)),'image_dimension':2*g-1,'target_dimension':3*g-3,'cokernel_dimension':g-2,'Hilbert_tangent_dimension':2*g-2} for g in range(2,9)]
out['hyperelliptic_reason']='For char≠2 and y²=f(x), products of x^i dx/y (0≤i≤g−1) span x^j(dx/y)² for0≤j≤2g−2. These are independent. Riemann–Roch gives h0(ω²)=3g−3. This is a proof for every g≥2, beyond the displayed dimensions.'
out['alpha_p_moving_lines']={'base':'F_p[t] or its localisation/completion','ambient':'alpha_p²=Spec R[x,y]/(x^p,y^p)','subgroup':'y−t x=0','flat_rank':'p, with basis1,x,...,x^(p−1)','Hopf_check':'Δ(y−t x)=(y−t x)⊗1+1⊗(y−t x); ε=0 and antipode preserves the ideal','tangent_test':'over dual numbers t=ε the ideal(y−εx) differs from(y), yielding a nonconstant first-order family of finite flat subgroups','scope':'Unramifiedness of the moduli of all closed subgroup schemes fails; smooth connected abelian subgroups are a different functor.'}
out['nonample_isogeny']={'example':'E over C, L=O_E(−0)','degree_L':-1,'not_ample_reason':'On a proper smooth curve ample iff positive degree.','phi_L':'minus the principal isomorphism (sign changes if the manuscript uses t_−x); it remains an isomorphism','all_hypotheses':'E is a projective abelian scheme over Spec C; finite faithfully flat is satisfied; L is not ample.'}
out['perfect_not_centerless']={'group':'SL₂(F₅)','known_matrix_generators_check_scope':'Counterexample can be certified by full finite enumeration below'}
F5=[(a,b,c,d) for a,b,c,d in it.product(range(5),repeat=4) if (a*d-b*c)%5==1]
def mm(A,B):a,b,c,d=A;e,f,g,h=B;return ((a*e+b*g)%5,(a*f+b*h)%5,(c*e+d*g)%5,(c*f+d*h)%5)
def mi(A):a,b,c,d=A;return (d%5,-b%5,-c%5,a%5)
unit5=(1,0,0,1)
comm={mm(mm(mm(a,b),mi(a)),mi(b)) for a in F5 for b in F5}
generated={unit5};front=[unit5]
while front:
    a=front.pop()
    for b in comm:
        c=mm(a,b)
        if c not in generated:generated.add(c);front.append(c)
center=[a for a in F5 if all(mm(a,b)==mm(b,a) for b in F5)]
out['perfect_not_centerless'].update(order=len(F5),derived_order=len(generated),center=center)
out['rank_one_torus_isomorphisms']={'character_group':'Z','endomorphisms':'multiplication by every integer','automorphisms':[-1,1],'counterexample':'multiplication by0 is not invertible'}
out['contraction_nonuniqueness']={'ring':'Z','module':'Z/2','dual':'Hom_Z(Z/2,Z)=0','endomorphisms_distinct':['zero','identity'],'all_dual_pairings_identical':True}
print(json.dumps(out,indent=2,ensure_ascii=False))
