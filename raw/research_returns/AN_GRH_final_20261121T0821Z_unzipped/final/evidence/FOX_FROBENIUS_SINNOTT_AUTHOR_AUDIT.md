# Fox, Frobenius, and Sinnott: author proof and source-scope audit

Date: 2026-11-21.

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Reviewed source: `FOX_FROBENIUS_SINNOTT_PROBE.md`.

SHA256: `9007417edb41c7fe3ca0bfb52417a35ec11bd8c55fbbf1ff5ef9cea4f63bbb98`.

## Verdict and exact mathematical scope

**PASS, author complete-proof and scope read.** I read the complete note after writing it, including both full elementary algebra arguments. This is an author review, not an independent re-proof.

For the completed algebra, I checked the quotient-compatible averaging idempotents, their conductor evaluations and orthogonality, the finite-at-each-level definition of the infinite sum, and the exact exponent in each conductor. In the nonconstant-deck version I checked the character permutation, reduction of the orbit cokernel to one scalar relation, the lifting-of-exponent equality including coefficient prime two, and preservation of elementary-divisor exponents under finite unramified extension. The resulting example is explicitly an abstract completed module; it does not satisfy or claim geometric Weil-weight or polarization conditions.

For the fixed-rational-function implication, I checked normalization by a uniformizer, the exact order of prime-to-p roots after reduction, the degree of their minimal polynomials, eventual growth of that degree, and the Smith-invariant exponent bound when an actual fixed integral matrix is supplied. The applicability to a primitive Jacobian factor remains conditional on an identification that has not been obtained. A growing semilinear return product is not a fixed rational function.

I checked the distinction between a finite profinite presentation and a finite discrete-word presentation, including the failure of the pro-prime-to-p surface group to retain characteristic-p H1. The note does not claim that no geometric rationality theorem can exist. It records that the inspected statements do not give the needed theorem.

## Primary reading actually performed

The retained source manifest records the exact PDFs, extracted text, hashes, URLs, reference IDs, and reading scopes. In particular:

- Esnault–Shusterman–Srinivas: the finite-presentation definition, Theorem 1.1 statement, and surface-presentation distinction on pp.2–4. No complete audit of the general theorem's proof.
- Shusterman: the complete six-page preprint, including the displayed proof of Theorem 1.1 and Corollary 1.2. External cohomological inputs are used as cited.
- Kodani–Morishita–Terashima: the setup, continuous Fox rules, Magnus-cocycle definition, and abelianized power-series construction, including the complete displayed proof of Proposition 4.3.4. No whole-paper audit.
- Asvin G.: Definition 8/Remark 9, complete Lemma 17 and Lemma 21 proofs, the Section 3 setup, all of Section 3.1 including equation (6), statements/scopes of Theorems 23 and 26, and the first truncation paragraph of Section 3.3. No complete check of the long congruence proofs.
- Sinnott: Sections 1.8–1.16 and the complete displayed proof of Theorem 3.2 including Lemma 3.6. The independence theorem used there was not independently reproved.

The later targeted recheck reopened the retained Sinnott definitions and theorem, Asvin's Lemma 17 proof, equation (6), Theorems 23/26, and the truncation paragraph. These agree with the stated coefficient-prime and rationality restrictions.

## Independent check received

The effective-Galois agent separately read both complete elementary algebra arguments and passed them with their nongeometric and conditional scopes. That agent also directly checked the Asvin passages listed in its message: Definition 8 Case B/Remark 9, complete Lemma 17 proof, Section 3.1/equation (6), Definition 25/Theorems 23 and 26, and the first Section 3.3 paragraph. It did not claim to check the other four sources or the full congruence proofs. Its separate audit is owned by that agent.

## What was not done

No curve, actual infinite tower, arithmetic Frobenius presentation, or geometric p-primary group was computed. No counterexample to an actual geometric exponent bound is claimed. No new finding number, priority claim, universal witness theorem, or main-gate closure is assigned. This is a bounded failed-supply probe with an exact sufficient premise for a future route.

## Subsequent integral-source qualification

The earlier reviewed note remains unchanged at the hash above. A later direct reading of Asvin's complete printed Lemmas11–12, prompted by the effective-Galois reader, found an integral source issue: the natural map associated with [ell]:E→E on an elliptic curve is multiplication by ell on rank-two integral H1/Tate modules, so the inferred surjectivity and natural-image saturation fail. The A51 supplement records this explicit counterexample and treats the geometric integral finite-matrix description only as the paper's statement, not an established input. Its two algebra proofs and the abstract Section3 coefficient-prime limitation remain unchanged. The later exact-hash review is recorded in `A51_FOX_RATIONALITY_AUTHOR_AUDIT.md`.
