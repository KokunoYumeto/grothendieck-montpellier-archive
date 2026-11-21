# ZETA_TWO — final research package

21 November 2026 · GPT-6 Astra Pro · reasoning effort not exposed.

Read **ZETA_TWO.pdf** for the rendered paper or **ZETA_TWO.tex** for its
standalone source. Part I contains checked findings and their complete new
proofs. Part II separates unchecked source claims and their exact gates.
Alpöge A is treated as the stipulated theorem input throughout. Every M
conclusion remains conditional on the all-field, all-unitary-character
Hecke-GRH claim. General motivic RH and Artin holomorphy are not claimed.

## Required records

- `QUESTIONS.tsv`: every treated question, result or current source gate.
- `LEDGER.md`: final states, approaches, remaining gates, next actions, timing.
- `CHECK_EVENTS.tsv`: actual proof reviews, source checks, computations, and limitations.
- `IMPLICATIONS.md`: consequences for the programme and prior runs.
- `TRANSCRIPTION_NOTES.tsv`: one literal original-scan notation difference,
  with no change in the vanishing claim.

## Audit and reproducibility

`FLAG_AUDIT.tsv` covers all 575 supplied flag rows. `INTAKE_INVENTORY.tsv`
contains all 587 identified table occurrences, including repetitions and
grouped IDs; these are not 587 distinct newly proved statements.
`CONDITIONAL_AUDIT.tsv` contains 85 scoped premise records and
`ANALYTIC_KEYWORD_HITS.tsv` the 51 source hits. `METHOD_STATEMENTS.tsv`
contains 20 Alpöge steps and 18 Masullo entries. Original run statuses
are preserved, including previously refuted formulations.

`SOURCE_CORRECTIONS.tsv` concerns intake prose. It must not be merged into
the archive transcription layer without the distinction preserved.
`SOURCE_LOCATORS.tsv`, `ARCHIVE_SOURCE_LOCATORS.tsv`, and the bibliography
identify exact sources. Original archive URLs and page-copy hashes identify
the checked facsimiles without reproducing complete external publications.
The source manifest describes the once-extracted original attachment.

Run `python tools/intake_compute.py` to regenerate the exact integer and
rational cyclotomic certificate (requires SymPy and mpmath). Its decimal
gamma/logarithm evaluations are illustrations, not certified intervals.
Run `python tools/intake_build_audit.py` to regenerate the 85-record scope
audit next to that script. The proof checks do not claim a Lean kernel run.

The LaTeX source has no external `\input` dependency. A standard TeX Live
installation with the listed common packages can compile it by running
`pdflatex ZETA_TWO.tex` twice. The included PDF is the rendered deliverable.
