# Independent whole-proof review: I-31

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:47:16Z.

Scope: complete reading and independent mathematical rederivation of `I31_rank_spectrum.tex`. I also reopened Liu's primary PDF and read the whole image-cone argument in section 3.3, printed pp. 7–8, to check the attribution and the relation to the written specialization. This review does not certify the source's affine-orbit theorem or other unreviewed sections. No numerical computation was needed for the cone argument. This is an independent agent proof review, not a formal proof certificate or external peer review.

## Verdict: PASS

The proof gives an original-coordinate hitting generator for arbitrary fixed-width ROABPs in one hidden variable order, with the stated rank-spectrum-dependent pair count. Its sample count has the displayed exponent and does not establish a bound polynomial in variable width.

## 1. Cone equality and the critical deletion

The scalar image cone is the closure of the image of an irreducible parameter space, so it is irreducible. Equality of these cones preserves homogeneous identities. Composition on disjoint parameter blocks is valid: scalar multiples of the original matrix values are dense in each cone, their product is dense in the corresponding product domain, and a regular multiplication map has the same image closure after replacing its domain by a dense subset. Scalars in separate factors are absorbed into one scalar for the resulting product. This uses no field characteristic restriction.

For rank-`s` blocks with constant `P_s`, projection onto the first `s` columns makes the prefix cones nested. The zero parameter value of each new block fixes these projected columns. Since the initial projected matrix is nonzero, its cone is a line, and the ambient dimension `as` bounds the number of strict inclusions by `as-1`.

The deletion lemma is sound. Fix a next-block value whose active `s x s` block `E` is invertible; these values are dense because `E(0)=I_s`. Since this block has rank `s`, any left multiple is uniquely determined by its first `s` columns `Q` and equals `Q[I_s,E^(-1)F]`. After fixing the previous block to `P_s`, the projected cone at this fixed next-block value is precisely `VE`. It is contained in the original projected cone `V` because this is an actual restriction. Right multiplication by `E` is an invertible linear map on the projected matrix space, so `VE` is closed, irreducible, and has the same dimension as `V`. Proper containment would lower dimension; hence `VE=V`.

Every original output at the fixed next-block value has its projected columns in `V`, so the graph formula puts it in the restricted full cone. Taking closures over the dense next-block values proves full-cone equality. The reverse inclusion is automatic. This argument does not require the projected image itself to be closed, only its cone closure, and it correctly uses closure at each fixed next-block value.

Deleting one block leaves its own projected cone unchanged and leaves the following full cone unchanged. All later full and projected cones are therefore unchanged by disjoint-variable composition. Consequently successive deletions of all but the last block of each nongrowth run remain valid. Retaining strict-growth blocks and those last nongrowth blocks costs at most `2as-1`, including the cases of no growth, an empty run, or an empty word. Taking `R=I_w` gives the stated `2ws-1` bound without any first-block function-field argument.

## 2. Recursive coordinate compression

If the full word has rank `s`, every interval has rank at least `s`. Greedy shortest rank-`s` prefixes therefore produce rank-`s` blocks; each prefix chunk preceding the last factor has rank strictly greater than `s`, as do all its subintervals. If the final remainder has no rank-`s` prefix, its full rank is greater than `s`, and absorbing it into the last block keeps that block's rank exactly `s`. The same statements hold for constant ranks because all original intervals are preserved at zero.

At the block cuts, transported active spaces are complementary to the row kernels of the next rank-`s` constant block. Their adjacent products retain rank `s`. Choosing those kernels as passive spaces and transporting active bases makes every block constant exactly `P_s`. The gauge changes at the two ends are fixed invertible linear maps and do not affect zero-coordinate restrictions or cone equality.

After the deletion lemma retains at most `2ws-1` blocks, induction compresses the disjoint higher-rank prefix chunks and the possible final tail. Keeping the central one-variable factor gives at most `2D_s+1` positions per retained block. Cone equality composes through the unchanged central factor and all other blocks. There is no need to assume that arbitrary restrictions preserve image points exactly; equality of the scalar cone is the invariant used throughout. In fact rank preservation at zero also prevents a zero-coordinate restriction from lowering a generic interval rank below its original value.

The full-rank base case is valid independently: gauge the constants to identities, retain strict prefix-cone growths, and use dimension `w^2` starting from the line through the identity. This proves the recurrence for every allowed full-word rank.

## 3. Ground-space endpoints and rank descent

The rectangular absorption formula is exact: a constant right inverse of the full-row-rank endpoint gives `L_0 B(Y)=L(Y)`, with `B(0)=I_w`. Its determinant has constant term one. The column endpoint uses a constant left inverse and is identical in form. Therefore both new factors are generically invertible and preserve every generic and constant interval rank. This remains in the original `w`-dimensional matrix space and does not invoke a compound-space dimension bound.

A nonzero selected rank-`r` minor implies that the two selected rectangular endpoints have generic row and column rank `r`. Their nonzero univariate minors remain nonzero at every current center, since each coordinate is the original indeterminate `t` plus corrections independent of `t`. Equivalently, setting the previously introduced amplitudes to zero leaves a nonzero univariate polynomial at `t`. Single-factor tests can be written with one constant endpoint; empty interior chunks cause no exception.

After absorption, the interior word has only already preserved ranks greater than `r`. Cone compression applies to the complete enlarged word, including the endpoint variable positions. The selected determinant is a homogeneous polynomial of degree `r` in the full matrix entries. If its restriction were identically zero, it would vanish on the restricted cone and hence on the original equal cone, contradicting its chosen nonvanishing. Thus it has a nonzero restriction to at most `D_r` coordinate positions and is detected by that many fresh SV pairs.

Finitely many selected test minors survive simultaneously because their substituted product is a nonzero polynomial. Earlier ranks survive at zero new amplitudes. The previously checked local-test induction therefore preserves all internal ranks in descending order. Once all are preserved, the original nonzero scalar output is a homogeneous linear functional of the full word, and one final cone restriction followed by fresh SV pairs detects it.

## 4. Count and field scope

The recurrence makes `d_s` strictly increase as the allowed rank decreases, with each new value greater than twice the preceding maximum. The preservation cost at rank `s_i` is consequently `d_(s_(i+1))`; the final scalar cost is `d_(s_1)`. Their sum is exactly the stated `K_R`. Also `d_s+1 <= 4w^2(D_s+1)` and `d_w+1=w^2`; summing the resulting geometric decrease proves the displayed upper bound `2w^2(4w^2)^(L-1)`.

For the full spectrum, every nonzero ROABP has positive generic internal interval ranks: a zero interval matrix would make its scalar output zero. Thus the full positive rank set covers all nonzero width-at-most-`w` instances after padding, including instances where rank `w` never occurs. The common-center full-rank stage is simply vacuous in that case. The construction remains independent of the hidden order.

All geometric arguments may be carried out over an algebraic closure; a nonzero coordinate restriction found there is still nonzero over the original coefficient field. The final polynomial generator uses only the chosen working-field interpolation nodes. The Newton-simplex sampling argument needs distinct nodes rather than characteristic-zero factorial inverses, so the stated arbitrary-characteristic and extension-field conventions are consistent.

The resulting fixed-width statement is therefore proved by the written argument. A fixed number of rank levels gives polynomial pair count in `w`, while evaluating the full parameter grid still has exponential dependence on that count. Neither this proof nor the cited source provenance supplies a polynomial-size variable-width hitting set.
