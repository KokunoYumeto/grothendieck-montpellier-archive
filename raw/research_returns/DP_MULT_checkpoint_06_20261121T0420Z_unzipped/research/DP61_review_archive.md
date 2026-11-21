# DP61 — independent complete source-interface and polynomial review

**PASS.** Checker `/root/archive_binomial`, GPT-6 Astra Pro; runtime effort not exposed. Date2026-11-21 UTC. The entire seven-section memo was read at04:02:35; the mathematical and exact-source challenge closed at04:04:22. Whole memo SHA256: `9e3bc5cc5b2f116712e7d9359df7f8f33c04661f3b3cd32db21ec8400ed5e4e5`. No correction to the mathematical statement or proof was requested.

## Exact selected component

The source rank definitions give P=k+j−1, Q=m−j and the column count nV=k+m−1+t, independently of the growing endpoint rank N(j). I checked the original Ranks and HCParam fields. Strict interlacing, half-integrality ofu and integrality ofv,b,e justify the integer gap deductions.

The aPl and aMi definitions, their exact identification theorems, KapIs and kapTop were read. The negative partition really is reversed: aMi at rown equals aMinusQ at c=Q−1−n. The wtA definition places these partitions at conjugate embedding pairs, and the thGen/RecPJ interface uses that precise weight component and the fixed column count. No free reordering or arbitrary choice of row degrees was used.

The Wts.Ok condition fixes RowPar.of(hc), and RowPar.of is explicitly the triple(v,b,e); thus varying the word does not vary the selected partitions. The first and lastu values are separately fixed, while interioru values may vary. The source nonvanishing theorem's stated global-law, rank, level, harmonic-existence and last-positive-row conditions were read as hypotheses, not silently supplied for the new mixed CM geometry.

## Positivity and literal first-row exclusion

Successive sigma entries have gaps at least one, including the transition from the finalv to−b0. Theb gaps are at leastt+3. Subtracting the linear staircase makes A antitone, and its last entry is at least one. The C sequence starts at least one and rises by at leastt+2, so its reversalB is antitone and positive. The displayed first-row gap identities follow exactly. SinceP≥5, the unchanged DP58 polynomial has zero degree in an active later positive row whose prescribed degree is positive. Its exclusion from this component is therefore literal and valid; no stronger universal exclusion follows.

## Harmonic completion and primitivity

Subtracting a fromA0 andb fromB0 preserves dominance precisely under the displayed first-row-gap conditions. Prefix-row determinant products have the requested row degrees by telescoping, and the source's row additions add an earlier row to a later row. Each prefix determinant is invariant under those additions.

The chosen positive filler columns, negative filler columns, and two kernel columns are disjoint. Therefore every matching-column mixed derivative either has no variable of one sign or acts only on P_(a,b). The latter contraction vanishes by the exact two-term binomial recurrence. This accounts for all product-rule cross terms. Other embedding pairs use disjoint variables and can reuse the same column indices.

The diagonal monomial of the filler has coefficient one: any non-diagonal term would introduce an off-diagonal variable absent from that monomial, and nonnegative exponents cannot remove it. The s=0 term of P_(a,b) has coefficient one in the separate two columns. Hence the completed polynomial is nonzero and primitive over the integers. The source determinant lemmas confirming integrality, harmonicity, row invariance and row degree were actually read; the new content is their combination with this two-column factor and the precise residual-degree condition.

## Pure-kernel vanishing and finite windows

A nonconstant filler monomial differentiates some filler column in only one sign of variables. The normalized kernel restricts to one on either coordinate axis, so that positive-order derivative is zero. Columnwise factorization kills every summand. For the actual selected partitions the filler is necessarily nonconstant because later positive rows stay positive. Thus polynomial completion alone cannot transfer the nonzero pure-kernel value.

The cloud_v and be_close fields were read directly. They give A0−A1≤Sc−1 and B0−B1≤2eta−1. For Q≥2, the lower bound b_(m−2)−e_(j−1)≥H+(Q−2)(t+3), together with b_(m−1)−e_(j−1)≤eta, gives the sharper displayed bound. For Q=1 the formula forB0 gives eta−(t+1)/2. All edge indices and signs agree. These are finite bounds for a fixed datum and the particular sufficient completion ray; they do not restrict families in which the datum changes.

## Source and scope record

The JSON metadata records whole hashes and exact actually read ranges in twelve source files: Params, DataKap, AMiEqAMinusQ, RowDeg, LinksDefs, FWExist, PartitionExtendByZeroAntitone, RecPJThAllNeBot, AbelianHostFieldConditions, DataParams₂, ExistsBlockProductMemIntegralHarmonic and IsThRule. The recovery manifest contains many other files; recovery and a truncated manifest display are not counted as source readings. No Lean execution or audit of accepted automorphic theorems was performed.

The result resolves the selected-row bookkeeping, provides a sufficient harmonic completion, identifies its pure-kernel vanishing, and proves fixed-window bounds. It does not prove a new global multiplicity/lift estimate, a nonzero value of the completed polynomial with actual prefactors, a new mixed-type CM-object realization, or a universal obstruction to a shorter chain. In particular no forthcoming DP63 assertion is inferred from this proof.

## Complete intended fragment preservation, 04:12:21 UTC

The original9790c2c3 fragment was wholly read at04:10:49, compared against the unchanged memo reread04:11:05. Root changed source-path TeX formatting during capture. I then read the entire currentee35eaa6 fragment, not merely its hash: PASS. Current fragmentSHA256 `ee35eaa629cb8f24a5668d69caabf2db446ca298d4f2ce09b28bc626294b045e`; complete proposition/proofSHA256 `11e3a380bbd68ed2a5db861b1a91cf10fee38918d9814b6e2202e5056fa641a6`; exact main fragment count 1. All four proof parts and sufficient-only/no-geometric-identification limits are preserved. No Lean execution.
