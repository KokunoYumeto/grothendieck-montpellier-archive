# OBJ_H0A2-1_question: what our runs proved toward the main question

The main question of the prompt is his box on 57:97, « noyau nul si n ≥ 4 »: the injectivity of Pic(X) → Pic(Y) for a
smooth hyperplane section Y of a smooth projective X of dimension n ≥ 4 in characteristic p, with no cohomological
condition. This folder holds what our research runs wrote on it, as LaTeX and tables. Every status in these files is
the run's own claim; the check events say what was checked, by whom and how.

Put together on 25 November 2026 by the conference convener (Claude Fable 5.2 at effort max), from the returns as they
are on disk. Nothing in the files was changed.

## SA14/

From the return RESEARCH_SA14_SA19 (research on the Picard folders, cotes 43-44 and 57-60), by GPT-6 Astra (ChatGPT
Pro mode), checkpoint 08 of 20 November 2026.

- `RESEARCH_SA14_SA19_paper.tex`: the main file of the run's paper (preamble and macros; it inputs the sections).
- `sections/A.tex`: Part A, "Lefschetz for Picard groups in positive characteristic". It holds A4, A4b, A4c, A3r, A1r,
  A2b, A3n, A3s, A3f, A3R and A3, with proofs.
- `sections/K.tex`: the run's numbered register of all its statements (K.1, K.2, ...), each with its status and the
  place of its proof. For the main question: K.207 (A2D), K.219 (A2V), K.220 (A2W), K.225 (A2Y), and the rows on A1
  and A2.
- `work/bce/`, `work/dgj/`, `work/fhi/`, `work/root/`: the work files on Part A of the run and of its three workers:
  proofs (`A2_determinantal.tex`, `A2_cartier_leading.tex`, `A2_closed_forms.tex`, `A2_target_frobenius.tex`, ...),
  attempts (`attempt_A2_*`), audits, and the research notes.
- `RESEARCH_SA14_SA19_results.csv`: the run's results table (id, statement, status, where proved, pages settled,
  notes). The rows A1 and A2 are "Undecided".
- `CHECK_EVENTS.tsv`: the run's check events.
- `RESEARCH_SA14_SA19_references.bib`: its bibliography, with a note on each source saying what was opened.

The other parts of that paper (B to J) and the work files on them are not here.

## P90a_note_v3/

- `p90a_note_v3.tex`: our note on A3, the failure of Kodaira vanishing for a very ample sheaf on a surface, in every
  characteristic; posted as hexagon:2611.00936 (version 3, 24 November 2026). `METADATA_ABSTRACT.txt` is its
  abstract, `CHANGE_NOTE.txt` says what version 3 changed.

## POLISH_AG_paper_02/

From the return POLISH_ALGEBRAIC_GEOMETRY, by GPT-6 Astra (ChatGPT Pro mode), checkpoint 35 of 24 November 2026: its
paper 2, "Picard schemes, very ample surfaces and metabelian local groups".

- `main.tex` and the other `.tex` files: the paper and its sections. The theorems on the kernel of Pic(X) → Pic(Y)
  for a curve Y on a surface are in it: the genus bound for a class of order p trivial on a smooth very ample curve,
  and the lower bound for the excess in the conductor inequality (`thm:positive-excess-picard`).
- `STATEMENTS.tsv`: every statement of the paper, with its proof location and check events.
- `CHECK_EVENTS.tsv`, `SOURCES.tsv`, `BUILD.md`, `DEPOSIT.md`: the paper's check events, its sources with locators,
  and the run's build and deposit records.
