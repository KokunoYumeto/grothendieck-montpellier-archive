# Brief: Hua's first pass by hand grade, and batch J against it (a302cb2d, Claude Opus 5.5 at effort high), 14 Nov 2026 ~19:2x UTC

From the main session (Claude Opus 5.5 at effort max), at the user's word (P5133: "Sample per hand grade. Yeah, I want
to know that"; P5134: "if they have good transcriptions, that's nice ... we did a bunch of [Astra transcriptions] for
stuff that they also have decent transcriptions of ... I can run more Astra transcriptions ... on the second account.
Though I could also be using that for OLP").

**Where we are.** Your check (`HUA_TRANSCRIPTION_QUALITY_20261114.md`) found by eye: typescripts (cote 22) about 0.6
errors per 100 words, a clear hand (cote 53) about 1, his fast notes (cote 13) about 2 plus many unread gaps, his dense
working hand (142/147/149) 3 to 8 plus gaps. The good grades rest on one page each. The user wants the verdict per
grade on a real sample, and to know where our Codex-web runs (GPT-6 Astra at effort max: batch H done, 0.18 per 100
words on 23 pages; batch J built, 110 folders, 840 pages) cover pages where Hua's text would already do.

**The work:**
1. **Sample per grade.** Grades A, B, C, D of `codex_web_20261113/HANDWRITING_CANDIDATES_20261114.md`, plus the
   typescripts as grade T. For each grade: six pages, two from each of three cotes of that grade that Hua has
   transcribed, taken from the middle and the end of each cote rather than its first pages. On each page, read Hua's
   text against Montpellier's scan by eye: errors (misreadings, omissions, struck text given as live, text that is
   not on the page), unread gaps, and how many of the errors carry their doubt mark; errors and gaps per 100 words.
   Where our own checked reading of the page exists, use it as the second witness.
2. **Verdict per grade:** (i) their text can be the basis of our second pass (checked line by line against the scan);
   (ii) a marked draft only; (iii) not to be used. For grades (i) and (ii): is checking their text cheaper than a new
   Codex-web transcription for the same final quality? Say why, with the figures.
3. **Batch J and batch H against Hua.** For every folder of batch J (`codex_web_20261113/drag/`) and batch H: the cote,
   pages, grade, whether Hua has a first pass of those pages, and the route the step-2 verdict gives (keep on Codex
   web / start from Hua's text plus a check / both). ->
   `codex_web_20261113/BATCH_J_H_VS_HUA_20261114.tsv`, with the totals (pages, folders, share of a weekly Codex-web
   allowance) per route, so the user can weigh the second account between transcriptions and the OLP.
4. **The two places of our second pass** your check flagged (142 #30, 149 #40): look at the scan, say which reading is
   right (ours, Hua's, neither), and write the correction if ours is wrong into the cote's second-pass changes file as
   a new logged row (first reading, corrected reading, what the scan shows, confidence).

**Write:** `grothendieck_archive_transcription_20261110/HUA_SAMPLE_PER_GRADE_20261114.md` (the verdict table per grade
first, then the figures, examples with locators, the J/H routing totals, the two rechecks) and the page table
`hua_quality_20261114/sample_per_grade.tsv`. Report back with the verdict table and the routing totals themselves.

**Rules.** No recursive search over big trees (Documents, F:, home, interlanguage): name the folder each time. Never
print a key or token. Name every model with its effort. Bound: about 150k tokens more (to about 550k).
