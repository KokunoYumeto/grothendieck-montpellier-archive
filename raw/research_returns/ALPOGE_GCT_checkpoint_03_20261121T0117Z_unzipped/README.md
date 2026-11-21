# ALPOGE_GCT research package

Read `ALPOGE_GCT.tex` (or its compiled PDF when present) for the mathematical paper, `IMPLICATIONS.md` for the ranked implications, `QUESTIONS.tsv` for item states, and `CHECK_EVENTS.tsv` for the proof audit. `LEDGER.md` records actual progress and unresolved gates.

This is research in progress. P-F19 refutes the stronger canonical modular-index clause of ordinary plethysm PH3, already for the fixed inner shape (3). The weaker numerical positive-form clause, narrow PH2/SH and an asymptotic determinant/permanent obstruction remain open. P-F11–P-F12 prove the positive-form implication to PH2; P-F14–P-F15 refute the broader rank-only subgroup-restriction index hypotheses. The paper makes no P versus NP or ordinary complex-field VP versus VNP claim. A checkpoint is a snapshot of the work at its stated time, not a declaration that every requested research target is complete.

The `work/` folder preserves the authored fragments, check notes, computations and assembly scripts. `supplied_sources/` preserves the extracted attached inputs; `SOURCE_MANIFEST.json` records their hashes. Full external literature downloads are not redistributed; exact source URLs and locators appear in the paper and notes.

The paper is a single standalone LaTeX source. On a normal TeX Live installation, run `pdflatex ALPOGE_GCT.tex` twice. The explicit font-map lines support the present runtime; standard installations may emit harmless duplicate-map warnings. The source uses ordinary AMS, geometry, booktabs, tabularx, longtable, hyperref, enumitem and Latin Modern packages.

Finite computation files are sanity checks, not proof-assistant certificates. The supplied Alpöge/OpenAI results are accepted as cited premises as instructed. The imported Lean proofs were not rebuilt in this run. Every check records its actual method and available model/effort information.
