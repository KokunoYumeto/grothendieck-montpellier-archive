# A.2: further normalization investigation

Started 2026-11-20 03:51 UTC. This is research in progress, not a checked addition to the paper or outcome table.

## Candidate: nonnormal semilocal models of a quasi-excellent strictly local field

Let B be a quasi-excellent strictly henselian Noetherian local domain, p a unit, d=dim B, and K=Frac(B). The checked Mori–Nagata argument puts B inside the normalization Rbar of every Noetherian model R of K, even if Rbar is not finite or Noetherian. The checked finite-type birational B-approximation argument actually bounds cd_p(T) by d for any intermediate ring B⊂T⊂K, without requiring T Noetherian: it is a filtered union of finite-type birational B-algebras, and étale cohomological continuity applies.

Thus, whenever Spec(R) has a nonempty geometrically unibranch open, its normalization over that open is a universal homeomorphism, giving the same bound for all affine subopens. The generic lower witness then supplies the full A.2 quantifier. Stacks Tag0GIQ, currently Lemma29.55.12, was opened and its proof read at03:52 UTC. The universal-homeomorphism claim does not require finite normalization.

If R is semilocal with maximal ideals m1,…,mr, put C=∏ completion(R_mi). This is a Noetherian faithfully flat R-algebra whose minimal-prime quotients are complete local domains and hence Japanese. EGA IV1, Chapter0, Proposition23.2.4(ii), printed p218, then gives a finite birational R-subalgebra R1⊂Rbar such that Spec(Rbar)→Spec(R1) is radicial. Since it is also integral and surjective, it is a universal homeomorphism. Choose one a≠0 with R1[1/a]=R[1/a]. The normalization over this principal open is therefore a universal homeomorphism. This would prove the candidate for all semilocal models, in every dimension, and not only the previously checked normal or surface models.

The exact EGA primary text is stored at sources/EGA/EGA_IV1.pdf and .txt. Proposition23.2.4 and Corollary23.2.5 were read through their proofs. Corollary23.2.5 gives the local version directly; the finite-product completion argument supplies the semilocal version. Independent audit was requested from PartC. Nothing is promoted to the checked paper pending that audit and a complete written comparison.

## Boundary of the route

This does not yet handle arbitrary Noetherian models without a dense geometrically unibranch open. One cannot silently replace the finite product of completions by a product over infinitely many maximal ideals: that product need not be Noetherian, so EGA23.2.4 would not apply. Nor does local existence of a finite subalgebra imply that one finite subalgebra works globally. Searches for a global topological normalization theorem were initiated; no such theorem has been accepted.

Primary search locators opened: https://stacks.math.columbia.edu/tag/0GIQ. A publisher PDF for a Kollár paper on variants of normality returned403 and was not read or used. Search phrases included “geometrically unibranch dense open noetherian” and “noetherian normalization finite universal homeomorphism local”.

At03:52 UTC, PartC reported an independent proposed-proof audit after reading EGA0.23.2.4–5 and the actual checked approximation fragments. It found no gap in faithful flatness of the finite product, Japanese minimal-prime quotients, the radicial integral surjection, the single localization, or the non-Noetherian normalization continuity step. The full statement will be written and integrated after the scheduled checkpoint05; the checked paper remains frozen for that checkpoint.
