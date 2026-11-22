# CX_GRH — final research package

Research run **CX_GRH-20261121**, begun 21 November 2026, 00:00:34 Europe/Berlin (20 November, 23:00:34 UTC).

## Reading order

1. **CX_GRH.pdf** is the typeset paper. **CX_GRH.tex** is its complete, self-contained LaTeX source; no external bibliography or component input file is required to compile it.
2. **IMPLICATIONS.md** explains the conclusions for computational complexity and the corresponding Grothendieck frameworks.
3. **QUESTIONS.tsv** records each treated question, its exact source locator, and its proved result, refutation, or current gate.
4. **CHECK_EVENTS.tsv** records the checks that actually occurred, including author readings, independent readings, source checks, background dependencies, and the limited finite diagnostic. It distinguishes all of these from formal verification.
5. **LEDGER.md** records the progression of the main gates, alternatives tried, checkpoint timing, and the state of the stronger unproved extensions.

The paper has three parts: checked analytic and computational findings; separate checked geometric restatements and dictionaries; and unproved extensions with their current gates and verification conventions. The 39 finding IDs are CX-R01–R02, CX-K01–K08, CX-N01–N15, CX-E01–E08, and CX-G01–G06. The six CX-U IDs designate unproved extensions, not additional theorems.

## Central conclusions and their premises

The task's convention is retained throughout: Alpöge's rational Dirichlet theorem (**A_D**) and the supplied OpenAI fixed-width counting theorem (**E**) are accepted as theorems. Every result using Masullo's all-number-field Hecke claim (**M**) remains **conditional on M**. No kernel replay of a full Lean development is claimed.

- A_D discharges the quadratic-character hypothesis of Miller–Bach, the prime-field nonresidue search, and qualified primitive-root constructions. CX-N13 extends the nonresidue construction to every supplied finite-field extension for a specified prime dividing p−1.
- Koiran's checked AM proof reaches the Dedekind zeta function of a bounded solution field, which need not be normal. M supplies that premise. A_D supplies an explicitly bounded abelian-witness promise; the universal abelian-witness shortcut is refuted.
- The GCT V transfers preserve the distinction between a small separating system and an optimal-cardinality homogeneous parameter system, the equation-access premise, and the later unconditional PSPACE construction.
- CX-N15 gives a complete general deterministic finite-field factorization proof under an explicit sufficient family of cyclotomic–Kummer Dedekind-zeta hypotheses, all supplied by M. Its bound is **(d^{log d} log q)^{O(1)}**, retaining quasipolynomial dependence on degree. Its proof does not depend on the unretrieved internal EVD94 reduction or the historical radical oracle.
- Class-group generators, index verification, and complete class-group computation have different outputs and costs. The paper includes a rigorous conditional imaginary-quadratic Las Vegas computation theorem and retains its subexponential expected running time.
- E refutes the stated ETH/SETH variants and yields the proved parameter-preserving counting transfers. The supplied nearly linear Boolean circuit lower bound is in E^NP. These deductions do not settle P versus NP or VP versus VNP, or construct a GCT orbit-closure obstruction.

Every finding has a geometric restatement or explicit proof-carrying dictionary in Part II. The archive references use both cote and scan, with manuscript sheet numbers when present. Historical companion passages are distinguished from the sources of modern complexity theorems.

## Scope of the unproved extensions

The requested source-specific hypothesis classifications and transfers are proved at their stated scope. The stronger questions in Part III are not marked solved: an unrestricted A_D-only proof for HN or general finite-field factoring; a general polynomial degree bound for deterministic factoring; unrestricted class-group relation-search complexity; removal of the equation-access or symbolic/equivariant GCT gates; and stronger quantitative ETH transfers. Specific failed shortcuts and the strongest established reductions are recorded, without claiming logical independence or impossibility.

## Research record and reproducibility

The `work/` directory contains the authored component proofs, source and scope notes, independent review reports, component check ledgers, the GCT V source-label concordance, and assembly scripts. These preserve the development history; **the top-level paper and registers are the authoritative final versions**. In particular, `work/eth_factoring_composition_projector_draft.tex` is a superseded construction retained as a development record. It is not merged into the paper. Source-audit reports state their own snapshot hashes and counts; the final consolidated register includes their later additions.

The original task is included as `research/PROMPT.md`. `research/SOURCE_FILES.tsv` records hashes and local provenance for supplied and consulted source files. Full third-party PDFs and OCR dumps are not duplicated in this archive; exact editions, URLs, statement numbers, and pagination are in the paper and source notes. The user's original attachments remain the supplied-source record.

On a normal TeX Live installation, build the self-contained paper by running `pdflatex -interaction=nonstopmode -halt-on-error CX_GRH.tex` twice. It uses standard packages listed in its preamble. The source assembly scripts in `work/` can also regenerate a `deliverables/` directory from the component files; the already assembled top-level source requires none of them.

The package includes SHA-256 manifests for its contents and for the final proof fragments. These are integrity records, not mathematical certificates. The finite test of the CX-N13 construction is a diagnostic only; the general result has a separate complete proof. All new proofs were read in full, and the actual readers and scope are recorded. No new finding is advertised as formally verified.

No earlier checkpoint ZIP is embedded. The first checkpoint is preserved separately under its original name.
