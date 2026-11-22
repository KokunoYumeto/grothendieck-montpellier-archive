# C.3bk: source and proof-input audit

This record accompanies the final `C3_higher_product_integral_kernel.tex`, promoted and registered 2026-11-19T15:15:53.945543+00:00. The superseded draft is retained as a pointer, and its full audited content is preserved under output/C3bk_initial_audited_draft.tex. The safe dimension ranges are r=2,N≥4; r=3,N≥7; and r≥4,N≥3r−1. No broader Smith/saturation argument is used.

## Newly applied exact integral Chow input

**Qingyuan Jiang, published Cambridge version (2023), On the Chow theory of projectivizations, JIMJ 22(3),1465–1508; DOI10.1017/S1474748021000451.** Existing bibliography key `cyJiang2023` is reused, so no duplicate key is added.

Freshly opened full primary HTML and read Section1.2 conventions, Theorem2.4 and its displayed maps/proof, and Section2.3/Theorem2.8(3) and its displayed maps/decomposition. The ground field is unrestricted. The blow-up statement concerns a locally complete intersection centre; the point×smooth-factor centres here are smooth of codimension two. Applying this formula with arbitrary smooth coefficients proves the exact integral external-product ring of products of cubic surfaces. It does not assert a Kunneth formula for arbitrary projective varieties.

Primary URL: https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/on-the-chow-theory-of-projectivizations/3DA5197C99935D82CCB4E359214AF439 . Exact fresh retrievals on2026-11-19 around15:03–15:04UTC: `turn514555530view0`, `turn514555530view1`, `turn457846617view0`, `turn457846617view1`.

**Stacks Lemma42.36.2, Tag02TX.** Existing key `cyStacksProject`. Full primary statement and proof freshly reopened/read at https://stacks.math.columbia.edu/tag/02TX (`turn457846617view2`). Its integral projective-space-bundle formula gives the coefficient recursion, including all Picard torsion. No characteristic reduction is made when the ample degree is used as a positive integer.

## Earlier this-window exact primary inputs, carried forward with their scope

* Rost1996, Proposition4.1(3), Section5, Corollary6.5, Proposition8.6 and Section12, printedpp351,355–360,370,382–383; full author primary PDF and author corrections opened/read for C.3bj. The all-r generation induction is an additional proof in the present fragment, using those exact graded localization, homotopy and pullback inputs. Existing key `cyRost1996`; see `K2_cohomology_divisibility_independent_REVIEW.md` and `C3bj_SOURCE_AUDIT.md`.
* Kerz, author version29Apr2008, Definition2.1 and Theorems7.1/7.5, authorpp3,20–22; full exact proofs/standing excellence hypotheses opened/read for C.3bj. All residue fields here are infinite. In the final use of the Chow ring comparison, the line bundles and the finite rational-equivalence relation are descended to one actual smooth finite-type pointed-etale model. No Bloch formula on the nonreduced first neighbourhood is used. Existing key `cyKerz2009Milnor`.
* Braunling2013, published§3pp557–558, diagram(22), exact ring/Čech compatibility freshly read for C.3bj. This is applied only on that smooth finite-type model; the resulting Milnor class can then be restricted to the nonreduced neighbourhood. Existing key `cyBraunling2013`.
* Stacks Lemma33.47.3 **Tag0FD6** (individual lemma; sectionTag0FD4), full proof opened/read for C.3bj. Very-ampleness supplies the immersion hypothesis on every successive base locus. The m=0 endpoint uses ordinary smooth-divisor Bertini. Existing key `D_StacksBertiniUniformHigher`.
* Stacks Lemma10.131.9 Tag00RU, Definition10.138.1 and Proposition10.138.13 Tag00TN: full exact primary inputs opened/read for C.3bj. General conormal exactness alone does not claim left injectivity; the split-algebra calculation proves it here. The rank-one exterior-power kernel is elementary linear algebra. Existing keys `D_StacksConormalUniformHigher`, `frStacksFormalSmoothRelativeMilnor`.

## Prior audited inputs reused, not claimed freshly reopened for C.3bk

* Huybrechts, Cubic hypersurfaces, Chapter4 Proposition2.4, p178, all-characteristic cubic-surface blow-up description; used and independently source-checked in C.3bi/bj. Key `D_HuybrechtsCubics`.
* Illusie1972 Theorem2.6/formula(2.7.2), pp166–167, actual first-neighbourhood line-bundle obstruction; exact source and author errata checked earlier in C.3m/bf/bg.
* Brion, Commutative algebraic groups up to isogenyII, Section3.2.3 equation(3.8), authorp23, integral all-characteristic Ext classification before the later characteristic-zero restriction. This exact primary passage was independently opened by owner/root/frobenius for C.3bf.
* Ordinary quartic/Verschiebung and the actual curve-family construction are fully proved in C.3bg and repeated with the new factors in C.3bk. No universal bundle on the whole abelian variety is assumed.
* Proper formal existence, Popescu descent and smooth henselian lifting, plus Elkik1973 unnumbered Picard corollaryp573: exact prior primary inputs of C.3bf/bg/bj. The actual inverse line bundle and first-jet identification are included in finite descent data. The result concerns a fixed actual product with a proper curve.

## Finite certificate and its limits

`code/check_C3bk_higher_product_kernel.py`, complete output `code/check_C3bk_higher_product_kernel.out`, structured output `output/C3bk_higher_product_certificate.json`.

Run2026-11-19T15:10:53.456062UTC; runtime0.176992202999827seconds;91passes,0failures. It checks exact integer recurrences for r=2..12, the m=0/r=2 free-lattice determinant−12288 and primitive coefficient, the m=1/r=3 gcd(2,3) endpoint, and ordered tensor cup matrices for s=1..9. The general infinite-family proofs remain in prose. No finite computation is claimed to prove Bertini, the actual families, the sheaf comparison, or all characteristic/dimension cases.

The cycles-authored nine-case Smith calculation is independently inspected in `C3bk_exceptional_lattice_independent_REVIEW.md`; it is not used to assert any interval outside the fully proved safe range. Its newly appended general reduction after that review is a separate research input and is not part of that earlier pass.
