# Brief: grade the Codex-web test HC1-01 (14 Nov 2026, ~21:1x UTC)

From the main session (Claude Opus 5.5 at effort max) to a302cb2d (Claude Opus 5.5 at effort high), which designed the
routing plan (ROUTING_THREE_TIERS_20261114) and graded Hua's first pass by hand grade.

Sub-agents allowed: 0
Compute bound: about 120k tokens of new work; stop and report at that point with what is graded.

## The return

HC1-01 is the Codex-web test of grade C working notes: cote 1 ("Analyse fonctionnelle : notes manuscrites (s.d.),
lettre (1953)"), scans 4, 12, 15, 24, 27, 35, 39, 49. The user sent it ~19:57 UTC; it froze its transcription at
20:47 UTC. Filed unchanged at:

- `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/HC1-01/out/` (pages/, HC1-01_transcription.tex,
  doubts, audit, inventory, notes, progress.log; its own count: 265 unsure, 8 illegible, 116 deleted);
- its prompt and inputs: `codex_web_20261113/drag/HC1-01/` (PROMPT.md, PREAMBLE.tex, HC1-01_scans.zip with the whole
  page and three thirds per scan). Unzip the scans into a scratch folder of your own, not into the drag folder.

## The task

1. Grade all 8 pages by eye against the scans with your per-grade method: errors per 100 words by kind (misreadings,
   omissions, false certainty where the hand is unclear, formulas symbol by symbol, deletions and insertions), and
   whether its doubt marks fall where the hand is really unclear.
2. Compare with what we know for grade C: Hua's first pass (1.5 per 100 words; 3-8 on dense pages) and our Pro
   transcriptions of grade C pages where you have their rates. If any of these 8 pages has a transcription by Pro or
   by Hua, use it as a second witness.
3. Verdict for the routing plan: can Codex web take grade C working notes (light, dense, or neither), and does the
   answer change ROUTING_THREE_TIERS_20261114 (which pages move from Pro to Codex web)? Name every model with its
   effort setting; where the Codex-web effort is not on record, say so.

Write `codex_web_20261113/GRADE_HC1-01_20261114.md` (table per page, the verdict, the change to the routing plan) and
a row per page in `codex_web_20261113/GRADE_HC1-01_20261114.tsv`. Do not edit the return or the routing plan itself.

Machine safety: no recursive search over big folders (Documents, interlanguage); open the files named here.
