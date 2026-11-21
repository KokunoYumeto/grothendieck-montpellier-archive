# Independent full check of THETA3-B18

Reviewer: GPT-6 Astra Pro, /root/theta_032, 21 November 2026. Inherited effort label not exposed. The complete main proof and all final additions were read and reconstructed. **PASS after the explicit bilinear-input convention correction described below.** No Lean compilation or transitive dependency audit is asserted.

## Real rank-three to rank-two table

The six signature entries follow from the shifted Harish-Chandra parameters for m0=-2,0,2. The active canonical parameter is (1,0;-1); the compact parameter is (1,0,-1;empty). The five ordinary cases have Atobe chain length one. The compact m0=0 case instead has chain length three, base signature (0,0), and l=1; this gives the stated mixed target. Necessity of these three m0 values and nonvanishing at the stated base/tower point agree with Atobe Definition1.6/Theorem1.7 and Ichino Theorem4.1(ii), which were read.

## Finite and global parameter statements

Gan–Ichino Theorem4.4 and its enhanced packet rule supply the nonsplit deletion formula for the local oscillator quotient. Minguez Corollary6.3 and the transpose-inverse action convention supply the split formula without a temperedness assumption; Ichino Lemma8.4 corroborates the chosen character normalization. The assumption that base changes are isobaric sums of unitary cuspidal representations is explicit. Under that assumption strong multiplicity one identifies the displayed isobaric sum. A cuspidal GL2 summand makes the GL1 constituent unique; changing the other splitting character only determinant-twists the smaller representation on the same local spaces. The obstruction and finite-list alternatives are correctly conditional on these specified transfer hypotheses.

## Equal-rank central value and local tests

Jiang–Wu Theorem3.3(1), m=2, epsilon=0, j=1 gives lowest occurrence at most two at a finite nonzero central value. A noncharacter local component excludes rank zero. First occurrence is cuspidal, and the real condition forces the constructed global rank-two space to be definite; global construction supplies finite coherence.

I visually re-read Jiang–Wu printed p15: its integral is theta times f, without complex conjugation. Hence its integrating automorphic representation rho corresponds to local Howe input tau=rho-dual. The final B18 revision now explicitly uses tau in all local Harish-Chandra and epsilon rules, while preserving rho=sigma times chi-inverse in the global theorem. B16 received the same clarification. This correction supersedes any unqualified use of rho as the local Howe input in earlier drafts.

For a mixed equal-rank discrete series with half-integral parameters a,b, an integer m0/2 strictly between them exists and yields the definite target determined by their order. For compact input, choosing outside their interval gives a definite target. The character-extension lemma globalizes these choices but does not prove central-value nonvanishing. The finite equality in B18e agrees exactly with Gan–Ichino Theorem4.1(ii), p13: epsilon(1/2,phi_tau chi_Y^{-1},psi_2^E)=epsilon(Y)epsilon(X), with psi_2^E(x)=psi(Tr(delta x)). The factor1/2 belongs to their separate Whittaker-normalization character, not this epsilon-test character.

The final text correctly does not conclude that the newly constructed rank-two representation lifts back to the originally specified rank-three representation or satisfies the arithmetic kernel/covolume law.
