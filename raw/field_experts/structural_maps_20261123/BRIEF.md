# Structural maps across the fields: the brief (23 Nov 2026, evening)

From the main session 329fb1e6 (Claude Opus 5.5 at effort max), at the user's word (23 Nov ~19:5x UTC):

> "Which of the maps are the most [interesting] ... give some commentary on the maps and what kind of interesting
> mathematics they suggest for each of them, because we're mapping the Riemann proofs through all kinds of stuff like
> Hodge, NCG, GCT. Now checking in on Moonshine, there's also the Langlands where it's very clearly mappable. Global
> Langlands like stuff ... And we have some extensions of it sitting here and there. Like the question is sort of like
> how does this all become a coherent map throughout all these different fields of mathematics? That is structurally
> interesting. So like make them all make those interesting structural notes on that as well."

The Riemann hypothesis is proved for every Dirichlet L-function, zeta included (L. Alpöge, 20 Nov 2026,
https://alpo.ge/remark.pdf, formalized in Lean). That is the GL_1 layer of the automorphic picture over Q.

## What to write
Write a note in this folder, `field_experts/structural_maps_20261123/<YOUR_FIELD>.md` (the field named in your
message), built from our files and the sources: the runs you took in, their primers
(`field_experts/intake_20261121/intakes/<RUN>/PRIMER_<RUN>_20261123.md`), and the papers you open.

1. **The maps in your field, written out.** For each place where Alpöge's theorem, or one of our results built on it,
   enters your field:
   - the objects on each side;
   - the correspondence or functor between them;
   - what is transported across it;
   - what our runs proved there, with locators.
2. **Towards global Langlands.** Where each map sits in the automorphic-motivic-Galois picture:
   - Dirichlet and Hecke characters as GL_1;
   - modular forms and theta series as GL_2;
   - motives and Galois representations on one side, automorphic representations on the other;
   - functoriality: symmetric powers, base change, theta lifts;
   - the trace formula.

   Say which rung each of our results lives on, and what the next rung would need, as concrete statements.
3. **Structural notes.** Where the same mechanism appears in two fields, write the two instances side by side and the
   dictionary between them. Examples of the kind meant: a positivity, a trace formula, an index theorem, a lift, a
   symmetry eigenspace, a period, a counting function.
4. **What it suggests.** The interesting mathematics each map points to, as statements to prove or compute next, most
   promising first.

## How
- **Build the maps; do not grade them.** Work through the mathematics: write the objects and maps explicitly, compute
  and prove where you can, open the source at a locator where a step rests on it.
- **No labels from memory.** Never label anything proved, conjectural, true or false from memory. This mathematics
  postdates your training. Status comes only from what you did or opened in this task, or from the check events
  already recorded in our intakes.
- **Negatives.** A negative is a precise obstruction you proved to one formulation, followed by the next formulation.
- **Length.** As long as the mathematics needs, kept compact.
- **Rules.** No sub-agents; name every model with its effort; no git; no Grep or Glob over the whole of
  `<local>/Documents`. Leave unopened: prompt 74, SAT_KRONECKER_FINITE_FIELDS, SAT_WITNESS_EXTRACTION, the
  S6_SERIES_PUBLISH returns. If a safety notice stops you on a paper, drop that paper and move on.

## Final reply (under 200 words)
The two or three maps you find most interesting and why; the path of your note.
