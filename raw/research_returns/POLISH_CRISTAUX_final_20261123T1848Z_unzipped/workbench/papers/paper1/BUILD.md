# Building the paper

The project is standalone. Keep `main.tex`, `injectivity.tex`, and `positive_ranges.tex` together in this directory. It requires pdfLaTeX and standard TeX Live packages: amsmath, amssymb, amsthm, mathtools, lmodern, geometry, microtype, booktabs, enumitem, natbib, hyperref, and xurl.

From this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. The bibliography is included in `main.tex`, so BibTeX is unnecessary. There are no external figures, fonts, or local style files.

The arithmetic certificate can be run from the workbench root with:

```sh
python3 programs/paper1/pole_semigroup_certificate.py
python3 programs/paper1/iteration_certificate.py
```

Expected result: `"status": "PASS"`, characteristic-two values `g=7`, `h0_N=2`, `h0_N3=4`, `h0_L=6`, `h0_L9=556`, `B2=35`, and `embedding_dimension=561`. The iteration program also returns `"status": "PASS"`; its negative-cohomology dimension checks are 360, 1, 0 on the second Tango threefold and 1203, 1, 0 after the root cover, with a 361 lower bound on the degree-one integral kernel. These programs check finite arithmetic and transition identities; the geometric and cohomological arguments are in the paper.
