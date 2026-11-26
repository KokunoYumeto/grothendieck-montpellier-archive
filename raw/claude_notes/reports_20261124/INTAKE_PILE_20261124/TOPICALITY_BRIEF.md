# Topicality pass over the intake pile: brief (25 Nov 2026)

From the main session 329fb1e6 (Claude Opus 5.5 at effort max). The user, 24 Nov 2026 ~22:3x UTC, on the pile's results:
"check them for topicality, because they're like a week old, which in AI mathematics terms means basically 4 decades. But
if they survive current new postings, deprecation, well, they might be interesting." After the weekly reset, Claude Fable
5.2 will hold a conference on the pile and write papers for the items that survive. Your verdicts decide which do.

## Input

- Your group's cluster files in `<local>/Documents/reports_20261124/INTAKE_PILE_20261124/`: `<CLUSTER>.md` and
  `<CLUSTER>_ITEMS.tsv`. Take every item rated useful, and the marginal ones the cluster file ranks among its most
  interesting.
- `LITERATURE_20261124.md` and `.tsv` in the same folder: what appeared from 14 Nov to 24 Nov, with an appendix listing all
  531 Hexagon posts of that window. It already shows one item overtaken: KTOWER's K_{4k}(Z) = 0 for k ≤ 20, against
  Mok–Zheng (to degree 120) and Pintar (to degree 104).

## For each item

Search for work that proves it, more than it, or a part of it, newer or older:
- newer postings: arXiv (full text where the abstract is not enough), Hexagon (https://hexagonmath.org), the AI
  laboratories' releases (github.com/openai/math with its history.md; github.com/anthropics/formal-math), ECCC;
- the classical literature the run or the cluster file names as the gate (for example Dwyer 2014 for the S₅ fields,
  Sweeney 2025 for S2COUNT, Elliott 2011 for Int(R), Lochak–Schneps 2006, Nakamura–Schneps 2000, Cais–Ellenberg–Zureick-
  Brown 2013, Clark 2006), and any standard reference the statement belongs to.
Open each source you rely on at the statement; a title or an abstract that only sounds close is not evidence.

Verdict, one of:
- **STILL NEW**: no work proves it; list the searches made (queries and where) so the verdict can be checked;
- **OVERTAKEN**: newer work proves it or more (cite with locator and date);
- **PARTLY**: newer or older work covers a part (cite, and say exactly what remains new);
- **KNOWN BEFORE**: older literature has it (cite with locator);
- **UNSETTLED**: you could not decide (say what would decide it).
Then: **worth a paper now?** yes or no, and why, in one or two sentences (usefulness first: does it contribute something
meaningful to its field?). And its Hexagon status where it has one (posted with id, drafted, or none).

## Output

In the pile folder: `TOPICALITY_<GROUP>.md`, opening with the items worth a paper now (ranked, one paragraph each: what,
why it still matters, the evidence for its novelty, where its proof is), then every item with its verdict; and
`TOPICALITY_<GROUP>.tsv` (cluster, run, item id, statement in one line, verdict, evidence links, worth a paper now, Hexagon
status). If writing is refused, put the content in your final message.

## Rules

Name every model with its effort setting. Leave unopened SAT_WITNESS*, SAT_KRONECKER*, the prompt-74 files and Codex's
runs; if a safety notice stops you on a paper, drop that paper and move on. No git. Keep notes in
`<local>/Documents/agent_notes/<your agent id>_NOTES.md`. Final message: the items worth a paper now, the items
overtaken or known, and anything you could not settle.
