# Fixed-PDF visual review

Rendering produces images for inspection. It never creates a successful inspection record.

## Commands

After a complete, mechanically clean build:

    python edition/scripts/pdf_review.py freeze READER_NAME
    python edition/scripts/pdf_review.py render READER_NAME --pages required --dpi 160
    python edition/scripts/pdf_review.py list READER_NAME --pending

The manifest is build/visual_review/READER_NAME/FULL_PDF_SHA256/manifest.json. Full-page images are p001.png, p002.png, and so on in that same directory. Page numbers include front matter. The manifest lists 40 evenly spread samples (all pages for a shorter PDF), every landscape page, all source-page ranges with historical overflow or a local typesetting repair, and every current text/vector/image geometry flag.

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

## Geometry dispositions

Flag kinds are text_outside_sheet, text_outside_permitted_area, vector_paths_outside_sheet, vector_paths_outside_permitted_area, images_outside_sheet, and images_outside_permitted_area.

For a text type-area flag, the accepted exception is single-letter-overhang, with a concrete visual reason. For a conservative sheet, path, or image rectangle that overestimates visible ink, use conservative-rectangle-no-visible-overflow and explain the visible result. Actual ink crossing the sheet, or an impermissible overhang, requires a repair and a new build. A disposition never substitutes for full-page inspection.
