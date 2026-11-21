# HECKE_DIV_20261121

## Bounded division on Hecke orbits

**Date:** 21 November 2026.

This archive contains the completed research report, its sources, exact arithmetic certificates, and proof-review records. The main report is **`HECKE_DIV.pdf`**. Its companion **`HECKE_DIV.tex`** is a flattened, self-contained LaTeX source with the bibliography included. The original modular LaTeX sources are retained in `source_tex/` for editorial reference; they are not needed to compile the flattened file.

The report treats fixed rational flat Hodge or Weil classes in fixed polarized families. Cycle degree always means the intersection degree of each **integral effective positive and negative part**, without factorial normalization. Every uniform bound is subject to the stated class, polarization, lattice, and family hypotheses.

## File guide

| File or directory | Contents and recommended use |
|---|---|
| `HECKE_DIV.pdf` | Complete report, with proofs, exact source locators, numerical bounds, and a separate discussion of stronger extensions and source limitations. Start here. |
| `HECKE_DIV.tex` | Complete flattened source for the report, including its bibliography. |
| `IMPLICATIONS.md` | Consequences of the findings, explicit fourfold and eightfold formulas, dependency statements, and mappings to the supplied sketch and earlier run labels. |
| `QUESTIONS.tsv` | Source questions, exact locators, final states, finding identifiers, and the result or remaining limitation for each question. |
| `CHECK_EVENTS.tsv` | Actual proof-reading, independent-reconstruction, and computational check events, with their scopes and outcomes. |
| `LEDGER.md` | Final research status, dated historical updates, movement, checkpoint timing, and verification conventions. |
| `TRANSCRIPTION_NOTES.tsv` | Verified archival or bibliographical corrections, with confidence and limitations. |
| `SOURCE_MANIFEST.tsv` | Paths, sizes, and SHA-256 hashes of the twelve supplied originals in `source/`. |
| `MANIFEST.sha256` | SHA-256 checksums for every other file in the final archive. |
| `source_tex/` | Modular LaTeX sources used to assemble the flattened report. |
| `work/REPRODUCING_COMPUTATIONS.md` | Full script inventory, dependencies, execution order, asserted checks, output files, existing timings, and the distinction between arithmetic and geometric proofs. |
| `work/primary_sources/` | Preserved Severn version 1.5 PDF and TeX with their download URLs and SHA-256 hashes. |
| `work/` | Exact Python scripts and saved results, source audits, independent mathematical reviews, and intermediate research notes. |
| `source/` | The twelve supplied original inputs, including the Markman LaTeX source, bridge sketch, supplied papers, statement index, and Lean entrypoint files. The manifest identifies each input. |

The identifier prefixes provide a compact route through the report: **R** for corrected reductions, **P** for quantitative and motivic propositions, **M/MR** for the Markman construction, **SQ** for the eightfold quantitative extraction, **A** for arithmetic routes, and **G** for the archival correction.

## Mathematical status

### Fourfold route through Markman

The report uses Markman's *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds* (2025, arXiv:2502.03415v2), particularly Theorem 1.5.1 and Corollary 1.6.1, as the cited geometric input. The qualitative fourfold conclusion is distinguished from the new numerical extraction.

Findings **M7–M10** give the quantitative route: explicit output and normalized regularity, effective Chern-cycle degrees on the sixfold source, controlled lattice and polarization comparison, and the compensation correspondence to the principal split fourfold family. The normalized regularity is `2065542`; a sufficient effective source degree is

```text
3426088289770714707027306735206400
```

The report and `IMPLICATIONS.md` give the resulting bounds for every fixed rational Weil target, including a single common multiplier. The argument uses the proved local regularity and cycle-locus mechanisms; it does not assume that all the deformed sheaves are globally slope-stable or Gieseker-stable. The specific higher-genus semiregularity obstruction is also recorded with its exact scope.

### Split eightfold route through Severn

Findings **SQ1–SQ9** extract explicit uniform bounds from the supplier and dominance construction in Severn (2026), *Weil classes on abelian sixfolds and eightfolds of Weil type for Q(sqrt(−3))*, Hexagon **2610.00387v2**, internal **version 1.5**, dated **21 October 2026**.

**This unrefereed manuscript is retained as a geometric input.** The supplier construction and its repair, the transfer, and the dominance argument received the targeted readings identified in the report. The finite reflection group, parabolic basis, cup-product form, and all seventeen geometric monodromy matrices were reconstructed exactly. The new degree and denominator estimates are proved separately in SQ2–SQ9; they are not attributed to Severn's manuscript.

The conclusion concerns a fixed polarized split Weil datum over `Q(ω)` with an integral `Z[ω]`-stable lattice, including the principal balanced `E⁸` datum. The degree bound is an explicit finite factorial expression. The report also supplies integral clearing and degree bounds for every fixed rational Weil class and a common-multiplier variant. These are sufficient bounds, with no assertion of optimality or practical decimal expansion. The Weil-plane conclusion is distinguished from a full Hodge-conjecture statement for every additional class on every special eightfold.

### Reductions, arithmetic, and verification

The report proves the corrected bounded-Chow, tensor-compatible Hecke, and CM-sequence reductions, and states the exact bounded-prime lifting criterion. It records counterexamples to the unqualified signed-divisor-degree and extra-endomorphism-degree assertions in the supplied sketch. The positive fourfold and eightfold bounds do not use RH or GRH.

The proof-review ledger distinguishes cited inputs, new proofs, independent reconstructions, and exact computations. **No formal Lean verification of this report is claimed.** The supplied Lean entrypoints were inspected in their stated source context; their full dependency trees were not compiled. The Python calculations check finite algebraic statements and do not replace the geometric proofs or change the publication status of cited sources.

## Reading historical working notes

The final report, `QUESTIONS.tsv`, and `IMPLICATIONS.md` state the completed conclusions. Earlier notes in `work/`, and any retained checkpoint or ledger records, preserve the sequence of the research. They can contain statements that a numerical degree was still unknown, an independent check was pending, or an initial regularity estimate was weaker. Those entries describe their dated stage and are superseded where the final report gives the completed argument.

Similarly, some result files retain historical weaker arithmetic fields alongside explicitly named improved bounds. The reproduction guide identifies these cases. A repeated execution of the same script is not counted as an independent derivation, and a file hash establishes identity relative to a checkpoint rather than mathematical correctness.

## Rebuilding the PDF

From the archive root, use a normal TeX installation with the packages named in the preamble, including the AMS packages, `mathtools`, `lmodern`, `microtype`, `geometry`, `booktabs`, `longtable`, `array`, `enumitem`, `natbib`, `xcolor`, `hyperref`, `fancyhdr`, and `xurl`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error HECKE_DIV.tex
pdflatex -interaction=nonstopmode -halt-on-error HECKE_DIV.tex
pdflatex -interaction=nonstopmode -halt-on-error HECKE_DIV.tex
```

The repeated passes stabilize the cross-references and contents; the clean build of the supplied flattened source required three passes. The bibliography is embedded, so no separate bibliography database or BibTeX pass is required. The modular files in `source_tex/` are editorial sources, not compilation dependencies of the flattened file.

## Reproducing the exact computations

The recorded environment is **Python 3.12.14** and **SymPy 1.14.0**. The scripts use exact integer and rational arithmetic; the independent projector and Markman checkers also include implementations using only the Python standard library. Detailed descriptions and the complete dependency map are in **`work/REPRODUCING_COMPUTATIONS.md`**.

Run from the archive root with ordinary Python, without `-O`, so assertions remain enabled. Install SymPy in the chosen Python environment if necessary:

```sh
python -m pip install sympy==1.14.0
```

An ordered reproduction sequence is:

```sh
python work/compute_projectors.py
python work/check_projectors_independent.py
python - <<'PY'
import json
from pathlib import Path
root = Path('work')
rows = json.loads((root / 'projectors.json').read_text())
row = next(row for row in rows if row['n'] == 3)
(root / 'projector_n3.json').write_text(json.dumps(row, indent=2) + '\n')
PY
python work/check_projector_n3_independent.py
python work/integral_seeds.py > work/integral_seeds.json
python work/markman_regularity.py
python work/markman_output_numbers.py
python work/check_markman_numbers_independent.py
python work/check_severn_printed.py
python work/severn_monodromy.py
python work/severn_group.py
python work/severn_pants.py
python work/severn_quantitative.py
```

The projector producer includes **`n=2,3,4`**, corresponding to dimensions four, six, and eight. The sixfold case has an additional independently coded check. The extraction command creates its separate input file for that check and the Markman calculation.

Rerunning these commands replaces their result files. `integral_seeds.py` prints its JSON, hence the explicit redirection. The group and pants programs import `severn_monodromy.py` and thereby repeat its top-level reconstruction; this expected side effect is described in the reproduction guide. Several conclusions are saved as Boolean fields, so inspect the recorded success flags as well as the process exit status. The saved outputs contain the successful checks from the research run.

The enormously large supplier bounds and common least common multiples are retained as explicit integer expressions. Their decimal expansion is not needed for the proofs or for reproducing the finite arithmetic certificates.

The metadata builders `work/build_metadata.py` and `work/consolidate_checks.py` document how the historical tables were assembled. They are not proof-verification programs: rerunning them does not perform a new proof reading or create an independent check. The original event files and final consolidated ledger retain the actual scope of the checks performed in this run.
