# DP46: independent complete unit-arrow and invariant-frame review

Reviewer: `/root/archive_binomial`, **GPT-6 Astra Pro**, inherited model; runtime reasoning effort **not exposed**. Date: **2026-11-21 UTC**. Event **ABA-CE47**. Complete original reading began **02:42:37 UTC**; the entire precise-scale version was reread at **02:44:50 UTC**, and its hash was checked unchanged at closing **02:44:58 UTC**. No main-paper edits.

## Outcome and exact scope

**PASS.** The theorem extends the exact primitive mixed-line radius to every stated arbitrary-unit singleton/complement cyclic display and every normalized invariant integral frame. The proof directly handles the actual unit-arrow display; no finite-unramified twist-trivialization theorem is smuggled into the argument.

- Entire memo SHA-256: `df8ef42e644d250deeba25bd4db0a90cd9054b575ad0f456b0c64ac7c383f14a`.
- Complete statement and proof, §§1–6, SHA-256: `278cdb907bd509129ff6befe5867fa2a627545dc0bd9c066fe4ec628a7341cb3`.
- Frozen copy: `late_proof_snapshots/DP46_complete_checked.md`.
- Metadata: `late_proof_snapshots/DP46_DP48_check_metadata.json`.

Root had already found the missing plus sign in UI10 and malformed `quad` in UI12; they were corrected before my initial full reading. My one additional precision suggestion was to choose the scales explicitly as powers of a common `π` with `π^e=p`. The final version does so, making the ordinary-arrow scale ratios equal to one and the later identity for `μ` literal. This was a clarification of an available choice, not a counterexample to the theorem.

## 1. Variable ghost matrices and signs

I independently checked the ordered product inverse of `z_n↦B_nz_(n+1)−z_n`; no matrix commutation is needed. The selected-component logarithm telescopes on the relation module, and full cycles provide the required positive powers of `p` against the uniformly bounded denominators on nilpotent truncations. Reciprocal dual arrows give `B_n^t B'_n=pI` with the stated conventions.

In the frame comparison, applying `V^(−1)` to the first defect produces the prefix `P_(n,r+1)` in exactly the displayed order. Zink's negative `hex` and the inverse scalar splitting give the negative double pairing sum; the second frame factor gives `+L_G C_H`. Thus UI10 has the correct order, signs and correction term. Counting the unique cyclic paths gives the denominator exponents `n+l+1`, `a`, and `dl+h−i` in UI11–UI13. Every ghost of a Witt unit is a unit, so no path valuation is changed by the arbitrary coefficients.

## 2. Exact mixed-line coefficient

The coefficient `a_d^(−1)/p` at `SY_d^p` has a unique source. The ordinary dual first arrows are `a_(i−1)^(−1)Y_(i−1)^p/p`. Recursively inverting them gives at the final coordinate the product with exponents `p^(d−r−1)`; raising to the final `p`th power and multiplying by `a_d^(−1)` gives exactly

`θ_j=∏_(r=j)^d a_r^(−p^(d−r))`.

For odd `p`, the sign is `(-1)^(k_*−1)`. I checked both the final-coordinate case `j=d` and the full chain. The initial term has degree `p^(k_*)+1` and hence nonzero formal derivative modulo `p`.

The weights strictly exceed the original contraction weights throughout the stated interval. Ordinary-arrow scale defects are exactly one, while the exceptional defect is greater than one. Multiple selected-arrow paths acquire positive scaled valuation. The first-family gap and the product-family excess have the same strict inequalities as DP42, because every additional coefficient is a unit. The exact common-root scale choice now proves the equality `μ=γ^(p^(k_*)+1)/p^(S_(k_*))`, not merely equality of valuations.

Earlier nonunit inputs have valuation at least one over the unramified lattice and vanish in the scaled reduction; later inputs vanish by their strictly smaller output weights. Only the first unit coordinate survives. The resulting positive residue error descends to divisibility by `p` in the original coefficient field. This proves the stated exact congruence, not only its valuation.

## 3. Radius, prefactors and intrinsic index

The DP41 fraction-field multiplier argument applies to the full restricted initial form, including any nonzero integral prefactor restriction. At the endpoint the minimum equals `s`, so the exponential and its inverse are integral with constant one. Gauss multiplicativity supplies the finite norm equality, and monotonicity gives the full range of weights. The factorial inequality and exact coefficient liminf follow as in DP42.

The restricted `p`-operation has a single semilinear chain: ordinary arrows give a unit multiple of the next invariant direction and the last power vanishes. The first unit coordinate therefore has nilpotency length `h−j`. The ordinary coefficient calculation agrees with this assertion; torus characters exclude extra directions. Consequently the index and the transport conclusion are intrinsic, not artifacts of an arbitrary choice of coordinate labels.

## 4. Invariant frames for arbitrary integral exponential scalars

For an invariant nonconstant monomial, the torus congruence makes its original weight an element of `s Z`. Because all original weights are positive, this weight is at least `s`, even if the congruence integer itself is negative. The new weight increments are all strictly positive; their finite minimum gives a uniform positive margin for every nonconstant monomial. Hence the contracted `J−1` has coefficient infimum strictly greater than `s`.

The logarithm estimate preserves that strict margin. Therefore `exp(±λ log J)` and its inverse are integral units for every integral `λ`, with constant one. They preserve the finite Gauss norm and the unboundedness threshold; their logarithm lies strictly above the mixed-line initial term, so the congruence is preserved too. The proof correctly avoids the false general claim that an uncontracted unit has integral binomial powers for every element of an arbitrary unramified coefficient ring. The separate `λ∈Z_p` statement for arbitrary integral frames is consistent with ordinary binomial integrality.

## 5. Transport and limitations

The direction `ψ=(φ^(−1))^D` is correct. Its tangent map and that of `φ` are integral invertible maps, preserve primitive projections and the restricted-power nilpotency length, and preserve nonzero restrictions. Naturality transports the primitive identity class. Unramified coefficient extension preserves the valuations. The theorem explicitly assumes a supplied integral CM isomorphism for this transport assertion, while the direct proof needs none.

Primary source conventions are the already directly checked Zink statements listed in §7. This event checks the whole new proof and their use, not complete external theorem proofs or a new retrieval of the unused Drinfeld/Hazewinkel route. Odd primes, `h≥3`, the specified actual cyclic pair, unramified primitive lattices, invariant integral frames and nonzero prefactor restrictions remain in force. No geometric theta normalization, harmonic selection, global cost or lift-count conclusion is claimed.
