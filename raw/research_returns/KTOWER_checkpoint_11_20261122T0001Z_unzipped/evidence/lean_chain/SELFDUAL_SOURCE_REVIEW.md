# Independent review of the self-dual actual-source exclusion

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21. No Lean kernel build was run.

## Verdict and exact scope

PASS after a whole read of `selfdual_source_exclusion.tex`, the entire five-page Ramakrishnan author note, and the source interfaces listed below. The separately proved scalar-normalization lemma supplies the determinant-free last step. The result excludes every **self-dual** actual stable Type I source under the exponent-e auxiliary unit. It does not exclude the remaining conjugate-self-dual sources whose dual is their distinct conjugate.

The first reviewed version has SHA256 `16ac07f7123faa68b2b500f1aef49d7c58a606de0eee8361b59f53a9b94f77c6`. A requested wording clarification makes the corollary assume the base hypotheses without assuming self-duality; this is not a mathematical change. The adjacent manifest records the final version when reconciled.

## Mathematical audit

Self-duality makes the actual determinant sign-valued; the residual determinant is identically one and p is odd, so the determinant is exactly one. Full Frobenius characteristic-polynomial attachment, with the already checked rank-three common cyclotomic normalization, transfers both self-duality and trivial central character to the unitary-normalized cusp representation over E.

Conjugate self-duality then gives Galois invariance. Arthur–Clozel's cyclic quadratic descent is explicitly cuspidal. A descended central character lies in `{1, eta}`. The other possible duality fiber would change that central character by eta, which is impossible in odd rank. Twisting the descent by its central character therefore produces a self-dual, central-character-one cusp representation over Q with unchanged base change.

Ramakrishnan's Theorem A supplies a non-dihedral GL2 origin; his explicit archimedean compatibility identifies its real parameter. The complex-character ratio is `(z/bar z)^e`, so its discrete-series weight is e+1. A holomorphic vector gives a classical form of that weight. Its nebentypus is odd because e is even, hence its Galois representation has complex-conjugation eigenvalues 1 and -1. No determinant or classical-level claim is made before the scalar twist.

The full compatible unramified polynomials identify the adjoint restriction with the original irreducible R. An adjoint representation with irreducible semisimplification of dimension three is itself irreducible, so the identification is an actual isomorphism. This also forces absolute irreducibility of the rank-two origin; no additional all-primes big-image theorem is required.

`KT-ODD-ADJOINT-SCALAR-NORMALIZATION` now applies to the odd origin. It constructs a scalar twist with residual pair `1 + eta omega^e`, unramified ordinary quotient, and unramified restriction away p. The reviewed ordinary rank-two unit exclusion then gives the contradiction. This uses the actual ordered inertia flag, not a converse from crystallinity.

## Exact primary source checks

* D. Ramakrishnan, *An exercise concerning the selfdual cusp forms on GL(3)*: entire five-page author version read, including the complete Theorem A proof, Proposition C proof and Corollary B proof. Theorem A is on author page 1; Corollary B pages 1–2; Proposition C(b) page 3; formula (6b) page 4. Author PDF SHA256 `54b25c1e2b2e02d7ecb934ba294bcc73975d323e773a836235bec497e1632a11`, preserved under `unitary_audit/reducible_comparison/primary/`. The foundational transfer/descent inputs cited within that note were not reconstructed.
* Arthur–Clozel, *Simple algebras, base change, and the advanced theory of the trace formula*: Chapter 3 Theorem 3.1 and entire displayed proof, printed page 201; Theorem 4.2 setup and clause (d), page 202; Theorem 5.1 and entire displayed proof, pages 212–213. These were reread in the preserved author-book copy. The full lengthy weak-lifting proof was not reread in this event; its previously checked theorem is the imported input.

## Exact pinned-source interfaces

At commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`:

* `AfStmt.lean:29–32` supplies irreducibility, automorphy of the common cyclotomic twist, and `Level` with ordered exponents `(e,0,-e)`; the whole file was reread.
* `IsAutomorphicOverImagQuad.lean:35–36` explicitly supplies regular algebraic, conjugate-self-dual **cuspidal** automorphy; the whole file was reread.
* `KeepLevel.lean:30–82,95–101` gives the infinitesimal character and full Satake/Frobenius compatibility; the whole file, including its proofs, was reread.
* `BlochKatoSelmerVanishes.lean:66–82` gives `KillsMu`, `algSat`, and attachment by full characteristic polynomials. Lines 102–114 give a stable full decomposition-group flag, with inertia characters determined by the ordered exponents. For N=2 every finite character is trivial. These exact definitions were reread.
* The actual-point residual transport, away-prime inertia, and finite-coefficient descent use the earlier whole source checks of `IsPtOf.lean:124–166`, `PtInertiaAway.lean:54–69`, and `TanDet.lean:212–216` (including the full `fin_gen`, `pow_le`, `fin_quot` proof chain). They were not replaced by a bare admissibility or ambient-spectrum assertion.

The result is a new arithmetic restriction on the actual source class. It gives no class-group/Selmer vanishing without a further argument excluding the remaining non-self-dual stable systems.
