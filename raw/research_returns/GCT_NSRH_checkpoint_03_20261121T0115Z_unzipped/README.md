# GCT_NSRH research package

**Status: WORK IN PROGRESS — active research checkpoint material.**

Read `GCT_NSRH.tex` (and its compiled `GCT_NSRH.pdf`) for the mathematical argument, `QUESTIONS.tsv` for exact item states and next gates, `CHECK_EVENTS.tsv` for the real verification events, `LEDGER.md` for dated changes, and `IMPLICATIONS.md` for scope and consequences. The authoritative statements are the current paper; agent memoranda document source work, alternative approaches and checks, and can contain earlier wording explicitly corrected later.

## What has been checked

The paper now integrates F01–F42, with complete proofs; full proof reviews and exact scopes are in CHECK_EVENTS.tsv and the review files. The newest generated fragments are matched separately to their reviewed reports. Literature theorems are cited with locators; reading a source statement is not represented as independently checking its entire proof. The path numerical checks and exact character script are supplementary. No Lean verification of this paper is claimed. The prompt's stipulated Alpöge results are accepted as premises; the supplied short Lean wrappers are not the absent imported development.

The main application to designated nonstandard canonical bases remains open. The classical pure Tate Satake realization, actual rank-three right action, finite normalized-trace obstruction, derived rank-one comparison, and all-rectangle Young-orbit obstruction have been proved. The actual nonstandard branching tower, primitive Grassmannian coefficient motives, and countable-spectrum/visible-duality extension are integrated. Explicit stack traces, coherent Frobenius repairs, tensor-inversion obstructions and the smooth proper category test now sharpen the realization gate. F40 supplies a checked smooth corner resolution retaining the actual collision algebra and tensor action. Its relative extension and a joint positive left/right action are actively being tested. The known Kahle–Michałek theorem refutes the attached homogeneous PH1; the current package distinguishes that closed historical target from later formulations. None of these results settles the designated canonical-basis comparison.

## Resume information

The input archive was unpacked once and its nested literature bundles were already directories. `SOURCE_MANIFEST.json` records the unchanged supplied files. Original attachments remain the source of those materials; they are not duplicated in this package. External complete PDFs and archive scans are research inputs and are not redistributed. Their exact references and selected-leaf descriptions are in the paper and source memoranda. The selected-page retrieval script is retained for reproducibility where relevant.

`RUN_METADATA.md` records the start and review/checkpoint schedule. Checkpoint ZIPs must be saved every45 minutes of active work, under new numbered names, with no old checkpoint nested. The first scheduled progress review is approximately three hours after start, then hourly; the two-consecutive-no-movement stop rule has not yet been triggered. Packaging itself does not count as progress.

Model: GPT-6 Astra Pro as supplied by the runtime. Precise effort setting: not exposed. All model/effort/run records retain that limitation.

## Reproduction

Compile the LaTeX with a normal pdfLaTeX installation using the standard AMS, geometry, booktabs, longtable, enumitem, microtype, hyperref and fancyhdr packages. Two passes resolve references. This environment needed a locally generated pdflatex format because its system format cache was absent; that is an environment repair, not a paper dependency.

Run `python3 check_path_bound.py` for the finite numerical path checks. The script's output records the tested range and tolerances. Run the separate exact character script according to its main section for its certificate. These computations do not replace the displayed proofs.

Exact symbolic rank-three matrix identities can be reproduced with `python3 verify_rank3_matrices.py`. The reports retain failed proposals and their repairs; they are not all assertions of the current paper. No earlier checkpoint ZIP is contained in this package.
