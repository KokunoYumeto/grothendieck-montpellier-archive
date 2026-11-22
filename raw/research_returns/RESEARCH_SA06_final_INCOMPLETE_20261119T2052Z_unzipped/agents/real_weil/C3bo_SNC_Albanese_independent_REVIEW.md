# C.3bo / AM.1–AM.9: independent full proof and source review

Completed: **2026-11-19 17:41:29 UTC**.

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not exposed. The reviewer is a sibling agent of the proof owner, not a separately identified model family.

**Outcome: PASS of the complete typed proof under its stated C.3bm hypotheses. No mathematical correction is requested.**

Reviewed file: `../frobenius/C3_SNC_Albanese_matrix_draft.tex`, all four proof steps and equations AM.1–AM.9. This receipt does not certify a new computation or build run.

## Complete mathematical check

1. The canonical Albanese is taken to be the dual of the reduced connected Picard variety. For the curve Abel map into its Picard Jacobian, Milne's exact sign is `f* lambda = -id`. Therefore the canonical dual-valued Albanese map is `-lambda f`. With this convention, the surface intersection homomorphism kappa_H is the negative of mu_H, and for a smooth curve C in the surface, mu_C is exactly `r^vee lambda_C r`. This establishes the signs of both diagonal and off-diagonal blocks in AM.7.

2. If H is ample, sufficiently large n gives a smooth connected C in |H^n| and H1(V,H^-n)=0 by surface Serre duality and Serre vanishing. The divisor sequence makes H1(O_V) to H1(O_C) injective. Passing to the tangent space of the reduced connected Picard variety preserves this injection; a positive-dimensional kernel would have positive-dimensional tangent space. Thus restriction has finite kernel, without asserting that the full Picard scheme is reduced. The pullback of theta is ample, so n mu_H is a polarization. The argument works in characteristic p and does not require a Hodge-theoretic Lefschetz theorem.

3. I expanded AM.8 independently. Its diagonal from the first term is minus a_i squared times mu_Ni minus the sum of a_i a_j mu_Ce. Each edge difference map adds precisely the corresponding positive diagonal term and negative off-diagonal terms. The double-curve terms cancel on the diagonal, leaving the weighted blocks of T^vee Lambda T. Disconnected double curves are correctly treated as separate edges, and triple points introduce no additional codimension-two cycle in this calculation.

4. After one common positive multiple, the right side of AM.8 is the pullback of an actual product of positive theta powers. The restrictions to the chosen ample curves already have finite kernel, hence the full map to the product of Jacobians has finite kernel. Its image is closed, and pulling an ample line bundle back through a finite morphism is ample. Thus the composite is a polarization and Lambda is an isogeny. This conclusion retains possible inseparability; no inverse to an inseparable morphism on schemes is asserted.

5. Each exceptional Picard class is represented by an actual normalized Poincare family on E_i times a smooth proper connected curve through the two required points of A_i. Such Poincare bundles exist here because the smooth projective component has a k-point. Its divisor cycle is pushed into the fixed regular Z times that curve. The previously proved EP comparison therefore puts theta(Pic0) inside the actual proper-perfect relation group J_K. This step does not push a perfect complex from E_i into the singular union E, and does not replace a family by pointwise surjectivity.

6. Surjectivity of an isogeny on k-points over algebraically closed k gives the claimed full component-Albanese image. The exceptional Picard classes have zero component degrees. For the final denominator, if j+q is Albanese-zero, choose u in the common subgroup U with alpha(u)=alpha(q); then j+u and q-u are separately Albanese-zero and remain in their respective denominator subgroups. This proves the equality of the residual denominator, rather than merely surjectivity of one quotient map.

The result removes component Albanese coordinates only. Component Albanese-kernel cycles and SNC family compatibility remain. The every-characteristic polarization calculation is not used to enlarge the positive-characteristic algebraizable ordinary-Chow scope inherited from C.3bm.

## Fresh primary-source inspection

- Milne, J. S. (2021, June 12). *Jacobian varieties*. Official corrected author PDF, https://www.jmilne.org/math/xnotes/JVs.pdf . I opened the full official PDF, read Proposition6.1 and its complete proof on authorpp19–20, and visually read the retained image of authorp23 containing Lemma6.9, its complete proof, and Remark6.10(c). The minus sign is explicit in the primary statement. The current title page dates the version and says original numbering is unchanged. This is not a claim to have freshly read every page of the chapter.
- Stacks Project, Lemma30.17.2, Tag0B5V, https://stacks.math.columbia.edu/tag/0B5V : full statement and proof freshly read; only the finite-pullback ampleness direction is required here, on the closed image.
- Stacks Project, Lemma30.17.1, Section30.17 Tag01XO, https://stacks.math.columbia.edu/tag/01XO : full criterion/proof freshly read. The cohomology application is to omega_V tensor H^n followed by Serre duality.
- Stacks Project, Lemma45.8.3, Tag0FH7, https://stacks.math.columbia.edu/tag/0FH7 : full proof freshly read. The lemma's formal conclusion is divisibility; the prescribed-point smooth connected Bertini construction occurs in its proof and is the part used here. No extra prime-to-p divisibility conclusion is imported into the matrix argument.

Primary retrieval refs in this review: `turn441265999view0`–`turn441265999view3`, `turn758453941view1`. Local sign image: `../frobenius/sources/Milne_Jacobians2021_p23.png`.

The previously audited EP/C.3bm comparison, Picard–Albanese duality, and rational Chern comparison are reused in their already stated scopes. No claim of a new full primary opening of their complete foundational references is made in this short additional audit.
