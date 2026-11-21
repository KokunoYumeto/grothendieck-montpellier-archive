# Review of the main paper: archive, binomial, and related proofs

Reviewer: `/root/archive_binomial`. Model: GPT-6 Astra Pro, inherited. Reasoning effort: not exposed by the runtime. Client date: 2026-11-21, Europe/Berlin. The reviewed root file is `DP_MULT_work/DP_MULT.tex`; it is being edited concurrently. No root paper edits were made by this reviewer.

## Review event ABA-PR01

**Actual interval:** 2026-11-21 00:06:41--00:07:32 UTC. The completed DP7--DP14 statements, whole proofs, and their immediately surrounding qualifications were read from the root file, not inferred from the earlier agent report. In this snapshot DP10 had not yet received the announced Cech restricted-power paragraph, and DP15--DP16 were not present.

This is a separate review of the root's draft by another agent. Some components of DP10--DP14 originated in this reviewer's earlier ABA report, so it must not be described as an independent second derivation of those components. DP1--DP6 were used as inputs for DP7--DP9; their complete proofs were not audited in this event. External theorems were checked at the statement/application level, not reproved.

| Statement | Whole-proof result | Details |
|---|---|---|
| DP7 | Pass relative to the cited coefficientwise bounds DP1, DP3, DP4 | A formal-group homomorphism intertwines the invariant vector fields. Pullback is integral. On a product, each operator acts in its own factor and preserves divisibility already supplied by the others. Formal coefficient manipulations are finite for each fixed output degree and derivative order. No integral direct-factor hypothesis is needed for the first directional assertion. |
| DP8 | Pass | The multiplicative product gives a valid total-height counterexample. The rank-one CM Tate module gives the local heights, the CM type gives local dimensions, and conjugate pairs give d_v+d_barv=h_v. For a self-conjugate place this means 2d_v=h_v. For a distinct conjugate pair with d_v=1, the pair contributes h_v to the dimension, proving g>=h_v. A typesetting typo remains in the multiplicative-product notation: the exponent contains an extraneous comma. |
| DP9 | Pass | The exact quotient c_h/c_2 and its strict upper bound are correct. The unit 1+t has local multiplicity zero despite all applicable derivative bounds. Multiplication by p^N preserves its generic-fibre divisor. This refutes only the stated implication, as the following text properly says. |
| DP10 | Needs the announced restricted-operation identification before full acceptance | The vector-kernel calculation, Cartier sequence, orthogonality, and Oda reconstruction are correct. However, an arbitrary p-semilinear map makes an abelian Lie algebra restricted, so the current phrase x^[p]=F(x) does not on its own identify the actual p-operation of the universal extension. The Cech symbolic-power computation in ABA-2 closes this precise gap; details below. |
| DP11 | Pass | All localization, digit-lifting, ideal-membership, and comaximality steps are valid without noetherian or completeness assumptions. Torsion-freeness is used for unique division and embedding in S_Q. The Newton-identity argument and the converse via rational polynomial identities checked on nonnegative integer ranks establish the full special lambda identities. Ring-map compatibility uses torsion-freeness of the target. |
| DP12 | Pass with minor precision edits | The Newton basis, leading coefficient, coproduct, finite differences, ordinary-derivative counterexample, and both p-derivation identities are correct. Add the antipode x->-x to make the Hopf conclusion explicit. State Delta b_n=b_(n-1) for n>=1 and Delta b_0=0, or define b_(-1)=0. Qualify the nonordinary-derivation assertion by a nonzero-ring condition, since the zero ring is a torsion-free unital ring under the convention allowing it. |
| DP13 | Pass as an application of Horel; clarify notation | Horel's hypotheses match the stated connected nilpotent finite-type case. The mapping direction A_Y->A_X is correct. The left Map(X,Y) must mean the derived mapping space in the category of spaces; a raw simplicial mapping complex would require a fibrant Y. No proof of Horel's theorem is being claimed, correctly. |
| DP14 | Pass | The coefficient-of-t counterexample is exact, and the reference to DP12 correctly distinguishes ordinary differentiation. The proof explicitly leaves richer comparison constructions open rather than asserting a universal no-go theorem. |

### DP10: exact missing compatibility and source

Use the universal extension E(B), B=A^vee, as the group of algebraically trivial line bundles on A, rigidified at the origin and equipped with integrable connection. A tangent vector is represented on an affine cover by transition functions 1+epsilon f_ij and connection forms epsilon omega_i, hence by the de Rham Cech cocycle (f_ij,omega_i).

SGA 3 VII_A, 6.2--6.3 computes the symbolic p-power by tensoring p independent infinitesimal copies and then sending the elementary symmetric functions sigma_1,...,sigma_(p-1) to zero and sigma_p to epsilon. The tensor product has transition functions product_j(1+epsilon_j f_ij)=sum_r sigma_r f_ij^r and connection forms sigma_1 omega_i. Thus the actual restricted operation is (f_ij,omega_i)->(f_ij^p,0), which is Oda's de Rham Frobenius (Definition 5.3). This is an identity of the actual operations, not a choice of an arbitrary semilinear structure.

The exact primary URL for the moduli realization is:

https://arxiv.org/pdf/2504.14801

Gyujin Oh and Koji Shimizu, *Moduli stacks of crystals and isocrystals*, arXiv:2504.14801v1 (2025), Theorem 9.6 and Remark 9.7, PDF/printed pp.94--95. The theorem explicitly gives the universal vector extension of A^vee as triples (L,u,nabla) with an integrable connection. It cites Mazur--Messing, LNM 370 (1974), chapter I, 1.10 and 2.6 for existence and Propositions 2.6.7, 3.2.3, 4.2.1 and (4.6.3) for the moduli interpretation. Remark 9.7 verifies compatibility of the projection and vector kernel, citing Mazur--Messing pp.3,15--16,40. This is a convenient inspected primary research source reporting the classical theorem; the original Mazur--Messing proof was not inspected directly in this run.

The Oh--Shimizu hypotheses in this subsection are a projective abelian scheme over a noetherian base. They cover the abelian variety over a perfect field used in DP10.

### Additional source and notation checks

- Oda Theorem 1.1 begins on printed p.67; Corollary 1.3 is on pp.69--70. The root citation to pp.68--70 should be widened to pp.67--70. URL: https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf . This was rechecked in the actual primary text during the review.
- The precise derived-adjunction direction in DP13 is Map_cBRing(A_Y,A_X) = Map_cBRing^op(A_X,A_Y) ~= Map_S(X,G(A_Y)) ~= Map_S(X,Y). The final step uses the unit for Y. No reversal is needed.
- The final cote47 integrality expression is deliberately excluded from forced-correction claims: as transcribed, it is chi times the true kth Chern coefficient and can be a valid weaker consequence.

## Review event ABA-PR02

**Actual interval:** 2026-11-21 00:09:31--00:10:09 UTC. Read the latest actual DP10--DP16 statements and complete proofs, including the newly inserted Cech compatibility and the finished DP15--DP16. Also checked the modified DP12 and DP13 statements, the DP10 page locator, and the Mazur--Messing/Oh--Shimizu bibliography entry. This was a full reading of these proofs, not only a diff review.

| Statement | Result after rereading | Precise scope |
|---|---|---|
| DP10 | PASS | The inserted transition-function and connection-form calculation identifies the actual restricted p-operation with Oda's Frobenius. The reconstruction no longer relies on arbitrarily assigning a semilinear map. The Oda locator has been corrected to pp.67--70. The MM bibliography clearly identifies the inspected Oh--Shimizu source and its exact original references. |
| DP11 | PASS | Reread the entire Fermat and lambda proof. No remaining mathematical defect found. The zero ring, if allowed, causes no problem for this equivalence. |
| DP12 | PASS | The explicit antipode completes the displayed Hopf verification. The n=0 convention and the nonzero-ring condition remove the previously noted boundary ambiguities. All identities were reread, including the nonordinary-derivation example. |
| DP13 | PASS | The mapping spaces are now expressly derived, and their contravariant direction is correct. This remains a checked application of Horel, not a newly reproved reconstruction theorem. |
| DP14 | PASS | The complete coefficient counterexample and precise limitation were reread. |
| DP15 | PASS for the stated proposition | The subset expansion is integral. With complement-ordered target basis, the matrix is J-I. Its determinant is 2; an entry is 1 and a 2-by-2 minor is -1, so the Smith invariants are 1,1,2 and the cokernel is Z/2. To make the title's implication for the full Lefschetz map explicit, the reviewer recommended adding that this is a direct block: no exterior basis monomial outside the paired source span can contribute to a target made of two complete pairs. The stated restricted-map proposition is already proved. |
| DP16 | PASS | Conditional on the generating formula and chi nonzero as in the supplied source, the binomial coefficient is exactly the displayed rational expression. Quadratic, cubic and general recorded denominators are each missing one factor chi. The final weaker integrality consequence is explicitly excluded from forced-correction claims. No integral Chow or K-theory formula is being asserted. |

### Remaining editorial items at the 00:10:09 UTC snapshot

1. The root had announced that it would explicitly add the smooth proper X/k hypotheses to the crystalline comparison paragraph; this phrase was not yet present in the reviewed snapshot. The review approves that comparison only with its proper hypotheses.
2. The optional direct-block sentence in DP15 would connect the checked restricted-map calculation to failure of the full integral Lefschetz map transparently.
3. The extraneous comma in the exponent of the multiplicative-product notation was still present in DP8 and its later recap. This is typesetting, not a proof defect.

No proof of an external reconstruction/comparison theorem, no computer proof, and no Lean verification was performed in these paper-review events. The proofs reviewed from the root file have no remaining mathematical objection within the stated scope and cited inputs; the three points just listed are tracked to prevent unobserved edits from being called verified.

## Review amendment ABA-CE13

At 2026-11-21 00:17:49 UTC, the exact-line check for `TRANSCRIPTION_NOTES.tsv` refined the historical shorthand in ABA-PR01's final exclusion note. The unsigned expression in cote47 scan009 line48 is `(-1)^k chi c_k`, not literally `chi c_k` for odd k. Its integrality consequence is unchanged, so it remains excluded from the forced corrections. The root was notified to write “up to sign, chi times the kth Chern class.” Earlier event records are preserved above as the actual review history. The current research report and exclusion note give the precise formula.
