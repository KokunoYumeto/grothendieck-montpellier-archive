# A19/A37 inputs to KT-RM-FROB-AVOID

This note distinguishes a proved negative theorem from a failed positive forcing proposal. The parent requested this clarification on2026-11-21. Reviewer: `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed, KTOWER.

## Exact proof locations

Under `input/RETURN_AN_GRH_final_20261121T0821Z/`:

- `final/proof_sources/finite_support_theta.tex` is A19. The integrated statement and full core proof are in `AN_GRH.tex2934–3124`, equationsFS.1–FS.10.
- `final/proof_sources/rm5_finite_support_avoidance.tex` is A37. The integrated statement and full six-step proof are in `AN_GRH.tex7219–7506`, equationsRM.1–RM.15.

I read those entire integrated proofs again during the current follow-up. The new draft uses A19's rationality result and A37's ordinary HB family, full joint odd-level monodromy, fixed-level generic avoidance, and twisting construction.

## A19 hypotheses and actual theta

A19 applies to every genus-two curve C/F_Q in characteristic2 and every finite set of **odd** primes S, including3 and5. It sets X=C^(1), J=Pic0(X), and Theta=i_B(X), where B is the actual degree-one locally exact differential line bundle. B itself and this Abel translate are defined over F_Q; no rational effective divisor for B is required. Thus Theta is stable under every positive power of Q-Frobenius.

If Phi^d fixes every J[ell] for ell inS, all geometric S-primary theta points lie in J(F_(Q^d)). The proof is elementary and self-contained:

1. A nonzero translate intersects a genus-two Abel curve in at most2 geometric points, by the degree-two Riemann–Roch argument.
2. For U=1+M, M divisible by oddell, the higher terms in (U^(ell^(s−1))−1)v vanish when (U−1)v has orderell^s. The bound j−2−v_ell(j)>=0 is valid even in the tight caseell=3,j=3.
3. Congruence-kernel orbits of ell-primary torsion have ell-power order. Raising a Frobenius power to the product of all other primary orbit lengths isolates one moved component. The powering lemma gives a nonzero ell-torsion translation T fixed by that Frobenius power.
4. Frobenius stability puts the entire ell-point translation cycle on Theta and Theta+T, contradicting2. This handles arbitrary exponents and products, with no semisimplicity hypothesis.

The unavailable original Boxall chapter is explicitly **not a premise**.

Original full-proof provenance is retained in `final/evidence/A19_PROOF_AUDIT.md` and `A19_A20_independent_audit.md`, and `final/CHECK_EVENTS.tsv27–28,422,470–472`: author, old root and effective_galois whole-proof passes, including the borderline prime3 check. These are original reported checks, distinct from my fresh complete read.

## A37 status

A37 is a complete **negative finite-support avoidance theorem**. Its conclusion defeats the attempted positive strategy that a fixed finite prime support could force an odd theta witness on every ordinary O5 curve. The label 'failed constructions A36–A44' does not turn A37's proved negative component facts into conjectures.

The original full six-step proof has author source SHA256 `68f88b13eb8057d92ee3ec186596a19b7e6dc193c233075129131efb85c88c20`. Its producer report is `final/evidence/A37_PROOF_AUDIT.md`; its independent entire-proof report is `final/evidence/A37_WHOLE_PROOF_REVIEW_GT.md`. Both entire reports were read in this run. The producer report says the old root review was pending at that snapshot, so I do not relabel it as an old root pass. The independent gt_certificates pass is explicit and recorded at `final/CHECK_EVENTS.tsv528`; primary input events are107–110.

## Published moduli inputs carried with exact original scope

These are the statements checked by the original A37 reviewers. I have not claimed a new complete proof of the published papers in this interval.

- **Yu**, arXiv0807.0516, Theorem1.1 and full moduli definition on manuscriptpp1–2: full leveln>=3 prime to the residue characteristic; no exclusion of primes dividing discriminant5. Original reviewers also read§6.1 and the complete short Lemma6.1 proof, pp18–19. A37 applies irreducibility directly at the joint composite levelhn, rather than inferring independence from separate prime-adic images. URL:https://arxiv.org/pdf/0807.0516 .
- **Deligne–Pappas**, Theorem2.2 and§§2.4–2.6,2.11–2.13, printedpp64–67: smoothness away from level and field discriminant; polarization moduleO gives the O-linear principal polarization; the inverse-different-valued alternating pairing is perfect at every odd level, including5. Original reviewers read these statements and definitions, not the whole proof of the paper. URL:https://numdam.org/item/CM_1994__90_1_59_0.pdf .
- **Landesman**, arXiv1911.02084, Theorem1.2 and entire§6 proof: genus-two Torelli is an immersion overSpecZ, including characteristic2. URL:https://arxiv.org/pdf/1911.02084 .
- **Cléry–van der Geer**,§4, printedp5211, DOI10.1093/imrn/rnaa239: in characteristic2 the Torelli image is the open complement of the product locus. Together with the immersion and the reduced smooth HB base this gives the actual universal curve on the open before specialization. URL:https://pure.uva.nl/ws/files/76013670/Modular_Forms_of_Degree_2_and_Curves_of_Genus_2_in_Characteristic_2.pdf .
- The ordinary open is nonempty at the actual A13 Jacobian with its integral Rosati O5 action, whose A33 supplement is separately proved and checked in the archive.
- **Stacks0245**, effective affine descent, and **Poonen**, Theorem7.7.1(ii)–(iii), printedp222, supply the exact finite-field torsor twist and eventual points in every large extension degree; these are the already checked A22 inputs reused in A37.

## Joint monodromy and Raynaud compatibility

The cover H_hn→H_h is the full O-linear symplectic n-frame torsor, with groupSL2(O/n). Both level schemes are geometrically irreducible, and restricting to a nonempty ordinary Jacobian open preserves irreducibility of the source. This proves full joint monodromy. The inverse different is essential at5. Relative Frobenius identifies the odd torsion of the original and Frobenius-twisted Jacobians by an O-linear symplectic similitude of multiplier2, preserving the determinant-one group.

The relative sequence O_X→F_*O_C→B constructs the actual Raynaud line bundle throughout the family. Its proper translated Abel image has closed fixed-n torsion incidence. Generic monodromy orbits contain odd translation cycles, so the incidence misses the generic point. Hence the required finite avoidance open is genuinely nonempty.
