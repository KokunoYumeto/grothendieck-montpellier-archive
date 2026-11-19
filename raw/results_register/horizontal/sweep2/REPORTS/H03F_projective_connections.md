# H03F: projective connections and opers. The two statuses, and the sign on 159/20 read on the scan

By the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), horizontal sweep 2, part 2, 18 Nov 2026.

## Where it is
| item | topic | cote and scans | notes | status on the pages |
|---|---|---|---|---|
| SA04-9 | SA04 | 93/036, 043, 086-091 | MPL_93_047-091 and Codex K93 (`returns/MPL_93_*_unzipped/*_notes.md`) | worked; some boxed factors checked by the notes |
| SA01-31 | SA01 | 93/092-134 | MPL_93_092-134 (missed by NOTES_INDEX, placed in sweep 2) | sketched; formulas corrected later on the pages (factor 2, the Riccati equation) |
| SA32-4 | SA32 | 159/018-021 | MPL_159 (`returns/MPL_159_unzipped/MPL_159_notes.md`, N042-N045) | computed on the page with a sign conflict |

## The "disagreement" in sweep 1 was not one
Sweep 1 listed H03F as the one real disagreement between agents: "boxed factors checked" in SA04-9 against "a sign conflict" in SA32-4. The two statuses concern different pages:
- SA04-9 speaks of cote 93 (scans 36-91);
- SA32-4 speaks of cote 159 (scans 18-21).

They describe the same object, projective connections as PGL₂-opers, as their agents state ("= H03F"). Both statuses stand, each for its own pages.

## 159/20, read on the scan (159.pdf page 20 at 300 dpi; the scan number is the PDF page, footer "19")
**The ink:**
- c_{D_t}(dt) = −2dt
- c_{D_t}(1) = 1
- c_{D_t}((dt)⁻¹) = 0
- below them: c_{D_t}(λdt + μ·1 + ν(dt)⁻¹) = λ′dt² + (μ′ − 2λ)dt + (ν′ − μ)·1

The transcription (`MPL_159_unzipped/pages/MPL_159_159_scan020.tex`, L12-19) has this right.

**Decision: his slip, not a misreading.**
- With the three values above, linearity and the derivative terms give c(λdt + μ + νdt⁻¹) = λ′dt² + (μ′ − 2λ)dt + (ν′ + μ)·1.
- The values themselves are consistent with an sl₂ structure: put (dt)⁻¹ = f, 1 = κh and dt = 4κ²e, with [h,e] = 2e and [f,h] = 2f.
- So the general formula's "−μ" is the slip, given c(1) = 1. The rest of the page uses c(1) = 1 (the computation of φ(1)).
- The page also gives [−ω, 1] two values, "ω" and then "−2ω", which is a second sign inconsistency.

**What it changes.** No Schwarzian normalization should be read off the computation on 159/20 until the convention is fixed, as the Pro note N042 says. The boxed factors of cote 93 (SA04-9) are not affected.

## Check event (GLOBAL/CHECK_EVENTS_broad.tsv)
SA32-4: 159/20 read on the scan image; the transcription is confirmed; the slip is his, in the sign of μ in the general formula (my computation).
