# Whole-proof and primary-source review of K-022

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `SMOOTH_CANCELLATION_COUNTEREXAMPLE.tex` and
`verify_smooth_cancellation.py`; replayed the exact verifier successfully.
Independently opened Corti–Reid, *Weighted Grassmannians*,
<https://arxiv.org/pdf/math/0206011>, and read section2(iii)–(v), printedpage4;
all of Proposition2.1, its equivariant resolution (2.4), and its proof,
printedpages5–6; the weight definition and charts, printedpage7; and the
Hilbert numerator, printedpage8. The source's resolution is a stated
classical input. The new cancellation argument is checked in full here.

The Plücker ring is the actual SL2 invariant ring, and the displayed
positive column weighting is an allowed one-parameter subgroup with `u=0`.
Restriction of the equivariant resolution gives precisely the numerator
and denominator in K-022b. On each nonzero Plücker chart, one invertible
coordinate and six free coordinates describe a smooth seven-dimensional
open set. Connectedness and the absence of SL2 characters make ambient
irreducible factors invariant, proving factoriality. The codimension-three
self-dual resolution gives Cohen–Macaulayness and Gorensteinness.

For the rational-singularity check, all the twisted projective-space terms
have degree at least minus5, hence have no positive cohomology on P9.
The resolution therefore proves the required vanishing on the ordinary
Grassmannian for every nonnegative twist. The total space of O(-1)
resolves the affine cone, and its affine projection reduces the structure
sheaf cohomology to those vanishing groups. Normality supplies the
degree-zero pushforward. This argument concerns the ungraded singularity
and is compatible with the new weighting.

For every `M=2^a>=8`, exactly the Plücker weights `p15` and `p34` are zero
modulo M. Restricting all five Pfaffians gives exactly the ideal
`(p15*p34)`. Thus the complete positive-dimensional fixed scheme consists
of the two asserted smooth curves; neither additional curves nor embedded
nonreduced components are hidden in the restriction. Both closures are
weight-M polynomial lines and have normalized density one.

The six chart eigenvalues at either line give the displayed moving products.
Writing `x=zeta_M`, their determinants are exactly
`-4i(x+x^-1)^3` and `+4i(x+x^-1)^3`; they are nonzero for M>=8.
Their inverses therefore cancel exactly. Independently, expanding the
two-variable Laurent factorization K-022f gives the numerator identically;
`u^2+1=Phi_M(t)` after `u=t^(M/4)`, so it cancels both denominator factors.
The complete M8 reduced numerator and all cyclotomic denominator exponents
were replayed, including their gcd check.

The result refutes a qualitative smooth-fixed-component transfer in the
stated weighted invariant-ring class. It does not establish cancellation
for the uniformly graded triple-tensor ring, and it does not bound all
other actual pole orders in this family. Those limits are stated correctly.
No defect or correction was found.
