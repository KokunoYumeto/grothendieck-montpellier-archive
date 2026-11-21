# DP56: independent complete quantitative jet-level proof review

**Verdict: PASS.** The complete memo, §§1–9, was actually read and independently challenged. No mathematical correction is requested. Main paper and author's memo were not edited.

## Check provenance

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; runtime effort not exposed. Date:2026-11-21 UTC. Complete text read observed at03:37:20; targeted checks continued through03:39. Whole memo SHA256: `b7622257fd02ee676ba48fc2c4532229772b55731ce5bd405dca48e0e49a9372`. Full snapshot and exact dependency hashes are in `late_proof_snapshots/DP56_complete_archive_checked.md` and `DP56_archive_review_metadata.json`. This is a mathematical proof review, not execution or machine formalization.

## Integral interpolation with fixed linear threshold

A relatively ample line over the affine DVR has a power defining an immersion into a fixed projective space; properness makes it closed. The author uses exactly Stacks Lemma29.40.4(2),(5), Tag01VT, whose statement was independently opened and read. Since the projective coordinate sections generate the line at the closed point of the section, one has unit value. Its normalized pullback is one on the entire base. Subtracting the values at the section times that coordinate is an invertible triangular change over R.

The ratios generate the augmentation ideal on the affine chart, hence its conormal module. Smoothness makes that module free of rank g. A surjection from a finite free module onto it admits a g-column minor invertible modulo the maximal ideal, hence invertible over R. Thus the selected ratios have a unit linear change of formal parameters. The inverse formal-coordinate construction uses only unit inverses. Equivalently, the regular section has associated graded symmetric conormal algebra, so these chosen parameters identify the completed neighbourhood with R[[t]]. There is no hidden inversion of p.

Homogenizing each monomial of a jet of degree at most n with the nonvanishing coordinate produces a global section of L^(rn). The exponent n−|alpha| is always nonnegative. Arbitrary higher multiples work identically. To obtain every power kappa>=rn+b, the source's global-generation theorem supplies a section of L^(kappa−rn) having unit value at the closed point. It remains a frame on the whole section and its nilpotent thickening. Multiplication by it reduces every target to the same homogenization. This is valid also for n=0. The constants r,b depend only on the fixed scheme, line and section; neither the target jet nor n changes them.

Stacks Proposition28.27.13(7), Tag01Q3, was independently opened and read and gives precisely global generation of all sufficiently large powers for the finite-type quasi-coherent sheaf O_X. The paper cites these known implications and proves only the required integral linear-threshold form.

## Coefficientwise tensor parameter

The estimate is proved for coefficients in the indeterminate T, not inferred from values at integer T. After a finite ramified scaling of rational weight w, every coefficient of the zero-constant logarithm has valuation at least s=1/(p−1). The mth exponential term therefore has coefficient valuation at least ms−v_p(m!)=s*s_p(m)>=0. For a fixed Z-degree only finitely many m contribute. This gives actual integrality of each polynomial Z-coefficient in T, with no infinite-degree ambiguity.

Applying an integral homogeneous polynomial differential operator of degree n multiplies the coefficient at multiindex alpha by P_alpha*alpha!. Legendre's identity gives the stated lower bound cn−sigma(P) coefficient by coefficient in T. The maximum of the finite digit sums is correctly used; nonzero P avoids an empty maximum. The D-variable logarithmic error is uniform with fixed D. Zero coefficients, degree zero, and possible negative c in the general lemma cause no problem.

## Actual primitive logarithm profiles

The exact profile in DP46 §4 was directly reread, including common scaling, integral inverse maps, unique group-coordinate minimum and the restricted initial form. At the ordinary critical weight the full restricted logarithm has infimum s, not merely an integral exponential. Arbitrary unit arrows and invariant frame corrections do not reduce this infimum.

The full-polydisc proof in DP51 §6 was directly reread. At the j=1 profile the scalar and first dual weights equal w*, while each later dual weight is smaller. Replacing every independent additive weight by w* contributes nonnegative extra factors before the integral contracted inverse map. Substitution into the full scaled primitive logarithm therefore preserves the lower bound s before exponentiation. Two independent copies have the same bound for their sum. This justifies the exact logarithmic hypothesis used for the harmonic tensor-parameter polynomial; it is not an unjustified converse from exponential integrality.

## Congruence, integer rounding and square-level estimate

Let L=cn−sigma(P) and V=v(F_P(1)). The coefficientwise estimate implies V>=L. Hence B=floor(V−L)+1 is a positive integer, and B+L>V even when V−L is an integer. Every scalar T congruent to one modulo p^B preserves the selected nonzero valuation. This uses the nonarchimedean strict inequality correctly.

The integer M=1+p^B*ceil((m0−1)/p^B), with m0=ceil(sqrt(rn+b)) for n>=1, satisfies M>=m0 and M<m0+p^B. Its square meets the interpolation threshold and stays congruent to one. M is a p-adic unit, so the source normalization M^(-n) changes no valuation.

Along an actual sharp sequence, V/n tends to c and sigma(P)=O(log n), so B/n tends to zero. The upper bound sqrt(rn+b)+1+p^B then gives log M=o(n). This remains true if V−cn is occasionally negative: V>=L makes the displayed upper bound for B nonnegative. Squaring doubles its logarithm. The proof concerns one fixed prime and does not silently impose a growing collection of simultaneous congruences.

## Number-field descent and remaining limits

The finite interpolation over the complete ring can involve arbitrary p-adic coefficients. Algebraic projective coordinates do not make those target coefficients algebraic. The memo correctly treats exact complete-ring interpolation and approximate number-field descent separately. For each already selected power, DP54 flat base change and density approximate the global section while preserving the finite nonzero selected value, including product-copy evaluations. This changes neither M nor its tensor exponent.

The theorem proves a fixed linear interpolation threshold and subexponential tensor levels along sharp sequences. It gives no numerical value of r,b, no coefficient-height or archimedean-norm bound, no approximation-height estimate, and no realization inside the required translated theta family. Logarithmic size of the tensor exponent is not identified with the full global cost. No shorter-chain or no-shortening conclusion follows from this result alone.

## Complete integrated proof and caught precision issue

At03:40:23 UTC the complete intended integrated theorem, all proof paragraphs and final scope were actually read. All quantitative arguments and original proof content were preserved. One generality issue was identified: unlike the memo, the integrated statement did not assume pure relative dimension, so `g=dim(X/R)` could be ambiguous for disconnected smooth components of different dimensions. The reviewer requested the precise rank along the given section. Root replaced that one line by `g=rank_R(e^*Omega^1_{X/R})` in both fragment and main.

At03:41:17 UTC the exact one-line change was read and independently verified to be the only byte change from original fragment SHA256 `1c6ca3a8ca87fd69a660d8d277e0f0870f3f622d93ae90bf8fc6057b99773fbd` to final SHA256 `e05df0139cc0a0b1dc8447009e91e8f9dba1b5ef79cca1c235f9577822b0edb2`. The unchanged remainder had already been read in full. **PASS for the corrected complete proof.** This is a full original reading plus a separately verified delta, not a fictitious second full rereading. Complete final theorem/proof SHA256: `5e8e73482856f4b462ea559d7e45d6456cb707400d22a670a0af1066eb64b088`. Exact final fragment count in main: 1. All fixed-model, all-power, coefficientwise, strict-rounding and scope arguments are retained.
