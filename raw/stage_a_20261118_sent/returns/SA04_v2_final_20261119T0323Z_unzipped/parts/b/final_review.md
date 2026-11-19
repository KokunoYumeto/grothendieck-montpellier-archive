# Independent final locator, direction, and packaging review

Review snapshot: 19 November 2026, 02:56 UTC. Reviewer: stream B, GPT-6 Astra Pro. This review checks source locators, reference integrity, and assembly requirements. It adds no mathematical scope and changes no verdict. The only final file edited was `final/SA04_directions.md`, following the root agent's explicit follow-up instructions.

## Directions

All 30 numbered directions have an item reference, a claim reference, a problem reference, author provenance, a bounded aim, known limits, a first step, an interest rank, and a separate feasibility score. All active references resolve against the final registers at the review snapshot. The old identifiers C-SA04-217, MP-SA04-201, and MP-SA04-204 occur only in the introductory explanation of their consolidation into C-SA04-122, MP-SA04-164, and MP-SA04-168 respectively.

Two authorized changes were made during this review:

- Direction 12 now cites MP-SA04-168 once, with MP-SA04-204 retained only as an introductory alias.
- Direction 13 and the priority table now describe Néronian targets without a semiabelian restriction. They state that scans 48 and 53 already remove that restriction, that the exact SGA7 I extension result is identified, and that the no-Ga fact has both an opened BLR1990 §10.1 Proposition 8, pp. 293–294 match and an independent proof in this audit. The future task is confined to remaining image and pushout construction inputs and a specified good-reduction variant.

The structural check is saved in `outputs/b_final_review.json`. The three old identifiers in the introduction are deliberate historical aliases, not unresolved operative references.

## Reading locators

Twelve root reading rows used descriptions after the filename rather than numeric line locators. Every replacement was chosen after reading the actual numbered transcription passage. The proposals are saved in:

- `parts/b/root_reading_locator_patch.tsv`: keyed old/new line fields, with source-check explanations.
- `parts/b/root_reading_rows_corrected.tsv`: the full root reading snapshot, changing only those twelve line fields.

Apply the keyed patch to the current register if root edits have continued. The full snapshot should not overwrite unrelated later changes. A numeric multirange such as `codex/K93-12_transcription.tex:113;122–125` is already a valid locator and was not changed.

The replacements identify the ordinary characteristic-two normal form, Proposition 6.1 cross-reference, genus-one duality, the degree-two differential-operator factorization, Gauss–Manin bidegree and base-form entries, Cartier's target/splitting/axioms, the p-curvature tensor target, the determinant sign, and the imperfect-field conic example. They do not decide the manuscript ink or alter the proposed mathematical reading.

## Cross-reference item locators

Stream C independently noticed abbreviated or descriptive target locators in SA04-268 through SA04-279. The resulting patch is `parts/b/cross_reference_item_locator_patch.tsv`. It gives complete JSON arrays for the existing `lines` field, preserving the statements and verdicts.

The patch expands Codex filenames and exact ranges for the later connection, Gauss–Manin, Cartier, p-curvature, Picard, obstruction, and organizational-plan passages. It removes the malformed Pro-prefix-before-Codex locator in SA04-276. For SA04-277–279 it adds the actual second-package period, differential-operator, and torsor passages instead of the descriptive dossier names. In SA04-268 the supplied scans 135–140 are in K93-01, lines 2–273; K93-02 is not their source. These are explicit navigational repairs to cross-references already discussed in the audit.

## Remaining reference and manifest corrections

The following changes belong to root assembly:

1. `C-SA04-448.fate_date` still contains the old free-text key `deJongErratum`. Replace that token with `deJongErratum1999`; its structured `refs` array is already canonical. Old keys in bibliography annotations labelled “Additional stream verification” and in `BIBLIOGRAPHY_PROVENANCE.json` record provenance and need not be erased.
2. `SOURCE_MANIFEST.json` currently gives `SA04_texts/PREAMBLE.tex`, line 19, a scan marker with cote `C` and scan `N`. Those are arguments in a macro example, not manuscript identifiers. Keep the file's hash and line count, but exclude the example from scan markers; limiting scan-marker extraction to transcription files is sufficient.
3. After MP-SA04-204 is consolidated into MP-SA04-168, update `ID_ALIASES.tsv` and the README's “two” consolidations/aliases wording. There are three claim/problem absorptions and the separate indexed-entry reassociation.
4. Stream C has separately reported four supplement events whose type is abbreviated to `refuted`; the required full taxonomy is `refuted, with the refined statement’s id`. Their outcomes already name the refinement IDs. This is a formatting correction, not a change to the check performed.

## Unindexed source and packaging checks

The current root source-derived register contains 59 items, each with an empty indexed-source list and explicit transcription locators. This is the intended representation for additional sources: none should acquire an invented `NOTES_INDEX` verdict. The final entries table contains no Codex-derived index IDs. The source manifest covers the supplied Codex and mixed Pro transcriptions and notes, while `SOURCE_SCOPE.tsv` distinguishes the three main cotes from the catalogue-only cotes and describes the cote161-5 material contained in the second93 package. The absence of source scans or second-pass files is correctly disclosed and is not an assembly gap.

The nine substantive computation programs checked in this review all have saved result files: the A, B, and C computation programs; B's supplement and Tits check; C's Manin and genus-two checks; and root's general and GIT computations. The detailed path-to-output mapping is in `outputs/b_final_review.json`. This confirms the presence of those calculation artifacts; it does not assert that a finite computation proves every unrestricted mathematical claim. Existing proof notes state those distinctions.

Eleven saved programs contain the original absolute workspace path. Their code and outputs are present, but the README's generic reproduction instruction is not sufficient to run them unchanged in an arbitrary new directory. Either document the original-path mapping/path substitutions or convert those path constants to paths relative to each program before the final reproduction instructions are issued. The JSON review lists the exact programs. External PDF/OCR caches are intentionally outside the package; their bibliographic URLs, locators, checks, and search records remain in the audit. No redistribution of those source copies is needed to satisfy the supplied packaging instructions.

At the review snapshot, `SA04_dossier.md` and the final-root copy of `progress.log` were still pending; root explicitly said both were being assembled. Their temporary absence is not reported as a completed-package defect. The completed ZIP must include them, the final registers, `CHECK_EVENTS.tsv`, all written programs and saved outputs, and the stream analyses/proofs/search logs needed to document the work. The log must include the actual UTC end time. Original attachments and earlier checkpoint ZIPs should remain outside the final ZIP, as the supplied instructions require. Only `SA04.zip` should be offered as the final download.

## Review artifacts and boundaries

`programs/b_final_review.py` preserves the manually chosen locator proposals and runs only structural reference, field, and file-presence checks. Its detailed and concise outputs are `outputs/b_final_review.json` and `outputs/b_final_review_stdout.json`. No root register, final register, bibliography, manifest, or assembly program was edited during this review. The authorized directions edits are identified above.
