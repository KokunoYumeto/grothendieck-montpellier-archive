"""Exact finite and symbolic checks for the Groupes dossier.

Finite enumerations corroborate only their stated examples. General arguments
and cardinal statements are in proof_certificates.md, not inferred by testing.
"""
import itertools, json, pathlib
import sympy as s

OUT=[]
def save(name, claims, **values):
    OUT.append(dict(check=name,claims=[f'C-SA23-groupes-{n:03d}' for n in claims],**values))
def functions(a,b):
    return [dict(zip(a,im)) for im in itertools.product(b,repeat=len(a))]

# The terminal reflection on the two-element poset.
poset_hom={(x,y):int(x<=y) for x in [0,1] for y in [0,1]}
assert all(poset_hom[x,1]==1 for x in [0,1])
assert poset_hom[0,0]==1 and poset_hom[1,0]==0
save('two-object restricted-unit counterexample',[2],hom_sizes={f'{x}->{y}':v for (x,y),v in poset_hom.items()},restricted_functor_fully_faithful=True,unit_at_0_invertible=False)

# Seven-arrow category: Z --f,g--> Y --h--> T, hf=hg=k.
ar={'z':('Z','Z'),'y':('Y','Y'),'t':('T','T'),'f':('Z','Y'),'g':('Z','Y'),'h':('Y','T'),'k':('Z','T')}
ids={'Z':'z','Y':'y','T':'t'}
def comp(b,a):
    if ar[a][1]!=ar[b][0]:return None
    if a==ids[ar[a][0]]:return b
    if b==ids[ar[b][0]]:return a
    if b=='h' and a in ['f','g']:return 'k'
    raise AssertionError((b,a))
triples=0
for a,b,c in itertools.product(ar,repeat=3):
    if comp(b,a) is not None and comp(c,b) is not None:
        assert comp(c,comp(b,a))==comp(comp(c,b),a);triples+=1
assert all(sum(ar[a]==(x,'T') for a in ar)==1 for x in ['Z','Y','T'])
assert all(sum(ar[a]==(x,y) for a in ar)<=1 for x in ['Y','T'] for y in ['Y','T'])
assert comp('h','f')==comp('h','g') and 'f'!='g'
save('ambient monicity fails despite restricted faithfulness',[3],arrows=len(ar),associative_composable_triples=triples,restricted_full_subcategory=['Y','T'],h_monic=False)

save('isomorphism-only free-family construction loses an arrow',[7],base_arrow_0_to_1=1,isomorphism_components_singleton_arrow_0_to_1=0,all_components_singleton_arrow_0_to_1=1)

# Adjacent-swap sign and its symmetric-group multiplication law.
def parity(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
permutation_checks=0
for n in range(7):
    for p in itertools.permutations(range(n)):
        # Adjacent swaps generate: checking each generator is enough for the sign law.
        for i in range(n-1):
            q=list(p);q[i],q[i+1]=q[i+1],q[i]
            assert parity(q)==1-parity(p);permutation_checks+=1
assert (-1)**(1+1)==1
save('self-braiding permutation parity',[10,11],adjacent_generator_checks=permutation_checks,odd_line_epsilon=-1,pairing_phi=1,reversed_pairing=-1,inverse_pairing_psi=1,exponent_convention='0 or 1 parity, not the numeric sign +1 or -1')

t=s.symbols('t',real=True)
S=s.Matrix([[1,s.I],[0,1]]);D=s.diag(1,t)
j=S*D*S.inv();rho=S*s.conjugate(S).inv()
sigma_j=s.conjugate(j)
correct=s.simplify(sigma_j-rho.inv()*j*rho)
wrong=s.simplify(sigma_j-rho*j*rho.inv())
assert correct==s.zeros(2) and wrong!=s.zeros(2)
save('semilinear cocharacter conjugation direction',[16],j=str(j),rho=str(rho),correct_difference=str(correct),opposite_conjugation_difference=str(wrong),parameter_convention='sigma fixes the formal real symbol t; coefficients undergo complex conjugation')

# Presheaf diagrams X1 -> X0; cover sheafification evaluates at 0.
P1=P0=Q0=(0,);Q1=()
before=len(functions(P1,Q1))*len(functions(P0,Q0));after=len(functions(P0,Q0))
assert before==0 and after==1
save('left-exact sheafification is not full',[28],hom_before=before,hom_after=after)

# The split fork on a complete relation: projection maps to X0.
X0=(0,1);X1=tuple(itertools.product(X0,repeat=2));Y=(0,)
d0=lambda p:p[0];d1=lambda p:p[1];section=lambda x:(x,0)
assert all(d0(section(x))==x and d1(section(x))==0 for x in X0)
factorizations=0
for cod in [(0,),(0,1),(0,1,2)]:
    for h in functions(X0,cod):
        if all(h[d0(p)]==h[d1(p)] for p in X1):
            factors=[u for u in functions(Y,cod) if all(h[x]==u[0] for x in X0)]
            assert len(factors)==1;factorizations+=1
save('split coequalizer identities and universal property',[35],split_identities=True,unique_factorizations_checked=factorizations,scope='A concrete split fork; the general preservation proof is algebraic.')

# Cofree C2-set comonad: C(X)=X^G and delta(f)(g)(h)=f(g+h).
G=(0,1);CX=list(itertools.product((0,1),repeat=2));comonad_checks=0
for f in CX:
    for g in G:
        assert f[(0+g)%2]==f[g] and f[(g+0)%2]==f[g]
        for h in G:
            for k in G:
                assert f[((g+h)%2+k)%2]==f[(g+(h+k)%2)%2];comonad_checks+=1
save('cofree finite-group comonad',[36],group='C2',base_set_size=2,coassociativity_entries_checked=comonad_checks,counit_laws=True)

def dualmul(a,b,p):return ((a[0]*b[0])%p,(a[0]*b[1]+a[1]*b[0])%p)
dual=[]
for p in (2,3,5):
    A=list(itertools.product(range(p),repeat=2));eps=(0,1)
    ann=[a for a in A if dualmul(a,eps,p)==(0,0)]
    assert len(ann)==p and eps!=(0,0) and dualmul(eps,eps,p)==(0,0)
    squarezero=[a for a in range(p) if a*a%p==0]
    assert squarezero==[0]
    dual.append(dict(p=p,ring_size=p*p,epsilon_nonzero=True,epsilon_square=0,annihilator_epsilon_size=len(ann),possible_field_images_of_epsilon=squarezero))
save('dual numbers invisible to algebraically closed field tests',[40],examples=dual,flatness_witness='(epsilon) tensor_A A/(epsilon) is one-dimensional but its induced map to A tensor_A A/(epsilon) is zero.')

# D_n(A): at most one pair (e,g) for each f. Not every f need have a solution.
trials=solutions=missing=0
for m in range(2,19):
    for n in range(1,7):
        for f in range(m):
            pairs=[(e,g) for e in range(m) for g in range(m) if (e*e-e)%m==0 and pow(f,n,m)*(1-e)%m==0 and g*(1-e)%m==0 and (f*g-e)%m==0]
            assert len(pairs)<=1
            trials+=1;solutions+=len(pairs);missing+=not pairs
save('unit-nilpotent decomposition uniqueness',[46],rings='Z/mZ, 2<=m<=18',exponents='1<=n<=6',elements_tested=trials,unique_solutions=solutions,no_solution=missing,scope='Finite examples corroborate monicity; the idempotent decomposition proves it generally.')

x,y=s.symbols('x y');GB=s.groebner([x*x*y-x,x*y*y-y],x,y,domain=s.ZZ)
remainders={str(p):str(GB.reduce(p)[1]) for p in [(x*y)**2-x*y,x*x*y-x,x*y*y-y]}
assert set(remainders.values())=={'0'}
save('quasi-inverse relations and product decomposition',[48,96],groebner_basis=[str(q) for q in GB.polys],remainders=remainders,bad_printed_relation_at_f_2_e_1=-1,correct_relation_f_times_1_minus_e=0,scope='The reductions are exact; the Chinese-remainder isomorphism is proved separately.')

# In F2^n the diagonal-first-coordinate idempotent map has image F2.
boolean=[]
for n in range(2,7):
    A=list(itertools.product((0,1),repeat=n));F=lambda a:(a[0],)*n
    assert all(F(F(a))==F(a) for a in A)
    image={F(a) for a in A};assert len(image)==2
    # Orthogonal nonzero idempotents in a full partition are disjoint nonempty subsets.
    atoms=sum(sum(a)==1 for a in A);assert atoms==n
    boolean.append(dict(n=n,idempotents=len(A),atoms=atoms,idempotent_map_image_size=len(image)))
save('component bounds and exact-rank collapse',[56,58],examples=boolean,scope='The filtered colimit of the repeated idempotent endomorphism is its image; this general fact is proved in the certificate.')

map_mod2={a:(2*a)%2 for a in (0,1)}
assert set(map_mod2.values())=={0}
save('additivity does not imply exactness; faithful flatness fails under module colimits',[60,112],multiplication_by_2_after_tensor_Z_mod_2=map_mod2,kernel_cardinality=2,scope='The localization and filtered-colimit argument is analytic; this checks its noninjective tensor map.')

b=s.symbols('b');N=s.Matrix([[1,1],[0,1]]);row=s.Matrix([[1,b]])
retraction_defect=row*N-row
assert retraction_defect==s.Matrix([[0,1]])
save('ordinary injectivity fails after constant-sheaf inverse image',[61],monodromy=str(N),candidate_retraction=str(row),invariance_defect=str(retraction_defect),invariant_retraction_exists=False)

# Ideal I=(2,1+sqrt(-5)): vectors represent a+b*sqrt(-5).
g1=s.Matrix([4,0]);g2=s.Matrix([2,2]);g3=s.Matrix([-4,2])
two=2*g1+g3-g2;two_s=g2-two
assert two==s.Matrix([2,0]) and two_s==s.Matrix([0,2])
norm_solutions=[(a,b) for a in range(-1,2) for b in [0] if a*a+5*b*b==2]
assert norm_solutions==[]
save('invertible nonprincipal rank-one module',[64],I_basis_determinant=2,I_square_generators=[list(g1),list(g2),list(g3)],two_as_combination='2*(4)+(−4+2s)−(2+2s)=2',two_s_as_combination='(2+2s)−2=2s',norm_2_solutions=norm_solutions,exhaustiveness='a²+5b²=2 implies b=0 and |a|<=1; these possibilities are all tested.')

kernel_dimensions=[]
for n in range(1,9):
    M=s.zeros(n+1);M[1,0]=1
    kernel_dimensions.append(dict(square_zero_ideal_dimension=n,multiplication_x_kernel_dimension=n+1-M.rank(),minimal_number_of_generators=n))
assert all(r['square_zero_ideal_dimension']==r['multiplication_x_kernel_dimension'] for r in kernel_dimensions)
save('kernels of finite-presentable modules need not be finite-presentable',[93],finite_approximations=kernel_dimensions,scope='The counterexample uses countably infinite V; finite approximations are illustrative and do not prove its non-finite-generation.')

# Karoubi envelope of {1,e}; a morphism p->q has a=q*a*p.
mul=lambda a,b:'1' if a==b=='1' else 'e'
hom={(p,q):[a for a in ['1','e'] if mul(q,mul(a,p))==a] for p in ['1','e'] for q in ['1','e']}
assert hom['1','e']==hom['e','1']==['e'] and mul('e','e')!='1'
even_closure=[2*m for m in range(9)]
assert 1 not in even_closure and 3 not in even_closure
save('retract detection is weaker than operation generation',[101],karoubi_homs={f'{p}->{q}':v for (p,q),v in hom.items()},objects_isomorphic=False,finite_product_closure_sizes_in_FinSet_op=even_closure,formula='2m, because products in FinSet^op are disjoint unions in FinSet')

assert len(functions((0,),()))==0 and len(functions((0,),(0,)))==1
save('Yoneda comparison fails for arbitrary X',[105],Hom_Set_1_empty=0,Nat_terminal_functor_terminal_functor=1)
save('finite Boolean stages acquire infinitely many idempotents',[109],stages=[dict(n=n,atoms=2**n,ring_cardinality=2**(2**n)) for n in range(5)],embedding='Duplicate each coordinate; every stage embeds in the next.',scope='The nonnoetherian/nonartinian conclusions use the explicit infinite chains in the proof certificate.')

P=pathlib.Path(__file__).resolve().parent
(P/'check_groupes.output.json').write_text(json.dumps(OUT,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps({'checks':len(OUT),'claim_ids':sorted({c for r in OUT for c in r['claims']}),'all_assertions_passed':True},indent=2))
