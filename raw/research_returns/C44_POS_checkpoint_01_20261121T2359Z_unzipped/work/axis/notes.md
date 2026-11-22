# Axis research notes

Run C44_POS, agent /root/axis_independent, GPT-6 Astra Pro, effort setting not exposed. Date 2026-11-22 Europe/Berlin (UTC session began 2026-11-21).

## Exact carried inputs read

- JAC1964.tex H9-T7, equations (H9.17)–(H9.24), full proof: exact isometry and L_Bw=0.
- H9-T8a: characteristic-zero sign. No reproving.
- H9-T5: odd variable local system, slope interval [m−1,m] and geometric monodromy irreducibility.
- H9-T13, paragraph “Why this does not close the arbitrary fixed-axis gate”: ambient pushforward of w⊠P_E is zero; this is already a settled route obstruction and must not be relabeled as new.
- H9-T16 full proof: semistable degeneration, operational Chow gluing, generic monodromy obstruction, support-preserving incidence locus failure. These do not supply reverse Chow specialization.
- JAC-P16: specifically excludes positivity for geometric abelian-type varieties' own geometric intersection forms. Underlying motivic type is not alone a metric transfer.

## Findings written

C44-A01: exact primitive direct sum; entire remaining I(B) gate. New deduction of a form not explicitly stated in H9-T7; no positivity closure. Distinguishes semidefinite from definite.

C44-A02: every graph map B→abelian target kills A_B, via Albanese isogeny. Direct H1-curve-to-even-middle correspondence also ruled out by parity. General correspondences remain possible.

C44-A03: potential Tate-root vanishing criterion and explicit finite cyclotomic test; one out-of-range slope insufficient for the fixed even axis. No universal witness.

## Approaches tried without closure

1. Nonliftability inherited from ambient examples: impossible via restriction because projector kills all restricted classes. Official primary Agugliaro PDF checked Proposition5.12, Remark3.5. This fails to manufacture nonliftable A_B.
2. Supersingular X: all ambient even cohom slope r, no conclusion on B variable part. Looked for known supersingular smooth ample complete-intersection axes and did not find a usable source. Search absence is not claimed as a theorem.
3. Graphs of quaternionic endomorphisms on supersingular elliptic products: can obstruct simultaneous lifting of marked supports, but not lifting a rational cohomology class in A_B; no valid class-level counterexample.
4. Many disjoint abelian subvarieties in B: root owns explicit positive calculation. Such examples lift and are not nonliftable classes; no dimension argument established enough algebraic rank to exceed all Hodge lifts.
5. Products of supersingular curves or theta subvarieties: straightforward product embeddings have nonample defining divisors and do not give an axis in |h|². No valid conversion obtained.
6. Cayley trick/blowup realization: h(Bl_B X)=h(X)⊕h(B)(−1), so transferring positivity this way reproduces the unknown center sign.
7. Finite-field rational Chow on X (JAC-P15) strengthens κ_*w=0 to a rational Chow-kernel statement after choice of representatives, but localization leads to higher Chow classes on X\B without positivity. No improvement of main sign gate.
8. Pure Frobenius weights/semisimplicity: even potential Tate block can coexist with out-of-range slopes elsewhere. Full sign cannot follow solely from purity.

## Primary web sources opened

- Agugliaro, official EMS final PDF https://ems.press/content/serial-article-files/53071 . Proposition5.12 pp876–877; Remark3.5 p870. Current final article Doc.Math.31 (2026)855–904, DOI10.4171/DM/1057. Web IDs turn500642281view0, turn500642281view1, turn500642281view2.
- Milne course notes official https://jmilne.org/math/CourseNotes/AV.pdf . Direct official PDF open and find checked I Theorem3.2, printed p17 / PDFp23, web IDs turn517429084view0 and turn517429084view1.

No source states universal nonliftability of the fixed-axis classes. No such statement is asserted.

## Geometry lifting (C44-A05)

The embedded smooth complete-intersection axis always lifts, including supersingular ambient X. Written full proof in axis_contribution.tex using polarized lifting, exact ample line-bundle lift, base change for sections, universal section-pair parameter space, open Jacobian smoothness, and an explicit arithmetic-curve trait reduction. This does not assert a cycle lifts.

Primary sources:
- Oort, Did Earlier Thoughts Inspire Grothendieck?, Theorem(8.3).1 p29, author PDF https://webspace.science.uu.nl/~oort0109/AGRoots-final.pdf; direct theorem checked.
- Olsson, Compactifications of moduli of abelian varieties: an introduction, MSRI Publ59(2011), Lemma2.1.8 and proof pp299-300 preserves the chosen special-fibre ample bundle; §2.1.4 p299 gives higher-direct-image vanishing and base change. Official PDF https://library.slmath.org/books/Book59/files/65olsson.pdf.
- Stacks Project tags01ZM,0C0C,081F give finite-presentation, smoothness, and properness descent.
- Stacks tag0CM2 gives a general trait, but the written proof uses a separate elementary parameter/height/excellence argument to ensure finite residue field, hence the original geometric special fibre.

C44-A04/A04a independent whole-proof review PASS. Exact SGA sources checked at Katz author PDF https://web.math.princeton.edu/~nmk/old/pinclef.pdf: XVII1.1-1.2 pp213-214;3.2.1-3.2.4 p219;3.3 p221;3.7 p234;4.2-4.3 pp236-239. Imposed-centre construction is a new incidence argument, not a verbatim SGA result.
