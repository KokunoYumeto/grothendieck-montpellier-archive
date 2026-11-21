# A51 finite-matrix/rationality supplement: whole-proof review

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH `/root/row_audit`.

**PASS, targeted proof check of the entire source**
`work/gt_certificates/positive_rank_theta/A51_FOX_RATIONALITY_SUPPLEMENT.tex`,
SHA256 `ef80c2a2f4e124d439d529d385639ab640c40bece4c910ccdb605f429bfd985c`.

No mathematical correction is requested. This review covers the full two algebra proofs and the written scope comparison. The primary readings are limited to the exact passages listed below; no claim is made to reprove the long cited literature theorems.

## Complete algebra checks

The averages e_a are compatible even at the transition n=a: the next-level average maps to1. Their character evaluations give the conductor idempotents, and only finitely many survive at each level. The arbitrary coefficient sum and its inverse are therefore legitimate elements of the inverse-limit algebra. On the conductor-a component, the ordinary cokernel exponent is p^{b_a}.

For the semilinear version, the coefficient action fixes each conductor idempotent. After a finite unramified splitting extension, each character orbit is a weighted cyclic permutation with common weight c_a. Eliminating successive generators gives the single relation1−c_a^{d_a}. The displayed lifting-of-exponent argument is valid also atp=2 because b_a≥2; unramified extension preserves the exponent. This proves exact exponent p^{b_a+v_p(d_a)}. The construction is explicitly abstract and asserts no weight, polarization or geometric realization.

For the rational-function lemma, normalization of numerator and denominator gives nonzero reduced Laurent polynomials. Multiplication by monomials preserves values' valuations at roots of unity. A primitive ell^a root has unchanged residue order and minimal polynomial degree ord_(ell^a)(p^s), so it is not a zero of either reduction once that degree exceeds their fixed bound. The degree tends to infinity by the stated finite-set argument. Thus the valuation is eventually the single constant mu. For an integral fixed matrix, the sum of elementary-divisor valuations equals that determinant valuation, giving a uniform exponent bound. The actual geometric identification remains an explicit missing hypothesis.

## Exact integral source issue

I directly read Asvin's complete Lemma11 statement/proof in the retained primary `fox_probe_sources/asvin2023.txt`, lines334–350, and the paper's initial conventions. The statement has no genus-at-least-two restriction. For [ell]:E→E, both the induced pullback on integral H1 and the covariant Tate-module map are multiplication by ell, with cokernel(F_ell)^2. Their rational versions are isomorphisms, but the natural integral images are not saturated. Thus the note accurately identifies the false inference from surjectivity of the abelian-variety map to surjectivity on integral Tate modules. It does not claim that all later abstract statements in the paper are false.

The retained primary PDF is `work/gt_certificates/positive_rank_theta/fox_probe_sources/asvin2023.pdf`; publisher URL https://msp.org/ant/2023/17-12/ant-v17-n12-p03-p.pdf . A fresh web open returned no readable lines (`turn905874079view0`), so the complete locally retained primary text was used rather than claiming a successful fresh web text retrieval.

## Other exact source passages checked

- Esnault–Shusterman–Srinivas: profinite generation/presentation definition, Theorem1.1, and the prime-to-characteristic surface presentation distinction onpp2–4.
- Shusterman: complete Theorem1.1 and Corollary1.2 statements and surrounding scope onpp1–2. The full theorem proof was not reread here.
- Kodani–Morishita–Terashima: Proposition4.3.4's infinite-sum formula and its displayed Fox/Gassner computation passage. No whole-paper audit is asserted.
- Asvin: Lemma17 statement, Section3's explicit coefficient-prime convention and return-product setup, and the Section3.3 polynomial-truncation paragraph. The long congruence theorem proofs were not audited here.
- Sinnott: complete Section1.16 rational-measure definition and Theorem3.2 statement, with its unit-group support hypothesis. The theorem's long proof was not reread in this review.

These passages were read from the retained primary PDFs' extracted texts in `fox_probe_sources/`. Their definitions and hypotheses support the narrow comparisons in the supplement. The new complete algebra proofs do not depend on the questioned integral geometry assertion.

No finite-curve enumeration, actual tower, completed geometric Frobenius matrix, or new main-gate movement is claimed.

## Final wording-only delta

The final source SHA256 is `5d23ca9743c256c0226e6c37382bf9edd15fcea75b24beaba5b69db1f83a4fa7`. I checked the sole change: the questioned implication is now described as coming from a surjective map of abelian varieties, rather than an isogeny. This matches the primary Lemma11 proof exactly. It leaves the explicit elliptic isogeny counterexample and both algebra proofs unchanged. This is a narrow final-delta check, not another whole-proof reading.
