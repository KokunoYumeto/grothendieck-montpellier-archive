# Building the paper

Engine: pdfLaTeX (TeX Live), orchestrated by latexmk. In this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Inputs: analytic-weil-sheaves.tex, effective-sixfolds.tex, eisenstein-eightfolds.tex, equivariant-eightfolds.tex, finite-cover-eightfolds.tex, galois.tex, gaussian-trace-networks.tex, introduction-additional.tex, localized-support.tex, main.tex, mumford-coniveau.tex, mumford-fiber-product.tex, mumford-surfaces.tex, mumford.tex, one-prime.tex, polarization-quotients.tex, pure-weil-complexes.tex, references.tex, research.tex, sign-cube-obstruction.tex, simple-hodge-bundles.tex, sixfolds.tex, small.tex, spin-obstructions.tex, theta-eightfolds.tex, tree-extension-obstruction.tex, weil.tex. Only standard TeX Live packages and Latin Modern fonts are used. No network access or external bibliography processor is required.

The current 120-page PDF was compiled from a fresh copy of every local input. The build has no warnings or overfull/underfull boxes. All 120 pages were visually inspected. Complete expert and newcomer source readings cover all 27 inputs, and both final source manifests match these delivered files. The separate visual and source-reading records state their scope and limitations. The PDF SHA-256 is `e8d7f3743f495bd576b44cd1a6c5138d655a7128756c8fee380dfe6f84411abd`.
