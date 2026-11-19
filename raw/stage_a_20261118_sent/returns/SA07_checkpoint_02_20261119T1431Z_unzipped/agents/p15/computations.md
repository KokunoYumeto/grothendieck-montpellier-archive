# Checks and derivations for package p15

All manuscript locators refer to physical lines in the supplied diplomatic transcription. The derivations below are this run's checks, not added manuscript text. Numerical or symbolic checks are in `code/compute_checks.py`, with the complete output in `evidence/compute_checks.out` and structured results in `evidence/computation_results.json`. Sixteen exact calculations were executed. No sampling is used as proof of a general assertion. References are keyed to `refs.json`.

## D1. Scalar transport and descent

For a field automorphism σ of L, put σ*V = V ⊗_{L,σ} L. A σ-semilinear map V→V is equivalently an L-linear map σ*V→V. An automorphism fixing the field over which an object is defined can act through descent data; an automorphism moving that field embedding produces a conjugate object. Composition uses the cocycle identity, rather than an unidentified canonical comparison. This checks CL-SA07-003 and the distinction used in CL-SA07-004–007. Deligne's comparison theorem [P15-D82, §1] provides specified period-ring/coefficient comparisons, not an arbitrary Q_l-linear identification.

## D2. The three real conjugations

Let X/R be smooth proper. On H_B(X(C),Q)⊗C, let c_B conjugate scalar coefficients and let f∞ be the Q-linear pullback of the topological involution on X(C). Since f∞ is defined on the rational lattice, c_B f∞ = f∞ c_B. Under the de Rham comparison, real descent conjugation is c_DR = f∞ c_B, so c_DR²=1 and c_DR commutes with c_B. Pullback by the antiholomorphic map exchanges (p,q) and (q,p). These identities require the geometric comparison diagram [P15-D82, pp7–9].

C09 checks why semilinearity alone is insufficient: A(z)=conjugate(z) and B(z)=i conjugate(z) are both involutions, but AB(z)=−iz and BA(z)=iz. Thus the handwritten “à vérifier” is a compatibility calculation, not a formal consequence of having two involutions. Claims008–010 retain this distinction.

## D3. A rational filtration intersection need not be a Hodge substructure

This checks only the natural ordinary-Hodge-filtration interpretation of the uncertain level formula, not every possible meaning of its index ρ. Let τ be a nonreal root of x³−2; choose the root with positive imaginary part and set E=C/(Z+τZ). Put V=H¹(E,Q)^{⊗3}, a rational Hodge structure of weight3 and dimension8. With suitable rational bases, the map V_C→V_C/F¹ has coefficients τ^{|I|}, indexed by the eight subsets I of a three-element set. Since 1,τ,τ² are Q-linearly independent and τ³=2, its kernel on V_Q has dimension8−3=5. C12 constructs the exact 3×8 rational matrix and computes rank3.

A rational Hodge structure of odd weight has even dimension: its summands (p,q) and (q,p) occur in conjugate pairs and p=q is impossible. Hence V_Q∩F¹ cannot itself be a Hodge substructure. This is the elementary obstruction behind the corrected “largest sub-Hodge structure” formulation [P15-G69, §§1–2].

The example also fits the real-variety setting of the manuscript. Take the real abelian variety A=Res_{C/R}E and X=A³. Over C, X is E³×conjugate(E)³ and H³(X,Q) contains V as a rational Hodge direct summand. For a real variety, f∞F¹=conjugate(F¹); a rational vector in F¹ already belongs to its scalar conjugate. The projection of H³(X,Q)∩F¹∩f∞F¹ onto V is V_Q∩F¹. If the former were a Hodge substructure, its Hodge projection would be one, contradicting dimension5. This is a check of an interpretation, explicitly separated from an ink decision.

## D4. The quaternion obstruction to a real fibre functor

Assume the category contains h¹(E) of a supersingular elliptic curve and every geometric endomorphism, and that the proposed ordinary real realization has dimension2 on h¹(E). Voight42.1.9 identifies End⁰(E) with the definite quaternion algebra ramified at p and infinity [P15-Voight21]. A faithful real tensor realization would give an injection H→M₂(R), where H is Hamilton's quaternion algebra. In fact no such representation exists: after choosing I²=−1, a real basis makes I=[[0,−1],[1,0]]. A matrix anticommuting with I has the form J=[[a,b],[b,−a]], so J²=(a²+b²)1, which cannot be −1. C04 verifies these equations symbolically.

Any fibre functor over a totally real number field could be extended along a real embedding, giving the forbidden real functor. The qualification about all geometric endomorphisms is essential: a smaller category over a finite base field may omit them. This checks CL-SA07-013 without identifying every gerbe mentioned elsewhere with the Deuring quaternionic gerbe.

## D5. Twisting a fibre functor

For a neutral tensor category with fibre functor ω and G=Aut^⊗(ω), a right G-torsor P gives ω_P(V)=P×^Gω(V), by faithfully flat descent of the vector bundle and all its tensor maps. Evaluation, tensor product and unit descend because the G-action preserves them. Locally trivializing P identifies ω_P with ω; transition functions conjugate G, so Aut^⊗(ω_P) is the corresponding inner form. This is the torsor construction of [P15-DM82, Theorem3.2], checking CL-SA07-015. It classifies fibre functors relative to a neutralization, not geometric points of a variety.

## D6. Generation by real Frobenius

Suppose 1→H→G→C₂→1 is exact and H=G⁰. If f maps to the nontrivial element of C₂, every geometric point of G lies in H or Hf, so the closed subgroup generated by H and f is G. The group calculation is elementary; the equality H=G⁰ is the substantive premise. The corrected [P15-DM82,6.22(a),6.23(a), footnote21] imposes the absolute-Hodge hypothesis for the relevant motivic connectedness statement. Thus CL-SA07-025 is conditional and does not repair an omitted motivic premise by group theory.

## D7. One fibre and monodromy in the abelian moduli case

Let S be reduced, connected and of finite type over C, and A,B/S abelian schemes. Suppose an isomorphism of integral R¹ local systems is given globally and at one point comes from an isomorphism of abelian varieties. Deligne4.1.3.2 extends that fibre morphism uniquely to a morphism A→B; applying the same statement to the inverse makes it an isomorphism [P15-D71, printed43]. If the given map respects polarization and sufficiently rigid level data at one point, the corresponding tensor identities continue, so the maps into the fine moduli space agree.

Identical based monodromy data and an identified fibre can supply the global local-system isomorphism. This proves the stated restricted reconstruction test. It does not prove that arbitrary polarized-motive moduli exist or that all spaces with such rigidity are motivic moduli. Claims026–029 separate these assertions.

## D8. Finite spreading, countable limits, and the false tower assertion

EGA IV3,8.8.2 proves that finitely presented objects and morphisms descend along affine inverse limits;8.8.3 explicitly extends the statement to finite diagrams and finitely many relations. The original printed28–33 were read. Theorem8.10.5, printed37–38, descends the listed properties of morphisms;9.7.7, printed79–80, gives constructibility of geometric connectedness, irreducibility and reducedness of fibres. These results concern finite data and suitable shrinking. They are not an infinite coherence theorem.

For a sequence of nonempty sets P_i with surjective maps P_{i+1}→P_i, select p₁, then recursively p_{i+1} above p_i. Countable dependent choice gives an inverse-limit point. Without surjectivity, even a sequence can fail: the inclusions {n,n+1,…}→{n−1,n,…} have no compatible element. The category of paths and the π superscript in the transcription must also be identified; ordinary and profinite path torsors are not interchangeable.

The page's preceding tower assertion is false for arbitrary countable k. Set k to an algebraic closure of Qbar(t) and k₀=Qbar. Both fields are countable, k₀ is the algebraic closure of Q inside k, and X=Spec(k) meets the stated normality and irreducibility setup. Suppose k=⋃A_i for finitely generated k₀-subalgebras, with Spec(A_j)→Spec(A_i) smooth and geometrically connected on fibres for j≥i. Set K_i=Frac(A_i). The generic fibre is smooth and geometrically connected; its components after algebraic closure are disjoint because it is regular, hence it is geometrically integral. Consequently K_i is relatively algebraically closed in K_j. Every element of k algebraic over K_i belongs to some K_j, so it lies in K_i. Since k is algebraically closed, K_i must be algebraically closed.

But a finitely generated field K_i/Qbar of positive transcendence degree cannot be algebraically closed. Choose a transcendence basis t₁,…,t_r and let d=[K_i:Qbar(t₁,…,t_r)]. Algebraic closedness would put t₁^{1/n} in K_i for every n, while X^n−t₁ is irreducible over the rational function field by the t₁-adic Eisenstein criterion, so n≤d for every n, impossible. Therefore all K_i would equal Qbar, contradicting ⋃K_i=k.

This refutes only CL-SA07-134, the blanket geometric tower construction. It leaves the final integral fibre-functor comparison unsettled. A relevant precise later result is [P15-BT25, Lemmas4.12–4.13], giving paths and Betti equivalence for finitely generated regular extensions with arc points. Its hypotheses are narrower than “every countable k,” and its rational Nori formulation is not silently substituted for the manuscript's integral category.

## D9. The elliptic-family test

For E_t:y²=x³+A x+B, with A=−3t/(t−1), B=−2t/(t−1), the characteristic-zero formulas give

Δ=−16(4A³+27B²)=1728t²/(t−1)³,
and j=1728·4A³/(4A³+27B²)=1728t.

C01 verifies both identities exactly. The family is smooth for t≠0,1; the base in the note also removes infinity. The displayed equation belongs to the earlier run, not the manuscript. An integral Hodge isomorphism H¹(E_s,Z)≅H¹(E_t,Z) identifies the associated complex tori, hence elliptic curves, so j(E_s)=j(E_t) and s=t. Rational Hodge isomorphism gives only an isogeny class [P15-MilneSV,6.8–6.9]. If a motivic category contains this family specialized at each a∈k minus{0,1}, and the comparison preserves these integral Hodge structures over the identity of C, it forces the two chosen embeddings to agree on every such a. This conditional test does not classify torsors or forget complex conjugation conventions.

## D10. Modified sections and the kernel formula

Let σ:π→E be a homomorphic section and u:π→N a homomorphism into the kernel whose image commutes with σ(π). Then
σ(a)u(a)σ(b)u(b)=σ(ab)u(a)u(b)=σ(ab)u(ab).
Thus σu is another section. Equality of two sections constructed this way requires an extra compatibility. C05 gives E=Z×Z→Z, σ₁=σ₂:n↦(0,n), u(n)=(n,0), and the second modifying homomorphism trivial. The two sections are (n,n) and (0,n); symbolic addition verifies the homomorphism property, and their values at1 differ.

If u and v=jχ are homomorphisms with commuting images, φ=uv^{-1} is a homomorphism. On kerχ one has φ=u, so kerχ∩kerφ=kerχ∩keru. Equality with all of keru holds exactly when keru⊆kerχ. C06 tests the missing premise on the complete two-element group: u=1, χ=sign, j=id; keru=C₂ but the intersection is trivial. This does not refute any unseen LM6 premise. Claims047–050 record the refined statements.

## D11. The p-adic analytic quotient

Let π be profinite and u:π→G(Q_p) continuous, with G a finite-dimensional linear algebraic group. The image is compact and hence closed in the Hausdorff p-adic Lie group. The continuous bijection π/keru→u(π) is a homeomorphism because its source is compact. The closed-subgroup theorem gives u(π) its p-adic Lie structure [P15-Gl16, Proposition2.2]. This proves CL-SA07-051 under these explicit hypotheses; an arbitrary abstract quotient is not automatically analytic.

## D12. Tate indices

With Q(n) of weight−2n and Hodge type(−n,−n),
W_i(E(n))=W_{i+2n}(E)(n), F^p(E(n))=F^{p+n}(E)(n), and
Gr_i^W(E(n))=Gr_{i+2n}^W(E)(n).
Already E=Q, n=1 disproves an unshifted graded formula: Q(1) lives in weight−2. C14 records the symbolic index changes. Forgetting the displayed tensor factor can be harmless under a chosen underlying-vector-space identification; forgetting the shifted index is not. Complex conjugation on the conventional Betti generator(2πi)^n contributes(−1)^n [P15-D82, p9].

## D13. Filtrations, splittings and central cocharacters

Let G be reductive in characteristic zero and P=L⋉U a parabolic with Levi L. A fixed filtration orbit is G/P; a compatible grading orbit is G/L. Thus dimFil=g−b and dimBig=g−ℓ=g−b+u. The map G/L→G/P forgets the grading. Its fibre P/L is a U-torsor after a Levi is chosen; no canonical reverse map exists. A grading cocharacter centralizes L because L preserves all weight subspaces. It need not be central in G. In contrast, a grading of the identity tensor functor is central in the full tensor group [P15-DM82, Definition5.1].

C08 checks G=GL₂: g=4,b=3,ℓ=2,u=1. Fil has dimension1, Big dimension2, and the space of splittings over a filtration has dimension1. The inverse image in P of a Tate G_m in L has dimension2. Consequently an H′-torsor and the space of Levi splittings cannot both be denoted Q without an extra quotient or trivialization; the manuscript does not settle which is intended.

For three fibre functors ω₁,ω₂,ω₃, composition is Isom(ω₂,ω₃)×Isom(ω₁,ω₂)→Isom(ω₁,ω₃), descending to the appropriate contracted product. Reversing the order of factors reverses composition. The manuscript's α,β,γ triangle is checked by domains and codomains; it provides rational relations among their fields of definition, not genericity.

## D14. Transcendence-degree bookkeeping

For finitely generated field extensions k⊂L⊂K, trdeg_kK=trdeg_kL+trdeg_LK. If K=k(α,β), trdeg_k k(α)≤g and trdeg_{k(α)}K≤u, equality trdeg_kK=g+u forces equality in both bounds. Applying the same argument through β and γ gives the manuscript's further equalities only when their individual bounds refer to the same torsors and base. The uncertain denominator at18/11 L1146–1147 must be k; writing trdeg(k(α)/K) with k(α)⊂K reverses the field extension. This remains an ink alarm, not an emendation.

For a period matrix P with determinant T=2πi in the chosen basis, adjoining √T permits P/√T∈SL₂. C15 computes det(P/√T)=det(P)/T. This proves one determinant relation, not algebraic independence of the three remaining coordinates. Likewise a transcendental parameter j contributes one to trdeg over Qbar compared with Qbar(j); a functional theorem does not decide every specialization. The full non-CM elliptic period claim remains distinct from the generated-torsor theorem [P15-BC16; P15-KSV26] and from the function-field result [P15-BT25].

## D15. CM produces an algebraic Hodge splitting

For a CM elliptic curve over Qbar, pass to a field defining a nonscalar CM endomorphism a and both eigenvalues a,conjugate(a). Its algebraic action on H¹_dR has distinct eigenvalues, so
e=(a*−a·1)/(conjugate(a)−a)
is an algebraic idempotent projector onto one eigenline. Its complementary projector gives the other. Under comparison these eigenspaces are the two Hodge lines [P15-Katz76, Lemma4.0.7; P15-BDP13,1.4.1]. The converse requires proving algebraicity of the projector implies an endomorphism; it is not formal. Confusing the Qbar-de Rham structure with the rational Betti structure invalidates that converse argument.

## D16. Residue normalization and the Gysin shift

Parameterize the positive unit circle by z=exp(it),0≤t≤2π. Then dz/z=i dt and its integral is2πi; C02 executes the symbolic integral. For p ordered complex normal coordinates, the product cycle with product orientation gives(2πi)^p. Thus the local analytic/algebraic residue generator maps to(2πi)^p times the integral topological generator, giving the manuscript's inverse factor for P_top.

If Y⊂X has complex codimension p and dimX=n, then a transversal T meeting Y in isolated points has dimT=p because dim(Y∩T)=(n−p)+dimT−n. The written n−p is incompatible with this ordinary codimension interpretation except accidentally when n=2p.

A complex normal bundle of rank p has oriented real rank2p. The Thom isomorphism and hence a closed-immersion Gysin map shift cohomological degree by2p, not p. Comparing the Thom class locally and using naturality/excision is the required local-to-global proof. The manuscript gives the circle computation but leaves that final explanation unfinished. The p18 continuation explicitly has degree+2p and the same(2πi)^{-p} scalar. Different duality-trace conventions can introduce further signs, so the comparison is stated in the manuscript convention [P15-BC16,§1.1.2].

## D17. Rank-one highest weights and divided powers

In sl₂, take [H,E]=2E,[H,F]=−2F,[E,F]=H and a highest-weight vector v with Ev=0,Hv=mv. Induction using the commutators gives E F^n v=n(m−n+1)F^{n−1}v. With v_n=F^n v/n!,
Hv_n=(m−2n)v_n, Fv_n=(n+1)v_{n+1}, Ev_n=(m−n+1)v_{n−1}.
C11 checks all three commutators symbolically. In characteristic zero, the nonzero vectors have distinct H-weights. If the module is finite-dimensional, choose q with v_q≠0,v_{q+1}=0. Applying E yields(m−q)v_q=0, hence m=q≥0. The usual finite string is therefore forced.

For m∈Z_{≥0}, divided powers act by F^r/r!:v_n↦binomial(n+r,r)v_{n+r} and E^r/r!:v_n↦binomial(m−n+r,r)v_{n−r}. Also binomial(H,r) has integral values on integral weights. This verifies the rank-one lattice, not every integral Chevalley structure requested elsewhere [P15-MilneLAG,§9]. The missing Casimir normalization cannot be inferred from these formulas.

## D18. Elementary automorphisms and Cartan subalgebras

Whenever the elementary automorphisms are exp(ad x) with ad x nilpotent in characteristic zero, a exp(ad x)a^{-1}=exp(ad(a x)). The generators are preserved by automorphism conjugation, so their generated group is normal. Transitivity requires the algebraically closed characteristic-zero or appropriate split hypotheses of [P15-MilneLAG,8.17,8.27].

If h is nilpotent and self-normalizing in g, it is so in every intermediate g′: N_{g′}(h)=g′∩N_g(h)=h. For the stronger statement that a subalgebra a containing h is self-normalizing, use the Fitting decomposition for the h-action in the standard finite-dimensional characteristic-zero setting. The zero Fitting part of g is h. Since a contains h, the zero part of g/a vanishes; a normalizer element gives an h-invariant class in g/a and hence belongs to a. This is distinct from replacing rank by the dimension of the centralizer of an arbitrary regular nilpotent element.

Restriction of scalars admits a separate algebraic proof. If h is a k-Cartan subalgebra of a K-Lie algebra, K h is nilpotent of at most the same class. Every proper subalgebra of a nilpotent Lie algebra has a larger normalizer: choose the least term of the ascending central series not contained in it. Thus self-normalization of h forces K h=h, so h is K-linear. Conversely the normalizer and nilpotence conditions do not change for a K-linear h when forgetting scalars. If “Lie algebra” is restricted to finite-dimensional algebras over the ground field, require[K:k]<∞ to stay in that category. Milne8.5 concerns extension, not this restriction assertion; the proof here is independent.

## D19. Rank and the adjoint characteristic polynomial

In the manuscript convention, rank(g) is the least algebraic multiplicity of0 in the characteristic polynomial of ad X. For a nilpotent algebra each ad X is nilpotent, so the rank is dim g. In characteristic2, sl₂ has basis E,F,H=1, with[E,F]=H central and[H,E]=[H,F]=0; C03 checks this exact matrix calculation. Thus it is nilpotent of class2, confirming the author's objection to an unrestricted positive-characteristic transfer.

In characteristic-zero analytic groups, Ad(exp X)=exp(ad X). In a sufficiently small exponential neighborhood, eigenvalues of ad X cannot reach a nonzero element of2πiZ (and the analogous small p-adic exponential is injective on its domain). Hence the multiplicity of1 in Ad(exp X) is at least the multiplicity of0 in ad X, at least rank(g). Over R or C, divisibility of the characteristic polynomial by(t−1)^r is the vanishing of finitely many analytic coefficient functions. Vanishing on an identity neighborhood extends to a connected analytic group. This verifies the explicit bound, not the unknown “Lefschetz lemma” or the missing rank formula.

## D20. Generalized weights and the Ad/ad alarm

If(D−λ)^r v=0 and(D′−μ)^s w=0, then on v⊗w the additive tensor action minus λ+μ is N⊗1+1⊗N′. The summands commute; every term in its(r+s−1)-st power has at least r copies of N or s of N′, hence vanishes. An equivariant bilinear map sends this vector into the generalized λ+μ space. For a multiplicative action, A⊗B−λμ=(A−λ)⊗B+λ·1⊗(B−μ); the same commuting-nilpotent expansion proves the product-weight statement. Galois descent needs stable spaces and cocycle data; the missing characteristic-space correction is not reconstructed from this calculation.

For a genuine group element g, Ad(g) is invertible, with inverse Ad(g^{-1}). On a nonzero vector space it cannot be nilpotent. The differential ad X can be nilpotent. This raises the reading alarm at15/204 without deciding whether the source uses an older notation.

## D21. Nonempty open subsets

In an irreducible topological space every nonempty open subset is dense, directly from the definition. Affine space over an infinite field has dense nonempty principal opens: a nonzero polynomial cannot vanish identically on every point, and the product of two nonzero polynomials is nonzero. Over an algebraically closed field the scheme-theoretic version follows from the domain coordinate ring. The statement fails for a reducible space: one component of a disjoint union of two points is open and not dense. The manuscript therefore needs its ambient irreducibility hypothesis; no general density theorem follows from the word “open.”

## D22. Roots, compact real forms and exponential lattices

For a complex semisimple Lie algebra with Cartan h, a root α is a functional on h and g_α={x:[h,x]=α(h)x for every h∈h}. The printed α(x) is ill-typed. For a compact real Lie algebra, complex characters are weights on its complexification; multiplication of a real vector by a general complex character does not define a real eigenspace. These are reading alarms, not source emendations.

The exponential lattice depends on the global group. In sl₂(C), H(z)=diag(z,−z), and expH(z)=diag(e^z,e^{-z}). For SL₂ the kernel is z∈2πiZ; for PGL₂ it is z∈πiZ. The coroot is H(1), the coweight H(1/2), so the extreme lattices are2πiQ∨ and2πiP∨. The quotient describes the order-two centre of SL₂ or fundamental group of PGL₂. The dual character lattices are the weight and root lattices respectively. This checks the normalization explicitly; the general classification is [P15-ConradPi1, Theorem1.1 and§2; P15-SGA3XXI]. Restricted roots are a separate, possibly nonreduced system [P15-Knapp23,6.53; P15-Conrad20,11.3.8].

## D23. Local group identities

The four pairs for local associativity are(x,y),(y,z),(m(x,y),z),(x,m(y,z)). Replacing the last pair by the product m(x,m(y,z)) is a type error because Ω⊂G×G. With the corrected type, θ(e)=e follows from the unit and inverse axioms. For θ²(x)=x, take a=θ²(x),b=θ(x),c=x. The pairs(a,b),(b,c) are inverse pairs, and(m(a,b),c)=(e,x),(a,m(b,c))=(a,e) are unit pairs. Thus all domain conditions hold, and a=m(a,e)=m(m(a,b),c)=m(e,c)=c.

For a C^r multiplication, r≥1, near(e,e) with m(e,x)=m(x,e)=x, the derivative in either variable at(e,e) is identity. The implicit-function theorem gives a right inverse r(x) and a left inverse l(x), with the same regularity, after shrinking. Local associativity gives l(x)=l(x)(x r(x))=(l(x)x)r(x)=r(x) on a small enough neighborhood. Shrink again so the inverse is defined and invariant on that neighborhood. This proves the asserted local inverse under the analytic hypotheses; it does not globalize an arbitrary local group [P15-Bruhat58, Chapter2§2.2; P15-Olver, Definition2].

## D24. Tangent and distribution constructions for local groups

For point-supported distributions S,T, define(S*T)(f)=(S⊗T)(f∘m). Only the germ of m at(e,e) matters. If the orders are a,b, the right side requires a+b derivatives; in class C^r it is defined when a+b≤r. Associativity follows by applying S⊗T⊗R to the two equal local functions f(m(m(x,y),z)) and f(m(x,m(y,z))) wherever the sum of orders is allowed. The delta distribution at e is the identity. For a morphism h, h_*S(f)=S(f∘h), and h∘m_G=m_H∘(h×h) gives h_*(S*T)=h_*S*h_*T. The smooth operator correspondence has a precise modern form in [P15-BN14, Theorem5.2].

For the tangent construction, T(G×G)=TG×TG and TΩ is an open subset. The chain rule sends associativity, unit and inverse diagrams to the corresponding tangent diagrams. The identity is0_e and inversion isTθ. Differentiating a C^r map gives a C^{r−1} map on tangent bundles. Naturality of the tangent projection gives the morphism TG→G. These arguments check the individually written constructions; they do not reconstruct absent propositions3,3bis,11,12 or every claim in sections12–16.

## D25. Invariant top forms and the modular character

For ω_e∈∧^nT_e^*G, set ω_x=(dL_{x^{-1}}|_x)^*ω_e. This is the unique left-invariant n-form with valueω_e, so the invariant space has dimension1. In coordinates its coefficient is det(D₂m(x^{-1},x)), giving15/218(31). Since right translation commutes with left translation, R_y^*ω is another such form. At e, translate back by L_{y^{-1}}: the derivative is Ad(y^{-1}), so R_y^*ω=detAd(y)^{-1}ω.

Over a local field the coordinate measure associated with|ω| transforms by the field module of this determinant and is left Haar. For C the module is the squared ordinary complex absolute value; writing merely a complex modulus without this convention would be ambiguous. Li's δ_G uses|detAd|; the manuscript's Δ is its inverse [P15-Li26, Remark1.24, Example1.39, Proposition1.40].

C10 checks G={(a,b):a>0},(a,b)(c,d)=(ac,b+ad). Left Haar is da db/a² and right Haar da db/a. Right pullback by(c,d) scales the former by1/c, whereas detAd(c,d)=c. This fixes the direction of the inverse rather than comparing symbols by name.

## D26. The covering-number existence proof

Let K_+ be the nonnegative continuous compactly supported functions and g∈K_+ nonzero. A positive lower bound for g on a nonempty open set and a finite translate cover of supp f give f≤Σc_iL_{s_i}g. Define(f:g)=infΣc_i. Translating a cover, scaling its coefficients and adjoining two covers prove invariance, homogeneity and subadditivity. Taking a point where f has its maximum gives(f:g)≥sup f/sup g. Replacing every translated g in a cover by a cover in h gives(f:h)≤(f:g)(g:h); approximate infima suffice, so no minimum is assumed. For fixed nonzero f₀ this implies
1/(f₀:f)≤I_g(f):=(f:g)/(f₀:g)≤(f:f₀).

For approximate additivity choose h≥1 on supp(f+f′), F=f+f′+εh/2, and φ=f/F,φ′=f′/F there, extended by0 outside. These are continuous compactly supported functions. Uniform continuity gives a compact identity neighborhood V with oscillation≤η under right increments in V. If g is supported in V, multiplying a cover of F by φ and φ′ gives
(f:g)+(f′:g)≤(1+2η)(F:g).
Subadditivity and submultiplicativity bound its excess over(f+f′:g) by[ε/2+2ηC+εη](h:g), C=(f+f′:h). Taking η=ε/[2(2C+ε)] makes the bracket exactly ε; C13 verifies this algebra. This reproduces the displayed inequality without assuming attained infima.

Choose one ultrafilter on nonzero test functions refining the filter of supports shrinking to e. Each coordinate I_g(f) lies in a fixed compact interval, so it has a limit I(f) along that same ultrafilter. Invariance and homogeneity pass to the limit. Subadditivity gives one inequality and approximate additivity gives I(f)+I(f′)≤I(f+f′)+εI(h) for every ε>0, hence equality. Also I(f₀)=1. Extend additively from the positive cone to C_c(G,R), then complexify; local boundedness follows from positivity and a compactly supported majorant on each compact set. Riesz representation produces a nonzero positive Radon measure. The manuscript supplies the beginning and key estimates; its missing continuation is reconstructed from the full matching proof in [P15-Li26, Theorem1.20], not attributed to the available sheet.

## D27. Haar uniqueness and complex invariant measures

Let μ be positive left Haar and ν right Haar, or more generally a complex right-invariant Radon measure. Choose f∈C_c(G) with μ(f)≠0 and put
D_f(x)=μ(f)^{-1}∫f(y^{-1}x)dν(y).
The integrand is supported on a compact set locally uniformly in x, so D_f is continuous. Fubini applied to f(x)g(yx), with its compact support in G×G, and the two invariances gives ν(g)=μ(D_fg). Thus for f,f′, μ((D_f−D_f′)g)=0 for every test g. Taking g to be the conjugate difference times a nonnegative cutoff shows the continuous difference vanishes because μ has full support. Denote it D. At e,
μ(f)D(e)=ν(check f)=checkν(f).
Both sides are linear in f; by adding a fixed test function of nonzero μ-integral, the identity extends to every f. Thus checkν=D(e)μ. If ν is positive and nonzero the scalar is positive; if complex it may be any complex number, including0. This proves the page's corollary with the necessary complex-conjugate modification to the real square argument. The full matching setup is in [P15-Li26, Theorem1.20].

## D28. Haar examples, unimodularity and relative invariance

On(R,+), substituting u=x+a preserves dx. On(R_{>0},×), u=tx gives dx/x=du/u. On R/Z, integrating a periodic continuous function over[a,a+1] is independent of a, and translation merely moves that interval. These verify all three manuscript examples.

Inversion turns a left Haar measure into a right one. In the unimodular case checkμ=cμ with c>0; applying inversion twice yields c²=1, hence c=1. Translation and inversion formulas then hold for integrable functions and measurable sets. A compact conjugation-invariant identity neighborhood V has0<μ(V)<∞; conjugation rescales its measure by the modular character but leaves V fixed, forcing that character to1. Counting measure proves the discrete case, trivial conjugation proves the abelian case, and a compact group's character into R_{>0} has compact image, necessarily{1}. For finite G, counting mass|G| and total mass1 differ by|G|.

For connected real or complex Lie groups, detAd(exp X)=exp(tr ad X). If g is nilpotent, ad X is nilpotent and has trace0. If g is semisimple, g=[g,g] and tr ad[X,Y]=tr[adX,adY]=0, so the linear trace functional vanishes on g. Thus the modular character is1 on an identity neighborhood and, by connectedness, on G. This supplies the explicitly deferred proof.

Neither closed subgroups nor quotients preserve unimodularity in general. Set G=R⋉R² with multiplication(t,x,y)(s,u,v)=(t+s,x+e^t u,y+e^{-t}v). Its adjoint determinant is1 (C16). The closed subgroup y=0 is ax+b, with determinant e^t; the closed normal subgroup N={(0,0,y)} has quotient the same ax+b group. Both are nonunimodular. The example verifies the quotient assertion with normality, not just an arbitrary homogeneous space.

For a right action with μ(As)=χ(s)μ(A), the pushforward of μ under x↦xs has valueμ(As^{-1})=χ(s)^{-1}μ(A), hence∫f(xs)dμ(x)=χ(s)^{-1}∫f dμ. Inversion pushforward gives checkμ(A)=μ(A^{-1}) and checkμ(f)=μ(check f). Passing to the opposite group changes which composition is called a left action, not these explicit formulas. This is the convention check for15/228.

## D29. Formal maps and coalgebras

Work first over a commutative ring K with finite free formal disks, whose continuous coordinate algebras are K[[X₁,…,X_m]] and K[[Y₁,…,Y_n]]. Let U be the direct sum of coefficient-extraction distributions e_α, paired with X^α. Its diagonal is Δe_α=Σ_{α₁+α₂=α}e_{α₁}⊗e_{α₂}. Writing ψ(e_α)=Σ_βa_{αβ}e′_β, diagonal compatibility is exactly the manuscript convolution formula(32); this is obtained by comparing the coefficient of e′_{β₁}⊗e′_{β₂}.

The actual condition ψ(U₀)=U₀ says a_{00}K=K and a_{0β}=0 forβ≠0. Thus a_{00} is a unit; compatibility makes a_{00}²=a_{00}, so a_{00}=1 over any commutative ring. Merely nonzero would be insufficient: C07 gives(1,0)∈Q×Q, a nonzero idempotent different from1. The proposition does not suffer this gap when its onto condition is retained.

Set B_β(X)=Σ_αa_{αβ}X^α. Formula(32) says B_{β₁+β₂}=B_{β₁}B_{β₂}. In particular B₀ is idempotent with constant1, hence is1 by comparing the lowest nonzero homogeneous term of B₀−1; equivalently a formal series with unit constant term is a unit, so B₀²=B₀ implies B₀=1. The series φ_j=B_{e_j} have zero constant term, and B_β=∏φ_j^{β_j}. They therefore define a unique continuous augmented substitution Y_j↦φ_j. Transposition is ψ. Conversely every such substitution preserves the diagonal and degree-zero line. Since φ_j have positive order, a_{αβ}=0 for|β|>|α|, so ψ preserves the order filtration, not necessarily homogeneous degree.

The pairing also identifies formal N-valued series with Hom_K(U,N), pointed series with the maps vanishing on U₀. The other supplied package gives an immediate continuation:18/018 L5–9 is source page A–20, preceding this package’s A–21; it defines the filtered coalgebra with counit and begins the sentence completed at18/016 L1236. Moreover18/022 L83–93 defines formal charts over a ring K and morphisms between them. For infinite free modules and general separated modules, row-finiteness, topology and the still earlier polynomial-map convention require further source checking. [P15-Strickland00, Definition4.58, Proposition4.59, Remark4.62] supplies one precise good-basis setting; it is not automatically the entire manuscript convention.

## D30. Splitting coefficients and the Tate period in the comparison field

**Claims:** CL-SA07-135–136; 18/011 L1134–1137. These are two additional explicit formulas on the leaf, separate from its transcendence conjecture. The following is an independent finite-dimensional check, using the pure Hodge realization furnished by [P15-D82, Theorem1.4 and §3].

Choose rational Betti coordinates and k-rational de Rham coordinates, and let P be the matrix of the comparison from Betti to de Rham. Put L=Q(k(P),conjugate(k(P))); this field contains k, its conjugate, P, its inverse, and both conjugate matrices. Betti conjugation, transported to de Rham coordinates, sends a vector v to P conjugate(P)^{-1} conjugate(v). Because the Hodge filtration is defined over k, both F^p and its transported conjugate filtration are defined over L. For a pure structure of weight w, each Hodge subspace is F^p intersect conjugate(F^{w-p}). Intersections are kernels of finite matrices over L. Thus the direct-sum decomposition and the inverse isomorphisms from its summands to gr_F^p are defined over L. Every coefficient of the canonical splitting beta lies in L, proving k(P,beta)⊂L. This argument covers this canonical pure Hodge splitting. An arbitrary chosen splitting need not satisfy the inclusion.

For the second formula, restrict the tensor comparison to its Tate object Q(-n). In compatible bases the comparison is multiplication by a power (2pi i)^n or its inverse, depending on whether the comparison and object are written covariantly or contravariantly. Deligne82 §1 explicitly gives the Betti lattice 2pi i Q and de Rham line k. Evaluation of an Isom-torsor point on an object is defined over k, so the scalar is in k(alpha). Its inverse is in the same field. A nonzero change of k-rational basis multiplies it by k^*, and therefore does not alter the stated field inclusion. No claim of transcendence degree follows from either calculation.

## Verification limits

The original SGA6 PDF assembly omits printed580, the middle page of X7.13.11, as well as582–584. Printed579 and581 were visually checked, and the omission was confirmed in the assembly source. The exact integral specialization square on580 remains unverified in an original scan; no AI retypesetting is accepted as a replacement. The requested manuscript Casimir formula, source propositions5–6 and3(c), the half-root formula and several operator definitions are absent from the supplied pages. They have no executable calculation to reproduce, and are explicitly indexed as unidentified rather than supplied from memory.
