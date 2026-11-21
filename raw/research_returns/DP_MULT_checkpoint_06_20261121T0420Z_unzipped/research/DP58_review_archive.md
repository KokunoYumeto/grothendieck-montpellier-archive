# DP58: independent complete explicit-witness and linear-level proof review

**Verdict: PASS.** The complete saved memo, §§1–8, was read and independently challenged. No mathematical correction is requested. The main paper and author's memo were not edited.

## Provenance

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; effort not exposed by runtime. Date:2026-11-21 UTC. Complete text reading observed at03:43:07; targeted DP51 initial-form and harmonic-extraction reread completed at03:43:52. Whole SHA256: `b28b7ae31c54a29aab6e0690b3f57ef3cc0371fbf7f797717809c24c0346cc88`. The full snapshot and dependency hashes are preserved in `late_proof_snapshots/DP58_complete_archive_checked.md` and `DP58_archive_review_metadata.json`. The checker had independently derived the exact factorial formula before reading the completed memo; that informal calculation is not counted as a separate whole-proof event.

## Critical exponential lemma

The hypothesis concerns the entire reduction of the normalized logarithm, not merely its first ordinary-degree coefficient. With z=mu Q and v(mu)=s, the scalar in exponential order m after dividing the exponential by mu has valuation s(s_p(m)−1). It is a unit exactly for m=p^r. Every other order vanishes in residue. The reduction of Q is the single monomial u Z^alpha, so its p^r-th power is exactly u^(p^r) Z^(p^r alpha). Because alpha is nonzero, these degrees are distinct. All displayed leading coefficients are units; there is no cancellation between different surviving orders.

The proof is formal coefficientwise: zero constant term makes the contribution to any fixed ordinary degree a finite sum. It does not exchange a nonconvergent infinite sum with reduction. The discrete value group gives the stated positive gap, though the reduction proof already suffices. An Artin–Hasse cancellation would require additional logarithmic monomials at the same lowest valuation, excluded by the full initial-form hypothesis.

## Actual ordinary path and exact factorials

DP46's complete initial-form calculation after the actual inverse logarithms was directly reread during the preceding DP56 check. Its critical profile gives mu=varpi^(N+1)/p^S with v(mu)=s and exactly one initial monomial of degree N+1. Multiplication by every unit lambda changes only its nonzero residue scalar. Invariant integral frame corrections stay strictly above this valuation. The h>=3 and primitive-projection hypotheses are retained, including first surviving dual index j and k=h−j>=1.

At degree n=(N+1)p^r, the scaled exponential coefficient therefore has valuation exactly s. Removing the scale gives v(A_n)=s−wn=−(p^(k+r)−1)/(p−1). Since n=p^(k+r)+p^r has two nonzero base-p digits in distinct positions, v(n!)=s(n−2). Their sum is exactly (p^r−1)/(p−1)=cn−s. This calculation is valid at r=0 and for every unit lambda, and proves each witness nonzero. It is not an equality statement for arbitrary integral prefactors.

## Harmonic diagonal correction

The actual two-variable initial form was directly read in DP51 §2, HA7 and its complete following proof. It is an independent-variable computation through the actual inverse coordinates; it is not inferred from substituting x=y. Applying the new lemma gives all valuation-s exponential monomials on the ray (p^r,N p^r).

Because N>1, that support has no nonconstant diagonal monomial. Every scaled diagonal coefficient consequently has valuation strictly greater than s. Thus mu^(-1)(D(−varpi²XY)−1) is integral with zero reduction. Multiplication by the integral exponential cannot reintroduce a valuation-s contribution from that factor, so the complete harmonic generating series retains exactly the same lowest-valuation support.

The finite coefficient identity H_(a,b)=a!b!*[x^a y^b](F D(−xy)) was checked directly, including every binomial coefficient and both i! factors. It keeps all alternating summands. At a=p^r and b=p^(k+r), both factorial digit sums are one, giving the same exact valuation (p^r−1)/(p−1). There is no omitted cancellation from the second column. The full source-shaped HaO interpretation stays limited to the first permitted negative row; other eigenaxes are not asserted to permit reordering the prescribed datum.

## Linear square tensor levels

The fixed integral interpolation threshold from DP56 is An+B0. With m0=ceil(sqrt(An+B0)), choosing either m0 or m0+1 makes M prime to11. Then M>=sqrt(An+B0) and M<sqrt(An+B0)+2, so

An+B0 <= M² < An+B0+4sqrt(An+B0)+4.

Hence M=O(sqrt n) and kappa=M²=An+O(sqrt n). Because the exact local witnesses work for every unit parameter, the interpolated exponent lambda=−kappa needs no congruence to a previously chosen unit. The source factor M^(−n) is a unit. The p11 ordinary degrees12*11^r and122*11^r and harmonic row degrees(11^r,121*11^r) match the two primitive restricted-p lengths exactly.

A single complete jet through a chosen maximum degree realizes any finite prefix, and two copies of that same section realize the product harmonic evaluations. Every earlier selected coefficient still has the same unit exponent and exact valuation. The density argument can preserve finitely many selected nonzero values at the already chosen power, so number-field approximation does not change the linear tensor bound.

## Exact scope

The new theorem strengthens the existing local sharpness into explicit degrees and exact valuations, and the finite global realization into linear tensor powers. It does not construct one fixed section realizing infinitely many degrees, prove the same exact values for all prefactors, or identify the selected sections with the prescribed translated theta family. It gives no archimedean section norm, coefficient height, approximation cost, unrelated row-degree compatibility or full global endpoint/cost comparison. The unit-parameter regime is explicit and does not contradict the nonunit behavior of DP50. No numerical experiment or Lean formalization is claimed.

## Complete integrated proof and explicit-hypothesis preservation

The complete initial intended theorem, all proof paragraphs and scope were actually read at03:47:02. Original fragment SHA256 `784e02a61c6b0e589c8c2748fd0020c2094ab5af8e8542024af523fccbded95e`. All mathematical arguments were preserved. The reviewer requested explicit u-unit/v-primitive conditions already present in the original memo and established terminology. At03:50:29 the exact one-line addition was read and verified to be the only change. Final fragment SHA256 `7f40bf5de027209c75a3c4d1f1c8bafd9fe1380ee712667d98bd2f797635e616`; complete theorem/proof SHA256 `810ec43038ed117acd59c4b3d1ba96c3f1ebc5b41ee6b0da9a4fe90fb64d699b`; exact main count 1. **PASS.** This is a whole original reading plus exact delta verification, not a fictitious repeated whole reading.
