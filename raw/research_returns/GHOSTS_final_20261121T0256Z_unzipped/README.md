# GHOSTS — final research package

This package contains the final paper GHOSTS.tex, its reading copy GHOSTS.pdf, the question ledger, check-event record, implications, transcription notes, and the complete authored research trail. Original supplied attachments remain the cited sources; retrieved source URLs and exact locators appear in the paper and proof memos. Third-party source PDFs and disposable build/render files are not duplicated.

Compile GHOSTS.tex from this directory with pdflatex twice. All section and bibliography files are included. Historical proof memos preserve superseded candidates and earlier constants; the final paper and latest check events govern the accepted statements. Historical status entries are not silently rewritten.

## Principal outcomes

- Corrected bounded-specialization criterion B01–B06, including automatic multiplier boundedness from bounded total integral numerator degrees.
- Realization-compatible CM transport with charged numerator/denominator formulas C01–C07, and the explicit constant-growth T9 example C18.
- Exact minimum16 for t_star and its primitive half-class t0 at every geometric good reduction, ordinary and supersingular, by P13 and V06.
- Exact complex minimum24 for w=e_W[Gamma1], by W01–W04; cofinite local value24 by B03, with no assertion about an uncomputed exceptional prime.
- Explicit uniform bounds for every fixed Eisenstein Weil fourfold lattice and vector, R10–R24, and the Dirichlet-GRH finite-prime gate R30–R31.
- A terminating procedure for the entire good-prime function from actual equations, polarization data, and an exact marked Betti class, R40–R45.

## Reproducing the computer-assisted proof

Run `python3 research/w_exact24_certificate.py`. It uses Python's standard library, regenerates all catalogs, verifies the target and degree24 identity, and exhausts the lower-degree comparison using exact arbitrary-precision integers. The final line is `PASS W04`. Its output and the independent root rerun are included. Mathematical completeness of the finite lists is proved in W01–W04; this calculation is not represented as Lean or other formal verification.

Every accepted proof received a complete mathematical reading, recorded in CHECK_EVENTS.tsv with the actual kind of check and agent identity. The supplied 2026 Hodge, Tate, standard-conjecture and Dirichlet-GRH results are used as requested theorem inputs; their complete formal developments were not rebuilt. TRANSCRIPTION_NOTES.tsv is header-only because no mathematical correction to a supplied Grothendieck transcription was established. Source-locator corrections are recorded separately.

DELIVERABLE_MANIFEST.tsv lists the size and SHA-256 hash of every other included file. No earlier checkpoint ZIP is nested in this package.
