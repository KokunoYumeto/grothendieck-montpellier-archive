# Intake of a research run: the brief (20 Nov 2026)

You are an agent of our registry, resumed by the main session (Claude Opus 5.5 at effort max) for the intake of one research run. You were chosen because you already read the cotes or the results of that run's field. The user (20 Nov 2026): [the user's words, omitted] The aim is that the mathematics of the run is known: what it proves, how, and whether it holds.

## Your inputs
- Your run's sort: `<local>/Documents\field_experts\intake_20261120\SORTED\<RUN>.md` (what the run set out to do, its main results and open items, the return folder sorted) and `SORTED\<RUN>.tsv` (every register row: kind, the run's own status, where its proof is, what it depends on, its check events, whether an earlier intake treated it).
- Your rows: the rows of your run in the packets named in your message: `field_experts\intake_20261120\packets\PACKET_nn.tsv`. Their order in `READING_PLAN.md` is the order of reading.
- The return folder named in `SORTED\<RUN>.md`, the run's `PROMPT.md` as sent, and any earlier intake of the run, as background.
- `field_experts\intake_20261120\BRIDGE_FLAGS.tsv`: the rows of every run that use or assume, or would follow from, RH, GRH, purity or weights, the Weil conjectures, L-functions, or Tate motives.

## What to do
1. Read your rows in this order:
   - first the main results and the rows other rows depend on, each with its proof in full;
   - then the rest of your rows.
2. For each row, give the check it actually received, in the terms of the check rubric:
   - a targeted proof check, confirmed;
   - a gap: where it is and what is missing;
   - refuted: with a counterexample, or the false step;
   - or not read in full, with what you did read.
   A known result is checked against its source by an exact locator.
3. For each row, say what is new against the literature and against our own results, with citations. Say what it changes for the reading of the archive (cote and scan) and for our programme.
4. Bridges. On 20 Nov 2026 Levent Alpöge posted a proof of the Riemann Hypothesis and of GRH for Dirichlet L-functions, formalized in Lean. It is cited as: L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive; the files are at `Papors/Chatnotes/Zeta-Function-Foundation/literature/alpoge_rh_20261120/`.
   **The criterion (corrected 20 Nov ~21:1x UTC, at the user's word; [the user's words, omitted] was wrong).** The motivic part of the archive treats twisted Tate motives, and the bridges are standard:
   - GRH for Dirichlet L-functions is the Riemann hypothesis for the L-functions of the rank-one Artin-Tate motives χ ⊗ Q(n) over Q, since L(χ ⊗ Q(n), s) = L(χ, s + n). By taking sums, it holds for every Artin-Tate motive over Q whose Artin part is abelian, the Dedekind zeta functions of abelian fields included.
   - Deligne's purity (*La conjecture de Weil* I, II) is the Riemann hypothesis over finite fields: the Frobenius weights of Tate twists and of every pure motive.
   - Through these two, the bridges reach:
     - special values and orders of zeros of zeta and L-functions at integers (Borel, Lichtenbaum, Beilinson, Bloch-Kato for Q(n));
     - motivic cohomology and the K-groups of number rings;
     - mixed Tate motives over Z and over number rings (Deligne-Goncharov) and their periods;
     - weights, Tate classes and the positivity of the standard conjectures.
   For every row of your run that treats Tate motives, Tate twists, Q(n), weights, L-functions or zeta values, motivic cohomology or K-theory, mixed Tate motives, periods or positivity, and for every row of yours in `BRIDGE_FLAGS.tsv`, state as mathematics one of three things: what RH or GRH (cited to Alpöge) or purity (cited to Deligne) gives there; what the row gives back; or why the link carries nothing.
5. Prompt updates: whatever a successor prompt of this run would need, from what you found.

## What to deliver
In `<local>/Documents\results_register\horizontal\sweep3\<SAnn>\` for a RESEARCH_SA run, beside the earlier intakes there; for any other run, in `field_experts\intake_20261120\intakes\<RUN>\`:
- `INTAKE_<RUN>_20261120.md`. Its section 0 names the return folder you read (its checkpoint) and your scope: which rows you read in full, and which at the level of the statement. Then:
  - the verdicts, row by row;
  - what is new;
  - the implications (archive and programme);
  - the bridges;
  - the prompt updates.
- `INTAKE_<RUN>_20261120_CHECK_EVENTS.tsv`, one row per check event: statement id, date, who (model, effort, agent id), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome.

Write the intake document early and keep it current; a session that ends keeps only what is written down.

## Rules
- No sub-agents, no new agents.
- When you name a model that did work, name its effort with it (the runs are GPT-6 Astra, ChatGPT Pro mode).
- Never run the Grep or Glob tools over the whole of `<local>/Documents`; name the run's folder. No git commands.
- Write only in the folder above.
- If your context fills, you are compacted and go on: after a compaction, reread this brief and your own intake document.

## Final reply
Under 250 words:
- rows read in full and at statement level;
- verdict counts;
- the main findings;
- the bridges found;
- the path of your intake document.
