# Cote 44 and integral Lefschetz investigation

Run HODGE_SIGN, agent `/root/arithmetic_sl2`; model GPT-6 Astra Pro; effort setting not exposed. Date 2026-11-21 (UTC). This note accepts Alpöge's RH/Dirichlet-GRH as theorems under the user's convention. It does not infer further theorem statements from filenames.

## AR-01 — The literal high-codimension formula of cote 44 Th. 5 is false

**Statement (counterexample).** Work over an algebraically closed field k of characteristic zero. There is a smooth projective fourfold X with a Lefschetz pencil of hyperplane sections all of whose fibres are geometrically integral, and an integral codimension-two cycle class Z with restriction zero in CH²(Y) on the generic member Y, but Z²=3. Consequently the assertion of ARCHIVE_44_scan004.tex, Th. 5, that the height pairing of the restrictions equals (+1)Z² for m=2, is false under its written hypotheses. H9(a), including its assertion that geometric integrality of fibres removes the need for vertical corrections, is also false in this scope.

**Proof.** Take X=P²_k×P²_k, write a,b for the two hyperplane classes, and use the Segre polarization H=a+b. Its Chow ring is Z[a,b]/(a³,b³), with deg(a²b²)=1. Put Z=a²−ab+b². Then HZ=0 and

Z²=a⁴−2a³b+3a²b²−2ab³+b⁴=3a²b²,

so deg Z²=3.

Consider the hyperplane pencil

Y_[λ:μ]: λ(x₀y₀+x₁y₁+x₂y₂)+μ(x₁y₁+2x₂y₂)=0.

The coefficient matrix is diag(λ,λ+μ,λ+2μ). It has rank three except at [λ:μ]=[0:1],[-1:1],[-2:1], where it has rank two. A bilinear form of rank at least two is irreducible: a factorization of a bihomogeneous polynomial of bidegree (1,1) into positive bidegrees would necessarily be a product of a form of bidegree (1,0) and one of bidegree (0,1), and hence have rank one. Thus every member is geometrically integral.

A rank-three member is smooth, since its two projective gradients cannot vanish. A rank-two diagonal member has just one singular point, namely (e_i,e_i) for the vanishing diagonal coefficient. In affine coordinates x_i=y_i=1 around it, its equation is the sum of two nonzero scalar multiples of x_jy_j, j≠i, a nondegenerate quadratic form in four variables. Each singular member therefore has one ordinary quadratic singularity. None of these three singular points lies on the base locus, since Σx_jy_j=1 there. If the base locus were singular, the gradients of its two defining equations would be dependent at a point of the base locus, and that point would be singular on a member of the pencil. This is impossible by the preceding observation. The base is smooth. Blowing it up consequently gives the asserted Lefschetz pencil; its fibre over a parameter is isomorphic to that member because the base is a Cartier divisor inside the member.

Let K=k(P¹). The generic coefficient matrix is invertible, so by a K-linear change of y coordinates the generic fibre is the incidence variety Σx_iy_i=0. Projection π:Y→P²_x identifies it with the projective bundle of lines in the rank-two kernel E of O³→O(1). Here c(E)=1−a+a² and b is the first Chern class of the dual tautological line. The projective bundle relation is b²+c₁(E)b+c₂(E)=b²−ab+a²=0. Hence Z|Y=0 in CH²(Y), in particular it is algebraically equivalent to zero. Every bilinear height pairing on any quotient of these restricted classes has ⟨Z|Y,Z|Y⟩=⟨0,0⟩=0. Th. 5 as written would give 0=(−1)²deg Z²=3, a contradiction. ∎

**What this does and does not refute.** It refutes the raw intersection identity in Th. 5 under all the explicitly displayed transcribed assumptions, not Hodge positivity: indeed Z is primitive and Z²=3 has the correct Hodge sign. The source has an ellipsis after “fibres sont géom. intègres...”; this proof does not rule out an unstated additional admissibility condition intended there. The generic fibre is cellular, so its algebraic intermediate Jacobian in this degree is zero; its polarization is vacuous. Thus this example also disproves any proposed *injective/isometric* realization of all primitive middle algebraic cycles through that generic Jacobian. In codimension m≥2, a geometrically integral fibre can carry codimension-(m−1) cycles, which are vertical codimension-m cycles of the total space. Fibre integrality only removes additional vertical **divisors** on a surface fibration. It does not remove these higher-cycle corrections.

**Exact sources used.** Cote 44 scan004 Th. 5 and margin “variante locale”; scan002 Th. 4; scans008–009 letter dated 12.8.1964; WARGAME H9(a). The Chow calculation uses the projective bundle formula in Fulton, *Intersection Theory*, 2nd ed., Theorem 3.3(b), and the Chern relation there; the counterexample is independently proved above. No assertion about the original handwriting, beyond the supplied transcription, is made.

## AR-02 — Bost slopes do not determine the sign of a bilinear form

**Statement.** The data of a Hermitian lattice, an injective integral map to its Hermitian dual, all local operator norms, and Bost's slope inequality do not determine whether the associated symmetric bilinear form is positive.

**Proof.** Over Spec Z let E=Z with Euclidean norm and let E∨ have its dual norm. Both maps u₊:E→E∨, 1↦1 and u₋:E→E∨, 1↦−1 are integral isomorphisms, of norm one at every finite and infinite place. All ranks, degrees, maximal slopes and map heights coincide; they are zero except for rank one. Both satisfy Bost's slope inequality with equality. The forms b₊(x,y)=xy and b₋(x,y)=−xy have opposite signs on E_R. Thus any implication from just these norm/slope data to positivity is false. ∎

The geometric analogue is the distinction between a polarization λ:A→A∨ and the symmetric isogeny −λ, which is not a polarization on a nonzero abelian variety. Multiplying a map by −1 preserves all local operator norms. Identifying a particular intersection pairing with a positive Hermitian pairing is additional content; Bost's inequality does not supply it.

**Cited statement, exact scope.** For Hermitian vector bundles E,F over O_K and an injective K-linear map φ, Bost, *Algebraic leaves of algebraic foliations over number fields*, Publ. Math. IHES 93 (2001), §4.1.4, Proposition 4.5, equation (4.11), gives

deĝ_n(E) ≤ rk(E)(μ̂_max(F)+h(E,F,φ)).

The filtered variant is Proposition 4.6, equation (4.14). Their hypotheses, statements, and complete printed proofs were read and checked in this run: Proposition4.5 uses the saturated image, the determinant norm bound, and maximal slope; Proposition4.6 applies it to the induced filtered quotients and adds degrees. Basic arithmetic-degree properties are carried as background. URL: https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf . Alpöge's note step13 states only “Bost slope inequality.” The attached Lean MAP §5 row13 lists `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean` and `Formalism/LatticeSlopes/Statement.lean`; neither file was included in the attachment. Module names alone do not identify an arithmetic intersection theorem.

Those files were subsequently retrieved and read. `Formalism.F.SlopeInequality` states: for nonzero discrete Z-lattices L,M in finite-dimensional positive Euclidean spaces, an injective Z-linear φ:L→M satisfying ||φx||≤C||x|| implies μ(L)≤μ_max(M)+log C. Here deg(L)=−log covol(L) and μ=deg/rank; the hypotheses imply C>0. The complete proof `slopeInequality_of` uses a basis Gram determinant to show covol(φL)≤C^rank(L)covol(L), and then the defining maximum-slope bound for the image lattice. The positive inner products are hypotheses. No algebraic-cycle intersection form appears in this theorem.

The separately retrieved `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovGeometry/MoriwakiSt.lean` defines `MoriwakiHSStatement` and `MoriwakiBigStatement`: arithmetic Hilbert–Samuel asymptotics and a volume bound, with semipositivity, nefness and, for the asymptotic statement, nonnegative heights as hypotheses. These are not statements of the sign of a primitive cycle-intersection pairing. Their complete upstream proofs were not inspected.

## AR-03 — A fixed finite-fibre theory cannot determine arbitrary Arakelov self-intersections

Let X=P¹_Z and let L₀=O(1) have a smooth conjugation-invariant Hermitian metric. Scale its squared norm by e^(−t) to get L_t. Put x=ĉ₁(L₀). In the convention deĝ a(η)=½∫η, ĉ₁(L_t)=x+a(t), a(t)²=0, and x·a(t)=a(t c₁(L₀)). Since ∫_{P¹(C)}c₁(L₀)=1,

deĝ ĉ₁(L_t)²=deĝ x²+t.

**Proof.** The first Chern class is represented using −log||s||²; rescaling adds t. The arithmetic product of an analytic class a(η) with x is a(ηω(x)); the product of a(t) with itself vanishes because dd^c t=0. Expanding the square and using the stated arithmetic degree convention gives the formula. ∎

Thus the sign can be chosen arbitrarily with no change in any finite fibre, its ℓ-adic sheaves, Frobenius eigenvalues, or intersection pairing. This refutes an unqualified passage from finite-field purity to arithmetic positivity. It does **not** refute the primitive arithmetic Hodge-index theorem with its ampleness, metric, and primitivity hypotheses.

Source for the product and degree conventions: Gillet–Soulé, *Arithmetic intersection theory*, Publ. Math. IHES72 (1990), §4.2.11 and §4.3, especially Theorem4.3.2; https://www.numdam.org/article/PMIHES_1990__72__93_0.pdf .

## AR-04 — What is already a theorem, and the exact gate for cote 44

Cote44 Th.4 is about a canonical self-duality of an algebraic intermediate Jacobian P^m(X) for dim X=2m−1, over an algebraically closed field (made explicit in scan008). It is not itself a statement about a regular scheme over Z with Hermitian metrics. Th.5 is a function-field height comparison for a hyperplane pencil, not an Arakelov intersection identity over O_K. Its higher-cycle version needs at least an admissible extension modulo vertical cycles, and AR-01 shows why.

The following **cited background** is available independently of Alpöge:

- Moriwaki, *Hodge index theorem for arithmetic cycles of codimension one*, Math. Res. Lett.3 (1996), TheoremA(2) and TheoremB (the arXiv version alg-geom/9403011v4 has these same labels). For a regular projective flat arithmetic variety of relative dimension d≥1 and an arithmetically ample Hermitian H, if nonzero x∈CĤ¹(X)_R satisfies ĉ₁(H)^d x=0, then deĝ(x² ĉ₁(H)^(d−1))<0. TheoremB provides the generic-degree-zero weak inequality and its equality criterion. URL https://arxiv.org/pdf/alg-geom/9403011 . This source's theorem statements were checked, not its full proof.
- Künnemann, *Some remarks on the arithmetic Hodge index conjecture*, Compositio99 (1995), Theorem4.1, establishes the indicated arithmetic standard conjectures for projective space with its specified Fubini–Study metric. The introduction and §5 distinguish abelian schemes, where a positivity conjecture for heights of higher cycles remains an additional input. URL https://www.numdam.org/article/CM_1995__99_2_109_0.pdf . Only the cited statements, not full proofs, were checked.
- For curve Jacobians (m=1 in cote44 Th.4), the canonical principal polarization is classical. In surface pencils the relevant height identity and reducible-fibre corrections are classical; the elliptic case is Shioda, *On the Mordell–Weil lattices*, Comment. Math. Univ. St. Pauli39 (1990), Lemma8.1, Theorem8.4, and Theorem8.6, equations(8.8),(8.11)–(8.14). The local corrections are entries of the negative inverse component intersection matrix. URL https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf . Search retrieved exact primary-source theorem text after direct PDF retrieval failed.

No new case of the polarization theorem or a well-posed higher arithmetic Hodge-index theorem follows from steps5 and13 as supplied. This conclusion is about the proposed derivation, not a claim that all those cases are false. The raw universal Th.5 formula *is* refuted by AR-01. A valid higher version requires a construction of admissible cycle extensions, a treatment of vertical correction groups, and a proof comparing that corrected intersection pairing with the particular canonical self-duality (including the primitive signs noted in scan008's margin).

## AR-05 — The exact divisibility–slope consequence

Let L,M be finite-rank discrete lattices in positive Euclidean spaces, with L≠0. Let φ:L→M be injective with ||φx||≤C||x|| and C>0, and assume φ(L)⊂dM for a positive integer d. Then

log d ≤ μ_max(M)−μ(L)+log C.

**Proof.** Division by d gives an injective integral map ψ:L→M with operator norm at most C/d. Apply the actual slope inequality just stated to ψ and rearrange. ∎

If both lattices have the same rank r, the sharper determinant statement is

log[M:φL] ≤ r log C + deg(M)−deg(L).

**Proof.** The injective map extends to an isomorphism between their real spans. The product of its r singular values is its absolute determinant, at most C^r. Thus covol(φL)≤C^r covol(L). Since covol(φL)=[M:φL]covol(M), taking logarithms gives the claimed inequality. Also φL⊂dM implies [M:φL]≥[M:dM]=d^r, yielding log d≤μ(M)−μ(L)+log C in this equal-rank case. ∎

This is a precise way in which a divisibility lower bound can compete with archimedean norm bounds. It still does not determine a signature: φ=±d·id on Z^r with its standard metric has the same exact index d^r, norm d, slopes and equality in the displayed estimates, while its associated symmetric forms have opposite signs. Thus even augmenting AR-02 by exact divisibility and equal-rank index does not produce Hodge positivity.

## SL-01 — Integral divided-power Lefschetz blocks

Let M=⊕_{a=1}^n(Ze_a⊕Zf_a), p_a=e_a∧f_a, ξ=Σp_a, and L(u)=ξ∧u. For m≥0, write L^(m)=L^m/m!; this is integral since ξ^m/m!=Σ_{|R|=m}p_R.

Fix a set I of s coordinate pairs on which a basis wedge uses exactly one member, and fix which member in each. Put v=n−s. The remaining coordinate pairs are either empty or contribute both members. In degree j=s+2t, the resulting block has basis p_T, |T|=t, times the fixed singleton wedge. In degree j+2m its basis has |K|=t+m. Multiplication by ξ^m/m! sends p_T to Σ_{K⊇T,|K|=t+m}p_K, with coefficient+1. Different choices of I and singleton members never mix. Thus each block is the transpose of the inclusion matrix W_{t,t+m}(v), with multiplicity C(n,s)2^s.

**Proof.** Expand the divided power. Terms using an occupied pair vanish by repeated exterior generators; every empty m-set R contributes precisely T∪R. Complete pairs have even degree and commute with all other pair blocks. Moving an adjacent complete pair past a singleton or another pair introduces an even number of sign changes, so coefficients are +1. Every exterior basis wedge has exactly one decomposition by singleton pairs I, their choices, and occupied pairs T; this proves the direct sum assertion integrally. ∎

When t≤t+m≤v−t, Wilson's diagonal entries are C(t+m−r,t−r), with multiplicity C(v,r)−C(v,r−1), for 0≤r≤t. **This range is necessary**; H8's unqualified general-m statement omits it. For j=i≤n, m=n−i, every block has t+m=v−t and the range holds. Wilson's “diagonal form” is not necessarily a Smith normal form: e.g. entries2 and3 combine to1 and6 in the SNF.

Exact cited theorem: Ghorbani–Khosrovshahi–Maysoori–Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv0709.3144v1, Corollary3 (p.10), which proves Wilson's diagonal form; published JCTA115 (2008),878–887. Original source: R.M.Wilson, *A diagonal form for the incidence matrices of t-subsets vs. k-subsets*, Europ. J. Combin.11 (1990),609–615. We opened and checked Corollary3, not the original Wilson paper. URL https://arxiv.org/pdf/0709.3144 .

## SL-02 — Integral hard-Lefschetz consequences

For 0≤i≤n, the map L^(n−i):Λ^i M→Λ^(2n−i)M is a Z-isomorphism exactly when i=0, i=1, or i=n (with duplicates understood). For i=2≤n its cokernel is Z/(n−1). Over a commutative unital ring A, every undivided map L^(n−i) in the sense of ordinary power L^{n−i} is an isomorphism if and only if n! is a unit in A.

**Proof.** At i=0,1, the singleton decomposition leaves t=0 in every block; each block is1×1 with entry1. At i=n the map is the identity. If 2≤i<n, take s=i−2, t=1 and v=n−i+2=m+2. This block is W_{1,v−1}(v), whose diagonal contains v−1=m+1>1. Thus the whole map has nonzero cokernel. At i=2 the only nontrivial block has s=0,t=1,v=n, and, after complementing target indices, is J_n−I_n. Wilson gives diagonal(1,...,1,n−1); every remaining block is a unit. This gives the cokernel.

Necessity of invertibility of n! follows from L^n:Λ⁰→Λ^{2n}, which is multiplication by n!. For sufficiency, each block diagonal of L^m is m!C(t+m−r,t−r)=(t+m−r)!/(t−r)!, a product of integers between1 andn. If n! is a unit, each such factor and hence each diagonal entry is a unit. Wilson's integral equivalences remain invertible after base change to A. ∎

The third H8 consequence, for a principally polarized complex abelian variety of dimension g and cup product with θ^(g−2)/(g−2)!, follows upon choosing an integral symplectic basis of H¹ and identifying H*(A,Z)=Λ*H¹; its cokernel is Z/(g−1). This statement concerns cohomology, not algebraicity of the divided powers in the Chow ring.

## SL-03 — Explicit small-degree computations, and what step10 does not specify

The script `wilson_checks.py` constructs16 integer incidence matrices (v≤6), computes their actual Smith forms with exact integer arithmetic, checks them against Wilson's diagonal, and aggregates27 hard-Lefschetz cases for n≤6. It also constructs the full signed exterior-algebra matrix directly in14 cases n≤4 and independently verifies the aggregate Smith forms. The complete tables are `wilson_block_checks.tsv`, `wilson_lefschetz_checks.tsv`, and `wilson_exterior_direct_checks.tsv`. Every comparison returned PASS.

Some examples (1^r denotes r unit invariant factors):

| n | i | m=n−i | Smith form of L^m/m! | Smith form of L^m |
|---:|---:|---:|---|---|
|2|0|2|1|2|
|3|2|1|1^14,2|1^14,2|
|4|2|2|1^27,3|2^27,6|
|4|3|1|1^48,2^8|1^48,2^8|
|5|2|3|1^44,4|6^44,24|
|5|4|1|1^166,2^43,6|1^166,2^43,6|
|6|3|3|1^208,4^12|6^208,24^12|

The exterior-algebra parameter m here is a power of the fixed operator L. Alpöge's step10 in the prose note states a sufficient lower bound on divisibility of an m-fold iterated theta lift without specifying its numerical parameters. The attached MAP row10 lists `Formalism/SharpRestriction/Divisibility`, `Formalism/LocalToGlobal/Divisibility`, and `Formalism/GradedWeylDivisibility`. These underlying sources were absent from the ZIP, but were subsequently retrieved by the parent agent and inspected in this run. SL-06 below gives the actual local valuation statement and its hypotheses. Thus these Smith forms are verifiable predictions of the H8 exterior model, not computations of an actual theta lift. Matching them requires an integral comparison with the modules and maps actually used, not an identification of the letter m.

## SL-04 — Contraction is not the normalized co-Lefschetz operator

Set D=Σι_{f_a∨}ι_{e_a∨}, and let H act by n−j on Λ^jM. Directly on each four-dimensional exterior factor one has [D,L]=H; summing gives the same relation on the full exterior algebra. The commutators [H,L]=−2L and [H,D]=2D follow from degrees. On a primitive vector v of degree i≤n, meaning Dv=0, put d=n−i. For 0≤r≤d, induction using [D,L]=H gives

D L^r v=r(d−r+1)L^(r−1)v,

where the displayed L^r is the ordinary power. Consequently

D^r L^r v=r! d!/(d−r)! v.

**Proof of the last formula.** For r=1 the commutator and Dv=0 give DLv=Hv=dv. If the formula for D L^r holds, then D L^(r+1)v=(LD+H)L^r v=[r(d−r+1)+(d−2r)]L^r v=(r+1)(d−r)L^r v. Iterating this scalar lowering rule proves the displayed product. ∎

The normalized inverse-string lowering Λ_N satisfies Λ_N L^r v=L^(r−1)v. It differs from D by the factor r(d−r+1) on the rth step. The endpoint inverse relation Λ_N^d L^d v=v is therefore incompatible with treating Λ_N as ordinary contraction D.

In particular H8's scalar (r!)² is the endpoint specialization d=r. For an arbitrary primitive vector and an arbitrary r≤d, the coefficient is r!d!/(d−r)!, as above.

For n=2, let Ω=e₁∧f₁∧e₂∧f₂. Then L²(1)=2Ω, D²Ω=2, and D²L²(1)=4. In particular ARCHIVE_16_scan014.tex's identification Λ₀=ξ₀*⌟(−), if ordinary contraction is intended, cannot simultaneously satisfy the scan016 identity (Λ₀²L₀²−1)π₀=0. Also L² is not an isomorphism of the integral end degrees. This is an internal incompatibility of the supplied text, not a proof that Grothendieck wrote a wrong theorem: the original scan must distinguish a normalization, coefficient ring, or revision layer.

## SL-05 — An abstract Arthur SL2 does not fix integral Lefschetz divisibility

The standard Arthur block μ[t] is μ⊠Sym^(t−1)(C²). Its SL2 weights are t−1,t−3,...,1−t. Its associated unramified exponents are (t−1)/2,(t−3)/2,...,(1−t)/2, not canonically the unshifted integer Tate twists0,...,t−1. Exact reference: Mok, *Endoscopic Classification of Representations of Quasi-Split Unitary Groups*, arXiv1206.0882v5, §2.3, equation(2.3.1). URL https://arxiv.org/pdf/1206.0882 . The representation-theoretic block is not itself a motive with an integral lattice and algebraic cup-product correspondences.

**Integral counterexample.** In V=Sym²(Q²), with coordinates x,y and e=x∂/∂y, the two lattices

Λ₀=Zx²⊕Zxy⊕Zy²,
Λ₁=Zx²⊕Z(2xy)⊕Zy²

are both stable under SL2 over Z. Indeed substituting ax+by,cx+dy with determinant one sends the three displayed generators of either lattice to integral linear combinations of those generators (for Λ₁ the cross coefficients of the squares are even). Over Q they give the identical irreducible representation. But the map e from the lowest weight line to the middle line is multiplication by2 on Λ₀ and multiplication by1 on Λ₁; its cokernel is Z/2 in the first case and0 in the second. This proves that a rational/complex SL2 identification alone does not determine integral divisibility. ∎

The same failure occurs for each requested small power m, not only m=1. In Sym^d(Q²), d=m+1, compare the monomial lattice with the binomial lattice generated by C(d,r)x^{d−r}y^r, 0≤r≤d. Both are stable under SL2_Z. To see this for the latter, take the permutation-invariant tensors in (Z²)^{⊗d}; the orbit sums with r copies of y form a basis, and their images under symmetric multiplication are precisely these binomial generators. This map is equivariant, so its image is stable. On the line from y^d to x^m y, e^m has indices (m+1)! and m! respectively, whereas e^m/m! has indices m+1 and1. The coefficients follow directly by differentiating y^d m times and expressing the answer in the respective target basis. Hence:

|m|representation|ordinary e^m index pair (monomial,binomial)|divided e^m/m! index pair (monomial,binomial)|
|---:|---|---|---|
|1|Sym²|(2,1)|(2,1)|
|2|Sym³|(6,2)|(3,1)|
|3|Sym⁴|(24,6)|(4,1)|

Each entry is the Smith invariant of this one-dimensional weight-to-weight map. These are fully specified countermodels to a lattice-free identification, not values of Alpöge's theta-lift maps.

It is therefore false that the occurrence of an Arthur SL2 block by itself identifies step10 with Wilson's integral indices. A geometric correspondence respecting the grading, the raising operator and the specific integral lattices is necessary. Cote16 scan016 stresses preservation of the degree projectors as essential; scan017 gives its n=1 counterexample to uniqueness without a prescribed grading. A theta-lift chain changes the automorphic group and adds direct-sum blocks, whereas cup product moves within a fixed graded realization; the integer counting lifts and the dimension of an Arthur block are distinct pieces of data. The supplied statements do not supply the needed comparison. H8(iv), about the index of an associative order inside a product of matrix rings, also needs a specified ambient integral order: it does not follow from the Smith form of one multiplication map.

## SL-06 — What the retrieved divisibility code actually states

This section reports declaration-level source inspection, not a Lean kernel check and not a verification of every imported theorem. Paths below are relative to the retrieved `lean_evidence/` directory. The underlying archive was retrieved and its provenance handled by the parent agent.

`Formalism/LocalToGlobal/Divisibility/Inputs.lean`, declaration `ColChain`, specifies a length `mm`, varying dimensions `c : Fin (mm+1) → ℕ`, rectangular matrices `Kj` of size `c(j+1) × c(j)`, and a final linear period functional `PtL`. Its `fact` field identifies the original period with that functional evaluated on the product of these matrices. No Lefschetz grading, inverse lowering operator, SL2 commutator, or exterior-algebra lattice is part of this declaration.

The local estimate has a precise scalar content. Let ℓ be a prime, let w be a place of K above ℓ with ramification index e_w, and use the valuation convention |ι(a)|_ℓ=|ℓ|_ℓ^{v_w(a)/e_w}. Let J be a finite nonempty set with distinguished j₁. Suppose a period P∈K has a finite expansion

ι(P)=Σ_π x_π y_π r_π γ_{P,π}^{−1} ∏_{j∈J}(γ_{π,j}^{−1} ε_{π,j} a_{π,j}).

Assume |x_π|,|y_π|,|r_π|,|ε_{π,j}|≤1; D is a nonzero natural number; every γ_{π,j} and γ_{P,π} divides D; γ_{π,j₁}=1; and |a_{π,j}|≤|ℓ|^{s_j}. Then

P=0 or v_w(P) ≥ e_w Σ_{j∈J}(s_j−v_ℓ(D)).

**Complete proof of this scalar statement.** Each inverse denominator has norm at most |ℓ|^{−v_ℓ(D)}. The product over J has at most |J|−1 such losses because γ_{π,j₁}=1; the final denominator γ_{P,π} contributes at most one further loss. Thus each summand has norm at most |ℓ|^{Σ_j s_j−|J|v_ℓ(D)}. The ultrametric triangle inequality gives the same bound for the finite sum. If P≠0, substitute the valuation formula and use 0<|ℓ|<1 to reverse the inequality on exponents. Multiplication by e_w>0 gives the result. ∎

Exact declarations are `PathData`, `PathData.val`, `StabDvd`, and `IsExpansion` in `.../JetBounds/IsExpansion.lean`; `PathBound`, `LocalValuationBoundAt`, and `PlaceInputAtEntry` in `.../JetBounds/Statement.lean`; and theorem `valuation_of_entry_bounds` in `.../JetBounds/JetBoundsProofs/ValuationOfEntryBounds.lean`. The complete proof bodies of this last theorem and of `path_height_bound`, `embedding_lower_bound`, and `norm_inv_natCast_le_of_dvd` in `.../JetBounds/JetBoundsProofs/NormInvNatCastLeOfDvd.lean` were read. They implement exactly the ultrametric argument above, together with the stated input bounds. The upstream construction of all entry bounds and the full global application were not re-proved here.

For |J|=1,2,3, the local lower bounds are respectively

| number of factors | valuation lower bound for a nonzero period |
|---:|---|
|1|e_w(s₁−v_ℓ(D))|
|2|e_w(s₁+s₂−2v_ℓ(D))|
|3|e_w(s₁+s₂+s₃−3v_ℓ(D))|

These are actual specializations of the inspected statement, with its actual parameters still visible. They are lower bounds, not claims of exact valuations or Smith invariant factors. If the right side is nonintegral, integer-valued v_w gives its ceiling. Determining numerical bounds requires the entry estimates s_j and D from the intended lift. The full code also treats weights and prime types: `Numbers.lean` defines `FOrb`, `FInert`, `FRamD`, `FjP`, and `Fo`; `FjP` branches on distinguished primes, ramification, and inertness, while `logHook` involves a highest-weight hook product. None is specified by the count m alone.

The actual arithmetic parameter family, structure `Ranks` in `Formalism/LocalRingCardinality/Params.lean`, requires m even and m≥2, along with m+3≤k, k+m+4≤t, 3m<t and m≤2ord≤k. Thus the m=1,3 matrix examples above are universal algebraic models, not instances of this family; the earlier one-, two- and three-factor local bounds refer to |J|.

**The concrete m=2 evaluation.** `NumbersLemmas.lean`, `numEx`, has k=8,t=15,nV=24,q=11,d=7 and distinguished primes3697,7393. The actual source `SpanPowerMembership/ExampleRanksRankComplement.lean`, R0, gives N(j)=8+16j, hence ranks8→24→40. `SpanPowerMembership/ExampleWeightMiddleEntries.lean`, hcV,hcB,hcE, gives constant place data v=(24,20,16,12,8,4,0), b=(91,109), e=(100,118). Here |R.A|=4 and |RPl|=8. Exact substitution in `Numbers.lean` gives aPlus1=(109,106,103,100,97,94,91,1), aMinus1=(1); aPlus2=(126,123,120,117,114,111,108,18,1), aMinus2=(). Therefore Dplus=(5608,6704), Dminus=(8,0), FTypeG=(-2808,-3352), FRamD=(-1400,-1652). In particular the first ramified and zero contributions agree with the explicit source declarations ex_FRamD,ex_FjP_d,ex_FjP_2,ex_FjP_q.

**Exact orbit optimization.** In `DataParams₂.lean`, lpFeasible(p,d0,Ds), suppose p≥2,d0≥2, and Ds=A≥0 constant. The variables x(s,i)≥0 vanish unless i<d0 is odd, and satisfy Σ_i p^i x(s,i)+Σ_i x(s−i,i)≤A. Summing in s gives (p+1)Σ_{s,i}x(s,i)≤Σ_{s,i}(p^i+1)x(s,i)≤d0A. The feasible assignment x(s,1)=A/(p+1), all other variables zero, attains this bound. Thus the optimum is d0A/(p+1), and lpF=p d0A/(p²−1)−d0A/(p+1)=d0A/(p²−1). ∎

At inert or signal primes used by FjP, A=7e_j gives FInert_j=56e_j/(p²−1): the signal orbit length is at least2; for a nonzero inert Frobenius element its order is at least2; the zero inert element has a special branch giving the same formula directly. No assertion is made for unused FInert values in other prime classes. The cutoff for numEx is X''=8exp(2^(1/300))∈(21,22), rigorously certified by (101/100)^300>2, exp(101/100)<11/4 using a rational Taylor remainder, and e>8/3. HostCls and hostEx_psQ classify primes through (-7/p),(-11/p). The entire support table is:

|p|class|F_1,p|F_2,p|sum|
|---:|---|---:|---:|---:|
|2|ram2|0|0|0|
|3|signal|700|826|1526|
|5|signal|700/3|826/3|1526/3|
|7|ramD|−1400|−1652|−3052|
|11|ramQ|0|0|0|
|13|inert|100/3|118/3|218/3|
|17|inert|175/9|413/18|763/18|
|19|inert|140/9|826/45|1526/45|
|3697|distinguished|−2808|−3352|−6160|
|7393|distinguished|−2808|−3352|−6160|

Consequently Fo=12208Σ_{p∈{3,5,13,17,19}}log(p)/(p²−1)−3052log7−6160(log3697+log7393), approximately−108518.601323. This is solely the F contribution. `step10_numeric_checks.py` reproduces exact rational entries, the cutoff certificate and20 optimizer certificates; it writes step10_m2_parameters.tsv, step10_m2_local_contributions.tsv and source hashes. This is not a Lean kernel run.

**A precise small-example limitation and the source's repair.** The test datum numEx cannot satisfy NumFacts in NumbersLink.lean for any choices of its auxiliary constants: the n2 field would require Nm²≤b, while Nm=40 and b=exp(2^(1/100))<e²<9. Hence it would require1600<9. This proves incompatibility of this tuple with these specific hypotheses, not a failure of the conditional theorem. The same file explicitly supplies NumInst.numBig with MBig=200+|numEx.logOm| and x=exp(100MBig), and constructs numFactsBig : numBig.NumFacts wd0 1 1 5 5 1 53 4. Its v,b,e data are unchanged; one u entry and the scale change. Thus the distinguished/ramified coefficients and constant-weight FInert formula remain valid, with additional primes under its much larger cutoff. The exact declaration and parameters were checked; a complete re-proof of every numFactsBig dependency is not claimed.

Neither numerical datum nor NumFacts selects a nonzero period or its two integral lattices. The record-level definition in DataParams₂.lean is sg(u,w)=Σ_{j=1}^m(gainD(j,w)+F(j,w)−E(u,j,w)), with gainD zero at dropped primes. Its global gain term also subtracts tau, whereas the local sg definition does not. Numerical valuations additionally require a record linking F to the computed F_j,p, the gain/error data, the period expansion, entry estimates, integral row/column lattices, stabilizer denominator, and the displayed threshold inequality in PlaceInputAtEntry. The companion ExampleWeightMiddleEntries file supplies an emptyColumnChain and trivialPeriodMap with identically zero period; it does not supply a nonzero matrix with a Smith form to compare to Wilson.

At the level of matrix-chain data and factorization, no divisibility invariant depends only on length. For any length m≥1 and s≥0, take all c(j)=1, all frames1, all Kj=1 except K₀=[ℓ^s], and the final functional to be multiplication. Then the period is ℓ^sxy, satisfying the factorization and taking valuation s at x=y=1. Fixed length permits every nonnegative valuation. This is a counterexample for bare matrix-factorization data, not a claim that these arbitrary chains instantiate every field of the complete automorphic structures or satisfy a particular theta-lift construction.

`Formalism/GradedWeylDivisibility/StatementA.lean` defines `rowDiv R a b k f` as the coefficient of T^k after the row transvection X_{b,s}↦X_{b,s}+T X_{a,s}. It defines the Weyl lattice by applying words in those operators to a highest-weight polynomial, and the dual Weyl lattice by column homogeneity and upper-unipotent invariance. `StatementB.lean` uses the factorial-weighted Fock pairing; `StatementD.lean` and `StatementE.lean` treat transformed integral lattices and their duals. This is a concrete integral GL-row action. The inspected definitions contain no identification of that action with multiplication by a unimodular alternating two-form on an exterior algebra.

**Refined comparison gate.** One would need an explicit map from the intended chain and its Weyl/dual-Weyl lattices to a fixed graded Lefschetz realization, an equality of the individual operators with the specified divided powers, and compatibility of all integral lattices and denominators. Without these data, Wilson's invariant factors and the local period bound answer different questions. A scoped text search of the three divisibility directories and the supplied `PositivityTheory` and `Formalism/HermitianCurvature` directories found no named Hodge-index or arithmetic intersection comparison. This is a scoped search result, not a proof that no such theorem exists elsewhere. In particular, `HermitianCurvature/Statement.lean` contains Fourier-recursion estimates and Hermitian linear algebra, not a statement of arithmetic Hodge index.

## SL-07 — Frobenius distinguishes the untwisted operators

Let X/F_q be smooth projective of positive dimension and let η be the class of an ample hyperplane divisor defined over F_q. Let F denote cohomological geometric Frobenius on untwisted ℓ-adic cohomology, ℓ≠char F_q, so that Fη=qη. Put L(x)=η∪x. Then

F L = q L F.

**Proof.** Pullback by the q-power Frobenius morphism sends O_X(1) to O_X(q), and the first Chern class and cup product commute with pullback. Hence Fη=qη and F(η∪x)=qη∪Fx. The same formula follows from the Galois-invariant class η∈H²(X̄,Q_ℓ(1)). ∎

In contrast, in a local Arthur parameter ψ:L_F×SL₂(C)→{}^LG, the images of the two factors commute. In a linear realization, E=dψ(e) therefore commutes with ψ(w,1). If an isomorphism identifies E with a nonzero L and ψ(Frob,1) with the above untwisted F, the two identities imply (q−1)LF=0. As F is invertible and q≠1 in characteristic zero, this forces L=0, a contradiction. Already X=P¹ gives a concrete two-dimensional example: F=diag(1,q), while L maps1 toη.

This obstruction concerns precisely that unnormalized identification. Degreewise Tate twists remove it: on the even grading ⊕_r H^{2r}(X̄,Q_ℓ(r)), and separately on ⊕_r H^{2r+1}(X̄,Q_ℓ(r)), hyperplane multiplication commutes with Frobenius. These integer Tate twists are also available integrally over Z_ℓ for ℓ≠char F_q; it would be incorrect to call every such normalization nonintegral. A uniform weight-zero normalization on all degrees can involve half twists. Moreover the associated Langlands parameter is φ_ψ(w)=ψ(w,diag(|w|^{1/2},|w|^{−1/2})), not ψ(w,1), and need not commute with E. Thus SL-07 specifies a normalization gate; it does not exclude a properly normalized geometric comparison.

Primary locators checked: Milne, *Lectures on Étale Cohomology*, version2.21, Theorem23.3(a,b), §27 “The Frobenius map,” and Proposition27.3; https://www.jmilne.org/math/CourseNotes/LEC.pdf . Mok, cited above, §2.2, equations(2.2.9) and(2.2.10), for the product parameter and diagonal specialization. These definitions and statements were read; no assertion about a conjectural global Langlands group is needed.

## SL-08 — A correct normalized universal Lefschetz ring

There is an elementary integral model that realizes the matrix-unit calculation in cote16 while keeping it separate from ordinary contraction. Define

Φ_n^str = ∏_{i=0}^n M_{n−i+1}(Z).

The ith factor acts on a string with basis v_{i,0},…,v_{i,n−i}, placed in degrees i,i+2,…,2n−i. Define L v_{i,r}=v_{i,r+1} and Λ_N v_{i,r}=v_{i,r−1}, with zero outside the string. Let E_i^{β,α} be the corresponding matrix units, with degree2(β−α), and π_j the sum of the diagonal units in degree j. Then

E_{i'}^{β',α'} E_i^{β,α} = δ_{i',i} δ_{α',β} E_i^{β',α},

and Φ_n^str is generated over Z by L and Λ_N. It is free of rank Σ_{i=0}^n(n−i+1)²=(n+1)(n+2)(2n+3)/6. In particular its rank for n=1 is5, as in scan017. The string indices must satisfy 0≤α,β≤n−i; the bound2n−i in scan015 is incompatible with the indicated degrees and its claimed basis.

**Proof of generation.** Let B=1−LΛ_N, the projection to the bottom of every string. For d=0,…,n, the operator

Q_d=B(Λ_N^d L^d−Λ_N^{d+1}L^{d+1})B

is the bottom projector of the string of length d+1: on a bottom vector the two terms are respectively the indicators for length at least d+1 and at least d+2. Every matrix unit on that string is L^β Q_d Λ_N^α. Thus every matrix unit belongs to Z[L,Λ_N], proving generation and the asserted rank. ∎

**Universal property.** Let A be a commutative ring and M=⊕_{j=0}^{2n}M^j a graded A-module. Suppose L raises degree by2 and the ordinary maps L^{n−i}:M^i→M^{2n−i} are isomorphisms for 0≤i≤n. Then M has a canonical primitive decomposition into unit-step strings, and a unique graded representation of A⊗Φ_n^str carrying L and all π_j to the prescribed operators. Its lowering operator is Λ_N. Conversely such a representation implies the displayed hard-Lefschetz isomorphisms. The same assertion for a unital graded A-subalgebra E⊂End_A(M) containing L is equivalent to Λ_N and the degree projectors belonging to E.

**Complete proof.** Put P^i=ker(L^{n−i+1}:M^i→M^{2n−i+2}) for i≤n, interpreting out-of-range groups as zero. For i≥2, the map

x↦(L^{n−i+2}:M^{i−2}→M^{2n−i+2})^{−1} L^{n−i+1}x

splits L:M^{i−2}→M^i. Its kernel is P^i, so M^i=P^i⊕L M^{i−2}. For i=0,1, P^i=M^i. Induction gives the direct sum decomposition in degrees≤n. For j>n, transport the decomposition in degree2n−j by the given isomorphism L^{j−n}; this gives

M=⊕_{i=0}^n ⊕_{r=0}^{n−i} L^r P^i.

The map L^r:P^i→L^rP^i is injective because L^{n−i} is injective. Matrix units therefore act unambiguously by L^αv↦L^βv on each primitive string. This constructs the representation and Λ_N, and it proves the converse. To check uniqueness, any representation with the specified degree projectors decomposes M into its matrix-unit summands. The bottom summand of the ith factor is exactly P^i: L^{n−i+1} vanishes there and is injective on every other summand in degree i. The other summands are consequently L^rP^i, and L forces all matrix units between them. Hence the representation is unique. All the matrix units are generated by L,Λ_N, so the subalgebra assertion follows. ∎

The degree condition is necessary. For n=1, conjugation by 1+tL in the M₂(Z) factor fixes L but sends Λ_N to Λ_N+t(E_{11}−E_{00})−t²L. Distinct integers t give distinct ungraded ring maps with the same L. They do not preserve the prescribed degree projectors, explaining the warning in scan016 and the negative answer in scan017.

The symplectic exterior lattice of SL-01 does not supply this integral unit-step model with ordinary powers: SL-02 proves that all its hard-Lefschetz maps are isomorphisms only after n! becomes a unit. Already at n=2, Λ_N(Ω)=ξ/2 because L²1=2Ω, so Λ_N does not preserve the original exterior lattice. After base change to Z[1/n!], the ordinary hard-Lefschetz maps are isomorphisms and the universal property above applies. This is a precise repair of the normalized universal calculation, not an identification of Φ_n^str with the integral contraction order Z[L,D]. No index of that latter order in an unspecified ambient order has been asserted.

## Status and checked boundaries

- AR-01 is a complete counterexample to the literal cote44 Th5/H9(a), with a smooth base and integral nodal fibres checked explicitly.
- AR-02 and AR-03 completely refute the two broad formal positivity implications stated there. They do not refute correctly formulated arithmetic Hodge-index theorems.
- AR-04 is an exact scope statement and gate, with literature results cited as background.
- SL-01, SL-02, SL-04, SL-05, SL-07, and SL-08 have complete elementary proofs above; SL-03 has exact computation certificates. SL-06 gives the actual local bound and a complete independent proof of its scalar content, with the scope of source inspection specified.
- An actual identification of the theta-lift chain with a geometric Lefschetz module, or a numerical equality between step10 and Wilson's indices, remains unproved after inspection of the retrieved declarations. This is not a counterexample to every possible normalized comparison.
