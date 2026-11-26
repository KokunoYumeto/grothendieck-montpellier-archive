# Build

This is an independently editable LaTeX project. The single `main.tex` contains the text and bibliography; there are no local inputs or figures.

Engine: pdfTeX with the standard LaTeX packages listed in the preamble.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

For a clean build, copy this project into an empty directory first. The returned `main.pdf` is built from such a fresh copy. Bibliographic/source verification and current mathematical release gates are in the associated records; successful compilation is not mathematical certification.
