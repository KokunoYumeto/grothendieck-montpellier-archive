# Local comparison programme: Part B

AI-produced by GPT-6 Astra (OpenAI), agent `/root/period_triangle`, 19 November 2026. This is a proof and source record, not a claim that the whole RESEARCH_SA07 task is complete.

## B.0. Reading, categories, and conventions

Read the supplied first-witness transcriptions of 18:5, 18:6, 18:43; the second witness of 18:5–6; notes [I] P01–P06, P32–P33; and the supplied discussion of H3. No manuscript scans were supplied. The ambiguous “double réseau|viseur” is retained as a pair of realizations with an explicit comparison. The prime in 5′ remains a genuine alternative: its interpretation is decided below, not silently edited.

For Fontaine's comparison set-up impose **mixed characteristic**: K is complete discretely valued of characteristic zero, its residue field κ is perfect of characteristic p, O_K its valuation ring, K_0=W(κ)[1/p], e=[K:K_0]<∞ arbitrary, C the completed algebraic closure, and G_K=Gal(Kbar/K). Every positive theorem below includes p=2 except where an older theorem's restriction is explicitly recorded. No finite-residue-field assumption is imposed unless stated.

Let BT(O_K) and BT(K) denote finite-height p-divisible groups, and append a subscript Q to invert isogenies. Use the covariant lattice T_pG=lim G[p^n](Kbar) and V_pG=T_pG⊗Q_p. Call r the **Hodge–Tate exponent** of C(r); in particular Q_p(1) has exponent +1. For G/O_K the exponents of V_pG are 0 and 1. For the contravariant cohomological realization V_pG^∨, the filtration on D_cris(V_pG^∨) has possible jumps 0 and 1. This dualization, rather than an unexplained change of weight convention, relates the two descriptions.

A single Hodge–Tate grading is supplied by the theory. A bigrading can be obtained from it by assigning (r,w−r) only after a separate pure weight w has been supplied. A general p-divisible group is not supplied with such a motivic weight by the notation on 18:5.

The word “pseudo-motif” on that page is not accompanied by a category, morphisms, or realization functors. The precise replacements below classify representations and p-divisible groups in named categories. They do not claim an essential-image classification for an undefined category of pseudo-motives or for all geometric motives.

## B.1. The four local descriptions

### B.1.1. Groups over K and over O_K

There is an equivalence

\[
 BT(K)\longrightarrow\operatorname{Rep}_{\mathbb Z_p}^{\rm free,cont}(G_K),\qquad G\longmapsto T_pG.
\]

Indeed every finite group scheme of p-power order over a characteristic-zero field is étale. Finite étale descent identifies G[p^n] with its finite G_K-module of geometric points; for a height-h p-divisible group these are free Z/p^n-modules and the transition maps recover the lattice. Conversely a free continuous lattice T gives the finite étale group schemes corresponding to T/p^nT, with their usual inclusion and multiplication maps; the p-divisibility axioms can be checked after the faithfully flat extension Kbar/K, where they are the usual axioms of (Q_p/Z_p)^h. These constructions and the Hom identifications are inverse. Every finite-dimensional continuous Q_p-representation has a stable lattice: compactness of its image, applied to a fixed lattice, bounds all its translates, and their sum is a stable lattice. Thus BT(K)_Q classifies **all** continuous finite-dimensional Q_p-representations.

This proves why a good-reduction condition is necessary in 6′. It is not an extra condition on every object of BT(K). An explicit non-potentially-Hodge–Tate example is available for every p. Take K=Q_p(μ_p) for odd p, and K=Q_2(i) for p=2; put s=1/(p+1), and

\[
 \rho_s(g)=\exp\bigl(s\log\chi(g)\bigr).
\]

Here χ(G_K) lies in 1+pZ_p, or in 1+4Z_2; the logarithm and exponential converge and define a continuous Z_p-valued unit character. It gives a height-one étale p-divisible group over K by the preceding construction. Exactly ρ_s^(p+1)=χ. If ρ_s became Hodge–Tate over a finite extension L, its one-dimensional C-extension would have an integer exponent r. Tensoring p+1 times gives exponent (p+1)r for χ, whereas the cyclotomic character has exponent 1. Tate's Theorem 2, giving H^0(G_L,C(m))=0 for nonzero m, makes those exponents unique. Thus (p+1)r=1, impossible for an integer r. This proof applies after every finite extension and uses no unverified Sen theorem locator. Differentiating the explicit character also gives its Sen eigenvalue s, in agreement with the same conclusion.

Tate's *p-Divisible Groups* (1967), §4.2 Theorem 4 and Corollary 1, proves

\[
 \operatorname{Hom}_{O_K}(G,H)
 =\operatorname{Hom}_{G_K}(T_pG,T_pH).
\]

His theorem applies more broadly to normal noetherian integral domains of characteristic-zero fraction field. Here its hypotheses hold because O_K is a DVR. Tensoring this equality with Q_p gives full faithfulness up to isogeny; conversely a rational equivariant map becomes integral after multiplication by a power of p. Hence the restriction BT(O_K)_Q→BT(K)_Q is fully faithful.

Its essential image consists exactly of **crystalline representations with exponents in {0,1}**. Integrally it consists of all stable free Z_p-lattices in those representations. The opened proof chain is Kim, Theorem 2.3 (Kisin's results), Theorem 4.1 (the missing integral p=2 case), and the finite-height construction explained below. Tate supplies full faithfulness. To see the integral statement from the rational existence theorem, start with one group giving a lattice T_0 in V; any other stable lattice T can be scaled into T_0 with finite index. The finite G_K-subgroup defining the quotient is the generic fibre of its finite flat schematic closure in an appropriate G_0[p^n]; the quotient of G_0 by that finite flat subgroup gives the prescribed isogenous lattice, with variance fixed by choosing T or its scaled superlattice. Equivalently use the exact height-one Kisin classification. No restriction e<p−1 is being carried over from Fontaine–Laffaille theory.

For potentially good reduction, the image is exactly the representations becoming crystalline of exponents {0,1} over a finite L/K. One direction is base change. For the other, apply the classification over O_L to the restriction and use the original G_K-representation to construct the object over K by the étale equivalence above. Its base change has the desired O_L-model. This does not provide an O_K-model. To classify the original K-object by the L-data one must retain descent. For example a nontrivial quadratic character cut out by Q_5(√5)/Q_5 and the trivial character become identical after that extension, but their Hom space over G_Q5 is zero. Their one-dimensional p-divisible generic fibres therefore cannot be identified over Q_5.

If the words on 18:5 are read as allowing equal characteristic, take K=F_p((t)) and G=μ_{p∞}. Its geometric p-power torsion points are all the identity, hence T_pG=0, while id_G is nonzero. Thus 5′ is not faithful under that reading. The Fontaine/Q_p/C comparison set-up above explicitly addresses mixed characteristic. Characteristic-p replacements require Dieudonné/crystalline data, as in B.3, including the connected part that this Tate functor kills.

### B.1.2. 5′ and the prime ℓ

For ℓ=p, 5′ is exactly the functor just classified. For ℓ≠p, multiplication by ℓ is invertible on every p-primary group sheaf: at level p^n choose integers a,b with aℓ+bp^n=1. It follows that G[ℓ^m]=0 and T_ℓG=0 for every p-divisible G. The functor then has only the zero object in its essential image and is not faithful; G=Q_p/Z_p already detects the nonzero identity sent to zero. Thus the p-reading gives the advertised information, whereas the literal different-prime reading gives the zero functor. For an abelian variety the whole ℓ-divisible group A[ℓ∞] is a different input, and the exact morphism relating the constructions is the decomposition of its torsion into its prime-primary summands.

### B.1.3. 3′ and 2′: what Hodge–Tate data retain

For a Hodge–Tate representation V put

\[
 D_{{\rm HT},r}(V)=(V\otimes_{\mathbb Q_p}C(-r))^{G_K},\qquad
 \iota_{\rm HT}:\bigoplus_rD_{{\rm HT},r}(V)\otimes_K C(r)
       \xrightarrow{\sim}V\otimes_{\mathbb Q_p}C.
\]

The map is evaluation, and its images give the canonical grading. Tate 1967, §4.1 Theorem 3, Corollary 2, supplies the p-divisible-group case (duality translates his displayed Hom(T(G),C) formula). Consequently:

* Retaining V with its continuous G_K-action and adjoining its canonical Hodge–Tate grading gives a fully faithful functor on BT(O_K)_Q. Every equivariant map preserves the displayed invariant spaces, so this statement follows directly from Tate's full-faithfulness theorem. Its essential image is precisely the crystalline exponent-{0,1} representations equipped with this evaluation isomorphism. The same statement with potentially crystalline representations applies to potentially good groups.
* If 3′ or 2′ retains only a Q_p-vector space and a grading of its C-extension, the functor is faithful but **not full**, even for good reduction. Let κ=F_p, and let T_a be the rank-one unramified lattice on which arithmetic Frobenius acts by a. Use a=1 and a=1+p for odd p, or a=1 and a=5 for p=2. The characters are continuous through Zhat→Z_p→Z_p^×. They correspond to étale p-divisible groups over O_K. Their Hodge–Tate exponents are both zero, so the bare graded objects are each Q_p with the whole C-line in degree zero. Every Q_p-linear map preserves this grading. But equivariance of a scalar x between the two lattices requires (a−1)x=0, so only x=0 occurs. Inverting isogenies does not change that obstruction.

There is an explicit complete parametrization of the bare essential image, though forgetting the action destroys classification of morphisms. For each weakly admissible filtered φ-module D with Fil^0D_K=D_K and Fil^2D_K=0, form V_cris(D)^∨ by the formula in B.2, its invariant spaces above, and then forget G_K. These, up to graded Q_p-isomorphism, are exactly the bare objects arising from BT(O_K)_Q. Necessity and sufficiency follow from the equivalence of B.1.4. This parametrization uses only finite-dimensional filtered φ-linear algebra and Fontaine's explicitly specified period rings; it does not refer back to an unknown p-divisible group. For potentially good reduction, range over finite extensions L/K and retain a G_K-descent action until the final forgetful step. A bare arbitrary C-grading, without this condition, is not asserted to come from a group.

“After finite extension” does not turn a general representation into a Hodge–Tate one, as ρ_s proves. Hodge–Tate-ness itself descends across finite extensions: the canonical exponent spaces over L are G_K-stable by their invariant definition; finite Galois descent of their L-coefficient spaces yields the same total dimension over K. Good reduction, in contrast, may genuinely require L. Modifying the domain or forgetting descent are explicit functors with the effects just described.

### B.1.4. 6′: filtered Frobenius data and exact essential image

Let MF_K^φ be finite-dimensional K_0-vector spaces D with bijective σ-semilinear φ and an exhaustive separated decreasing filtration on D_K=D⊗_{K_0}K. Morphisms are φ-compatible K_0-linear maps whose scalar extensions preserve the filtration. Set

\[
 t_H(D)=\sum_i i\dim_K\operatorname{gr}^iD_K,
 \qquad t_N(D)=v_p(\det\phi),
\]

where the second expression is calculated in a basis; changing basis changes the determinant by σ(detB)/detB, of valuation zero. Weak admissibility means t_H(D)=t_N(D) and t_H(D′)≤t_N(D′) for every φ-stable K_0-subspace D′ with induced filtration. Then

\[
 BT(O_K)_{\mathbb Q}^{\rm op}\simeq
 \{D\in MF_K^{\phi,wa}:\Fil^0D_K=D_K,\ \Fil^2D_K=0\},
 \qquad G\mapsto D_{\rm cris}(V_pG^\vee).
\]

Colmez–Fontaine, Theorem A and §4.3 Theorem 4.3 with its corollary, identifies weak admissibility with admissibility. Its N=0 subcategory gives crystalline representations. The exponent condition becomes precisely the two filtration jumps after the indicated dual. Kisin/Kim then gives the required p-divisible group. Full faithfulness is the composition of the Tate Hom isomorphism and the fully faithful D_cris functor. This is a proof of the displayed anti-equivalence from the opened statements, not an assumption that all filtered modules are geometric.

An arbitrary filtered φ-module need not be weakly admissible. Already D=K_0e, φ(e)=e, Fil^1D_K=D_K and Fil^2D_K=0 has t_H=1 and t_N=0. Thus the data listed in the square bracket on 18:5 are insufficient without admissibility.

The placement of σ is also substantive. Frobenius belongs on K_0, and the filtration belongs after extension to K; a lift of σ to K need not exist. Here is an explicit all-hypotheses counterexample to a required σ-semilinear endomorphism over K itself. Put p=2, K_0=Q_2(ζ_3), σ(ζ_3)=ζ_3², and K=K_0(π) with π³=2ζ_3. This is an Eisenstein, totally ramified extension of degree 3, with perfect residue field F_4. If σ extended to an automorphism of K, then z=σ(π)/π would be a unit with z³=ζ_3. Reducing gives a nonzero element of F_4 whose cube is the primitive cube root ζ_3bar. Every nonzero element of F_4 has cube 1, contradiction. The necessary correction to 6′ is the exact scalar-extension map D→D_K, not an identification of the coefficient fields.

For integral classification choose a uniformizer π and its Eisenstein polynomial E(u), put S=W(κ)[[u]], φ(u)=u^p. A height-one Kisin module is finite free over S, with linearized φ-map φ^*M→M injective and cokernel killed by E(u). Breuil's opened Theorems 1.2 and 4.2.2.9 give the strongly divisible-module theory for p>2; his crystalline essential-image Theorem 1.4 assumes p>2 and κ⊂F_pbar. Kim's Theorem 2.3 records Kisin's unrestricted perfect-residue rational result and p>2 integral equivalence; Kim Theorem 4.1 establishes the integral equivalence for p=2. Kim Proposition 4.2 identifies the associated Dieudonné crystal evaluated on the PD-envelope with the corresponding strongly divisible module. Thus the modern statement is all p and arbitrary finite e, while the historical restrictions remain visible. At p=2 the naive map from the Kisin realization into the Breuil A_cris realization need not be an isomorphism (Kim, immediately before Theorem 4.1); the corrected equivalence must be used.

## B.2. What replaces 1′ and 4′

### B.2.1. The comparison pair and its inverse

Fontaine's de Rham period field is B_dR=Frac(B_dR^+), where B_dR^+ is the kerθ-adic completion of A_inf[1/p], A_inf=W(O_C^flat), θ:A_inf→O_C. With compatible p-power roots of unity ε, t=log[ε] is a uniformizer of B_dR^+ and g(t)=χ(g)t. Put Fil^iB_dR=t^iB_dR^+. The crystalline period ring is B_cris=A_cris[1/p,1/t], where A_cris is the p-adically completed divided-power envelope of kerθ; it has Witt Frobenius φ. B_st additionally carries N with Nφ=pφN; an embedding into B_dR uses the usual compatible logarithm/uniformizer choice.

For a representation V and B=B_dR, B_cris or B_st, set D_B(V)=(V⊗B)^{G_K}. The coefficient fields are K for B_dR and K_0 for B_cris,B_st. B-admissibility is the equality of the corresponding dimension with dim_QpV. Under this equality the evaluation map

\[
 \iota_B:B\otimes D_B(V)\xrightarrow{\sim}B\otimes_{\mathbb Q_p}V
\]

is the precise local analogue of the Betti–de Rham comparison. It preserves the filtration after B_dR-extension, Frobenius on the crystalline side, and N in the semistable case. For weakly admissible D the inverse is

\[
 V_{\rm st}(D)=
 (B_{\rm st}\otimes_{K_0}D)^{\phi=1,N=0}
 \cap\Fil^0(B_{\rm dR}\otimes_K D_K),
\]

inside the common B_dR-extension; for crystalline D use B_cris and omit N. Colmez–Fontaine Proposition 4.2 and Theorem 4.3 prove the inverse identities on the stated categories. This reconstructs both the Galois module and the filtered φ-module, including all its tensors, by explicit functors.

The filtered K-space D_dR alone does not reconstruct V. The two unramified rank-one representations in B.1.3 both have D_dR=K in degree zero, while their Frobenius on D_cris differs; their Galois Hom space is zero. The exact loss of information is the forgetful functor (D,φ,Fil)↦(D_K,Fil). Retaining V and the B_dR comparison gives the “double viseur”; retaining crystalline Frobenius makes the reverse reconstruction possible from the filtered module alone.

For X/K proper smooth, every i has the canonical filtered G_K-equivariant isomorphism

\[
 H^i_{\rm et}(X_{\bar K},\mathbb Q_p)\otimes B_{\rm dR}
 \simeq H^i_{\rm dR}(X/K)\otimes_K B_{\rm dR}.
\]

Scholze Theorem 1.6 and Corollary 1.8 provide this for proper smooth rigid-analytic spaces under the same complete-DVR, perfect-residue hypotheses, with no restriction on e, p, or reduction. Apply analytification to algebraic X. Good reduction upgrades the comparison to B_cris and the special fibre's crystalline cohomology. Semistable reduction gives B_st and Hyodo–Kato cohomology with N. Tsuji's author survey, Theorem 1.1 (2002), states the exact semistable theorem; Theorem A1 gives the proper-smooth de Rham consequence. Its semistable model is proper flat regular over O_K, with reduced normal-crossing special fibre; all p and arbitrary e are allowed. Tsuji ICM1998 Theorem 2.2.1 and Corollary 2.2.3 also give semistability and potential semistability, respectively.

### B.2.2. The relative comparison and Gauss–Manin

Let f:X→Y be proper smooth between smooth rigid-analytic varieties over K. Let L be a de Rham lisse Z_p-sheaf on X, with associated filtered vector bundle with integrable connection (E,∇,Fil). Assume R^if_*L is lisse; this holds in the analytification of the algebraic situation. Scholze Theorem 1.10 states that R^if_*L is de Rham and that its associated filtered connection is

\[
 R^if_{{\rm dR}*}(E,\nabla,\Fil).
\]

For L=Z_p this is H^i_dR(X/Y) with its Gauss–Manin connection and Hodge filtration. The pro-étale period sheaf O_B_dR provides the relative comparison; the connection on the right is transported to the canonical connection on that sheaf, and Griffiths transversality is part of the filtered-connection structure. This is the exact replacement for 4′. It does not identify a rational local system with a bundle before extending coefficients.

The 2016 corrigendum was opened. It corrects the covering condition in the pro-étale topology and the p-adic completion in the definition of O_B_dR^+; it explicitly retains the comparison results. We use those corrected definitions. In particular, arbitrary open surjections of profinite sets must not be substituted for the corrected coverings.

### B.2.3. Integral data and their limits

For a proper smooth formal scheme 𝔛/O_C, BMS Theorem 1.8 constructs a perfect A_inf-complex with Frobenius and gives four derived comparisons: with crystalline cohomology over W(κ_C), de Rham cohomology over O_C, crystalline cohomology over A_cris, and Z_p-étale cohomology after inverting μ=[ε]−1. Its specializations retain integral torsion. BMS Theorem 1.4, under torsion-freeness in crystalline degrees i and i+1, reconstructs integral crystalline H^i from the étale lattice with the B_dR^+-lattice supplied by the comparison. The lattice component is indispensable.

These are derived base changes; replacing ⊗^L by an ordinary tensor product in each cohomological degree without a flatness/torsion hypothesis would discard Tor terms. The filtered complex of differentials gives the integral Hodge filtration of a chosen smooth model; cohomology groups can have torsion and the associated filtration need not be a filtration by direct summands. Rational smooth-proper comparison supplies vector spaces, the de Rham filtration, and the relative Gauss–Manin connection. It does not make those integral torsion issues disappear.

Bhatt–Scholze, *Prismatic F-crystals and crystalline Galois representations*, Theorem 1.2 (=5.6), gives a separate exact integral classification for Spf(O_K): prismatic F-crystals in finite locally free O_Δ-modules correspond to free Z_p-lattices in crystalline representations. Evaluate on the Breuil–Kisin prism (W(κ)[[u]],(E(u))) to obtain integral Frobenius-module data. Its crystal property is the required compatible change-of-thickening data; evaluation on crystalline thickenings gives the associated connections. This statement is for the indicated local base. We do not silently assert that all relative cohomology groups of every smooth proper family are finite locally free integral crystals.

## B.3. The four questions of 18:43

### B.3.1. Problem 1a: “réseaux”

For an algebraic embedding k→C, the exact comparison is H^i_dR(X/k)⊗_kC≅H^i_B(X(C),Q)⊗_QC. If “réseau” denotes the rational/algebraic forms inside that C-space, this is the answer and their relative position is the period point of Part A. If it denotes a Z-lattice versus an integral de Rham lattice, the latter also needs an integral model. Even with the standard model of P¹ the comparison multiplies the algebraic codimension-one class by 2πi. In the orientation and α convention of Part A, α(e_B)=(2πi)^−1e_dR. Thus the image of Z e_B is (2πi)^−1 Z e_dR, not Z e_dR: the explicit map proves the failure of the unscaled lattice identification. Tensor powers give the analogous factor in every Tate degree. This calculation is already proved in F.1 and is not assumed merely from an analogy.

### B.3.2. Problem 1c: real structures and splittings

For a real model use real bases of D and a rational Betti basis. The cohomological real Frobenius f_∞ is rational, and the comparison satisfies

\[
 \kappa_D\alpha=\alpha f_\infty\kappa_B,
 \qquad \bar\alpha=\alpha f_\infty.
\]

Consequently the actual real de Rham subspace is

\[
 D_{\mathbb R}=\alpha\bigl((V_B^+\otimes\mathbb R)
                       \oplus i(V_B^-\otimes\mathbb R)\bigr).
\]

The rational Betti real form instead transports to α(V_B⊗R). These formulas compare the two forms without identifying them. The Hodge splitting is the opposed-filtration splitting of F_D and α f_∞α^−1F_D; its maps and field of definition are established in A.1–A.2. Thus the real structure is exactly comparable, while algebraicity of that splitting is the concrete period question in A.4(c), not a consequence of the existence of the real form. For a motive without a real model, conjugation relates M to c*M through the semilinear map of A.2; an endomorphism f_∞ of the same rational object is not supplied unless descent data are given.

### B.3.3. Problem 3

Read “p-adic cohomology” as H^i_et(X_Kbar,Q_p): the B_dR comparison in B.2 answers the proper smooth case, with all the hypotheses specified there. Read it as the special fibre's crystalline cohomology: a good-reduction model supplies D_cris and a B_cris comparison. For semistable models one replaces ordinary crystalline cohomology by log crystalline/Hyodo–Kato cohomology, adds N, and uses B_st. The map to de Rham cohomology is the Hyodo–Kato comparison and depends on the uniformizer convention; the representation and its full filtered (φ,N)-module retain the invariant information. This states exactly which inputs are needed for each reading. A comparison for arbitrary unspecified spaces or raw integral lattices is not asserted by the sentence on the page.

### B.3.4. Problem 4: characteristic p

Let X be a scheme of characteristic p over a perfect field κ and K_0=W(κ)[1/p]. The following table gives precise positive replacements, with explicit scope.

| Theory and scope | Integral object | Frobenius | Filtration / connection | Comparison used here |
|---|---|---|---|---|
| Crystalline, X smooth proper/κ | Perfect W(κ)-complex; finite cohomology, possibly torsion | σ-semilinear; isogeny after inverting p | A smooth lift supplies its de Rham filtration; relative crystals supply integrable connections | Crystalline–de Rham specialization, or the crystalline prism below |
| Rigid, X separated finite type/κ | Rational K_0-cohomology; no integral lattice is part of this definition | Frobenius isomorphism (σ-linear), including compact supports | Overconvergent coefficient crystals carry connections; a Hodge filtration requires additional lift/geometric data | For smooth proper X it agrees with crystalline cohomology after inverting p |
| Prismatic, smooth p-adic formal X over A/I for a bounded prism (A,I) | Perfect A-complex when proper; integral and derived | φ_A-semilinear, an isogeny after inverting I | Nygaard filtration and de Rham specialization; crystal descent encodes connections | (W(κ),(p)) gives crystalline; Breuil–Kisin/A_inf prisms give mixed-characteristic de Rham and étale comparisons |

The exact primary locators are Bhatt–Scholze *Prisms and prismatic cohomology*, Theorem 1.8(1)–(6), Theorem 1.16 (=15.3), and Example 1.9(1); Berthelot *Finitude et pureté cohomologique en cohomologie rigide*, Proposition 1.9 (smooth-proper crystalline comparison) and Theorem 3.1 (smooth schemes and supports in a closed subscheme); Kedlaya *Finiteness of rigid cohomology with coefficients*, Theorems 1.2.1–1.2.2 (all separated finite-type schemes, ordinary and compactly supported cohomology). Déglise's author proof in *Proper cohomological descent in rigid cohomology*, Proposition 6.2 and Remark 6.3, gives Frobenius invertibility: proper smooth hypercover descent reduces ordinary cohomology to the smooth case, and compactification/localization gives compact supports. For (W(κ),(p)), Frobenius on the base is an automorphism, so the Frobenius pullback in the prismatic–crystalline comparison is merely a scalar twist and can be undone canonically. This gives the exact morphism relating those two entries of the table. The integral statement for smooth proper X follows from perfectness over the DVR W(κ); its cohomology is finitely generated and inverting p gives finite-dimensional vector spaces with bijective Frobenius.

The étale comparison in Prisms Theorem 1.8(4) requires a perfect prism and refers to the generic fibre. At the crystalline prism (W(κ),(p)), a characteristic-p scheme has empty characteristic-zero generic fibre; that formula is not an identification of all crystalline cohomology with the special fibre's p-adic étale cohomology.

An unfiltered characteristic-p special fibre does not itself select the Hodge filtration of every characteristic-zero lift. The input to that filtration is the lift and the de Rham comparison. This is recorded by the scalar-specialization maps in the table; no arbitrary identification of a Nygaard filtration with a chosen Hodge filtration is made.

## B.4. The two splittings of 18:6

### B.4.1. Exact group calculation

Let 1→H→E→π→1 be a topological group extension, with H=G′(C), and continuous sections σ_1,σ_2. Transport u:π→G(Q_p) into H using the specified C-isomorphism α. Write u for this transported homomorphism, j:G_m(Q_p)→H for j_2, and χ:π→Q_p^×. The page assumes σ_1(π) centralizes u(π) and σ_2(π) centralizes jχ(π). These assumptions show that σ_1u and σ_2jχ are sections: multiplying their values and using the stated commutation gives the section law.

They do not imply that the sections are equal. That equality is the additional compatibility written on the page. With it, cancellation in E gives exactly

\[
 \varphi(\gamma)=\sigma_1(\gamma)^{-1}\sigma_2(\gamma)
 =u(\gamma)j(\chi(\gamma)^{-1}).
\]

No commutation of u with j is used in this cancellation. The map φ need not be a homomorphism. Its exact right-cocycle law is

\[
 \varphi(\gamma\delta)
 =\sigma_1(\delta)^{-1}\varphi(\gamma)\sigma_1(\delta)\varphi(\delta).
\]

This follows by substituting σ_2(γ)=σ_1(γ)φ(γ) into the two section laws. Its identity fibre, denoted kerφ here, is the equalizer of the sections and is a subgroup, but need not be normal.

The compatibility is genuinely additional. Take π=C_2, H=C^×, E=H×π, σ_1(γ)=(1,γ), σ_2(γ)=((−1)^γ,γ), u=1, χ=1, j=id. All stated centralizations hold and both modified maps are sections, but they differ. This finite counterexample is completely checked in the accompanying program.

### B.4.2. Kernels and χ descent

Under the compatibility, χ=1 implies φ=u. Therefore the always valid equality is

\[
 \ker\chi\cap\ker\varphi=\ker\chi\cap\ker u.
\]

The page's claimed equality with keru holds **exactly when** keru⊂kerχ. Necessity follows by inclusion of the left side in kerχ, and sufficiency follows from the displayed equality. A sufficient motivic condition is a character ε:G→G_m with χ=ε∘u; this is the exact morphism needed to use a Tate character in the generated tensor category.

Even the full splitting compatibility does not force this kernel inclusion. Take π=C_2, χ(γ)=(−1)^γ, u=1, E=C^××π, σ_1(γ)=(1,γ), σ_2(γ)=(χ(γ)^−1,γ), j=id. Then σ_1u=σ_2jχ, but keru=π while kerχ∩kerφ={1}. The same construction works with π=G_K and its cyclotomic χ. The finite version makes all assertions mechanically checkable.

The character χ descends to Π_1=π/keru if and only if keru⊂kerχ. Necessity and sufficiency are precisely the universal property of the quotient; when it descends, χ_1([γ])=χ(γ). Thus the two gaps in the page's final lines have one exact common condition.

### B.4.3. Analyticity and the relation to Sen

Assume π is profinite, u is continuous, and G is a finite-dimensional linear algebraic Q_p-group. Then u(π) is compact and closed in G(Q_p). The quotient map induces a continuous bijection π/keru→u(π); compactness of the source and Hausdorffness of the target make it a homeomorphism. The closed subgroup theorem for p-adic Lie groups makes u(π) a p-adic analytic group, for every p, including p=2. This proves the analytic assertion under exactly the continuity and finite-dimensional hypotheses. No Hodge–Tate assumption enters this proof.

For a Hodge–Tate representation V, the grading gives h:G_m,C→GL(V_C) acting by z^r on the exponent-r part and Θ=dh(1) acting by r. Sen's theorem controls the Lie algebra of the **inertia** image: it is the smallest Q_p-subspace of End(V) whose C-extension contains Θ. For Hodge–Tate V this Lie algebra is algebraic. When the residue field is algebraically closed the whole G_K is inertia, and Serre 1979, §1.3 Theorems 1 and 1′, §1.4 Theorem 2 and its equivalent forms, states that the connected algebraic envelope is the smallest algebraic Q_p-subgroup containing h after C-extension. The residue-field hypothesis is explicit in Serre §1.1; it cannot be dropped when replacing inertia by the full Galois image.

Here is a sharp counterexample to that dropped hypothesis. Set K=Q_5 and let s=√6∈Z_5 be the root congruent to 1 mod5; Hensel's lemma constructs it and s∉Q. The continuous unramified representation on Q_5² sends Frobenius to diag(6,exp(s log6)). Its image is the Z_5-parameter group

\[
 z\longmapsto\operatorname{diag}(\exp(z\log6),\exp(sz\log6)).
\]

It has Lie algebra Q_5·diag(1,s) (the common nonzero scalar log6 is irrelevant). Both characters are unramified, hence arise from étale p-divisible groups over Z_5 and are Hodge–Tate of exponent zero. Thus h is trivial and Θ=0. The full image nevertheless has a nonzero one-dimensional Lie algebra. Moreover that Lie algebra is not the Lie algebra of an algebraic subgroup of G_m²: a connected one-dimensional algebraic subgroup is cut out by x^m y^n=1 for nonzero (m,n)∈Z², which would force m+ns=0, impossible. Its Zariski closure is the full two-dimensional torus by the same character argument. Inertia is trivial, in exact agreement with Sen.

The concrete relationship to 18:6 is therefore: the page compares two sections and, with one compatibility, expresses their cocycle in terms of u and the cyclotomic grading character; differentiation of the grading gives Θ. The page's algebra proves the cocycle, kernel, and analytic statements above. It does not prove the minimal-Lie-algebra theorem: no equality between the coefficient span of Θ and Lie u(I_K) follows from those group identities. The unramified example proves that even the proposed full-image version would be false. H3 understood as the claim that these few lines already prove Sen's theorem is refuted; H3 understood as a historical anticipation is a priority question, not a consequence of the algebra.

## Source audit and unresolved source obligations

Opened full sources with exact locators used:

1. Tate, *p-Divisible Groups*, Proc. Conf. Local Fields (1967), §4.1 Theorem 3 Corollary 2; §4.2 Theorem 4 and Corollary 1: https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf . Web refs turn699450439view0, turn494595070view1, turn780112825view0. Printed pp180–181.
2. Colmez–Fontaine, *Construction des représentations p-adiques semi-stables*, author PDF https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf : Theorem A; §4.3 Proposition 4.2, Theorem 4.3 and following corollary. Web ref turn966091557view0. Introduction states perfect residue and arbitrary finite ramification.
3. Breuil, *Groupes p-divisibles, groupes finis et modules filtrés*, author PDF https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/p-divisibles.pdf : Theorems 1.2, 1.4, 4.2.2.9 and 5.3.2. Web refs turn796606530view3, turn425261056view1. Theorem 4.2.2.9 was verified directly in the full text, web ref turn887812515view2.
4. Wansu Kim, *The classification of p-divisible groups over 2-adic discrete valuation rings*, https://arxiv.org/pdf/1007.1904 : Definition2.1, Theorem2.3, Remark2.4, Theorem4.1, Proposition4.2, Corollaries4.3–4.4. Web refs turn146996013view0, turn469019112view0.
5. Scholze, *p-adic Hodge theory for rigid-analytic varieties*, https://people.mpim-bonn.mpg.de/scholze/pAdicHodgeTheory.pdf : Theorems1.5,1.6,1.10; Corollary1.8. Web refs turn553424266view0, turn469019112view1.
6. Scholze corrigendum, https://www.math.uni-bonn.de/people/scholze/pAdicHodgeErratum.pdf , items(1)–(3), full 3-page text opened; ref turn630541371view0.
7. BMS, *Integral p-adic Hodge theory*, https://arxiv.org/pdf/1602.03148 : Theorems1.4,1.6,1.7,1.8. Web refs turn181453555view0, turn771183395view2.
8. Bhatt–Scholze, *Prismatic F-crystals and crystalline Galois representations*, https://arxiv.org/pdf/2106.14735 : Definition1.1(4.1), Theorem1.2(5.6). Web refs turn181453555view1, turn934172339view4.
9. Bhatt–Scholze, *Prisms and prismatic cohomology*, https://www.math.uni-bonn.de/people/scholze/prisms.pdf : Theorem1.8(1)–(6), Theorem1.16(15.3), Example1.9(1). Web refs turn109184195view0, turn934172339view3.
10. Tsuji, *Semi-stable conjecture of Fontaine-Jannsen: a survey*, Astérisque279(2002), https://www.numdam.org/item/AST_2002__279__323_0.pdf : Theorem1.1, TheoremA1; §2.2. Web ref turn549658917view2. Tsuji ICM1998 author article https://ems.press/content/book-chapter-files/27150?nt=1 : Theorems2.2.1,2.2.2,3.2.1; Corollary2.2.3; web ref turn549658917view1.
11. Serre, *Groupes algébriques associés aux modules de Hodge-Tate*, Astérisque65(1979), https://www.numdam.org/item/AST_1979__65__155_0.pdf : §1.1, §1.3 Theorems1,1′; §1.4 Theorem2 and equivalent forms. Web refs turn699450439view1, turn780112825view1, turn116829401view4. This opened primary treatment explicitly attributes the central theorem to Sen1973 §6.
12. Benois author lecture text https://www.math.u-bordeaux.fr/~dbenoua/Documents/Introduction%20to%20p-adic%20Hodge.pdf : Proposition10.2.9, Theorem10.2.11, Example10.2.13. Web refs turn796606530view2, turn425261056view2. These are a checked exposition, not the original Sen papers.
13. Berthelot, *Finitude et pureté cohomologique en cohomologie rigide*, https://wstein.org/people/berthelo/publis/Finitude.pdf : Proposition 1.9 and Theorem 3.1, verified in the full author PDF. Web refs turn104180905view1, turn109304902view1, turn938589563view1.
14. Kedlaya, *Finiteness of rigid cohomology with coefficients*, https://arxiv.org/pdf/math/0208027 : Theorems 1.2.1–1.2.4, PDF pp3–4. Web refs turn309855580view0, turn966319760view1.
15. Déglise, *Proper cohomological descent in rigid cohomology*, author workshop text, https://deglise.perso.math.cnrs.fr/docs/2005/proper.pdf : Theorem 4, Proposition 6.2, Remark 6.3, printed pp11–12. Full proof opened; web refs turn188591387view1, turn900413238view0. Chiarellotto–Tsuzuki2003 https://www.numdam.org/item/RSMUP_2003__109__63_0.pdf was also opened: Theorem 11.7.1 and Remark 11.7.2 give the étale descent spectral sequence; §12.2 expressly warns the analogous relative Frobenius map is not an isomorphism in full generality. Web refs turn188591387view0, turn122252750view0, turn900413238view1.

Attempted but not obtained in full: Fontaine–Messing1987 (author publication list, DOI10.1090/conm/067/902593, AMS volume URL); Faltings1989 (exact-title searches via both engines, publication metadata only); Tsuji1999 Inventiones original (publisher PDF URL redirects to subscription preview); Sen1973 Annals original (Annals metadata and JSTOR stable page opened, direct PDF and guessed Annals PDF unavailable); Sen1980 Inventiones original (publisher PDF redirects to preview; the search-indexed digizeitschriften.de/download/pdf/356556735_0062/log12.pdf returned404, alternative download/resolver URLs also inaccessible); Kisin2006 original (author page linked wam.dvi, web tool cannot parse DVI, direct HTTP download returned403; guessed same-stemPDF unavailable). These are source obligations still outstanding; no claim is made to have opened them. The mathematical statements above are supported where possible by the explicitly named opened replacements. The attached historical bibliographic table is not substituted for an opened theorem.

Computable counterexamples are in `work/code_triangle/comparison_counterexamples.py` with exact output in the adjacent `.output.txt`; they check finite section identities, cocycles and kernels, the F_4 cube obstruction, the weak-admissibility arithmetic, and a finite Hensel approximation used only to illustrate the rigorously constructed 5-adic root. Approximate digits are not used to prove irrationality or nonalgebraicity.
