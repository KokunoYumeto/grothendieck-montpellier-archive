# Algebraic cycles and motives workbench

This repository candidate contains one checked research paper on uniform bounds for algebraic cycles, its standalone editable source, and the proof, source and computation records needed to assess it.

Start with `work/UNFILED/v1/paper/main.pdf`. The paper has 120 pages; all 27 local TeX inputs and the inline bibliography are beside it. `paper/BUILD.md` gives the exact build command. The introduction states the main equivalence in its first pages and explains the uniformity quantifiers before the proofs.

## What is proved and what remains open

The main theorem expresses rational HC for all complex abelian varieties as a familywise uniform cycle bound tested at reductions of CM fibres. It uses the identified published geometric foundations. The paper also proves effective Weil extraction, lattice transport and degree estimates, stated conditional higher-dimensional bounds, minimum-degree specialization, and precise construction obstructions and Mumford correspondence criteria.

The paper does not prove HC. Uniform split Weil suppliers, the first non-Eisenstein eightfold detector and the exceptional Mumford supplier remain open. The positive Gaussian network solves diagonal trace equations only; full deformation and semiregularity remain open. See Section 33 and `checks/records/FINAL_STATUS.md`.

## Reading the records

Unless stated otherwise, the following paths are relative to `work/UNFILED/v1/`. `PREDEPOSIT_VALIDATION.md` and `FILING.md` are at the repository root.

- `STATEMENTS.tsv` indexes all 74 formal environments and 15 open, unchecked or refuted research assertions. Provisional suffixes are stable; printed theorem numbers can change.
- `CHECK_EVENTS.tsv` preserves prior events and adds final readings, with model and exposed effort information. Statement-only re-proofs, targeted checks, computations and complete-source readings are distinguished.
- `SOURCES.tsv` gives 67 cited sources, exact use and how each was read. Rich source hashes/access limitations are in `checks/records/source_details.tsv` and the final source audit.
- `checks/programs/README.md` gives the complete reproduction index. The standard-library Gaussian certificate checks 6272 exact equations. Finite character-catalogue computations explicitly state their scope.
- `DEPOSIT_SHEET.md` supplies the abstract, subject, keywords, provenance, opening-requirement map and credit list.
- `MANIFEST.sha256` identifies all version files. `PREDEPOSIT_VALIDATION.md` records the actual official-checker outcome; it does not call provisional identifiers a pass.

All source files are original work or original derived calculations. Other authors' papers, scans, source packages and unchanged attachments are excluded. No human has checked this work. Same-model review is not formal proof-assistant certification.

## Filing and licence

The user assigns the permanent WB number and record page. `UNFILED` is an explicit placeholder. No public commit, publication or deposit has been invented. `FILING.md` gives the remaining filing steps and the manifest/seal issue that must be resolved by the catalogue convention.

The original text and code are dedicated to the public domain under CC0 1.0. The dedication conveys no rights in cited third-party works, which are not included.
