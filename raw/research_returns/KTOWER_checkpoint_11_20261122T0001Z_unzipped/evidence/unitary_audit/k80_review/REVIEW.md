# Independent review of the completed degree eighty

Reviewer: `unitary_audit`, GPT-6 Astra Pro. Reasoning effort is not exposed. No Lean kernel execution was performed.

## Whole-proof conclusion

**PASS** for the complete `further_vanishing_e40.tex` at SHA256
`c83012f830cd23921875edfc9a23a4200345b4f679cea1d35898d8076a7709d0`.
The byte-identical text read is preserved as `further_vanishing_e40_reviewed.tex`.
The proof and its component/Soulé corollary were read in full, including every displayed residue, hypothesis and scope qualification.

The conclusion is `K_80(Z)=0` under the stipulated archive-theorem convention and the carried arithmetic inputs of KT-K64-VANISH. Together with the previously checked range, this gives `K_(4k)(Z)=0` for `1<=k<=20`. The periodic safe component interval is `[-16,20]`; the negative endpoint is unchanged. The Soulé conclusion concerns the full-domain character kappa_41, not a deeper filtration.

## Logical checks

The carried small-prime results remove two and all odd primes below `2^31`. A remaining prime is therefore greater than 81, distinct from the tested primes 7 and 13, and satisfies the required nondivisibility of 80 by its predecessor. The actual initial-field GD and closed OneChar criterion therefore apply at parameter 40.

Both initial comparison factors use the full spaces. Their exact nonzero products at 7 and 13 force every remaining prime into the support of the two displayed residual integers. The support calculation does not factor those residual integers and needs no primality or squarefreeness assertion about them.

For each residual modulus, the completed alternate-field report gives all 2667 identifying rows and all thirteen actual frames per row, with the entire harmonic kernel and saved integer model checked. The two evaluation determinants are units over the quadratic residue algebra. The independent denominator and Eisenstein-scalar gcds are one. The carried residual-ring lemma consequently gives the full two-class unitary unit condition at every coefficient place above every prime dividing the modulus.

The separate full dimension-157 classical determinant is a unit at each of those primes. These are precisely the two full-space hypotheses in K17-MINUS7-GENERAL-SOURCE. That theorem yields strict rational negative Selmer vanishing, and the carried K-group comparison contradicts the putative nonzero primary part. Finiteness completes the argument.

The component corollary uses the previously proved interval through 19, the new endpoint 20, exact class-component periodicity, and the already checked exceptional-character argument. It does not infer periodic equality of K-group orders.

For this review the exact carried statements were reread in `input/RETURN_K17_checkpoint_08_20261121T0616Z/K17.tex`: K17-MINUS7-GENERAL-SOURCE (statement beginning 6277 and the source-datum proof), K17-U3-RESIDUAL-RING (statement beginning 6803), and K17-COMPONENT-CONTROL / K17-ODD-COMPANION-EXCLUSION (beginning 10975 and 11084). Their previously audited deeper inputs remain carried; this event is not a claim to have reconstructed all imported automorphic or arithmetic proofs.

## Fresh arithmetic and report reconciliation

The whole 178-line `check_k80.py` was read, then executed freshly using only the Python standard library. It adapts the separately checked degree-76 reconciliation algorithm to the present fixed data. It independently performs:

- Exact Horner evaluation of all four saved initial characteristic polynomials, with the correct comparison points and degrees.
- Nonvanishing and exact gcd reconstruction, including trial-division proofs of every listed small prime and of the Krylov certificate prime 1000003.
- Input/report hash reconciliation with the frozen completion snapshot, and unchanged start/end hashes in the completed model reports.
- The complete native coverage flags, dimensions, row/frame counts, exact Schur quotient congruences, determinant-norm units, and denominator/scalar gcds for both moduli.
- Fresh multiplication and elimination for both 157 by 157 classical matrices over the composite residue rings, allowing only verified unit pivots. Both residues agree with the manuscript and completed reports.

The fresh run returned **PASS**, with report SHA256
`93cca2e9735e3da75b0af6d089a2881c187dbd01901bab04942c9aab327b0071`.

No new large unitary execution or independent Python replay of its 2667 rows is claimed. The numerical checks here are exact reconciliation of the completed reports plus fresh initial polynomial/support and classical-matrix arithmetic. The mathematical conclusion additionally uses the whole-reviewed proof above.

## Formatting lineage

The final formatting successor has SHA256
`b75ab50604a3b437c047a981b9b59be303af041fa0b9c5c1dcc57d0ec46fb9a3`.
A fresh exact byte comparison against the preserved reviewed proof proves that its only change is the single table spacing `tabcolsep` from `3pt` to `0.5pt`. All mathematical text is unchanged. This comparison is recorded in `layout_lineage.json`; the whole mathematical review therefore also covers this final successor.

No higher degree than 80 is asserted by this review.
