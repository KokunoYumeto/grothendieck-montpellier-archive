# Fermat sections: proofs and verification records

This workbench studies Grothendieck's question about sections of the arithmetic fundamental group of Fermat curves. The main paper gives the full-group Selmer theorem and separates the deduction about all sections from its local input. A companion studies solvable and pro-3 quotients.

The papers are self-contained mathematical arguments. Published inputs are cited with exact statements. This directory contains only original text, calculations and verification records; external sources and input attachments are not redistributed.

## Research stopping decision and completion status

Mathematical research stopped at formal review13 on 25 November 2026 at 17:02:49 UTC after two consecutive reviews without main-gate movement. Paper writing and verification are complete; the current step is packaging and delivery. The open mathematical questions below are retained. All twenty current principal companion statements have complete direct or assembled same-model statement-only coverage with exact exposure qualifications. The additional class-three result FQ.284 also has a frozen exact independent reconstruction and root whole comparison, completed at17:14:03UTC. No human or formal proof-assistant verification is claimed.

Both standalone editable source identities are frozen and verified. The final16-page main PDF and169-page companion PDF have complete page coverage and whole expert/newcomer readthrough acceptance. The exact final PDF/source hashes and the actual-view/unchanged-bitmap evidence are recorded in the final QA receipts; no earlier pre-identity review is silently promoted to a final-PDF review. The main receipt is `records/root_main_final_visual_identity_pass.json`; the companion receipts are `records/root_companion_final_visual_identity_pass.json` and `records/root_companion_final_whole_read_pass.json`.

## Reading order

1. `papers/fermat/main.pdf` and its editable LaTeX project.
2. `papers/quotients/main.pdf` and its editable LaTeX project.
3. `QUESTIONS.tsv`, `STATEMENTS.tsv`, and `CHECK_EVENTS.tsv` for the precise mathematical and verification status.
4. `checks/` for independent calculations and expected output.

This is an unfiled workbench edition. The custodian assigns the WB number and permanent record page. Local statement tags remain stable; no number in the central registry is claimed.

Canonical proposed repository: https://github.com/KokunoYumeto/k-theory-and-galois-groups-workbench
Permanent record registry: https://github.com/KokunoYumeto/mathematics-workbenches

## Reuse

Original mathematics, text and code are dedicated to the public domain under CC0 1.0. Citations identify third-party works; their copyright is unaffected. No human verification has been performed or claimed. See each paper's method note for the precise model-checking provenance.

## Mathematical state

The main theorem proves that for every odd n>=3, the full profinite point-or-cusp Selmer sections of the affine Fermat curve are exactly its three rational cusp packets, each parametrized by the full completed Kummer group H1(Q,Zhat(1)). The corollary about all full sections remains conditional on the explicitly unrefereed proper p-adic input, together with the established real theorem; it is not asserted unconditionally. The positive-genus Y1(N) and even-exponent results are proved separately.

The finite-derived, metabelian and maximal geometrically prosolvable Selmer theorem holds for every odd exponent divisible by 3, 5, or any regular prime greater than 5. The first prime not classified by this range is 37. The three rational cusp packets are disjoint and each is parametrized by H1(Q,Zhat(1)); the proof permits infinitely supported completed Kummer parameters and does not assume a full global lift of an unknown quotient section.

For every regular prime p>5 and every n=p^r with r>=1, the full geometrically pro-p group, every finite-derived quotient, every stated ordinary lower-central quotient, and every stable quotient retaining abelianization with torsion-free ordinary lower-central factors have the corresponding three H1(Q,Zp(1)) cusp packets. The separate arithmetic-source theorem gives whole nonabelian localization and integral compact localization for every odd regular prime. The fixed pro-17 fibre inside the prosolvable section set is now classified: its Selmer subset is exactly the torsor of cusp parameters at coefficient primes other than 17, not the entire relative nonabelian H1 set.

The pro-3 range is unchanged: n=3^r, 5*3^r, or 7*3^r with r>=1. The full group and the same finite-derived, ordinary-central and stated torsion-free-grade quotients are covered. Compact base-five/seven pro-3 images and compact localization at exponent eleven are additional proper-curve results, not new affine pro-3 classifications.

For p>=5 with cyclotomic class rank r<(p+3)/8, one fixed set of at most p local points contains every compact Tp datum with curve-valued witnesses at all finite places. At 37, 59 and 67 the set lies in the three cusp residue discs; equality with the three cusps is not proved. At odd n=pm, the fixed-set bound is (p-3)d^2+3d, where d=gcd(m,p-1). The first-case relative-rank and odd-character congruences are proved separately in the proper mod-p abelian quotient. The prescribed supported-tower condition needed for further irregular cusp-disc isolation is explicit and remains unproved in those cases.

The separate Jacobian arithmetic results remain part of the paper. They include the complete quintic, septic, eleven and nineteen analytic/arithmetic certificates, finite full Sha for the exponent-eleven Jacobian and the rank-zero nineteen complement, and the split-prime rational Selmer theorem for the classical thirteen Prym. No finite whole Sha theorem is asserted for that Prym. Their section consequences at regular exponents are subsumed by the new cyclotomic argument, while their proper-curve and arithmetic conclusions remain independent.

For every odd n>=5, a hypothetical noncuspidal prosolvable Selmer section has individually and jointly open two-adic and three-adic Frey images, with common integral pure Frobenius polynomials on a Dirichlet-density-one set. A stable cyclic subgroup modulo nine instead implies cuspidality. These reductions do not establish finite ramification and do not automatically apply to sections given only in a metabelian quotient.

At seventeen every simple factor of the Fermat Jacobian has positive rational rank, so the rank-zero-target method fails there. The regular-prime section argument nevertheless classifies all odd multiples of seventeen. Similarly, the separate rank/Sha questions about the complementary tenfold at thirty-one remain arithmetic questions; the section classification at thirty-one is already proved.

Producing proofs, exposed whole comparisons, and separate same-model statement-only reconstructions are recorded separately in CHECK_EVENTS.tsv and the principal-statement coverage matrix. Targets22,23,24,25 and the higher-exponent addendum have preserved completed proofs and source audits. Target21 is one continued recovery reconstruction with declared earlier proof memory; it is not a second independent worker and does not restore lost original bytes. Target19's continued reconstruction passed whole comparison for its original arithmetic, primary and whole-fibre claims. Its kernel claim proves the whole-fibre bijection; the later Target21/all-regular argument supplies the classified Selmer subset.

The complete current FQ.005 and FQ.009 statements were separately reconstructed by a fresh no-history worker and frozen before proposed-proof exposure. Root's whole proof, source and identity comparison passed on 25 November 2026 at 16:31:48 UTC. This covers every stated exponent, quotient, ramification set, and both noncuspidal families; the earlier partial-check qualifications remain in the historical records. Target26 checks the earlier quintic/septic finite-field theorem only. The separate exact Target27 reconstruction of the stronger general theorem, including the 3-divisible clause, is frozen and whole-compared: root receipt `root_finitefield_general_complete_comparison_pass.json`, 16:50:12 UTC. Its prior exact A/B and SGA1 exposure and initial-inventory timing are disclosed; no producing-proof exposure preceded its freeze. Recovery and further checking are not counted as mathematical movement. No human has checked this work.

## Finite-field coordinate-boundary fibres

For every n>=3 over k=F_Q of characteristic prime to 3n, the full proper geometrically pro-3 point-section map separates rational points on different coordinate-boundary components. The full arithmetic group G_k is retained and conjugacy is by the geometric kernel. If the rational boundary is nonempty and d=gcd(n,Q-1), each component has d points. There is one divisor h of d, with 3 not dividing h, such that every boundary fibre is a coset of mu_h(k) in the regular mu_d(k)-action. There are exactly 3d/h boundary section classes. If 3 divides n, h=1, so the boundary map is injective over every allowed finite field.

For every prime exponent a>=5, the nonsplit case Q not congruent to 1 modulo a has three distinct boundary classes. In the split case either all 3a classes are distinct or each whole coordinate component is one fibre. For odd n prime to 3, the specified sufficient injectivity primes q with gcd(n,q-1)=1 have natural density product over p dividing n of (p-2)/(p-1), including 3/4 at n=5 and 5/6 at n=7. For 3 dividing n, all good primes give injectivity. The density is that of a stated sufficient set, not a claim that it equals the density of every injectivity prime.

Every fibre in this assertion is intersected with the coordinate boundary. No claim excludes an ordinary proper point from the full fibre of a boundary point, and no new affine pro-3 exponent is classified. The exact coordinate-divisor order is proved in every characteristic not dividing n. Pál's theorem is used only for C3 with 3 retained, never for S3 with only 3 retained. Target26 independently checked the earlier a=5,7 theorem with its declared related-work exposure. The separate exact current-theorem Target27 froze on 25 November 2026 at 16:46:56 UTC; root completed the whole proof, source/exposure audit, 23-entry manifest and exact-code comparison at 16:50:12 UTC. It covers the full general theorem, including the 3-divisible clause and exact divisor order. Earlier exact A/B and SGA1 exposure, and the initial inventory following a disclosed short interval of internal reasoning, remain explicitly qualified.

## Records and reproducibility

Every numbered theorem, lemma, proposition, corollary, definition, hypothesis, and remark appears in the statement inventory. Check events distinguish unexposed same-model re-proofs, post-exposure comparisons, certified computations, and published background inputs. The source table gives exact statements, pages, addresses, and reading limitations; the source-hash table fingerprints excluded external artifacts.

Each paper has its own `BUILD.md`, deposit sheet, editable sources, and PDF. The mathematical certificate commands and expected bounds are in those build files and the original check records. `FORMAT_PREPARATION.md` explains stable local tags, registry allocation, the supplied filing utility, validation, and the manifest protocol. No central WB number is fabricated.


Long exact numerical witness records are stored in line-aligned parts below the format-1 per-file limit, with complete SHA-256 reconstruction manifests. To reconstruct all original long records in a separate working folder, run `python3 tools/reassemble_records.py /tmp/fermat-record-replay`. The helper verifies every chunk and the reconstructed files. Each final paper also includes its own standalone certificate inputs and commands.

The separately frozen statement-only septic proof is also reproducible directly from its text inputs: `python3 records/fresh_checks_target15_rerun.py --gp /absolute/path/to/gp`. It requires PARI/GP and python-flint, creates isolated temporary copies, verifies 590 principal witnesses and two ideal-class relations, checks complete coverage of the 592 bounded prime ideals, and proves the strict root-discriminant contradiction. Expected output is `all_assertions: PASS` and `preserved_inputs_unchanged: true`. Its full proof, exposure record, input hashes, independent code, root replay and whole-proof comparisons are preserved separately.

## The remaining arithmetic question at thirty-seven

For the cyclic quotient C: y^37=x(1-x)^10, its Jacobian is rationally isogenous to a sixfold A and a twelvefold P. The factors are rationally simple, End_Q^0(A)=Q and End_Q^0(P)=Q(zeta_3); A has positive rational rank, the rank of P is even, and P(Q)_tors is cyclic of order 37. Their conductors are 37^12 and 37^24; the root numbers are -1 and +1. The complementary representation uses a Dirichlet character of order nine, whose relevant Hilbert twists have nontrivial cubic central characters over a real sextic field.

These are structural and applicability results. Neither L(P,1) nonvanishing, rank P(Q)=0, whole-Sha finiteness, nor the split-prime Tate-Sha hypothesis is proved. The sixfold's positive rank prevents it from being a rank-zero target. The twelvefold is the only possible positive-dimensional rational rank-zero factor within this cyclic quotient, but its required arithmetic remains open. The exact program verifies finite structural arithmetic only. The all-prime exponent-37 classification and all remaining affine pro-3 gates are unchanged.

The finite-depth limitation FQ.284 shows that the entire proper quintic point map becomes constant through nilpotency class three at a specified density1/10 set of primes, including11. It does not prove a collision in the full pro-three group or classify another affine exponent. Its complete proof and exact standard-library Python certificate are in the companion project.

The independent class-three reconstruction froze17:10:01UTC before producing-proof exposure and passed root whole proof/source/code comparison17:14:03UTC. Its earlier exact A/B and Target27 exposure is disclosed. The diagonal-twist obstruction and the nonzero geometric diagonal-centralizer quotient are separately proved in FQ.285/FQ.286; neither supplies arithmetic compatibility or settles the remaining full same-component fibre.
