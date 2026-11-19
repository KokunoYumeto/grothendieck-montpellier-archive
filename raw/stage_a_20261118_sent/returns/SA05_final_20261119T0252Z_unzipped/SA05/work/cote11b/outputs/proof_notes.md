# Mathematical checks for the cote11b contribution

Date: 2026-11-19. These are current reconstructions, not diplomatic additions to the manuscript. A theorem read in an external source is distinguished from a proof completed here. Computation certificates are in `programs/checks.py` and `outputs/checks.json`; they check exact arithmetic and finite models, not arbitrary geometric theorems.

## 1. Correspondences and completion

For smooth projective varieties X, Y, Z over a field, work with rational Chow groups, or an oriented cohomology theory having the required proper pushforwards, pullbacks, product, projection formula and Cartesian base change. Write correspondences in source-first order in this paragraph. Define

\[
\beta\circ\alpha=(p_{13})_*(p_{12}^*\alpha\,p_{23}^*\beta).
\]

Their action is \(T_\alpha(x)=p_{2*}(p_1^*x\,\alpha)\). On X×Y×Z, projection formula and base change give

\[
T_\beta T_\alpha(x)=p_{3*}(p_1^*x\,p_{12}^*\alpha\,p_{23}^*\beta)=T_{\beta\circ\alpha}(x).
\]

The source uses target-first notation A(I′;I). Accordingly its displayed factor ordering must be translated before using this formula. In a graded theory, changing the order of homogeneous factors multiplies the expression by the associated Koszul sign; it is not legitimate to combine formulas using opposite order conventions. Pro11/046 line129 leaves an expression on the product of the outer factors after p31*, where the equality still needs its outer β″ pushforward to the target factor. This is a type check, not a decision about the ink.

For a third correspondence γ, both associations reduce, on X×Y×Z×W, to

\[
p_{14*}(p_{12}^*\alpha\,p_{23}^*\beta\,p_{34}^*\gamma).
\]

This proves associativity with unchanged factor order; the only ingredients used are the specified base-change and projection identities. For the diagonal, projection formula gives
\(p_{2*}(p_1^*x\,\Delta_*1)=p_{2*}\Delta_*(\Delta^*p_1^*x)=x\).
The same calculation on three factors gives both unit laws. Stacks 45.3.1 and 45.3.3 were read, including their proofs; they provide the exact Chow-theoretic reference.

The finite P¹ certificate uses H*(P¹,Z)=Z[h]/h², top integral ∫h=1, and Δ=h⊗1+1⊗h. It checks all16 products in a four-element correspondence basis and all64 associativity triples. This is an exact illustration, not a substitute for the four-factor argument.

Idempotent completion is an additional construction. For an idempotent e and integer m, define (X,e,m), with morphisms cut out by the source and target idempotents. Its identity is e. If q=eqe and q²=q, the same correspondence q gives inclusion and projection between (X,q,m) and (X,e,m), with composites q and the projector q on the latter. This verifies splitting directly. Adding finite sums and formally inverting the Tate factor are separate steps. Stacks45.4 verifies the complete construction. The sheets do not perform all these steps.

Grothendieck's 1969 *Standard conjectures on algebraic cycles* was read in rendered images, all seven printed pages193–199. Its §2 uses algebraic correspondences and diagonal Künneth components; §3, p196, explicitly describes an algebraic operator by pullback, multiplication by a cycle class and Gysin pushforward. It does not give the full correspondence-category proof in §1. This exact distinction replaces an initially too broad locator in the working draft.

## 2. Diagonal tables, partitions and excess

Assume X is connected, smooth and projective over C, of positive complex dimension d, and use rational cohomology. Let y be the normalized class of a point. The same discussion works in a classical Weil cohomology with the usual orientation and trace. The square y² is zero by degree. For the diagonal immersion Δ, its normal bundle is TX, so
\(\Delta^*\Delta_*1=c_d(TX)\), and \(c_d(TX)=\chi(X)y\) in top cohomology. Hence
\(\Delta_{12}^2=\chi(X)y_1y_2\).
Intersecting two independent equality constraints in X³ gives the small diagonal. Restricting a point constraint to that diagonal gives the product of all point classes. Intersecting one repeated equality constraint contributes the Euler class. Two independent redundant constraints give a product of two top-degree classes on X and vanish. These facts give each two- and three-factor identity on11/051.

The precise Chow statement uses c_d(TX), which need not be rationally equivalent to χ(X) times an arbitrarily chosen point. The cohomological normalization is therefore a real hypothesis. Stacks45.7.8 was read for the diagonal/Euler equality; Stacks42.54.3–5 was read for the excess formula and the definition of its excess normal bundle.

For two unmarked partitions R,R′ of k coordinates, suppose their join is the single-block partition. Let s,s′ count **nonempty** blocks. Their equality loci have tangent spaces TX⊗U_R and TX⊗U_R′ along the small diagonal, where U_R,U_R′ are the corresponding constant-coordinate subspaces of a k-dimensional trivial vector space. Their intersection is TX tensored with the diagonal line. Therefore the excess quotient is

\[
TX\otimes \left(k^k/(U_R+U_{R′})\right)\simeq TX^{\oplus e},\qquad e=k+1-s-s′.
\]

In particular e≥0. Excess0 gives the small diagonal, excess1 gives χ(X) times the total point class, and e≥2 vanishes by degree. For a disconnected join, apply this on each joined block and multiply. A point mark pins its joined block; two occurrences of a point factor on that same connected block give y²=0 in the intersection product. This concerns cycle classes, and does not say that the underlying set-theoretic intersection is empty.

The source explicitly includes ∅ as a partition block on11/055. If s=cardR includes it and no block is marked, the locus is X^{s−1}, not X^s. The smallest counterexample is I={1}, R={∅,{1}}: all listed partition axioms hold, but the locus is X. No change to the transcription is made.

For X=P¹ the exact certificate gives Δ12=h1+h2; the advertised list is therefore not always a linearly independent basis. P¹ is smooth, projective and connected, has Künneth and full Poincaré duality, and is allowed by the preceding manuscript examples. A formal diagram algebra can still have a basis before realization. The four-factor loop Δ12Δ23Δ34Δ41 equals 2h1h2h3h4, matching χ(P¹)=2.

For closure under a coordinate projection, integrate the forgotten factor. A generator not involving it integrates to zero since ∫1=0 for d>0; a point-marked factor integrates to1; an equality edge to a retained coordinate also integrates to1 by the diagonal identity. More complicated products first reduce by the preceding product rule. External products and permutations merely change indices. This proves the stated cohomological closure and its resulting correspondence composition. It does not restore the cancelled extraordinary-pullback claim.

Hua's November2026 preprint §1, Theorem1.1, its partition corollary and the one-factor stability paragraph were opened and read. They prove an exact algebraic multigraph rule under explicitly ungraded commutative diagonal identities. The paper itself excludes the geometric excess proof and the odd/Koszul model from that formalization. We read its written proof; no Lean executable or certificate was run. It does not prove universal independence after geometric realization, nor supply the kernel of every realized tautological algebra.

## 3. Mumford's reused configuration typescript

The attribution to Mumford is mathematical/textual, not an inference that Grothendieck authored printed versos. The source chart conditions specify a projective frame and nonzero determinants. Given an ordered basis of projective points, choose vector representatives and a matrix carrying that basis to the coordinate points. The additional frame point fixes the ratios of the column scalings; multiplying the whole matrix by a scalar is immaterial in PGL. Thus the projective transformation is unique. Its entries and the remaining normalized coordinates are ratios of minors whose denominators are nonzero on the specified chart. This checks the structural inverse-map argument. It does **not** certify every OCR symbol in the displayed φ/ψ formulas, and typescript pages3.5 and3.16 remain absent.

If U_R≅PGL×A_R equivariantly and V⊂U_R is invariant open, membership of (g,a) is equivalent to membership of (1,a). Pullback along the identity slice shows B={a:(1,a)∈V} is open, hence V=PGL×B. This proves Corollary3.2 without a quotient existence theorem.

For a full-dimensional finitely generated closed cone C in a finite-dimensional real vector space, separating an interior point from C is impossible with a **nonzero** supporting functional of the displayed sign. The zero functional satisfies the literal weak inequalities for every point. Thus C=R²_{≥0}, x=(1,1), ℓ=0 refutes the statement with the missing condition. If the cone lies in a proper subspace, the corresponding assertion must be phrased using relative interior in its span.

Let λ0≤⋯≤λm with Σλi=0. Define vβ to have first β+1 coordinates −(m−β) and the remaining m−β coordinates β+1. Then

\[
\lambda=\sum_{\beta=0}^{m-1}\frac{\lambda_{\beta+1}-\lambda_\beta}{m+1}v_\beta.
\]

The right side has successive differences λ_{j+1}−λ_j and total sum0, so it equals λ. The coefficients are nonnegative. This proves the formula for allm; the saved symbolic checks for m1..8 check the implementation.

The greedy minimum-weight basis assertion is a linear-matroid fact. Process columns in nondecreasing weight and retain a column exactly when it raises span dimension. After each weight threshold, the selected columns have cardinality equal to the rank of that prefix. Any independent basis has at most that many elements in the prefix. Writing total weight as a constant minus a sum of nonnegative weight gaps times these prefix cardinalities shows that the greedy basis has minimum weight. Equal weights cause no change to the argument. This is the flag step used on11/056; it does not fill the missing last typescript page.

The opened1982 edition of GIT contains the chart and R-partition argument and Theorem3.8. Its OCR around Proposition3.6 is incomplete, so an exact character-by-character monomial collation is not certified. Theorem3.8's stable configuration quotient, local PGL triviality and ample descended tensor polarization match the source. EGAII4.5.2, pp83–84, was actually opened and read: affine nonvanishing opens covering the base characterize ampleness. This is the ampleness citation used by the continuation on11/052.

## 4. Quadrics, cones and vanishing cycles

### Integral quadric lattice

For a split smooth quadric Q^D, let h be its hyperplane class and d=floor(D/2). The cell basis consists of h^i for0≤i≤d and linear-subspace classes l_i for0≤i≤d, with the duplicate middle degree in even dimension interpreted as the two ruling classes. The relevant relation is h^{d+1}=2l_{floor((D−1)/2)}, with h·l_i=l_{i−1}; in even dimension l_d² is1 or0 in the top generator according to D≡0 or2 mod4. These are the exact relations read in Karpenko's Theorem1.10 and its proof. The scripts construct all integral hyperplane matrices for D1..8 from them and compute kernels/cokernels.

For Q^{2ν}, ν≥1, the middle ruling basis α,β satisfies h^ν=α+β and λ=α−β. The change-of-basis matrix has determinant−2 and Smith invariants1,2. Its inverse is half that matrix. Therefore (h^ν,λ) is an index2 sublattice, and (h^ν+λ)/2=α is integral. Moreover λ maps to twice a generator of the quotient by Zh^ν. A statement that λ itself generates that integral quotient needs correction or coefficients with2 inverted.

The parity of the ruling intersection gives λ²=(−1)^νh^{2ν} and hλ=0. For Q²=P¹×P¹, with a²=b²=0, h=a+b and λ=a−b, this is λ²=−2ab. This is a complete counterexample to a uniform positive λ-square. The ring, variety and generator convention are all checked, so it cannot be dismissed as a numerical experiment. Restriction from Q^{2ν} to Q^{2ν−1}, and pushforward into Q^{2ν+1}, send the two ruling classes to the same class; hence they kill λ. A hyperplane pushforward raises codimension by1.

### Punctured cones and coefficients

The punctured cone E over a smooth projective X is the nonzero total space of O_X(−1). Its Gysin map is multiplication by −h. Replacing it by h changes chosen signs but not kernels or cokernels. For a connected full cone C, contraction gives H⁰(C,Z)=Z and no positive cohomology, and the long exact sequence of (C,E) identifies H_a^i(C,Z) with reduced H^{i−1}(E,Z). In particular degrees0 and1 vanish when E is connected. An unmodified degree0 identification with a shifted vanishing group would lose the unit.

For Q^D the integral Gysin sequence and the matrices above give:

| D | Nonzero H^i(E,Z) |
|---|---|
| odd D>0 | Z in degrees0 and2D+1; Z/2 in degreeD+1 |
| even D>0 | Z in degrees0,D,D+1,2D+1 |

The odd source table places torsion in2ν−2 instead of2ν when D=2ν−1. The even source table puts its lower middle free group in2ν−1 instead of2ν. Q¹ with hyperplane bundle O_{P¹}(2), and Q²=P¹×P¹, already detect the two errors. These are integral/Z₂ interpretations. For a finite coefficient ring A with2-torsion, the adjacent kernel A[2] appears as well as A/2A. For example the odd-dimensional cone has H^D(E,A)=A[2], H^{D+1}(E,A)=A/2A. A literal finite-coefficient table cannot be imported from the integral one. The source μ/M notation is an ink question.

### Affine quadric and orientation

For U^D={Σz_i²=1}⊂C^{D+1}, write z=x+iy. The equations are |x|²−|y|²=1 and x·y=0. The map (x,y)↦(x/|x|,y) identifies U smoothly with TS^D, with inverse (u,v)↦sqrt(1+|v|²)u+iv. Scaling v retracts it onto S^D. Hence H*(U,Z) is Z in degrees0,D for D>0, and Poincaré duality gives compact supports in D,2D. D=0 gives two points, so overlapping degree slots must not be read as a single copy ofZ.

The compact-to-ordinary middle map is the self-intersection of the vanishing sphere. The normal bundle is JTS^D. Comparing the interlaced complex orientation (e1,Je1,…,eD,JeD) with (e1,…,eD,Je1,…,JeD) contributes (−1)^{D(D−1)/2}; the Euler number of S^D is2 for evenD and0 for oddD. For D=2ν this is (−1)^ν2. Deligne1974 §4.1's table gives2,0,−2,0 forD mod4 and confirms this orientation convention. A bare positive2 with freely chosen generators in the source is not by itself a decided sign mistake.

### Regularity and inertia

Consider the projective family over R=C[[t]]:
\[
X:\quad x_0^2+x_1^2+x_2^2=t^2x_3^2\subset\mathbf P_R^3.
\]
R is a complete strictly henselian DVR of characteristic0. The equation is monic in x0, so the graded homogeneous coordinate ring is R-flat; thus the projective family is flat. It is projective. The generic quadric is smooth. The special fibre is a rank3 quadric surface with a unique ordinary quadratic vertex. Over K=C((t)), the coordinate change u3=tx3 identifies the generic fibre with the constant smooth quadric Σ_{i=0}²x_i²=u3². Its cohomology therefore has trivial inertia. The total space is singular at the special vertex: all partial derivatives, including the t derivative, vanish there. These checks are both stated here and recorded symbolically in the saved output.

Thus the source's flat/projective/one-singular-special-point assumptions do not imply nontrivial sign monodromy. The regular ordinary smoothing, with residual characteristic≠2 and prime-to-residual-characteristic coefficients on which−1≠1, has the usual parity character. Deligne1974 §4.2 explicitly assumes the total space regular, and §4.3 gives the local character. An even ramified base change can kill that character. The source's final unspecified purity phrase is not turned into a theorem about weights or middle extension.

### Contracting comparison

Braden2003 Lemma6 was read with its precise setup and proof. Put the positively weighted affine space into E=P(W)\P(W_+) with W=W_+⊕W_- and dimW_-=1; then B=P(W_-) is the fixed point. A closed equivariant cone C⊂E and the closed pushforward of a weakly equivariant constructible complex give the desired costalk/compact-support comparison. This verifies the source's expected comparison for the contracting cone under the coefficient and equivariance assumptions of that lemma. It does not claim the comparison for arbitrary nonequivariant sheaves.

## 5. Group schemes and the Weyl counterexample

The SGA3XII theorem and corollaries were compared with their actual printed statements in the2008 retypesetting; the1970 volume and attribution were checked in publisher metadata. The rank theorem is for smooth affine group schemes of finite presentation. Local constancy of reductive rank is not removable from the local maximal-torus conclusions. If at s the unipotent rank is0, write r=ρr(s)=ρn(s). Lower semicontinuity ofρr and upper semicontinuity ofρn give, after shrinking, r≤ρr(t)≤ρn(t)≤r. This proves the stated neighbourhood conclusion.

If R commutes with a maximal torus T and the product-image theorem applies, the image of R×T is a torus containing T and hence equalsT. This proves R⊂T; representability of the image is a cited structural input, not proved here. The unique-torus consequences are then formal descent once local existence is known. Reductive-centre results were checked against their exact affine-fibre and connected-fibre hypotheses; no theorem is inferred from the ill-typed intersection on56/023.

### Explicit degeneration

Over Z_(3), let G=Spec R[x,(1+3x)^{-1}], with law x⋆y=x+y+3xy. Its inverse is−x/(1+3x), identity0, and associativity follows by expansion. The coordinate u=1+3x converts the generic law into multiplication and identifies G_Q with G_m; modulo3 the law becomes addition and G_F3=A¹=G_a. G is an open subscheme of A¹_R and thus smooth. The source only asserts existence; this model is an earlier-run idea independently checked here.

### Nested tori without maximality

Let G=SL4(C), with diagonal maximal torus D. In X_*(D)={v∈Z⁴:Σv_i=0}, take v=(3,1,−1,−3) and the one-dimensional connected torus R it defines. It is primitive. In X^*(D)=Z⁴/Z(1,1,1,1), take a=(1,2,−7,4), and let T=ker(a:D→G_m). Differences from the last coordinate are−3,−2,−11, of gcd1, so the character is primitive and T is connected of dimension2. The pairing a·v=0 proves R⊂T.

All four coordinate weights restrict distinctly to R since the entries ofv are distinct. They restrict distinctly toT since no e_i−e_j is a rational multiple ofa modulo the diagonal vector. Therefore C_G(R)=C_G(T)=D. Any normalizer of either torus normalizes its centralizerD, so its Weyl quotient is a subgroup of N_G(D)/D=S4. A permutation preserves R exactly when it carries the line Qv to itself; the only possibilities are identity and reversal. A permutation preserves T exactly when it carries Qa to itself modulo the diagonal. Since Σa_i=0, the possible diagonal correction is0. The multiset{1,2,−7,4} admits neither a nontrivial preserving permutation nor its negation. Thus W_G(R)=C2 and W_G(T)=1. The script checks all24 permutations and the stated primitivity/centralizer tests exactly.

A nontrivial group cannot be a subquotient of the trivial group. This refutes the unrestricted nested-torus lemma as transcribed and as stated in the checked SGA3XII retypesetting. The source's proof invokes a maximal-torus conjugacy step that does not hold for an arbitraryT.

For the corrected assertion, assume T maximal inG. For n∈N(R), T and nTn⁻¹ are maximal tori of C_G(R)⁰. Conjugate the second to the first by c∈C_G(R)⁰. Then cn belongs to N(R)∩N(T) and represents the same element ofW(R). Thus the subgroup (N(R)∩N(T))/C(T) ofW(T) surjects ontoW(R). This is the precise refinement C2049, not an invented source reading.

## 6. Delzant's offprint and the degree-two questions

The source gives the Grothendieck–Witt ring, retaining rank. Its offprint author is Antoine Delzant, explicitly named in the supplied transcription at 56/036 line1785 and corroborated by the bibliography. An earlier draft of this audit had misreported that first name; the final direct source recheck removed the resulting false alarm. The transcription has not been changed.

Let h=⟨1,−1⟩. For charF≠2, the quotient GW(F)→W(F) has kernel Zh and rank(h)=2. Its restriction J=ker(rank)→I=ker(dim mod2) is injective because no nonzero multiple ofh has rank0. It is surjective: an even-rank representative q has the rank-zero lift q−(rankq/2)h. Since hq=rank(q)h, this is compatible with multiplication in the ideals. Consequently J^r maps isomorphically toI^r.

Write d_a=⟨a⟩−1, and let u=(a),v=(b) be Kummer classes. Whitney multiplication on virtual differences gives
\[
w(d_ad_b)=\frac{1+u+v}{(1+u)(1+v)}=1+uv+\text{terms of degree≥3}.
\]
The equality uses characteristic2 coefficients. A three-factor product has no positive term of degree≤2. J is additively generated by thed_a, so J³ is killed in those degrees. The exact truncated-polynomial computation is saved. Milnor1970 §3, Lemma3.2 and §4, Theorem4.1 were read; the source itself identifies Delzant's classes as images of Milnor's symbols.

For charF≠2, μ₂ is the constant groupZ/2, and the Kummer sequence with Pic(SpecF)=0 identifies H²(F,μ₂) with Br(F)[2]. Milnor's degree2 comparison identifies K₂^M(F)/2 withI²/I³. Merkurjev's1981 theorem then gives the isomorphism toBr(F)[2]. The original Russian article's theorem on printedp543 and the later author's proof, Theorem2.2, were both opened. This settles both injectivity of Delzant'sJ²/J³ arrow and generation of2-torsion Brauer classes by quaternion symbols. The exact map is checked, so this is stronger evidence than merely citing a related theorem name.

Over R, if a quadratic form hasn negative squares, its total class is(1+x)^n inF₂[[x]], and its rank supplies the positive-square count. The factorization
\((1+x)^n=\prod_j(1+x^{2^j})^{n_j}\)
recovers the binary digitsn_j ofn. The saved tests for0≤n≤64 check the arithmetic, and the displayed factorization proves it for all nonnegativen. For virtual classes with identical rank and total class, add the same genuine form so both become genuine; their invariants remain equal. Finite local fields are classified by rank, determinant and Hasse invariant; the number-field local-global theorem then gives the offprint's injection. Milnor1970 explicitly records Delzant's number-field result. This does not assert injectivity for arbitrary fields.

The bare positive-class map would fail even overR: ⟨1⟩ and⟨1,1⟩ both have total class1, but unequal rank. The source's own final theorem retains rank; the untilded diagram target is therefore a reading alarm, not a refutation of that final theorem.

The Clifford comparison is more delicate. The offprint normalizes relative to the same-rank unit form and distinguishes full versus even Clifford algebras. Its cited Springer1959 text could not be opened through the located DOI. Milnor's exact statement confirms the relationship to the Hasse–Witt invariant, but does not by itself certify every descent normalization in the offprint. This residual verification is explicitly left documentary; no claim of an independent full proof is made.

## 7. Reused finite and affine reflection sheets

These are not original motifs conjectures. Coxeter1934 was opened for the finite simplicial chamber theorem, the presentation theorem and the orthogonal product reduction. Bourbaki1968 publisher/author bibliography confirms the corresponding subject and edition, but does not identify the exact number383 typescript. All arguments below concern the essential Euclidean subspace W; an unconstrained fixed factor would invalidate a claim that every pair of chamber vectors has nonnegative scalar product.

The essential reduction is E=E^G⊕W. Each reflection fixes E^G and restricts to a reflection onW. An element trivial onW is also trivial onE^G and hence onE. Conjugating a reflection carries its fixed hyperplane to the conjugate hyperplane, givingg s_H g⁻¹=s_{gH}.

For a finite reflection group, the local chambers around a pointx are separated exactly by the reflecting hyperplanes containingx: choose a small ball meeting no hyperplane not throughx. Reflections in these hyperplanes connect their adjacent chambers, so they act transitively on the local chambers. Ifg fixesx, bothC andgC belong to this local family. The simply transitive global chamber action then identifiesg with a word in those reflections. This proves the point-stabilizer assertion. A closed chamber has a unique representative of each orbit; uniqueness of the carrying group element fails on walls precisely by these stabilizers.

For inward unit simple normals with Gram matrixG, the correct angle identity is G_ij=−cos(π/m_ij). It does not transfer unchanged to the dual vectors: their Gram matrix isG^{-1}. In typeA3,
\[
G=\begin{pmatrix}1&-1/2&0\\-1/2&1&-1/2\\0&-1/2&1\end{pmatrix}.
\]
The dual-vector cosine for indices1,3 is1/3, whilem13=2 andcos(π/2)=0. This is a finite, essential, real orthogonal reflection group, satisfying every relevant hypothesis. The exact inverse and normalized quotient are saved.

The nonnegative-angle corollary nevertheless follows by elementary linear algebra. If b is entrywise nonnegative and Gx=b, write x=x_+−x_- with nonnegative disjoint-support parts. Were x_- nonzero, then x_-^T b=x_-^T Gx_+−x_-^T Gx_- would be strictly negative: the first term is nonpositive because the off-diagonal entries ofG are nonpositive, and the second is positive by positive definiteness. This contradicts x_-^T b≥0. Thus x≥0 and every entry ofG^{-1} is nonnegative. Vectors in the closed essential chamber are nonnegative combinations of the dual simple vectors, so their inner products are nonnegative. This repairs the proof without adopting the false equality.

For the affine case, assume a proper discrete action by Euclidean isometries. If infinitely many distinct mirrors meet a compact ballK, their distinct reflections each fix a point ofK, so eachg satisfiesgK∩K≠∅. Properness allows only finitely many suchg, a contradiction. This completes the local-finiteness proof cut off on12/126. An invariant orthogonal decomposition places each rank-one reflection normal in one summand, since its rank-one orthogonal projection commutes with the summand projection. The reflection therefore acts trivially on the other summands; the generating subgroups commute, intersect trivially and generateG. A pointwise fixed factor must be retained.

## Limits of these checks

No original manuscript image was supplied, so no diplomatic reading was changed. Printed-source images were used only for bibliographic/theorem checking. Exact finite certificates do not replace the general arguments above. SGA7 chapter metadata, Bourbaki edition metadata, and the inaccessible Springer1959 original are not represented as proofs read. No Lean verification from earlier runs or from Hua2026 was executed in this run.
