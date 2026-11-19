# Final PDF visual and typesetting QA

**Result: passed on the final 59-page PDF identified below.** Every page was inspected at thumbnail scale. The dense B1 pages, the new support-theorem clause, and a spread of other pages were also inspected as full-page 125 dpi images. No clipping, overlapping text, colliding equations, missing glyphs, or unresolved reference markers were observed. The remaining observations are minor spacing and page-break issues, recorded explicitly below.

This is a visual/typesetting audit. The mathematical proof and source audits are separately recorded in the statement registers and check-event tables. The review was completed on 19 November 2026 at approximately 12:39 UTC. No master or part TeX file was edited during this audit.

## Exact PDF versions

| Version | Pages | Bytes | SHA256 |
|---|---:|---:|---|
| Initial 59-page QA baseline | 59 | 585187 | `6845bc7b323ee021d8c2c7dda344b4d3d77f9bf92dd19ed892bfc8e1eb99a5db` |
| Final stable fourteenth build | 59 | 586805 | `06dba124f9966cbfe3ba6c222da782c8f6fea05941419f3356921184b3be6984` |

The final source is `logs/RESEARCH_SA21_paper.pdf`. Its manifest is `qa/final_manifest.json`, and the exact build log audited here is retained as `qa/final_build.log`. The baseline manifest and build log are `qa/baseline_manifest.json` and `qa/baseline_build.log`. The immutable baseline PDF used to avoid a concurrent-build race remains in the external source area; it is not another deliverable PDF. The `qa/` tree contains no PDF files.

## Render evidence and actual inspection coverage

Rendering used `code/render_pdf_qa.py`, Poppler, and Pillow. Both versions were rendered in full at **125 dpi**, approximately 1034 by 1462 pixels per A4 page. Each render produced 59 page PNGs and seven labelled contact sheets. The recorded baseline render time was **26.15894421900157 seconds**; the final render time was **26.86010785899998 seconds**. These are rendering times only. No duration for the entire human-readable visual inspection is asserted.

The final command, from the parent scratch directory, was:

```sh
python RESEARCH_SA21_work/code/render_pdf_qa.py \
  RESEARCH_SA21_work/logs/RESEARCH_SA21_paper.pdf \
  RESEARCH_SA21_work/qa/final \
  > RESEARCH_SA21_work/qa/final_render_log.json
```

The final PNGs are `qa/final/page-01.png` through `qa/final/page-59.png`. The final contact sheets, **each actually opened and visually inspected**, are:

| Evidence image | Pages inspected |
|---|---|
| `qa/final/contact_01_09.png` | 1–9 |
| `qa/final/contact_10_18.png` | 10–18 |
| `qa/final/contact_19_27.png` | 19–27 |
| `qa/final/contact_28_36.png` | 28–36 |
| `qa/final/contact_37_45.png` | 37–45 |
| `qa/final/contact_46_54.png` | 46–54 |
| `qa/final/contact_55_59.png` | 55–59 |

Full-page images were actually opened for the following pages:

| Version and mode | Exact page numbers | Scope |
|---|---|---|
| Baseline, direct full-page inspection | 7, 8, 11, 12, 17, 20–36, 39, 42, 44, 49, 55–59 | 31 pages: finite/infinite flags, ten-element Hasse diagram, support theorem, split-poset proof, every B1 page, event-structure samples, cell-model truth table, Part C, citations and all bibliography pages |
| Final, direct full-page inspection | 1, 11, 12, 20–36, 39, 42, 52, 53 | 24 pages: corrected title/contents, support part(d), every B1 page after the chronological correction, event-structure samples, and all-dimensional signed CW theorem/proof |
| Final, prior full-page inspection transferred by exact pixel identity | 8, 44, 49, 55, 56, 57, 58, 59 | 8 further pages: the Hasse diagram, truth table, Part C opening, McCord citations and bibliography are pixel-for-pixel unchanged |

Thus **all 59 final pages received direct thumbnail inspection**, and **32 final pages have full-page visual coverage**, counting only direct final inspection or exact identity with an inspected baseline page. No claim of full-size inspection of every page is made.

The page-by-page pixel comparison is retained in `qa/final_page_diff.json`. It found 22 identical pages:

`6,8,9,10,15,16,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59`.

The other 37 pages changed through the final title/status, definition-title, chronological-attribution, cross-reference and consequent reflow corrections. All changed pages appear in the final contact-sheet review; the entire changed B1 span was also re-opened at full-page resolution.

## Targeted findings

| Target | Inspected pages in final pagination | Finding |
|---|---|---|
| Cover, abstract, audit status and contents | 1–2 | Working-edition placeholder has been replaced by the final audit-status paragraph. The title, body, and contents fit; the contents continuation is orderly. |
| Finite/infinite flag scope and A11 reconstruction | 7–8 | Baseline full-page check plus final thumbnail/pixel comparison: statement and counterexample remain legible; the set-label table fits. The Hasse diagram is centered, its ten vertex labels are distinct, and the caption explicitly distinguishes unmarked edge crossings from vertices. |
| A16 part(d), open sets and incidence coverage | 11–12 | The displayed criterion is numbered (5), its two formerly unresolved references now print (5), and the proof remains within the margins. The adjacent theorem references now resolve to Theorem 1.18. |
| Old B1 overflow locations | 20–27 and 33–35 | The notation display, long source directory, transcription locators, and source-reading paragraphs wrap inside the text block. No clipping or collision was observed after the final reflow. |
| B1 chronological table | 21–22 | Both columns remain readable and within the text block. The longer 156-6/156-7 qualification fits. Table continuation carries complete rows. |
| B1 seven-object model | 30 | Both data tables and the lists of figures/pairs are legible, with clear columns and mathematical symbols. |
| B1 comparison ledger | 36 | All entries fit. The former `Counterexample ??` is now `Counterexample 2.30`. Some justified cells retain visibly stretched word spacing, a cosmetic issue only. |
| B3 formulas and B4 truth table | 39, 42, 44 | Definitions, polar identities, refinement formulas and the three-column truth table are legible. No equation runs into a tag or table column. |
| All-dimensional C theorem and signed reconstruction | 52–53 | All four conditions and the boundary-chain proof fit cleanly. The Björner citation, superscripts, sums, and orientation signs are rendered correctly. |
| McCord comparison and bibliography | 55–59 | Citations and accented author names render correctly. Bibliography text stays inside the margins. Entries naturally continuing across pages remain legible; the mostly empty final page contains the final continuation and Winskel entry, not an accidental blank page. |

## Build-log comparison and resolved defects

The retained ninth LuaLaTeX stdout log, `logs/lualatex_ninth_stdout.log`, had **five overfull horizontal boxes**, of widths **59.7472 pt, 119.97313 pt, 73.88742 pt, 186.3769 pt, and 69.139 pt**. They were associated with the B1 notation display and long source strings. The QA baseline already had zero overfull boxes, but still had three unresolved references and a rerun warning.

The final audited log has:

| Check | Final result |
|---|---:|
| Overfull horizontal boxes | 0 |
| Underfull horizontal boxes | 19 |
| Undefined cross-reference warnings | 0 |
| Undefined citation warnings | 0 |
| Actual rerun warnings | 0 |
| Extracted-text occurrences of `??`, across all 59 pages | 0 |

The package-identification line for `rerunfilecheck` is not counted as a rerun warning. The remaining underfull boxes do not indicate lost text; the affected visual spacing was examined in the dense tables/source paragraphs.

Three baseline issues were resolved in the final PDF:

1. The p1 working-edition placeholder was replaced by the final audit statement.
2. The references to `eq:incidence-coverage` on pp11–12 now print the correct equation number (5).
3. The B1 ledger reference to `SA21-B-spatial-separations`, visibly unresolved on baseline p36, now prints Counterexample 2.30. The final stable pass also corrected the earlier one-step-stale theorem/equation numbers.

## Residual cosmetic observations

- The p36 comparison table retains some widely stretched justified spaces. Every entry remains readable and within its column.
- The two-line B3 heading on p39 has noticeably wide justification on its first line. It does not overflow.
- Counterexample 2.22 starts in the final two lines of p32 and continues on p33. This is a short opening at a page boundary, not missing text. The baseline's more awkward Counterexample 2.4 opening at the foot of p22 was removed by the final reflow; that counterexample now begins on p23 with its statement together.

These observations do not block delivery. No further TeX or mathematical changes were made as part of this QA.

## Program-inventory synchronization

`parts/maquettes/PROGRAM_INVENTORY.md` has been updated to the retained current `code/outputs/check_supports.json` run: **0.2201011680008378 seconds**, including the eight scan87/scan90 open-set comparisons, eight open-lieu polar comparisons, and part(d) checks on all 20 figures of the older eight-stratum countermodel. The previous result is explicitly retained as `code/outputs/check_supports_before_part_d.json`, **0.1883168230051524 seconds**, and is not counted as a second census population. The operational inventory also records both render runtimes above.
