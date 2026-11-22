# Verification of the final package

Verified on 21 November 2026, during the HODGE_SIGN run begun at 00:14 UTC (01:14 Europe/Berlin).

## Mathematical checks

The proof-check record is CHECK_EVENTS.tsv. It contains 209 actual events after final integration, including whole-proof readings, independent reconstructions, source inspections and exact computations. Every HS, SG, AR, SL and Q3 finding ID appearing in the paper has a direct check event. Event descriptions distinguish cited background, source-level inspection, mathematical proof and computation. No Lean kernel compilation is claimed.

The checked results and the stronger assertions not established are in separate parts of the paper. In particular, the automatic untwisted Arthur/Lefschetz identification is refuted; a newly specified normalized integral comparison is not declared refuted merely because its data are absent. The actual m=2 theta calculation is a conditional bound and a local-contribution calculation, not an exact valuation of a selected nonzero period.

## Exact computations retained

- 16 Wilson inclusion blocks, 27 aggregated divided-Lefschetz cases and 14 direct exterior-algebra matrices.
- Three stable SL2 lattice comparisons.
- Two m=2 lift steps, the exact rational local-contribution table and hashes of seven source files.
- Six integral-order calculations: ordinary and normalized lowering for n=1,2,3; 104 HNF-basis rows, with full certificates.

The scripts use Python 3; Wilson and integral-order calculations require SymPy. Run `python3 wilson_checks.py`, `python3 normalized_order_indices.py` and `python3 step10_numeric_checks.py` from the extracted package. The last script locates the retained Lean source files under evidence/lean_source. It was run from a fresh extracted package at00:57UTC; all three output tables matched the retained versions byte for byte. The selected source tree is evidence, not a complete independently buildable copy of the upstream Lean archive.

## Source, register and typesetting checks

All TSV records have the expected number of columns. QUESTIONS.tsv has 51 unique question IDs and separately includes all 17 SA06 C.1 rows. TRANSCRIPTION_NOTES.tsv has 18 archive rereading candidates; confidence and lack of original scan images are explicit. SOURCE_CORRECTIONS.tsv keeps three non-archive corrections separate. SOURCE_MANIFEST.tsv hashes all 47 supplied archive members.

The self-contained HODGE_SIGN.tex compiles to 42 PDF pages. Bibliography keys and cross-references resolve. The final LaTeX log has no overfull boxes or undefined references. Two harmless hyperref warnings concern mathematical tokens in PDF bookmarks. The local TeX installation lacked format and font-map caches; build_pdf.py repairs only a local cache and preserves the source. A conventional installation can compile HODGE_SIGN.tex directly with pdflatex twice.

All 42 pages were rendered with Poppler at 60 dpi and visually inspected in four contact sheets. Pages 6, 15, 24, 30 and 39 were additionally inspected at 130 dpi, covering the Gysin proof, the SA06 table, the actual m=2 calculation, the order proof and the unestablished-assertions table. No clipping or table collision was found. Text-box bounds and unresolved `??` markers were also checked. Rendered pages, contact sheets, detailed views and final compilation logs are retained under verification/.

## Archive checks

The complete archive passed a CRC integrity check and SHA256/byte-count verification for every manifest member. All required deliverables were present; member names were unique and had no absolute paths or parent traversal. No earlier ZIP, checkpoint, external literature PDF, TeX format cache or full upstream archive was embedded. The packaging script repeats these checks after each final integration.

FILES.tsv lists every packaged member except itself, with its size and SHA256. The package retains the original supplied sources, prompt, 3,138 selected Lean files, additional targeted search matches, work history, independent proof checks and provenance. The complete retrieved upstream archive is identified by URL, size and SHA256 in its provenance note.

## Timing

Content checks and the first complete ZIP verification finished by 00:56 UTC (01:56 Europe/Berlin), before the first scheduled checkpoint at 00:59 UTC (01:59 Europe/Berlin). No early checkpoint was made. Final delivery is separate from that checkpoint schedule. No three-hour progress review was due or simulated.
