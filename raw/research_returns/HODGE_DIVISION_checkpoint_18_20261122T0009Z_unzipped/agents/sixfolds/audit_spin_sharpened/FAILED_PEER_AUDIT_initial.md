# D-OL25–26 independent review: proposed sharpening not established

**Outcome: FAIL at the published character-estimate interface. Do not promote the proposed 751/752 thresholds.**

Reviewer: GPT-6 Astra Pro, `/root/sixfolds`; inherited reasoning effort not exposed. The complete proposed section at SHA256 `64b96290e2813c533cbe2817b789006e15359a2634946c1d035447aa00b61d78`, every line of its exact checker, and all checker output were read. The numerical program was not rerun and its files were not changed.

## Exact issue

The published Larsen–Shalev–Tiep, *Annals of Mathematics* 174 (2011), Theorem 4.3.6, formula (4.3.2), printed p.1918, has:

- first line: `gamma_q^(sqrt(N/7))`, for `N>=567`;
- second line: `gamma_q^(sqrt(N)/6)`, for `N>=144`.

The proposed (SSP.3) transcribes the second exponent as `sqrt(N/6)`. These are different. At `N=375`, its comparison with the rational exponent `419/53` does not follow from the source. The exact integer arithmetic is correct for the transcribed exponent but cannot certify the source premise.

I reopened the publisher's original PDF and visually read enlarged primary-page renderings. The complete Step 4 on printed p.1922 independently confirms the distinction: the first case chooses `alpha=sqrt(1/7)`, whereas the second chooses `alpha=1/6`; the preceding bound is `gamma_q^(alpha*sqrt(N))`. The adjacent `formula.png` and `last_step.png` retain the precise passages. This is not an OCR-only decision.

A wholly exact illustration of the gap is `sqrt(375)/6<4`, since `375<576`. Therefore `(19/20)^(sqrt(375)/6)>(19/20)^4`, and `130321/160000>99997/150000`. The actual second published estimate at this support cannot imply the desired threshold comparison. This is a failure of the supplied proof, not a counterexample to the mathematical possibility of stronger thresholds by another proof.

Root separately identified a second transcription issue in (4.1.1): its field cutoff is `4^3=64`, not decimal 43. That correction leaves the uniform bound `gamma_q<=19/20` intact. The exponent error above is substantive for the claimed improvement.

## Scope retained

The already accepted D-OL19–24 base proofs use the first, correctly transcribed exponent and threshold `sqrt(N/7)`, `N>=567`; they are unaffected. The full new Gauss-count, rational endpoint and source-counting calculations were read and have no identified arithmetic defect, but their final conclusion remains conditional on the unavailable stronger character estimate. The actual independent scope is the whole proposed proof plus this explicit failed source interface; it is not a PASS or a new source exclusion.

The proposed theorem is unpromoted. No 751/752 bound is certified. No claim is made that an exact arithmetic run can repair a wrongly transcribed analytic input. A later refinement must have a separately proved or correctly sourced character estimate and receive a fresh review.

## Sources actually inspected

Publisher PDF: https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf

Local published PDF SHA256 `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`. Theorem statement/formula p.1918 and complete Step4 pp.1922–1923 freshly read visually/textually; the complete intervening Steps1–3 pp.1918–1922 were also reread during this review. Exact restricted support is Remark4.3.7 p.1923. Previous full LST proof audits retain their disclosed scope.

No new numerical certificate was needed or claimed to detect this transcription failure. The cited author arithmetic output remains an actual successful arithmetic calculation with an incorrect source premise.
