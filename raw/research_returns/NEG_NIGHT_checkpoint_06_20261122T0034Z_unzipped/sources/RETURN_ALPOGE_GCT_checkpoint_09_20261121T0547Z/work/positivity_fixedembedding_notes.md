# P-F16: proof and scope notes

Author/reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-20 UTC.

## Statement produced

`positivity_fixedembedding.tex` proves a uniform bound for all considered ray diagonals of one fixed positively multigraded complex domain. If the fixed homogeneous generator matrix is `M`, `m` is the number of generators, and `Delta` is the maximum absolute nonzero square minor (with one included), then every ray algebra is generated in ray degrees at most `D=m Delta`. For rays whose algebra is nonconstant, Cohen--Macaulay, and has a global quasi-polynomial Hilbert function, put `L=lcm(1,...,D)`. There is an h.s.o.p. all of degree `L`, a nonnegative numerator `H` of degree `<rL`, and

`s(f) <= p(f) <= max(0,deg H-L) <= (r-1)L <= (dim R-1)L`.

The last sharpening was suggested by root and is independently proved in the text by factoring each binomial constituent after the shift `max(0,deg H-L)`. The theorem has no historical-priority claim.

## Whole-proof check actually performed

I reread the entire written proof, rechecked each inequality and reduction, and then checked the revised final bound. This is a same-agent targeted whole-proof check, not an independent re-proof or a formal certificate. The following points were explicitly checked:

- Positivity of the linear functional makes all relevant components finite dimensional, kills nonzero degree-zero monomials, and bounds each polytope cross-section.
- A vertex has independent support columns; Cramer's rule uses a square minor of the fixed matrix, not a minor involving the varying ray. Hence the primitive ray's last coordinate is at most `Delta`.
- The proof that the bounded cross-section is a convex hull of these vertices is included by support reduction in both directions of a kernel vector. That vector must have both signs.
- The cone dimension is at most `m` because its last coordinate is determined by the first `m`. Conical dependence reduction leads to at most `m` independent rays. Subtracting integral coefficients leaves an integral residual of degree `<m Delta`. The zero vector is handled separately so no invalid `0<0` inequality remains.
- Passing to a quotient preserves generation degree because the original map is multihomogeneous and surjective degree by degree. The number of possible low-degree semigroup elements can depend on the ray, but it is finite; only their degrees are uniformly bounded.
- Each generator satisfies a monic equation over the degree-`L` subalgebra. Finite generation by integral elements gives a finite module, so dimensions agree.
- The homogeneous Noether-normalization induction is supplied in full. Dehomogenization of a nonzero homogeneous relation is nonzero; choosing a suitable point over the infinite field makes the relation monic in the last generator. The induction retains degree-one generators in the regrading.
- The finite parameter quotient is connected graded and Artinian, hence has the unique homogeneous maximal ideal. Going up gives full local dimension. The exact Cohen--Macaulay regular-parameter theorem applies locally, and the nonzero scalar constant term of any element outside the homogeneous maximal ideal detects every nonzero homogeneous kernel globally.
- The regular-sequence exact sequences yield a polynomial Hilbert **series** with nonnegative coefficients. The text was corrected from the potentially misleading term “Hilbert polynomial.” Global quasi-polynomiality is used for properness and to identify eventual constituent formulas with global constituents; the isolated constant algebra is excluded from this part.
- Equal denominator degrees allow the sharper direct coefficientwise shift bound. For `r=1`, the empty product gives positivity index zero. The final dimension comparison uses the subdomain hypothesis and transcendence degree.

## Exact external locator

The only new external theorem invoked beyond the earlier paper's properness argument and elementary algebraic dimension facts is the Cohen--Macaulay parameter criterion: **Stacks Project, Lemma 10.104.2, Tag 02JN**, <https://stacks.math.columbia.edu/tag/02JN>. I opened the exact statement and verified the hypotheses. Own refs: `turn142233113view0`, `turn142233113search0`. It says that in a Noetherian local Cohen--Macaulay ring, a sequence cuts the expected dimension if and only if it is regular. The text explains the graded localization step instead of silently treating the cited local statement as a graded one.

## Remaining gate

This theorem does not automatically apply to the full `C[GL/U]` branching algebra: determinant units violate the strict positive-functional hypothesis. An application must produce a suitable polynomial branching algebra with the required positive grading and identify its components with the multiplicity spaces; it must also verify the diagonal Cohen--Macaulay and global-quasi-polynomial hypotheses. This is explicitly left as input to verify.

The quantities `m`, `Delta`, and especially `L` depend on the fixed algebra and its embedding weights. The torus counterexamples P-F14--P-F15 show that this dependence cannot simply be dropped. The formula involving an l.c.m. is an effective finite bound, but no polynomial bound in binary input or polynomial-time construction is claimed. Even polynomial numerical control of `m Delta` alone does not establish a polynomial bound for this particular `L`.

Root independently read the initial full proof and found it valid, then suggested the sharper final shift. Complexity has reported a complete independent reconstruction of the final proof, including that shift and the exact Stacks hypothesis check, with no gap found. Its event is recorded by that reviewer in its own check ledger; this note does not substitute for that event. The author files are now stable for merging.
