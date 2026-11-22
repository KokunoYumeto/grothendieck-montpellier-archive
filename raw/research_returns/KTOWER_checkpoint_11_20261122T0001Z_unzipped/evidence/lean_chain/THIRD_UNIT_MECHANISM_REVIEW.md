# Third-unit character and proposed mechanisms

**PASS with the exact limited conclusion stated.** Read the complete 211-line `main_gate/third_unit_character_obstruction.tex`, the entire small conductor-sum certificate, Knospe–Washington formula (1), Proposition 2.1 and full proof, Theorem 2.4 and full proof, and Corollary 2.5. Re-read Benmerieme–Movahhedi's full derivation surrounding equation (2.4), pp.4–5. The source hashes and fresh replay are in `third_unit_59_replay/manifest.json`.

## Branch congruence

For a nontrivial even character of order dividing p−1, a value different from 1 remains different modulo p. The chosen regularizing factor is therefore a unit for every s in Z_p. The finite sums in Corollary 2.5 have half-integral coefficients with denominator 2, which is a p-adic unit. Their remaining factors are integral and have the same reduction for every s. The convergent limits preserve both integrality and their congruence. Dividing by the regularizing unit proves TU.1. The theorem's analytic domain contains Z_p for odd p, and its conductor hypotheses allow a p-factor. This is a full derivation of the new branch lemma from the cited expansion, not a claim to re-prove Washington's imported construction of the p-adic L-function.

## Character and unit projections

Disjointness gives `Gal(L/Q)=C2×F_p^×`; the kernel of `χ_D ω^−1` is exactly global complex conjugation. Thus it is faithful on the cyclic degree p−1 real field. At s=0 the interpolated character is `χ_D ω^−2`, primitive at p when p>3, so the p Euler factor is exactly 1. The Bernoulli sign and inverse power in TU.4–TU.6 agree with formula (1). The already checked finite-character transport gives the second congruence.

For any multiquadratic M, its intersection with the cyclic field K has degree at most 2. The subgroup fixing M therefore has order greater than 1 and the faithful character is nontrivial on it. The character idempotent is integral because the full compositum degree is prime to p. A unit from M is fixed by this subgroup, so its theta projection is zero. Galois conjugation and Z_p-linear generation preserve that conclusion. This excludes only the proposed unit-projection mechanism, not all possible arithmetic information from those fields.

## Full p-rationality is stronger than the desired component

For irregular p, an ordinary even Bernoulli index gives a nonunit `L_p(1,ω^k)` by interpolation and the branch congruence. This character occurs already in `Q(μ_p)^+`. Every other nontrivial character of K also has integral L-value, so cannot cancel its positive valuation. In Benmerieme–Movahhedi equation (2.4), `K(μ_p)=L` contains μ_p and cannot contain μ_(p²), since its degree is 2(p−1). Thus **m=1**, including all possible D under the theorem, and the required product valuation is zero. The obstruction follows without confusing a single character component with full p-rationality.

## Actual numerical replay

The independent frozen-copy run exited 0 and produced a byte-identical report, SHA256 `83bd8f20c343193df35a65c8c5cfb6d72554ef6e06537c916ec9e392d5faa7c5`. It computes the exact rational `B44/44`, verifies valuation one at 59, and independently evaluates the two conductor sums modulo 59² before division. Their residues are 13 and 5. Both agree with the previously independently replayed prefix scan at D=−244 and D=−228. The character formula is correct for squarefree parts 61 and 57, and the `a^59 mod 59²` Teichmüller lift retains the precision required by division. No floating point, large-prime assumption, or prefix formula enters this small direct computation.

This proves that full p-rationality of the real compositum is not necessary for the third unit. It proves neither an all-prime third-unit theorem nor a new Selmer upper bound.
