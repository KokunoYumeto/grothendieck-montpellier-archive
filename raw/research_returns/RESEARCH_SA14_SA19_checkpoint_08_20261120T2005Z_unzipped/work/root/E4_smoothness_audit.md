# Targeted independent audit of E4.S

Date: 2026-11-20 17:44 UTC. GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited and not exposed.

Outcome: PASS for the exact distinction between fibrewise and relative smoothness, after reading `work/bce/new_E4_smoothness.tex` in full. DGJ's separate complete audit is `work/dgj/audit_E4_cusp.md`.

The displayed Weierstrass cubic has ordinary smooth generic fibre and integral cuspidal special fibre. Its infinity section is smooth. Diagonal translation by the nonzero two-torsion section on the fixed ordinary elliptic factor makes the constant Z/2 action free, so the quotient remains projective flat with geometrically integral reduced fibres.

The rigidified product/descent argument works for the singular curve because its proper geometrically integral fibres still have only scalar global units. The infinity rigidification removes the scalar ambiguity in the involution linearization. Pullback from the quotient elliptic curve accounts for the character ambiguity and is split by the fixed infinity section. Product cross-correspondences cannot enter the numerical-triviality part. Thus Pic-tau is the stated product with the two-torsion of the relative generalized Jacobian, compatibly with base change.

The ordinary generic two-torsion is nonsmooth of dimension zero; the cuspidal generalized Jacobian is Ga and its two-torsion in characteristic2 is all Ga. Consequently the Picard fibre improves from nonsmooth dimension1 to smooth dimension2, while its tangent dimension stays2. Fibrewise smoothness is therefore not open, and tangent-minus-dimension is not upper semicontinuous. This does not contradict openness of the smooth locus of the total relative morphism: a relative smooth point in the special fibre would force nearby relative dimension2, absent generically. No normal-special-fibre conclusion is inferred.
