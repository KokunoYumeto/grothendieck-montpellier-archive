# Boyle–Chen Appendix A: exact scope and failed boundary claim

Checked 2026-11-19, independently by the singularities/duality and Lie theory agents; root also opened the original pages.

## Original inspected

Keegan Boyle and Wenzhao Chen, *Negative amphichiral knots and the half-Conway polynomial*, Revista Matemática Iberoamericana 40 (2024), no. 2, 581–622, DOI 10.4171/RMI/1442.

Original full PDF: https://ems.press/content/serial-article-files/47105?nt=1 . Appendix A, Theorem A.6 and its proof, printed pp. 614–615 (PDF indices 33–34), were visually inspected. Original web retrieval: turn936163457view0; original-page screenshots: turn704329307view0 and turn704329307view1.

## Exact failure

The source models the projective plane as a disk with antipodal identification **only on the boundary**. Its displayed twist is

\[
 T_1(r,\theta,y)=(r,\theta+\pi y,y).
\]

At the upper interior point represented by Cartesian coordinates \((1/2,0,1)\), this gives \((-1/2,0,1)\). These are distinct points of the upper projective plane: neither lies on the disk boundary, so the quotient does not identify them. Consequently this literal \(T_1\) is not in the group fixing the whole boundary pointwise, and it cannot generate the relative-boundary mapping class group asserted in Theorem A.6.

The exact rational-coordinate certificate is saved and was executed by the Lie theory agent:

- `RESEARCH_SA20/agents/lie_theory/code/check_boyle_chen_top_boundary.py`
- `RESEARCH_SA20/agents/lie_theory/logs/check_boyle_chen_top_boundary.txt`

The recorded runtime is 0.000053159 seconds, with the two distinct interior quotient classes verified. This is a source-error certificate, not a computation of the full relative-boundary mapping class group.

The subsequent winding argument also cannot be imported as stated: winding relative to a chosen fixed annulus is not automatically invariant under arbitrary ambient isotopy. No claim of infinite order is used here. Merely replacing the half-turn by a full turn would not justify that argument.

## What the new proof uses instead

A.127 proves the free-top concordance component statement by its own complete annulus argument. It proves irreducibility from the orientation double cover, removes inessential intersection circles with an explicit ball argument, uses a relative arc theorem and proper-disk uniqueness, and extends annulus isotopies through the normal-orientation double cover.

Its twists are constructed as actual jointly PL families. A boundary translation is extended through a PL collar; a relative disk Alexander isotopy corrects its endpoint to the exact antipodal linear map. Repetition gives the required winding, and the free-top contraction is explicit. The argument never claims that the first twist fixes the top, and never promotes winding to an ambient-isotopy invariant. Thus the incorrect relative-boundary conclusion of Boyle–Chen A.6 is not an input to A.127.

## Other checked but insufficient projective-plane leads

- Seiya Negami, *Irreducible 3-manifolds with non-trivial pi2*, Yokohama Mathematical Journal 29 (1981), 133–144, original downloaded as `logs/negami1981.pdf`. Lemma 1.1, pp. 134–136, makes an interior projective plane in the product parallel to the boundary. It does not compute the entire product mapping class group. Its annulus-cut method is compatible with the new proof but is not used as a replacement for that proof.
- Kalliongis–Ohashi, *Finite actions on the 2-sphere, the projective plane and I-bundles over the projective plane*, Ars Mathematica Contemporanea 15 (2018), 297–321, DOI 10.26493/1855-3974.806.c9d. The full primary text was opened on ResearchGate. Theorems 7.3–7.4, pp. 313–314, concern finite-action conjugacy. Section 8 concerns the twisted I-bundle. Neither supplies the required arbitrary concordance statement.
- Johannson's simple-three-manifold paper explicitly restricts all three-manifolds to be orientable, p. 49; its I-bundle arguments cannot be applied to the product RP2 times I without a new proof.
- Rubinstein's 1977 *Isotopies of the projective plane in 3-manifolds*, Topology 16, 217–226, DOI 10.1016/0040-9383(77)90002-7, was identified bibliographically but its original theorem pages were not opened. It is not used as an input.
