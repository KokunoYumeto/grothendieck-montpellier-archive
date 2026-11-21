# Finding A08: finite prime avoidance in positive 2-rank

Date: 2026-11-21. Checker and proof author: GPT-6 Astra Pro, `/root/effective_galois`; effort not exposed.

## Result

For each f in {1,2} and each finite set S of odd primes there is a smooth projective geometrically connected genus-two curve C over some finite extension of F2, of 2-rank f, whose Raynaud theta support has no nonzero geometric ell-torsion for any ell in S. The extension degree is allowed to grow with S. Thus there is no curve-independent finite list of candidate primes, even after fixing either positive 2-rank.

Full section-ready proof: `finite_prime_avoidance.tex`. No final file was edited.

## Primary source checks

- Ekin Ozman and Rachel Pries, *Ordinary and almost ordinary Prym varieties*, Asian Journal of Mathematics 23(3) (2019), 455–478, DOI 10.4310/AJM.2019.v23.n3.a5. Published Theorem 1.1(2), p456, and Theorem 8.3, p473, explicitly allow every prime p and genus g>=2, provided f is nonzero when g=2. For each irreducible component of M_g^f the geometric generic curve has no theta point of order ell, for each fixed ell!=p. The full geometric quantifier is essential. The published statement was read directly, together with the complete short proof of Theorem 8.3. The long proof of Theorem 1.1(1) was not independently re-proved here.
- Published Section 8.1, p472, defines the theta divisor on the Jacobian of the relative Frobenius twist, via the cokernel B of O -> F_*O, with theta support given by nonzero H0(B tensor L). The proof keeps this twist explicit.
- Published Section 2.5, p458, recalls locally closed p-rank strata and lower semicontinuity. The new proof additionally explains the genus-two Hasse–Witt rank calculation that preserves a fixed p-rank after shrinking.
- Rachel Pries and Hui June Zhu, *The p-rank stratification of Artin-Schreier curves*, Annales de l'Institut Fourier 62(2) (2012), 707–726, DOI 10.5802/aif.2692. Lemma 2.6, p712, supplies the genus and p-rank formulas used solely to exhibit nonempty genus-two strata. The two example models have pole-order lists (3,1) and (1,1,1), respectively.

Primary URLs:

- https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2019/0023/0003/AJM-2019-0023-0003-a005.pdf
- https://www.numdam.org/item/10.5802/aif.2692.pdf

Web references root can reopen:

- `turn773491003view0`: published Ozman–Pries full PDF.
- `turn719018644view0` and `turn719018644view1`: exact published Theorem 8.3, p473.
- `turn157375857view0`: published Sections 8.1–8.4 and exact theta convention.
- `turn719018644view2`: p-rank strata, Section 2.5, p458.
- `turn157375857view1`: published Pries–Zhu full PDF.
- `turn459516695view0`: exact Lemma 2.6, p712.

## Whole-proof check

**PASS, as a mathematical proof audit rather than formal verification.** I checked the entire deduction after writing it, including the following possible failure points.

1. One component and one geometric generic curve work for every prime in the finite set. No inference from one generic cyclic cover to every cover is needed: the primary theorem states precisely the required theta exclusion.
2. A curve at a geometric generic moduli point is taken over an algebraically closed field. Its equations and one marked point descend to a finitely generated integral F2-algebra. This avoids assuming a universal curve on a coarse moduli space or an unproved field-of-moduli descent. A finite-type scheme family is produced before any incidence projection.
3. Smoothness, geometric connectedness and genus survive after shrinking. For fixed 2-rank f, rank(H H^(2)) is the stable Frobenius rank on the two-dimensional H1. Larger minors vanish identically on an integral base, and one nonzero f-minor gives the required open set. Thus the rank-one statement does not accidentally specialize to rank two.
4. Relative Frobenius for a smooth curve is finite locally free of degree two; its cokernel by the unit section is a line bundle, and the construction commutes with base change. A section of the curve supplies an actual Poincare bundle.
5. The theta incidence is closed by proper cohomological semicontinuity. Only its support is used. The reduced closed subset on a noetherian scheme suffices; no global Cartier theta assertion is silently assumed.
6. Nonzero ell-torsion forms a finite etale scheme because ell is odd. Removing zero retains finiteness, since the zero section is open and closed in the finite etale group scheme. Its intersection with theta is therefore finite over the base, and its image is closed. This projects all geometric torsion points at once, not only rational torsion sections.
7. Each bad image misses the generic point by the theorem and faithful field extension to the chosen algebraically closed field. A finite union still misses it. A nonempty finite-type F2-scheme has a closed point with finite residue field.
8. The conclusion explicitly allows the finite field and curve to depend on S. It neither interchanges the quantifiers nor asserts that a countable intersection of open sets has a finite-field point. It supplies no effective extension-degree bound.

The explicit three-parameter Artin–Schreier family proposed initially is unnecessary. Spreading a single geometric generic curve removes the need to prove that particular family dominates the ordinary moduli stratum, while also obtaining the 2-rank-one case from the same argument.

## Exact foundational locators and recovered source scope

The recovered `ANABELIAN_SUCCESSOR_final_text/ANABELIAN_SUCCESSOR_paper.tex`, A.16, was read in full. It already proves the ordinary finite-list obstruction, for arbitrary characteristic and genus. The current argument states the theta-support exclusion and proves it using a scheme family, and also covers fixed 2-rank one. No novelty claim is made for the ordinary result.

- **Finite-presentation spreading:** Stacks Project, Lemma 32.10.1(1)–(3), Tag 01ZM, covers descent of objects, morphisms and equalities along an affine inverse limit. It applies to the curve together with its marked-point morphism. Directly read at https://stacks.math.columbia.edu/tag/01ZM ; web ref `turn776880654view0`.
- **Original Grothendieck spreading locator:** EGA IV, third part, Theorem 8.8.2(ii) for objects and (i) for morphisms, printed p28, in Publ. Math. IHES 28 (1966), 5–255, DOI 10.1007/BF02684343. The full original French primary PDF finished downloading and the exact theorem was read in `EGA_IV3.txt`. Primary PDF: https://www.numdam.org/item/PMIHES_1966__28__5_0.pdf ; bibliographic page ref `turn457558539view1`. This now appears directly in the proof, with the Stacks equivalent retained.
- **Connected fibres after shrinking:** EGA IV_3, Theorem 9.7.7(ii), printed p79, states local constructibility of the geometrically connected fibre locus for a finitely presented morphism. Directly read in the original same volume. On the noetherian integral base a constructible subset containing the generic point contains an open neighbourhood of it. Smoothness follows by removing the proper image of the nonsmooth locus in the projective model.
- **Constant genus:** EGA III_2, Theorem 7.9.4, printed pp76–77, gives local constancy of Euler characteristic for a proper morphism and a bounded coherent base-flat complex. Directly read in the original French volume; applied to O in degree zero after smoothness, with connected fibres, it preserves the genus.
- **Semicontinuity:** Grothendieck, EGA III, second part, Theorem 7.7.5(I), printed p67, in Publ. Math. IHES 17 (1963), 5–91, DOI 10.1007/BF02684890. The original French primary PDF was downloaded and the exact statement read. It assumes a locally noetherian base, proper morphism and coherent base-flat complex, and asserts upper semicontinuity. Here the complex is the line bundle in degree zero on the smooth proper curve over the relative Jacobian, so every hypothesis holds. Primary PDF: https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf ; bibliographic page web ref `turn457558539view0`. The web service rejected the PDF because of its size; the original text is locally retained as `EGA_III2.txt`.
- **Modern exact formulation:** Stacks Project, Lemma 36.32.1, Tag 0BDN, states upper semicontinuity and arbitrary base-change compatibility for fibre cohomology dimensions of a finitely presented base-flat sheaf under a proper finitely presented morphism. Directly read at https://stacks.math.columbia.edu/tag/0BDN ; web ref `turn121276613view0`.
- **Finite cohomology complex, if needed:** Stacks Project, Lemma 30.22.1, Tag 07VK, and Remark 30.22.2 give perfect cohomology and its arbitrary base-change compatibility over a noetherian affine base. Directly read at https://stacks.math.columbia.edu/tag/07VK ; web ref `turn121276613view1`. The direct semicontinuity citation suffices for the proof.

Root and `/root/gt_certificates` each reported an independent whole-proof PASS on the prior mathematical version. The changes in this section add exact source locators and prior-source credit, without changing the proof.

## Ordinary strengthening: finite lists of arbitrary odd integers

At root's request A08 now also includes, only for f=2, avoidance of every nonzero point of J[n] for any prescribed finite set of odd integers n>=3. This covers any finite list of prime-power candidates in A11.

Primary input: Yu Yang, *Raynaud–Tamagawa theta divisors and new-ordinariness of ramified coverings of curves*, Journal of Algebra 587 (2021), 263–294, DOI 10.1016/j.jalgebra.2021.07.032. I directly read the author-hosted Theorem 3.5 and its entire proof, Definition 3.3, Lemma 3.2, and definitions 2.1.3 and 2.2.2. Theorem 3.5 applies to every degree m prime to p and every cyclic cover of the geometric generic pointed curve. In the unpointed etale case all ramification divisors D(j) are zero, and the displayed degree equalities in Definition 3.3/Lemma 3.2 are automatic. Hence every such cover has ordinary new factor. The generic base is ordinary, also recorded in Yang's Theorem 1.1. Theorem 3.5's underlying Proposition 3.4 proof and the original Nakajima theorem were not independently reconstructed in this check.

Primary URL: https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/RTOC.pdf . Own web refs: `turn554282525view0` (full author PDF), `turn952509222view0` (Theorem 3.5 and complete immediate proof), `turn952509222view1` (Lemma 3.2 and Definition 3.3), `turn904242845view1` and `turn904242845view2` (definitions). Author PDF page numbers for Theorem 3.5 are20–21; these are not asserted to be the journal's printed page numbers.

**Complete added proof check: PASS.** A hypothetical exact odd-order-d theta point L gives M=(F*L)^e with 2e=1 mod d, M^(2)=L, and a zero Frobenius arrow from H1(M) to H1(M²) in the degree-d Kummer cover's nontrivial-character sum. This makes that sum's stable rank deficient, contradicting new-ordinariness. No multiplication by d or projection of a theta point is assumed to preserve theta. For finite n-lists, J[n] minus zero is finite etale and includes every nonzero torsion point of any order dividing n. Thus the same finite closed-image argument applies without needing separate exact-order subschemes. The original finite-set/variable-finite-field quantifier is unchanged. The f=1 result remains prime-only, as required by Yang's Section 3.6.2 and Corollary 3.6.
