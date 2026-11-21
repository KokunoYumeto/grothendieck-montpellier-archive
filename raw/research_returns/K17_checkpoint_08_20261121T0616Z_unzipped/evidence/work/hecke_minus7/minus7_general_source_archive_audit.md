# Independent whole-proof audit: uniform alternate-field criterion

**Verdict: PASS, under the stipulated arithmetic source theorem and the full-space determinant hypotheses explicitly stated.**

Reviewed in its entirety: `work/hecke_minus7/minus7_general_source_section.tex`, proposition K17-MINUS7-GENERAL-SOURCE. Reviewed SHA-256: `d6882197e06d8f400e765ebf8507f22f7181302f54c5cfcd05988abfd13c1b7c`.

Actual reviewer: GPT-6 Astra Pro, run `/root/archive_kummer`, 2026-11-21. This records a mathematical/source-interface audit, not a new Lean execution or a new determinant calculation.

## Scope and datum

The quantifiers are even integers `e >= 2` and primes `ell > max(2e+1,7)`. They imply `ell-1 > 2e`, hence the source's nondivisibility condition, while excluding the discriminant prime 7. The field, class number, modulus, trivial character, and parity checks from the fixed-weight lemma remain valid. The condition eta is correctly checked by ramification at 7. The direct OneCharU_s statement permits geometric Frobenius above 2 even though N=2; no restrictions from the separate counting theorem are imported.

## Rank-three family

The source retains Adm3Alt, Unl, and the literal level witnesses. Triviality of KillsMu 2 characters and the common cyclotomic twist give weights `(e-1,-1,-e-1)` at modulus one. Keep.levelKA_alt gives infinitesimal character `(e,0,-e)`, so the compact highest weight is `(e-1,0,1-e)`. Regularity holds throughout the stated range, including e=2.

The global packet argument depends on rank, conjugate self-duality, sign and regularity, not on e=16. The three infinity characters remain distinct and conjugate-orthogonal. The same generic pure-inner multiplicity theorem and odd-rank temperedness theorem apply. Triviality of the central character follows from the unchanged class-number-one argument. The ramified-7 local construction depends only on a unitary unramified root u and covers every such root, including the nontrivial quadratic case. No omitted supercuspidal q restriction becomes relevant at another weight.

The source/Satake identity is `tr rho(s) = alpha/2^e`, with alpha an eigenvalue of `2^(e-1) T_2`. The exponents are correct: the usual rank-three positive minuscule operator contributes the factor 2, independently of the coefficient weight. The previously proved full-space conjugation between minuscule directions is also independent of bidegree.

## Rank-two family

The fixed conductor proof uses the weights only through `2e+1` and the coefficient-prime slope gap `2e`. For e even and at least 2, the weight is odd and the gap is at least 4. Thus the full Saito compatibility and exact potentially semistable functor argument still give N=0 at ell; a nonzero monodromy operator would require slope gap one. Finite inertia with trivial graded characters is trivial in characteristic zero. The argument does not silently replace full Weil--Deligne compatibility by semisimplified compatibility.

At 7, both global mod-7 inertia characters remain allowed. Twisting one off preserves cuspidality and weight. The determinant character remains odd under a square twist; hence the remaining ratio is nontrivial and odd, and the twisted primitive form has conductor exactly 7. This covers original conductor-49 cases. Untwisting at 2 yields one of the three values in mu_3. The trace formula is therefore `1 + zeta a_2(f)/2^e` for the full weight-`2e+1` level-seven space.

## Determinants, coefficient extension, and conclusion

Multiplying the two comparison-trace differences by the ell-adic unit `2^e` gives precisely the two expressions displayed in the proof. Integral Hecke lattices imply integrality of every eigenvalue after finite coefficient extension. A unit determinant therefore makes every individual factor a unit. The identity involving `t_0^3 I - T_2^3` covers all three possible twists, with no eigenvalue selection or multiplicity replacement.

The proof applies the recovered direct unit theorem to both complete source families. This kills the source Selmer group over Q. The auxiliary imaginary quadratic field is not incorrectly made the Selmer base field. Faithful coefficient extension preserves and reflects zero. The unchanged local-2 condition is automatic because multiplication by `2^(-e)-1 != 0` is onto the divisible coefficient module. Formula (K5), with e even, gives the stated `K_(2e)(Z){ell}=0`.

## Checks actually performed

Read the entire new proposition and proof. Freshly reread the complete fixed-weight source coverage section and complete level-seven GL2 proof, the direct unit source lemma and its assembly proof, and the entire strict-duality/local-condition proof of (K5). Reconstructed every weight-dependent substitution and both determinant implications. The previously logged primary-source audits supply the unchanged KMSW, Shin, Adler--Lansky, Saito, Carayol, and Colmez--Fontaine inputs. No new primary theorem or numerical calculation is needed for this generalization.

No mathematical correction requested. A purely expository improvement would be to declare O explicitly as the valuation ring of a sufficiently large finite coefficient extension at each place; the intended meaning is already unambiguous from the fixed-weight criterion and the phrase “at every coefficient place above ell.”
