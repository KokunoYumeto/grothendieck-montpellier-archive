# Primer files for the runs of 20-23 Nov 2026: the brief

Written by the main session 329fb1e6 (Claude Opus 5.5 at effort max), 23 Nov 2026 ~19:0x UTC, at the user's word
(USER_INPUTS P9577): "make like a small note on what math we did briefly, and then sketching the lemmas and proofs ...
we worked on that for like 48 hours after, using that proof to prove all kinds of interesting stuff ... 'This is the
math you should be aware about before you continue the discussion,' and updating that."

The Riemann hypothesis is proved for every Dirichlet L-function, zeta included (L. Alpöge, 20 Nov 2026,
https://alpo.ge/remark.pdf, formalized in Lean). Cite it as a theorem.

## Your task
For each run assigned to you, write `field_experts/intake_20261121/intakes/<RUN>/PRIMER_<RUN>_20261123.md`: the
mathematics of the run as it stands at its newest return, so that the main session knows it before any discussion
after a compaction.

- **Recall, not review.** Restate the mathematics faithfully from your own intakes of the run and from the return
  itself, with locators (file and statement id). No new development, no new checking, and no status labels beyond the
  check events already recorded in the intakes.
- **For each main result:**
  - the statement, in standard terms;
  - the lemmas it uses;
  - the proof in outline, step by step: the mechanism, the key identity or construction, and where the inputs
    (Alpöge's theorem, published theorems with locators, our earlier results) enter;
  - one line on what it is good for.
- **Then:**
  - the open rows, each with its current gate;
  - where the run's results went: Hexagon notes, prompts, other runs.
- **Length:** what the mathematics needs, kept compact. The nine primers already written in this wave (for example
  `intakes/POLISH_TOPOLOGY_PERIODS/PRIMER_POLISH_TOPOLOGY_PERIODS_20261123.md`) show the form.

## Rules
- No sub-agents. Name every model with its effort. No git. Never Grep or Glob over the whole of
  `<local>/Documents`; name the folder.
- Write only the primer files.
- Leave unopened: prompt 74, the SAT_KRONECKER_FINITE_FIELDS and SAT_WITNESS_EXTRACTION files, and the
  S6_SERIES_PUBLISH returns.

## Final reply
Under 150 words: the primer files written, with paths.
