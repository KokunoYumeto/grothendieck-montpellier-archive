# K17-GL2-CONDUCTOR: independent whole-proof audit

Date: 2026-11-21. Reviewer: /root/vandiver_k, GPT-6 Astra Pro.
Effort: not exposed. Run: K17.
Verdict: PASS for the complete conductor and trace bridge, relative to
the explicitly cited established comparison theorems.

I read all of gl2_conductor_bridge.md and the final
gl2_conductor_section.tex, and reconstructed every implication.
The result is uniform for e at least one and coefficient prime ell
greater than three.

## Exact source and normalization checks

The actual source Newform definition was read in full. Its normalization,
geometric-Frobenius attachment, weight, semisimplicity, and explicit
minimal-level clause support the passage to the primitive normalized
classical eigenform. Chebotarev and Brauer–Nesbitt identify its Deligne
representation with the source R. A finite coefficient field and finite
extension containing the local flag may therefore be used.

The global KillsMu6 condition factors through Gal(Q(mu3)/Q), so its only
characters are 1 and chi_-3. The literal away-from-ell level condition
diagonalizes actual inertia, not merely its semisimplification.
Consequently monodromy is zero there, and only the tame quadratic
character at three is allowed. The cited Carayol theorem applies over Q;
its extra discrete-series hypothesis in even total degree is inapplicable.

The decisive coefficient-prime source has now been independently read:
Takeshi Saito, *Galois representations in arithmetic geometry*,
section 2c, Theorem 3, printed page 9, with the definitions on pages 7–8
and the complete printed proof outline on page 9. The author's primary
PDF is https://www.ms.u-tokyo.ac.jp/~t-saito/pp/suams.pdf and is saved as
saito_galois_arithmetic_survey.pdf/.txt. I also read the preceding
classical representation/weight and geometric-Frobenius normalization
on pages 5–6.

The theorem explicitly identifies the Frobenius-semisimplified *full*
Weil–Deligne representation of the classical form over Q, retaining
monodromy. Its proof outline separately compares Weil traces and ranks
of monodromy. The Hilbert analogue is stated in a separate following
paragraph. This is sufficient primary attribution; I did not recover
or claim a fresh full read of the original 1997 article.

## Coefficient-prime deduction reconstructed

After twisting, the two graded ordinary characters are an unramified
character and an unramified character times chi_ell^(-2e).
Continuity and compactness force each unramified Frobenius value to be
an ell-adic unit. The two rank-one crystalline slopes therefore differ
by exactly 2e. Exactness of D_pst preserves the graded factors.
After a common finite semistable extension, using the appropriate power
of Frobenius divides both slopes by the same residue degree.

A nonzero rank-one monodromy operator in a two-dimensional module
satisfying N phi = ell phi N forces slope difference one. Since 2e is
at least two, monodromy vanishes. The finite WD inertia has a flag with
trivial graded characters; characteristic-zero finite-group
semisimplicity then makes its entire action trivial.
Saito's full compatibility therefore gives an unramified automorphic
local component at ell. This does not assert that arbitrary extensions
of crystalline characters are crystalline.

For a source-internal cross-check I read the complete proofs in the
pinned source copies under work/hecke_coverage/interface:
BuildingsResidueChars__DpstRightExact.lean,
BuildingsResidueChars__WeilDeligneDpstLeftExact.lean,
BuildingsResidueChars__CyclotomicWeilCharProperties.lean, and
BuildingsResidueChars__TridiagonalWeilDeligne.lean.
Their exact exported results respectively provide admissible exactness,
left exactness, the rank-one cyclotomic character formula, and averaging
of finite-inertia triangular representations. The full
CompatAtLQ.lean theorem was also read, but its conclusion is SsCmp;
I have not mislabelled it as full WD compatibility. These reads are
source checks, not an independent Lean build.

## Finish and scope

The finite nebentypus is now unramified outside three and tame of order
at most two there. Odd parity forces chi_-3. Exactly one of the two
inertia characters at three is nontrivial, giving Artin conductor
exponent one and primitive level exactly three.
At a split prime p, the geometric-Frobenius twist multiplies the trace
of W by p^e, so the rank-three trace is exactly 1+a_p/p^e.

No dimension, Hecke eigenvalue, source unit criterion, or K-group
conclusion is inferred in this audit alone. Those are separate checked
arguments. The full local-to-global conductor implication and the
normalization asserted in the reviewed lemma pass.
