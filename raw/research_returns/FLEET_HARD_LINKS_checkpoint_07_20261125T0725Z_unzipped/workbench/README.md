# Permanent level spaces, graph circuits, and formal-group height

This is a research workbench in progress, begun on 25 November 2026. It contains three independently editable papers, original proofs and computational checks, and a dated account of the questions that remain open. It does not claim a solution to P versus NP, to the uniform linear level-space conjecture, or to the unrestricted graph-circuit conjecture.

## Start here

- `papers/A/main.tex` and `main.pdf`: permanent level spaces. The unconditional bound is now 3 dim L ≤ n²+2n−1, hence 9 ≤ LS(6) ≤ 15. The paper also proves the bound ten in specified symmetry classes, connected rook-cumulant formulas, and the exact pure and mixed Klein restrictions. The uniform linear conjecture and LS(6) ≤ 10 remain open.
- `papers/B/main.tex` and `main.pdf`: monotone graph circuits. Four induced missing edges require four private products; both optimal six-deletion and optimal seven-deletion gain-four profiles are excluded. The latter combines separately rederived reductions for one, two and three visible cuts with complete DAG enumeration and checked RUP refutations. The last gain-four profile, with six deleted gates and one excess quadratic-frame gate, is also excluded: full context supports and disjoint affected stars force a cover smaller than gain four. For smaller gain, both optimal five- and six-deletion P4 disjoint K2 profiles are excluded, as is the optimal five-deletion K3 disjoint K2 profile, and any branch with exactly one deleted addition requires D ≥ 2^d−1. Lower cover-gain cases remain. A shared bilinear architecture admits size-preserving normalization under an explicit universal-row condition. The unrestricted conjecture and general bidegree (2,2) remain open.
- `papers/C/main.tex` and `main.pdf`: counting hypersurfaces and Artin–Mazur height. An exact replica-orbit criterion separates height two from height at least three at every prime. Promised height-two decision is Mod_pP-complete; logically equivalent formulas with equal satisfying counts can give different height-two status. A finite coefficient rule determines every height including infinity, and analysis of the established quasi-F-split matrix gives deterministic polynomial space and a separate dense time bound 2^{O(d log p)}poly(s,d,log p). The original finite-trace proof remains as an alternative appendix. Fixed-prime exact-height decision with unary requested height is Mod_pP-complete; allowing both prime and height in unary gives exact-counting oracle equivalence. With the prime included in the input, even promised height-two decisions recover exact counting by polynomially many nonadaptive oracle queries. Matching full-function complexity remains open. Additional sections treat character actions, bounded-rank trace presentations, specialization of separation degree, class-group minors, p-adic root valuations, and odd theta characteristics.
- `QUESTIONS.tsv`: every requested research question, its current state, and its next mathematical obstruction.
- `STATEMENTS.tsv`, `CHECK_EVENTS.tsv`, and `CROSSWALK.tsv`: statements, precise check types, and relationships to earlier work.
- `LITERATURE.md` and `SOURCES.tsv`: sources actually consulted, with exact locators and hashes where source bytes were fetched.
- `DICTIONARY.md`: the proved translations into geometric and arithmetic language, with limits stated explicitly.
- `LEDGER.md`: research progress, as distinct from drafting and packaging.

## Reproduce the papers

With Python 3 and a standard TeX Live installation, run:

```
python build.py
```

The script copies each paper's editable inputs to a fresh temporary directory, invokes pdfLaTeX three times, and places its PDF beside the source. `checks/build_latest.json` records overfull boxes, unresolved references, and PDF hashes. A compiling draft is not by itself a mathematically finished paper.

## Reproduce the mathematics

The `research/` directories contain original programs, detailed proof reports, independent re-proofs, and explicit certificates. Reports and command sections record the applicable inputs, commands, expected output, and the limits of each check. `checks/rook_cumulants.py` independently compares the connected-partition calculation with a matching dynamic program and the formal logarithm on exact integer matrices.

All numerical searches are labelled exploratory. A failure to find a matrix space or circuit is not a proof of nonexistence. A modular rank certificate is an exact integer-matrix argument, but is not a Lean or other proof-assistant certificate. Separate workers in this workbench use the same model, GPT-6 Astra Pro, with inherited effort; an effort level not exposed by the runtime is not invented. No human has checked the work.

## Filing convention

The intended home is `https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench`; records are to be filed at `https://github.com/KokunoYumeto/mathematics-workbenches`. This folder is local preparation, not a public deposit. No registry number, repository commit, or permanent paper page has been assigned. The stable local statement tags will be mapped to the registry's permanent tags when the owner files the papers. No `DEPOSITED.md` is created prematurely. Version manifests record the local bytes without inventing a public commit.

Only original work produced for this task is included. The input archive, earlier unchanged documents, and external source papers are excluded. The latter are cited and linked. Original text and programs are dedicated to the public domain under CC0 1.0, except where a file explicitly documents a cited statement rather than claims ownership of it.

## Reading and verification status

The wider task remains research in progress. Paper A is frozen at 27 pages and Paper C at 46 pages, each with complete expert and newcomer readings and every-page visual inspection of the final PDF. Paper B has grown to 37 pages following the accepted six-deletion path result; the earlier 34-page version had both full readings and every-page inspection, and the new proof has separate reproof and targeted checks. Its final incremental reading and layout inspection remain pending further results. The new weighted A bound and the main C height constructions have separate statement-only same-model re-proofs. The paper-specific manifests bind each reading and visual check to the version inspected. A normalization error in the displayed Klein basis was corrected from E01 to E02 after an independent reconstruction; all384 exact coefficients and the finite no-extension calculation were then checked independently.

The dated ledger controls continuation and stopping. A new result is not called a solution of an open row merely because its subcase is proved. Source citations, check-event types, and unsuccessful searches are kept separately so that a fresh reader can recover what is proved and what remains a gate.
