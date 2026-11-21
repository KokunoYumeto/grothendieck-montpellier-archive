# Intake audit: source register and check scope

Date: 21 November 2026, Europe/Berlin. Agent: GPT-6 Astra Pro,
run `ZETA_TWO/intake_audit`; reasoning effort is not exposed in this session.

## Primary sources opened

These sources were opened through web retrieval or the local PDF copy recorded
below. Citations in the paper use bibliographic statement locators, not web-tool
reference tokens. The parent should reopen web sources it cites in chat.

| Short name | Exact locator used | URL |
|---|---|---|
| LLS | arXiv:1309.3595v3; Theorem 1.5 pp.3–4; Corollary 1.1 p.2; Corollary 1.2 p.3; Corollary 1.3 p.4; eq.(1.3) | https://arxiv.org/pdf/1309.3595 |
| IMS | Ihara–Murty–Shimura, *On the logarithmic derivatives of Dirichlet L-functions at s=1*, Corollary 3.3.2, eq.(3.3.3), p.9 | https://www.kurims.kyoto-u.ac.jp/~kenkyubu/emeritus/ihara/Publications-and-Recent-Preprints/RecentArticles/pdf-files/4A.pdf |
| HJM | Habegger–Jones–Masser, *Six unlikely intersection problems in search of effectivity*, eq.(5.9), Lemma 14(i), printed p.22, PDF p.23 | https://pure.manchester.ac.uk/ws/portalfiles/portal/36388863/final.logged.pdf |
| Wei | *Smallness of Faltings heights of CM abelian varieties*, arXiv:2111.00617v1; definitions p.2; Theorems 1.3/1.4 pp.4–5; Corollary 4.3 eq.(13) p.14; Proposition 4.7 p.17; proof of Theorem 1.3 and Theorem 4.8 p.18; Proposition 5.3 pp.19–20 | https://arxiv.org/pdf/2111.00617 |
| Delfs–Galbraith | arXiv:1310.7789; geometric count p.1; rational supersingular j-count equation (1), p.2 | https://arxiv.org/pdf/1310.7789 |
| Miller | *Real cyclotomic fields of prime conductor and their class numbers*, arXiv:1407.2373; Theorem 1.1 p.1, unconditional p≤151 clause only | https://arxiv.org/pdf/1407.2373 |
| Thakur | *Fermat's last theorem for regular primes*, in the *Cyclotomic Fields* lecture collection, printed p.172 / PDF p.179, displayed relative class-number formula, citing Washington Theorem 4.17 | https://www.sas.rochester.edu/mth/sites/dinesh-thakur/BPCyclotomic.pdf |
| Siviero | *Realisable classes, Stickelberger subgroup and its behaviour under change of the base field*, Lemma 4.5, equation (16), p.82 | https://www.numdam.org/item/10.5802/pmb.13.pdf |
| Ullom | *Normal bases in Galois extensions of number fields*, p.159, citing Rim, Theorem 6.24, p.711 | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CDAF1160D7312AB5A5E2D32BA8B540FF/S0027763000024521a.pdf/normal-bases-in-galois-extensions-of-number-fields.pdf |
| Sutherland | *18.785 Number Theory I*, Fall 2021, Lecture 19, Theorem 19.12 p.9 (class-number residue) and Theorem 19.15 p.11 (abelian factorization) | https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec19.pdf |
| NIST DLMF | Equations 25.15.3, 25.11.13, 25.11.18 (Dirichlet-Hurwitz expansion and special values) | https://dlmf.nist.gov/25.15 ; https://dlmf.nist.gov/25.11 |

Local copies available under `work/intake_sources/`:
`LLS_1309.3595.pdf`, `IMS_log_derivatives.pdf`, `Wei_2111.00617.pdf`,
and `Thakur_Cyclotomic.pdf`. Thakur's file exceeded the web tool's size limit,
so it was retrieved directly, extracted to `Thakur_Cyclotomic.txt`, and its
printed p.172 was rendered and visually checked as `Thakur_p172.png`.
The HJM direct download returned HTTP 403; its theorem page was nevertheless
successfully opened and visually checked through web retrieval earlier.

LLS p.4, IMS p.9, HJM printed p.22, and Thakur printed p.172 were also checked
visually using PDF screenshots. The cited theorem statements and hypotheses were rechecked;
the original full proofs of these literature theorems were not independently
reproved. IA04–IA06 were additionally checked by the independent agent
`ZETA_TWO/alpoge_special`, who reopened all three primary sources and read the
entire new proofs. That check passed, including height normalization and both
factorials in IA05.

## Bibliographic and source limitations

The original Rim paper was not opened. Its exact theorem/page locator was
confirmed through Ullom p.159, and the class-group isomorphism was opened in
Siviero Lemma 4.5. Washington's textbook was not opened; the exact formula and
Theorem 4.17 locator were confirmed in Thakur p.172. Those two results are
carried as known background with their displayed formulations rechecked.

The original full proofs behind `BRIDGE_FLAGS.tsv` are not attached. The
575-row audit is an audit of the supplied statement/context metadata, with
the original run status retained. It does not independently certify the
source status of every row. The 587 intake table records include repeated
bridge-summary occurrences and grouped row IDs; they are records, not 587
distinct mathematical statements.

Two source questions remain: the ring R in SA06 A.8c, and the exact expansion
of DS/RH in LM8_PUSH A.69. Title searches in the user's available files for
`RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z` and
`LM8_PUSH_checkpoint_17_20261116T0252Z`, followed by simpler title queries
`RESEARCH_SA06` and `LM8_PUSH`, all returned no result. This is a failed
retrieval, not evidence that no such source exists. The strongest permissible
conclusions are recorded in the TSV, without attributing an invented proof.

No original Grothendieck archive scan was attached. Therefore this subtask
has produced **no new transcription correction**. The separate
`intake_source_corrections.tsv` corrects supplied intake prose and scope;
those rows must not be relabeled as readings of Grothendieck's handwriting.

## Computation notes

The final IA07 computation uses the determinant of an explicit integer
multiplication matrix. A preliminary unreduced-polynomial resultant call
gave a sign inconsistent with the real odd character; it was rejected.
The final matrix determinant was independently computed by custom Bareiss
integer elimination and SymPy Berkowitz elimination, both giving
`-127262242448329728 = -3072*23^10`. The determinant, the full matrix, the
Bernoulli product, and the code are retained. This is an exact arithmetic
computation with a reproducible certificate, not a Lean formal proof.

The quartic CM height and the phi-related values use high-precision numerical
evaluation for illustration. Their displayed exact gamma/logarithm formulas
are the mathematical deliverables. No rigorous interval enclosure is claimed
for every printed decimal digit.
