# Direct generated-fragment review: F20 and F24

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026.

## F20

Read the complete statement, ordinary Satake proof, GL2 determinant example, framework paragraph, and complete motivic refinement in `finding_F20.tex`, SHA256 `df8b106756b17e5fa86c21552aeeaa0572109097eca2edc052b0bc5abde387a4`. **PASS.** The fragment was a verbatim substring of main source SHA256 `ca83a1cdde354ddd82bc7ec1ae42dac5a58d8d7ca8acc64d0512cb83af466690` at this check; this is not a claim to have reviewed every other part of that main-source revision.

The natural unnormalized Weil IC has weight `D_mu`, the twisted IC is normalized arithmetically on its dense open orbit, and proper pushforward retains complex weight while Satake supplies perversity. The cited Richarz published numbering and BBD second proof of 5.3.2 / Remark5.4.9 agree with the earlier checked primary statements. The corrected symmetry is defined over the finite field, the rational Young idempotent is primitive, and the rank-one Specht projection gives the asserted Schur functor rather than its Specht-dimension multiple.

The canonical geometric Hom decomposition carries conjugation Frobenius and gives weight `dD_mu-D_lambda`; it does not assume arithmetic semisimplicity. When invoking `j*=j!`, the open stratum is understood as open inside the support of its isotypic IC summand. Adding those words would make the ambient/support convention maximally explicit. The product-group Kronecker weight and all dimension restrictions are correct.

For the GL2 example the source dimension is two, the central convolution fiber is P1, and stalk degree zero is H2(P1). The positive-dimensional open IC has no H0 stalk at the boundary point by strict intermediate extension. Thus the determinant multiplicity is Q_l(-1), and the corrected Satake swap acts by minus one. This excludes a permutation basis in that line while leaving geometric realizations intact.

The motivic refinement uses precisely the semisimple, convolution-stable rational Satake subcategory and realization-compatible symmetry already source-checked in Richarz–Scholbach. Purity forces every coefficient motive at lambda to be 1(-h), with `h=(w-D_lambda)/2`. For plethysm the cancellation of total sizes gives `h=n(lambda)-d n(mu)`; for the product standard-input construction it gives `h=n(lambda)+n(mu)`. Realization is scalar geometric Frobenius q^h. The fragment correctly distinguishes the coefficient motive from the potentially vanishing untwisted motivic Hom vector space. This is a theorem for these specified natural motivic objects, not an inference that an arbitrary pure Weil module is Tate or semisimple. No new proof of the cited general Satake/BBD theorems is claimed.

## F24

Read the complete updated generated statement, full signed-even proof, powered-extension paragraph, and both countermodels in `finding_F24.tex`, SHA256 `4079cab04eec46d08b39ecd648cbef0b5543a611515b2f77d2551673f09fafd1`. **PASS.** It too was a verbatim substring of the same main source hash at the check.

The previous full independent audit is in `agent_signed_even_full_review.md`. The updated fragment agrees mathematically with that checked argument. The complex-i countermodel now uses `k>=6`, `k=2 mod4`, so its two positive output roots are distinct and the former k=2 multiset notation issue has disappeared. Grouped real coefficients, nonvanishing by Vandermonde, retention of a positive top coefficient for even powers, lower-radius exclusion, error exponents, all-embedding qualification, and powered top-spectrum visibility remain correct. The trace-zero mixed-degree example appropriately limits conclusions to visible roots.

## Derived note self-check

Read all of `agent_rankone_derived_gate.md`, SHA256 `57a0b7ed5bd25f177d3874c1e985d4878fbafb007e5cd65567a243269a400b08`, after making the monoidal-category/unit hypothesis explicit and replacing arbitrary-module 'vector bundle' wording by quasi-coherent sheaves, with finite-projective and field-specialization cases stated separately. The four-point model preserves actual character actions after the stated localization; the inherited KL cone and the character cone are different. The exact-amplitude lemma and its separate scope, the explicitly constructed zero-differential model, and the finite inverse-trace pole proof all check. This is an author self-check, not a fresh independent review of that note.
