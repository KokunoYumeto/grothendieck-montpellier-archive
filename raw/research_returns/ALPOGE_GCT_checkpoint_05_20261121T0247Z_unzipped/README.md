# ALPOGE_GCT research package

Read `ALPOGE_GCT.tex` (or its compiled PDF when present) for the mathematical paper, `IMPLICATIONS.md` for the ranked implications, `QUESTIONS.tsv` for item states, and `CHECK_EVENTS.tsv` for the proof audit. `LEDGER.md` records actual progress and unresolved gates.

This is research in progress. P-F19 and P-F30–P-F31 refute both the canonical modular-index clause and the numerical positive-form clause of ordinary plethysm PH3, already for the fixed inner shape (3). Narrow PH2/SH, uniform effective shifted counting and an asymptotic determinant/permanent obstruction remain open. P-F32 gives a direct exterior-duality reduction and a square-root index lower bound, compatible with the remaining polynomial upper-bound questions. P-F11–P-F12 prove the positive-form implication to PH2; P-F14–P-F15 refute the broader rank-only subgroup-restriction index hypotheses. The paper makes no P versus NP or ordinary complex-field VP versus VNP claim. A checkpoint is a snapshot of the work at its stated time, not a declaration that every requested research target is complete.

The `work/` folder preserves the authored fragments, check notes, computations and assembly scripts. `supplied_sources/` preserves the extracted attached inputs; `SOURCE_MANIFEST.json` records their hashes. Full external literature downloads are not redistributed; exact source URLs and locators appear in the paper and notes.

The paper is a single standalone LaTeX source. On a normal TeX Live installation, run `pdflatex ALPOGE_GCT.tex` twice. The explicit font-map lines support the present runtime; standard installations may emit harmless duplicate-map warnings. The source uses ordinary AMS, geometry, booktabs, tabularx, longtable, hyperref, enumitem, mathrsfs and Latin Modern packages.

Finite computation files are sanity checks, not proof-assistant certificates. The supplied Alpöge/OpenAI results are accepted as cited premises as instructed. The imported Lean proofs were not rebuilt in this run. Every check records its actual method and available model/effort information.


The paper now integrates P-F39–P-F46: exact nonstandard trace/norm models and a positive operator; Klein stabilizer phases; the identified theta/discriminant subalgebra; an unconditional actual cubic average-polynomial bound; the binary-degree-twelve parameter counterexample; an exact signed global cone contribution; and the precise full-eigenspace ball range of the cyclic cubic cover; and the exact positive E6 theta input with a proved obstruction to direct coefficient reindexing. Their complete proofs and actual whole-proof checks are included. The first formal three-hour review and its historical open-row inventory are in FORMAL_REVIEW_03H.md.


Checkpoint05 paper status:153 compiled and visually checked pages through P-F46, including its unitary-lift extension. Working fragments P-F47 (exterior-volume/Fermat evaluation) and P-F48 (density scope) are preserved separately with their actual author/peer checks and source corrections; they are not yet incorporated in this paper. The emerging Hessian/Cayley nonvanishing attempt P-F49 is a research route, not a conclusion of the checkpoint paper.
