# Full targeted review of root NN-S001–NN-S011

Reviewer: `/root/gct`, GPT-6 Astra Pro (inherited), effort not exposed by runtime.
Date: 2026-11-21 UTC. Files read in full: `work/root/chapter.tex`, `chapter2.tex`, `chapter3.tex`.
This is an independent agent's full proof reading and targeted verification, not a claim to have rebuilt every proof without reading it.

## Findings

- S001: checked closure, fibre identity, inverse, supported-scalar action, and the Z/2 counterexample. The module/skeleton distinction is correct.
- S002: checked representing equations, nonflatness from 2-torsion, both fibres, and the statement that the equalizer itself commutes with base change. Correct.
- S003: checked universal ring reflection and scalar-extension identity. All rank-one q^j examples have the same Boolean action and different weights. Correct. The finite permutation linearization is correctly distinguished from an additive union map.
- S004: directly checked corpus16's definition, complete ideal classification, prime classification and dimension corollary. The Bourne quotient collapses the entire zero fibre and has no further amplitude identifications. The ideal product contains every z_lambda because e_L z_lambda=z_lambda, and its amplitude is exactly JK. The chain example has n lattice primes and split dimension n+1. Correct; recommend explicitly retaining 'commutative unital' in R's hypotheses.
- S005: checked normal convergence with M>t, cancellation of the apparent poles at 1−k, the zero-times-pole limit at k=m+1, and cancellation of all finite subtractions. The residue correction is −kappa_K t^(m+1)/(m+1), including m=0. The Gaussian example is correct. No RH input is used.
- S006: checked the normalized complex-Dirichlet reflection, leading coefficient relation, uniqueness of the reduced logarithm and coefficient parity. The real coordinate w=−iz is invariant. Clarify that 'normal phase odd' refers to the reduced germ, or to the full phase modulo2pi, since there is no continuous logarithm through the zero. This is a precision issue, not a failure of the coefficient identity.
- S007: constructibility proof is correct. The tail proof should explicitly reindex the infinite nonzero subsequence as i_n and put a_j^n v_(i_n) in those coordinates, zero elsewhere, so consecutive exponents yield the stated Vandermonde. With that harmless clarification the proof is valid over any characteristic-zero field.
- S008: checked both affine coordinate maps, the excluded trivial zero −2, the strip, and the Klein-four quotient. Distinction between reduced support and jet action is correct.
- S009: checked constant-zero/cancelled-zero equality, arbitrary-presentation example, and finite witness sum encoding. Correct.
- S010: checked semiring map for arbitrary composite m as well as primes, universal congruence direction, independence examples, and the two no-homomorphism statements. Correct.
- S011: checked the matching algorithm justification, the two matrices, their product, and all three split determinants. Correct. Efficient instance evaluation is correctly separated from a monotone circuit for the universal polynomial.

No mathematical error was found in the supplied root proof drafts. Exact SGA/EGA citation verification remains root-owned as agreed; this review does not turn provisional locators into verified primary citations.

## NN-S012 full review,2026-11-21T21:16:19Z

Read all178 lines of work/root/chapter4.tex and source OURS_TRANSLATION_SPLIT_ZERO_20261121.md section9,lines275–309. Root chapter SHA256: e40fe51861ee1084fbb6d620c5867aa2bcb9cbcfb41fbd7f1ccb7c620cc02940.

PASS. The characteristic-two gadget was checked on all four Boolean inputs at every primitive gate. Neither lambda nor1+lambda is zero, and multiplication by h occurs only with the Boolean value b equal to tau or1; zero divisors cannot introduce a hidden zero. For2 nonzero, the usual a+b−ab gadget has supported intermediate values1,2,−1,all nonzero where used. OverF2 every nonempty upward-closed support contains the all-ones assignment, forcing one summand at each permitted addition gate to be identically absent; deletion leaves only conjunctions and constants. The finite-ring lookup simulation is constant-factor precisely because the ring is fixed. The base change toF4 keeps the split finite Boolean scheme and changes the available constants.

The source correction is fairly scoped: section9 leaves the phrase no supported zeros ambiguous, and the root separates its valid output-only interpretation from the false every-gate interpretation overF2. The distinction between an exponential ratio and a polynomial upper endpoint is logically correct and makes no unproved assertion about actual CLIQUE circuit sizes. No mathematical correction found. Exact primary EGA verification remains root-owned.

## NN-S013 full review,2026-11-21T21:25:10Z

Read the entire work/root/chapter5.tex. SHA256: 78bbd3afed4f2a05576836d6ec4a69c51d52dd5dab15bd58f83e17697e55f028. Independently opened the Goldreich–Izsak primary PDF and checked Theorems1.1,1.2,3.1; section2's explicit uniform/nonuniform conventions; section3's slice/OWF argument; and section4.2's actual coordinate and two-coordinate AND distinguishers. Primary URL: https://theoryofcomputing.org/articles/v008a010/v008a010.pdf .

PASS. The conjunction-map inverter computes the least possible preimage from all requested-one output supports and correctly rejects a requested-zero support contained in that union. The monotone OWF conversions preserve the Boolean map and adversary convention. For the PRG claim, the shared-input coupling bounds disagreement of the one/two-bit distinguisher by the union of the corresponding final supported-zero events; nonuniform security permits the selected test family. The two-event union bound loses only a factor2,so the final gate hasOmega(2^n/n²) supported-zero inputs. The separation between E's subexponential preimage algorithms and polynomial inversion is retained. One wording clarification sent: specify circuits overG(R) in item3,rather than ordinary ring circuits,so the selected support lift is explicit. No mathematical error found. Primary EGA/SGA locators remain root-owned.

## NN-S014 full review,2026-11-21T21:44:24Z

Read all169 lines of work/root/chapter6.tex, SHA256: 68ecd4df826472773e816c56992d38c3fc09931252afc0018b4e42185b9bf52f. PASS. The cutoffc0 logn/n² is small enough for the uniform KKL constant; Talagrand yields the logarithmic covariance and the marginal-product correction is at mostdelta. Parseval bounds the influence inner product by1. The n^8 independent training samples,Hoeffding union bound,selection of maximum empirical bias,and complementing its acceptance convention give the displayed oriented advantage. Independence of the challenge prevents training reuse. Coupling changes each selected test by at most2b_n; averaging bad training events loses at most2eta_n,so the uniform security conclusion follows. Two wording clarifications sent: use the absolute value of the first Fourier coefficient unless choosing the2x−1 convention explicitly,and state the displayed failure probability in the sampling guarantee. No mathematical error found. This is a full proof read,not a claim to reprove KKL or Talagrand independently.

## 2026-11-21 23:24:17 UTC — full S017/S018 read
Read entire work/root/chapter9.tex and chapter10.tex. Main S018 proof passes: null reduced diagonal for suspension wedge, primitive Bott generator pullback, unstable Adams action, torsion-free Newton recovery, exact Stirling gamma polynomial, gcd filtration, odd-v Z/2 quotient, and parsimonious padding. Suggested replacing ambiguous Tate weight v by gamma degree v/Tate twist v, and scoping Chow torsion-freeness to the bases actually covered by the cited comparison or adding a direct localization proof over Z. No new primary PPR/SGA page audit asserted.

## 2026-11-22 00:01:02 UTC: complete mass-twelve exclusion proof
Read every line of work/root/w12_exclusions.tex (131 lines). Targeted whole-proof PASS. Checked the mass-twelve character classification, primitive irreducibility and nonunit constant of H=W/D, determinant-at-zero D-adic argument, both84/88 orientations,84/84, and both80/96 rows with minimal cells. The final reversed80/96 orientation correctly uses the independent NN-G030 mod-four relation. No positivity of polynomial quotients or support-degree cutoff was used. This is a mathematical full read, not a fresh source-locator audit.

## 2026-11-22 00:11:26 UTC: two lowest remaining mass-twelve rows
Read the complete root proof w12_lowest_exclusion.tex. PASS for all content, determinant, integer-evaluation, H-factor and mod-four arguments, in both orientations. No quotient effectivity or support bound assumed.

## 2026-11-22 00:20:19 UTC: reverse mass-twelve row
Read all113lines of root w12_reverse_exclusion.tex. PASS for the nonzero-W(0) C(0) bound, zero-W(0) exact R=psi consequence, complete monic J divisor list, and central bottom coefficients120 and140 against144. This is an independent whole-proof reading; source-locator audit is not claimed anew.
