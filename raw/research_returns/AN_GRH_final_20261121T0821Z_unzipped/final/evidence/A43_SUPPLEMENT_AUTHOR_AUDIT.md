# A43 general-target supplement — author check

Date: 2026-11-21. GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

Source: `A43_GENERAL_TARGET_SUPPLEMENT.tex`, SHA256 `ebe6bd8e885d404bce814b78a6b160440d8cb5201497d951e33d6fd934c7beff`.

**PASS, author whole-proof check.** This is a complete short consequence of the already checked A37; it is not an independent re-proof of A37 or a new main-gate closure.

Checked: relative Frobenius twists every automorphism and its integral polynomial relation; a fixed-point-free order-three action would give an etale genus-two quotient with impossible genus; the defining locally exact differential sequence identifies the actual Raynaud line bundle under the twisted automorphism; a fixed point therefore gives a nonzero theta class annihilated by three; ordinary non-effectivity excludes zero; A37(2) with exactly `S={3}` supplies finite-field ordinary Rosati-O5 curves where this is impossible geometrically. The Torelli consequence is limited to polarization-preserving automorphisms satisfying the displayed order-three identity. The final two Frobenius/Rosati identities were expanded directly using commutation and `T²+T=1`.

Exact primary sources inspected: Stacks Project Section53.12 and Lemmas53.12.2/53.12.4, Tags0C1D/0C1F, including their displayed proofs; Ozman–Pries §§8.1–8.2 (published p472; arXiv1502.05959v3 pp17–18), the defining sequences, theta-support criterion and ordinary-origin criterion. The publisher PDF open failed, while its indexed primary excerpt and the author arXiv PDF supplied the passages. The invariance of B is proved in the supplement, rather than attributed to an unlocated separate theorem. The full underlying Raynaud papers were not reread for this short consequence. MilneJV Torelli12.1 is used with the exact statement and uniqueness/descent review already recorded for A43.

No computational certificate or formal verification is claimed. No final-directory file was edited.

Final clarification: source SHA256 `8773d4ca3157d17fa8c4eae08065e25a5702944298d7cbbb7864bcfe3ff110f7` differs only by explicitly saying that the specified RM action is defined over the finite ground field, hence T commutes with q-Frobenius and its Rosati dual in the last algebra paragraph. I checked this narrow clarification; it does not change the hypotheses of the intended target class or add a second whole-proof review.
