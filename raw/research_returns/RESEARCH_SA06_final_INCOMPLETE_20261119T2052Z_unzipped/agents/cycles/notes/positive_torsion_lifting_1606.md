# Torsion lifting and the remaining positive-characteristic cokernel

Research/source audit, 2026-11-19, completed source reading by 16:06 UTC. This note proves a group-theoretic reduction and records precisely why the sources inspected do not yet prove the required local cycle lifting. It makes no new main-task closure claim.

## 1. Exact group-theoretic reduction

Let f:A→B be a homomorphism of divisible abelian groups, let I=f(A), and let C=B/I. Then I and C are divisible. For every positive integer n the natural map B[n]→C[n] is surjective: if n b belongs to I, choose i in I with n i=n b, and b−i is an n-torsion lift of the class of b. Its kernel is I[n]. Thus

    C[n] = B[n]/I[n].

In particular C has no n-torsion precisely when B[n] is contained in I. If every torsion element of B lies in I, then C is torsion-free as well as divisible, hence is a Q-vector space. In that situation f is surjective if and only if f tensor Q is surjective. With one prime ell only, lifting B[ell-infinity] implies that C has no ell-primary torsion; other-primary torsion may remain.

For ordinary algebraic equivalence on the fixed products in this project, A and B are the algebraically trivial Chow groups. Their divisibility follows by representing differences using smooth proper curves and the divisibility of their Jacobian point groups. A finite sum of such images remains divisible: divide each summand in its Jacobian. Therefore the reduction applies to restriction. It requires lifting a torsion target class to some ordinary source class. It does not require that this source class itself be torsion. A theorem lifting torsion to torsion would be sufficient but stronger.

There is also a useful constraint on any proposed obstruction. The restriction cokernel is divisible, so a bounded-exponent cokernel must vanish. A nonzero torsion cokernel would necessarily contain torsion of unbounded exponent. The finite, exponent-p first-neighbourhood detectors used for the proven kernel results cannot simply be turned around to prove a cokernel is nonzero.

## 2. Prime-to-characteristic cycle maps: exact input and missing steps

Freshly opened and read Alexandrou–Schreieder (2023), Theorem 1.1, printed p.2; Theorem 4.2, Lemma 4.3 and Corollary 4.4, pp.13–14; and Lemma 4.5, p.14. For a smooth finite-type variety and ell invertible, their codimension-two torsion map identifies CH²[ell-infinity] with N¹H³(Qell/Zell(2))/M³. The denominator M³ is defined using continuous cohomology over finitely generated fields of definition. The source proves its vanishing for smooth projective varieties over algebraically closed fields, and identifies that special case with Bloch's map. We do not remove M³ for an arbitrary puncture.

Primary published PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/65A5FB842FB89629FED3B7BB8D603CA8/S2050509423000518a.pdf/on_blochs_map_for_torsion_cycles_over_nonclosed_fields.pdf
DOI: 10.1017/fms.2023.51. Full text was opened; the exact theorem paragraphs above were read. The separate timed fetch script records whether the binary was retained successfully.

This yields three separate obligations for the proposed local application at codimension two, source dimension six:

1. Establish the required cohomology restriction theorem for the actual pair of punctures. C.3p is a theorem about finite etale covers and H¹; it is not a theorem identifying H³. No higher-degree conclusion is inferred from equivalence of finite-cover categories.
2. Establish the appropriate coniveau and M³ compatibility. An isomorphism on full H³ does not by itself identify the subgroup represented by torsion cycles. Nor is the theorem's finite-type formulation silently identified with an arbitrary excellent henselian puncture: limits, supports and the quotient must be checked.
3. Ensure that a lifted Chow-torsion class is ordinary algebraically trivial. A preimage in the full Chow torsion group alone does not satisfy the group reduction in Section 1.

These obligations are not claimed logically necessary in this precise form for every possible proof; they are the missing steps in this particular proposed method. None has been supplied here in the general local scope.

## 3. Projective torsion Lefschetz: rejected auxiliary lemma and separate erratum

We freshly read the complete author version of Patel–Ravindra, Theorem 1.3/Remark 1, Theorem 2.5 and Section 3, and the one-page author erratum. Theorem 1.3 states a smooth-projective Chow-torsion Lefschetz result, with a prime-to-p version. Their erratum places an additional intermediate-Jacobian hypothesis on the Section 5 statements concerning Griffiths torsion; it explicitly distinguishes that correction from Sections 1–4.

The literal open-complement Lemma 3.2 is already rejected, with an independently checked explicit example, in the retained note:

    research/agents/real_weil/PATEL_RAVINDRA_TORSION_SCOPE.md

The present rereading independently confirms the issue. A simpler dimension-three instance uses Y=P³, X=(x0=0), and the smooth quadric V=(x0 x3+x1 x2=0). The divisor V contains the line (x0=x1=0), meets X properly, and X−V is A¹ times G_m. The smooth-divisor Gysin sequence gives H¹(P³−V,Z)=0, whereas H¹(X−V,Z)=Z. Thus the asserted open-complement isomorphism below dim X fails. The higher-degree generality and published-version comparison are already recorded in the earlier note; no new claim of main-theorem refutation is made here.

In particular, we do not use the mixed compact-support/ordinary-cohomology sequence in that proof to establish local torsion lifting. This is a repeated source limitation, not new task movement.

Author PDF: https://www.math.purdue.edu/~patel471/torsionWL.pdf
Erratum: https://www.math.purdue.edu/~patel471/torsion_erratum.pdf
Both were freshly opened. UMSL published-binary openings timed out in this pass; the indexed primary snippet agrees with the earlier published-text reading, but is not described as a new binary or page-image inspection.

## 4. The characteristic-primary map

Freshly opened and read Achter–Casalaina-Martin–Vial, 45-page author version, Appendix A.3.5, p.40, and Propositions A.27/A.30, pp.42–43. It records Gros–Suwa's construction and codimension-two injectivity with p-primary coefficients in the smooth projective setting, citing Gros–Suwa III, Definition 1.25 and Proposition 3.4. This is not a local surjectivity theorem. The appendix's flat-pullback/proper-pushforward assertions also do not remove the need to check the actual restriction construction and its image.

Opened author PDF: https://www.math.colostate.edu/~achter/math/bloch0720.pdf

Gros–Suwa (1988), Application d'Abel-Jacobi p-adique et cycles algebriques, Duke Mathematical Journal 57(2), 579–613, DOI 10.1215/S0012-7094-88-05726-2: the DOI opening failed; the Project Euclid article/PDF endpoints returned a security-check page. No original theorem text was obtained, and no attempt was made to bypass that control. Its original scope is therefore not described as independently verified. The exact projective statements above are attributed only to the opened ACMV review. Searches found citations and separate works, not the original full text.

Frobenius independently reopened Morrow (2019), Theorem 6.18 and Remark 6.19, printed pp.1597–1598. That formal inverse-limit cohomological result does not provide an actual torsion cycle lift. We do not reverse the already proved relative Milnor kernel detectors into such a lifting statement.

## 5. Current outcome

The group reduction is proved. No general prime-to-p or p-primary torsion lifting result for ordinary codimension-two cycles on the dimension-six puncture pair has been established. Consequently the remaining high-range integral and rational surjectivity questions are not identified unconditionally by this investigation. The split-cone rational comparison in the separate research note remains valid in its stated scope.
