# Independent audit of the Greenberg integral corollary

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; reasoning effort not exposed.

**Verdict: PASS.** Read the complete `work/greenberg_integral_corollary.tex` and its bibliography. The proof correctly extends the infinite-even-indecomposables conclusion to irregular primes satisfying the already audited one-variable Greenberg hypothesis. It gives no converse to that hypothesis and does not extend the asserted primitivity of a prescribed full-domain Soulé normalization.

Reviewed TeX SHA-256: `b550f6592e44a1f802bd5720a4f29ffff6cd01c2ac316060c8a299fd1c0aaa63`.

## New primary arithmetic input

Freshly opened Ribet's author scan, <https://math.berkeley.edu/~ribet/Articles/invent_34.pdf>, and visually read printed p. 151 in full, including the Main Theorem (1.1). Its hypotheses are 2≤k≤p−3 with k even, and its conclusion identifies divisibility of the numerator of B_k with nonvanishing of the χ^(1−k) eigenspace of the class group modulo p. Since 1−k is odd, this lies in the minus part. Thus irregularity gives A_0^-≠0 without a plus-class-number assumption. The converse used in the text only says that a nonzero p-part of the minus class group makes the full class number divisible by p, hence p is irregular. The stated citation and bibliography match the scan. Retrieval references: `turn108936888view1`; screenshot `turn818585723view0`.

## Whole-proof check

The regular-prime conclusion is explicitly inherited from the previously checked regular-prime theorem. In the irregular case the already audited Greenberg kernel theorem supplies faithfulness of H, hence separation of its actual weight filtration; the previously checked outer saturation proposition identifies the relevant integral filtration. Neither implication presupposes integral odd generation.

The class-group step uses the actual injection A_0^-→A_infinity^- and actual Kummer duality for M^+, not merely a pseudo-isomorphism to infer nonvanishing. The pseudo-isomorphism and Ferrero–Washington are used only for finite generation over Z_p. Freeness of H makes its abelianization Z_p-torsion-free. Consequently nonzero M^+ is finite free of positive rank. All three roles are correctly separated, so a finite pseudo-null error cannot invalidate the nonvanishing assertion.

For the induced filtration M^n, images of the compact F^nH are compact and closed. If x belongs to every M^n, the nonempty compact fibres F^nH∩π^{-1}(x) form a nested family, whose intersection is nonempty. Separation of H forces x=0. Therefore the induced filtration on M, and on its plus part, is separated. The natural surjection gr_n(H)→M^n/M^{n+1} kills Lie brackets, giving the displayed surjection from the degree-n Lie abelianization.

Complex conjugation acts by (−1)^n on the weight-n graded piece. Since p is odd, the plus projector is integral and exact. Thus the induced filtration of M^+ changes only in even weights. Each integral graded Lie piece is a finite free Z_p-module through its outer Johnson embedding. Degreewise Lie abelianization is finitely generated, and rational freeness on the odd generators makes its even parts zero after tensoring with Q_p. Hence those even parts, and their quotients in gr(M^+), are finite p-groups.

If only finitely many plus graded quotients were nonzero, the filtration would stabilize. Separation makes its stable tail zero. The exhaustive filtration would then express M^+ as a finite succession of finite groups, contradicting its positive Z_p-rank. Thus infinitely many even gr(M^+) pieces are nonzero, and the displayed surjections force infinitely many nonzero finite even Lie indecomposable pieces. Odd homogeneous integral generators would annihilate every such even indecomposable piece, so their existence is impossible at these irregular primes.

## Scope

No first exceptional weight or torsion exponent is determined. The hypothesis remains X^+ finite. The corollary does not establish one-variable Greenberg, does not claim a reverse implication from kernel faithfulness to Greenberg, and does not need Vandiver's condition. The proof and the final qualification accurately preserve these limits.
