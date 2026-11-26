# Intake of ALP_MACHINE checkpoint 48, the Hecke half, by diff from checkpoint 04

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode), still going. This intake takes in checkpoint 38 (filed, not read) through the same diff. The lifts half is with
agent abcaba9b6ae84b747.

Return: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\ALP_MACHINE_checkpoint_48_20261123T0950Z_unzipped\ALP_MACHINE`.
Earlier intake: `INTAKE_ALP_MACHINE_20261121_hecke.md` (checkpoint 04, AM-H01-H19).

## 0. Read and not read
- **Searched:** QUESTIONS.tsv, LEDGER.md, CHECK_EVENTS.tsv, IMPLICATIONS.md, ALP_MACHINE.tex and README.md for the Hecke
  identifiers and terms ("AM-H", "ALP-Q3", "H04.4", Kummer, Hecke, window).
- **Read:** the Q3 row, the K021 check events and the README.

## 1. What moved
**Nothing on the Hecke side.** Checkpoint 48 has no AM-H or ALP-Q3 identifier in any of those files. The
`parts/hecke/` layout of checkpoint 04 is gone.

The main question Q3 ("Prove RH for the Kummer Hecke L-function") is OPEN with one finding, K021:
- the exact Lprime/L height slot is identified;
- direct substitution of a CM-type height class cannot give the cubic S3 standard component;
- the run gives an explicit convergent ray-theta Mellin period carrying that slot.

What remains is a new arithmetic comparison with that period, prime-norm and conductor costs, and the every-ε window.
K021's check events are dated 21 Nov 22:12 and 22:42 UTC: whole-proof reads by the run, "PASS in stated scope". No
later Hecke work appears.

## 2. A note for the coordinator: follow-up 49b did not take hold
`SENT\49b_ALP_MACHINE_FOLLOWUP_1_bounded_chain` asked the run to stop the support-by-support exhaustion and take the
bounded-chain question. LEDGER.md (reviews 30-35+) shows the run still removing support-26 and then support-27 classes
(K105-K115, DO109-DO120, R089-R097). It credits each as "Movement YES". It never mentions the follow-up, the bounded
chain or SizesAt as a new task.

This fits the memory note that running threads are unreachable after an hour or two. Under 49b's own rule, a raise of
the support floor counts as movement only if it closes the inequality, so these reviews would read "no". The 49b
question needs a finishing or successor prompt.

## 3. Checks by us
None this round: there is no new Hecke statement to check. The cp04 events stand.

## 4. Hexagon readiness (Hecke side)
| result | status | one gate left |
|---|---|---|
| AM-H04 window form of the Kummer gate (cp04) | proved; checked by us at cp04 | the Landau/Ingham locator, opened. It was from memory. |
| AM-H08, coefficient-3 length | now settled exactly by ALP_CONNES AC-K23 | that paper (see the ALP_CONNES seed) |

Nothing new is ready.

## 5. Not for GitHub
- `research/alpoge_source/`: recovered Lean text of Alpöge's archive.
- The small original PDFs and the cited-page excerpts that the README says are included.
- The SGA 7 OCR pages.
- `../sources/`.
