# GCT_NSRH research package

**Status: WORK IN PROGRESS.** This is an active research checkpoint, not the final return. The scheduled stop rule has not been triggered. Read `STATUS_TIME.txt` for the current TeX/PDF build state and `REVIEW_STATE.json` for the exact next review and consecutive no-movement count.

## Entry points

- `GCT_NSRH.tex` is the authoritative current paper. `GCT_NSRH.pdf` is its compiled reading copy; the checkpoint-specific QA record identifies the exact checked hashes and page count.
- `QUESTIONS.tsv` records each question, its actual state, the strongest proved gate, approaches tried and next step.
- `CHECK_EVENTS.tsv` records what checks actually occurred, including reviewer, model, effort visibility, method and exact result.
- `LEDGER.md` records dated changes. `PROGRESS_REVIEW_*.md` and their frozen question snapshots implement the user's hourly movement test.
- `IMPLICATIONS.md` states what the findings change for the GCT route and the Grothendieck framework.
- `TASK_PROMPT.md`, `RUN_METADATA.md`, `CHECKPOINT_INDEX.tsv` and the source manifests support a precise continuation.

## Current mathematical scope

The current paper integrates F01–F69, including the complete bounded scalar-complex closure in F59, the separate central polynomial-coefficient analysis, the fixed arithmetic-parameter classification in F65, positive whole-tensor construction F66, whole-output iteration obstruction F67 and universal actual-object inversion obstruction F68, and actual variable-group quotient with its composition boundary F69. Active supplements and later reports are accepted findings only after their complete proofs and final fragments have been checked and explicitly integrated. Their mere presence in a checkpoint does not promote a draft to a paper theorem.

The main question remains the transfer from the stipulated sign-only mechanism to the designated nonstandard GCT objects. The paper proves exact sufficient spectral/duality criteria and constructs actual trace, perverse, graded-kernel and tensor realizations in the stated cases. It also proves limits of several stronger comparison routes. Those results do not identify the designated canonical basis, supply the missing independent local and dual estimates, establish general rectangular multiplicity positivity, or prove a complexity separation.

The current ordinary type-A scalar route is closed for every bounded scalar coefficient with the required Euler class. The distinct perfect diagonal-coefficient route requires nonflat cohomology on both sides, the designated generator class, and actual centrality and quadratic maps. Actual nonproper geometry and its Chern extension are retained. Strict effective iteration, naive weight/cohomology extraction and actual coefficient inversion fail in the exact tested senses. Mixed, filtered and genuine geometric quotient operations have their own remaining comparison obligations.

The original homogeneous PH1 in the attached GCT VI version is distinguished from later formulations and is refuted by the precisely cited known Kahle–Michałek result. The prompt's Alpöge theorems are accepted as stipulated premises; this research does not re-referee them. No Lean verification of this paper is claimed, and the supplied short wrappers are not represented as the absent imported Lean development.

## Verification and historical records

Every integrated new finding has a complete proof and a separate PartIII Grothendieck-framework dictionary with exact locators. The author and independent review files retain the specific scopes of their checks. A source-statement/context reading is not reported as an independent verification of its whole literature proof. Numerical and symbolic certificates are supplementary to the proofs. The main QA record describes actual full-page contact-sheet and selected detailed-image inspection; it does not claim inspection of images that were merely generated.

Agent memoranda and older integration scripts document the work, including failed proposals and corrections. They can contain historical wording superseded by a later explicit correction. The current paper and current question gates control. Do not rerun old integration or scheduled-review scripts indiscriminately: most are one-shot mutations of an earlier state. The final F66 coherence proof restores labeled coefficient order by canonical symmetric permutations; the earlier raw-reduction overstatement is explicitly recorded as corrected.

The runtime identifies the model as GPT-6 Astra Pro. The precise reasoning-effort setting is not exposed. Records preserve that limitation.

## Inputs and continuation

The supplied archive was unpacked once; its nested literature bundles were already directories. Do not extract it again into an existing source tree. `SOURCE_MANIFEST.json` records the supplied materials. Original attachments and complete external research PDFs/scans are not duplicated in each checkpoint; `EXTERNAL_INPUT_MANIFEST.json`, exact bibliography locators and source memoranda identify them and their access status. Restore the attached source tree beside this work directory if resuming from the checkpoint in a fresh environment.

Checkpoint ZIPs are created every45 minutes under new increasing names. No checkpoint may be overwritten or nested inside another. Mathematical movement means an existing open row closes or a main gate strictly narrows; new side rows, source refinements, restatement and packaging do not qualify. The dated hourly reviews, beginning approximately three hours after the start, apply the two-consecutive-no-movement stop rule. A checkpoint is not a scheduled review and does not reset its count.

## Reproduction

Compile the paper twice with pdfLaTeX and the standard AMS, geometry, booktabs, longtable, enumitem, microtype, hyperref and fancyhdr packages. This environment required a locally generated pdfLaTeX format because its system format cache was absent; that environment repair is not a mathematical dependency.

`build_checkpoint_pdf.py --number NN` runs two passes, checks serious build diagnostics, renders every PDF page and prepares contact and detailed images. Its temporary rendered PNGs and format/build cache can be reproduced; the retained QA reports document the actual inspections and hashes. `package_run.py checkpoint --number NN` is deliberately time-gated and refuses overwrite. It snapshots member bytes once, writes a per-member manifest and verifies ZIP integrity. The final package is made only under the user's stop rule or an actual session ending.

Exact computation scripts are individually named `verify_*.py`; their associated reports state the formulas and finite scope checked. The finite path script is `check_path_bound.py`. None of these scripts certifies a broader source conjecture or replaces the full displayed proofs. No earlier checkpoint ZIP is included in this package.
