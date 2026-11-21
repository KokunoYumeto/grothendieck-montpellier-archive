# Checkpoint 04 PDF visual QA (in progress)

The root reviewer rendered and visually inspected pages87–99,114–123,151–156,1,3,168–169 of the 169-page PDF with SHA2569f99ddf25aeefa04c8cfcbfa82d44827f0483a353130030af9c02a64b769e391. The contact sheets were generated from the actual PDF using PyMuPDF; every listed page was displayed. The build also reported zero warnings and no text blocks outside page bounds.

A collision between the GP.66 equation and its tag was found on page97. The displayed formula was split over two lines, and its coordinate-range qualifier moved into the following sentence. This is a layout change only. The corrected page must be rendered and inspected after the next build. All other displayed pages had readable formulas, intact margins, and no observed clipping or collisions.

Earlier unchanged portions retain the preceding checkpoint visual checks. Mathematical whole-proof checks are recorded separately in CHECK_EVENTS.tsv; this visual inspection is not a proof check.

## Final integrated build and inspection

The188-page final build has SHA2562a7184489a490254e91ec5b519a5677b5644e09078f2e134511365318261eda9, zero TeX warnings and no text blocks outside page bounds. Root rendered and visually inspected current pages97,99–109,124–126,134–140,187–188. The GP.66 tag collision is fixed. An additional GP.81 width warning was fixed by splitting the S1 assertions from the trace identity; the corrected page99 was displayed and checked. The new GP009, JP001–003, NR001 and CGP001–003 pages have no observed clipping or equation/tag collision. Earlier inspected CQ/RB/GP pages retain their preceding visual checks. The final page contains the concluding bibliography entry and is sparse but has no missing content.
