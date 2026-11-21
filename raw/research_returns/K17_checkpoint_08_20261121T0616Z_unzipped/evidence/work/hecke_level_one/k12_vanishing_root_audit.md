# K17-K12-VANISH — root complete proof audit

Date: 2026-11-21 04:27 UTC. Model: GPT-6 Astra Pro; effort not exposed; run K17 root.
Verdict: PASS after complete proof readback and primary-source checks.

## Whole proof and source scope

Read the entire final conductor section and K12 vanishing section, including the periodicity corollary, twice after authoring. Read the complete final direct-unit/source-U3 interface, complete KeepLevel and FOneCharU source proofs, final U3 coverage proof, final U3 finite-model proof, full classical GL2-model proof, and both standalone finite certificates. The source predicates retained are Adm3U_s and Adm2A; no old trace-product divisibility is assumed.

For the conductor bridge, read Carayol section0.3 and sections0.5–0.7/TheoremA pp409–411; read Saito's entire survey section2a–c and visually inspected pages8–9 with Theorem3; read Colmez–Fontaine section3.3 p21, Proposition4.2 p23, and Proposition4.4 with its complete rank-one proof p24. The classical coefficient-prime compatibility is explicitly a full Weil–Deligne assertion, including monodromy. A larger Fontaine2004 PDF was also retrieved, but it was not needed for the cited comparison chain. Original Saito1997 publisher full text was not recovered; the precise same-author theorem statement is used instead.

The ordinary local flag yields two crystalline character slopes separated by2e. Exactness and N lowering slopes by1 force N0; finite inertia with two trivial graded characters is trivial. The odd nebentypus has conductor dividing3 and is chi_-3. Exactly one tame inertia character at3 is nontrivial, so primitive conductor3 and the geometric trace normalization follow.

The U3 coverage and finite-model proofs have independent archive and vandiver whole-proof audits. The full GL2 model has independent archive author and tripod audits. Archive independently read the final conductor and K12 chain and reported PASS. No Lean build or external referee review is claimed.

## Exact arithmetic replay

Reran u3_orbit_certificate.py and gl2_weight13_certificate.py. Independently multiplied the U3 comparison factor by the GL2 characteristic value and compared with the displayed prime-power product:

    N7 = 36703455074769833036351681539319447519232
       = 2^15 3^19 7 13^5 37 43^3 47^3 61 271^3.

All primes above2^31 therefore have unit differences in both complete admissible branches at7. Source GD for e6/N2/E=Qsqrt(-3) is exactly the prior checked specialization. Finite source Selmer length is zero by the retained OneCharU_s inequality; strict arithmetic duality identifies its dual with K12 primary part. Published Vandiver covers odd primes below2^31, and Rognes–Weibel covers2. Finiteness concludes K12=0. Periodicity and full-domain kappa7 index are applications of previously checked exact comparison statements, not claims about restricted weight-subgroup primitivity.

## Reviewed final files

- gl2_conductor_section.tex: SHA256 `6419cf200c28a8ffff42aaf7778049c86a60e3f265a67767db1947632c1671c3`
- gl2_conductor_bibitems.tex: SHA256 `90ff482fb0cf3cc206814ecb2e7912d06fb22a62f63a09df2f1112fe796b5eda`
- k12_hecke_vanishing_section.tex: SHA256 `98eaa9733c5ac311b988ed491fb19a179cba9f5d27d46a93cccc2594bb28fa9c`
- u3_hecke_section.tex: SHA256 `454170ba09eefab28c1a717e28559e5050de7c738df8acb30a654178444b6087`
- gl2_weight13_section.tex: SHA256 `8465519484928cd1ddf09f9532cc139a6accc5fd5a19afb6440fa336960b7188`
