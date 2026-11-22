# Cote 15 primary-source notes

Research date: 21 November 2026 UTC / 22 November 2026 Europe/Berlin. Agent: GPT-6 Astra Pro, `/root/cote15`. These notes distinguish a cited published theorem, a selected statement/proof passage actually inspected, and a whole-proof check of our deductions. They do not claim independent verification of whole published papers. No Masullo page images or text copies were accessed or copied.

## Archive and inherited inputs

- Physical p94 / footer93 / `input/ARCHIVE_15_scan094.tex`: Q′ and its setting.
- Physical p98 / footer97 / `input/ARCHIVE_15_scan098.tex`: norm discussion.
- Physical p100 / footer99 / `input/ARCHIVE_15_scan100.tex`: boxed purity and conjecture forte.
- Checkpoint 09 `research/consequences_criteria_cross_cycles.tex`: CC-XC03 (semisimple projected Tate equivalence), CC-XC04 (consequences on mixed products). The full arguments were read to check their use. These inherit the all-abelian fullness hypothesis.
- `consequences_criteria_rational_spectral_target.tex`: CC-XC11–12, rational target and simultaneous rational certificate; inherited, no new proof claimed.
- `consequences_criteria_fermat_certificates.tex`: CC-XC08(1) already treats all curves and products. C×C is not newly settled here.
- `consequences_criteria_separated_hypersurfaces.tex`: CC-XC10 already proves the separated-variable join and degree calculation; split cubic fourfolds are an application.
- `consequences_criteria_chow_generation.tex`: CC-XC16 finite extension/induction/restriction-of-scalars/trace argument is in rational Chow motives. Its exact descent formulas were checked as used.
- `consequences_criteria_noncyclic_descent.tex`: CC-AG14, all seven proof parts and the classical corollary read through; index and all-label exclusion checked in full. `root_class_number_descent.tex`: BR-15-CLASSBOUND and BR-15-SLOPEBOUND read through. Supporting script executed successfully; see `cote15_honda_computation.txt`.

## Published sources used for the new deductions

### 1. Tate: Honda–Tate index and isogeny criterion

John Tate, *Classes d’isogénie des variétés abéliennes sur un corps fini (d’après T. Honda)*, Séminaire Bourbaki, exposé 352, talk November 1968, published 1971, pp95–110.

- Primary scan: https://www.numdam.org/article/SB_1968-1969__11__95_0.pdf
- Exact locator: Theorem 1(i)–(ii), equations (1)–(2), Remark 2, printed p96 = PDF physical p3. The page was also inspected as an image because the text extraction drops the formulas.
- It gives occurrence, local division-algebra invariants, dimension, and characteristic polynomial as minimal polynomial to the index power. This is the published input to ARCH-15-HONDA-CHECK. Sign convention is for End of the abelian variety, opposite to the cohomological-motive convention; indices agree.
- Web refs available to parent for navigation: `turn451096804view3`, screenshot `turn258717699view2`.

John Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Invent. Math. 2 (1966), 134–144.

- Primary scan: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf
- DOI: https://doi.org/10.1007/BF01404549
- Main theorem, p134, for homomorphisms; Theorem 1(c), p139 = PDF p6, for equality of Frobenius polynomials iff isogeny. Selected statements and relevant application proof read. Used for the Honda check and the ordinary Tate theorem on C×C.
- Refs: `turn986341345view1`, `turn724643982view3`.

### 2. Published Tate on elliptic products, with the needed scope

Michael Spieß, *Proof of the Tate conjecture for products of elliptic curves over finite fields*, Math. Ann. 314 (1999), 285–290.

- Journal DOI/page: https://link.springer.com/article/10.1007/s002080050295
- Author publication page: https://www.math.uni-bielefeld.de/~mspiess/Preprints.html
- Publication metadata verified. The original full-text PDF could not be retrieved in this run. No theorem number or whole-proof read of this paper is claimed.

J. S. Milne, *The Tate conjecture for certain abelian varieties over finite fields*, Acta Arith. 100 (2001), 135–166.

- Author version: https://www.jmilne.org/math/articles/2001aP.pdf (header: submitted August 1999, minor exposition changes February 2001).
- Exact locator: Appendix A.7, first Example on author p21, text beginning “Let A0 be isogenous to a product of elliptic curves”. It explicitly cites “Spiess 1999, Proposition”, proves P(A0)=L(A0), and concludes that no product of elliptic curves has exotic Tate classes. The selected example was read, as was the introductory explanation p2 relating geometric Tate to finite-field full Tate and pole orders.
- Scope covers **arbitrary finite products, their powers, isogeny factors, finite extensions, and mixed products inside that same elliptic sector**. It is not just the divisor theorem. The descent from geometric classes to invariant classes over a specified finite field uses trace averaging; semisimplicity and duality then give numerical–homological equality. This suffices for both split-cubic and elliptic Kummer target sectors.
- Refs: `turn451096804view2`, `turn258717699view0`.
- The second Example on the same author p21 is the “K3-type” abelian case (unique degree-one slope0 place, conjugate slope1, remaining slopes1/2); reserved for the separate ordinary-target reduction. Its proof and scope were inspected. It does not assert Tate for arbitrary mixtures of unrelated abelian varieties.

### 3. Cubic fourfold semisimplicity and ordinary Tate

Yuri Zarhin, *The Tate conjecture for powers of ordinary cubic fourfolds over finite fields*, J. Number Theory 108 (2004), 44–59, DOI 10.1016/j.jnt.2004.04.006.

- Primary author version: https://arxiv.org/pdf/math/0304014 (v1, 1 April 2003).
- Publication page: https://www.sciencedirect.com/science/article/pii/S0022314X04000848
- Exact inspected locators: introduction p1 defines an arbitrary smooth cubic fourfold over a finite field of characteristic p; the sentence following the Betti-number calculation states Frobenius semisimplicity and credits Rapoport. No characteristic restriction is imposed there. Corollary 5.2, author p8, states Tate for every self-power of an ordinary cubic fourfold; its proof continues to p9.
- Uses: semisimplicity in ARCH-15-CUBIC-GATE; warning that the ordinary self-power theorem has a different product scope from mixed X×abelian-target Tate. Refs: `turn451096804view0`, `turn258717699view1`.

M. Rapoport, *Complément à l’article de P. Deligne «La conjecture de Weil pour les surfaces K3»*, Invent. Math. 15 (1972), 227–236.

- Author-hosted primary scan: https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/ComplementaDeligne.pdf
- Inspected: introduction pp227–228 explaining extension of Deligne’s method; Table1 p228, cubic Hodge numbers; Theorem3.12 p236 verifying the required monodromy condition for cubic fourfolds. The text is about the Kuga–Satake/Weil argument and does not itself print the word “semisimplicity”; that deduction is explicitly recorded by Zarhin above. We do not invent a nonexistent semisimplicity theorem number in Rapoport.

P. Deligne, *La conjecture de Weil pour les surfaces K3*, Invent. Math. 15 (1972), 206–226.

- Official author page: https://publications.ias.edu/deligne/paper/362
- Primary scan: https://publications.ias.edu/sites/default/files/16_ConjectureDeWeilK3.pdf
- Selected locators: Proposition6.5 p222; §6.6, equation(6.6.2), p223; primitive exterior-square inclusion in the Clifford realization, p224. Cited for the classical cohomological construction, not algebraicity of its mixed cross-correspondence.

Keerthi Madapusi Pera, *The Tate conjecture for K3 surfaces in odd characteristic*, Invent. Math. 201 (2015), 625–668, DOI 10.1007/s00222-014-0557-5.

- Author research/publication page: https://keerthimadapusi.com/research
- Inspected author preprint: https://arxiv.org/pdf/1301.6326 (v3, 4 June 2014).
- In this inspected version, §5.14(2)–(3), author p27, supplies the cubic Kuga–Satake statement and Tate for codimension2 cycles in odd characteristic. **Numbering is version-specific:** do not relabel this §5.14 as an independently checked journal theorem number. The published K3 Kuga–Satake theorem is cited as Theorem5.17 by IIK2021.
- Only Tate surjectivity is used. It does not supply algebraicity of the general mixed forward correspondence.

Asher Auel, Avinash Kulkarni, Jack Petok, Jonah Weinbaum, *A census of cubic fourfolds over F2*, Mathematics of Computation, electronically published 24 September 2024, DOI 10.1090/mcom/4010.

- Author-hosted journal PDF: https://jonahweinbaum.github.io/material/cubic_fourfolds.pdf
- Exact locator: Theorem4.10 and its proof, §4.6, p20 of this 24-page journal PDF. It states Tate for codimension2 cycles on a smooth cubic fourfold over **any finite field of characteristic2**. The proof describes extension of the orthogonal Kuga–Satake map and notes the determinant-cover subtlety in even rank. Statement and the entire printed proof sketch were read, not the cited integral-model literature in full.
- Only the surjectivity consequence is used here. Refs: `turn923025564view1`, `turn571200210view0`.

### 4. K3 surfaces: finite height, square Tate, Kummer and slopes

Kazuhiro Ito, Tetsushi Ito, Teruhisa Koshikawa, *CM liftings of K3 surfaces over finite fields and their applications to the Tate conjecture*, Forum Math. Sigma 9 (2021), e29, 1–70, DOI 10.1017/fms.2021.24.

- Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9E14D5849CED8ABFC81CC49818267366/S2050509421000244a.pdf/cm-liftings-of-k3-surfaces-over-finite-fields-and-their-applications-to-the-tate-conjecture.pdf
- Inspected selected locators: Theorem1.1 p2 (finite-height CM lifting after finite extension); Theorem1.5 p3 (all-codimension Tate on the square, including p2,3); §1.3 p4 (cohomological embedding); Remarks6.9–6.10 pp35–36 (integral Kuga–Satake corrections); Remark10.5 p54 (crystalline semisimplicity); Lemmas10.9–10.10 pp55–56 (transcendental part, square Tate, Frobenius semisimplicity used explicitly). No whole-paper proof check claimed.
- Scope: these statements do not assert the mixed Tate maps on X×Y needed in ARCH-15-K3-GATE. Refs: `turn260375939view3`, `turn147042678view3`, `turn833960206view3`.

Daniel Huybrechts, *Lectures on K3 Surfaces*, Cambridge University Press, 2016. Author’s prepublication draft inspected; final pagination not assumed identical.

- Author page: https://www.math.uni-bonn.de/people/huybrech/K3.html
- Draft: https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf
- Chapter1 Example1.3(iii), draft pp8–9: Kummer quotient for char≠2, blowup of 16 two-torsion points and degree-two map. Full local discussion in the passage read.
- Chapter1 §2.2, p11: Hodge index; Proposition2.4, p12: Pic=NS=Num for a K3 surface.
- Chapter18 §§3.2–3.3, pp399–401: slope/height polygon on p400; equation(3.5) p401 identifies the formal Brauer group’s rational Dieudonné module with the slope[0,1) piece, hence the two heights coincide. These are the precise published-book results used for heights1,2 of the Kummer examples.
- Refs: `turn260375939view0`, `turn833960206view0`, `turn833960206view1`.

### 5. Geometry of the explicit Chow maps

T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J. 31 (1979), 97–115.

- Primary scan: https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf
- DOI: https://doi.org/10.2748/tmj/1178229881
- Lemmas1.1–1.2 pp98–99; Remark1.10 p102, equation(1.1′), for separated forms; Lemma2.1 p103 for the blowup cohomology. The detailed join/base-ideal/degree argument is inherited from CC-XC10, read through in this run.

Qingyuan Jiang, *On the Chow theory of projectivizations*, J. Inst. Math. Jussieu 22(3) (2023), 1465–1508, DOI 10.1017/S1474748021000451 (online November2021).

- Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3DA5197C99935D82CCB4E359214AF439/S1474748021000451a.pdf/on-the-chow-theory-of-projectivizations.pdf
- Exact inspected locators: Theorem2.8(3), p1472, Chow blowup isomorphism, explicitly summarized from Fulton’s Proposition6.7; Corollary3.10 p1484, motivic isomorphism with its stated blowup specialization. Ground field arbitrary in §1.2. The codimension-two inverse maps in our proof are directly checked by intersection, projection formula, and normal bundle O(−1).
- Ref: `turn724643982view2`.

For the classical curve–Jacobian Chow identification, CC-XC08 is an authorized inherited input. Scholl’s *Classical motives*, PSPM55.1 (1994), pp163–187, is the usual primary exposition:
https://www.dpmms.cam.ac.uk/~ajs1005/preprints/classical_motives.pdf
The PDF failed repeated retrieval (502/timeouts) in this run. No newly verified section/theorem number or whole-proof check of Scholl is claimed. The inherited C×C conclusion does not depend on treating that failed retrieval as a verification.

### 6. Exact limit of the proposed published CM replacements

P. Deligne (notes by J. S. Milne), *Hodge cycles on abelian varieties*, in LNM900 (1982), pp9–100.

- Updated author transcription: https://www.jmilne.org/math/Documents/Deligne82.pdf
- Original scan: https://www.jmilne.org/math/Documents/Deligne82_1982.pdf
- Exact locator read: Main Theorem2.11, author transcription p19. Its conclusion is absolute Hodge, not algebraic. We did not infer algebraicity from it.
- Refs: `turn260375939view1`, `turn650548640view2`.

J. S. Milne, *Lefschetz motives and the Tate conjecture*, Compositio Math.117 (1999), **45–76**.

- Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/962D833FAAC3219F55A58B193323B52A/S0010437X99000317a.pdf/lefschetz-motives-and-the-tate-conjecture.pdf
- Exact locator: Theorem7.1, journal p72, conditional on the Hodge conjecture for all complex CM abelian varieties. Statement and surrounding categorical scope inspected. It does not remove the algebraicity hypothesis.
- Ref: `turn833960206view2`.
- The 2026 all-CM preprint is kept as a named outside hypothesis in the fixed-target part. Milne’s unpublished 2022 `tcav2.pdf` is not relabelled as a published theorem here.

## Source corrected by the verified inherited counterexample

Steve Thakur, *Isogenies of certain abelian varieties over finite fields with p-ranks zero*, arXiv:2001.00210v1, 1 January2020.

- Inspected PDF: https://arxiv.org/pdf/2001.00210 (the retrieved header explicitly says v1). Version-specific /pdf/2001.00210v1 retrieval failed, so the header was checked rather than assuming the bare URL was v1.
- Exact inspected passages: Definition2.1 p3; Definition2.3 and Proposition2.9, including proof, p6. Its isogeny-model convention and assigned center/class number match BR-15-CLASSBOUND. The correction is restricted to that version and proposition.
- Refs: `turn724643982view1`, `turn816475981view0`.

## Review limits

The all-characteristic cubic semisimplicity citation is the explicit general sentence in Zarhin plus the classical Deligne–Rapoport construction; it is not inferred from the later ordinary-power theorem. The finite-field trace argument uses rational coefficients; there is no integral descent claim. A numerical/homological target projector in CC-XC11 has only a chosen Chow representative here. Exact Chow idempotence is asserted only where the retraction proves it. Published square/power Tate results are not silently widened to mixed products with an arbitrary abelian target.
