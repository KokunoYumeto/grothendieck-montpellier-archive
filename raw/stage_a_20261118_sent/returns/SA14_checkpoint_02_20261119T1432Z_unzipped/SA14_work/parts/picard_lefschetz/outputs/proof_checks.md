# Independent mathematical checks: Picard and Lefschetz packets

All manuscript line numbers below refer to the exact supplied `.tex` file, not to reconstructed manuscript lines. These arguments are reconstructions in this run. They do not settle any doubtful ink. Numerical outputs are in `calculations.json`; their generating code is `scripts/calculations.py`. A finite test is distinguished below from a proof.

## P1. Connectedness under specialization: the missing geometric hypothesis

Source: `MPL_58_020-067_transcription.tex`, scan23, lines114–151; itemSA14-274.

Put A=Z_(5) and B=A[T]/(T²+1). The polynomial is irreducible over Q, so B is a domain and X=P¹_B is integral. The map SpecB→SpecA is finite, hence X→SpecA is proper. The unique irreducible component of X dominates SpecA. A is a regular discrete valuation ring, and therefore normal and geometrically unibranch. The generic fibre is P¹ over Q(i), regarded as a Q-scheme. It is connected and its unique component has dimension1. Thus with h=0 the written connectedness and dimension≥h+1 hypotheses hold.

Over F₅ the polynomial has the distinct roots2 and−2. The Chinese remainder theorem gives B/5B=F₅×F₅. Consequently X₀ is the disjoint union of two copies of P¹_F₅ and is not connected. The same counterexample works for every h≥0 by taking X=P^{h+1}_B: an irreducible generic fibre of dimension h+1 stays connected after deleting any closed subset of dimension<h, while its special fibre still splits into two components. Thus the failure does not depend on admitting h=0. The symbolic calculation certifies the irreducibility and factorization used here. The generic fibre is not geometrically connected; that is exactly the missing hypothesis the example detects. This refutes the literal statement, not every possible repaired geometric connectedness theorem.

## P2. H¹/H² vanishing does not give categorical faithfulness

Source:58:41, lines841–883; itemSA14-292.

Let X=Spec k[[t]], Y=V(t)=Spec k. This is a noetherian scheme and an effective Cartier divisor, and X is its own t-adic formal completion. All H¹(Y,O_Y) and H²(Y,O_Y), and all such groups for the powers of the conormal line, vanish because Y is affine. On the invertible sheaf O_X, multiplication by1 and multiplication by1+t are distinct automorphisms. Both restrict to the identity on O_Y. Thus restriction of the category of invertible sheaves is not faithful, hence is neither fully faithful nor an equivalence.

The formula `(1+t)^{-1}=1−t+t²−…` proves invertibility; the saved calculation checks every displayed truncation modulo tᴺ for N=2,…,6. Both Picard groups of isomorphism classes are zero, so the example does not contradict the group-level Picard assertion. The missing control is in H⁰ of the successive additive layers of the unit group.

## P3. Positive graded finite generation versus negative twists and formal support

Source:58:58, lines1460–1528; itemsSA14-313 and315.

Take X=Pʳ_k with r≥1, Y=(x₀=0), p=[1:0:…:0], U=X and F=k(p). Every twist F(m) is isomorphic to F as a sheaf on its one-point support, so H⁰(X,F(m))=k for all integers m. The positive graded section module is S/(x₁,…,xᵣ)=k[x₀], a cyclic module over S=k[x₀,…,xᵣ]. Hence finite generation in nonnegative degrees does not imply negative-twist vanishing. No Serre vanishing theorem is contradicted: the error is the alleged equivalence between these different assertions.

Multiplication by x₀ is invertible on F, so F is t-regular. If the surrounding convention insists that F/tF be nonzero, replace F by O_X⊕k(p); its positive section module is still finitely generated and its negative H⁰ has the same nonzero skyscraper summand. Because the support of k(p) is disjoint from Y, its completion along Y is zero. Thus H⁰(F)→H⁰(F̂) is k→0. For U=X, the missing boundary Z=X−U is empty, so a condition applying only near Z is vacuous and cannot imply that comparison. This gives a precise test of the star’s possible scope.

## P4. Exactness forces the direction of α

Source:58:56, lines1355–1370; itemSA14-311.

In the localization exact sequence

H^{i−1}(X,F) → H^{i−1}(U,F) → H_Z^i(X,F) →ᵅ H^i(X,F),

the cokernel of the first map is identified with kerα. Therefore the first map is surjective if and only if α is injective. Surjectivity of α controls the next cokernel and has no such implication. This is a proof by exactness, not a statistical check or an ink decision. The calculation file records the same algebraic relation.

## P5. Hom-depth inequality

Source:58:46, lines1046–1066; itemsSA14-304 and341.

Let R be a noetherian local ring and F,G finite R-modules. A finite presentation Rᵇ→Rᵃ→F→0 gives

0→Hom_R(F,G)→Gᵃ→Gᵇ.

If depthG≥1, any G-regular element is regular on the submodule Hom(F,G), so the latter has depth≥1. If depthG≥2, write I for the image in Gᵇ. Since I is a submodule of Gᵇ, depthI≥1 when I≠0; if I=0 the desired result is immediate. The depth lemma applied to 0→Hom(F,G)→Gᵃ→I→0 gives depthHom(F,G)≥2. Thus

depthHom_R(F,G)≥min(2,depthG).

No depth assumption on F is used. This explains why the target alone can carry the depth bound in a Hom comparison, without implying that all other global hypotheses may be removed.

## P6. Precise local Hom comparison via Raynaud

Source:58:46, lines992–1066; itemSA14-341. Published input: Michèle Raynaud1974, I.0, I.1.1 and I.1.3; local depth localization: Stacks tag0FCC. Both primary endpoints were opened.

Let (A,m) be a noetherian local quotient of a regular ring, complete for the t-adic topology, with t∈m. Set P=SpecA−{m} and D=V(t)∩P. Let G be coherent on P, with depthG_q≥2 at each point q closed in P and outside D. For every coherent F on P we claim

Hom_P(F,G) ≅ Hom_{P̂}(F̂,Ĝ).

We check the n=2 hypotheses in Raynaud’s comparison theorem instead of treating the reference as a black box with different quantifiers. Write U=P−D. A point u of U whose closure in P misses D must have dim(A/p_u)=1, hence be closed in P. Indeed if dim(A/p_u)≥2, quotienting the local domain A/p_u by the nonzero nonunit t leaves a positive-dimensional closed subset, so its puncture meets D. At these closed points the required depth≥2 is exactly the hypothesis.

For u whose closure meets D, Raynaud requires depthG_u≥2−dim(closure_P{u}). If the closure dimension is at least2, the bound is automatic. The only nontrivial case is closure dimension1, equivalently dim(A/p_u)=2. In the two-dimensional local domain A/p_u choose a height-one prime avoiding t. Such a prime exists by choosing an element of the maximal ideal outside the finitely many height-one primes containing t and taking a height-one prime over it. The lifted prime q specializes u, is closed in P, and lies outside D. Since A is a quotient of a regular ring, the dimension calculation is catenary; dim((A_q)/p_uA_q)=1. The localization depth inequality gives depthG_u≥depthG_q−1≥1, as required.

Apply this same check to M=Hom(F,G), using P5 at the closed off-D points. Raynaud’s I.1.3 with n=2 gives the H⁰ isomorphism. On noetherian affine charts, completion is flat and F is finitely presented; hence completion commutes with Hom(F,G). The formal H⁰ is exactly the right side displayed above. This proves the precise target-only statement. It does not prove the entire quotient-category or essential-image assertions around it, and it does not dispense with t-adic completeness or the regular-ambient hypothesis.

## P7. Unrestricted quotient-category fullness fails

Source:58:46; itemSA14-309. This counterexample is an earlier-run proposal independently checked here.

Take A=k[[x,y,z]], t=x, P=SpecA−{(x,y,z)}, and F=G=O_{V(y)∩P}. On its support write B=k[[x,z]]. The formal completion along x has endomorphism ring k((z))[[x]]: after x-adic reduction the point z=0 is the deleted origin, so z is inverted. In the quotient by coherent sheaves supported on closed subsets disjoint from D, the germ endomorphism ring at the remaining prime(x) is B_(x). This can be seen by shrinking away from finitely many other height-one primes and taking the filtered union of the corresponding section rings.

The series f=Σ_{n≥0}z^{-n²}xⁿ belongs to k((z))[[x]]. Suppose f=h/g with h,g∈B and g∉(x). Write g=Σg_i(z)xⁱ and let e=ord_z(g₀)<∞. Comparing coefficients in gf=h shows inductively that the pole order of f_n is at most(n+1)e: the recurrence divides once by g₀ and every g_i,h_i has nonnegative z-order. The actual pole order is n², contradicting this bound for large n. Therefore f∉B_(x), so the quotient functor is not full.

At the closed off-D point of the support corresponding to(z), G has depth1, not2. Consequently this example does not refute P6. The numerical pole-order table illustrates the growth; the recurrence argument proves the exclusion.

## P8. Split criteria for divisible p-primary groups

Source57:292, lines407–423; itemSA14-230.

The source’s second paragraph explicitly restricts M,N to finite direct sums of Q_p/Z_p. Their contravariant duals are finite free Z_p-modules. This restriction matters: the same assertions cannot be transferred indiscriminately to groups with a finite summand.

For a map u:M→N, write the dual map between free Z_p-modules in Smith normal form. It is a split injection precisely when it has full source rank and every nonzero invariant factor is a p-adic unit. The same condition is equivalent to injectivity modulo p, and to surjectivity of the transpose dual lattice map T^p(M)→T^p(N). Dualizing back gives a split quotient of divisible groups; reduction on the p-torsion is the corresponding surjectivity over F_p.

If H is a fixed nonzero finite p-group, tensoring a nonunit diagonal factor pᵃ with H produces a nontrivial kernel: H has elements killed byp. A zero diagonal factor also produces a kernel. Thus tensor-injectivity for any one nonzero H detects exactly the same condition. If H=0, every tensor map is injective, including the zero map on nonzero lattices. The saved finite cyclic calculations exhibit this failure. The correction is therefore “H nonzero” or “for every finite p-groupH,” with the original finite-corank divisible restriction retained.

## P9. Finite-cotype p-groups and rationalization

Source57:291–292, lines370–423; itemsSA14-228–229.

For a p-primary torsion group with finite M[p], its injective envelope is a finite sum of Prüfer groups: the number of summands is bounded by dim_FpM[p]. Pontryagin/character duality with Q_p/Z_p identifies subgroups of that envelope with quotients of a finite free Z_p-module, hence with finite generated Z_p-modules. The structure theorem over the discrete valuation ring Z_p gives M≅F⊕(Q_p/Z_p)^ρ. The largest divisible subgroup and the finite quotient determine the two invariants; a splitting need not be canonical.

The written T_p(M)=Hom(M,Q_p/Z_p) is contravariant, includes the finite dual ofF, and is finite generated. The inverse-limit T^p is covariant, killsF, and is Hom_Zp(T_p(M),Z_p). Multiplication byp on Q_p/Z_p has finite kernel and is therefore an isomorphism after quotienting by finite groups, but its map on the integral Tate lattice is multiplication byp and is not invertible. Tensoring with Q_p is necessary to obtain the isogeny-category equivalence with finite-dimensional Q_p-spaces. These statements are pure group theory and do not identify full finite group schemes from their geometric points.

## P10. The conditional p-divisibility specialization mechanism

Source57:289–290, lines322–368; itemSA14-223.

Let X be an abelian scheme over a trait, F,G finite flat subgroup schemes, and let q_F:X→A=X/F, q_G:X→B=X/G. If [p](F)⊂G, the homomorphism[p] followed byq_G descends to u:A→B with u q_F=[p]q_G. If u=[p]v, then ([p](v q_F−q_G))=0. A homomorphism from an abelian scheme’s connected fibres to a finite group scheme is zero, so v q_F=q_G; in particular F⊂G. Conversely F⊂G gives a descended v and u=[p]v. Thus the criterion is exactly containment ofF inG, once the displayed descent condition holds.

If F_generic is not contained inG_generic but F_special⊂G_special, this proves the desired jump of p-divisibility. The literal equality pF=G is incompatible with the stated nonzero order-p groups because pF=0. The repair pF⊂G is sufficient for descent, but is not adopted as a reading. The next page’s generic inclusion also conflicts with the intended nondivisibility. Maulik–Poonen2012, Example3.12 is a verified separate construction of p-torsion in a specialization cokernel, using CM orders. It does not verify the manuscript’s elliptic subgroup realization.

For C=A×B^∨, the correspondence summand in NS(C) is Hom(A,B). Writing C=A×B instead changes the Hom target to B^∨. The duality alarm is therefore independent of the subgroup-containment alarm.

## P11. Igusa inversion control and scheme structure

Source57:285,287; itemsSA14-221,222,247.

Assume the quotient construction has the stated free translation action by a constant group of order2 on B, and inversion on the abelian scheme A. The displayed fixed subgroup on A^∨ is ker([−1]−[1])=A^∨[2]. Multiplication by2 on an abelian scheme of relative dimensiona is finite flat of rank2^{2a}; its kernel remains finite flat in characteristic2. It is étale when2 is invertible. In characteristic2 its tangent space has dimensiona because the derivative of[2] is zero, so it is non-smooth for a>0.

Thus the formula Pic^τ(X)=Y^∨×A^∨[2] describes a flat object with non-smooth fibres, not nonflatness. In characteristic2 both inversion tangent representations in the page’s Hodge-difference formula become the identity. Consequently this basic control gives h^{0,1}=h^{1,0}=a+b, whereas away from2 the two fixed tangent contributions vanish and both areb. This does not prove the four distinct pathologies announced on288. The calculation file records exact ranks and dimensions for illustrative values; the derivative and finite-flat-kernel arguments give the general calculation.

The source’s map Γ_S→B cannot literally be an isomorphism when dimB>0; a finite subgroup embedding supplies the intended translation action. Its ink remains undecided.

## P12. Gluing along an inverted punctured axis

Source57:298,300, lines541–592 and608–623; itemSA14-236.

On A²−{0}, global functions are k[x,y]. Glue the two punctured x-axes by x=t on one side and x=t^{-1} on the other. A pair of global functions(f₁,f₂) on the pushout must satisfy f₁(t,0)=f₂(t^{-1},0) in k[t,t^{-1}]. The intersection k[t]∩k[t^{-1}] is k, so every global function is constant on the image of the glued G_m. There are nevertheless many nonconstant global functions away from that curve, for instance compatible functions vanishing on the axes. The claim is constancy along the curve, not Γ(X,O)=k.

A quasi-affine scheme embeds into an affine scheme, and restrictions of the latter’s global functions separate its distinct rational points. Over an algebraic closure the glued G_m has distinct points that every global function identifies, a contradiction. Equivalently the canonical map to SpecΓ fails to be an immersion along this curve. The finite-degree linear systems in the code illustrate the Laurent intersection; the ring intersection argument proves it in all degrees.

The involution quotient proposed later requires an affine neighborhood for every finite orbit (or an algebraic-space formulation); this extra existence condition is not a consequence of the function calculation and remains a separate source gap.

## P13. Two projective spaces with Picard-trivial pushout

Source57:302, lines649–654; itemSA14-238. Published structural match: Ferrand2003, §6.3 and Theorem5.4.

Let E be a complex elliptic curve and choose degree3 line bundles L₁,L₂ whose difference L₂⊗L₁^{-1} has infinite order in Pic⁰(E). Degree3 line bundles embed E in P². If L₁^a⊗L₂^b is trivial, degree gives a+b=0, and the infinite-order difference then gives b=0, hencea=0. The restrictions are Z-linearly independent as required by the source.

The finite pinching construction yields the scheme X=P² amalgamated with P² along these two copies ofE. The units/Picard exact sequence contains

k*×k* → k* → Pic(X) → Z² → Pic(E).

The first map is the ratio and is surjective. The last map has zero kernel by the preceding independence. Therefore Pic(X)=0. SinceX is positive-dimensional and proper, it cannot be projective: a projective scheme has a nontrivial ample line bundle, and a trivial line bundle cannot be ample on a positive-dimensional proper scheme. Its normalization is the disjoint union of the two projective planes, which is projective. The finite-generation/existence input and unit term are essential to this completion of the manuscript’s short argument.

## P14. Pinching units and a nodal control

Source57:304, lines679–722; itemsSA14-239,248.

For a pushout along a finite closed conductor square, a line bundle is described by bundles on the two pieces with an identification on the common closed subscheme; changing trivializations acts through units. This gives the familiar exact units-to-Pic sequence. The relative kernel in the source must be a quotient of units; dropping that term would lose the generalized-Jacobian contribution.

For P¹ with two distinct rational points identified, the two-point units group is G_m² and the constant units from the normalization and node map to the diagonal G_m. Their quotient is G_m. Hence the degree-zero Picard kernel is a one-dimensional torus. This is an independent explicit specialization of the page’s setup, not a new construction claimed to be written there.

## P15. Normalization genus and graph rank

Source58:66, lines1885–1966; itemSA14-330.

For a reduced connected proper curve C over an algebraically closed field and finite normalization ν:⨿C_i→C, the exact sequence

0→O_C→ν_*O_{⨿C_i}→Q→0

has Q of finite length Σδ_s. Euler characteristics give

1−p_a(C)=Σ_i(1−g_i)−Σ_sδ_s,

hence p_a(C)=Σg_i+Σδ_s−number_of_components+1. For a nodal curve, each node hasδ=1, so the extra term is the first Betti number of the connected dual graph. The multiplicative normalization sequence similarly gives torus rank equal to that graph rank. The incidence matrices in the code verify the illustrative tree, triangle, double edge and self-loop calculations, while the exact sequence proves the general formula.

A branch count alone is insufficient for a cusp or a worse singularity; δ, not the number of branches, is the needed invariant. The displayed model k[x,y,z]/(xy) is two-dimensional, so it cannot be substituted into a curve-genus formula without an additional cut or interpretation.

## P16. Factorial versus categorical parafactorial

Source58:66, lines1858–1884; itemSA14-329. Published endpoint: SGA2 XI3.4–3.5.

A noetherian local ring A is categorically parafactorial only when line bundles and their isomorphisms are recovered from the punctured spectrum. For a DVR A with fraction field K, both Pic groups are zero, but automorphisms of the trivial bundle are A* and K*. A uniformizer lies in K* but not A*, so restriction is not full. The usual criterion separates the two duties: depthA≥2 for H⁰/automorphisms and Pic(puncture)=0 for isomorphism classes. The literal unrestricted implication from factoriality therefore fails in dimension1. This is another instance of the same group-versus-category distinction exposed in P2.

## P17. Seminormal graded contraction and line-bundle invariance

Source58:65,67; itemsSA14-326,334. Published input: Traverso1970, Theorem3.6 for reduced noetherian rings with finite normalization (in particular finite-type algebras over a field).

Let R=⊕_{d≥0}R_d be a reduced seminormal finite-type k-algebra with R₀=k. The grading defines h:R→R[t], a_d↦a_d t^d. Evaluation att=1 gives id_R; evaluation att=0 factors through k. Polynomial Picard invariance says pullback along R→R[t] is an isomorphism, so the two evaluation maps induce the same inverse on Pic. Applied to h^*, this identifies every class with the pullback of its value in Pic(k)=0. Thus Pic(R)=0. This is a proof under an added sufficient hypothesis, not verification of an undefined box on65.

For a line bundle E→X with X reduced seminormal of finite type, choose a Zariski affine cover trivializingE. On every affine intersection the Picard groups of the base and its polynomial extension agree; because the rings are reduced, units in a polynomial ring are constant units. A line bundle onE therefore descends locally fromX and its transition isomorphisms descend uniquely. Descent glues these to a line bundle onX. Pullback is also split injective by the zero section. Hence Pic(X)≈Pic(E) under these hypotheses. The same argument does not establish necessity of seminormality for one particular bundle, and an affine cusp alone is not a counterexample to the exact projective-cone setup.

## P18. Projective-cone Picard calculation: conditional model

Source58:67, lines1967–2023; itemSA14-333.

Assume the projective cone is formed from the full section ring of an ample line bundle on a connected proper k-scheme X with Γ(X,O_X)=k, and assume the stated cone contraction f:X′→Ĉ satisfies f_*O_{X′}=O_Ĉ. Its projective-bundle model gives Pic(X′)=Pic(X)⊕Z. Restricting to the exceptional section identifies the Pic(X) summand, so classes pulled back fromĈ lie in the complementary Z generated by the tautological cone hyperplane class. Since O_Ĉ(1) pulls back to that generator, every such integer occurs. Finally f_*O=O and the projection formula make f^*:Pic(Ĉ)→Pic(X′) injective. Thus Pic(Ĉ)=Z.

This proves the conditional model spelled out by the manuscript, without treating SpecS[z] as ProjS[z]. Exact EGAII8.7.5/8.8.6 content must be checked separately from the bibliography. A failure of the full-section-ring or connectedness hypotheses can change the contraction calculation.

## P19. Diangle and determinant identities

Source57:295 and58:51,53; itemsSA14-241,322.

In the commutative algebra generated by S with S²=δI,

(ξI+ηS)(ξ′I+η′S)=(ξξ′+δηη′)I+(ξη′+ηξ′)S.

Dividing the two coefficients gives the written τ addition law where denominators are invertible. The norm ξ²−δη² is multiplicative. Squaring gives (ξ²+δη²)I+2ξηS; the off-diagonal/order-two condition must therefore account for characteristic2 and invertibility. The code proves these polynomial identities symbolically, rather than checking random numbers.

The Jacobi identity uses signed complementary minors. The symbolic3×3 residual is zero over the integer polynomial ring. In general it follows on the open set detX≠0 by applying the2×2 minor formula to detX·X^{-1}; polynomial identity then extends it to every square matrix over a commutative ring. The source’s conventions for the sign in X^{ij,hk} are required. Rank equals the largest nonzero minor over a field by the wedge criterion; the numerical matrices are illustrations, while the basis/wedge argument supplies the general proof.

## P20. Two low-degree Lefschetz arguments

Source58:34–39; itemsSA14-283–290.

For n=0, an H¹ class in a vector bundleF is an extension0→F→E→O→0. If its formal restriction vanishes, the formal extension splits. Weak LG applied toHom(O,E)=E lifts the formal splitting section; weak LG onO makes its composite with E→O equal to1 algebraically. Hence the extension splits. This proves the injective H¹ endpoint from H⁰ comparison for vector bundles. For higher n, injective resolutions are not resolutions inside the vector-bundle exact category; an additional argument is required.

If every vector bundle admits0→F→P→F′→0 with P a finite sum of chosen generators and F′ locally free, the two long exact cohomology sequences give the advertised induction. One must retain comparison in the adjacent degree and the embedding hypothesis. On a quasi-projective scheme an ample family supplies the intended twists; on an arbitrary scheme it may not.

Once formal comparison is fully faithful for vector bundles, multiplication and unit on a finite locally free algebra are morphisms of vector bundles. Their identities are equalities between maps out of tensor powers, so faithfulness tests them. Effective algebraization supplies the underlying bundle on a neighborhood, and openness of the étale locus permits shrinking to make the algebra étale. This proves the finite-étale neighborhood statement. Replacing a neighborhood by all ofX is a different purity assertion.

## P21. Proper support and a cohomological permanence route

Source58:42–44; itemsSA14-294–301.

For a projective morphism f:X′→X with X noetherian quasi-projective and F′ coherent, flat overX and with support proper overX, the finite-presentation/flat proper cohomology theorem supplies a perfect complex representing Rf_*F′ locally; a bounded locally free model can be used under the needed global resolution hypothesis. Base comparison for each vector-bundle term propagates to the resulting hypercohomology in the allowed degree range, provided derived base change and formal limits are compatible. This explains the modern route for the cohomological part, and identifies each required input.

This paragraph is a checked conditional proof reduction, not a complete proof of the manuscript’s effectivity statement. Algebraizing a formal coherent sheaf, an algebra structure or a polarized projective scheme is an additional step. Properness also makes the nonflat or nonfree locus removable after shrinking: its image is closed in the base and, if it missesY, its complement is a neighborhood ofY. Without proper support the image need not be closed. The exact broad permanence/effectivity theorem was searched, but no source matching every written quantifier was identified in the searches recorded here.

## P22. Rigidification, product Picard functors, and the missing component

Source57:283–286 and309; claimsC-SA14-210–212,249. This is a functor calculation under the explicitly added representability and universal O-pushforward hypotheses, not a claim that an arbitrary Picard presheaf already has a universal bundle.

Let g:X→Y have a section s, and suppose g_*O_X=O_Y universally. Pullback g^*:Pic(Y)→Pic(X) has left inverse s^*. For every bundle L, the bundle L⊗g^*(s^*L)^{-1} is rigidified along s, and L is recovered by tensoring this factor with g^*s^*L. The same construction after every base change, with descent for line bundles, proves the splitting of the relative fppf Picard sheaves. Universal O-pushforward ensures that an automorphism of a bundle trivial on the section is the identity, which is the point needed to rigidify descent data rather than merely split groups of geometric points.

For pointed proper factors (Y,y),(Z,z), a bundle L on Y×Z is first divided by its restrictions from Y×{z} and {y}×Z, with the common base factor corrected once. The residual bundle is trivial along both pointed axes. Regarded as a family on Z parametrized by Y, it defines a pointed map Y→Pic_{Z/S}; conversely the rigidified universal family pulls back along such a map. These operations are inverse and commute with base change. If only a sheafified universal class exists, the argument is made fppf locally and the rigidifications glue it. The construction proves precisely the asserted relative formula when these assumptions hold.

For smooth proper geometrically connected varieties over an algebraically closed field, the pointed-map contribution factors through the Albanese variety into the Picard variety. A homomorphism between abelian varieties killed by n has image in a finite group scheme, and a map from a proper geometrically connected reduced variety to that finite affine scheme is constant. Thus this Hom group is torsion-free. It follows that the torsion component of the product has no additional correspondence contribution. This checks the geometric smooth-proper case; a broader relative formula must retain the representing, base-change and rigidity assumptions rather than being inferred from this pointwise argument alone.

Finally set Γ=1 and take B to be a point in the full-Pic interpretation of57:284. It would identify Pic(A) with A^∨=Pic⁰(A). An ample line bundle on a positive-dimensional abelian variety has positive top self-intersection, whereas an algebraically trivial line bundle is numerically trivial. Hence it is not in Pic⁰. This refutes the transient A-dual substitution in line208. The manuscript itself restores NS and the torsion-component restriction in lines212–219 and retains full Pic in the later formula at258–279. The counterexample does not refute those corrected statements or the later hypotheses involving Γ-coinvariants.

**P22-cosets (C-SA14-206–207).** For a quotient homomorphism q:G→Q with kernel H, q⁻¹(a) can lie in H only if a is the identity: every point of H maps to the identity. A nonidentity quotient class therefore refutes the literal ambient-kernel sentence; the corrected ambient is G. For a represented fppf quotient, the inverse image of its diagonal under G×G→Q×Q is the relation g₁g₂⁻¹∈H. Thus closedness of H gives closedness of the relation, and closedness descends along the faithfully flat covering to the diagonal. This checks separatedness once the quotient exists; it does not construct the quotient or prove its unramifiedness.

## P23. Square-zero lifting and the obstruction degree

Source57:294,297. Let X₀⊂X be a square-zero thickening with ideal I. Multiplication identifies 1+I with the additive sheaf I, giving 1→1+I→O_X^*→O_{X₀}^*→1 on a topology where the unit map is locally surjective. Lift transition functions g_ij of a line bundle on X₀. On triple overlaps their products differ from1 by elements a_ijk of I. Associativity makes (a_ijk) a Čech2-cocycle; changing the lifts changes it by a coboundary. Its class in H²(X₀,I) vanishes exactly when the transition functions can be corrected to glue. When it vanishes, isomorphism classes of lifts form a torsor under H¹(X₀,I), modulo the preceding unit boundary when no rigidification is fixed. Automorphisms of a fixed lift reducing to the identity are H⁰(X₀,I).

If X₀ is smooth over k and X is a first-order deformation, the deformation is represented by a Čech1-cocycle of derivations in T_{X₀}. Contracting that cocycle with dlog(g_ij), the Čech representative of c₁(L) in H¹(Ω¹), gives the obstruction class in H²(O). The sign depends on the chosen Čech convention; the cohomological degree does not. This explains why a doubtful H¹/H² source index is substantive. FGA236 §2.6 is the opened published match for the obstruction and lifting groups.

Lifting every geometric point of a Picard component, lifting a finite subgroup scheme, constructing a p-divisible group, and flatness over the base are different assertions. The calculation above concerns individual bundles and their automorphisms. It supplies none of the missing coherence or compatibility data for a subgroup or a p-divisible system. Oda’s absolute perfect-field results do not automatically bridge this gap.

## P24. The two derived-limit spectral sequences

Source57:296. Work in modules over a ring and use a small filtered direct index category for A_i. Resolve the colimit by the standard simplicial replacement: in each degree its terms are direct sums indexed by chains of arrows of the A_i, and its augmented homology is the filtered colimit in degree0 and zero in positive degrees because filtered colimits of modules are exact. Apply Hom(-,J^•), where J^• is an injective resolution of B. The resulting first-quadrant double complex has one filtration computing Ext(colim A_i,B); the other has E₂^{p,q}=R^p lim_i Ext^q(A_i,B). This is the module version of the displayed spectral sequence. Smallness, filteredness, and the abelian category are real hypotheses, not decorations supplied by the torn preceding page.

For the second pair, let R be noetherian regular of finite global dimension and A a finite R-module. Choose a finite resolution P_• by finite projectives. Apply the Roos inverse-limit complex to the system Hom_R(P_•,M_i). Finite projectivity lets Hom(P_j,-) commute with the products used in that complex and preserves exactness. The two filtrations yield respectively R^p lim Ext^q(A,M_i) and Ext^p(A,R^q lim M_i), converging to the common total cohomology. Finite resolution length gives the needed boundedness. The inverse-system category may be arbitrary small here if its full Roos complex is used; that observation does not identify the undefined L_k or prove the separate vanishing bound in the detached text.

Laudal1965 supplies the opened derived-limit framework and backward references to Roos. The exact Roos original and the preceding definition on this physical sheet were not recovered. Accordingly the reconstructed spectral sequences are checked, but the printed induction’s precise bound remains unidentified.

## P25. The editorial field-theory tasks

Source57:299,301,303. The “lemme de Zariski” actually written at57:299 is a relative-constants statement, not the different lemma about a field finite type as an algebra. Let K⊂E and let T be a tuple algebraically independent over E. Write u=a(T)/b(T) with a,b coprime in E[T], normalizing one nonzero coefficient of b to1. If u is algebraic over K(T), its orbit under the K-automorphisms of a sufficiently large algebraically closed universal domain containing E (acting trivially on T) is finite, because every conjugate satisfies the same nonzero polynomial in K(T)[Z]. The normalized coprime pair (a,b) is uniquely determined by u. Thus each coefficient of a,b has finite orbit under that automorphism group. An element with a finite orbit in a universal algebraically closed field is algebraic over K: a transcendental element can be taken to infinitely many transcendental elements by extending isomorphisms of transcendence bases to algebraic closures. Hence all coefficients lie in K₀, the relative algebraic closure of K in E. Conversely any rational function with finitely many coefficients algebraic over K is algebraic over K(T), since it lies in E₀(T) for a finite algebraic extension E₀/K. Therefore the relative algebraic closure is exactly K₀(T). This completes the written Chevalley argument, including the normalization suppressed in its sketch. Searches under the name Zariski lemma mostly returned the unrelated finite-type-field theorem; that theorem is not used as an exact source match.

In characteristic0 every field extension is separable. If k is relatively algebraically closed in K, the extension is regular in the field-theoretic sense: separability plus absence of new algebraic constants is the geometric-integrality criterion. Thus K⊗_k k′ is a domain for every field extension k′; it need not be a field. For example k(t)⊗_k k(u) does not invert every nonzero polynomial involving both independent variables. The appropriate regular extension after base change is its fraction field. This distinguishes the source’s legitimate regularity task from an overstrong tensor-is-a-field reading.

For a finite exponent-one purely inseparable extension K/k in characteristic p, adjoining successively elements b_i not already generated by the preceding ones gives extensions of degree p until K is reached. The monomials b₁^{e₁}⋯b_r^{e_r}, 0≤e_i<p, form a k-basis, so [K:k]=p^r. The relations b_i^p∈k have zero differential; the usual polynomial presentation then gives Ω_{K/k}=⊕K db_i. Assigning arbitrary values to the b_i therefore defines a unique k-derivation. Stacks07P2 proves the p-basis/differential criterion in the general setting. The October1957 date remains attached to the reused Tribu editorial sheet, not to adjacent Picard handwriting.

## P26. A finite torsion scheme can have infinitely many sections

Source57:310. Let k be an infinite field of characteristic p, A/k a positive-dimensional abelian variety, and S=Spec k[ε]/(ε²). The kernel of A(S)→A(k) at the identity is canonically Lie(A)⊗_k εk. Multiplication by p has differential p·id=0, so every such first-order section lies in A[p](S). There are infinitely many because Lie(A) is a positive-dimensional k-vector space. Yet A[p] is a finite group scheme. Thus finite type, or even finite flatness of the torsion scheme, does not imply a finite set of S-valued sections. This example needs no supersingularity assumption and avoids conflating geometric points with infinitesimal sections. The section statement rejected in the margin is therefore independently refuted.

## P27. Reused scalar algebra and invertible ideals

Source57:312 and58:20,47,49. If V′ is a K′-form of a K-vector space V, the natural K-linear map K⊗_{K′}V′→V sends a⊗v to av. A K′-basis of V′ is a K-basis of V precisely when this map is an isomorphism. The asserted universal extension property is then the tensor-product universal property, so it is equivalent to the same criterion. No Galois descent datum is silently added.

For a bilinear form Φ on an A-module, the scalar-extended formula Φ′(a′⊗x,b′⊗y)=a′b′⊗Φ(x,y) respects both balancing relations because Φ is A-bilinear. It is bilinear over A′, and uniqueness follows because pure tensors generate. The cut-off Proposition3 on57:312 cannot be reconstructed merely from this complete formula.

Let A be a domain with fraction field K. A finite projective rank-one module P is torsion-free and embeds in P⊗K≅K after a choice of basis. Its finite set of generators has a common denominator, so its image is a fractional ideal I. Local freeness of rank1 makes I·I^{-1}=A, where I^{-1}={x∈K:xI⊂A}; this can be checked at each prime. Conversely an invertible fractional ideal is locally generated by one nonzero element and is finite projective rank1. The evaluation P⊗P^∨→A is the corresponding isomorphism. A different K-basis scales I by K^*, which is the exact ambiguity. Stacks0B8I and0BD6 supply the checked modern module formulation; the physical Bourbaki edition is not identified.

## P28. Associated points: the closure condition is essential

Source58:37, lines674–689. Assume X is noetherian quasi-projective with an ample line bundle L and weak Lefschetz comparison for all vector bundles. Suppose x∈Ass(O_X) and Z=closure{x} is disjoint from Y. The coherent submodule H_Z⁰(O_X) is nonzero: at x the associated element has support in Z. On a noetherian scheme this local-cohomology-in-degree-zero submodule is coherent, since the annihilators of powers of a coherent ideal defining Z stabilize. For sufficiently large m its twist by L^m is generated by global sections; hence it has a nonzero global section. The injection H_Z⁰(O_X)⊗L^m→L^m makes that a nonzero section of a tested line bundle. Its formal restriction along Y is zero, contradicting injectivity of weak Lefschetz comparison.

Thus x with closure disjoint from Y cannot be associated. This proof does not exclude an associated point outside Y whose closure meets Y. It also does not prove the next, stronger question about depth≥2 at all off-Y points. The distinction has been restored in both itemSA14-286 and claimC-SA14-284.

## P29. Exact completion and removing t-power torsion

Source58:46,48. On a noetherian affine chart, adic completion is flat and completion of finite modules is tensoring with the completed ring. Hence completion of coherent sheaves is exact. A finite module completes to zero at a point of D exactly when its restriction modulo the defining ideal is zero; Nakayama then makes its stalk zero there. Therefore the kernel consists precisely of coherent sheaves with closed support missing D. This is a Serre subcategory. The induced exact functor on the Serre quotient is faithful: if a map becomes zero, its image belongs to the kernel, so the map is zero in the quotient. It is conservative because the kernel and cokernel of a map sent to an isomorphism vanish in that quotient. None of this proves fullness; P7 supplies an explicit failure.

For a coherent module M, the ascending sequence ker(t^n:M→M) stabilizes locally and, on a quasi-compact noetherian scheme, uniformly. Call the stable submodule T. It is coherent. If t·(m+T)=0, then tm∈T, so some t^{N+1}m=0, hence m∈T. Thus t is regular on M/T. This verifies the dévissage on48 but leaves the separately doubtful dimension/depth hypotheses untouched.

## P30. Duality, localization, and the degree-zero endpoint

Source58:56,58–62. For X=P^r_k and coherent F, duality identifies H^i(X,F(−m))^∨ with Ext_X^{r−i}(F,ω_X(m)). For sufficiently large m, Serre vanishing in the local-to-global Ext spectral sequence identifies this Ext group with global sections of the coherent sheaf Ext_X^{r−i}(F,ω_X)(m). The support of these Ext sheaves is then translated into depth by local duality/regular ambient dimension. This is the precise negative-twist route; it is not equivalent without further indexing restrictions to finite generation of ⊕_{m≥0}H^i(F(m)). P3 demonstrates the distinction.

For j:U=X−Z→X, the degree-zero localization sequence is 0→H_Z⁰(F)→F→j_*F|U→H_Z¹(F)→0. Only for i>0 does one have R^i j_*F|U≅H_Z^{i+1}(F). Thus an aggregate depth reformulation that uses F=j_*F|U has explicitly killed the first two obstructions. Ignoring this condition changes the statement in degree0. Exactness also gives the injective/surjective reversal in P4.

For a countable inverse system of complexes there is a Milnor exact sequence 0→lim¹H^{i−1}→H^i(Rlim)→limH^i→0. Consequently even where formal cohomology is represented by the derived limit of thickenings, replacing it by the ordinary limit of cohomology needs the lim¹ term to vanish. Mittag–Leffler is a sufficient condition; proper coherent finiteness or SGA2 IX2.1 gives it in the specific settings read. The torn or revised manuscript formulas do not supply it automatically. These are targeted checks of the logical route, not a new proof of all SGA2 finiteness theorems.

## P31. Brauer–Witt induction on the reused representation-theory page

Source58:63, lines1706–1741. Insert a summation symbol only for the purpose of checking the proposed formula: 1=Σ n_λ Ind_{H_λ}^G φ_λ, with n_λ integers and φ_λ characters of E-representations. This is the external induction input attributed on the sheet to Witt/Swan; it is not proved by the fragment. Multiplying by an E-valued character χ and using the tensor-induction identity gives χ=Σ n_λ Ind(φ_λ·Resχ). If E[H_λ] is decomposed, the E-valued characters in the parentheses are realizable over E. Thus χ is a virtual integral combination of characters of E-representations of G.

Why this virtual conclusion suffices needs the missing earlier criterion(b): in characteristic0 the character lattice of E-representations is generated, for each Galois orbit of absolutely irreducible characters, by its orbit sum multiplied by the corresponding Schur index. An actual character in this lattice has nonnegative multiplicities, so its orbit multiplicities are nonnegative multiples of those indices and it is realizable. Applying this to every E-valued character forces all the relevant Schur indices to1. Equivalently E[G] is a product of matrix algebras over commutative centres. It does not force all those centres to equal E; “décomposée” must not be translated as E-split.

Fontaine1971 §8 supplies the opened Schur-index and elementary-subgroup framework. The sheet’s precise physical source and its preceding criterion(b) are not identified here, and its theorem3 is cut off before the definition(R_p) can be recovered. The induction check is conditional on the displayed external induction theorem and carefully distinguishes this from an independent proof of that theorem.


## P32. Projectivity from finite-order approximation

Source57:272 line20. Let A be a noetherian local ring, X proper over A, and suppose the finite-order approximation property C202 holds for line bundles on X after completion. If X_Â is projective, choose an ample invertible sheaf L̂ on X_Â. Approximation on the closed fibre gives an invertible sheaf L on X with L|X₀≅L̂|X₀, so L is ample on X₀. The opened Stacks Lemma37.50.3 (0D2S) gives an open neighborhood V of the closed point on which L is relatively ample. In SpecA every open containing the closed point is all of SpecA: any basic open D(a) containing the maximal ideal has a∉m, hence a is a unit. Thus L is relatively ample everywhere. Since X→SpecA is proper and the affine base has an ample invertible sheaf, the opened Stacks Lemma37.50.1 (0B44) implies X→SpecA projective. This checks the implication from approximation, not approximation for rings outside Artin’s hypotheses and not projectivity descent along arbitrary faithfully flat maps.
