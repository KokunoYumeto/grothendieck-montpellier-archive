# Independent whole audit of D-HES-04–06

**Result: PASS.** The complete proof excludes the stated irreducibly acting normal products of higher symplectic groups over every even field, including arbitrary mixed fields and compatible outer, scalar and tensor-permutation actions.

- Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed; HODGE_DIVISION.
- Actual audit record time from the clock tool: **2026-11-21 19:04:29 UTC**. The complete proof reading and independent arithmetic run were finished before this timestamp.
- Reviewed mathematical file: `agents/imprimitive/lie_small_fields/higher_even_symplectic_all_fields_section.tex`.
- Mathematical SHA-256: `ab4898d2725c48b0993539ead8e56c27b9630f0433aee185514c48ab1546ae18`.
- The author reports the final status-only SHA-256 `542df27baf0e3810906e03585b967d1cebaf083302b2df85ffc13232a616e837`; no mathematical change is reported.

## Whole proof

The elementary degree bound is valid over every finite field: the embedded GL_n(q) row subgroup has q^(n−1)−1 nontrivial additive characters, transitively permuted by its Levi subgroup. Faithfulness forces all of them to occur. The q4 endpoint378 follows from restriction to the actual block Sp6(4) subgroup and the previously checked complete ESC table.

The general-field shear construction is sound. Diagonal entries of vvᵗ recover v because squaring is bijective in a finite field of characteristic two. The h-normalized elementary subgroup is subsequently treated as an F2-module; no unsupported Fq-linearity is asserted. The line-parabolic construction has the displayed group law and remains abelian of exponent two over all even fields. Odd-order averaging supplies the fixed hyperbolic pair. Maschke's theorem over F2 then gives a fixed-point-free subgroup U of order at least4.

The weight-orbit calculation gives inner support at least `(1−c(q))/2`, for both odd-prime parabolic elements and involutions. In the elliptic case, the trace-defined Hermitian form, norm-surjectivity argument, multiplicity-one primary decomposition and product-of-tori centralizer are correct over F_(q^(2d))/F_(q^d). The universal elliptic estimate is already below1/2 at n4,q4, and the displayed monotonicity proves it for every later rank and field. Fourier inversion bounds every eigenspace. Prime-order powers have the correct support inequality direction.

For q≥8, the commutator of a nonscalar normalizer with a suitable core element is nonidentity. Since the core is faithful and centerless it is nonscalar. The rank-of-commutator inequality then gives support greater than7a/64. This covers every compatible outer automorphism without assuming its order or type.

For q4, the published outer group is C2, and the natural-trace witness correctly shows that entrywise Frobenius represents its nontrivial element. A nontrivial inner square transfers the core a/8 bound. If the automorphism squares to identity, its semilinear lift has square1 because the symplectic group is centerless. The explicit fixed-space identities `a=v+s(v)` and `b=ω²v+ωs(v)` give `v=b+ωa`, and applying s to a dependence proves the fixed F2 basis is also an F4 basis. The restricted pairing is F2-valued and nondegenerate, yielding a symplectic descent by a genuine core element. This checks the whole descent, not just its dimension count.

After scalar normalization T²=1, the row-group characters have equal nontrivial multiplicity m. The averaging inequality gives m≥a/(4N). Frobenius fixes exactly M=2^r among N=4^r parameters; all other characters occur in pairs. Each paired weight sum has equal plus and minus eigenspaces of dimension m. Therefore support is at least `(N−M)m/2`, yielding7a/64 when r≥3. No claim that an eigenvalue-specific bound survives an arbitrary tensor convolution is made.

The full normal-product argument is valid with different field sizes. Factor-preserving intertwiners use normalized multiplicity convolution. A genuine factor-permutation cycle has the stronger quarter bound by weighted word-orbit counting; finite order ensures the cycle product is diagonalizable. Gow's reality theorem yields a unique invariant bilinear-form line on the whole tensor product. Its multiplier is nontrivial by inclusion of the original imaginary quadratic field in the inducing character field. The actual intermediate-cover factorization forces genus zero and at least twelve effective branches if rank is nine. Two nontrivial multipliers cost at least e; the remaining ten cost at least7e/64, giving e≤64. Multiple factors have degree at least35², a single q4 factor at least378, and a single q≥8 factor at least511. The remaining single q2 case is correctly handled by the previously checked sharper e≤24 theorem. All stated cases are exhausted.

## Corrected proposed bound and source audit

During the derivation, the proposed assertion `c(8)<1/2` was rejected by a fresh visual inspection of Liebeck's original author PDF, Theorem2.4(i), numberedp4. The denominator is **sqrt(q)−1**, with the subtraction outside the radical. The proof now uses the correct comparison c(q)<9/16 for q≥8, equivalent at q8 to625<648. This yields core7/32 and normalizer7/64, which suffice. The former stronger proposal is not used or retained as a checked theorem. Existing q2 and q4 statements only use the unchanged3/4 bound.

Li–Xia, *Factorizations of almost simple groups with a solvable factor*, Memoirs AMS279(2022), no1375, author arXiv1408.0350v3, §2.2.2 and Table2.1 on numberedp14, were freshly read in full relevant context and rendered visually. The table states Out(PSp_(2m)(q))=C_(2,q−1)×C_f for (m,p)≠(2,2). Thus the q4,n≥4 conclusion is exact. Local original PDF SHA-256 is `4ef16aa4308f8c487a06e9c8e84ece77247d0e763146f0215d8e109e443e3a93`. The fresh browser opening of its arXiv URL was disabled; the retained actual primary PDF was read locally, and this is not labelled a successful browser retrieval.

The previous complete HHM exceptional-multiplier, Gow and ESC source checks retain their recorded scopes. No unavailable GM1998 theorem is used, and the computed Sp12(2) table is redundant.

## Independent exact arithmetic

`audit_higher_even_all_fields.py` and `.json` were independently written and actually run, PASS in **0.019795 seconds**. They use no author code. The complete Sp2(F4) toy model has60 matrices,10 semilinear-involution cocycles and six fixed symplectic bases per cocycle; all160 vector descent identities pass. The independent character calculation checks all4096 rank-three dual weight pairings, with64 parameters and8 fixed. It also checks every rational7/32,7/64, elliptic and degree64 constant. These computations are explicitly arithmetic witnesses for the separately read universal proof, not an extrapolation from finitely many group dimensions.

No character-table reconstruction or TeX compilation is claimed. All arithmetic and source qualifications above are part of this PASS.
