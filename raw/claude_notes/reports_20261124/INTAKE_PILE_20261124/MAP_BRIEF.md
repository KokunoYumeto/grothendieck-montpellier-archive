# Connection maps over the intake pile: brief (25 Nov 2026)

From the main session 329fb1e6 (Claude Opus 5.5 at effort max). You are Claude Opus 5.5 at effort max. The user, 24 Nov 2026
~23:1x UTC: "have some 5.5 max agents do the thing where they look for all the connections between everything, including
the new hexagon results or whatever else results you can find. Because that makes the conference easier, because that
should include stuff from outside of our own research as well, wherever it informs new knowledge on top of our research
or to go with it." After the weekly reset, Claude Fable 5.2 holds a conference on this pile and writes papers; your map is
what it reads to see how everything fits and what new knowledge follows.

## Inputs (all in `<local>/Documents/reports_20261124/INTAKE_PILE_20261124/` unless named)

- The cluster files `<CLUSTER>.md` and `<CLUSTER>_ITEMS.tsv` (ALPOGE, ZETA_GRH, HODGE, GCT, AG_POLISH, SWEEP3_A, SWEEP3_B,
  LONGUE_MARCHE_A, LONGUE_MARCHE_B, DERIVATEURS); they point to the runs' proofs in `research_returns/` and elsewhere.
- `LITERATURE_20261124.md` and `.tsv` (14-24 Nov, with all 531 Hexagon posts of the window in its appendix);
  `TOPICALITY_*.md` and `OLDER_*.md` as they arrive (other agents are writing them now).
- Our earlier maps: `<local>/Documents/field_experts/structural_maps_20261123/`, the joint GCT lemma space
  `<local>/pequalnp_work/fleet_map/JOINT_GCT_LEMMA_SPACE.md`, and `<local>/Documents/knowledge/04_research/`.
- Outside: search Hexagon (https://hexagonmath.org), arXiv, ECCC and the AI laboratories' releases beyond the literature
  file wherever your region needs it. Open every source you rely on at the statement.

## How to work

Read the mathematics of the items you connect (the statements with their hypotheses, and the proofs where a link depends
on them). Then, for your region and its borders with the other regions:
- **Links as mechanisms.** A statement of one run is an input, a special case, a generalization, an obstruction, or a
  counterexample for another's; an outside result proves, strengthens, refutes, or supplies a missing input for one of
  ours. State each link as a map between exact statements, and say what it carries. A link is stated as real and its
  mechanism worked out; "no relation" is not an answer you give without having tried the standard bridges.
- **New knowledge.** Where a combination gives a new statement (an outside theorem plus one of ours, or two of ours),
  state it exactly and prove it if the proof is short; otherwise give the argument, the step that remains, and what would
  close it. Record each proof you check as a check event in `MAP_<REGION>_CHECK_EVENTS.tsv` (as BRIEF.md describes).
- **The project's terms.** Where it is real, say where a link lives in Grothendieck's frameworks (schemes over Z, λ-rings
  and K-theory, motives and correspondences, weights, Galois theory and anabelian geometry, topoi and derivators) and in
  his texts (cote, scan; SGA, EGA, FGA locators).
- When an argument stalls at an obstruction, try once defining the object that would cancel it and working on that.

## What to write

`MAP_<REGION>.md`, opening with **the new knowledge**, ranked by usefulness (each: the statement, its proof status, which
items and outside results it comes from, why it matters), then **the outside results that change our items** (and how),
then **the links** grouped by theme, then **conference topics and paper candidates** that cross clusters. And
`MAP_<REGION>.tsv`: one row per link (from, to, kind, mechanism in one line, status, locators). If writing is refused, put
the content in your final message.

## Rules

Name every model with its effort setting. Leave unopened SAT_WITNESS*, SAT_KRONECKER*, the prompt-74 files and Codex's runs;
the S6 series is another session's. If a safety notice stops you on a paper, drop it and move on. Never publish or send
anything; no git. Notes in `<local>/Documents/agent_notes/<your agent id>_NOTES.md`. Final message: the new
knowledge (short), the outside results that change our items, and the files written.
