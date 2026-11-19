# C.3az: smooth exceptional divisor in positive characteristic

## Status and exact scope

The final complete proof is in `C3_smooth_exceptional_top.tex`. Root and real_weil independently read the complete proof and exact primary inputs and passed it; real_weil completed at 11:38:43.203963 UTC, and both receipts were present at the 11:39:52 UTC tool-clock reading. The canonical result row is now registered. The hypotheses are an algebraizable strictly henselian normal local ring of characteristic p, a regular projective modification that is an isomorphism on the puncture, a single smooth connected exceptional Cartier divisor E, and ample conormal L. The result applies in every positive characteristic and every dimension d+1 >= 2. No cone retraction is assumed.

The conclusion is stronger than the ordinary-quotient vanishing alone: refined restriction gives CH^d(Z)_Q ≅ CH_0(E)_Q; Chow localization then gives CH^d(X)_Q ≅ CH_0(E)_Q/(c1(L) CH_1(E)_Q). The ordinary quotient on Z is Q by restricted degree, and that on the puncture X vanishes.

## New step, with the uniform exponent made explicit

The previously audited KST/GH argument supplies injectivity, without any retraction. The new argument constructs actual families. Through any two points of E, successive ample sections cut a smooth projective curve C, and lifted sections cut a regular projective surface W. Properness over a local base forces global regularity once regularity is known along the closed fibre.

For every proper smooth parameter curve P and line bundle F on C×P, the obstruction at the nth infinitesimal step is H²(C×P,L_C^n⊠O_P) = H¹(C,L_C^n)⊗H¹(P,O_P). Choose n0 so that the first factor vanishes for every n>=n0. The finitely many earlier additive obstructions are killed by taking pth tensor powers; after at most n0−1 such operations, the same exponent p^e works over the entire parameter curve and for all later infinitesimal levels. This does not use an unbounded sequence of p-powers.

The ideals defining C and the closed fibre are cofinal. Projective formal existence algebraizes the compatible family over the completed base. Popescu descends that actual line bundle to a smooth algebra over R; henselian smooth lifting supplies a map back to R with the same residue point. Hence the result is a line bundle on the actual fixed product W×P, with precisely F^(p^e) on C×P.

Take P=C and the normalized diagonal line bundle. Proper pushforward of its two fibre Chern classes supplies an ordinary algebraic relation on Z restricting to p^e([x]−[o]). After rationalization every degree-zero class lifts. An exceptional curve has restriction −c1(L)[D] of nonzero degree, which supplies the remaining degree, proves the top Chow isomorphism, and kills the open ordinary quotient.

## Opened primary source ledger

All entries below were actually opened and read on 19 November 2026. The eight new Stacks entries have opened markers in `C3_smooth_exceptional_references.bib`.

- KST, arXiv:1611.08466v4, Theorem A and equivalent exact sequence (1.6), author pp. 2–3. The full noetherian abstract-blowup scope was freshly checked during the 11:21:27 C3ax audit. No characteristic-zero hypothesis is imported.
- Geisser–Hesselholt 2011, published Theorem A, p. 29: nil-relative nonconnective K groups in every integer degree are p-primary bounded torsion. Fresh source audit recorded in C3ax review.
- Thomason–Trobaugh 1990, Theorem 8.1, printed p. 367: nonconnective Mayer–Vietoris for quasi-compact opens of quasi-separated schemes. Fresh full statement/proof audit recorded in C3ax review.
- Fulton, *Intersection Theory*, Example 15.2.16(b), pp. 294–295: rational total Chern ring isomorphism, natural for pullback. Parent freshly opened this exact page for C3ax; the current proof uses total Chern degree preservation, not an additional Adams assertion.
- Stacks Lemma 30.17.1, tag 01XO: relative Serre vanishing over an affine noetherian base. Ref `turn133200967view0`.
- Stacks Lemma 45.8.3, tag 0FH7, proof: sufficiently ample successive smooth connected sections through two prescribed points, including positive characteristic. Ref `turn209377135view4`.
- Stacks Lemma 37.4.1, tag 0C6R: square-zero Picard obstruction sequence. Ref `turn209377135view0`. It is applied to each successive square-zero step, not to a higher-order ideal in one step.
- Stacks Lemma 30.24.3, tag 0885: projective formal existence. Ref `turn541833485view0`. Lemma 30.24.1 alone gives only full faithfulness and is not substituted for existence.
- Stacks Theorem 16.12.1, tag 07GC: Popescu. Ref `turn209377135view1`.
- Stacks Lemma 32.10.3(2), tag 0B8W: descent of actual invertible modules under filtered affine-transition limits. Full proof read, ref `turn133200967view1`.
- Stacks Lemma 15.13.3, tag 0H74: smooth algebra maps lift over a henselian pair. Ref `turn209377135view2`.
- Stacks Lemma 15.51.14, tag 0AH2: completion of a G-ring is regular. Full statement and proof read, ref `turn262661384view0`. The current HTML numbering is 15.51.14; an older downloaded Stacks book labels the same stable tag 15.50.14, so we cite the current HTML numbering and tag.

## Verification and limits

The first standalone LuaLaTeX/BibTeX build completed with return code zero, four pages, 160,467 bytes, in 2.925814209 seconds, without warnings or box errors. The final build, including the completion citation, started 11:43:55.275776 UTC, took 3.365656671 seconds, and produced five pages, 160,725 bytes, with return code zero and no warnings or box errors. There is no finite numerical test that substitutes for this proof; no artificial test is included.

The SNC extension is still unproved. In particular, K_0(E)_Q for a singular reduced exceptional fibre can contain gluing terms that are absent for smooth E, and this proof does not identify them with ordinary relations. A separate dual-complex/K_1 investigation is pending. No claim about arbitrary isolated singularities or characteristic-zero lifting is made.

## Focused literature comparison; no priority claim

At 11:38 UTC we searched the exact themes “Chow group punctured local singularity smooth exceptional divisor positive characteristic algebraic equivalence zero cycles” and “positive characteristic exceptional divisor Chow group henselian rational zero cycles ample conormal,” alongside the SNC exceptional-divisor construction. We opened Kollár, *Specialization of Zero Cycles*, arXiv:math/0205148v1, Theorem 2, author p. 2: that result concerns smooth proper families over a henselian local Dedekind base with separably rationally connected special fibre. It does not directly assert C.3az, whose base has dimension d+1, whose proper morphism is a resolution, and whose smooth exceptional fibre need not be rationally connected. We also opened Binda–Krishna, *Zero-cycle groups on algebraic varieties*, JEP9(2022),281–325, DOI10.5802/jep.183, the primary publisher abstract and bibliography: its comparison of singular zero-cycle and modulus groups is relevant context, not an exact source identified for this statement. No full theorem audit of that second article is claimed.

No exact existing theorem with the whole stated C.3az scope was located in this focused check. That is a search outcome only, not evidence of originality or a priority claim. The paper should present the complete derived proof and its actual cited inputs without claiming novelty.
