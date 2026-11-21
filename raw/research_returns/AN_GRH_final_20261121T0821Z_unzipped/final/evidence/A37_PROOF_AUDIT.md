# A37: ordinary RM5 finite-support avoidance

- Date: 2026-11-21 UTC.
- Author/checker: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.
- Complete first-draft source: `A37_RM5_FINITE_SUPPORT_AVOIDANCE.tex`.
- SHA-256: `68f88b13eb8057d92ee3ec186596a19b7e6dc193c233075129131efb85c88c20`.
- Status: complete source written and self-reviewed. `/root/gt_certificates` independently whole-read this exact source and reported **PASS**, with no corrections. Root's independent review is pending at the time of this update.
- Formal verification: false.

The independent review is retained at
`work/gt_certificates/positive_rank_theta/A37_WHOLE_PROOF_REVIEW.md`,
SHA-256 `f30033e248e662acf8348513b57fd60a238d7a05c209764d1ebf5c568c1e32bf`.
That checker also reopened all four primary moduli/Torelli inputs and
independently whole-read the A13 integral-RM supplement. Its events
remain in that checker's own fragment rather than being relabelled as
new checks performed by this agent.

## Exact source inputs checked

1. **Yu, Theorem 1.1 and immediately preceding moduli definition.** Read the entire definition on author-manuscript p.1, the entire statement on p.2, and the separate level-torsor/monodromy setup and proof of Lemma 6.1 in Section 6.1, pp.18–19. The theorem allows every level `n >= 3` prime to the residue characteristic; it does not exclude primes dividing the totally real discriminant. The monodromy group is the automorphism group of the integral polarization lattice. The theorem is attributed to Rapoport and Deligne–Pappas. A37 uses Theorem 1.1 directly at the composite level `hn`, rather than deducing independence from separate prime-adic images.

   Primary URL: <https://arxiv.org/pdf/0807.0516>. Web refs `turn132426867view1`, `turn923603145view2`. Local retained PDF/text: `rm5_sources/yu2008.pdf`, `rm5_sources/yu2008.txt`. PDF SHA-256 `56f8b34c8f8e54331ed43e86354949fba19c16397665f19074aaee2ce492ab21`.

2. **Deligne–Pappas, Theorem 2.2 and Sections 2.4–2.6, 2.11–2.13.** Read the actual statements and surrounding definitions on printed pp.64–67. Theorem 2.2 gives smoothness away from the level and the field discriminant. Section 2.6 identifies polarization module `L=O` with an O-linear principal polarization. Sections 2.11–2.13 supply the inverse-different-valued perfect alternating pairing on finite torsion. This is the reason the group at the ramified level 5 is still `SL_2(O/5^a)`; an uncorrected trace pairing on O would be insufficient. Section 2.4 also describes geometric irreducibility over the finite étale Stein base. The proof of the entire Deligne–Pappas paper was not rechecked or reproduced.

   Primary URL: <https://numdam.org/item/CM_1994__90_1_59_0.pdf>. Web refs `turn893744158view0`, `turn319420949view0`. Local PDF SHA-256 `bc795da7fcc57b4b5fd2257bc22fc2187c98bf70eaeb1f7efddc92f4af58c2d5`.

3. **Landesman, Theorem 1.2, genus-two assertion over Spec Z.** Read the complete theorem and the entire Section 6 proof, including the representability/isotropy point, and the relevant genus-two tangent-space assertion. The theorem explicitly states that `phi_2` is an immersion over Spec Z; the characteristic-two failure in higher genus is not applicable to genus two. The whole 25-page paper was not independently reproved.

   Primary URL: <https://arxiv.org/pdf/1911.02084>. Web refs `turn194255619view0`, `turn132426867view0`. Local PDF SHA-256 `6d9e57cadb23a9311e376ce05a9705c2086f169fdffcb1607bfabc1bca186cef`. The author's bibliography independently confirms Trans. AMS Ser. B 8 (2021), 354–378: `turn536859037view1`.

4. **Cléry–van der Geer, Section 4, printed p.5211.** Read the published primary PDF's statement that, over characteristic two, the Torelli image is the open complement of the product locus `A_1,1`, together with the preceding characteristic-two moduli-stack setup. Together with the immersion and the reduced HB base, this identifies the fibre product with the actual open subscheme, hence gives a universal curve before any arithmetic specialization.

   Primary published URL: <https://pure.uva.nl/ws/files/76013670/Modular_Forms_of_Degree_2_and_Curves_of_Genus_2_in_Characteristic_2.pdf>. Web refs `turn963537857view2`, `turn179827973view2`. The web tool displayed the PDF and required passage. A separate attempted local download returned HTTP 403; no local PDF is claimed. DOI `10.1093/imrn/rnaa239`.

5. **Existing checked deductions reused.** A13/A33 supplement supplies an actual ordinary RM5 Jacobian and was independently whole-read at the hash below. A19 supplies the geometric genus-two translate-intersection bound and the fixed-support rationality lemma. A22 supplies the already checked relative-Raynaud-theta incidence construction, affine descent twist, and Lang–Weil specialization argument. A37 repeats the relevant specialization details to make the exact field and modified O-linear matrix reviewable.

## New proof checks

- **Nonempty open and curve descent.** The auxiliary full-level HB scheme is geometrically irreducible and smooth because characteristic 2 is unramified in Q(sqrt5). The ordinary Jacobian open is nonempty at the explicit A13 RM point. The universal curve exists on this open, not merely after a finite extension at a specialized point.
- **Joint levels.** Choosing auxiliary h coprime to n makes `H_hn -> H_h` a full finite level-n torsor. Its source remains irreducible on every nonempty base open. Thus the generic geometric image is the whole finite product group, including simultaneous levels and the ramified prime 5.
- **Pairing.** The inverse-different trace form is unimodular over Z. Its reduction remains perfect at every odd level. O-linear preservation of the rank-two alternating form is exactly determinant one. The relative Frobenius map is an O-linear symplectic similitude of multiplier two, so it preserves this monodromy conclusion on the Frobenius-twisted Jacobian.
- **Local orbits.** In each local factor, a nonzero vector is sent to `pi^v e1`. The lower unipotent matrices with entries `j*pi^(a-1-v)` produce the full order-ell translation cycle by `T=pi^(a-1)e2`. All other local coordinates stay fixed. This works when O/5^a is nonreduced, and does not assume transitivity on all nonzero vectors.
- **Theta contradiction.** Galois stability puts the cycle in theta. Because the full cycle is invariant under translation by T, its at least three points belong to both theta and theta+T, contradicting the genus-two intersection bound 2.
- **Auxiliary-level quantifiers.** A new auxiliary h may be chosen for each odd n. Absence of a geometric torsion point is unchanged on a finite level cover, so this proves a property of the geometric generic RM curve. No common finite-type open excluding infinitely many levels is asserted.
- **Arithmetic specialization.** Over a sufficiently large finite constant field containing the required roots of unity, the full level-N^2 torsor is geometrically integral. The chosen matrix is O-linear `diag(1+ell,(1+ell)^(-1))`, including at 5. Its underlying rank-four matrix is I modulo ell, and its quotient by ell after subtracting I is invertible modulo ell.
- **Exact field.** The affine twist by this matrix has points over all sufficiently large constant extensions; choosing the degree 1 modulo N realizes the desired matrix. The existing universal curve specializes over that exact field, so no later field extension can alter the prescribed rational Sylow groups.
- **All powers/products.** `Phi-I=ell*A_ell` with A_ell invertible gives precisely `J(F_Q)[ell^infty]=J[ell]`. A19 with d=1 places every geometric S-primary theta point in that rational group; the finite N-torsion avoidance open excludes its nonzero elements.
- **Limits.** The argument is unconditional and existential. It does not claim an effective field bound, an explicit avoiding curve, or absence of variable-prime witnesses on each fixed curve.

## Alternative considered but not used

A torsor of rigidified line bundles representing the principal polarization would have geometrically connected abelian fibres and a universal theta divisor; its smooth-divisor open could also produce a curve family without a finite curve-descent extension. Deligne–Pappas Sections 1.1–1.4 support the Picard construction. Once the exact characteristic-two genus-two Torelli result was located, the shorter cited open-immersion route was used instead. No unproved Picard-torsor or theta-to-Jacobian step is a premise of A37.

## Narrow independent review: the A13 integral RM5 supplement

- Source: `work/row_audit/A33_SUPPLEMENT_A13_RM5.tex`.
- SHA-256: `87a2edb3d9a51b8018b3c04af15682d40fe5eb5d9ddaae45b7ae3f08f811f3f1`.
- Entire source read; outcome **PASS**.
- The argument splits the full finite group scheme A[2] over the perfect field F2, uses Cartier self-duality to identify its connected factor with mu_2^2, and checks Frobenius plus Verschiebung is identity on both factors. The quotient property of [2] therefore gives an integral endomorphism, not merely a rational or étale-Tate-module one.
- The polynomial and Rosati calculations yield `T^2+T-1=0` and `T^dagger=T`. The resulting O5 action is injective.
- The concluding pure-two-primary theta argument uses the exact Frobenius relation, invertibility on the étale Tate module, A35, and the three rational Weierstrass points. The canonical class of a non-Weierstrass point indeed has a nonzero odd-primary component, since it is minus twice its translated Abel class.
- This was a mathematical whole-proof read, not a new implementation or independent rerun of the existing A13 point-count certificate.
