# Building the paper

Use a standard TeX Live installation with pdfLaTeX, latexmk, AMS packages, lmodern, geometry, microtype, natbib, xurl and hyperref.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The source is standalone: all statements, full proofs and references are in main.tex. It reads no other paper, downloaded article or network resource. The author line is intentionally empty.

The reviewed PDF has 14 pages. A fresh source-only build has zero overfull boxes and zero unresolved references. The two complete readings of the preceding version carry over for the byte-identical mathematical body. The revised opening, model wording and contextual citation were reread, and all14 pages of the final PDF were individually inspected visually.

All congruence-section classifications are proved symbolically. The workbench programs congruence_quartic_and_order_check.py and congruence_lift_matrix_check.py give separate exact corroborations; their finite output is not an assumption in the written proof.

The text and original code are dedicated to the public domain under CC0 1.0. Third-party works are cited and linked, not included.
