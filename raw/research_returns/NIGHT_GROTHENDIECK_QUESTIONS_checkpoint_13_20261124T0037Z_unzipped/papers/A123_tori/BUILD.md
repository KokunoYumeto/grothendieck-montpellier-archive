# Build and exact checks

This is a standalone LaTeX project. The complete article and its inline bibliography are in `main.tex`. There are no local inputs, custom styles, external bibliography files, or figures.

The checked engine is pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev (Debian), with LaTeX2e 2024-11-01 patch level 2. It uses standard packages: `fontenc`, `inputenc`, `lmodern`, `microtype`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `booktabs`, `array`, `longtable`, `enumitem`, `natbib`, `hyperref`, and `xurl`.

From this directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The third pass stabilizes page references after the first fresh build. Subsequent unchanged builds require no extra pass. The output is `main.pdf`, currently 17 pages. The delivered PDF was built from a fresh directory containing only a copy of the returned `main.tex`. There are no overfull boxes, underfull boxes, undefined references, or unresolved citation warnings in the stable log. Author metadata and the author line are empty.

Every page was rendered and visually reviewed. The complete text was reread for mathematical correctness and then for exposition. The external records distinguish targeted mathematical review from independent statement-only re-proofs. The folding refinement and the eight outer-fixed opposite classes in type A3 have a separate same-model statement-only re-proof. The additional all-types baseline statement-only review is complete: it independently reconstructed the count, freeness, all-types opposition classification, outer-fixed existence criterion, and split type-A field criterion, with the published cyclic-element theorem and standard Lie theory explicitly retained as inputs. Its exceptional-root certificate is preserved with the external check records.

## Reproduce the finite calculations

Python 3.8 or later, standard library only:

```sh
python apposition_certificates.py > reproduced_certificates.json
diff -u certificates.json reproduced_certificates.json
```

Expected: successful exit and no differences. The JSON reports:

- The 27 and 56 extremal weights in the chosen `E6` and `E7` representations, with Coxeter cycle lengths `[3,12,12]` and `[2,18,18,18]`.
- All 48 and 240 roots for `F4` and `E8`, their displayed reflection words, highest-wedge tests, heights, and Coxeter powers.
- The exact skew-adjoint classical matrices in ranks 2 through 8; the 64 allowed `C2` Borel pairs; and the two fundamental `G2` pairing tests.
- Counts of classes for Fourier models of degrees 2 through 5: `1,2,18,144`, with `1,0,8,0` inverse-transpose-fixed classes.
- In degree 4, 16 opposite classes and 8 classes that are both opposite and outer-fixed.
- Affine fixed-point-free involution counts in even degrees 4 through 24, including the pointwise-principal-cyclic-group condition. The latter leaves four degree-4 classes.

These finite exact checks supplement the symbolic proofs. They are not proof-assistant formalizations, and the rank range of a calculation is not a substitute for the general arguments in the paper.

## Rights

The article, original program, and original records are dedicated to the public domain under CC0 1.0. Third-party publications and archive scans are cited and linked; none is included in this project.
