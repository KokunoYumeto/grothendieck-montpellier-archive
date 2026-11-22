# Cote 1: direct search for a date or letter in physical PDF pages 1–72

The source is the complete original PDF retrieved by root, retained as
`sources/root_manuscript1_ranged.pdf`, SHA256
`38a9610e2a9227201f1bc162a28f2a2ac20951406bba7c9ccf507553f53e71e3`.
This note records the original finding-aid inspections and a subsequent
individual full-page visual inspection of physical pages 25–72. It is not
a transcription of all handwriting.

Geometry inspected the three original whole-page contact sheets for physical
PDF pages 1–72, then full renders of physical pages 3, 4, 6, 11, 18 and 36.
These are an index and mathematical notes, without an evident date or
correspondence salutation. The modern cover identifies undated notes and a
letter dated 1953, but does not identify which mathematical sheets belong to
that letter. All upper and lower strips in the nine readable finding sheets
`notes/geometry_cote1_edges/edges_001_008.jpg` through
`edges_065_072.jpg` were then visually inspected. They were rendered directly
from the source by `code/geometry_cote1_edges.py`; exact strip fractions and
timing, 7.282029397 seconds, are in `logs/geometry_cote1_edges.json`.

## A correspondence scrap on physical PDF page 26

This page contains a short typewritten German opening beneath the handwritten
mathematics. The salutation reads **Liebe Paula**, and the following line
begins **Wieder ein Breif** (the apparent letter order is retained here rather
than silently corrected). Only these two typed lines are evident; no typed
date was found. Full physical pages 25 and 26 were rendered at width 2400 and
visually inspected. Page 25 shows the lettering through the paper in reverse.
The full renders are `notes/geometry_cote1_folios/page_025.png` and
`page_026.png`; the reproducible render and timing are logged in
`logs/geometry_render_cote1_025_026.json`.

Physical page 26 has public PDF footer 25 and archival pencil number 27.
This is a correspondence-like opening on reused paper. It does **not** identify the
catalogue's 1953 letter, date the mathematical overwriting, or connect that
writing to the trace/genus-zero sheets. No conclusion about the recipient's
identity is inferred from the forename alone.

## Negative search scope

No other correspondence opening or explicit calendar date was identified in
the inspected top and bottom strips of physical pages 1–72. Page middles are
omitted from those strips. Handwriting and faded show-through are difficult
to read, so this observation proves no exhaustive absence. The separate
72-page OCR is a weak finding aid: it found the year 1953 only on the modern
cover. Its successful run, 10.400876059 seconds, and the interrupted first
attempt are recorded in `logs/geometry_cote1_date_search.json` and
`logs/geometry_cote1_date_search_attempt1.txt`.

Root and the category agent are inspecting the later physical pages. Until
a dated source is actually linked to the particular mathematical folios,
the manuscript-date assertion remains unproved. Public PDF footer numbering,
physical PDF numbering and archival pencil numbers must be recorded separately;
there is no justified global replacement of the supplied folio references.

## Completed individual inspection of physical pages 25–72

Geometry subsequently inspected every physical page from 25 through 72
individually at a full-page width of 1800 pixels. These images are preserved
as `notes/geometry_cote1_full/page_025.jpg` through `page_072.jpg`.
The rendering program is `code/geometry_cote1_full_audit_render.py`, and
`logs/geometry_cote1_full_audit_render.json` records the original PDF hash,
all 48 output paths, and the successful rendering time of 5.962332416 seconds.
Pages 57–60 were reopened after an earlier display result was truncated;
only the later successfully displayed images count as the individual readings.

The per-page record is `notes/geometry_cote1_full_observations.tsv`. Every
page was inspected for a date, letter heading, salutation, address or
nonmathematical correspondence content, including visible page middles and
margins. Apart from the two typed German lines on physical page 26, no
readable calendar date or correspondence form was identified. Mathematical
topics on each page are recorded to make this a verifiable page-level audit
rather than a claim based on OCR keywords. Pages 37, 43 and 47 are effectively
blank; physical pages 38, 62 and 63 contain damaged or overlapping areas;
pages 71–72 have damaged top edges. Faint reverse show-through, cross-outs,
overlaid slips and hurried handwriting prevent an exhaustive absence proof.

Algebra separately reports an individual full-page inspection of physical
pages 1–24, and category and root report corresponding inspections of
73–110 and 111–150. Their scopes and observations belong to their own audit
notes; geometry does not relabel those readings as its own. The catalogue's
1953 letter has not been securely identified by this combined search, and
none of these observations dates the four trace/genus-zero folios.
