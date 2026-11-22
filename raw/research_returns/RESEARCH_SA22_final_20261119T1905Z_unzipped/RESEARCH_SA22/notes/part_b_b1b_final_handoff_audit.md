# B.1(b): final editorial and source-scope handoff audit

19 November 2026, 18:11:53 UTC; GPT-6 Astra, OpenAI, agent `part_b_cycles`.

**Outcome: no concrete discrepancy found.** The active theorem, report generator, generated report, contributor and aggregate results, and both bibliographies consistently identify the all-invertible-prime abelian-fourfold conclusion as a checked deduction using Broe's 2026 preprint. They do not attribute it to Ancona alone or present this work as an independent audit of the entire preprint proof. No edit is requested.

## Current deliverable cross-check

| Item read | Exact current locator | Assessment |
|---|---|---|
| Conventions and theorem | `sections/part_b.tex:4–11,174–196,199–249` | Rational cycle coefficients and geometric `Q_l` cohomology are explicit. The theorem covers abelian fourfolds over any field with `l` different from its characteristic. Its heading says “Known with checked deduction from a 2026 preprint”; lines 206–215 name Broe's theorem and the finite-field input. |
| Equivalence distinctions | `sections/part_b.tex:145–171,174–196,210–215,238–249` | Homological primitive positivity is distinguished from positivity after quotienting by numerical equivalence. The displayed radical example refutes an inference, not standard conjecture D. Rational=numerical is used over finite fields; the arbitrary-field conclusion is numerical=geometric homological, not rational=numerical. |
| Report generator | `code/root_reconcile_report.py:31–32,61,76–77` | Explicit Broe preprint qualification accompanies the all-prime result. The exact conditional method criterion and the separate geometric examples are not described as a proof of D for every positive-characteristic fourfold. |
| Generated report | `RESEARCH_SA22_report.md:32,34–35,77,821,829–830,1300,2353–2355` | Matches the generator and maintains the published Ancona versus Broe-preprint distinction. Its later source-read note explicitly disclaims full-proof verification. |
| Contributor results | `checks/part_b_results.csv:4–8` | The abelian row says “Known with checked deduction from 2026 preprint”; its dependency and notes name Broe and distinguish Ancona's infinitely-many-primes theorem. The characteristic-zero and conditional-method rows remain separate. |
| Aggregate results | `RESEARCH_SA22_results.csv:93–96` | The normalized status “Known” at the abelian row is accompanied by explicit Broe dependencies, preprint language and the retained contributor status detail. The aggregate theorem text includes rational coefficients and the invertible-prime condition. |
| Contributor bibliography | `sources/part_b.bib:7–12,21–25` | Ancona is the published 2021 article; Broe is an arXiv 2026 miscellaneous/preprint entry. The note specifies the actually checked statements and disclaims an audit of every part of the proof. |
| Assembled bibliography | `RESEARCH_SA22_references.bib:468–473,482–486` | Same source descriptions and qualifications as the contributor bibliography. |

## Original passages reread for this bounded check

- **Broe**, original saved author source `sources/broe/TateAbelianFourfold.tex:240–260,778–799`: Theorem 1.1 gives the finite-field Tate statement in codimension two with `Q_l` coefficients for every invertible prime; Corollary 1.2 and Corollary 8.2 give D over arbitrary fields. The paragraph at line 781 expressly fixes rational cycle coefficients for equality of equivalence relations. Corollary 8.1(i) is the finite-field rational=numerical input. Remark 1.3 distinguishes the two positivity formulations. Original identifier: [arXiv 2608.28651v1](https://arxiv.org/abs/2608.28651v1).
- **Ancona**, original saved author source `sources/ancona/fourfolds_2020.tex:369–417,438–461,490–530,570–589`: the conventions require invertibility of the realization prime; Conjecture 3.10 is positivity on numerical primitive classes; Proposition 3.11 and Corollary 3.12 distinguish the homological radical and semipositivity; Theorem 3.18 gives the positive-characteristic Hodge-type result; Corollary 3.19 transfers equality from a specialization; Theorem 3.20 asserts equality for infinitely many primes. The characteristic-zero Hodge–Riemann statement is separately discussed at lines 525–530. Original identifier: [arXiv 1806.03216v3](https://arxiv.org/abs/1806.03216v3).

This review read the relevant original statements and active wording. It did not recheck the full proof of Broe's Tate theorem, rerun finite computations, make new external requests, or change any theorem status. Only this note and its audit event were added; no TeX, bibliography, report generator or aggregate file was changed. Exact locators refer to the active files at the audit time and may move during later assembly.
