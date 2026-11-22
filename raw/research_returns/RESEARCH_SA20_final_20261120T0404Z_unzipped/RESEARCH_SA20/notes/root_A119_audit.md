# Independent root audit of the countable concordance presentation

Status: the dimension-at-least-nine draft passes, subject to integrating the explicit group-law and Kan-formula clarifications below. It remains outside the assembled checked inventory during checkpoint07 source freeze. The proposed improvement to dimension six is a separate audit.

We reread the entire draft and checked the finite-cell countability argument, finite-factorization restriction of the hammock comparison, group-completion hypotheses, abelian-cover construction, Hurewicz comparison, and quotient by the full unit image. The construction gives every relation on integral two-cycles, including extension relations; it does not claim a finite invariant-factor answer or a terminating word algorithm.

For a finite cell source, a simplicial family with finite parameter set uses finitely many generators in an omega-stage acyclic-cell fibrant replacement. Each used cell has finitely many dependencies at earlier finite stages. Inducting down the largest stage gives a finite dependency-closed subextension. The same argument works relative to a finite parameter boundary and for the two inverse homotopies. This is the required finite-object restriction, not an assumption that a general fibrant replacement is finite.

The monoid used for group completion is the disjoint union of classifying spaces, with direct sum, not the uncompleted connected telescope. Its components form the natural numbers and adjoining a rank-one identity is cofinal. Acyclicity supplies local-coefficient homology isomorphisms, hence integral homology isomorphisms on the pulled-back universal covers. The targets are infinite loop spaces with abelian fundamental groups; their pulled-back covers are the universal abelian covers described by edge labels. Hurewicz is applied on the simply connected target covers, not directly on possibly nonsimply-connected source covers.

## Group law

Waldhausen–Jahren–Rognes, Remark1.1.11 and equation(1.1.12), printedp12, explicitly identify the product h-cobordism component with BC(M). A bar two-simplex identifies its composite edge with concatenation, giving the group isomorphism pi0 C(M)=pi1 BC(M). Apply pi1 to the stable h-cobordism equivalence H^st(M) ≃ Omega WhDiff(M); no H-space compatibility of the unlooped equivalence is required. Positive stabilization is represented by the product functor on h-cobordism bundles, with the usual collar adjustment for the boundary-fixed concordance model. This gives the group identification with pi2 WhDiff(M).

## Original sources independently opened by root

- Hovey–Shipley–Smith, Symmetric spectra, Theorem3.4.4 printedp180 and Definition3.4.9/Lemma3.4.10 pp181–182. https://homepages.math.uic.edu/~bshipley/symmetric.pdf
- Schwede–Shipley, Algebras and modules in monoidal model categories, Theorem4.1(1) pp498–499 and its proof p504, including free-module images of generating acyclic cofibrations. https://www.math.uni-bonn.de/~schwede/AlgebrasModules.pdf
- Dwyer–Kan, Function complexes in homotopical algebra, Section3 finite hammocks and Proposition4.4/Application4.6 printedp432. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/dwyer-kan-3.pdf
- Goerss–Jardine, Simplicial homotopy theory, V Section5, formula(5.1), printedp276, specifies the Kan loop group and its face operators. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf
- Gritschacher, Acyclicity in the group-completion theorem, arXiv1709.02036v2, Proposition1.1 and proof pp1–7; universal-abelian-cover reduction p3.
- Jahren2010, Section2 pp247–248, free-rank group-completion and unit models, splitting and basic homotopy diagram.
- Waldhausen–Jahren–Rognes, 166-page author version: Theorem0.1 p2; Remark1.1.11 p12; Definition1.3.4/(1.3.5) p18; smooth stability Theorem1.4.1 p21. https://www.mn.uio.no/math/personer/vit/rognes/papers/plmf.pdf

The n>=9 deduction uses k=1 in n>=max(2k+7,3k+4). Smoothability and the already checked Burghelea–Lashof smooth-to-PL component comparison remain explicit. A.113 transfers components to the definable model over every real closed field.

## Separate lower-range audit

Root has also opened Hatcher–Wagoner PartI ChapterIV Section1 printedp130, Remark (first obstruction unchanged by suspension), and Igusa2021 arXiv2112.08293v1 Theorem3.1 p6 and Section4.2 pp8–9 (corrected sequence and normalized second obstruction compatible with positive suspension). Before promoting n>=6, check the induced identification of the corrected kernel quotient and the fixed-boundary convention under repeated suspension. No source-free splitting of the exact sequence is used.

Root audit recorded at 2026-11-19T16:17:18.937690+00:00.

## A.120 stable nonsmoothable extension

Root independently read the complete draft and passed it. The explicit cofiber triangle is WhDiff(*) smash K+ -> WhDiff(K) -> WhPL(K), obtained from the composite unit and assembly. The first spectrum has no homotopy in degrees0,1,2: degree0 is the rank-unit isomorphism; degree1 is Wh1(1)=0; degree2 is the stable smooth-disc concordance component group, which is zero by the smooth-to-PL component comparison on a sufficiently large disc and the Alexander contraction of PL disc concordances. Finite K+ has cells only in nonnegative degrees, so smashing preserves this connectivity. The exact homotopy sequence gives the required isomorphism in degree2. The stable PL h-cobordism theorem and the already checked classifying-space group law identify the result with the stable concordance component group. Relative PL/definable comparison is applied stage by stage before taking the colimit.

Original WJR166-page author version independently opened: introductory p4 identifies pi1 WhDiff with the classical Whitehead group; pp16–18 give the unit and PL assembly definitions; pp22–23 state the PL comparison and PL-disc contractibility. The proof does not replace a general nonsmoothable PL manifold by a smooth one and makes no assertion that its unstable group has stabilized.

## Superseding checked ranges

A.119's original n>=9 smoothable statement remains as the base theorem. A.120 gives stable arbitrary PL components. A.121 removes smoothability for unstable n>=9 by skeleton localization. A.122, independently checked by root and lie_theory, lowers the final all-PL range to n>=6 using the full corrected geometric exact sequence and the explicitly verified dimension6 smoothing chain. Current gates are recorded in unchecked_A.tex and the report; the earlier pending-language above is dated audit history.
