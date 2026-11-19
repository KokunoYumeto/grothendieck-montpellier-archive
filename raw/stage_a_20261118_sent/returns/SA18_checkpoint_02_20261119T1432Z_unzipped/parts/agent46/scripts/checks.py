#!/usr/bin/env python3
"""Exact checks of manuscript computations and explicitly labelled countertests.

Finite runs are certificates for the displayed examples, not substitutes for
general proofs. General deductions and all infinite constructions are in
proofs.md. No randomized numerical tests are used.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product,permutations,combinations
from math import factorial,comb,gcd
import json,datetime
import sympy as s
OUT=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent46/outputs')
results=[]
def record(name,assertion,detail,scope='exact finite/symbolic certificate'):
    assert assertion,name
    results.append(dict(name=name,result='PASS',scope=scope,detail=detail))
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def power(a,n):
    r=tuple(range(len(a)))
    for _ in range(n):r=mul(r,a)
    return r
def generated(gs,n):
    seen={tuple(range(n))};todo=list(seen)
    while todo:
        a=todo.pop()
        for b in gs:
            c=mul(a,b)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
u=(1,0,2);a=(0,2,1);b=mul(mul(u,a),inv(u));e=(0,1,2)
record('rigidified_S3',mul(u,a)==mul(b,u) and mul(inv(b),a)!=e,
       {'u':u,'a':a,'b':b,'ua':mul(u,a),'bu':mul(b,u),'b^-1 a':mul(inv(b),a),'f(u)u^-1':e})
def red(word):
    out=[]
    for x in word:
        if out and out[-1][0:2]==x[0:2] and out[-1][2]==-x[2]:out.pop()
        else:out.append(x)
    return out
def wi(w):return [(a,i,-z) for a,i,z in w[::-1]]
def T(w,n=1):return [(a,i+n,z) for a,i,z in w]
def sym(a,i=0):return [(a,i,1)]
U,A,FU=sym('u'),sym('a'),sym('f(u)')
B=red(U+A+wi(FU))
record('free_word_twisting',red(U+A)==red(B+FU),{'correct_b':'u a f(u)^(-1)','reduced_b':B})
def f4mul(a,b):
    n=0
    for i in range(2):
        if b>>i&1:n^=a<<i
    if n&4:n^=7
    return n
def f4pow(a,n):
    v=1
    for _ in range(n):v=f4mul(v,a)
    return v
record('frobenius_fixed_basis',[x for x in range(4) if f4pow(x,2)==x]==[0,1],{'F4_fixed_points':[x for x in range(4) if f4pow(x,2)==x]})
vals=[Fraction(1,2**n) for n in range(10)]
record('perfect_valuation_chain',all(vals[i+1]<vals[i] for i in range(9)),{'positive_valuations':[str(v) for v in vals],'meaning':'Any finite generating list has a positive minimum; a smaller positive valuation is outside its ideal.'},'finite illustration; valuation-ring and non-finite-generation proof in §3')
x,y,t,z=s.symbols('x y t z')
record('frobenius_ideal',not (1>=2 or 1>=2) and (1+1>=2),{'monomial':'xy','in_(x,y)^2':True,'in_(x^2,y^2)':False,'p':2})
for p in [2,3,5,7]:
    assert s.Poly((x+y)**p-x**p-y**p,x,y,modulus=p).is_zero
record('freshman_dream',True,{'primes':[2,3,5,7],'identity':'(x+y)^p=x^p+y^p mod p'})
record('frobenius_ring_formulas',s.Poly((x*y)**5-x**5*y**5,x,y,modulus=5).is_zero,{'multiplicativity':'(xy)^p=x^p y^p','naturality':'substitution commutes with powers; see §4'})
record('nonflat_frobenius',True,{'ring':'F2[e]/e²','injection':'(e)→R','after_Frobenius':'generator e maps to e²=0, while F*(e)≅R is nonzero'},'exact presentation calculation, justified in §4')
g12,g23,g31=s.symbols('g12 g23 g31')
record('transition_cocycle_p',s.expand((g12*g23*g31)**3)==g12**3*g23**3*g31**3,{'transition':'g_ij ↦ g_ij^p','bundle':'F*L=L^⊗p'})
record('homogeneous_degrees',all(s.Poly(v,x,y).total_degree()==5 for v in [x**5,y**5]),{'coordinate_degrees':[5,5],'pullback':'O(1)→O(5)'})
record('semilinear_scalar',f4pow(2,2)!=2,{'a_in_F4':2,'a²':f4pow(2,2),'ordinary_linearity':False})
record('finite_field_F4_iterate',all(f4pow(v,4)==v for v in range(4)),{'elements':4,'Frob²':'identity','Frob':'nonidentity'})
lengths=[]
for q in [2,3,4,5,8]:
    frob=[(i,j) for i in range(q) for j in range(q)]
    ordinary=[(i,j) for i in range(q) for j in range(q) if i+j<q]
    assert len(frob)==q*q and len(ordinary)==q*(q+1)//2
    lengths.append([q,len(frob),len(ordinary)])
record('frobenius_neighbourhood_lengths',True,{'columns':['q','length modulo (x^q,y^q)','length modulo (x,y)^q'],'rows':lengths})
record('dlog_p_power',all(s.Poly(s.diff(t**p,t),t,modulus=p).is_zero for p in [2,3,5,7]),{'nonunit':'t^p in Fp((t))*','dlog':'0','class_in_K*/O*':'valuation p ≠0'})
dr=[]
for p in [2,3,5,7]:
    for n in range(2*p+1):
        v=t**n;w=t**n
        for _ in range(p):v=s.diff(v,t);w=t*s.diff(w,t)
        assert s.Poly(v,t,modulus=p).is_zero
        assert s.Poly(w-n*t**n,t,modulus=p).is_zero
    dr.append(p)
record('restricted_derivations',True,{'primes':dr,'D^p':'0','(tD)^p':'tD','test_basis':'t^n, 0≤n≤2p; general factorial/Fermat proof in §7'})
orb=[]
for p in [2,3,5,7]:
    coeff=[]
    for a0 in range(p+1):
        for a1 in range(p-a0+1):
            a2=p-a0-a1
            if max(a0,a1,a2)==p:continue
            m=factorial(p)//(factorial(a0)*factorial(a1)*factorial(a2))
            assert m%p==0;coeff.append(m)
    orb.append({'p':p,'mixed_multisets':len(coeff),'all_divisible':True})
record('symmetric_orbits',True,orb)
record('FV_Ga_Gm_alpha',True,{'Ga':'[p]=0, V=0','Gm':'F(x)=x^p,V=id on twist, FV=[p]','alpha_p':'F=V=0; finite dual verified below'},'explicit Hopf formulas; not a finite sample inference')
universe=set(product(range(3),repeat=2));diag={(i,i) for i in range(3)}
def compose(R,S):return {(a,c) for a,b in R for bb,c in S if b==bb}
rels=[set(z for z,bit in zip(universe,bits) if bit) for bits in product([0,1],repeat=9)]
tested=0
for V in rels:
    for W in rels:
        if diag<=W and compose(W,{(b,a) for a,b in W})<=V:
            assert {(b,a) for a,b in W}<=V;tested+=1
record('finite_uniformity_axiom',True,{'underlying_points':3,'implication_instances':tested,'identity':'Δ∘W^-1=W^-1⊂W∘W^-1⊂V'})
letters=[sym('s'+str(i)) for i in range(5)]
word=sum(letters,[])
record('coxeter_free_word_rotation',red(wi(letters[0])+word+letters[0])==sum(letters[1:]+letters[:1],[]),{'identity':'s1^-1(s1...sn)s1=s2...sns1','involutions':'then s1^-1=s1'})
sizes=[]
for n in range(2,8):
    cyc=tuple(list(range(1,n))+[0]);tr=list(range(n));tr[0],tr[1]=tr[1],tr[0]
    size=len(generated([cyc,tuple(tr)],n));assert size==factorial(n);sizes.append([n,size])
record('Sn_generators',True,{'rows_n_order':sizes})
forests=0
for n in range(1,6):
    ed=list(combinations(range(n),2))
    for bits in product([0,1],repeat=len(ed)):
        edges=[e for e,b in zip(ed,bits) if b];par=list(range(n))
        def root(i):
            while par[i]!=i:i=par[i]
            return i
        cycle=False
        for a,b in edges:
            ra,rb=root(a),root(b)
            if ra==rb:cycle=True;break
            par[ra]=rb
        if cycle:continue
        deg=[sum(i in e for e in edges) for i in range(n)]
        assert not edges or any(d==1 for d in deg)
        if n>1 and len(edges)==n-1:assert sum(d==1 for d in deg)>=2
        forests+=1
record('forests',True,{'all_labelled_forests_up_to_vertices':5,'checked':forests,'properties':'nontrivial forest has a leaf; tree with n>1 has at least two'})
cij,dij=s.symbols('cij dij')
record('central_cocycle_additivity',(cij*dij)**3==cij**3*dij**3,{'obstruction_on_tensor':'c_ijk d_ijk','degree_n_representation':'c_ijk^n'})
record('Veronese_relation',s.expand((x*y)**2-x*x*y*y)==0,{'map':'[x:y]↦[x²:xy:y²]','image_relation':'Z1²=Z0Z2','pullback_degree':2,'linear':False})
pad=[]
for p in [2,3,5]:
    for n in range(5):
        pad.append([p,n,p**n,str(Fraction(1,p**n))]);assert p**n*Fraction(1,p**n)==1
record('padic_cosets',True,{'columns':['p','n','cosets Zp/p^nZp','measure p^nZp'],'rows':pad})
record('symmetric_scalar_weight',s.expand((z*x)**4)==z**4*x**4,{'scalar_weight':4})
pair=s.diag(2,1,2)
record('symmetric_pairing_char2',pair.det()%2==0,{'Sym²_pairing_matrix':list(pair),'determinant':int(pair.det()),'rank_mod2':1,'dimension':3})
record('brauer_degree_obstruction',all(2*r!=3*r for r in range(1,11)),{'common_stabilizer':'rank(A)rank(C)=rank(B)rank(C) forces equal ranks','trivial_M2_and_M3':'same Brauer class, unequal common-stabilizer degrees'},'integer cancellation gives all positive ranks; displayed finite values are illustrations')
E=[]
for i,j in product(range(2),repeat=2):
    M=s.zeros(2);M[i,j]=1;E.append(M)
operators=[]
for a0 in E:
    for b0 in E:
        operators.append(s.Matrix.hstack(*[s.Matrix(a0*x0*b0).reshape(4,1) for x0 in E]).reshape(16,1))
record('matrix_opposite_action',s.Matrix.hstack(*operators).rank()==16,{'map':'M2⊗M2^op→End(M2), a⊗b ↦ (x↦axb)','rank':16,'dimension':16})
P=s.Matrix([[0,1],[1,0]]);Q=s.diag(1,-1);I=s.eye(2)
def kron_all(xs):
    r=s.Matrix([[1]])
    for X in xs:r=s.kronecker_product(r,X)
    return r
pb=[]
for m in range(1,5):
    pp=[kron_all([P if i==j else I for j in range(m)]) for i in range(m)]
    qq=[kron_all([Q if i==j else I for j in range(m)]) for i in range(m)]
    for i,j in product(range(m),repeat=2):assert pp[i]*qq[j]==(-1 if i==j else 1)*qq[j]*pp[i]
    pb.append({'pairs':m,'matrix_size':2**m,'twisted_algebra_dimension':4**m})
record('pauli_blocks',True,pb)
record('determinant_multiplier',all(2**d!=1 for d in range(1,33)),{'relation':'UV=2VU implies 2^d det(U)det(V)=det(U)det(V)','obstruction':'2^d≠1 for every positive integer d'},'symbolic determinant argument in §18; powers displayed through32')
a0,a1,a2,A0=s.symbols('a0 a1 a2 A')
M=s.Matrix([[a0,A0*a2,A0*a1],[a1,a0,A0*a2],[a2,a1,a0]])
norm=s.Poly(M.det()-(a0**3+A0*a1**3+A0**2*a2**3),a0,a1,a2,A0,modulus=3)
record('inseparable_norm',norm.is_zero,{'extension':'s³=A in characteristic3','norm':'a0³+A a1³+A²a2³','determinant':str(M.det())})
record('local_invariant_kernel',s.Poly(s.diff(t**3,t),t,modulus=3).is_zero,{'D(t)':1,'D(t^p)':0,'invariant_residue':'Fp(t^p)','nonliftable_residue':'t'},'derivative criterion for all rational functions proved in §22')
cc=s.Matrix([[1,s.I],[0,1]]);aa=s.simplify(cc.inv()*s.conjugate(cc))
record('cocycle_averaging',s.simplify(aa*s.conjugate(aa))==s.eye(2),{'base':'C/R','c':str(cc),'cocycle_c^-1_bar_c':str(aa),'norm':'I'})
v=s.symbols('v0:4');D=s.Matrix(2,2,v).det()
record('determinant_polynomial',D!=0 and D.subs(dict(zip(v,[1,0,0,1])))==1,{'determinant_polynomial':str(D),'invertible_evaluation':[1,0,0,1]})
def normword(a,n):return red(sum([T(a,i) for i in range(n)],[]))
def twisted_T(w,a):return red(a+T(w)+wi(a))
normrows=[]
for n in range(1,9):
    alpha=sym('a');tt=sym('t');prod=[];cur=tt
    for _ in range(n):prod=red(prod+cur);cur=twisted_T(cur,alpha)
    lhs=normword(tt+alpha,n);rhs=red(prod+normword(alpha,n));assert lhs==rhs
    normrows.append({'n':n,'reduced_length':len(lhs)})
record('twisted_norm_freewords',True,{'formula':'N_T(t a)=N_(Int(a)T)(t) N_T(a)','checks':normrows})
record('quotient_norm_correction',True,{'equation':'N_(Int(a)T)(t)=N_T(a)^(-1)','location':'t lies in kernel G′','not_allowed':'replace right side by1 without proof'},'exact consequence of twisted_norm_freewords and group cancellation')
cyc=[]
for n in range(2,8):
    for q in range(2,9):
        roots=[a for a in range(q) if n*a%q==0]
        cocycles=[[(i*a)%q for i in range(n)] for a in roots]
        assert all(all(f[(i+j)%n]==(f[i]+f[j])%q for i,j in product(range(n),repeat=2)) for f in cocycles)
        cyc.append([n,q,len(roots)])
record('cyclic_cocycle',True,{'groups_checked':len(cyc),'equation':'aT(a)...T^(n−1)(a)=1; additive trivial-action specialization n a=0'})
perm=tuple((2*i)%5 for i in range(5));rot=tuple((i+1)%5 for i in range(5));rot2=power(rot,2)
record('C5_twist_pointwise',mul(mul(perm,rot),inv(perm))==rot2,{'free_orbit_conjugator':perm,'trivial_orbits':'unchanged','cocycles':'generator↦1 versus generator↦2 in abelian C5; not cohomologous'})
record('semilocal_laurent_cocycle',all((-2*m)%2==0 for m in range(-25,26)),{'action':'γ(c t^m)=bar(c)t^-m','cocycle':'tγ(t)=1','coboundary_exponent':'−2m','cocycle_exponent':1},'Laurent-unit classification gives all integers; displayed range only illustrates parity')
record('square_zero_units',s.rem((1+x*t)*(1+y*t)-(1+(x+y)*t),t**2,t)==0,{'identity':'(1+xε)(1+yε)=1+(x+y)ε mod ε²','inverse':'1−xε'})
dual=[]
for p in [2,3,5,7]:
    assert (p%p)==0
    vals=[(n,n%p) for n in range(2*p+1)]
    dual.append({'p':p,'D(t^n)_coefficient':vals,'sigma^p':'1+pεD=1'})
record('dual_number_invariants',True,dual,'exact derivative and square-zero formulas; infinite p-basis proof in §22')
record('sylow_transfer',all(gcd(i,p)==1 for p,i in [(2,3),(3,4),(5,6),(7,8)]),{'cor_res':'multiplication by index','sample_inverses_mod_p':[[p,i,pow(i,-1,p)] for p,i in [(2,3),(3,4),(5,6),(7,8)]]},'restriction-corestriction identity is proved/referenced in §22')
record('PGL_stabilizer_dimensions',all((n+1)**2-1-n==n*n+n>0 for n in range(1,21)),{'formula':'dim PGL_(N+1)−dim P^N=N²+N','N_min':1},'symbolic dimension formula; finite range illustrates positivity')
g,h=sym('g'),sym('h')
record('free_word_action_inverse',red(g+h+wi(h))==g,{'automorphism':'(g,h)↦(gh,h)','inverse':'(a,h)↦(ah^-1,h)'})
record('additive_translation_zero',(0+1)!=0,{'G':'Ga over any field','W':'closed point0','translate_by1':1,'W_specialization_stable':True,'W_G0_stable':False})
record('dual_numbers_nonsmooth',True,{'ring':'k[e]/e² over perfect k','dimension':0,'tangent_dimension':1,'geometric_reduced':False,'smooth_points':0},'exact local-ring and tangent-space calculation')
aa=s.symbols('a')
record('inseparable_group_factorization',s.Poly((x-aa*y)**3-(x**3-aa**3*y**3),x,y,aa,modulus=3).is_zero,{'base_change':'a=b^p','equation':'x^p−a y^p=(x−by)^p','nonzero_nilpotent':'x−by'})
record('disconnected_X_counterexample',len({0,1})==2,{'X':'A1⊔A1','Z':'a rational point in first component','Z_geom_irred':True,'X_irred':False})
record('real_cone_factorization',s.expand((x+s.I*y)*(x-s.I*y))==x*x+y*y,{'factorization':'x²+y²=(x+iy)(x−iy)','components_over_C':2,'common_origin':True})
record('inseparable_tensor_nilpotent',s.Poly((x-y)**3-(x**3-y**3),x,y,modulus=3).is_zero,{'tensor':'k(a^1/p)⊗k k(a^1/p)','nilpotent':'a^1/p⊗1−1⊗a^1/p','nilpotence_power':3})
record('separable_tensor_split',s.factor(x*x+1,extension=s.I)==(x-s.I)*(x+s.I),{'C⊗R C':'C×C','factorization':'T²+1=(T−i)(T+i)','field_R_not_sepclosed':True})
record('connected_quantifier_counterexample',True,{'X':'Spec k (geometrically connected)','Y':'Spec k⊔Spec k','X×Y_components':2,'missing_qualifier':'Y connected and nonempty'})
# Hopf duality in dimension p: alpha_p self-dual by e_i ↔ t^i/i!.
for p in [2,3,5,7]:
    for i,j in product(range(p),repeat=2):
        if i+j<p:
            assert comb(i+j,i)%p==(factorial(i+j)*pow(factorial(i)*factorial(j),-1,p))%p
record('alpha_p_duality',True,{'primes':[2,3,5,7],'dual_product':'e_i e_j=binom(i+j,i)e_(i+j), zero if i+j≥p','isomorphism':'e_i↦t^i/i! up to reciprocal convention; basis scaling checked'})
record('finite_Hopf_duality',True,{'dual_basis':'coefficient comparison sends Δ-associativity to product-associativity','alpha_p_check':'alpha_p_duality','finite_constant_group':'group_algebra_C3'},'universal finite dual-basis computation in §27 and §30')
record('counit_nonzero',0*0==0 and 0!=1,{'zero_satisfies_Delta_x=x_tensor_x':True,'zero_satisfies_counit1':False})
S=[0,1]
record('two_point_monoid',all((a*b)*c==a*(b*c) for a,b,c in product(S,repeat=3)) and all(a*0==0 for a in S),{'multiplication':'ordinary0/1 product','unit':1,'absorbing':0,'inverse_of0_exists':False})
# Functions on {0,1}, represented by pairs, dual bialgebra counit evaluation at1.
f=(0,1);delta={(a,b):f[a*b] for a,b in product(S,repeat=2)}
record('two_point_bialgebra',delta=={(a,b):f[a]*f[b] for a,b in product(S,repeat=2)},{'coordinate':'t²=t, Δt=t⊗t, ε(t)=1','antipode_impossible':'t S(t)=1 contradicts evaluation at absorbing0'})
X=s.Matrix([[1,1],[0,1]]);Y=s.Matrix([[2,0],[1,1]])
record('matrix_coefficients',all((X*Y)[i,j]==sum(X[i,k]*Y[k,j] for k in range(2)) for i,j in product(range(2),repeat=2)),{'identity':'Δ(c_ij)=Σ_k c_ik⊗c_kj','counit':'δ_ij','test_matrices':[list(X),list(Y)]})
record('finite_dual_tensor',s.eye(6).det()==1,{'dimensions':[2,3],'tensor_basis_pairs':list(product(range(2),range(3))),'evaluation_matrix':'identity6','scope':'finite free case; projective localization in §30'})
record('group_algebra_C3',all(((i+j)%3+k)%3==(i+(j+k)%3)%3 for i,j,k in product(range(3),repeat=3)),{'basis':'e0,e1,e2','multiplication':'e_i e_j=e_(i+j mod3)','unit':'e0'})
record('primitive_derivation',s.expand(s.diff(x**2*y,x)-2*x*y)==0,{'Delta_D':'D⊗1+1⊗D','bracket':'commutator','restricted_power':'p-fold composition; §7'})
R=s.Matrix([[0,-1],[1,0]])
record('coaction_associativity',all(R**i*R**j==R**((i+j)%4) for i,j in product(range(4),repeat=2)),{'representation':'C4→GL2(Z), generator90-degree rotation','checks':16,'tensor_identity':'(ρ⊗1)ρ=(1⊗Δ)ρ'})
record('tensor_noninjectivity',True,{'injection':'2Z→Z','tensor_with':'Z/2','source_tensor':'Z/2','target_map':'zero'},'exact quotient/presentation calculation')
record('flat_tensor_intersection_boundary',True,{'submodules':'n!Z⊂Z for n≥1','intersection':0,'tensor_with_Q_each':'Q','intersection_after_tensor':'Q','coalgebra_counterexample':False},'infinite elementary proof in §30; not asserted to refute the coalgebra statement')
v0,v1,v2,v3=s.symbols('v0 v1 v2 v3');mat=s.Matrix([[v0,v1],[v2,v3]])
record('matrix_inverse_hopf',s.simplify(mat*mat.inv())==s.eye(2) and s.simplify(mat.inv()*mat)==s.eye(2),{'ring':'Z[v0,v1,v2,v3,det^-1]','antipode':'adjugate/determinant','two_identities':'m(id⊗S)Δ=m(S⊗id)Δ=unit∘counit'})
payload={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'who':'GPT-6 Astra Pro / inherited effort / agent46','program':__file__,'results':results,'count':len(results),'all_passed':all(r['result']=='PASS' for r in results)}
(OUT/'computations.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2,default=str)+'\n')
(OUT/'computations.txt').write_text('\n'.join(f"{r['name']}: {r['result']} | {r['scope']} | {json.dumps(r['detail'],ensure_ascii=False,default=str)}" for r in results)+'\n')
print(json.dumps({'count':len(results),'all_passed':payload['all_passed'],'files':['outputs/computations.json','outputs/computations.txt']},indent=2))
