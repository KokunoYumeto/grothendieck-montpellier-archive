# Building the heat-flow note

Compile `heat_subdiscriminants.tex` twice with pdfLaTeX in a directory containing the source file. Its bibliography and TikZ figure are embedded. On the shared Windows host, acquire the existing single TeX slot before compilation.

```sh
pdflatex -no-shell-escape -halt-on-error heat_subdiscriminants.tex
pdflatex -no-shell-escape -halt-on-error heat_subdiscriminants.tex
```

The independent exact computation uses the Python standard library.

```sh
python -I -B check_heat_minors.py
```

The supplied PDF has three pages. The exact check reports 66 partitions and 416 principal minors.
