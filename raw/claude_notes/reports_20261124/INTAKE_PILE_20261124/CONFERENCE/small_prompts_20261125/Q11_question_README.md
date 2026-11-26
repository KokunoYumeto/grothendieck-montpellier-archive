# OBJ_H037_question: what our runs proved toward the main question

The main question of the prompt is part 2) of his theorem on 100:3 for a reduced base whose normalization is finite:
whether the functor F from abelian schemes over S to triples (A_U, M, φ) is an equivalence there. This folder holds
what our research runs wrote on it, as LaTeX and tables. Every status in these files is the run's own claim; the
check events say what was checked, by whom and how.

Put together on 25 November 2026 by the conference convener (Claude Fable 5.2 at effort max), from the returns as they
are on disk. Nothing in the files was changed; the two tables marked "extract" hold the rows of Part C only.

## SA15/

From the return RESEARCH_SA15 (research on the crystals folders, cotes 4-9, and cote 100), by GPT-6 Astra (ChatGPT
Pro mode), checkpoint 37 of 20 November 2026.

- `RESEARCH_SA15_paper.tex`: the main file of the run's paper (preamble and macros; it inputs the sections).
- `sections/C.tex`: Part C, "Extension and descent". It holds C-RD1 to C-RD14 with proofs: the normal case (C-RD6),
  the examples on bases that are not reduced (C-RD4, C-RD5), the reduced example with a normalization that is not
  finite (C-RD11), the effect of nilpotents (C-RD3, C-RD12), the description of the essential image (C-RD13, C-RD14),
  the descent of homomorphisms (C-RD1, C-RD2) and the local-system lemma (C-RD7 to C-RD10).
- `sections/F.tex`: the run's section of his passages with their locators; C.1 to C.4 there are on cote 100.
- `RESEARCH_SA15_results_part_C.csv` (extract): the 18 rows of the run's results table for Part C (ids such as
  `thm:C-RD11`), with their statuses and the pages of cote 100 each one settles.
- `CHECK_EVENTS_part_C.tsv` (extract): the rows of the run's check events whose statement id begins with `C-`.
- `RESEARCH_SA15_references.bib`: its bibliography, with a note on each source saying what was opened.

The other parts of that paper are not here.

## POLISH_CRISTAUX_paper4/

From the return POLISH_CRISTAUX, by GPT-6 Astra (ChatGPT Pro mode), checkpoint 34 of 24 November 2026: its paper 4,
"A reduced counterexample to Grothendieck's extension assertion, after Ferrand-Raynaud and Olberding".

- `main.tex`: the paper: the example of C-RD11 written out, with the example of C-RD4 beside it.
- `STATEMENTS.tsv`, `SOURCE_MAP.tsv`, `BUILD.md`: its statements with their check events, the map from the earlier
  files, and the run's build record.
