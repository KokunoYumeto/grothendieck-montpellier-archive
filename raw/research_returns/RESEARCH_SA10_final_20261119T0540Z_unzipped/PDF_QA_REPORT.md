# Final PDF publication check

**PASS.** The published LuaLaTeX PDF has **74 pages** and **762,332 bytes**. Its SHA256 is `1786ba59ec32382ec60392f23bd95ef926d14872f851478dbeb0771e12a79301`.

| Metric | Last retained failing draft | Final PDF |
|---|---:|---:|
| Overfull boxes, all sizes | 7 | 2 |
| Overfull boxes exceeding2pt | 4 | 0 |
| Largest overfull box | 142.84079pt | 1.42430pt |
| Missing-character warnings | See retained draft log | 0 |
| Undefined citations | See retained draft log | 0 |

The baseline is `logs/build_history/20261119T052014525518Z/build_pass2.out`. Its four excessive boxes are15.27339,142.84079,97.10779 and13.91151pt. Earlier intermediate failures remain in the build history; this comparison does not silently count only one of those earlier errors as the entire history. The final source repairs the affected titles, raw paths/URLs and obsolete metadata. Final successful build time: 23.495529s. Poppler render time: 23.081229s.

Every page was rendered at110dpi and visually reviewed in seven contact sheets. **49 distinct full pages** were separately inspected: 1, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 31, 33, 35, 36, 37, 42, 43, 45, 47, 48, 50, 55, 56, 57, 58, 60, 61, 62, 63, 66, 68, 69, 70, 71, 72, 73, 74. These include every identified former overflow location and a spread through every Part. Actual page-by-page observations are in the three inspection records. No clipping, overlapping text, unreadable glyph, footer collision or excessive display was found. Two nonblocking editorial observations are preserved in the B audit: separate bibliography entries for some works consulted by different subruns, and the explicit B4.8 equation tag preceding B4.7. They do not change statement IDs, references or mathematical content.

The C5 matrix is fully visible on page68. The former long C2 source title and C1 moduli citation line are fully visible on pages47 and43. The B3 heading, B56 file paths and bibliography wrapping were checked at full size. We have not inferred visual quality merely from a successful compile.
