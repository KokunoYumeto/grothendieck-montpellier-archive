# Mathematical verification record: cotes 11, 55 and 56

Author of these reconstructions: GPT-6 Astra Pro, SA18 consolidation, 19 November 2026. The source transcriptions are unchanged. Absolute line locators refer to the supplied combined files. Code is in `scripts/root_certificates.py`; its complete exact-arithmetic output is in `outputs/root_certificates.json`. A finite computation corroborates the model specified below; it is not a substitute for the general argument.

## R1. Correspondences, actions, associativity and units

Let X,Y,Z,W be smooth projective varieties over a field. Use the Chow intersection product, or a Weil cohomology theory with its proper pushforward, projection formula and Cartesian base-change identity. For degree-zero correspondences u from X to Y and v from Y to Z, put v∘u=p_XZ*(p_XY*u · p_YZ*v). More generally the codimensions shift by dimY under pushforward. This is the source's target-first A(I′;I) notation after relabelling factors. Applying the projection formula followed by base change shows that its action on a class x is v_*(u_*(x)); this identifies exactly the missing Cartesian axiom flagged at c11:46.

On X×Y×Z×W both parenthesizations of w∘v∘u are the pushforward to X×W of p_XY*u·p_YZ*v·p_ZW*w. This proves associativity. The projection formula for the diagonal embedding and p_1∘Δ=p_2∘Δ=id prove both unit identities. Chow classes have even cohomological degrees, so no exchange sign appears. For general graded classes, one must retain the Koszul sign each time the order of factors is exchanged; the source's margin does not establish a sign-free formula for arbitrary odd classes.

Idempotent completion is a separate construction: the object (X,e) for e²=e has identity e, and the inclusion/projection between (X,e) and (X,1) are both e. Matrix multiplication gives finite sums. A twist changes correspondence codimension and the realization degree; naturality of a Lefschetz map is g_(M(1))L=L g_M. This is an editorial construction, not a theorem written on these leaves. A general cycle quotient need not satisfy the perfect pairing assumed in the source's opening; numerical and homological equivalence must not be identified without the appropriate standard conjecture.

## R2. Products of diagonal classes

Assume X is connected smooth projective of positive dimension d, over C with rational cohomology (or a Weil theory with one-dimensional top degree). Let y be the degree-one top class, so c_d(TX)=χ(X)y and y²=0. For a partition R of {1,…,k} into **nonempty** blocks, let Δ_R be the locus on which coordinates in each block coincide. Its dimension is d·b(R). Admitting an empty block in the written set R changes its cardinality without changing Δ_R; hence the source's formula must count nonempty blocks.

For partitions R,R′, set-theoretic intersection is Δ_(R∨R′). On each block C of the join, form the bipartite incidence multigraph: vertices are the R-blocks and R′-blocks contained in C, and the |C| coordinates are edges. The graph is connected. Its cycle rank is e_C=|C|−b_R(C)−b_R′(C)+1. The tangent equations identifying coordinates show that the excess normal bundle is TX raised to e_C on that diagonal factor. Clean-intersection excess gives the factor c_d(TX)^{e_C}. Thus e_C=0 gives an ordinary diagonal, e_C=1 gives χ(X) times its point class, and e_C≥2 gives0. This proves the connected case anticipated at c11:57; it also states exactly the cohomological hypotheses under which replacing c_d(TX) by χy is justified. In the full Chow ring CH₀(X), c_d(TX) need not equal χ times a chosen point.

For k=2 this gives δ²=χy₁y₂ and δy_i=y₁y₂. For k=3, δ₁₂δ₂₃ is the small diagonal, δ₁₂ times the small diagonal is χy₁y₂y₃, and the square of the small diagonal is0 by degree. The P¹ certificate realizes these products in Z[y₁,…,y_k]/(y_i²), where δ_ij=y_i+y_j and χ=2. It also proves the printed list called a basis need not be linearly independent: δ₁₂−y₁−y₂=0. A four-cycle gives2y₁y₂y₃y₄, whereas a tree gives the small diagonal. These finite calculations corroborate the general excess-bundle proof.

## R3. The reused configuration typescript

The R-partitions here are **not** the disjoint partitions in R2. Their subsets S₁,…,S_ν cover {0,…,n}, and each new S_k meets the preceding union at exactly one index. Therefore Σ|S_k|=n+ν. On U_R the first n+1 points are a projective basis and all designated coordinates of the additional ν points are units. After sending the first points to e₀,…,e_n, the remaining diagonal coordinate changes can normalize every designated coordinate to1.

Why the normalization exists and is unique: make a bipartite graph with coordinate vertices0,…,n and point vertices1,…,ν, with edges (i,k) when i∈S_k. It is a tree, by the one-point attachment rule. Starting with one scale, recursively solve the unit equations along its edges. The single redundant common scale is exactly the scalar quotient defining PGL. This proof works with units over a general base ring, so it verifies the scheme chart rather than only its geometric points. The remaining coordinates are free in number ν(n+1)−(n+ν)=nν−n. This yields U_R≅PGL_(n+1)×A^(nν−n), with the group acting by left translation on the first factor. The determinant ratios in c11:45 are the coordinate expressions of this normalization, including their line-bundle weights.

For n=2, S₁={0,1}, S₂={1,2}, the normal form is e₀,e₁,e₂,(1,1,a),(b,1,1). This is a direct check of the chart, not proof that every configuration lies in a particular U_R. Gluing invariant quotient charts and descending the specified linearized ample bundle are the further hypotheses of the stable-quotient theorem; no arbitrary PGL quotient is inferred.

The sorted cone calculation is independent of geometry. Put N=m+1 and d_i=λ_i−λ_(i−1)≥0. If Σλ_i=0, then

λ_j=−(1/N)Σ_(i=1)^m(N−i)d_i+Σ_(i≤j)d_i.

The extreme ray r_i has i entries −(N−i), followed by N−i entries i. Hence λ=Σ(d_i/N)r_i. Every d_i is nonnegative, and the inverse formula proves this is an isomorphism with the nonnegative orthant. The certificate checks these rational matrices exactly in dimensions2–8; the displayed formula proves every dimension. A separating functional must be nonzero: ℓ=0 meets the source's nonnegativity and vanishing equations for every point and cannot certify failure of interiority.

## R4. Integral quadric intersections and punctured cones

Let Q^n be a split smooth projective quadric over C. Cellular decomposition gives a free integral group in each even cohomological degree0,…,2n, with one extra generator in the middle when n is even; odd groups vanish. Use codimension indices and h=c₁(O(1)). Below the middle, h^i is primitive. Above the middle, h^i=2l_i for the primitive class l_i of a suitable linear isotropic subspace. For n=2ν, write α,β for the two middle ruling classes. Their intersections are

α²=β²=[pt], αβ=0 if ν is even; α²=β²=0, αβ=[pt] if ν is odd.

These equalities follow by choosing linear representatives disjoint or transverse in a point; the component rule for the isotropic Grassmannian gives precisely that parity. Also h^ν=α+β and hα=hβ. Thus λ=α−β satisfies hλ=0 and λ²=(−1)^ν2[pt]=(−1)^νh^(2ν). In the surface case this reduces to a²=b²=0, ab=[pt] on P¹×P¹. The handwritten universal plus sign is therefore false. The change-of-basis matrix from (h^ν,λ) to (α,β) is [[1,1],[1,−1]], with determinant−2 and Smith diagonal(1,2). The half-sum formula for α is an integral-lattice statement, not permission to divide all classes by2.

Multiplication by h is an isomorphism between the one-dimensional adjacent primitive groups except at the middle. On Q^(2ν−1) its critical matrix is[2]. On Q^(2ν) the two exceptional matrices are [1;1] and [1,1], with free cokernel and kernel generated by a ruling class modulo the sum and by α−β respectively. The certificate implements the entire integral multiplication table and verifies basis associativity through n=12. The geometric argument above proves the rule in all dimensions; the finite check can expose implementation/index errors but cannot prove the geometric identification.

The punctured affine cone E is the complement of the zero section in O_Q(−1). The Gysin exact sequence is controlled by multiplication by −h. Since the base cohomology is even and free,

H^(2j)(E)=coker(h:H^(2j−2)(Q)→H^(2j)(Q)),
H^(2j+1)(E)=ker(h:H^(2j)(Q)→H^(2j+2)(Q)).

For n=2ν−1≥1, the nonzero integral groups are H⁰=Z, H^(2ν)=Z/2 and H^(4ν−1)=Z. For n=2ν≥2, they are Z in degrees0,2ν,2ν+1,4ν+1. In particular both middle-degree displays at c56:15 need alarms. For Q⁰, E is two disjoint copies of G_m and must be treated separately. With finite coefficients one applies the universal coefficient sequence; a2-torsion quotient can also create a kernel one degree earlier. The handwritten bare μ notation does not justify reusing the integral table unchanged for every coefficient module.

The projective cone is obtained by contracting one section of P(O⊕O(−1)); the projective bundle formula and the relative sequence give H^i(C_projective)≅H^(i−2)(Q)(−1) for i>0, while H⁰ is the constant coefficient group. Its positive-degree product has the extra hyperplane factor from the self-intersection of the section. The affine cone contracts to its vertex. Hence for connected E, H⁰_a=H¹_a=0 and H^i_a(C_affine)=H^(i−1)(E) for i≥2. In étale cohomology use coefficients of order prime to the characteristic; SGA7 XV2.1.2 and2.1.6 give the exact published contraction and sign statements.

## R5. Affine quadrics and monodromy

Over C, U^n={Σ_(i=0)^n z_i²=1} retracts onto S^n. Writing z=x+iy gives |x|²−|y|²=1 and x·y=0; project x/|x| to S^n and identify y with a tangent vector. Contract y to0 to obtain the retraction. For n≥1 this gives H⁰=H^n=Z and, by oriented real2n-dimensional Poincaré duality, H_c^n=H_c^(2n)=Z. The n=0 case has two points. For n=1, U≅C* and both degree-zero/one terms in the long exact sequence are indispensable.

The compact-to-ordinary middle map is the self-intersection of the real zero section in its cotangent model. Its normal bundle is isomorphic to TS^n, but comparison with the complex orientation contributes (−1)^(n/2) when n is even. Thus it is0 for odd n and (−1)^(n/2)2 for even n. SGA7 XV2.2.5(D,E) confirms this sign with dual generators normalized to pairing1. Changing one independently chosen generator changes the displayed matrix, but cannot remove the signed geometric self-pairing once the duality convention is fixed.

For a local ordinary quadratic smoothing, z₀²+…+z_d²=t, a loop t↦e^(2πi)t lifts through square-root scaling to the antipodal map on the vanishing sphere S^d; its degree is(−1)^(d+1). The base change t=s² traverses the original loop twice and makes this monodromy trivial. Its projective homogenization is flat over C[[s]] (the defining homogeneous polynomial is not divisible by s and the quotient has no s-torsion), smooth generically, and has the same corank-one special quadric. Therefore those three written hypotheses alone do not imply **nontrivial** quadratic monodromy. SGA7 XV2.2.5(D) describes a character of order1 or2; regular/simple discriminant hypotheses in the Picard–Lefschetz theorem distinguish the ramified case. No manuscript statement about total-space regularity is silently inserted.

## R6. Nested tori and the missing maximality hypothesis

Over C put G=SL₄ and D its diagonal torus. Let R be the image of t↦diag(t³,t,t⁻¹,t⁻³). Let T be the kernel in D of the character a=(1,2,−7,4). Characters of D are Z⁴/Z(1,1,1,1). The gcd of a_i−a₄ is gcd(−3,−2,−11)=1, so a is primitive and T is a connected two-dimensional torus. Since a·(3,1,−1,−3)=0, R⊂T. The four R-weights are distinct; the certificate checks that the four restricted T-weights are distinct as well, by exhibiting nonzero3×3 minors of(1,a,e_i−e_j). Thus C_G(R)=C_G(T)=D.

Any normalizer of either torus normalizes its centralizer D. Therefore the Weyl quotients are exactly the permutations in S₄ preserving the corresponding one-dimensional cocharacter/character data. For R, a permutation must take r to r or−r; only identity and reversal(14)(23) do. For T, a permutation takes the primitive character a to ±a modulo the all-ones vector; checking all24 possibilities gives only identity. The certificate is exhaustive because the preceding centralizer argument reduces the full algebraic normalizer to S₄. Hence W(R)=C₂ and W(T)=1, contradicting the literal unrestricted subquotient claim.

If T is maximal, the standard repair is valid. For g normalizing R, both T and gTg⁻¹ are maximal tori of C_G(R)⁰; after conjugating by an element of C_G(R)⁰ they coincide. This yields a surjection from the subgroup of N_G(T) preserving R onto N_G(R)/C_G(R), with a quotient of the appropriate subgroup of W_G(T). The printed SGA3 XII2.3 proof explicitly uses this maximality. The printed statement repeats the missing hypothesis, so publication alone does not validate its literal form.

## R7. A smooth G_m-to-G_a family

For R=Z_(3), take G=Spec R[x,(1+3x)⁻¹]. Set x*y=x+y+3xy. Then1+3(x*y)=(1+3x)(1+3y), which proves closure and associativity; identity is0 and inverse is−x/(1+3x). Smoothness follows because G is an open subscheme of A¹_R. Over Q, u=1+3x is a coordinate giving G_m. Modulo3 the inverted function is1 and the law is addition, giving G_a. Thus reductive rank drops from1 to0. There cannot be a torus over the whole local base restricting to the generic maximal torus, since the rank of a torus is locally constant and G_a has no nontrivial torus. This explains the later inserted constant-rank conditions.

## R8. Delzant's augmentation filtration and degree-two symbol

Let GW(F) be the Grothendieck–Witt ring of a field of characteristic≠2, J its rank-zero ideal, W(F) its Witt quotient and I the even-rank ideal. Put h=〈1〉+〈−1〉. For any q, hq=rank(q)h; in particular h²=2h. The kernel of GW→W is Zh, with rank(h)=2. Thus its intersection with J is0. Any even-rank representative q of a Witt class has q−rank(q)h/2 in J and the same Witt image. Changing q by mh changes this expression by mh−mh=0. This proves the multiplicative bijection J≅I and consequently J^r/J^(r+1)≅I^r/I^(r+1).

For d_a=〈a〉−1 and d_b=〈b〉−1, their product is〈ab〉−〈a〉−〈b〉+1. Writing u=(a),v=(b) in H¹(F,Z/2), its total Stiefel–Whitney class through degree2 is (1+u+v)/((1+u)(1+v))=1+uv+terms of degree≥3. The exact polynomial certificate performs this expansion over F₂. Products of three rank-zero line elements have no terms below degree3 by the same expansion/finite-difference rule. Therefore Delzant's degree-two graded map is the cup-symbol map under the explicit filtration identification; the comparison is not merely a similarity of notation.

For a real form with r negative squares, w=(1+u)^r. The coefficient of u^(2^j) is the j-th binary digit of r (Lucas' identity, also immediate by factorizing(1+u)^r in F₂[u]). Rank and all these coefficients recover the signature. The finite certificate verifies r=0,…,64; the binary factorization proves all r. This explains the real-place part of the number-field classification and why the rank coordinate is indispensable.

For the Clifford-normalization alarm, use the full ungraded Clifford algebra of q=〈a,b,c,d〉. The generators e₁,e₂ give(a,b); the commuting generators e₁e₂e₃,e₁e₂e₄ have squares−abc,−abd and anticommute. Hence [C(q)]=(a,b)+(−abc,−abd). For q=〈−1,1,1,1〉 over R, both symbols split, while for p=〈1,1,1,1〉 the second symbol is(−1,−1), the quaternion class. Thus [C(q)]−[C(p)] is nonzero but w₂(q)=0. This refutes only the **raw** relative-full-Clifford reading. A normalized invariant u(q) with a discriminant correction may equal w₂; the commentary does not replace Delzant's definition by the raw one.

## R9. The abstract Lemma A on ringed spaces

Take X=RP² with its usual compact topology and structure sheaf the constant sheaf C. This is a ringed space, with noetherian field stalks; O_X is coherent because matrices of locally constant functions have locally constant finite-dimensional kernels. Every coherent O-module is a finite-rank local system. Its representation of π₁(X)=Z/2 splits into trivial and sign summands because2 is invertible in C.

The cellular cochain complex for either one-dimensional representation is C→C→C with differentials g−1 and1+g. For g=1 these are0,2; for g=−1 they are−2,0. In both cases H¹=0. Direct sums give H¹(X,F)=0 for every coherent F. Yet the nonzero sign local system has Γ(X,F)=0, while A=Γ(X,O)=C and the functor M↦M⊗C O produces only trivial local systems. It is not essentially surjective. This checks **every** hypothesis of the unqualified main Lemma A at c55:6 lines148–168 and refutes its conclusion.

The separate marginal variant at line172 assumes a basis of quasi-compact neighbourhoods and only objects with global presentations. It is a different statement; this counterexample is not claimed to refute it. In particular RP² does not have a basis of compact open neighbourhoods. The later condition(β), generation of every finitely presented sheaf by global sections, supplies exactly what the main argument lacks.

Under coherent O, compact X, H¹ vanishing and global generation, every coherent F has a finite global presentation: choose finitely many generating global sections by compactness, then generate the coherent kernel similarly. Taking Γ is exact on these sequences. It follows directly that Γ(F) is finitely presented over A and that the unit/counit of the tensor–sections adjunction are isomorphisms. Flatness of stalks and coherence of A follow by testing kernels of finite matrices. This is the corrected version; the source's undefined word “pur” does not suffice to identify its maximal-ideal corollary.

## R10. Cote55's torus and dimension counterexamples

The literal lattice is generated by e₁,ie₁,e₂,e₁+ik e₂ for real irrational k. Subtracting the first generator from the fourth is an integral unimodular basis change and gives ik e₂. Thus the quotient is the product C/(Z+iZ)×C/(Z+ikZ), hence a projective complex torus. In its proposed proof, choose x=e₂: the first complex coordinate is zero, so the argument asserting that a scalar c must lie in Q(i) cannot be applied.

A **different**, explicitly editorial lattice realizing the stated existence goal is Λ=〈(1,0),(i,0),(0,1),(k,i)〉 with k real irrational. Its real determinant is1, so it is discrete cocompact. Projection to the second coordinate gives a surjection to C/(Z+iZ), with elliptic kernel C/(Z+iZ). If a complementary elliptic subtorus existed, its tangent line would be the graph of α:C→C. It would contain two lattice vectors(αz,z),(αz′,z′) with real-independent z=c+id,z′=c′+id′ in Z[i]. Write αz=u+kd and αz′=u′+kd′, where u,u′∈Z[i]. Eliminating α gives k(dc′−d′c)=u′z−uz′∈Q(i). The coefficient on k is a nonzero integer, so k∈Q(i)∩R=Q, a contradiction. Poincaré complete reducibility would supply such a complement if this torus were an abelian variety. This proves nonprojectivity of the alternative, not a change to the unread ink.

The reused dimension Proposition5 has a separate exact published erratum: its equidimensional+equicodimensional+catenary condition is too weak. Let A=k[x,y,z,w]/(xz,xw), localize away from the union P=(x−1,y), Q=(x,z,w), and call the resulting spectrum X. The minimal primes are(x) and(z,w). The component(x) is a localization of k[y,z,w] with only the retained maximal prime(z,w), of height2. The component(z,w) is a localization of k[x,y] with retained primes(x−1,y) of height2 and(x) of height1. Hence both components have dimension2, both maximal points of X have height2 (Q has height2 along the first component), and X is catenary because it is essentially of finite type over a field. Nevertheless the saturated chain(z,w)⊂Q has length1, while(x)⊂(x,z)⊂Q has length2. It is not biequidimensional. Requiring **each irreducible component** to be equicodimensional is the repaired condition in Pilloni–Stroh, ExposéXIV Lemma2.4.2 and its footnote, which credits Gabber and independently Chen's letter of26September2005.

Finally, the local height bound on c55:3 uses a faulty proof phrase: a maximal ideal need not be generated by dimA elements. Choose a system of parameters generating an m-primary ideal instead. If B is noetherian local over A and B/m_AB is zero-dimensional, the extended parameter ideal is m_B-primary; Krull's height theorem gives dimB≤dimA. This repairs the proof without imposing regularity. It does not justify the literal assertion that m_A itself has that many generators.

## R11. A direct negative answer to the coherent-ring elimination question

Let R=k[[u,v]], m=(u,v), and A=∏_(n≥1)R. This A is coherent. Indeed, for a finite row R^r→R its image I is either0 or a finite ideal of depth at least1 in the regular local ring R of dimension2. The regular-local resolution theorem gives pd(I)≤1, so its kernel K is finite projective, hence free, of rank at most r. For a row over A the kernel is the product of the coordinate kernels. Choose bases and pad them by zeros to r elements in every coordinate. The r resulting elements generate the product kernel. The finite-row criterion for coherence therefore applies to A. Stacks tag00O7 is the exact regular-local input, not an assertion that an arbitrary product of coherent rings is coherent.

In A[T], put U=(u)_n, V=(v)_n, W=(v^n)_n and J=(U−VT,W). The ideal has two generators. In coordinate n its image is J_n=(u−vT,v^n)⊂R[T]. The quotient map

R[T] → (k[v]/(v^n))[T], u↦vT,

is well-defined on formal power series, because all terms of total(u,v)-degree≥n vanish. A series f=Σc_ab u^a v^b maps to Σ_(d<n)v^dΣ_(a≤d)c_(a,d−a)T^a. Independence of these monomials shows its restriction to R has kernel m^n. Conversely, each generator u^a v^(n−a) of m^n lies in J_n, by the identity u^a−(vT)^a=(u−vT)Σ_(j=0)^(a−1)u^(a−1−j)(vT)^j. Thus J_n∩R=m^n exactly.

Projection of J∩A to coordinate n is all of m^n: multiply any finite polynomial representation in coordinate n by the coordinate idempotent e_n and lift its coefficients to A. There is no requirement of a degree bound uniform in n for these **individual** lifts. If J∩A had r generators, every coordinate image m^n would have at most r generators. But dim_k(m^n/m^(n+1))=n+1. This is impossible. Therefore the authored contraction claim fails, and so does the bounded-degree claim already in degree0. The argument was independently checked by the agent reviewing cotes46/53, including the product-kernel and idempotent-lifting steps.

This does not claim novelty. Literature searches found Yengui's2011 preprint, Theorem2 and Corollary3: for valuation/Prüfer domains, finite generation of all such contractions is equivalent to dimension at most1. These domains are coherent, so dimension>1 already supplies a published negative answer in the broader multivariable formulation. The one-variable monic case is positive in Lombardi–Schuster–Yengui, Theorem3. The direct product example above is retained because it makes the precise obstruction in the manuscript question explicit and independently checkable.
