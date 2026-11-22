# MA-RB-012: the finite relative-zeta envelope

Date: 2026-11-22 UTC. Model: GPT-6 Astra Pro. Effort: inherited/not externally exposed. Author: MAS_ARTIN /root/s5_audit.

## Result and current review scope

The full new theorem is in modules/s5_relative_variational.tex, final638lines, SHA61a618d4eb481c727719620023170ab4f0fe2aec94a585190a06ba331aeb20a1. The author read every line of the original680-line proof in three untruncated portions, then all additions through684lines and the complete final citation-only/positive-product delta. All new mathematics passes. Root has separately read the entire684-line version and passed; final shorter-delta and peer status have their own records. Do not infer a peer pass from the initial route outline.

Final review status at2026-11-22T00:15:53UTC: root read all final deltas and passed; PF independently read the complete final638-line proof, all four rendered Aramata pages and the exact RB002/RB008 antecedents and passed. The status-only promotion adds one line and has SHA2a060c3ef363336fe7cae082b056b41b0f4ead7984745809187f0d70f0e7471d. The mathematics is unchanged from the638-line61a618d4 version. Existing question MA-RBQ-003, not a replacement identifier, now records the strictly smaller gate. The peer reviews remain distinct from the author's own check.

The theorem proves an unconditional strict decrease from the existing MA-RB-008 residual comparison interval. For every nontrivial subgroup H of S5, set K=L^H and use the entire relative function D_H=zeta_L/zeta_K. Its completed divisor is the nonnegative difference of the two completed Dedekind divisors. The exact logarithmic derivative has no pole terms, is positive through sigma=1, and has degree-dependent gamma asymptotic. The actual failure branch retains at least m_H k copies of gamma and1-gamma, where m_H=5-dim(W^H)+min(4-dim((V eta)^H),6-dim(X^H)). Every m_H is positive.

The finite envelope of the resulting variational bounds includes H=A5. Here the exact denominator is H_full(L)-H_full(E), strictly below H_full(L), hence strictly below or equal to the old retained-Euler denominator. Evaluation at the old attained interior minimizer gives a strict new minimum inequality. The new minimum may occur at sigma=1; no interior attainment is asserted. Both the multiplicity transfer and strict improvement are unconditional: the quadratic order b is subtracted exactly from the already proved lower bound b+5n+9k. No use of A, M or R_B is hidden in the passage.

The three displayed examples H=A5, a transposition subgroup and a five-cycle subgroup have (m_H,relative degree,gamma exponents) equal to (9,118,58/60), (5,60,30/30), and (8,96,48/48). These use existing character rows, not a new subgroup enumeration or representation certificate.

## Complete author proof checks

Checked exact normality of L/L^H, all-prime divisibility, cancellation of completed zeros with their multiplicities, and the removal of both endpoint factors. The quotient canonical product has order at most one by a direct O(R log^2 R) bound; no reciprocal estimate near zeros is assumed. The functional equation fixes its Hadamard constant. Nonemptiness follows from its positive-degree gamma asymptotic, and positivity at sigma=1 follows from reflection of a nonempty containing-strip divisor. This supplies a genuine continuous finite endpoint value without using an Euler series there.

Rechecked every signed irreducible order at the actual residual gamma from MA-RB.19–26. All coefficients dim(U)-dim(U^H) are nonnegative; neither unknown five-dimensional factor is assumed globally holomorphic. The lower bound m_H uses only x_W=n+k and v1+e>=k. Reflection is applied to the actual completed relative function, not to an isolated unsigned Artin order. All denominators in the two-real-zero algebra are positive.

Checked every signature, the exact Gamma_R/Gamma_C duplication identity, conductor quotient, the attained old-minimum strict comparison, and the finite-family order of minimum/infimum. The Euler tail has coefficient bound120+n_H (122 for E) and integrates log(x)x^(-sigma) from N>=3. Its certified upper denominator is positive and gives a valid upper endpoint. Rational sigma samples plus finite truncations recover the infimum from above; no uniform bound at sigma=1 is asserted.

The added positive-product paragraph is limited to the same guaranteed multiplicities: its ratio is a weighted average of m_H/H_H. The guaranteed zero multiplicity is k times the numerator, which is stated explicitly. Such products cannot beat the finite envelope by this same argument. Higher actual orders or new arithmetic constraints remain outside that assertion.

The finite-cover placement is an actual rational complement of Q[G/H] in Q[G], with right-H averaging commuting with the left G-action. This gives an actual Artin representation, not merely a virtual class. Frobenius traces can still have either sign. The proof's positivity is that of the completed excess zero divisor.

## Exact source reading and classical-result scope

Aramata, H. (1933). Über die Teilbarkeit der Dedekindschen Zetafunktionen. Proceedings of the Imperial Academy,9(2),31–34. https://doi.org/10.3792/pia/1195580866 . Freshly read all four primary pages, including all formulas in Sätze1–6 and the final analytic argument, from rendered local page images. The exact theorem onp31 is normal-extension entireness, and the proof ends onp34. The original PDF was downloaded from https://www.jstage.jst.go.jp/article/pjab1912/9/2/9_2_31/_pdf/-char/en . It and the four rendered PNGs were moved outside the deliverable tree to /workspace/scratch/6669db261d5b/private_sources/aramata1933.pdf and aramata1933_page-1.png through-4.png.

A finite cyclic Fourier-character rederivation was independently checked during author QA, then removed from the paper at root's request to comply with the user's instruction to cite known results in their exact form rather than reproduce their proofs. This is classical Aramata divisibility, not a new finding. The final paper uses exact citation and application at MA-RB.177; tags178–180 remain unused.

Freshly read the supplied Hu–Kaneko–Martin–Schildkraut HigherOrderZeros.tex, lines125–193: the ramified-inertia Artin definition, lem:artin-L(a)–(d), induction holomorphy interface, Aramata lemma, and the entire proof of cor:hol-quotient. This is the scope used, not a fresh reading of that whole research paper or of every cited foundational monograph.

Freshly reread the full invoked NT-Z10 local zero-count argument, MA-RB.8–12's entire completed-Hadamard proof, MA-RB.19–26's actual order deduction, and MA-RB.85–96's positive Euler remainder and attained minimum. General Dedekind continuation/functional equation and fixed-strip growth remain the established inputs; no new full Simonic or Neukirch source-proof audit is claimed. SGA1 V section7, Deligne1979 Definition6.1/sections6.2–6.3/equation0.5.3, and Neukirch VII(11.7)–(11.9), printed533–534, are exact inherited locators.

## What remains open

This is one finite-family reduction of the pre-existing shared-real-zero gate. It does not prove that the new minimum is nonpositive for every actual field, exclude all shared real zeros in the remaining interval, prove R_B, or construct a positive-excess field. No numerical optimization, arithmetic zero search or new finite representation certificate was performed.
