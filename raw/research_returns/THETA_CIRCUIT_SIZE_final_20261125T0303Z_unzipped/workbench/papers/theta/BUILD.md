# Build the standalone paper

Engine: pdfTeX (LaTeX), tested with the installed TeX Live distribution.
All source inputs are local: `main.tex`, `leaves.tex`, `oddleaves.tex`, and editable TikZ `figure.tex`.
The bibliography is inline in `main.tex`.

```sh
cd papers/theta
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdftoppm -r 110 -png main.pdf rendered
```

For a clean returned-project build, copy this directory to a new temporary
directory first and run the same commands. Check the log for overfull boxes
above 2 pt, and inspect every rendered page. Build logs and render images are
temporary verification data and are not required to edit the paper.

The final deposit records the exact engine version, page count, overfull-box
check, visual review and read-through events.
