# Standalone build

Build from the five source files `main.tex`, `ample_difference.tex`, `finite_field.tex`, `spreading.tex`, and `no_zero_class.tex` with a standard TeX installation containing the packages declared in the preamble:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively run pdfLaTeX three times. No external data, bibliography processor or private macro file is required. The accompanying local-algebra program is independent of the typesetting build.

## Verified current edition

The fresh source-only build has **42 pages**. All three pdfLaTeX passes succeeded, with zero overfull boxes and no undefined references or citations. The source and build record is `audit/paper10_spreading_public/integration/build_final03.json`.

- `main.pdf`: `ffe492084e126016d7dfab8856c104db6e47bf20e0439490ebdfa38b5c3c57a3`.
- `main.tex`: `c86d75e5792d33eb978d383127ccfd31a001a37ad8b08dabfd31ec1fa524128d`.
- `spreading.tex`: `5adc55b07ce054d9d60bcec5b7bf253471d676d25260f161f04173d8716b5bf2`.
- `ample_difference.tex`: `694371865d03d24a48f0efdf5ec1a41bceb3e5ad5603fb7a1012d73a82fc35b8`.
- `finite_field.tex`: `f7d9ddf48a9609ea537a0e27575ba25bab3686cdedb0c9508b9a95ecf92f2d9b`.
- `no_zero_class.tex`: `8bce056157876dff01e64955f846e78dd50f43ca70ae7a3e66d484c2ae2cb0fa`.

The preceding final05 edition is preserved in `audit/paper10_spreading_public/integration/final05_snapshot/`, with its own manifest. The new proof and all changed opening, context, remaining-question, source and method text received complete expert and newcomer readings; earlier completed full readings carry only exact unchanged source. The visual record covers all42 final02 pages. Final03 changes only an exact standard-source tag: pages13 and42 were individually inspected, and the other40 rendered pages are byte-identical. Exact reader and page scopes are recorded in `audit/paper10_spreading_public/final_readings_and_QA.json`.

The eventual-rank theorem for every mixed pair has complete separate same-model statement-led reconstructions and reciprocal full comparisons at the explicit earlier theorem and standard-input scope. It does not settle smaller degrees, a uniform quantitative threshold, or the actual first-variation determinant. No human has checked the mathematics. The final active-file manifest is `audit/paper10_spreading_public/final_manifest.json`; prior manifests remain historical.
