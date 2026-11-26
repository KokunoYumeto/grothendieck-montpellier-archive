# Extended and grand RH research checkpoint

23 November 2026, 00:29 Berlin time. The research notes, editable proofs and arithmetic checks are filed here. The [second reading](SECOND_READING.md) follows the original workshop questions. The [logbook](MATHEMATICS_LOGBOOK.md) records the derivations and their review scope.

The correction of 23 November after rereading the original session applies the verified Dirichlet theorem to both rational shell counts. The [finite-ring proof](workshop/FINITE_RING_KERNELS.pdf) gives a separate arithmetic criterion for the nonabelian cubic. Equations (2) and (5) compute the local kernels and the change of the logarithmic period under removal of primes. The lower bound in (1) is open for this cubic. Page 2 expresses the cubic test using the average log gcd of the first ceiling of y to the three-halves values of the integer polynomial a cubed minus 269 with the product of the primes in (y,2y]. [Editable TeX](workshop/FINITE_RING_KERNELS.tex) · [Finite checks](workshop/check_finite_ring_kernels.py) · [Updated package receipt](PROOF_SCOPE_RECEIPT_20261123.json). The 00:29 manifest and placement receipt identify the earlier editions.

## The mathematical outcome

| Original question | Result at checkpoint |
|---|---|
| Can the Erdős–Straus divisor pairing detect an RH? | Yes, for explicitly averaged counts. Two counts at first-denominator candidates \(m\) and \(25m\) have quarter-power smoothed remainders exactly when ordinary RH holds. Cubic character weights modulo seven detect the corresponding Dirichlet RH. A marked ideal-divisor count detects RH of \(\zeta_{\mathbb Q(\sqrt[3]{269})}/\zeta\). [Editable proof](workshop/RH_FROM_SHELLS.tex) · [Reader](workshop/RH_FROM_SHELLS.pdf) |
| Which part still needs a proof? | Alpöge’s Dirichlet theorem proves the quarter-power error for both rational counts with either character. The required estimate still to prove is the quarter-power error for the Eisenstein ideal count. For the ideal count even a single fixed, nonnegative smooth test supported in \((1,2)\) suffices. A rigorous interval computation excluded the one real fixed point \(2/3\) in the converse. These are statements about fluctuations of counts over integers or ideals. A solution of \(4/p=1/a+1/b+1/c\) for every prime requires a pointwise existence argument. [Ideal proof](workshop/IDEAL_SHELL_CONVERSE.md) · [Certificate](workshop/CUBIC_REAL_VALUE.md) |
| What did the quartic sign add to the cubic test? | The sign of whether 3 is a fourth power and the cubic phase of 269 combine into a sixth-root character, with an explicit weight-one eigenform. The combined prime-plus-composite bound is unconditional. An upper bound on the composites alone on the stated windows would suffice for the mixed RH. [Paper](workshop/sextic_bridge.pdf) · [Editable source](workshop/sextic_bridge.tex) |
| How much reaches actual prime denominators? | Almost every compatible prime has a solution at every eligible sufficiently short shift. Primes 55,441 and 176,401 split completely in the same three fields, yet the first has 32 opposite-divisor pairs at shift three and the second has zero. The second has a solution at shift eleven. [Prime means](erdos_straus/shell_means.pdf) · [Moving shifts](erdos_straus/MOVING_SHIFTS.md) |

The first three-page prime-and-composite proof also has a correction to its hypotheses. The composite criterion for RH of the indicated cubic twists uses just those twists' own RH in the converse. The assertion about the full Dedekind zeta includes additional abelian factors covered by the Dirichlet theorem. The unconditional combined estimate works for cutoffs \(z=(\log y)^{2+o(1)}\) at each fixed modulus. [Corrected proof](rough_composites.pdf) · [Twist audit](algorithms/CUBIC_NOTE_AUDIT.md)

## Prompt state

All three revised pairs were verified in their ordinary waiting folders at 00:29 Berlin time. The user controls sending. **68** contains the rational signed-count questions and the spectral checkpoints. **69** contains the nonabelian cubic and mixed sextic questions. **62** contains the updated multiplicity and trial-vector comparison. **67** remained waiting and matched its prior build. The two corrected TeX sources from the twist audit are in the final 69 ZIP. [Second placement receipt](SECOND_QUEUE_VERIFICATION.json) · [Earlier 67 receipt](QUEUE_VERIFICATION.json)

| Prompt | Files in final ZIP | Newly attached | Checks run from ZIP |
|---|---:|---:|---:|
| 62 | 176 | 30 | 1 |
| 68 | 2,475 | 68 | 10 |
| 69 | 3,770 | 107 | 12 |

Both prompt lints passed for each pair. The current shared builder excludes four earlier Masullo-related working files from 68. Their names and the location of the preserved earlier package are in the placement receipt. The current upstream ALP_MACHINE seed adds its checkpoint-29 update to 68 and 69. The receipt lists every changed prior member.

## Latest source reading and resumption

Connes checkpoints 23–24 distinguish three results: the original trial estimate would imply zero simplicity under the supplied RH input, a separate finite arithmetic construction recovers multiplicities, and the actual lowest eigenvector still requires a uniform parity gap. Machine checkpoint 32 adds 24 lift results across checkpoints 30–32. Its K021 proof matches the source in 69 byte for byte; its three outstanding arithmetic requirements remain. The CP32 manifest and archive were verified directly. Its CP30 and CP31 history was read from that cumulative archive. [Connes intake](connes/CP24_INTAKE.md) · [Machine intake](machine69/CP32_INTAKE.md)

To resume the mathematics, start at section 4 of the signed-count proof and equation (5) of the ideal proof. Equation (5) there is the specific ideal sum whose quarter-power estimate remains to be proved. The rational analogues are consequences of the Dirichlet theorem. The prime-window route has its own one-sided composite bound to prove. At this checkpoint the results are private research notes with mathematical derivations, scoped second readings and reproducible finite checks.
