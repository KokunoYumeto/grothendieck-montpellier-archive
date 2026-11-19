# Mathematical checks for the bt contribution

These are checks of specific statements, not a claim that every deep theorem cited has been independently proved. Claim identifiers refer to `claims.json`; exact executable checks and results are in `compute_checks.py` and `compute_checks.output.json`. Bibliographical locators and the extent of each external reading are in `reference_checks.json`. All checks were made on 19 November 2026. The source text is never modified.

## 1. Characteristic and the closed-form target

**C-SA23-bt-001–002.** The phrase “constant coefficients” is defined later on the sheets by the kernel of evaluation along the stratification section. We therefore use that definition, not the different ordinary meaning “a polynomial in coordinate derivatives with scalar coefficients.” Assuming the asserted exact operator complex, write D=Δd⁰. Replacing Δ by Δ+Λd¹ does not change its restriction to ker d¹. This proves the proposed canonical factorization only under the exactness hypothesis that supplies the presentation.

Characteristic zero is substantive. In k[[x]] of characteristic p, the coefficient of x^(p−1)dx in d(Σa_n x^n) is p a_p=0. Hence x^(p−1)dx is closed and has no formal primitive. The finite tests p=2,3,5,7 merely illustrate this unrestricted coefficient argument. This does not assert that every positive-characteristic divided-power reformulation fails. Grothendieck, *Crystals*, §6.5, pp.349–350, explicitly separates the ordinary characteristic-zero Poincaré result from the positive-characteristic situation.

For a matrix-valued Maurer–Cartan form θ=g⁻¹dg, differentiation gives dθ=−θ∧θ. Thus the ordinary closed-form target requires a vanishing bracket, for example commutativity of the group. The retained page does not contain the preceding group assumptions, so the target is flagged rather than silently repaired.

## 2. Holomorphic integrals and Gauss–Manin

**C-SA23-bt-003–014.** Fix a reference path in a smooth fibre. A finite subdivision places each short segment in a relative primitive chart. Smoothness gives holomorphic local sections through the subdivision points. For nearby base points, continuity and local homotopy invariance let us replace the chosen segment by one connecting these sections in the same chart. Its integral is the difference of two holomorphic values of a primitive. Summing finitely many such differences proves holomorphy. A change of path is a closed-cycle period. Period annihilation therefore proves path independence of μ, and concatenation gives its endpoint cocycle identity.

For a base vector field v with two lifts ṽ and ṽ′, the difference w is vertical. On relative forms, L_w=dι_w+ι_wd. Hence the induced actions on relative de Rham cohomology agree. An integrable splitting gives a representation of base differential operators by lifted Lie derivatives, with flatness following from the bracket identity. A global lift or a global primitive is not guaranteed on arbitrary non-Stein spaces; the author's marginal warning is needed. Grothendieck §1.2 and §3.3, and Katz–Oda §2–4, use hypercohomology and the appropriate local/affine hypotheses.

For horizontal endpoint sections and ω=dφ in a primitive chart,

\[
D\bigl(\phi(b)-\phi(a)\bigr)
 = (\overline D\phi)(b)-(\overline D\phi)(a)
 =\int_a^b\overline D\omega.
\]

Subdivide and iterate to obtain the higher-operator formula. If ΣD̄_iω_i=dφ, the conclusion is μ(a,b)=φ(b)−φ(a). **It is not generally zero.** With X=A¹_x×S, product connection, ω=dx, D=identity, a=0 and b=1, every stated hypothesis holds: fibres connected, closed holomorphic ω, zero cohomology class, zero cycle periods and horizontal endpoints. The result is 1. This is the exact `horizontal_arc_counterexample` output.

The claim that arbitrary sections can be made simultaneously horizontal also fails at an intersection: a(s)=0 and b(s)=s in A¹×A¹ meet at (0,0) with different tangent lifts of ∂s. A splitting supplies one lift at that point. This is a local obstruction, independent of global existence of a connection.

For moving endpoints, in a primitive chart the chain rule gives

\[
\frac d{dt}\int_{a(t)}^{b(t)}f(t,x)\,dx
 =\int_{a(t)}^{b(t)}\partial_t f(t,x)\,dx
 +f(t,b(t))b'(t)-f(t,a(t))a'(t).
\]

The invariant version replaces endpoint derivatives by contraction with their vertical velocities relative to the chosen lift and uses a Lie derivative for the interior term. Local primitive expressions glue. The polynomial example in `endpoint_formula` checks all three terms with exact symbolic arithmetic; their difference is zero. This completes a first-order reconstruction of the source's unfinished calculation, and is not evidence that the manuscript itself completed it. Higher-order operators produce endpoint jets by iteration.

For the deleted closedness argument, take ω=t dx on A¹_x×A²_(t,u). It is relatively closed. The section x=u pulls it back to t du, and d(t du)=dt∧du≠0. This explains the mathematical necessity of distinguishing relative from absolute closedness, while preserving the author's cancellation.

The period criterion in the forward direction follows from integrating an exact form around a cycle. In the reverse direction, de Rham's theorem detects a **fibre** cohomology class. One must still have the correct cohomology sheaf and sufficient base-change/detection hypotheses before concluding a section vanishes. The smooth proper comparison supplies these; the naive global-form quotient on an arbitrary non-Stein space does not.

## 3. Formal operator complexes and principal parts

**C-SA23-bt-015–021.** The finite-order assertions on 93/231 are not proved merely by writing “formally exact.” The +1 order shifts require first-order operators, or a correspondingly changed bound. The left and right composition sequences also involve different exactness questions: covariant and contravariant Hom need not preserve a merely exact module sequence in the same way. No unrecorded definition of formal exactness is supplied here.

For the conditional injectivity question on 232, let Δ represent D=Δd⁰. If Δ vanishes on ker d¹, it vanishes on im d⁰, because d¹d⁰=0. Therefore D=0. Well-definedness under Δ↦Δ+Λd¹ follows directly. This resolves the injection **conditional on the stated quotient presentation**, without asserting surjectivity onto all additive maps of closed forms.

EGA IV₄, Definition 16.8.1 and Proposition 16.8.4, printed pp.39–41, identify order-≤i operators M→P with O-linear maps P^i(M)→P for the left module structure. Maps whose pullback to E has augmentation zero are precisely those annihilating Oρ_i(E). They are therefore represented by the quotient Φ_i. The maps P^(i+1)(M)→P^i(M) are surjective and take ρ_(i+1)(E) to ρ_i(E), giving surjective maps on the quotients. This proves the asserted strictness.

The notation ρ∞ alone does not encode a stratification. Its augmentation must be the stated surjection E→M, and the iterated principal-parts maps must satisfy a diagonal cocycle condition. Grothendieck's *Crystals* Appendix supplies the general cocycle definition, but the sheet's complete quotient-specific conditions remain unwritten.

## 4. Square-zero torsors and the derived comparison

**C-SA23-bt-022–031.** Let I²=0 in the base, and let smooth lifts have fixed identified reduction X₀. Smoothness supplies local lifts of isomorphisms. The difference of two lifts is a derivation into I O_X₀: expanding multiplicativity shows the quadratic error vanishes. For automorphisms reducing to the identity, (id+δ)(id+ε)=id+δ+ε and the inverse is id−δ. Their sheaf is therefore additive, and the isomorphism sheaf is a torsor under it.

A torsor P under an additive sheaf G determines an extension Ḡ of Z by G. Form the sheafification of G⊕Z[P] modulo [p+g]−[p]−g. The degree of each [p] is one. Choosing a local p identifies the quotient with G⊕Z and identifies degree one with P. Changes of local p give exactly the torsor transition cocycle. Thus the construction is independent of a local choice and exact.

Place L=[G→Ḡ] in degrees **−1,0**. A local section of P gives

\[
L\simeq \mathbf Z[0]\oplus [G\xrightarrow{1}G].
\]

The second summand is contractible, so L⊗K′→K′ is a quasi-isomorphism for any K′, without a flatness hypothesis. Tensoring a contractible complex has its explicit tensor contracting homotopy. This is why a general assertion that G or Ḡ is flat is neither needed nor justified.

In the Hom complex, a degree −1 map k has differential d_Hom(k)=d k+k d. The compatible affine relation is u(p+g)−u(p)=d_Hom(k(g)), with k additive. It supplies a chain map from L to Hom(K′,K″) and hence from Tot(L⊗K′) to K″. Together with the quasi-isomorphism above, it gives the desired roof. The geometric multiplicative torsor formula must first be translated into this additive Hom-complex formulation; the published §3.4 makes that translation explicitly.

The dependence on k is real in the abstract problem. On X=S¹, choose constant G=Z and a Z-torsor representing a nonzero H¹(S¹,Z) class. Put K′=Z[0], K″=Z[1] and u=0. Both k=0 and the identity degree −1 map satisfy the relation because differentials vanish. The first roof is zero; the second represents the torsor class in Hom_D(Z,Z[1])=H¹(S¹,Z). Thus the geometry must specify compatible homotopies; knowing only that local maps are homotopic is insufficient.

The boxed O_X≃RHom(K′,K″) cannot be universal: at a point, K′=K″=k² yields dimensions 1 and 4. What is needed is a morphism from the coefficient unit to ordinary Hom, then the natural comparison to derived Hom. Moreover de Rham differential satisfies d(fα)=df∧α+f dα, so it is generally not O_X-linear. The coefficient category is the appropriate inverse-image base ring, as in Grothendieck §1.3 and §3.4.

For the geometric contraction, write a relative form locally as a sum of f₀ df₁∧…∧df_r. Applying id+δ creates terms with one I-factor; two such factors vanish. Since I comes from the base, d_rel I=0. The one-factor expansion agrees with dι_δ+ι_δd. Contraction kills I-multiples and is additive in δ. Hence composed comparisons have compatible additive homotopies and the roof is transitive; the identity comparison is the identity. Local maps are isomorphisms, so the canonical derived comparison is an isomorphism. This is the precise first-order construction published in *Crystals*, §3.4, pp.326–329. It is not an unrestricted integral nil-invariance theorem.

## 5. Serre's envelope and Hodge–Tate arguments

**C-SA23-bt-032–042, 056–060.** Convergence of p-adic exponential and standard reductive Lie representation theory are carried as background. The finite-index semisimplicity step can be checked directly. For an open normal G₁, an irreducible G-module restricts semisimply: the sum of the finitely many G-conjugates of a simple G₁-submodule is the entire module. Conversely, average a G₁-equivariant projection onto a G-stable subspace over G/G₁; characteristic zero permits division by its order. The invariant subspaces for a small exponential subgroup and for its Lie algebra coincide.

The Zariski closure of a subgroup is a subgroup: the ideal of functions vanishing on G is stable under the Hopf operations, as checked after evaluating at G×G and G. Under semisimplicity, take the connected algebraic group with the algebraic envelope Lie algebra; a small open subgroup of G lies in it. G normalizes that Lie algebra and hence that connected group, so finitely many translates form the required algebraic envelope. Every component meets G. If the centre Lie algebra is algebraic, the Lie algebras agree and exponential neighbourhoods prove openness.

For tensor stabilization, add det(V)* to force a special-linear realization. In characteristic zero reductivity supplies invariant-polynomial separation of the closed left-H orbits H and Hg in the endomorphism space. Polarization expresses the polynomial obstruction using mixed tensor invariants. Equality of the closed subgroup schemes then gives the all-commutative-algebra point statement; merely checking rational points over the original field would not suffice.

Serre's proof of the Hodge–Tate injection uses a minimal nonzero C-linear relation among K-bases of the eigenspaces, normalized to have one coefficient one. Apply s∈G_K, divide by the character of the normalized term, and subtract. Minimality forces the coefficients to transform by the relative cyclotomic character. Tate's theorem that C has no such nonzero eigenspace for a nonzero twist, and C^G_K=K, reduces the relation to a K-linear dependence within one eigenspace, a contradiction. **Those Tate invariant results are the deep input; only the ensuing argument is rechecked.** Dualizing the direct-sum decomposition negates weights; tensoring adds them.

A G-invariant mixed tensor is Galois invariant and has Hodge weight zero. Thus the Hodge cocharacter fixes it, and the stabilizer theorem places the cocharacter in G_alg. A group generated by conjugates of a connected torus is connected. This does not eliminate finite components of the inertia envelope. For K=Q₃ and the ramified quadratic character from Q₃(√3), V is semisimple and becomes trivial over a finite extension, hence is Hodge–Tate of weight zero. Its Hodge group M is trivial, while I_alg=μ₂. This refutes the marginal equality without a superscript zero.

The course summary assumes **algebraically closed residue field** on scan19, line1007. Its weight-zero finite-image conclusion is not valid for finite-residue K: an infinite continuous unramified character has weight zero but infinite image. Likewise the unrestricted assertion that every Hodge–Tate image is open in its algebraic envelope fails in general. For p odd, choose α∈Z_p\Q and an unramified representation with Frobenius mapping to diag(exp(p),exp(pα)). Its compact image is the one-parameter group diag(exp(pt),exp(pαt)), t∈Z_p. An algebraic subtorus relation would require integers m,n with m+nα=0; none exists except m=n=0. The envelope is G_m² but the Lie algebra has dimension one, so the image is not open. Unramified p-adic representations are crystalline of weight zero; that standard fact is used as background here. These tests explain the scope boundary, not an error in the course's explicitly restricted theorem.

The proalgebraic component quotient remembers finite representations; all finite representations are Hodge–Tate after finite trivialization. The connected abelian quotient described by the inverse system of restriction-of-scalars tori is a protorus, not one finite-dimensional torus. The exact theorem and its standing hypotheses are read in Serre1979, §2.4, Theorem6.

## 6. Two-weight reductive groups and Jordan pairs

**C-SA23-bt-043–046, 061, 086.** Let h=n₀+n₁ with positive coprime n₀,n₁. The determinant-one cocharacter ψ has weights n₁ on the n₀-dimensional part and −n₀ on the n₁-dimensional part. Its determinant exponent is n₀n₁−n₁n₀=0. For ζ^h=1, ζ^(−n₀)=ζ^n₁, so ψ(ζ) is scalar. Since gcd(n₁,h)=1, these scalars exhaust μ_h.

The irreducible representation of a product of simple factors is an outer tensor product. Restricting a lifted cocharacter gives positive-coefficient Laurent character factors. If two factors each have at least two exponents, their support sum has at least three exponents: the least sum, a strictly intermediate sum, and the largest sum. Positivity prevents cancellation. Thus at most one factor has more than one weight. The product of dimensions of all other factors divides both n₀ and n₁, so coprimality makes that product one. This is the unrestricted argument behind the bounded polynomial enumeration; the enumeration alone would not prove it.

For the remaining simple factor, μ_h in its centre forces the centre-order divisibility used by Serre's classification lemma. The opened centre table in Milne §24c and the source's classification argument are consistent. The exceptional numerical checks were independently recomputed by closing simple roots under simple reflections for the displayed Cartan matrices. D₄ has 24 roots and dimension28; E₆ has 72 roots and dimension78. Thus the potential h=4 and h=3 cases cannot embed into SL₄ of dimension15 or SL₃ of dimension8. E₇ and E₈ centre determinants were also checked. This computation checks the numerical eliminations; it does not independently classify all root systems.

For the Jordan route, a two-weight cocharacter gives End(V) degrees −1,0,1. Any stable Lie subalgebra inherits that grading, with [g_±1,g_±1]=0 because degree ±2 is absent. The triple products T±(x,y,z)=−[[x,y],z] define a Jordan pair by the Jacobi identity, as in Bertram–Neeb §3.1. A unit and the additional structure needed for a unital Jordan algebra are not automatic. Serre1979 separately distinguishes algebraic classification from realizing each case by a BT group.

## 7. Formal groups and the ramification estimate

**C-SA23-bt-047–055.** Tate's full faithfulness and Hodge–Tate comparison are background theorems whose exact hypotheses were read, not re-proved. A Lie-commuting endomorphism commutes with a sufficiently small exponential subgroup; such an open subgroup corresponds to a finite extension. This explains why the geometric End(F), defined by allowing finite extensions, occurs in the Lie commutant statement. With semisimplicity and scalar endomorphism algebra, scalar extension preserves the commutant; complete reducibility then gives absolute irreducibility. The positive coprime multiplicities permit Proposition5. The height-one formal-group case in Theorem5 is treated separately in the source; it is not forced into the positive-two-weight hypothesis.

Put q=p^h. The source has a_q a unit, a_n∈m for n<q and a₁=p. Let c₁ be the positive minimum lower bound on v(a_n), n<q, with v(p)=1. Then v([p]x)≥φ(v(x)), φ(t)=min(qt,t+c₁). The inverse is ψ(t)=max(t/q,t−c₁). For 0<t<c₁/(q−1), the q-th term has uniquely least valuation, so equality v([p]x)=qv(x) holds. At the boundary cancellation can occur: for formal G_m at p=2, [2](x)=2x+x² and x=−2 gives zero although the boundary valuation is1.

For primitive p^n-torsion, d_n=sup v(x) satisfies d_n≤ψ(d_(n−1)). For positive t, ψ(t)<t. Iteration tends to a nonnegative fixed point; the only one is zero. Eventually d_n is strictly below the threshold, giving geometric decay with ratio1/q. Surjectivity of [p] from primitive p^(n+1)-torsion to primitive p^n-torsion gives the asserted equality of suprema in that range; a weaker upper bound already suffices. Hence v(x)≤c₃/q^n. The value group of K(x) gives v(x)≥c₄/e, where c₄ is the value of a uniformizer of K, and therefore e≥(c₄/c₃)q^n.

To deduce Proposition8, choose primitive z∈T. Its orbit U under compact G is compact, hence closed. The inverse images in T of its reductions U_n are decreasing clopen neighbourhoods with intersection U. Since |U_n|≥c p^(nh), their normalized Haar measures are at least c, and continuity from above gives μ(U)≥c. An analytic submanifold of lower dimension has measure zero, so the orbit has full dimension, is locally open and has tangent space g·z=V. This checks the source's measure argument and completes the temporarily postponed lemma.

The general centralizer result following Theorem5 is still an omitted proof on these pages; Sen's later theorem is not confused with the preceding completed scalar case. The inertia openness proof uses base change to the completed maximal unramified field and preservation of geometric endomorphisms. Asking for a direct proof is a methodological request, not an admission that openness is unproved. Sen's filtration theorem is matched exactly to bounded shifts of upper ramification and a Lie filtration, with e=v_K(p) and a totally ramified mixed-characteristic setting in Fontaine–Ouyang A.4.1/A.85.

## 8. Fibre functors, crystals and the category being extended

**C-SA23-bt-062–074.** Generic-fibre full faithfulness is matched to de Jong's exact normal-Noetherian integral-domain theorem in his ICM text. The one-page erratum was read: it corrects a semistable-reduction lemma and definition and explicitly says no other changes are needed. It does not retract the Hom theorem.

The Serre–Tate deformation theorem in Katz Theorem1.2.1 concerns p-nilpotent R, nilpotent I and triples consisting of an abelian scheme over R/I, a p-divisible group over R and a compatible identification on R/I. The theorem is an equivalence of categories. It is not a mere bijection of unrigidified isomorphism classes. Ordinary canonical lifting is the identity point of the formal-torus parameter space in Katz Theorem2.1; passing through compatible Artin quotients gives the Witt-vector lift.

The handwritten category M^BT is literally generated by **all** Hodge–Tate objects of weights0,1. The Tate-curve representation with v(q)>0 belongs to that larger category but is not crystalline, as checked in Gunton's explicit example. Liu's all-prime theorem identifies lattices arising from BT groups with crystalline two-weight representations under its finite totally ramified hypotheses. Therefore a period-functor answer on the actual BT-generated category does not answer the literal all-two-weight category without changing the question. Failure of crystallinity does not by itself prove that every abstract tensor extension with fewer conditions is impossible.

For a regular period algebra B, Fontaine–Ouyang Theorem2.13 proves that the B-admissible category is closed under subquotients, tensor products and duals and that D_B is an exact faithful tensor functor. Their §6.5 TheoremA supplies the semistable filtered-(φ,N) correspondence; N=0 is the crystalline subcase. These are the precise standard results supporting the restricted extension construction. They do not decide arbitrary uniqueness without fixed comparison maps and admissibility.

A tensor grading determines a cocharacter by t↦⊕t^i on every representation, and a cocharacter determines the grading. Ziegler Theorem3.6 states this equivalence. π-invariance alone is not a uniqueness condition: G_m already has distinct invariant integer-power cocharacters. For Hodge–Tate descent, an eigenspace with character χ^i must be tensored with the cancelling character. Whether the named Tate line is the line or its dual determines the printed sign; Pro and Codex differ, so both readings remain.

Ziegler's Theorems4.13–4.16 distinguish fpqc local splittability, the torsor of splittings, and global splittability under pro-smooth/affine hypotheses. Characteristic zero supplies the appropriate smoothness in the standard setting. Theorem4.39 identifies the reductive parabolic/unipotent case. A trivial splitting torsor still has no specified canonical section. If a section of R is chosen, P=R×^UQ is identified with Q, hence their automorphism **inner forms** are identified; this does not canonically trivialize Q or identify its inner form with the original G.

The page's L⊂K makes T_cr⊗_K L ill-typed if T_cr is the intended L-vector space. The natural comparison would tensor from L to K, but that remains a proposed reading. Frobenius, descent, the coefficient object S, and the embedding π⊂Γ are not specified enough to decide the full Γ problem. No missing normality or admissibility is supplied silently.

## 9. Relative nonabelian cocycles

**C-SA23-bt-075–081.** Fix a splitting α of 1→A→E→Γ→1 and let γ act on A by conjugation through α(γ). Writing another splitting as β(γ)=z(γ)α(γ), the homomorphism condition becomes z(γδ)=z(γ)γ(z(δ)). Conjugation by a∈A changes z to a z(γ)γ(a)⁻¹. This is a parametrization conditional on existence, not an existence proof.

If the restriction class to π is neutral, some conjugation normalizes z|π=1. Two normalized representatives are related by a conjugator preserving normalization precisely when a∈A^π. Hence the neutral fibre of restriction is normalized cocycles modulo A^π, without any normality assumption on π.

For normal π, compare z(πγ)=π(z(γ)) and z(γπ′)=z(γ). This forces the values into A^π and yields a cocycle on Γ/π. Without normality this quotient reduction is not available. The page names a kernel π̃ elsewhere; that does not identify the separately written π with it.

Trivial neutral fibre does not imply full injectivity. A complete finite counterexample is computed. Give A=A₅ the trivial Γ=A₅ action and take π generated by h=(12)(34). H¹ is homomorphisms modulo conjugation. Every nontrivial normal subgroup of A₅ is all of A₅; the code certifies this by enumerating the normal closure of every nonidentity element. Therefore a homomorphism killing h is trivial, so the neutral restriction fibre is trivial. Identity and conjugation by the odd permutation (12) have identical restrictions to π. The code checks all60 inner conjugators and finds none equating these maps, so the restriction is not injective. The general explanation is twisting of nonneutral fibres, as in Milne §23.52.

For a chosen full splitting, the stabilizer under A^π is A^Γ. Thus a single orbit is the homogeneous space A^π/A^Γ, not necessarily a torsor. This checks the local replacement of “torseur” by “esp. homogène”; it does not decide whether the whole paragraph was later cancelled, since the two transcriptions disagree about that.

The rank-one reconstruction fixes Γ=G_K×Z acting on Ω× through G_K, with K=Q_p. A normalized cocycle has multiplier b=z(1) fixed by G_K, hence b∈Q_p×. Fixed scalar conjugation is trivial, so b=1 and b=p remain distinct. In a semilinear version with valuation-preserving σ on a discretely valued F, every coboundary σ(a)/a has valuation0; a uniformizer has valuation1 and represents a nontrivial class in H¹(Z,F×). Both tests refute bare uniqueness in their stated models. They do not settle an unspecified admissible-period construction.

## 10. Restriction of scalars, valuation and models

**C-SA23-bt-082–084.** By definition, (Res_(K/Q_p)G_m)(R)=(K⊗_(Q_p)R)×. For a quadratic separable Galois extension, the algebra K⊗K splits into two K factors, using the two embeddings. Thus the points at Q_p and at K are different groups. This is a base-argument check, not a decision about an ambiguous handwritten subscript.

For a DVR, x=uϖ^n with n=v(x) and u∈V×. The map x↦(xϖ^(−v(x)),v(x)) has inverse (u,n)↦uϖ^n; changing ϖ changes the splitting. Jordan–Ribet–Scholl §1.1 explicitly gives the Néron lft model of G_m, its generic fibre G_m, special fibre G_m×Z and valuation on V-points. A generic-fibre product G_m,K×Z_K is disconnected and cannot be the same generic fibre. The source's Ñ diagram is therefore retained as unidentified until its base labels and model notation can be checked on scans.

## 11. Conditional arithmetic bridge

**C-SA23-bt-085.** Katz Theorem10.0 concerns a smooth proper family over a smooth connected arithmetic base with the stipulated locally free cohomology. Its global nilpotence conclusion is about nilpotent p-curvature at almost all relevant primes. The analytic leaves supply no arithmetic model or specified family, and nilpotent is not the same as zero. No absent elliptic-curve calculation or prior-run matrix is treated as checked here.
