# Fresh independent review: F34 compact-input dimension obstruction

Reviewer: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 UTC. Verification type: full direct report read, complete independent proof reconstruction, and exact supplied-TeX/primary-PDF-text source check. No formal proof assistant or numeric sampling was used.

Reviewed report: `agent_plethysm_dimension_gate.md`. The initial complete read covered SHA-256 `8ee31a8c17b18abc715f89cd33729a53466e60de9848d89d7efc2974174dd052`. The author then applied the two locator-only corrections below; the corrected report has SHA-256 `2074e18c0c9e27f8521cf68117645c9c610ee2361de99ba50ab9abaaa64a23fa`. The mathematical text is unchanged.

**PASS. No mathematical blocker.** The conclusion is a contradiction to the literal uniform compact-input bound in the supplied 2009 VI formulation. It is not a contradiction to positivity, the actual simplex formula, or a formulation charging the numerical inner weight or ambient rank as an input-size parameter.

## 1. Exact source and conventions

I directly read the complete supplied VI Problem `pintroplethysm`; the input-length paragraph; the full fixed-inner-weight stretching definition; all three clauses of `hph1plethysmintro` and their surrounding justification; and the entire explicit compact-encoding discussion in the opening of §3.4. I also matched their numbered statements to the downloaded v4 primary PDF's extracted text.

The actual source is Hypothesis **1.6.4**, printed p.23, with the ambient dimension polynomial in the bitlength of the inner partition and the heights of the outer and output partitions. The following 1.6.5 is SH. Equation (1.5), printed p.20, stretches the outer and output labels and explicitly keeps the inner label fixed. The general plethysm problem permits `H=GL_2`, `mu=(k)`, `G=GL_(k+1)`, `lambda=(1)` and `pi=(k−1,1)` with no additional restriction invalidating this family.

The source deliberately suppresses zero parts, including the trailing zero parts of a highest weight for a very large `G`. The original `H` has fixed rank two in the example. Thus neither the rank of `H` nor a hidden padding convention restores a polynomial-in-log-k dimension bound. The complexity wording is uniform across the family; allowing the bounding polynomial to depend arbitrarily on the inner input itself would remove the asserted uniform bound rather than satisfy it.

The two corrected locators are:

- The source problem begins at supplied TeX line 414, not 426; `pintroplethysm` is the stable label.
- The explicit zero-padding clarification is in the opening of **§3.4**, printed p.53, immediately before the heading §3.4.1. Its supplied TeX passage around lines 2899–2915 is correct. Calling it part of §3.4.1 was the only section-level discrepancy found.

## 2. Independent derivation of the actual coefficient

In `Sym^N(Sym^k C^2)`, a monomial in the `k+1` weight vectors has exponent tuple `(a_0,...,a_k)`, with `sum a_i=N` and second-coordinate weight `r=sum i a_i`. At `r=N` or `N−1`, every tuple of nonnegative `a_1,...,a_k` with weighted sum `r` has ordinary sum at most `r<=N`; therefore it admits exactly one nonnegative `a_0`. These weight multiplicities are the partition numbers with allowed parts `1,...,k`.

For polynomial GL2 modules of total degree `kN`, the weight multiplicity at second-coordinate exponent `r<=kN/2` is the cumulative sum of highest-weight multiplicities with second part at most `r`. Subtracting the preceding weight multiplicity therefore extracts the constituent `((k−1)N,N)`. The condition holds at `r=N` for every `k>=2`. Cancelling the part-one factor gives exactly

`c_k(N)=[z^N] product_(i=2)^k (1−z^i)^(-1)`.

This independently establishes D3 for every nonnegative stretch `N`, including `N=0`; it does not infer equality from sample values. I also read PPS Lemma 1.3 and its full two-variable Weyl-character proof, in the original local text and the v3 statement. The different notation for outer/output partitions is translated correctly. The width-bound simplification in the report is valid at both `N` and `N−1`.

## 3. Exact dimension lower bound

The weighted simplex has vertices `e_i/i` for `i=2,...,k`; these are affinely independent in the stated hyperplane, so its dimension is `k−2`. Its dilations count the coefficient exactly.

For `L=lcm(2,...,k)`, assigning `x_i=(L/i)y_i` to every weak composition `sum y_i=s` is integral and injective, and its weighted sum is `Ls`. The count of such weak compositions is `binom(s+k−2,k−2)`. The separate upper bound follows by choosing any `k−2` of the variables, each bounded by `N`, and solving for the remaining one. Thus the growth exponent is exactly `k−2`.

For an arbitrary bounded polytope of affine dimension `d`, the report's coordinate-projection proof of `O(N^d)` is valid: select `d` coordinate functions that are independent on the direction space. Their joint map is injective on each affine hull, sends integral points to integral points, and sends the dilated bounded set into a box with side lengths `O(N)`. This remains valid when the affine hull is translated or not rational. Comparing the two bounds on the unbounded progression `N=Ls` proves the lower bound on every candidate dimension, even for eventual equality of counts.

The fixed base labels have bitlength `O(log k)` and heights one and two. Since `k−2` exceeds every fixed polynomial in `log k`, the literal uniform PH1(2) bound fails. The actual positive simplex shows that this particular deduction is independent of a failure of Ehrhart existence: existence holds on this family, whereas compact dimension does not.

## 4. Full check of the output-size corollary

For `k=2m`, `N=m(m+1)`, the independent choices `x_(2i) in {0,1}` for `i=2,...,m` have total weighted cost at most `N−2`, and all costs are even. Filling `x_2` as displayed is therefore integral and nonnegative; distinct choices give distinct tuples. This proves the lower bound `2^(m−1)` exactly.

The four positive partition parts are `N`, `2m`, `(2m−1)N`, and `N`; each has `O(log m)` bits. The coefficients have binary output length at least `m`. A #P function on input length `L` has at most `2^p(L)` accepting witnesses for some fixed polynomial `p`, hence at most `p(L)+1` output bits. Along this family `m` exceeds every polynomial in `L=O(log m)`. This excludes a uniform #P representation for the fully compact binary function without a complexity-separation assumption.

This says nothing contradictory about unary-size #P statements or about the explicitly listed rectangular Kronecker input: the two rectangles there already require at least `k` listed parts. The distinction between these input conventions is necessary and is retained in the report.

## 5. Historical status and scope of this review

The report correctly identifies Kahle–Michałek's published non-Ehrhart ray as a prior result, not a new finding of this investigation. I independently opened and read their complete primary paper; a separate audit reconstructs the particular fixed-inner-weight ray and the reciprocity contradiction. That known result refutes universal ordinary Ehrhart existence; the present direct family isolates the additional dimension/input-size issue even where a positive simplex exists.

The effect on the research program is precise: a proposed purity or canonical-basis argument cannot prove the literal false conclusion under these parameters. Revised bounds, unary/rank-sensitive formulations, inhomogeneous objects with appropriately stated complexity, or nonpolyhedral counting rules require distinct claims. The underlying actual multiplicities and their representation/Satake interpretations remain compatible with the calculations.

Suggested check event: `F34-DIMENSION-GCT-FRESH`, full proof and exact-source review, PASS with the two locators corrected. This is a report review, not a final-text match to a later generated F34 fragment.
