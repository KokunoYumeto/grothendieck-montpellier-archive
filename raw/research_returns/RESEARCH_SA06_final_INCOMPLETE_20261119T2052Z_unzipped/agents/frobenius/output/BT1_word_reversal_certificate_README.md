# Administrative completion of the BT1 reversal certificate

Saved 2026-11-19T20:45:29.777969+00:00, after source freeze under the parent's explicit administrative authorization. No mathematical source, TeX or bibliography was edited.

The first stdout-only computation was not instrumented for its process runtime. Its exact program is now retained as `../code/check_BT1_word_reversal.py`, with embedded finite input additionally described in `BT1_word_reversal_input.json`. Its actual tool-returned stdout is retained verbatim in `BT1_word_reversal_original_untimed.out`. No start time, finish time or process runtime is retrospectively invented for that first execution.

Exactly one instrumented replay was then made by `../code/run_BT1_word_reversal.py`. It began 2026-11-19T20:45:16.682613+00:00 and ended 2026-11-19T20:45:16.695209+00:00; measured subprocess wall time was 0.012584313997649588 seconds, with exit code 0. Complete stdout, stderr and metadata are respectively `BT1_word_reversal_instrumented.out`, `.err` and `.json`. The replay's stdout matches the original byte for byte. No failed run occurred.

The program counts primitive cyclic words of lengths2–6 on the two-letter alphabet and lists the canonical classes changed by reversal. It confirms counts1,2,3,6,9, with the sole exchanged pair at these lengths ffvfvv / ffvvfv. This checks the finite labeling convention only. It does not prove the BT1 classification, geometric realizations, Hom rigidity or the infinite family exclusions. The owner's original certificate scripts and historical output were not rerun or overwritten.

This supplements `../C4_supersingular_BT1_independent_REVIEW.md`; it does not revise that receipt's mathematical or source-reading claims.
