# Arbitrary-manifold pi0: exact extension-law audit

This is a pending research note during checkpoint06 freeze, not a proved result.

## Opened sources

- Igusa, Generalized Grassmann invariant-redrawn, arXiv2502.19147v2, 23 March2025, https://arxiv.org/pdf/2502.19147. Local source_external/lie_theory/igusa2025.pdf and .txt. Independently opened webref turn831672093view0. Section3 pp12-14, Cor3.5 p14; Section7 pp23-27, Th7.1 p23, Lemma7.2 pp25-26, Remark7.3 p26, Th7.5 p27.
- Igusa, Second obstruction to pseudoisotopy in dimension3, arXiv2112.08293v1, https://arxiv.org/pdf/2112.08293. Independently opened webrefs turn825594976view0-2. Th3.1 p6, Cor3.2 p6 and subsequent application.
- Jahren, Pseudoisotopies and the Boeckstedt trace, Geom.Dedicata148(2010)245-261, https://www.maths.gla.ac.uk/~mpowell/Jahren2010_Article_PseudoisotopiesAndTheBokstedtT.pdf. Opened refs turn831672093view1-3. Section2 pp247-250, Cor2.7 p250; introductory range dimM>=7 p246.

## Exact conclusions

Igusa2025 Th7.1 assumes compact smooth M, dimM>=5, pi2M=0. It gives Wh3(pi) -> Wh1(pi;F2) -> pi0P(M) -> Wh2(pi) -> 0. The printed K3 in its description of H2(GL-prime) is an index typo; this is K2. The source refers pi2M!=0 to its referenceI3, the 1984 LNM1046 paper.

Its Lemma7.2 gives the change in the secondary invariant under a specified Steinberg commutation. Remark7.3 says the previous splitting result fails even when chi_Wh=0; this is a rejection of the general splitting claim, not a statement that every individual short exact sequence is nonsplit (the torus has Wh2=0). Cor3.5 identifies a class in H3(St(Z[pi]);H0(pi;F2[pi])) with a Postnikov invariant of GL(Z[Omega Bpi]).

Igusa2021dim3 Th3.1 restates the general exact sequence in dimension>=6 and gives a matrix-chain formula for the pi2-valued part of chi using k1M. This determines the indicated map in the exact sequence, not a multiplication/cocycle for arbitrary lifts of Wh2.

Jahren Cor2.7 packages the sequence as the homotopy sequence of the A-theory linearization. It supplies the full canonical group pi2WhDiff(X) in the stable description. Its splitting theorem2.4 is for the monomial map pi2^s(Bpi_+) -> K2(Z[pi]), not a splitting of the pseudoisotopy extension. No such conflation is permissible.

In the stable range the group is abelian. An exact sequence 0->A->E->B->0 by itself leaves an Ext1_Z(B,A) class. Knowing chi on K3 identifies A=coker(chi), but does not determine that class. The full three-cocycle/descent data may contain it, but no full descent identification or presentation has been proved here. The St group is superperfect; the displayed H3 class lives above the 2-connected cover and its homomorphism on H3 does not by itself specify an extension over K2 or Wh2.

## Source attempts

The original LNM1046 chapter DOI10.1007/BFb0072020 is linked by Numdam JEP2021 referenceIgu84, but currently redirects to Crossref deleted_DOI.html; direct Springer chapter/PDF routes return404. It is NOT OPENED.

The author-hosted manuscript Postnikov Invariants and Pseudoisotopy is indexed at https://people.brandeis.edu/~igusa/Papers/PostnikovInvariantsComp2.pdf and author Selected.htm labels it1975?. This is a different source. Direct ordinary HTTPS/HTTP attempts returned503; webopen returned502. Its full text is NOT OPENED; source-attempt log is adjacent. Search excerpts cannot upgrade this status.

## Exact remaining next step

Find/open a complete crossed-module or Postnikov presentation identifying pi0P including the extension law, or prove the identification from explicit algebraic data. A stable A-theory quotient description retains that law canonically, but is not an explicit computation of its values and does not alone settle low dimensions or nonsmoothable PL models without a correctly typed comparison. No gate shrink claimed.
