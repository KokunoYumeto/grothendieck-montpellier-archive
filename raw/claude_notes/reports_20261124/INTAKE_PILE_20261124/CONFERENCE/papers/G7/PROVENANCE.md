# G7: provenance, checks and literature search

- **Note:** `G7_paper.pdf`. Title: "A wild quasi-étale double cover over a single smooth genus-two exceptional curve in
  characteristic two". Source: `src/G7_paper.tex`.
- **Writer:** Claude Opus 5.5 at effort max (agent a3c8d7ded052a745e), 25 Nov 2026.
- **Brief:** `agent_notes/a3c8d7de_G7_NOTE_BRIEF_20261125.md`, from main session 329fb1e6 (Claude Opus 5.5 at effort max).
- **Program:** item G7 of the conference program (`CONFERENCE/PROGRAM.md`, sections (c) and (d)); board row S12d.
- **Status:** not posted.

## Who produced what

**Theorem A** (tameness at the radial valuation for completed graded surface cones) is due to the run RESEARCH_SA12 of
GPT-6 Astra (OpenAI, ChatGPT Pro mode). The run ended on 20 Nov 2026; its folder is
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA12_final_INCOMPLETE_20261120T2310Z_unzipped`.

| | Lemma 4.16 | Proposition 4.17 |
|---|---|---|
| Register id | D:formal-torus-lift | D:graded-cone-tame |
| Source file | `parts/C/D_graded_cone_tameness.tex` | `parts/C/D_graded_cone_tameness.tex` |
| Location in `parts/D/paper_D.tex` | line 1426 | line 1536 |
| Page of `RESEARCH_SA12_paper.pdf` (603 pp.) | 105 | 107 |

The note quotes the two statements verbatim, joined into one.

**Theorem B** (the example) is the run's Example 4.60, register id D:wild-genus2-single-curve. The run's status for it
is "Refuted", meaning that universal tameness above a single smooth exceptional curve is refuted.
- Source: `parts/B/D_wild_genus2_curve_B.tex`.
- Location: p. 143 of `RESEARCH_SA12_paper.pdf`.
- Certificate: `parts/B/code/check_wild_genus2_curve.py`.

The run's further statements are cited in the note's Scope, but not used or reproved there:
- Proposition 4.61 (D:wild-genus2-source, p. 146): the resolution of T, with C' the Frobenius twist of C and
  (C')² = −2;
- Corollary 4.62 (D:wild-genus2-pro2, p. 147): the maximal pro-2 quotients, 1 for T and Z/2 for S;
- p. 152: the run's bounds on the image of exceptional wild inertia, of order at most 4 for T and 8 for S.

**Due to the writer** (agent a3c8d7ded052a745e, Claude Opus 5.5 at effort max):
- **The proof of Lemma 2.3.** It shows that z² + tz = x defines a field from the residue at C: x̄ is not a square in
  k(C). The run instead proves non-triviality by a Čech torsor, h = y/x², on the family of genus-two curves over
  A¹_t. The writer used the residue argument at its intake on 22 Nov.
- **Corollary C (ii)-(iii).** The comparison surface S0: b² + t⁵b + a⁵ = 0 has the same exceptional curve with
  C0² = −1 and only tame covers (by Theorem A), so the completed germs of S and S0 are not isomorphic.
- **Corollary C (i).** The precise form of the run's remark that "the hypothesis of formal linearity in
  Proposition D:graded-cone-tame cannot be discarded".
- **The text and the arrangement of the proofs.**
- **The minimality of the completed resolutions** (§2.3, added 25 Nov when applying R7). The factorization through
  the minimal resolution (Lipman 1978, p. 155, remark A) cannot contract C, since the completed germ is singular, so it
  is an isomorphism. This replaces the (−1)-curve reason proposed in R7.

**Due to the independent checker** (agent a65dbdc241d1a129a, Claude Opus 5.5 at effort max, 25 Nov 2026; record
`CHECK_G7_INDEPENDENT.md`):
- **Lemma 2.6 and its proof (its R3).** A finite cover with a rational source, for instance a regular one, lies only
  over rational exceptional curves. So o' ∈ T is a singular, non-rational double point. The writer turned R3's remark
  into a lemma and reworded it slightly.
- **The argument identifying the radial valuation in Corollary C (ii) (its R6).** Applied with its wording.
- **The wording of R1, R2, R4, R5, R8, R9 and R10.** Applied as worded, with small changes:
  - in R10 the sentence on Artin 1977 says that rational double points have only rational exceptional curves,
    rather than citing Lemma 2.6 for both;
  - Theorem B (ii) now ends "The surface T is singular at o', and o' is not a rational singularity; T is smooth
    elsewhere".

## Checks

Every check of the note's statements is listed in `CHECK_EVENTS.tsv`, which uses the seven types of the rubric.

1. **The run's own audits.** GPT-6 Astra, ChatGPT Pro mode: sub-agents /root, /root/part_b, /root/part_c and
   /root/part_d, by `results_register/CHECK_REGISTER.tsv` (`who_checked.py D:wild-genus2-single-curve`). The register
   lists their actual-file readings; the writer did not reread their outcomes for this note.
2. **The writer's intake, 21-22 Nov 2026.** The events are in
   `results_register/horizontal/sweep3/SA12/INTAKE_RESEARCH_SA12_20261121_full_part2_CHECK_EVENTS.tsv`.
   - Theorem A: targeted proof checks of D:formal-torus-lift and D:graded-cone-tame.
   - Theorem B: an independent re-proof by hand, and a rerun of the run's certificate (26 assertions, exit 0).
   - The intake report is `results_register/horizontal/sweep3/SA12/INTAKE_RESEARCH_SA12_20261121_full_part2.md`
     (rows 433-435 in section 1.19).
3. **Cluster reader SWEEP3_A, 24 Nov 2026** (Claude Opus 5.5 at effort high; main session 329fb1e6).
   - It ran its own sympy script, `agent_notes/sweep3A_20261124_work/sa12_wild_genus2.py`, without importing or running
     the run's code, and made a targeted check by hand of the non-computational steps.
   - The events are in `reports_20261124/INTAKE_PILE_20261124/INTAKE_RESEARCH_SA12_20261124_CHECK_EVENTS.tsv`.
4. **Writing G7, 25 Nov 2026.** By the writer.
   - The run's certificate was copied unchanged into `checks/`; its sha256 matches the run's file. It was rerun from a
     scratch copy: exit 0, 26 assertions.
   - The writer's own program, `checks/check_g7_writer.py`, gave 24 assertions, exit 0.
   - The writer's own proofs (Lemma 2.3 and Corollary C) were reread line by line on the built PDF. This is not
     independent of their author. The residue argument of Lemma 2.3 was also checked by SWEEP3_A (item 3).

5. **The independent check, 25 Nov 2026, 14:36-14:55 UTC.** By agent a65dbdc241d1a129a (Claude Opus 5.5 at effort
   max), on the brief `agent_notes/a65dbdc2_G7_CHECK_BRIEF_20261125.md` from the main session.
   - It made targeted checks of Lemma 2.3, of §2.3 and of Corollary C (i)-(iii): all confirmed.
   - It found that T is singular at o' and not a rational singularity. It proved this independently, and confirmed it
     by its own program, `scratchpad/g7_check/t_point.py`.
   - It read the arXiv full texts of LS20, LS23, IS and Ma.
   - It checked the citations made from memory, as standard uses.
   - It proposed repairs R1-R10.
   - Its 16 events are merged into `CHECK_EVENTS.tsv`. One type name, "computational or formal certificate", was
     normalized to "computation or formal certificate", the spelling used in this file and in the other conference
     papers.
6. **Applying the repairs, 25 Nov 2026.** By the writer.
   - Lipman 1978 was opened at the source: the free copy on his Purdue page, p. 155, remark A, the unique minimal
     desingularization.
   - The writer's minimality argument was reread on the built PDF. It is not independent of its author.
   - Both are events in `CHECK_EVENTS.tsv`, which now holds 28.
   - R3 (Lemma 2.6) and R6 are the checker's own proofs. The main session will check them when it reads every page.

How to run the programs: see `checks/README.md`. The programs check polynomial identities only. Normality,
properness, the genus, connectedness and the ramification along C are proved in the text.

## The search of the literature

**22 Nov 2026, by the writer, at the intake.** These are web searches of arXiv and the journal literature, with
arXiv LaTeX opened where named.
- Wild quotients of smooth germs:
  - Artin, Wild Z/2 actions in dimension two (1975) and Coverings of the rational double points in characteristic p
    (1977);
  - Lorenzini-Schröer, arXiv:1904.08371 (Math. Z. 2020) and arXiv:2101.08090 (ANT 2023);
  - Ito-Schröer, arXiv:1209.3605.
- Coverings between rational double points: Matsumoto, arXiv:1812.03466, section 6.
- Tameness theorems:
  - Carvajal-Rojas-Schwede-Tucker, arXiv:1606.04088. The LaTeX was opened: Theorem A gives a finite local
    fundamental group of order at most 1/s(R) and prime to p for strongly F-regular rings.
  - Carvajal-Rojas-Stäbler, arXiv:2004.07628 (KLT threefolds, p > 5);
  - arXiv:1707.08611 (log terminal surface germs: finite).
- Hexagon, searched for "singularity", "wild ramification", "fundamental group surface" and "Artin-Schreier".
- Verdict then: not found; new provisionally, pending Cutkosky-Srinivasan 1993. The record is section 10 of the intake
  report.

**23 Nov 2026, by the main session 329fb1e6** (Claude Opus 5.5 at effort max). It read Cutkosky-Srinivasan, Comment.
Math. Helv. 68 (1993), 319-332, at the source (pp. 319-331).
- The paper has no characteristic-2 statement: its §3 assumes p > 3.
- Its p-part results concern purely inseparable covers of Brieskorn singularities.
- Its Theorem 1(b): finiteness of the prime-to-p completion forces rational exceptional curves in a tree.
- The example is not there. Record: `reports_20261123/s12d_note/GATE_CS1993_20261123.md`.

**25 Nov 2026, by the writer, for this note: what appeared since 22 Nov.**
- **arXiv API** (export.arxiv.org, sorted by submission date, newest first). The queries:
  - "wild quotient";
  - quasi-etale with characteristic;
  - "local fundamental group" with "positive characteristic";
  - "exceptional curve" with wild;
  - fierce or fiercely ramified;
  - math.AG with wild and singularity;
  - math.AG with "characteristic 2" and "double cover";
  - math.AG with quasi-étale or quasi-etale;
  - math.AG with tame and surface singularities.

  Nothing on this topic appeared after 22 Nov 2026. The nearest new or newly seen items:
  - Hübner-Temkin, Largeness of the wild locus, arXiv:2610.11864 (8 Oct 2026): curve tameness against valuation
    tameness for étale maps of smooth adic spaces;
  - Gonzalez-Hernandez, The classification of generalised Kummer surfaces in positive characteristic,
    arXiv:2608.21534 (Aug 2026): rational double points and their local fundamental groups.

  Neither contains the cover.
- **Hexagon** (hexagonmath.org), searched for "wild" (8 works), "exceptional curve" (0), "characteristic two" (9),
  "singularity" (10, on 22 Nov), "wild ramification", "fundamental group surface" and "Artin-Schreier". The November
  list (`/list/2611`, page 1 of 5, titles) was scanned as well.
  - None concerns wild covers of surface singularities.
  - The nearest are Kisin, "Serre's conjecture on the Artin character for a regular local ring" (28 Oct 2026, group
    actions on regular local rings), and works on characteristic-two arithmetic.
- **Verdict:** the cover is not in print in the sources searched. The note says "new, to our knowledge after the search
  described".

**25 Nov 2026, by the independent checker** (a65dbdc2, Claude Opus 5.5 at effort max). It read the arXiv full texts
of Lorenzini-Schröer 1904.08371 and 2101.08090, Ito-Schröer 1209.3605 and Matsumoto 1812.03466 (PDFs converted to
text). None has a wild cover over, or a quotient singularity with, an exceptional curve of positive genus.
- Ito-Schröer quotient by special p-groups, not by Z/p. The note was corrected (R2).
- Matsumoto's coverings of rational double points have regular sources (§6.2, Lemma 6.6).
- The one exceptional curve of positive genus in LS23 is Laufer's characteristic-0 elliptic example. It is not a
  wild cover.

Artin 1975 was not opened: ams.org refused automated access. Its title was corrected from the AMS record and the
three papers' bibliographies (R1): "Wildly ramified Z/2 actions in dimension two". Artin 1977 has no free copy. Their
sources are regular (Artin 1975, as recalled in LS20's Introduction) or their bases are rational double points
(Artin 1977), so neither can contain the example.

**Risk named by the checker, not searched:** papers whose covers have non-rational sources, such as elliptic or other
non-rational Gorenstein double points in characteristic 2. By Lemma 2.6, only such work could contain the example.

**Not opened by the writer** (past its reading limit): the full texts of Artin 1975 and 1977. Lipman 1978 was opened
on 25 Nov, at p. 155.
- The standard references are cited from the writer's knowledge, not opened: Hartshorne 1962 §2 (connectedness for
  depth ≥ 2), Matsumura Thm. 23.7, Serre, Local Fields III §6 Cor. 2 (the different of a monogenic extension), and
  Stichtenoth Prop. 3.7.8 (the genus of an Artin-Schreier curve).
- The note proves the genus directly, so the Stichtenoth citation is a cross-reference.
- Whether Theorem A itself is in the literature was not examined. The note uses it as proved in the run, with the
  writer's targeted check.

## Build

- **First version** (7 pages): pdflatex (MiKTeX), three passes, 25 Nov 2026. 0 overfull boxes, 0 underfull boxes, no
  undefined or multiply defined reference. Every page was rendered at 80 dpi and looked at (pages 6-7 again after the
  last edits).
- **After the repairs R1-R10** (25 Nov, 14:5x UTC): 8 pages, three passes, again 0 overfull, 0 underfull and no
  undefined reference. All eight pages were rendered at 80 dpi and looked at.

Where the repairs landed:

| Repair | Where | Page |
|---|---|---|
| R4 | abstract | 1 |
| credit for Lemma 2.6 | title footnote | 1 |
| T singular | Theorem B (ii) | 2 |
| R5 | Why it matters | 2 |
| credit for Lemma 2.6 | Credit | 3 |
| R2, R9 | Context | 3 |
| R8 | Scope | 3 |
| R3 | Lemma 2.6, and the proof of Theorem B | 6 |
| R7 | §2.3, minimality | 6 |
| R6 | Corollary C (ii) | 7 |
| R7 | Corollary C (iii) | 7 |
| credits of the checker | What is whose | 7 |
| R10 | Checks | 7 |
| R10 | The search of the literature | 7-8 |
| R1 and [Li78] | References | 8 |
- The build logs are `src/build1.txt`-`src/build3.txt` and `src/G7_paper.log`.

## Files

- `G7_paper.pdf`, `src/G7_paper.tex` (and its LaTeX by-products);
- `ABSTRACT.md`, `PROVENANCE.md`, `CHECK_EVENTS.tsv`;
- `checks/README.md`;
- `checks/check_wild_genus2_curve.py`, `.out` and `_output.json`: the run's certificate and our run of it;
- `checks/check_g7_writer.py` and `.out`: the writer's program and its run;
- `CHECK_G7_INDEPENDENT.md` and `CHECK_G7_INDEPENDENT_CHECK_EVENTS.tsv`: the independent check (a65dbdc2), whose 16
  events are also merged into `CHECK_EVENTS.tsv`.
