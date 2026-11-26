# Standalone build

Engine: pdfLaTeX (TeX Live with standard packages). From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The third pass stabilizes references if the first two report changed labels. The bibliography is inline. No external files, downloads, bibliography processor, shell escape or network access are required. The deliverable is `main.pdf`. Check `main.log` for unresolved references and overfull boxes.

Optional mathematical certificates in the accompanying programs directory require Python3 and SymPy (recorded version1.14.0). They are not needed to compile. The three distinct programs are `surgery_exact_certificates.py`, `surgery_algebraic_certificates.py` and `surgery_algebra_certificates.py`; the last is the root's separate Nori/Picard method. Outputs and original-source rerun provenance are in notes/checks.

Current verified build (2026-11-23T10:33:57.532915+00:00): 40 pages, three successful fresh standalone pdfLaTeX passes, with no warnings, unresolved references, or overfull/underfull boxes. All 40 complete rendered pages were visually inspected. Every current page differs from the prior reviewed 33-page release at 108 dpi because of the added material and repagination, so no unchanged-page exemption was used. Exact hashes, command environment, and per-page comparison are in `notes/paper04_collar_release_build_report.json` and `notes/paper04_collar_release_pixel_comparison.json`. The mathematical/source comparison and two-read record are separate in `notes/paper04_collar_release_review.md`.

Additional exact certificate (Python 3 standard library only), from the deliverables root:

```sh
python3 programs/paper04_strebel_polynomial_audit.py
```

Expected JSON: `checks: 5`, `passed: true`, slit radius `4`, half-plane radius `1`, both cross-multiplied coefficient arrays `["0"]`, cover coefficients `["2","2","2","-2"]`. This verifies finite rational identities only. The unchanged original checker rerun is recorded separately in `checks/paper4/strebel_original.json`.


Collar and circular-lens certificates (Python 3 standard library only), from the deliverables root:

```sh
python3 programs/paper04_collar_radius_identities.py
```

Expected JSON: `checks: 14`, `passed: true`. The program implements sparse polynomial arithmetic, factorial integration moments, rational inequalities, and arithmetic in Q(sqrt(-3)). It checks finite identities and the fixed comparison constants, not the global PDE or univalence arguments. Both unchanged original collar checkers were run only in temporary directories; their provenance and the new method's output are in `checks/paper4/collar_radius_comparison.json`.

The paper cites the programs once by their descriptive names through the proposed workbench. The name-to-file mapping is recorded in `notes/paper04_collar_radius_source_comparison.md`. The workbench is proposed; no repository publication or deposit is asserted.
