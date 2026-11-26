# G3: provenance, checks and literature search

Note: `G3_paper.pdf`. Title: "Multiplication by 2 and by 6 through products of Jacobians, and the Jacobian index of a very
general abelian variety of dimension 4, 5 and 6". Source: `src/G3_paper.tex`. Written 25 Nov 2026 by Claude Opus 5.5 at
effort max (agent a0012f1ff34e51fa6), on the brief `agent_notes/a0012f1f_G3_NOTE_BRIEF_20261125.md` from main session
329fb1e6 (Claude Opus 5.5 at effort max). Not posted.

## Who produced what

**Theorem A** (every characteristic):
- [2] factors through a product of Jacobians for every ppav of dimension <= 5, and [6] for every ppav of dimension 6;
- s_J divides gcd(2, δ) for surfaces and gcd(6, δ) for threefolds.

This is the run RESEARCH_SA06 of GPT-6 Astra (OpenAI, ChatGPT Pro mode), which ended 19 Nov 2026, statements C.4j and
C.4m-C.4p:
- the files are `agents/frobenius/C4_additions.tex`, `C4_prym_addition.tex` and `C4_pt6_addition.tex` of
  `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`;
- the run's own audits were done by its sub-agents `/root` and `/root/frobenius` (GPT-6 Astra, ChatGPT Pro mode);
- C.4i (s_J | (2g-1)!) is the run's re-derivation of known work, Scavia-Suzuki Prop. 3.4 and Beckmann-de Gaay Fortman §3.

**Theorem B** (s_J | m | s_J² for every complex ppav) and **Corollary C (i)-(ii)** (s_J = 2 for g = 4, 5 and 6 for
g = 6, very general):
- `MAP_GEOMETRY.md`, item NK2, by agent a5d5ce46 (Claude Opus 5.5 at effort max), 24 Nov 2026.

Due to the writer (a0012f1f, Claude Opus 5.5 at effort max), 25 Nov 2026:
- **Theorem D**: the identification of Grothendieck's second question on cote 14, scan 71 (sheet 70), for abelian
  varieties with the ideal I_J(A), and its proof;
- **Corollary C (iii)**: every prime p <= g/2 divides s_J, from Engel-Schreieder 2606.31894 and Theorem B;
- **Remark 2.3**: a second route to the evenness of s_J, via EGFS Cor. 1.5;
- the formulation of Lemma 2.2 and the text.

## Checks

All checks below are by Claude Opus 5.5 at effort max unless named otherwise.

- **C.4i, C.4j, C.4n, C.4p.** Independent re-proofs by a0012f1f, with exact computations (`check_c4.py`): the Matsusaka
  Pfaffian identity for 2d = 4, 6, 8, and the integer Lagrange identities in degrees 4 and 6.
  - Done in the SA06 full intake, round 2, 22 Nov 2026.
  - Recorded in `results_register/horizontal/sweep3/SA06/INTAKE_RESEARCH_SA06_20261121_full_CHECK_EVENTS.tsv`.
- **C.4m.** Read in full by a0012f1f on 22 Nov, including the characteristic-2 lifting route.
- **C.4o.** Checked by a0012f1f at the intake of 20-21 Nov 2026. Also used and re-read, without fault found, by the
  geometry map, 24 Nov.
- **NK2.** Second reading by a0012f1f, 25 Nov 2026: `../../CHECK_NK2.md` and `../../CHECK_NK2_CHECK_EVENTS.tsv`, 13
  events.
  - Verdict: holds, with bookkeeping repairs, which are carried into this paper.
  - The outside statements were read verbatim from text extracted by the writer:
    - BdGF 2202.05230v2 Thm 1.1-1.2;
    - EGFS 2507.15704v3 Thm 1.1, Cor. 1.2, Cor. 1.5;
    - EGFS2 2512.04902v1 Thm 1.2 and the table of Question 1.1.
- **The writing (25 Nov).** Every proof of the paper was derived again by the writer. Theorem D and Corollary C (iii)
  are the writer's own and have **no independent check yet**. Events are in `CHECK_EVENTS.tsv` (8 events).
- **Build.** pdflatex twice gives 6 pages, 0 overfull boxes and 0 undefined references or citations. The writer
  rendered all 6 pages at 80 dpi and looked at each.

## Literature search (25 Nov 2026, by the writer)

Searched:
- arXiv API:
  - all papers with author "de Gaay Fortman": 17 entries, 11 by Olivier de Gaay Fortman;
  - abstracts containing "product(s) of Jacobians": 22 entries.
- OpenAlex citers:
  - of BdGF (Compositio 2023): 13 works;
  - of EGFS, EGFS2 and Scavia-Suzuki together: 28 works.
- Hexagon (hexagonmath.org), searches "Jacobian" (34 results) and "integral Hodge" (2 results).
- Semantic Scholar was rate-limited (HTTP 429) and is not part of the search.

Opened:
- **de Gaay Fortman-Schreieder, arXiv 2401.06577** ([GFS25], Compos. Math. 161 (2025) 1404-1457; abstract): no power of
  a very general ppav of dimension >= 4 is isogenous to a product of Jacobians. It says nothing on [n] factoring or on
  split embeddings.
- **Scavia-Suzuki, arXiv 2507.09821v2.** Read through the summarizing fetch tool, not verbatim:
  - Thm 1.1: a ppav is a direct summand of a product of Jacobians iff the polarization and the minimal class are
    algebraic over k;
  - Prop. 3.4 and eqs. (3.1)-(3.3): n·(minimal class) algebraic gives [n·deg(θ^g/g!)] factoring;
  - Thm 5.2 (2)⇒(3): [n] factoring gives n^{4g}·ch(P) algebraic.
- **Engel-Schreieder, arXiv 2606.31894v1** (1 Jul 2026). Thm 1.1 and Cor. 1.2 read verbatim: primes p <= (k+1)/2 divide
  the minimal algebraic multiple of θ^k/k! on a very general ppav. There is no statement on Jacobian factorizations on
  pp. 1-3.
- **Other citers checked at their abstracts**, none relevant:
  - Milne 2509.06707 (integral Tate);
  - Kahn 2602.11135 (divided powers);
  - Hasan et al. 2407.06184 (integral Fourier duality);
  - Moretti-Passeri 2604.11799.

Result: no statement of the following was found:
- Theorems A, B or D;
- the exact values s_J = 2, 2, 6;
- the prime divisibility of s_J.

Known and cited in the paper:
- the factorial bound;
- the case s_J = 1 ⇔ m = 1 (Voisin, BdGF, Scavia-Suzuki);
- the values of m (EGFS, EGFS2) and the primes dividing m (Engel-Schreieder);
- EGFS Cor. 1.5 (no split embedding, even isogeny degree).

The search covers titles and abstracts and the opened statements, not full texts.

## Citations

Opened by the writer at the places cited:
- BdGF Thm 1.1, 1.2 (and §3, by its statement only);
- EGFS §1.2, Thm 1.1, Cor. 1.2, Cor. 1.5;
- EGFS2 Thm 1.2 and Question 1.1;
- Engel-Schreieder Thm 1.1, Cor. 1.2;
- Scavia-Suzuki Thm 1.1 and Prop. 3.4, through the fetch tool.

Opened by the SA06 run, not by the writer (locators as the run recorded them):
- ADFIO 2020 Cor. 2, p. 165;
- Beauville 1977 Prop. 2.2 p. 155, Thm 5.4 pp. 175-176, Thm 6.5(i) p. 178;
- Fulton Ex. 20.3.5 p. 400;
- Milne, Jacobian varieties, Lemma 6.9;
- Mumford, Abelian varieties §23 Thm 4 and Cor. 1 pp. 233-234, and §16 (Riemann-Roch);
- Oort 1971 Cor. 2.4.2 p. 287;
- Oort-Ueno 1973 Thm 4;
- Voisin 2024 Thm 1.4.

## Grothendieck's question (cote 14)

- **Text.** Codex web transcription K14-05, page `K14-05_14_scan071.tex`, in
  `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K14-05/out/pages/`. The sweep-3 reading is
  `results_register/horizontal/sweep3/SA06/readings/c14_c15rest_part2.md`, l. 36-52 and the hunch c14b-H1, l. 388-398.
- **Numbering.** Scan 71 is pencil sheet 70 (sheet = scan - 1). Prop. 2.7 is on scans 68-70.
- **Question 2.** Is there always an integral cycle giving the inverse of H^{2n-1}(X)(n-1) -> H^1(B_X)? If Question 1 has
  a positive answer, it suffices to answer Question 2 for abelian varieties.
- **What G3 answers.** Theorem D answers Question 2 for abelian varieties. Question 1 is not treated.

## Open items

- An independent check of Theorem D and Corollary C (iii).
- Surfaces with δ even, for example type (1,2) with End = Z, where s_J ∈ {1, 2}; threefolds with gcd(δ, 6) > 1.
- The characteristic-p analogues of Theorem B and Corollary C are not claimed.

## Before posting: the main session (329fb1e6, Claude Opus 5.5 at effort max), 25 Nov 2026 ~14:0x-14:2x UTC

- Read every page of the 6-page build. Checked line by line: Theorem B, Corollary C, Remark 2.3, Theorem D (the two the writer alone had checked) and the proofs of Lemma 2.2 and Theorem A as written (cited locators not opened). No mathematical error; five events in CHECK_EVENTS.tsv.
- Credit repaired: the half s_J | m of Theorem B is the known Matsusaka implication ([SS, Prop. 3.4], already named as known in the Context paragraph); only m | s_J^2 is new. Corollary C (i) already follows from published results ([SS, Prop. 3.4], [EGFS, Cor. 1.2], [EGFS, Cor. 1.5] via Remark 2.3); (ii) and (iii) need Theorem B. Changed: the abstract (TeX and ABSTRACT.md), the Context paragraph, Remark 2.3, the Checks and literature paragraphs of Section 4. Backup: src/G3_paper_before_main_credit_fix_20261125.tex. Rebuilt: 6 pp., 0 overfull, 0 underfull, 0 undefined; pages 4-5 looked at.
- Literature, beyond the writer's search: the full texts of Scavia-Suzuki arXiv:2507.09821v2 and Engel-de Gaay Fortman-Schreieder arXiv:2512.04902v1, and of arXiv:2507.15704v3 through its Section 3 (the HTML stops there), searched through a fetch tool's reading model for a least n with [n] through Jacobians, a bound on it, n^2 times the minimal class, non-principally polarized surfaces or threefolds, and (for 2512.04902) isogeny degrees divisible by 2, 3 or 6: none found. Engel-Schreieder arXiv:2606.31894v1 (30 June 2026) opened at its abstract: the least algebraic multiple of theta_k is divisible by every prime p <= (k+1)/2.
- POSTED as hexagon:2611.01067v1, committed 14:08:48 UTC (POSTING.md).
