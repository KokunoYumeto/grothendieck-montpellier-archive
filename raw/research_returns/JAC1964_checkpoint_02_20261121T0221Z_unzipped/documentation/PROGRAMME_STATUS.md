# Independent programme audit

Run: JAC1964-20261121. Agent: /root/programme_audit, GPT-6 Astra Pro. The effort setting is not exposed. The historical manuscript images were not provided: the archive audit concerns supplied TeX transcriptions and mathematical consistency, not palaeographic verification.

## Interpretation and status of cote 44

| Claim | Precise interpretation | Status reached in this run |
|---|---|---|
| Th.1 | Kernel of a family map into the quotient by Albanese/incidence equivalence, as a set of geometric points. | The incidence reading is realized by Saito's construction. The supplied page does not independently define every symbol; no stronger identification with a universal regular representative is made. |
| Th.2 | Dimension at most one half of the odd Betti number. | Cited background for all smooth projective varieties over algebraically closed fields, all characteristics: Saito Prop.3.4, pp109–110. |
| Th.3 | Higher Picard variety of algebraically trivial cycles modulo incidence equivalence; complementary indices are p and dim(X)+1−p. | Cited background, all characteristics: Saito Th.3.6 and Prop.4.4. Canonical duality is an isogeny; integral principal duality is not asserted. |
| Th.4 | Signed incidence form on the primitive middle higher Picard summand, for dim(X)=2m−1. | Root's JAC-T4.1–3 independently whole-read and checked. Under supplied 032 Cor.8.4 this gives a rational polarization for abelian X in every characteristic. The literal unqualified assertion on the full higher Picard variety fails: JAC-P03 gives an explicit E^3 calculation. General positive-characteristic X is not covered by the abelian Hodge-standard input. |
| Th.5 | Restricted cycles are explicitly algebraically trivial on the generic section; comparison with a Néron–Tate form is proposed. | The literal uncorrected formula fails even for a quadric pencil with geometrically integral fibres and rationally trivial restrictions (H9-C1, independently checked). H9 also enlarges the domain to homologically trivial restrictions; JAC-P04 gives an explicit abelian-fourfold obstruction. Admissible extensions, local correction terms, and an actual height comparison are distinct requirements. |
| Th.6 | Isogeny for 2p≤n−1; fixed factor equals ambient image in 2p=n; surjectivity for 2p≥n+1. | JAC-P02 proves the rational statements under algebraicity of the normalized lowering operator of X, hence for abelian X in every characteristic. The deleted finite-kernel critical clause also follows. The fixed-part clause is proved by spreading the cycle and using the blow-up formula, rather than inferring algebraicity from invariant cohomology. JAC-P00 treats the imperfect function field and norm multiplicities. |
| Th.7 | With customary tau equivalence: a nonzero multiple is algebraically equivalent to zero. | False even for a CM abelian threefold over a number field: Fermat-quartic Jacobian, Bloch Th.4.1 p104 and Lemma3.1 p99. JAC-P05 gives the numerical-versus-tau deduction. For divisors it is true in every characteristic (SGA6 XIII4.6). For zero-cycles on a connected smooth projective variety, degree-zero cycles are algebraically trivial, so the statement also holds. Thus the failure starts in intermediate codimension. |

Th.7 must not be silently read as numerical equivalence equal to homological equivalence. The supplied page does not define tau. Its customary meaning is the explicit assumption of the refutation. Over the algebraic closure of a finite field, algebraically trivial Chow classes are torsion; JAC-P06 proves this directly using curve families. Hence there the claim would identify rational Chow groups with numerical cycle groups, a conclusion not obtained from the Hodge standard conjecture.

## The new deductions and proof files

`sections.tex` contains JAC-P00–P06. P00 is rational descent, P01 detects incidence maps using their relevant odd cohomology, P02 proves the hyperplane and trace assertions, P03 gives the E^3 sign test, P04 gives an E^4 domain test, P05 refutes customary Th.7 even in CM type, and P06 clarifies the finite-field meaning. P00/P01/P02/P03/P04/P06 are deductions proved in the file; Bloch's non-torsion theorem itself is cited background.

The whole of `work/root/T4_proof.tex` was read independently. The decisive checks were: the primitive projector is self-transpose for Poincaré duality; P01 makes a homological idempotent an actual idempotent in End^0 of the incidence Picard variety; Saito transpose compatibility gives a block-diagonal isogeny and hence nondegeneracy on the primitive block; the mixed family projection preserves the induced map; the product primitive exponent is exactly genus(C); and the diagonal divisor factor is exactly 1/2.

An explicit inverse to the Abel-map pullback is

\[
(g-1)!\,(L_\theta^{g-1})^{-1}a_*:H^1(C)\to H^1(J(C)).
\]

Indeed, projection formula and the Abel-curve class give a_*a^*=L_theta^{g−1}/(g−1)!. The inverse Lefschetz operator is algebraic for the Jacobian. No Hodge conjecture is invoked in this step.

The nef-plus-nondegenerate criterion used by root was checked against Mumford's original printed pp60 and155. The index theorem counts the positive roots of chi(H^t tensor L); the nef polynomial has no such roots. Index zero gives effectiveness, and Application1 on p60 says that an effective line bundle with finite K(L) is ample. The argument applies in every characteristic.

## Independent H9 check

All of `work/h9/H9_results.tex` was read. H9-C1 was recomputed from its cycle construction: the row/column families of the split quadric give the plane identities; the top Chern class gives plane self-intersection (1+(-1)^m)/2; the conic parametrization works over C(t); and refined pullback in the incidence model gives u_infinity=t−e and u_0=−t−e. The exceptional self-intersection is e^2=2(-1)^m, its cross term with t is zero, both local matrices are 4(-1)^m, and each signed correction is +1. The corrected class is exactly zero. H9-T1's Schur-complement argument and H9-T2's specialization/cap-product argument were also checked under their stated hypotheses.

## Current monodromy advance

SGA7 I IX10.4, printed p444, supplies a single integral toric monodromy pairing for all primes and a positive, nondegenerate form for every genuine polarization. IX10.3.5, p443, multiplies it by the positive ramification index. These statements were read in the original scan. The original SGA7II XV3.3.3–3.3.6, pp191–192, fixes the vanishing generator up to sign and gives the exact Picard–Lefschetz coefficient.

The complete proof in `work/h9/H9_monodromy.tex` has now been independently whole-read and passed a targeted check under its explicit hypotheses. Nondegenerate incidence duality and absolute irreducibility make the universal-cycle realization an isomorphism for every ell. Tensor-faithfulness and geometric absolute irreducibility give End^0(B)=Q, so the signed incidence divisor is c times a genuine polarization with one rational c. Rank-one integral monodromy then gives a_ell^2=q0/(e c) for every ell away from the characteristic, with q0>0 rational and e>0 integral. A rational number square at all but finitely many primes is a rational square; the elementary Euler-product proof in H9-L1 checks. Hence c>0. This proves the variable polarization under the stated generic-pencil monodromy hypotheses, and combines with root's fixed primitive result. It does not prove the comparison on H9(b)'s larger homologically trivial domain or claim the same result for every special fibre.


## Checkpoint 02 update (2026-11-21 02:21:37 UTC)
New checked results since checkpoint 01: JAC-T4.4 actual primitive algebraic representative of an abelian threefold; JAC-T4.5 arbitrary-field descent; H9-T6a automatic variable monodromy; JAC-P07 automatic condition A for abelian pencils; H9-T7 full geometric-height decomposition; H9-T8 full semipositivity for abelian fourfold pencils; JAC-P09 geometric-generic degree-at-least-three axes; H9-T9 algebraically trivial incidence height and trace radical; H9-T10 actual algebraic representative of the generic threefold; JAC-P10 exact Fermat Faltings-height difference log(2)/4; AR-11 unconditional positive Fermat L-derivative; AR-12 exact theta reduction; AR-13 independently reviewed IEEE/Arb certificate proving the specified Fermat Ceresa height greater than 1/100. Full positivity on all CH(N) remains unproved. AR-13 is a reproducible numerical certificate under stated arithmetic assumptions, not formal verification. The latest individual proof fragments and per-agent check logs are authoritative for additions not yet integrated into the manuscript. The manuscript assembly will be refreshed immediately after this scheduled checkpoint. No stale compiled PDF is included.
