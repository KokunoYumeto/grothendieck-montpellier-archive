# Cross-model catches: what each model caught that the others missed

Started 16 Nov 2026 by the main session (Claude Opus 5.5 at effort max), at the user's suggestion (P5916): [the user's words, omitted]

**Why this is kept.**
- A competent model does not lie to protect its maker. What a second model catches is the first model's blind spots:
  the attractor states and biases of its knowledge (the user, P5915, P5917; for example, OpenAI's models went
  straight to Balaban for Yang-Mills).
- A model cannot report its own blind spots, so only a record of catches shows them (P5916).
- A different model family is not good in itself. What helps is complementary skills, and this ledger is how we learn
  what those skills are.

**What goes in.** Every case where a model or a reader found:
- an error;
- a gap;
- an overstatement;
- a claim of novelty that was not new;
- a provenance mistake.

Also list independent agreements, where two runs reached the same result without seeing each other's work. Mark them
as such: they validate a result and catch nothing.

**Count the checks that found nothing, too.** Give one line per check: who checked what, how, and that it was clean.
Without that count, a model that is rarely checked looks perfect, and its error rate cannot be estimated.

**Record the check method beside the model** (R/F/D/C/S/L in the Hexagon format). Every frontier model learned from
much the same literature, so a field-wide attractor is shared by all of them, as Balaban is for Yang-Mills. Another
model does not escape that kind of blind spot. Another method does: a computation, a formal proof, a reading of the
primary source, or a blind prompt that bars the standard route. (Main session, 16 Nov 2026.)

Each entry gives:
- the date;
- the statement;
- who produced it and who caught it, each with model, effort and agent or run;
- whether the catcher read independently, that is, with a fresh context and without the producer's reasoning;
- how it was settled;
- the record where it is written up.

**Reading it.**
- The patterns at the end are what we have learned about each model.
- Revise them as entries come in.
- Never cite them without the entries behind them.

## Entries

**C1. 16 Nov 2026, ~13:0x UTC. Seven corrections to my S6 notes (NOTES_20261115.md §18, §23, §24, §31, §33 (a), §34 (c)).**
- **Produced by:** Claude Opus 5.5 at effort max, the main session.
- **Caught by:** Claude Fable 5.2 at effort high (agent ad85dcfa, the S6 final intake). It read the six returns
  first and then checked my notes against them.
- **What was caught:**
  - **§18, two errors.** I took the corner obstruction to be the twist integer, when it is the γ-winding of F
    (B.4.33). I put the CDP failure at the corner, when it is at the cusp fibre of every member (C4f).
  - **§23, two slips.**
    - The splitting locus: the fibre also splits at the torsion points and at two further parameters (first run,
      D.1.1-D.1.2).
    - The cover group is C₃×C₃, not μ₃.
  - **§24, an overstatement.** χ₁₂(p) = 1 is necessary for the sphere condition and not sufficient: p = 11 and p = 13
    fail.
  - **§31, an over-reading.** A shared cube-root coordinate was read as more than that.
  - **§33 (a), a claim of novelty that was not new.** The absolute values are already S6_05 C.4.2.
  - **§34 (c).** Two limits needed stating.
- **Settled by:** the returns' own statements, as cited.
- **Record:** NOTES §38; reviews/S6_FINAL_INTAKE_20261116/INTAKE_FINAL.md §5.
- **Pattern, mine:** I over-read analogies and connections, and I called things new without checking the returns.

**C2. 16 Nov 2026, ~13:2x UTC. The mod-28 values of sections.**
- **Produced by:** Claude Fable 5.2 at effort max (agent aa7b8224, the S6 expert), in EXPERT_POSITION.md.
- **Caught by:** Claude Fable 5.2 at effort high (agent ad85dcfa), in RESPONSE_INTAKE.md.
- **What was caught:** on the page surface, (mP)·O = m² − 1, so P gives 0 and 6P gives 35 ≡ 7 (mod 28). The expert's
  list does not follow.
- **What the catch shows:** the model and the family were the same, so the catch came from an independent second
  reading, not from model diversity.
- **Settled by:** a direct computation, consistent with PUSH C.3.21.

**C3. Statement A4.2 of the S6_01 return (returned 12 Nov 2026): [AC26] Remark 9.21 is false.**
- **What was caught:** the remark makes a cusp-torsion claim for Ω¹. The support is S₁ ∪ S₂, and Remark 1.3 must
  distinguish p = 1 from p = 2.
- **Produced by:** [AC26], Alpöge's memoir, which is an AI-generated text.
- **Caught by:** GPT-6 Astra (ChatGPT Pro mode), in the S6_01_INVARIANTS run.
- **Confirmed by:**
  - Claude Fable 5.2 at effort high (agent ad85dcfa, in INTAKE_S6_01.md on 16 Nov);
  - the survey of 12 Nov, which made the same correction, checked by hand by two readers.
- **Record:** reviews/S6_FINAL_INTAKE_20261116/INTAKE_S6_01.md.

**C4. Statement E2.4 of the S6_01 return: the bound h⁰(T) ≤ 2 of Huckleberry-Kebekus-Peternell (Corollary 1.3, repeated in [AC26] Remark 9.26) is false for the comb members.**
- **What was caught:** the comb members have h⁰(T) = 2m+1 ≥ 25. The published bound rests on the
  Campana-Demailly-Peternell claim that a complex S⁶ has no non-constant meromorphic function, and that claim is now
  false.
- **Produced by:** human-written literature.
- **Caught by:** GPT-6 Astra (ChatGPT Pro mode), in the S6_01_INVARIANTS run.
- **Confirmed by:** Claude Fable 5.2 at effort high (agent ad85dcfa, in INTAKE_S6_01.md).
- **Limit:** this does not refute the bound in algebraic dimension 0.
- **Record:** INTAKE_S6_01.md.

**C5. 16 Nov 2026, ~18:0x UTC. The S6_07 writing prompt produced a paper with 32 findings printed without proofs.**
- **Produced by:** Claude Fable 5.2 at effort max (agent aa7b8224), which drafted the prompt from DECISION.md, and
  Claude Opus 5.5 at effort max (the main session), which rechecked it for lint and privacy only.
- **Caught by:** the user, on reading my summary of the draft check. The draft check itself, by Claude Fable 5.2 at
  effort high (agent a3da1122), flagged only the repository link.
- **What was caught:** a paper must report every finding with its proof; ours printed a status catalogue instead.
- **Settled by:** the binding rule in the Hexagon format, paper_completeness_lint.py and AGENTS.md (16 Nov).
- **Pattern, ours:** we checked a prompt against our rules (lint, privacy) and never asked whether its outcome would
  be a complete paper. Check prompts against the purpose of their outcome, not only against the rules.

## Patterns so far (revise as entries come in)

- **Claude Opus 5.5 at effort max (the main session):** it confirmed computations correctly (the §33-§34 algebra
  held). It over-reads analogies and claims novelty too readily (C1).
- **Claude Fable 5.2 (intake and expert agents):** reading the returns first and then checking against them caught
  most of what is in this ledger (C1, C2), including errors by another instance of the same model (C2).
- **GPT-6 Astra (ChatGPT Pro mode):** it found errors in both an AI-generated memoir and the human literature (C3,
  C4). What it misses is not yet recorded here: the intakes of its returns are where that will show.

## To fill

The intakes and reviews since October hold many more catches, including the S6_02 audit of DGKX v1 §6, the A57 sense
check, the transcription checks and the Dérivateurs intakes. A bounded backfill from those records is proposed to the
user. It has not been started.
