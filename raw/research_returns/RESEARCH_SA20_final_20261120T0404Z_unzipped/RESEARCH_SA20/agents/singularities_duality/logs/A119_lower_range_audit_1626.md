# A.119 lower-range audit, 2026-11-19 16:26 UTC

Status: PROMOTED as separate A.122 at 2026-11-19T16:48:29+00:00 after root and lie-theory audits. A.119 retains its original dimension >=9 base statement. The full corrected geometric exact sequence is a cited input; no partial-formula-only reconstruction is claimed.

## Exact maps, not merely two abstract exact sequences

Write A(M)=Wh_1^+(pi_1 M; Z/2 + pi_2 M). Use positive suspension throughout. Its formula on the normalized concordance subgroup is g on each fixed polar ray, so sigma(g h)=sigma(g)sigma(h). Igusa, Second obstruction to pseudoisotopy in dimension 3, section4.1 p8, gives this formula explicitly. Fixed lower and side collars are respected.

For dim M>=6 choose marked lens-shaped models in indices3,4. Both relevant sphere codimensions are at least3, and they remain so under positive suspension. Thus there is no need to change the index convention when the ambient dimension changes parity. Igusa, Second obstruction to pseudoisotopy I, Theorem1.8 p8 and Lemma1.10 pp9--10, identify the marked-lens group with framed1-bordism in Omega M modulo the identity component; taking marking coinvariants gives A(M). The displayed definition uses k=floor(n/2), but its proof uses only k>=3 and n-k>=3, so the same proof applies to fixed k=3 for every n>=6. The homomorphism theta_M:A(M)->pi_0C(M) forgets the lens model. Positive suspension preserves the complete framed1-bordism invariant, including its Z/2 framing coordinate: Igusa dimension3 paper section4.2 p9. Hence

    sigma_* theta_M = theta_(M x I) id_A.

The first obstruction Sigma is also unchanged: Hatcher--Wagoner, PartI ChapterIV section1, Remark printedp130, by the stable/unstable trajectory equality from PartI ChapterI section5, equation(5.2), p60. Therefore the right-hand quotient map on Wh_2(pi_1 M) is the identity.

The corrected sequence (Igusa dimension3 paper, Theorem3.1, printedp6) says, in its explicitly stated range dim M>=6,

    0 -> A(M)/im chi_M -> pi_0 C(M) -> Wh_2(pi_1 M) -> 0.

The entire image of chi is necessary. The displayed matrix formula in that theorem determines only the pi_2-valued component and cannot alone justify the framing-coordinate comparison.

The stable corrected sequence, with theta from the same marked-lens construction, is displayed in Igusa, Second obstruction to pseudoisotopy I, introduction (0.2) p2. The commuting square on p3 explicitly identifies forgetting a marked lens and then stabilizing with its framed-bordism invariant followed by stable theta. Thus the intended corrected chi in the unstable stable-range statement is the relation subgroup of this same stable theta, not an arbitrarily chosen map between isomorphic groups. Jahren2010 calls the functorial sequence of Corollary2.7 p250 Igusa's exact sequence; its basic diagram pp247--250 constructs the full chi (both summands) as a connecting homomorphism for A(X)->K(Z[pi_1X]), modulo the monomial unit. In particular the whole relation subgroup is preserved by M x I -> M.

Remaining source-audit point for root: this identifies the full chi using the two opened restatements and their declared matching of geometric and A-theory exact sequences. The original Igusa1984 chapter is not opened. Do not claim to have independently reconstructed its geometric-to-A-theory comparison from the pi_2 matrix formula alone.

Once the common chi image is accepted as the content of these corrected-sequence statements, the diagram

    0 -> A/im chi -> pi_0C(M)       -> Wh_2(pi_1M) -> 0
         | id          | sigma_*          | id
    0 -> A/im chi -> pi_0C(M x I)   -> Wh_2(pi_1M) -> 0

commutes, and elementary exactness proves sigma_* is a group isomorphism. Explicitly, injectivity follows by moving a kernel element into A/im chi and using the injective lower left arrow; surjectivity follows by lifting its Wh_2 quotient and then its difference in A/im chi. This does not assume either extension splits. Iterating identifies unstable components with the stable group E(K), giving the proposed n>=6 improvement.

## Boundary conventions

Igusa, Second obstruction to pseudoisotopy I, introduction p1, explicitly defines C(M)=Diff(M x I rel M x0 union boundary(M) x I) for any smooth compact manifold. Section1 p3 imposes the projection function on a neighborhood of all of boundary(M x I). Its Theorem1.8 and Lemma1.10 therefore use compact manifolds with boundary, with all modifications supported in the interior. This covers M x I^j after rounding corners. Hatcher--Wagoner's original setup is the compact pair (M,boundary M), p9, and section5 p55 replaces it by an equivalent subspace fixed near lower and side boundaries before suspension. Igusa's positive polar-ray formula also assumes those collars. There is no closed-manifold-only step in the diagram.

## Newly opened source locators

- Igusa2110.09659: https://arxiv.org/pdf/2110.09659 ; tool refs turn224183426view0 (full), turn891014556view2 (Theorem1.8 p8), turn891014556view3 (framed invariant and Lemma1.10 p9). The complete definition and proof of Lemma1.10 were read.
- Igusa2112.08293: https://arxiv.org/pdf/2112.08293 ; turn903732987view2 (Theorem3.1 p6), turn903732987view3 (positive suspension section4.1 p8 and invariant compatibility section4.2 p9).
- Hatcher--Wagoner: https://www.maths.gla.ac.uk/~mpowell/Hatcher-Wagoner.pdf ; turn794386770view0 (section5 pp54--61), turn794386770view1 (Remark p130).
- Jahren2010: https://www.maths.gla.ac.uk/~mpowell/Jahren2010_Article_PseudoisotopiesAndTheBokstedtT.pdf ; turn234348378view0 (full section2 pp247--250, including Corollary2.7).
- The distinct author-hosted PostnikovInvariantsComp2.pdf still returns502 in both http/https attempts (turn110144531view1/2). Original1984 chapter remains not opened.

## Rejected corroborating route

Kinsey--Prassidis2010, A Bass--Heller--Swan formula for pseudoisotopies, Geom.Dedicata148,263--289, https://www.samos.aegean.gr/math/prasside/pseudoisotopies.pdf, was opened. Its pp264--265 invoke a dimension>=7 stable range, but Remark6.5 p280 repeats an unqualified direct-sum Hatcher--Wagoner formula that omits the corrected chi quotient. It is not used to validate the lower-range claim. Tool refs turn110144531view0 and turn314666189view1. The original paper's other results have not been audited here.
