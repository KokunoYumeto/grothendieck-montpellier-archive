# Independent whole-proof review of AM-R-013

Reviewer: GPT-6 Astra Pro, /root/lift_accounting, ALP_MACHINE, 21 November 2026 UTC.

I read selected_analytic_source_predicates.md in full, R13.1–R13.13 and the source/scope discussion. I also read the literal predicates in CayleySignature.lean, lines106–166, and the TPar, Interlace, block, Dpar, Xpar and Centred definitions in DataTheta.lean, lines501–555. Goodman and Wallach (2009), Theorem8.1.1, printed p.364, was opened directly in the primary book PDF and its exact integral-weight interlacing statement checked.

**Result: PASS in the stated analytic interpretation.** This is a targeted independent proof check. It is not a Lean build, a new proof of the accepted local theta theorems, or an arithmetic row comparison.

The algebraic theta-image extraction is sound. Fixed finite level and compact real type give a finite-dimensional automorphic space; a nonzero first image therefore has a nonzero contribution from an actual irreducible source embedding. Local Howe uniqueness fixes the target isomorphism type at every place. Its finite global multiplicity makes the smooth isotypic module a finite direct sum of simple modules. Its algebraic theta span is therefore semisimple and contains an actual irreducible target copy. Every member of that copy is a finite sum of actual theta images by the definition of the algebraic span, and finite tensor decompositions give the source's factorizability requirement. ALP-LIFT-14 applies to each chosen actual embedding, including multiplicity copies. No passage from a merely dense Hilbert image to an algebraic identity is being made.

At the terminal even index \(m\), DataTheta's eta shift vanishes and all signature labels are positive. The \(X\)-list consists of the original \(k\) half-integers and \(m\) blocks of length \(t+1\); the \(Y\)-list consists of the original \(k-1\) integers and the \(m\) pairs \((-b_j,B_t(-e_j))\). The source Interlace and Centred inequalities place each intervening \(-b_j\) strictly between the appropriate block endpoints. The shorter block entries are the exact half-step midpoints. Subtracting the respective rho shifts converts strict HC interlacing to the weak highest-weight inequalities
\(\lambda_i\ge\beta_i\ge\lambda_{i+1}\).
The primary branching theorem applies to all dominant integral weights, including determinant twists, and gives the stated multiplicity one. The real conjugacy of the actual positive codimension-one subgroup suffices; no rational standard-basis isometry is needed.

The restriction detector also checks. The skew-Hermitian Lie algebra is an \(F'\)-vector space; weak approximation in its coefficients and the rational Cayley chart prove density of \(G(F')\) in the full real compact product. The Cayley denominator is invertible on real skew-Hermitian matrices, and the image omits only the closed eigenvalue-minus-one locus. Irreducibility of the real type ensures that a nonzero evaluation functional does not vanish on every translate of its nonzero branching subspace. A rational approximant therefore makes the desired evaluation nonzero.

For the finite right translate, left rational automorphy gives
\(\phi_v(\iota h,q_f^{-1})=\phi_v(q_\infty\iota h,1)\),
with precisely the order written in the proof. Finite translation commutes with the real right action, so choosing the branching vector before the translate ensures that the entire restricted function, at every finite point, has the selected terminal type. Its conjugate is an actual cusp form on the compact subgroup quotient. With the source's two conjugations, the terminal period becomes the positive squared restriction norm. This matches the quantified IsDv and PerNZ conditions read in the source.

The finite-class measure decomposition retains
\(\operatorname{vol}(K_H)/|\Gamma_c|\) and real Haar volume one, exactly as required. The unknown finite denominator of the rational translate, its resulting level, the arithmetic coefficient lattice, and the equality with the prescribed terminal matrix remain explicit. The other four AdmS predicates and old D7 construction are not claimed.

A typesetting defect in R13.9 was reported to the author: the exponent printed as \(^{,2}\) should be \(^{2}\). It does not change the proof.

Primary locator: Goodman, R., & Wallach, N. R. (2009), Symmetry, representations, and invariants, Theorem8.1.1, p.364, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/goodwallx.pdf (zero-based PDF page382).

