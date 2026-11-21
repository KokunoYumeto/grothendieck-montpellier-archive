# Frozen A01–A31 compilation, visual review, and package validation

Date: 21 November 2026. Build owner/reviewer: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.

## Result

**PASS.** The frozen standalone source compiled in three stable XeLaTeX passes to 88 pages. No canonical source or layout modification was needed. The matching reading PDF and current build manifest are installed.

- Source SHA256: `447fed6f4d8c8b3479fe08d96eb10c8cf8c7ae21840de43c7f2822615484e287`.
- PDF SHA256: `ed7908c3570a783dce30ef1c7289d6d583cad36281cd7319004f5edbdc92ded7`.
- Zero overfull boxes, undefined references, missing-character notices, or remaining rerun requests.
- Remaining compiler notices concern underfull spacing and the existing amsmath `over` command.

## Actual visual scope

All 88 pages were rendered with a 1600-pixel long edge. I visually inspected every page in ten contact sheets. I also inspected full-size pages 1, 8, 10, 12, 23, 35, 49, 65, 68, 70, 74–79, 82, 85 and 88: nineteen pages covering the revised abstract, dense proofs and bounds, tables, residual-scope summary and references.

The independent reviewer `/root/gt_certificates` opened and visually inspected every full-size page 51–64, covering all A26–A31 pages and the transition to effective Galois comparison. Its complete page-by-page report is retained as `qa/INDEPENDENT_PAGES51_64_VISUAL_QA.md`, with SHA256 `e99637792282aa6abf5eef424af7e2a08f2c4a55a0738be2f06210d1daf18cbf`.

Neither reviewer found clipping, overlap, missing glyphs, equation-label collisions, broken table boundaries or margin overflow. The snapshot retains all ten contact sheets and all 33 distinct full-size reviewed page images, with hashes of every one of the 88 generated images. The other full-size renders can be reproduced from the retained PDF and render script. This is a visual layout review, not a new mathematical rereading of every proof.

## Reproduction and installation

The executed build command was:

```sh
python final/reproduce/compile_standalone_tex.py --source final/AN_GRH.tex --build-dir work/effective_galois/tex_build/a01_a31 --format-dir work/row_audit/tex_build
```

The executed render command was:

```sh
python work/row_audit/tex_build/render_qa.py work/effective_galois/tex_build/a01_a31/AN_GRH.pdf work/effective_galois/tex_build/a01_a31/qa
```

The source hash was checked before and after compilation and again immediately before installation. The exact compiler commands, process-local environment overrides, all three pass logs, PDF metadata, render record, primary visual scope, and independent visual report are retained in `evidence/build/a01_a31/`. No source edit was made after the freeze; `LAYOUT_CHANGES.json` records an empty change list.

The previous 74-page A01–A25 source, PDF, logs and visual evidence remain intact under `evidence/build/a01_a25/`. Its former canonical manifest was preserved as `canonical_manifest_before_a01_a31.json`. The older A01–A20 evidence also remains intact. Installation updated only the current reading PDF and build manifest and added the new snapshot/evidence subtree.

## Full package validator

After installation, the actual command

```sh
python final/reproduce/validate_package.py
```

exited successfully. This was the **full package validator**, not merely its build-manifest function. It reported 1,371 question rows, 1,047 normalized check events without exact duplicates, 43 citation keys, and 124 retained source files with matching hashes. The expected row-register and finite-unit-certificate table sizes passed. Every numbered finding has a recorded mathematical proof-check event; A28 is intentionally presented as a cited and rechecked result rather than a new numbered finding.

The validator also verified the current source/PDF hashes, successful stable compilation, and visual-review scope matching the exact 88-page build. Its compilation warnings list is empty. A copy of this exact validator output is retained as `PACKAGE_VALIDATION_SNAPSHOT.json`; the live package result is `evidence/package_validation.json`.

The validator checks structure and evidence integrity. It neither establishes mathematical truth nor runs a proof assistant. The manifest explicitly records `formally_verified: false`.
