# Cote 16: proof checks and exact computations

**Audit date:** 19 November 2026. **Source:** the supplied diplomatic transcription, with the applicable second-pass changed readings. No manuscript image was available. Statements below labelled “reconstruction” are mathematical formulations; they do not amend the transcription. The executable certificates are `scripts/exact_checks.py`, `outputs/exact_checks.txt`, and `outputs/exact_checks.json`.

## 1. Finite gradings and recovery of degree projectors

For a finite family of orthogonal idempotents whose sum is 1, every element of a ring has the block decomposition `u=Σ π_j u π_i`. Grouping blocks by `j−i` gives a direct grading: multiplying blocks forces the middle indices to agree, so degrees add. Conversely the projections of a finite direct-sum grading have exactly these identities. Each π_i commutes with every degree-zero element, not with every element of the ring. These are direct checks of scans 3–4, independent of literature identification.

If e and f are central idempotents of a ring R and have the same annihilator, then 1−e annihilates f, so f=ef. Interchanging them gives e=ef, hence e=f. This proves the annihilator observation used in scans 5–7. The displayed induction base `i=n−1` does not leave just π_n unknown: it leaves π_{n−1},π_n,π_{n+1}. The natural base is i=n; that is a mathematical correction to confirmed source ink, not a new transcription.

There is a particularly transparent **reconstructed** version of the outer-projector induction in scans 8, 51, and 53. Suppose M is graded in degrees 0,…,2n, E is a graded subring of End(M), L has degree +2, and for every k<n there is a homogeneous w_k of degree −2(n−k) whose restriction to M^{2n−k} is the inverse of L^{n−k}:M^k→M^{2n−k}. Both inverse identities are assumed on the indicated groups. If the projectors outside [k,2n−k] have already been obtained, put

`T_k=1−Σ_{j<k}π_j−Σ_{j>2n−k}π_j`,

`V_k=T_k L^{n−k} T_k`, and `W_k=T_k w_k T_k`.

Degree counting shows that V_k has only its block M^k→M^{2n−k}, and W_k only the reverse block. Therefore W_kV_k=π_k and V_kW_k=π_{2n−k}. All factors lie in E. After induction π_n is the complement. This proves the membership statement, while keeping both cutoffs visible.

The **source’s** assertion on scan 53 that `L^{n−k}T_k` alone vanishes outside degree k is false globally. The exact certificate uses H*(P²) with basis 1,h,h², n=2,k=1,T₁=π₂. Then LT₁(h)=h²≠0 even though H¹=0. The cohomological inverse condition in degrees 1 and 3 is vacuous, and choosing the homogeneous w₁=Λ is permissible. Consequently w₁LT₁=π₂, not π₁=0. The two-cutoff expression is zero, as required. This identifies a flaw in that displayed proof, not a counterexample to algebraicity of the projectors. Kleiman (1968), Lemma 3.15, also uses a two-sided truncated block in the intrinsic uniqueness argument.

## 2. Primitive decomposition and support conventions

Assume every L^{n−i}:M^i→M^{2n−i} is an isomorphism, with finite grading and coefficients for which these are actual module isomorphisms. Put P^i=ker(L^{n−i+1}:M^i→M^{2n−i+2}) for i≤n. Since L^{n−i+2}:M^{i−2}→M^{2n−i+2} is an isomorphism, the map L^{n−i+1} splits off LM^{i−2}, and `M^i=P^i⊕LM^{i−2}`. Induction yields the primitive decomposition. The upper half is transported by hard Lefschetz. No semisimplicity of an ambient correspondence ring is required for this module decomposition.

In scan 11, `1−Σ_{α′>α}π_{i,α′}=Σ_{α′≤α}π_{i,α′}` is valid **on M^i**. As an equality of endomorphisms of M, the left side is identity on every other degree while the right side is zero there. A supported version has π_i in place of 1. With `q_{i,α}=π_i−Σ_{α′>α}π_{i,α′}`, the primitive-projector expression

`π_{i,α}=L^α w_{i−2α} L^{n−i+α} q_{i,α}`

works on the whole module: on a remaining summand L^βP^{i−2β} with β<α, the rightmost power of L kills it; when β=α, it reaches the opposite endpoint and w_{i−2α} returns the primitive vector. Previously removed summands are killed by q. The relevant inverse exponent is `n−(i−2α)=n−i+2α`. Any global expression with an arbitrary extension of w outside its prescribed block still needs its input/output support shown.

Unit-step Λ sends L^j p to L^{j−1}p for j>0 and kills p. Its degree is −2. Hence `LΛ=1−p_bottom` and `ΛL=1−p_top`; it kills the appropriate endpoints and has the indicated kernels and images. These facts check the endpoint relations on scans 13–14 and 33. The literal `Λ∈E^(2)` on scan 13 has the wrong degree. The unfinished brace-and-dots formula (6.5) is not treated as a supplied definition. A cancelled assertion is not used as the final theorem.

## 3. The integral exterior model and its distinct normalized replacement

For `ξ=Σ e_j∧f_j`, all degree-two summands commute and square to zero. In ξ^n each ordering of the n distinct summands contributes the same volume element; there are n! orderings. Thus ξ^n=n!·vol. The integral map Λ⁰→Λ^{2n} is multiplication by n!, which is not a unit for n≥2. The script checks n=1,…,5 directly in a bit-mask exterior algebra, yielding coefficients 1,2,6,24,120.

Ordinary contraction `D=Σ ι_{f_j∨}ι_{e_j∨}` satisfies `D(L^j1)=j(n−j+1)L^{j−1}1`. In particular DL(1)=n. The script checks every j for n≤5. Unit-step lowering instead has ΛL(1)=1 for nontrivial strings. This second defect persists after tensoring with ℚ. Calling D the draft’s normalized Λ is therefore a substantive error unless an extra convention is supplied. Rationalizing is not a complete repair.

The earlier run’s **replacement model** is the direct sum of one free integral string `v_{i,0},…,v_{i,r}` for each i=0,…,n, where r=n−i. Raising and lowering are the two unit shifts. Put e=1−LΛ. Then e projects onto all bottom vectors, and `eΛ^rL^re` projects onto bottoms of strings of length at least r+1. Their successive difference isolates the bottom of the string of length exactly r+1. Hence

`e_i=eΛ^{n−i}L^{n−i}e−eΛ^{n−i+1}L^{n−i+1}e`,

`E_i^{ba}=L^b e_i Λ^a`, for 0≤a,b≤n−i,

are all the matrix units, with integral coefficients. Every generator preserves the individual strings, so the generated algebra is exactly `∏_{i=0}^n Mat_{n−i+1}(ℤ)`. Its rank is the sum of squares, `(n+1)(n+2)(2n+3)/6`. The script checks every claimed unit on the universal representations for n≤5; the argument above proves all n. This does not identify that algebra with the **literal** ordinary-contraction order on scan 14.

The source’s bound 2n−i on scan 15 is confirmed ink but does not index this basis: the string exponent only runs through n−i. In n=1 the algebra is Mat₂(ℤ)×ℤ of rank 5. On its two-dimensional block, direct multiplication gives

`(1+tL)Λ(1−tL)=Λ+t(π₂−π₀)−t²L`.

This fixes L and changes the grading; it proves the circled “Non” on scan 17. It also shows why uniqueness of a **graded** homomorphism with prescribed projectors does not imply uniqueness from L alone. Separately, the literal criterion `(w_iL^{n−i}−1)π_{2n−i}=0` fails on this model: for i=0 it equals −π₂. The repaired criterion uses π_i on that side and the second opposite inverse identity.

## 4. A nonzero top power is not a Lefschetz criterion

The scan-22 experiment has the commutative graded algebra

`R=k[L,L′]/(L⁴,(L′)²−LL′,L²L′−L³,L³L′)`,

where both generators have degree 2. The script gives two commuting 6×6 multiplication matrices on the basis `1;L,L′;L²,LL′;L³` and verifies every defining relation. These matrices also prove those six normal forms are independent, while reduction by the relations proves spanning. L is a Lefschetz element: its middle map is the identity 2×2 matrix and L³≠0. The middle map for L′ has rank 1, but `(L′)³=L³≠0`. Thus a nonzero top power does not force all middle Lefschetz maps to be isomorphisms. This is the manuscript’s own counterexample mechanism, with its computation completed here.

For two already Lefschetz operators whose top and bottom correspondence spaces are free of rank one, the separate rank-one comparison is valid: writing `(L′)^n=αL^n` and `(Λ′)^n=βΛ^n`, the endpoint identities imply αβ=1. The failed converse cannot be substituted for the hypothesis that both operators are Lefschetz.

## 5. The hyperplane formulary

For a primitive X-string of length r+1, write x₀,…,x_r. Its restriction to a smooth hyperplane gives a Y-string y₀,…,y_{r−1}; restriction ρ sends x_j to y_j for j<r and x_r to 0, and Gysin γ sends y_j to x_{j+1}. An additional primitive middle summand E of H*(Y) is killed by γ and is not in the image of ρ. This is the linear setup supplied by weak and hard Lefschetz and Poincaré duality. On these strings:

* γρ=L_X and ργ=L_Y.
* `Λ_Y=ρΛ_X²γ`.
* `ρΛ_Xγ=1−p_E` on H*(Y).
* `q=γΛ_Yρ` is the identity on the strict interior of an X-string and zero at its endpoints.
* For m≥1, `γΛ_Y^mρ=qΛ_X^{m−1}q`.
* If `T=1+q`, then `Λ_XL_X+L_XΛ_X=T−p_n`, where p_n is the length-one middle-string projector, and `L_X²Λ_X+2L_XΛ_XL_X+Λ_XL_X²=L_XT+TL_X`.

All formulas are checked on the basis above, including r=0 and the additional middle primitive summand. The script verifies r=1,…,8 and m through r+2 exactly. The degree and endpoint argument proves the identities for every r. The transfer formula `γp_{Y,j}Λ_Yρ=p_{X,j+1}` requires j≤r−2. At j=r−1 the left side is zero, whereas the alleged top projector on the right is nonzero. This verifies the strict boundary condition in the corrected interpretation of scan 40.

Restriction does not commute with lowering on the original top endpoint, since ρ kills that endpoint but ρΛ_X need not. It does commute on the remaining shared parts; inserting the projector killing the original tops gives the corrected formula. The expression at the bottom of scan 38 with two pullbacks is not composable in the written variance; its mathematically suggested Gysin replacement remains a scan alarm.

These identities prove the formal hyperplane reductions conditionally. They do not supply algebraic cycles representing Λ. In particular, `Λ_Y=ρΛ_X²γ` gives B(X)⇒B(Y), not the reverse implication on its own. The product-cycle hypothesis in the letter is essential. The source’s A′/A″ inequalities on scan 50 still mix degree conventions and are not silently promoted to precise published statements.

## 6. Discriminant pairings and the geometric comparison they do not prove

Let Q be nonsingular symmetric integral. Changing x by Qz changes `xᵀQ⁻¹y` by the integer zᵀy, so the pairing on D_Q is well-defined. If it pairs x trivially with every y, then Q⁻¹x∈ℤ^r, hence x∈Qℤ^r. Since D_Q is finite, nondegeneracy implies perfection. For Q=(−m) the pairing is −ab/m modulo ℤ. These are independent proofs of the earlier notes’ lattice statements.

After a blowup with incidence vector v, the displayed matrix Q′ is integrally congruent to Q⊕(−1): the change of basis `[[I,0],[vᵀ,1]]` has determinant 1. The script checks the general symbolic 2×2 base case; multiplying the blocks proves the formula in every size. The extra unimodular rank-one summand has trivial discriminant group. Resolution independence additionally uses common domination by point blowups in the appropriate surface category.

None of this identifies the discriminant pairing with a pairing produced by local étale duality. That comparison involves functorial maps, orientation/twist conventions and the geometry of the resolution. It remains a separate problem record. Nor does Mumford’s topological negative-definiteness theorem by itself identify all étale pairings over arbitrary characteristic.

## 7. Hodge algebras and the earlier orbit examples

In the scan-25 algebra, all potentially nontrivial associativity checks reduce by grading and graded commutativity to the four-degree-one equation printed in the box. The pairing in degrees 1 and 3 is evaluation by construction; the degree-2 pairing is `1⊕Q`, so Poincaré duality is equivalent to nondegeneracy of Q. Multiplication by ξ from degree 1 to degree 3 is the map induced by φ, so hard Lefschetz is equivalent to nondegeneracy of φ. These latter conditions do **not** imply the boxed associativity equation. With V=k² symplectic and W=0, choose x=t=e,y=z=f: its left side is 1 and right side 0. This checks the earlier run’s warning, not a false claim asserted by Grothendieck.

For the isotropic-line example take the symmetric plane diag(1,−1), ξ=(1,0), and α(x∧y)=φ(x,y)(1,1). The image vector is isotropic, its pairing with ξ is 1, and φ is nondegenerate. Thus the pulled-back four-form is zero. The field characteristic is taken different from two to avoid conflating alternating and symmetric conventions.

The claim that an arbitrary φ can be obtained “up to scalar” from a vector ξ of norm 1 needs a qualification: the inverse image of φ under the nondegenerate form Q can have zero norm or a norm in an unsuitable square class. Nondegeneracy of φ alone does not remove either obstruction over an arbitrary field. No changed ink is asserted. Here is an exact counterexample satisfying the four-form constraint, rather than merely an arbitrary symmetric-form example. Take V of dimension six with paired bivectors p₁,p₂,p₃ and a four-form whose coefficients on p₁∧p₂,p₁∧p₃,p₂∧p₃ are 1,2,3. Its symmetric form Q on Λ²V has p-plane matrix C=[[0,1,2],[1,0,3],[2,3,0]] and full determinant 15552. For ξ=p₁+p₂−p₃/5, Qξ has paired coefficients (3/5,2/5,5), so the induced alternating form φ has determinant 36/25 and is nondegenerate. Yet Q(ξ,ξ)=0. Thus rescaling cannot normalize this ξ to norm one even over an algebraically closed extension. `nonzero_norm_not_automatic` in the exact output verifies the full 15×15 matrix and every stated value. This is an audit counterexample, not an assertion of geometric realization.

For the **earlier run’s explicitly normalized** operator `U=(Λ²φ♯)Q♭`, the script rebuilds the whole 15×15 pairing matrix in dimension six from the four-form. With paired bivectors p₁,p₂,p₃, the restriction of U to their span is

`C=(2/3)[[0,1,2],[1,0,3],[2,3,0]]`, and `ξ=(p₂+p₃)/2`.

The exact outputs are `Q(ξ,ξ)=1`, `det(Q)=2097152/59049`, φ equal to the standard symplectic form, `Uξ=p₁+p₂+p₃`, and `det[1,C1,C²1]=−32/27`. Every row sum of C is at least 2. Positive iterates therefore grow strictly and give infinite forward orbits for the specified vectors. This certifies the six-dimensional example under that operator convention.

For the already-proposed family let V have 2m symplectic pairs. Start with a block diagonal matrix with blocks `d_j[[0,1],[1,0]]`, with distinct positive rational d_j, and perturb every cross-block off-diagonal entry by a sufficiently small positive rational ε. At ε=0 the columns `1,C₀1,…,C₀^{m−1}1` have rank m by the Vandermonde determinant in the distinct d_j. Invertibility and that nonzero minor persist for sufficiently small ε. With `s=1ᵀC_ε⁻¹1>0`, put C=sC_ε and ξ=C⁻¹1. Then Q(ξ,ξ)=1 and the induced φ is standard. The determinant of the full four-form pairing is `det(C)∏_{i<j}C_{ij}⁴`, so it is nonzero. Taking d_j∈[1,2] gives row sums greater than 1 for m≥2 after sufficiently small perturbation; the same positive-growth argument applies. The script checks the earlier family for m=2,3,4 and ε=1/1000 and verifies the exact ranks and norms. The openness/Vandermonde argument proves the stated unbounded-dimensional family; these finite tests alone would not. The dimension-four threshold, the tensor-square normalization on the manuscript and the W/V parenthesis remain unresolved source questions.

## 8. Inverse correspondences, positivity, and semisimplicity

If w=uv is invertible and its characteristic polynomial is `t^d+a_{d−1}t^{d−1}+…+a₀` with a₀≠0, Cayley–Hamilton gives `w⁻¹=−a₀⁻¹(w^{d−1}+a_{d−1}w^{d−2}+…+a₁)`. Rational coefficients and composition preserve rational algebraic correspondences; hence `v⁻¹=w⁻¹u`. The script verifies the symbolic 2×2 instance; the displayed equation proves every dimension. This is the proof on scan 48 after explicitly resolving the operator order in mathematical notation, not in the ink.

For a finite-dimensional rational algebra A with involution * and positive trace form, its radical J is *-stable. If a∈J then a*a∈J is nilpotent, so its matrix trace vanishes, contrary to positivity unless a=0. More generally the nonvanishing form hypothesis of Kleiman’s Lemma 3.13 admits the argument with a highest nonzero power of a*a. If the correspondence algebra was initially only embedded in End_K(V), its rational finite-dimensionality can be justified as follows: for any rationally independent a₁,…,a_r the rational positive Gram matrix `(Tr(a_i* a_j))` is nonsingular. Any K-linear dependence among the a_i would give a vector in its kernel. Thus r≤dim_K End_K(V). Merely embedding an arbitrary ℚ-algebra in a finite-dimensional ℚℓ-space would not prove this.

Algebraic splitting of an injection between different varieties requires positivity and algebraicity in the relevant ambient correspondence setting. Under such hypotheses the adjoint construction `(u*u)⁻¹u*` gives a left inverse; analogous formulas give a right inverse for a surjection. Jannsen’s numerical-motive theorem is a distinct later result. A nilpotent homological-to-numerical radical is not necessarily zero, as the algebra of dual numbers illustrates. The present audit does not infer the still-conjectural general homological semisimplicity from the numerical theorem.

## 9. Contextual commutative and homological algebra

**Stalk adjunction.** For a point x, `Hom_X(F,i_{x*}I)=Hom_{O_{X,x}}(F_x,I)`. Stalks are exact and the second functor is exact for injective I, proving injectivity of i_{x*}I among all O_X-modules. This is stronger than merely injective in a quasi-coherent subcategory. Identifying the associated affine sheaf with this direct image uses the standard localization structure of the indecomposable injective over a noetherian ring.

**Derived Hom.** With a bounded-above coherent first argument and bounded-below coherent second argument, only finitely many finite Ext modules contribute to a given total degree. The finite injective-dimension alternative permits truncation of the first argument far enough to preserve any fixed RHom cohomology group. Without these controls, two zero-differential complexes with k in every nonnegative degree have degree-zero Hom equal to the infinite product ∏k; over a field all acyclic complexes split, so this computes derived Hom. The product is not finite-dimensional and therefore is not coherent on Spec(k). It refutes the unbounded extrapolation, not the qualified statement in scan 41.

**Fitting ideals.** Given q generators of M, a q×q minor of a relation matrix annihilates M by the adjugate identity, giving Fitt₀(M)⊂Ann(M). If a₁,…,a_q annihilate M, each a_j times the j-th basis vector is a relation; their determinant yields a₁⋯a_q∈Fitt₀(M). This proves Ann(M)^q⊂Fitt₀(M). The Kähler different is Fitt₀ over B of Ω_{B/A}; an A-linear presentation does not calculate the same ideal.

**Different transitivity.** In the two-equation model f(x),g(x,y), the Jacobian is block triangular with determinant f_xg_y. Under finite flat complete-intersection hypotheses this yields the expected product of differents. The determinant calculation does not establish an unrestricted transitivity formula from the isolated word on scan 52. A trace different additionally requires a generically separable extension.

**Finite-field monogenicity.** An element of 𝔽₂³ has at most two distinct coordinates. The subalgebra it generates consists of functions constant on equal-coordinate classes and has dimension at most two. Therefore no element generates the three-dimensional algebra, although the algebra is finite étale and every maximal ideal is principal. The script checks all eight elements and their zero Vandermonde discriminants. This also disproves the inference that a nonzero discriminant polynomial has a rational nonzero value over every field.

**Étale fibres without flatness.** For A=k[t], B=A×A/(t), the fibre at a prime not containing t is its residue field, and the fibre at (t) is k×k. All fibres are finite étale; B is finite over A. The element (0,1) is nonzero and killed by t, so B is not flat over the domain A. Hence B/A is not étale. This is a completely checked counterexample to the isolated criterion, and finite flat plus étale fibres is the established refinement.

**Unramified local structure.** A finite-type unramified neighborhood is a quotient of a standard étale algebra; it need not itself be étale or flat. The full Stacks10.152.1 proof constructs a monogenic subalgebra with the same indicated local ring, then a monic relation with derivative invertible. The kernel can contain additional relations. Only in the étale case does one obtain the standard étale local presentation itself (Stacks41.12.1). Thus the source’s monogenic-subalgebra assertion is not replaced by an invalid unramified-implies-flat statement.

**Limits of these checks.** The loose typescripts contain incomplete hypotheses, old pagination, cancelled text, and external authors’ results. None of the elementary checks above proves an unidentified theorem by Shatz, all SGA 3 corrections, or the proposed EGA editorial history. Those have separate searched literature records and confidence assessments.
