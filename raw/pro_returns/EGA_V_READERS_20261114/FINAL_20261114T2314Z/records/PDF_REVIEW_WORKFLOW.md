# Fixed-PDF visual review

Rendering produces images for inspection. It never creates a successful inspection record.

## Commands

After a complete, mechanically clean build:

    python edition/scripts/pdf_review.py freeze READER_NAME
    python edition/scripts/pdf_review.py render READER_NAME --pages required --dpi 160
    python edition/scripts/pdf_review.py list READER_NAME --pending

The manifest is build/visual_review/READER_NAME/FULL_PDF_SHA256/manifest.json. Full-page images are p001.png, p002.png, and so on in that same directory. Page numbers include front matter. The manifest lists 40 evenly spread samples (all pages for a shorter PDF), every landscape page, all source-page ranges with historical overflow or a local typesetting repair, source pages implicated by an actual earlier visual issue, the specific four-line-note routing cases, and every current text/vector/image geometry flag.

The compiler refuses to overwrite an actively frozen reader. A repair requires a recorded release:

    python edition/scripts/pdf_review.py release READER_NAME --reason "Concrete reason for the repair"

A replacement PDF requires records matching its new hash.

## Recording viewed pages

Open each image and inspect the whole page: text, formulas, diagrams, marginal material, apparatus, page markers, rules, and boundaries. Write a JSON file under records/visual_observations/ with this structure:

    {
      "reader": "EGA_V_FR_texte_de_lecture",
      "pdf_sha256": "EXACT_FULL_HASH_FROM_MANIFEST",
      "reviewer": "GPT-6 Astra / root",
      "observations": [
        {
          "pdf_page": 1,
          "result": "layout inspection passed",
          "findings": "Concrete observations of the material actually viewed on this page."
        },
        {
          "pdf_page": 72,
          "result": "layout inspection passed",
          "findings": "Concrete findings after examining the flagged glyph and the rest of this page.",
          "geometry": [
            {
              "flag_kind": "text_outside_permitted_area",
              "decision": "single-letter-overhang",
              "reason": "Describe the specific glyph and visible extent that satisfy the permitted single-letter exception."
            }
          ]
        }
      ]
    }

Use "layout issue found" when a page needs repair. The example contains no inspection findings; replace it with actual observations.

    python edition/scripts/pdf_review.py record READER_NAME --observations edition/records/visual_observations/OBSERVATIONS.json

The recorder checks both PDF and rendered-image hashes, then atomically appends PDF_VISUAL_REVIEW.tsv. Geometry dispositions append PDF_GEOMETRY_REVIEW.tsv. The newest observation for a page controls its status; prior observations remain documentary records.

The release gate also rejects every latest unresolved layout issue on the current PDF, including an optionally inspected page outside the required sample. The pending list includes those optional issues. A passing count for the original sample therefore cannot hide an issue found elsewhere in the volume.

## Identical full-page image evidence

An already viewed complete page image may support a different frozen PDF only when the two complete PNG files are byte-identical. This is recorded as image equivalence, with the source observation and both PDF hashes; it is never recorded as a second actual view.

    python edition/scripts/transfer_identical_pdf_reviews.py SOURCE_READER TARGET_READER

For a replacement version of the same reader, name its earlier released freeze explicitly:

    python edition/scripts/transfer_identical_pdf_reviews.py READER_NAME READER_NAME --source-sha256 EARLIER_FULL_PDF_SHA256

Both images must be present in their hash-specific manifests at the same page number and render resolution. The source's latest observation must be a direct successful full-page view. An equivalence-derived observation cannot serve as a new source: the program always requires the original actual view. No transfer is made for a differing PNG, an issue observation, a missing image, or an unmatched image hash. Differing required pages must be opened and inspected independently.

PDF_VISUAL_EQUIVALENCE.tsv retains the original review time and source image, the source and target PDF hashes, and both identical image hashes. PDF_VISUAL_REVIEW.tsv explicitly identifies the evidence method. Matching geometry dispositions retain their source provenance. The release audit independently checks these records and the complete image files through visual_evidence.py.

## Actual margin-line routing

The compiler counts the packed text rows in each running marginal note at the actual margin width. A note with more than three rows is placed in a labeled, ruled block at its attachment in the body. Nested glyph boxes inside a text line do not count as extra rows; independent packed display rows do. The compiler also proves that every expected note produced a routing measurement and that paired margin anchors and notes stay on the same PDF page.

Each reader's audit/margin_content_routes.tsv records the source page, note ordinal, measured row count and route. The aggregate records are MARGIN_LINE_AUDIT.tsv and MARGIN_LINE_SUMMARY.tsv. TYPESETTING_FIXES_margin_line_limit.tsv records the body-block decisions. These measurements establish the routing rule; the required complete-image review still checks the visible result, including labels, rules and collisions.

## Geometry dispositions

Flag kinds are text_outside_sheet, text_outside_permitted_area, vector_paths_outside_sheet, vector_paths_outside_permitted_area, images_outside_sheet, and images_outside_permitted_area.

For a text type-area flag, the accepted exception is single-letter-overhang, with a concrete visual reason. This exception does not cover an underline or another rule extending beyond the permitted area. For a conservative sheet, path, or image rectangle that overestimates visible ink, use conservative-rectangle-no-visible-overflow and explain the visible result. Actual ink crossing the sheet, or an impermissible overhang, requires a repair and a new build. A disposition never substitutes for full-page inspection.

## Cumulative reports and release

After the final observations and image-equivalence records have been appended, regenerate the cumulative reports before running the release audit:

    python edition/scripts/generate_build_reports.py
    python edition/scripts/audit_release.py

The generator writes CLEANUP_LOG.tsv, TYPESETTING_FIXES.tsv, TYPESETTING_REPORT.md, records/COMPILE_SUMMARY.tsv and APPARATUS_COUNTS.md. The typesetting report distinguishes direct inspections from recorded full-page image equivalence, retains the concrete observations and their outcomes, and gives each geometry flag's accepted disposition or pending status for the exact PDF hash.

records/BUILD_REPORT_PROVENANCE.json records the generation time, all input and output SHA-256 hashes, and the membership of each input-file inventory. It includes the review and geometry ledgers, freezes, equivalences, compile reports and logs, PDFs, current reader sources and their recorded source dependencies, and the apparatus/repair inventories. An input change during generation prevents the proof from being sealed. The release audit rejects a missing proof, a later change to an input or output, or an added or removed file matching an input inventory. Regenerate the reports after any such change. The provenance proves report freshness; the release audit separately checks the validity of the underlying visual evidence and every substantive release gate.
