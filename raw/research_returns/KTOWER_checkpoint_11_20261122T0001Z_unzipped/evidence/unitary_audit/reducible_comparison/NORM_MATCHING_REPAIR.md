# Norm matching: identified gap and explicit repair

## Historical scope correction

The checkpoint07 version of `cubic_shuffle_comparison.tex`, SHA256
`0268d7127561c8d93ea1da4dc99389b67683aedcf64d7696e86084ce91a32e3c`,
inferred realization of the specified binomial defining system by a Sharifi norm representative from the terminology in Lam–Liu–Sharifi–Wake–Wang §4.3. The associated scope paragraph had SHA256
`118cdf7a916d8b851b48a89d32ac3b0164a2bcf770c478f8b25627f43b1c16a3`.
That inference was incomplete. Earlier recorded reviews remain historical records; the present entry supersedes their properness-scope conclusion.

Both originals are preserved byte-for-byte in `review_snapshots/`. No checkpoint archive was edited. The cubic shuffle identities, Bockstein polynomial identity, and the K-group arithmetic certificates do not depend on this incomplete inference.

The issue was identified by the independent sibling `/root/lean_chain` during the new exact-norm audit. A concrete scope counterexample is available over any local field containing `mu_p`: choose characters `chi,gamma` with nonzero cup product, using local Tate duality, and take augmentation `v=0`. The binomial cocycle `f_2=gamma*x` is a valid abstract proper system modulo `x^2`, but its Bockstein is `chi cup gamma`, nonzero over the absolute group. Every particular Sharifi norm-y system with the maximal extension equal to the separable closure has zero transgression there. Thus binomial properness alone cannot imply a matched norm-y realization.

## Repair for the actual ordinary system

The new lemma **KT-CUBIC-MATCHED-NORM-SYSTEM**, in `cubic_excision_norm.tex`, adds and proves the needed implication under zero absolute inflation. Our actual ordinary system satisfies this extra hypothesis: its relative obstruction is locally zero everywhere, so after restriction to `K=E(mu_p)` the Brauer local-global injection kills its absolute inflation. Equivalently, the new excision argument places its p-only class in `Pic/p`, which also has zero image over the field.

The lemma first lifts the specified truncated cocycle to degree three on the absolute group. At each later augmentation stage the obstruction restricts to zero on `ker chi`, because the module sequence splits there. The cyclic relative Brauer exact sequence expresses it as `chi cup gamma`. Subtracting `gamma*x^(n-1)` cancels it and preserves the first two coefficients for `n>=3`. This gives a full regular-module cocycle while retaining the specified truncated class.

Shapiro, with the coefficient-of-identity evaluation and Sharifi's exact inversion pairing, then provides the norm representative. A constant regular-module conjugation gives the normalization used in Sharifi Lemma4.1. Dividing the representative by a base-field scalar makes its norm equal to the chosen `B_0`; the corresponding regular-module correction is supported on `x^(p-1)` and leaves the truncation unchanged. The annihilator `(I^2)^perp` verifies the required power condition on `D^(1)y`.

The full cocycle is constructed on the absolute group and may acquire ramification in coefficients of degree at least two. Only the original truncation descends to the p-only quotient. Accordingly the finite-ramification norm obstruction is not forced to vanish.

For a matched representative, Sharifi Proposition4.2 and the exact equation(5.2) in the proof of Theorem5.4 give an exact norm-ideal class. The lower-product quotient is needed only when that matching is forgotten. Formula CE.11 records the exact equality for the ordinary obstruction, with the full rational class component retained by excision.

## Present limits

No norm representative or ideal class has been arithmetically evaluated. No nonzero Massey value, strict-Selmer injection, actual-source-to-independent-jet theorem, or all-weight vanishing result is claimed. The new result repairs a source-scope gap and sharpens the comparison target; it is not a new arithmetic vanishing certificate.

The standard-library program `matched_norm_check.py` checks the stated polynomial correction, norm element, and inversion-pairing annihilator for five small primes, including 494 coefficient-correction cases. These are algebraic checks only; the general proof is in the manuscript and imports the exact absolute cyclic norm-residue theorem.

Model: GPT-6 Astra Pro. Reasoning-effort setting: not exposed. No Lean kernel execution.
