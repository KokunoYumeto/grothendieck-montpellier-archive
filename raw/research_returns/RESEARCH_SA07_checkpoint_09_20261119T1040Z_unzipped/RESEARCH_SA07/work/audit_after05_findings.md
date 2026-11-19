# Post-checkpoint 05 mathematical addendum

## F.3.18: the exact CM quotient

A one-dimensional Galois-stable subspace of an abelian variety's rational Tate module yields an **actual simple CM quotient** which detects that line. The proof first takes an ordinary rational isogeny-factor projection and clears its denominator. The rank-one Galois projector supplied by Faltings is then analyzed over every local factor of the division endomorphism algebra. Its rank is exactly a sum of positive integer products; equality to one forces the endomorphism algebra to be a field of degree twice the dimension. The commuting complex structure and Rosati positivity prove that this field is CM. No descent of the original ℓ-adic projector to a rational idempotent is presumed.

For a degree-n curve cover, the explicit map `n·id−f* f_*` lands in the connected Prym and acts by n on the relevant kernel line. Its composition with the CM quotient and Abel–Jacobi map gives the actual curve morphism. The quotient need not have dimension one, and a map to a punctured target still requires the exact inverse-fibre containment recorded in the proof. Root checked all of these steps.

## F.3.19: a CM surface really occurs in these Pryms

The Fermat curve `C20: x^20+y^20=z^20` maps by fifth powers to C4 and then to E0 through the earlier degree-32 map. This gives a degree-800 finite étale cover of the punctured elliptic curve, with compactification of genus 171. The separate degree-40 map `(X,Y)=((x/z)^4,(y/z)^10)` lands on the genus-two curve `Y²=1−X⁵`.

Its Jacobian has the actual degree-four endomorphism field Q(ζ5) and is absolutely simple. The proof rules out every possible elliptic isogeny decomposition, including matrix algebras over imaginary quadratic fields, by an explicit commuting-field dimension argument. Norm and pullback give a CM-surface inclusion in the connected Prym, injective on integral Tate modules even at 2 and 5. The inverse fibre of the genus-two point at infinity is already removed, so the corresponding punctured map exists on the same open cover. The construction supplies no procyclic arithmetic-normalizer lift. Root checked the complete proof and independently ran its exact finite certificate.

## F.3.20: all once-punctured elliptic targets

The new recognition proof applies to **every once-punctured elliptic curve over every number field, at every prime**. Its original-source input is the nonzero degree-six arithmetic quotient in Nakamura1996, pp.115–117. The End(J)=Z assumption in that paper's centralizer-finiteness theorem is not a premise of the graded-quotient theorem used here.

Faltings reduces a possible degree-one normalizer line to a split CM eigenline. A spectral polynomial projects the actual closed degree-six Galois image to the χ³ character. Clearing its ℚℓ denominators keeps the projected nonzero vector inside a compact closed ℤℓ-module, so it lifts to an actual Galois element in the degree-six kernel. The complete middle-weight special-derivation space has dimension two. Both exact obstruction matrices have determinant −8. Removing the lower rational inner conjugator through degree six leaves the degree-seven contradiction, including nonprimitive original abelian images. Degree two supplies the actual cyclotomic action and hence cusp inertia by Nakamura1994. Root independently checked the sources, every projection/lift step, both determinants, and the full proof, then independently ran the certificate.

This enlarges the available elliptic targets. It does not supply an elliptic target for every arbitrary finite cover or resolve the genus-two and full profinite A.22 requirements.

## Stable files and scope

F.3.18–20 are integrated by insertion into the live `F_audit.tex`, preserving root's edits. It now has 20 result environments. The new bibliography is `audit_after05_references.bib`; it records the original Nakamura1996 article and the earlier primary lecture-source lead. The four source-access rows are in `audit_after05_source_checks.csv`, including the exact Faltings locator correction. There are 13 canonical events in `audit_after05_CHECK_EVENTS.tsv`; source/output hashes and both agent and root wall times are in the computation records.

The assertion inventory still has **307 assertions from 154 entries**: **195 PROVED, 44 REFUTED, 28 OPEN, 30 READING, 9 DOCUMENTARY-GAP, and 1 NAMED-CONJECTURE-IMPLICATION**. Only the proof dependencies and exact scope of I.B05.01, I.B05.02, and II.MB15.02 were strengthened. No original status changed and no root combined report, ledger, results table, or compilation was edited.
