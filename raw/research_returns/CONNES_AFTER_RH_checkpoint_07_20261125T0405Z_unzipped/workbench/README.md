# Connes’s Lemma 3 in characteristic zero

This workbench studies the exact zero measure seen by a growing arithmetic prolate cutoff. The manuscript is `paper/main.tex`, with its PDF beside it. The complete Dirichlet full-index proof and the auxiliary deep-Hankel Hecke proof have passed targeted checks. The proof for every fixed Hankel threshold is integrated; its complete expert addendum and newcomer delta review have passed. Separate statement-only work reconstructs the natural transfer, the arithmetic mean-square and functional estimates, and the principal completion; the deep upper bound and uniform mass remain premises of that independent reconstruction. Both recorded whole-manuscript reads are complete. The windowed Godement–Jacquet construction has three checked finite-scale propositions, while its zero-limit gate remains open. Read `QUESTIONS.tsv` for the exact cutoff choices and remaining questions; the full statement-only reproof attempts are separately recorded as incomplete.

## Reading order

1. The paper introduces the cutoff and the harmonic zero measure.
2. `LITERATURE.md` compares the earlier cutoffs, with exact source locators.
3. `STATEMENTS.tsv`, `CROSSWALK.tsv`, and `CHECK_EVENTS.tsv` identify proof and review scope.
4. `research/` contains original proof-development and review records. These records distinguish statement-only re-proofs, targeted checks, and computations.
5. `checks/` and `certificates/` contain reproducible supporting calculations. Floating-point illustrations are not proof certificates.

## Build and checks

Run `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` inside `paper/` using pdfLaTeX. Run the two Python check programs from the workbench root; their expected outputs are described in `REPRODUCE.md`.

## Filing and identity

This is a staging directory for format 1 of the mathematics-workbenches registry. No WB number, permanent statement number, commit, deposit, or publication is claimed. The user assigns those when filing. The `CA-` tags are stable staging identifiers; the crosswalk preserves them when registry tags are allocated. A version manifest accompanies each returned archive. Registry metadata must be filled before public deposit, including the manifest hash and commit printed in the deposited paper. There is no `DEPOSITED.md` because this work has not been deposited.

All deliverable text and code were produced in this task and are dedicated to CC0 1.0. External works and unchanged attachments are cited, never included. No human has checked this work.

## Checkpoint07 additions

The 101-page manuscript includes the fixed-threshold harmonic cutoff for every fixed primitive holomorphic cuspidal newform, including weight one and complex nebentypus, and its specialization to every odd irreducible two-dimensional Artin representation. The full targeted proof and generalized delta checks passed. The separate statement-only reconstruction has established its packet and smoothed-transfer components; its bulk local upper bound and uniform mass estimates remain incomplete. The current source has a complete newcomer read of all 24 recursive TeX files, a fresh standalone build with no undefined references or overfull boxes, and visual inspection of all 101 pages. Exact scopes and hashes are recorded in research/. The prescribed GLn harmonic limit remains open.
