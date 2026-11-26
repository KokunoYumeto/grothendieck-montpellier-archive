# Build, version 2

Source: `nullstellensatz_am_half_plane.tex`, made from the posted version-1 source `../hnam_note.tex` by

    python -I -B make_v2.py

Engine: pdfLaTeX, three passes (no BibTeX):

    pdflatex -interaction=nonstopmode nullstellensatz_am_half_plane.tex   (three times)

State of the build of 25 Nov 2026 (Claude Fable 5.2 at effort max): 10 pages, 0 overfull boxes, 0 underfull boxes,
0 undefined references (`nullstellensatz_am_half_plane.log`; `build_1.log` to `build_3.log`).

Pages looked at: all ten pages of this build were rendered at 95 dpi (`pages/p01.png` to `p10.png`) and read; the
changes are on pages 1, 3, 4, 5, 6, 7, 9 and 10, and pages 2 and 8 only shifted by a few lines.

Field lengths (characters): ABSTRACT.txt 1,955; COMMENTS_FIELD.txt as printed by the count below; the limit of the
comments field is 2,000.
COMMENTS_FIELD 1903

Recheck (25 Nov 2026, Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7): Remark 3.3 last sentence changed in make_v2.py; make_v2.py rerun; three pdflatex passes: 10 pages, 0 overfull, 0 undefined. Page 7 rendered (pages_recheck/p-07.png) and read. COMMENTS_FIELD.txt now 1,968 characters; CHANGE_NOTE.txt and PROVENANCE_V2_SENTENCE.txt: "No statement of ours changes" replaced (Prop 3.1(b) bound changed form). Backups: field_experts/intake_20261121/integration_backups/20261123/HNAM/v2_before_recheck/.
