# Independent audit of the assembled registers

Auditor: GPT-6 Astra Pro, effort inherited and not separately exposed, SA04 stream C. Audit date: 19 November 2026. Final files and root files were read only. The reproducible checker is `programs/c_final_register_audit.py`; its complete findings, input hashes and snapshot timestamp are in `outputs/c_final_register_audit.json` and its stdout in `outputs/c_final_register_audit.txt`.

## Counts in the final assembly independently rechecked at 03:10:23 UTC

| Register or check | Count |
|---|---:|
| Indexed entries | 432, exactly once each |
| Items | 448 |
| Claims | 372 |
| Problems | 131 |
| Reading alarms | 163 |
| Links | 90 |
| Bibliography keys | 140 |
| Check events | 1,422 |
| Items lacking a check event | 0 |
| Claims lacking a check event | 0 |
| Bibliography keys lacking a check event | 0 |
| Orphan check-event identifiers | 0 |
| JSON field-schema errors | 0 |
| Item/claim class, kind, check, status or confidence enum errors | 0 |
| Broken claim/item/problem reference identifiers | 0 |
| Wrong-cote or out-of-range numeric source intervals | 0 |
| Blank-only exact source intervals after the A correction | 0 |
| Declared scans absent from their source ranges after the locator corrections | 0 |
| Event rows requiring the single exact category spelling | 0 |

All four specified TSV headers match their exact requested fields. No required TSV cell is empty. The nine source-only Codex claims with empty `items` lists still have precise source locators and check events; these are not broken references. The two problems with empty bibliography lists explicitly report an unidentified fragment or an independently completed lemma with no exact literature match, rather than claiming an opened reference that is absent.

## Final event vocabulary and coverage

The final snapshot contains no outstanding event-category defect. All39 refutation events now use the exact category `refuted, with the refined statement's id`. The earlier four abbreviated rows, eleven missing-apostrophe rows and nine curly-apostrophe rows were corrected by component regeneration and the assembler's explicit canonicalization. Their mathematical outcomes and refinement identifiers were preserved.

| Actual operation | Events |
|---|---:|
| used and rechecked in this run | 1,078 |
| targeted proof check | 40 |
| independent re-proof | 146 |
| computation or formal certificate | 113 |
| refuted, with the refined statement's id | 39 |
| carried as background without fault found | 6 |

All448 item IDs,372 claim IDs and140 reference keys have event coverage; no event identifier is orphaned. No audited input changed while the snapshot was read. The independent checker supplies coverage and source-boundary checks in addition to the assembler and final-quality checks.

## Concrete defects found and confirmed corrected during this audit

1. **Cross-cote scan-number collision in root locations.** The former root helper selected repeated scan numbers before the cote100 marker at mixed-Pro line1313. This polluted twelve items and twenty-one claims, and their inherited problem occurrences, with material from cotes9/4. The cote-aware helper now removes those foreign intervals. The independently parsed latest source ranges contain no remaining wrong-cote interval.

2. **Two distinct Milne works had been merged.** The 1986 *Arithmetic Geometry* chapter, corrected2022, uses `xnotes/AVs.pdf` and single-level section numbers. The 2008 course notes use `CourseNotes/AV.pdf` and II§1/III§11. The `RMilne2008` to `MilneAV` alias has been removed, preserving the two bibliography entries and their different locators.

3. **Four claims pointed to blank lines.** C-SA04-43/44/45/46 cited Pro lines130/132/134/136. The actual statements are131/133/135/137. A corrected its serializer; the latest assembly has no blank-only exact claim locator.

4. **Secondary source occurrences were omitted.** The rational-logarithmic quotient in C-SA04-640 is explicitly on K93-05 scan193 line5; the scan193 continuation is lines3–9. The relevant root records now include that file. C also added the scan231 occurrence at second93 lines245–264 to SA04-406 and the scan26 fibre-functor comparison at lines1371–1387 to SA04-463. Root refreshed inherited problem occurrences and scan metadata.

5. **Paired source/target locators were incomplete.** B's SA04-268–279 used shorthand Codex target filenames or omitted the second93 target ranges; SA04-276 additionally had a malformed Pro prefix before its Codex target. B supplied exact replacements. The latest assembly has no unparsed numeric locator or incomplete Codex target filename detected by the checker.

6. **The RDeligne1968 URL annotation was ambiguous.** The URL ending in `.pdf` actually returns the opened IHES HTML catalogue record. Root reopened it and verified the title,1968 date and M/68/28 identifier. Therefore this is not a falsely verified failed URL; the final bibliography annotation now explicitly distinguishes that HTML route from the separate full-PDF attempt.

Some line ranges are deliberately broad contextual envelopes and contain intervening scans beyond the topical `scans` list. Those are distinguished from the omitted or wrong-cote intervals above; the audit does not report an intervening contextual page as a mathematical source error.

## Closure

The independent final snapshot has zero unresolved structural or source-boundary defects. Thirty records have deliberately broad contextual source ranges containing intervening scans beyond their topical scan lists; none omits a declared scan. The separate dossier editorial review identified ten concrete wording or citation corrections, all confirmed applied in the final mainbody at the time of this check. This is structural and editorial validation, not a machine proof of every registered mathematical statement.
