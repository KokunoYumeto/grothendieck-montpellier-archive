# Build

Engine: pdfLaTeX (TeX Live), with the standard packages named in `main.tex`.

From this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. No shell escape, network access, bibliography download, or external source tree is required. Every local input is in `sections/`. Inline references are in `references.tex`.

For a clean reproduction, copy this directory to an empty directory, remove generated `.aux`, `.log`, `.out`, `.fdb_latexmk`, and `.fls` files there, and run the command above. The repository-level checking command and layout review are recorded with each version.
