# Component extension and framework: independent scope review

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict

I read both `KTOWER_work/sections/component_extension.tex` and `KTOWER_work/sections/framework.tex` in full. The component extension is a valid consequence of the carried K17 control and full-domain Soulé-index results together with the completed K52, K56 and K60 vanishing theorem. The original framework review below records its earlier snapshot; the new component section was reread in full after the final e30 reports passed. The framework's arithmetic indices and distinctions between integral, rational, pro-p, prime-to-p and full profinite realizations are consistent with these conclusions.

This is a whole-proof audit of the new component corollary and a scope/implication audit of the framework. I read the full relevant carried K17 arguments identified below. I did not re-prove their imported Iwasawa, arithmetic comparison, or cyclotomic-index theorems, and did not independently recheck every historical source locator in the framework. No kernel verification is claimed.

## Full carried arguments read

All K17 line numbers refer to `input/RETURN_K17_checkpoint_08_20261121T0616Z/K17.tex`.

| Carried result | Lines read | Role |
|---|---:|---|
| Exact comparison (K1)–(K3), including the complete character/Nakayama argument | 684–752 | K4k primary vanishing is equivalent to vanishing of the single even class component with exponent -2k. The assertion is periodic vanishing, not periodic group order or group isomorphism. |
| K17-TWELVE-DEGREES-PERIOD, complete statement and proof | 7082–7114 | Supplies the full old representative interval [-16,12], finite-layer and inverse-limit vanishings, and ramified integral freeness. |
| VK-SOULE, VK-SOULE-INDEX, VK-SOULE-NORM, complete proof and normalization discussion | 8377–8479 | The full cyclotomic kernel has index exactly the relevant finite K-group order for odd primes and odd weights at least3. |
| K17-COMPONENT-CONTROL, complete statement and proof | 10975–11082 | Base-layer vanishing kills every finite-layer component and the inverse limit. For nonexceptional even theta, the actual ramified component omega times theta inverse is integrally free of rank one. |
| K17-ODD-COMPANION-EXCLUSION, complete statement and proof, and explicit extension paragraph | 11084–11141 | Handles the exceptional odd characters omega and omega inverse and explicitly permits any further proved K-degree. |

## Component corollary: exact deductions

1. K52 corresponds to j=13 because 4j=52; K56 corresponds to j=14. Therefore (K2) supplies A0^[-26]=A0^[-28]=0 at each odd prime. Adjoining these two positive representatives to the carried interval gives exactly [-16,14]. No inference about a negative-degree K-group is needed.
2. If k is congruent to j modulo (p-1)/2, then -2k and -2j are congruent modulo p-1. They select the identical Teichmüller character. Consequently the base-layer component vanishing and (K2) give K4k{p}=0 for positive k. The k=0 K-group is never asserted to vanish.
3. The carried norm/coinvariant control applies to this exact even component. Hence A_n^[-2k]=0 for all n and X^[-2k]=0. No interchanging of unrelated characters or exactness assertion about inverse limits is required.
4. Substituting theta=omega^(-2k) into omega times theta inverse gives precisely omega^(2k+1). For p>=5, the nonexceptional control implication gives integral Lambda-rank-one freeness. The two exceptional characters are exactly omega and omega inverse and are covered by the separate Coleman calculation. No ramified freeness is claimed at p=3.
5. At weights m=27 and29, the index formula has degrees 2m-2=52 and56. Both orders are one. This proves surjectivity of the stated full-domain Soulé characters at every odd prime, in the cyclotomic-product normalization (K19). It does not prove a unit image on a deeper filtration subgroup.

The phrase in the corollary about the same F_p eigenspace is sufficient via the carried mod-p/Nakayama comparison. It could also be stated directly as the same Teichmüller character/idempotent over Z_p, because the exponent congruence itself is integral. This is an exposition option, not a missing implication.

## Framework arithmetic and scope

- With e positive even and m=e+1, the integral edge comparison has K-degree2e=2m-2. Its strict dual has twist1-m=-e. Thus the displayed integral H2 and strict negative-twist H1 groups have the correct indices. The new weights are27 and29, and the pending K60 weight is31.
- Rational mixed Tate Ext formulas do not retain finite integral K-groups. The text correctly avoids turning rational Ext2=0 or free graded rational Lie algebras into an integral torsion-vanishing theorem. The modern integral comparison is kept distinct from a factorial-normalized Chern character.
- The geometric-Frobenius convention gives the target trace terms from Q_l(-e), Q_l and Q_l(e). It remains separate from the purity of the normalized automorphic source systems; purity does not exclude residual congruences.
- The K0/exterior-power and line-bundle language is not used as an argument for vanishing of higher K-groups. The negative special value L(-2e,chi_D) uses B_(2e+1,chi_D), whereas the reflected rational class component uses the different ordinary Bernoulli number B_(l-1-e).
- The geometric comparison keeps the full profinite Teichmüller action, an arithmetic pro-p tripod action, a maximal geometric prime-to-p quotient, and rational unipotent realizations separate. The stated counterexamples therefore do not purport to contradict the characteristic-zero full profinite formulation of the Faltings letter.
- The crosswalk retains the remaining all-weight zero and Ihara/cubic gates. Selected component vanishing does not exhaust the characters at arbitrary large primes. The explicit quartic size bound likewise supplies no all-weight zero result.
- The framework's existing phrase “the endoscopic construction, when checked” is now conservative but stale: the injection has passed the independent review recorded in ENDOSCOPIC_REVIEW.md. Its all-weight converse remains a separate question.

## Completed e30 update

At 16:26 UTC all three e30 requirements passed the independent report reconciliation. I subsequently read the entire updated component_extension.tex: its j=13,14,15 extension gives exactly [-16,15], and its full-domain Soulé weights are27,29,31. The new K60 degree has the same exact character and control argument, with no new exceptional-character issue. This updated component theorem passes the whole-proof review. The root author owns both section updates; this review has not edited either root section.

At this reread the framework file still contained its earlier pending-e30 wording and interval[-16,14]. Those are integration-status updates, not failures of the arithmetic deductions. I sent the exact stale passages to the root author. The detailed list above describes the originally reviewed framework snapshot; its status should be read with this completed update.

## Reviewed file snapshots

- `sections/component_extension.tex`: SHA256 `aad0a13e92ffc4cb452a18951424997a8e51e16b406d24babc0b8c1045aaa9e8`.
- `sections/framework.tex`: SHA256 `3400be0a68ca0523e7d637c07afe1aab72072a7a119b35ba777956245741af49`.

Updated component snapshot SHA256: `e3dc6d2733d75b7d3f08716c48fe9ff8b3ea7cfb0ad507d0ebb69e201998845a`.
