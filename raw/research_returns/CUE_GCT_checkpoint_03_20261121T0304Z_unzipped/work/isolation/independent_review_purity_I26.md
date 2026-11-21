# Independent whole-proof review: I-26

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

**PASS after the two finite-field scope clarifications.** I read the entire proof and independently checked the determinant construction, minor-translation representation, all ten coefficients of the explicit quadratic, its width-four representation, and the matroid repair. The revised wording explicitly requires enough field or extension nodes for the width lower-bound consequence and for the final univariate sampling grid. No formal verification or external peer review is claimed.

## Determinant and centered annihilation

The kernel conditions impose at most `k+1` linear constraints on a `2k+2` dimensional polynomial space, so the required `k+1` independent polynomials exist. Evaluation on `n>=3k+2` distinct nodes is injective at degree at most `2k+1`, giving full row rank of `V`. Every maximal Vandermonde minor of `U` is nonzero. Hence a nonzero maximal minor of `V` gives a unique nonzero multilinear coefficient of the Cauchy–Binet expansion, in any characteristic.

The orthogonality equations are exactly `UV^T=0`, giving invariance under the common translation before taking the determinant. Each product `Y^i q_j(Y)` has degree at most `3k+1<=n-1`, so Lagrange reproduction is an exact polynomial identity, including over finite fields. The substituted matrix is a sum of only `k` outer products, while its size is `k+1`; its determinant vanishes identically. This is a genuine dense-generator annihilator, unlike a support lower bound alone.

## Any-order invertible representation

The vector of all square minors, including the empty minor, has the stated size by Vandermonde's binomial identity. Distinct minors have different row/column multidegrees, so they are linearly independent as polynomials. A rank-one translation changes each minor by a linear combination of smaller minors with exactly the cofactor signs shown. Two translations in the same direction, compared in two independent parameters, give `N^2=0`; different translation directions commute. Linear independence of the minor coordinates justifies both matrix identities without division by factorials or a characteristic restriction.

The full determinant selector and empty-minor selector give the scalar polynomial. Thus all interior factors commute and are invertible with identity constants, and every interior interval has full generic and constant rank. Appending rank-one endpoint matrices makes the final word an actual rank-one local test as in I-21, since every proper interior suffix remains full rank. This verifies the advertised test-class membership.

If the field or an allowed extension supplies `3k(w)+2` distinct nodes, universality for widths at most `w` requires `binom(2k(w)+2,k(w)+1)>w`. The resulting logarithmic necessity is valid; it neither rules out a logarithmic upper bound nor applies without a sufficiently large admissible number of variables/nodes.

## Explicit width-four quadratic

I checked the two kernel conditions for both displayed rational polynomials on `0,1,2,3,4`. Expanding their two-row minors against the Vandermonde minors gives, in the listed order, coefficients

`(6/5)*(3,-4,-15,16,4,8,-15,4,-4,3)`.

This matches every coefficient of `Q`. The ten products `a_i b_j` for `i<j` give the same unscaled list; in particular the entries with denominator `97` give `4,-4` and the last pair gives `3`. All triple products of the four-by-four block matrices vanish, and the linear/constant scalar contributions are zero. Therefore the claimed ordered product is exactly `Q`.

The smaller four-dimensional representation is only claimed in its displayed order and need not have square-zero or commuting individual `N_i`; its upper triangular unit diagonal is sufficient for invertibility. This is consistent with, and distinct from, the general commuting width-six construction for `k=1`.

## Matroid repair

Because every `U_S` is nonzero, the polynomial's support is exactly the set of column-matroid bases of `V`. Strictly distinct element weights have a unique minimum-weight matroid basis by greedy exchange. Therefore the coefficient of the least power under `X_i=T^i` cannot cancel, so the curve pullback is nonzero with degree at most `n(k+1)`. The repaired scalar grid requires that many plus one distinct elements, using an extension when necessary; the revised statement now says so. This establishes a repair for this particular family, rather than a general cocharacter hitting theorem.

## Independently checked primary-source scope

I opened the publisher PDF of Hu, van Melkebeek, and Morgan, *Polynomial identity testing via evaluation of rational functions*, *Theory of Computing, 20*(1), 1–70 (2024), DOI https://doi.org/10.4086/toc.2024.v020a001 , at https://theoryofcomputing.org/articles/v020a001/v020a001.pdf . I read the exact statements and local explanatory text of Theorem 1.3 on printed p. 6, Corollary 1.5 on p. 7, and Theorems 1.9–1.10 on p. 10. The determinantal generators, degree `k+1` and `2k+1` variable count for uncentered SV, and the retained low-degree-monomial hypothesis in the ROABP statements are accurately represented. I did not independently reread all proofs of that 70-page source. The source itself attributes the degree conjecture to Fournier–Korwar; the older slide deck was not separately reread in this review.
