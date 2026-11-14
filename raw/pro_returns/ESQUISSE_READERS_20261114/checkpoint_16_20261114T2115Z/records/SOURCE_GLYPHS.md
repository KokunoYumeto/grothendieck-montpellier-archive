# Recorded source glyphs

## 119A — rounded open glyph, alphabet identification unresolved

**Source:** cote 119, copy 1, site 42, PDF page 43, typescript page 40;
`scans/esq_119_042_a.jpg`. The first occurrence is the subscripted ring symbol
in the paragraph introducing the system of local rings. The same contour occurs
in the displayed-in-prose system and in the other three occurrences on that page.
The scan review records six typed occurrences.

The inspected contour has an open rounded bowl, a short inner right stem and a
low upturned terminal. Five font specimens were rendered beside one another:
Computer Modern calligraphic A, Euler script A, Ralph Smith formal script A,
Euler fraktur A and AMS blackboard A. The specimen images document their actual
strokes. No specimen was adopted as an alphabet identification for this glyph.
The edition retains the observed contour under an explicit doubt mark:

```tex
\unsure{\sourceglyph{119A}}
```

The source key `119A` identifies this recorded shape. It does not settle its
conventional alphabet. Each occurrence retains its scan link through `\unsure`.
Its subscript remains outside the uncertainty wrapper, as in
`$\unsure{\sourceglyph{119A}}_n$`.

### Vector definition and exact transformations

`templates/source_glyphs.tex` is the reusable definition. The generator embeds
its full contents in every standalone reader and master. It requires standard
TikZ and graphicx; no image file or external font resource is needed when compiling
a reader.

The vector was produced from the reviewed 250 × 305-pixel enlarged detail of the
first occurrence. The extraction box is `(38, 80, 146, 199)` in that detail. The
script converts the detail to luminance and records the dark-pixel set by the
explicit rule `luminance < 125`. All three dark components in that isolated box
are retained, including the inner stem and the terminal. Their areas are 1833,
674 and 66 pixels. The boundary is extracted at level 0.5 on the padded binary
array; polygon vertices are retained to a recorded 0.45-pixel boundary tolerance.

The coordinate map used in the TeX path is
`(x, y) -> ((x - xmin)/10, (ymax - y)/10)`. The three paths contain 82, 51 and
11 vertices. `SOURCE_GLYPH_119A.json` records the input detail hash, the extraction
parameters and the vector-definition hash. `scripts/trace_source_glyph.py` contains
the complete transformation.

The rendered vector is resized to the cap height supplied by the current math
style. The reference A in the measuring box supplies a height only. It does not
assign the source shape to that letter or alphabet. `\mathpalette` supplies the
four math styles; the glyph has its baseline at the bottom of the recorded
contour. The surrounding `\mathord` provides the ordinary-atom spacing and permits
subscripts outside the doubt wrapper.

### Rendered checks

- `glyphs/119A_font_comparison.png`: the five tested font specimens, plus ordinary
  Roman A and italic a for visual orientation.
- `glyphs/119A_vector_and_math_styles.png`: the traced contour enlarged, then the
  actual inline `\unsure` construction with an external subscript, the system
  expression and two smaller script contexts.

The vector probe compiled with LuaLaTeX without errors. The rendered image was
inspected: the rounded open bowl, inner stem and terminal are visible, the doubt
brackets remain readable, and the subscript is separate. Further occurrences are
reviewed individually; this definition does not authorize a global replacement
of another alphabet.

### Root visual confirmation

The root reviewer inspected `glyphs/119A_vector_and_math_styles.png` after the
three-component trace was installed and confirmed that the bowl, inner stem and
lower terminal are all present and that the text and script placements are
legible. Subsequent occurrences through sites 42–44 were checked individually
against their scans. `SOURCE_GLYPH_USAGE.tsv` gives the current checked-page
usage; it is regenerated from the checked files, without substituting a glyph on
an unreviewed page.

## 119bracketlower and 119bracketupper — copy 2 spacing marks

The independently checked upper half of site 118 (typescript p. 40) contains two
handwritten spacing brackets. The upper-position mark has a curved lower arm;
the lower-position mark has a separate long upper arm, a tall descending stem
and a short angled foot. Their exact source spans are recorded separately in
the copy 2 apparatus. The accompanying doubtful word `espacer` remains a separate
marginal item.

`templates/source_brackets.tex` records manually traced Bezier centreline paths
from `records/glyphs/119_bracket_source_detail.png`, the native scan rectangle
(300, 365, 475, 690). The path coordinates, stroke widths and the preserved gap
between the second mark's upper arm and stem are explicit in that file.
`SOURCE_GLYPH_119_BRACKETS.json` records provenance and hashes. The contour with
a lower arm is `119bracketlower`; the contour with an upper arm is
`119bracketupper`. Each is used inside its own source `\margin` macro.

The shapes retain their respective aspect ratios and are sized to two and
2.75 footnote baselines so that the marginal representation fits the documented
three-line height limit. This is a compact representation of the observed mark;
the apparatus records its original paragraph extent. The margin renderer supplies
the handwriting color. The standalone TeX source embeds both vector definitions;
it does not depend on the detail image when compiled.

The shared `\sourceglyph` dispatcher now also accepts text-mode use through
`\ensuremath`. Its existing `119A` polygons and mathematical style scaling remain
unchanged. The original detail used to trace `119A` is included as
`records/glyphs/119A_source_detail.jpg`; the tracing command is:

```sh
python scripts/trace_source_glyph.py records/glyphs/119A_source_detail.jpg templates/source_glyphs.tex records/SOURCE_GLYPH_119A.json
```
