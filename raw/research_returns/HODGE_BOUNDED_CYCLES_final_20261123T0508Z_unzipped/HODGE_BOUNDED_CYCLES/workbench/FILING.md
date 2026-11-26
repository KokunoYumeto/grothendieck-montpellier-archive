# Filing this checked work

The deliverable is a predeposit candidate for format1 of the mathematics-workbenches catalogue. Its mathematical text and check records are complete. The registry assigns the work number and permanent page; this delivery does not assign one or assert a publication, push or deposit.

## Current layout

`work/UNFILED/v1/` contains the standalone paper, the three canonical TSV tables, the deposit sheet, `checks/` and a version manifest. `UNFILED.001` through `UNFILED.089` are visibly provisional identifiers. The first74 identify every theorem-like environment in the paper; the remaining15 preserve open, unchecked and refuted research assertions. The user's permanent assignment will replace only the prefix, preserving these suffix identities.

The paper defines the requested workbench URL and record-catalogue URL exactly once. Its author line is empty. The final PDF and sources have two complete same-model readings and all-page visual QA. No human review is represented.

## Filing sequence

1. Obtain the next official WB number and individual record page from the catalogue. Confirm the existing field repository row; do not create an unused empty repository.
2. Rename `work/UNFILED` to the assigned work number. Replace `UNFILED.` in the version tables, tag map and record references by that work prefix plus a dot. Preserve all suffixes and all prior check events. Fill the author line only as the depositor directs.
3. Replace the paper's `recordurl` with the assigned individual permanent page. If this changes the TeX, compile from a fresh copy and reconcile the changed front/closing matter and final PDF; the mathematical source-hash certificates otherwise describe this delivered text.
4. Set the real version commit/tag and paper-seal metadata using the catalogue maintainer's convention. Do not insert a fabricated commit, a hash of an absent file, or an unassigned registry page.
5. Regenerate `MANIFEST.sha256` over the complete version and run the official `tools/check_workbench.py` obtained from the catalogue. It is referenced, not bundled. The exact current predeposit result is in `PREDEPOSIT_VALIDATION.md`; the pending identifier faults are not called a pass.
6. Read the complete addition list for ownership and sensitive data, then deposit. Create `DEPOSITED.md` only after the actual deposit. From that point leave the version folder immutable; corrections belong in a new version with a dated record-page entry.

## Manifest and paper seal

The delivered `MANIFEST.sha256` hashes every file in the version except itself and a future `DEPOSITED.md`, exactly as the official checker specifies. The hash of that manifest is recorded outside the version in `PREDEPOSIT_VALIDATION.md`.

Format1 also asks the paper to print its version manifest hash and commit. Those filing identifiers have not been inserted into this unfiled paper. There is an additional seal-order issue to resolve with the catalogue convention: if a manifest hashes the PDF/TeX that contains the hash of that same manifest, naïvely rewriting either changes the other. This delivery does not claim to have solved that self-reference by printing a stale hash. The depositor must use the catalogue's chosen external-seal or prior-commit convention and record it explicitly. No special exception to the official format has been silently invented.

## Running checks without editing a version

The version's `checks/programs/README.md` lists all20 executable programs and their exact expected results. Run writing programs in a copied reproduction tree outside the deposited version. The standard-library Gaussian verifier reads its certificate without modifying it; the catalogue verifiers regenerate metadata files, so they too belong in the reproduction copy.

## Source and licence limits

Only original text, original programs and derived calculations are included. Other authors' papers, attached-source copies, scans, extracted source text, package implementations and complete source datasets are excluded. The source ledger records references, exact used locators, access limits and hashes. CC0 applies only to the original work in this repository candidate.
