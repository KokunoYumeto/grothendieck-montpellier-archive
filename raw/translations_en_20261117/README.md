# Raw English translation of Grothendieck's notes around Pursuing Stacks: cotes 103-107 and 134-1

17 Nov 2026. A raw, close English translation of the French in the LaTeX page transcriptions of the Montpellier
archive cotes 103, 104, 105 (Champs 2), 106 (Champs 3), 107 (Closed models) and 134-1 (the Breen letters), one file
per page. Passages Grothendieck wrote in English are kept as they are.

- **Translation:** GPT-6.1 Sol (OpenAI) at reasoning effort max, OpenAI Responses API, Flex tier, one request per
  page (`_work/prompt/system.txt` is the instruction). Requests were prepared, run and checked by Claude
  (Claude Opus 5.5 at effort high).
- **Not a reviewed translation.** No human has read these pages against the manuscript. Mathematics, macros and page
  markers are carried over from the transcription unchanged; the translation is only as good as the transcription
  it starts from.

## Sources, page by page

`CHECK.tsv` names the source file of every page. No second-pass (corrected) page exists yet for 105-107: on 17 Nov
`second_pass/out/MPL_105` and `second_pass/out/MPL_106+107` are empty. So:

- 105: the first pass `returns/MPL_105_unzipped/pages/` (48 pages);
- 106 and 107: the first pass `returns/MPL_106+107_unzipped/pages/` (16 + 25 pages);
- 103: the Codex web return `codex_web_20261113/returns/H103-01/out/pages/` (8 page files; the coverage list
  `packages_work/CODEX_COVERED_SCANS.tsv` names 16 scans of 103, the others have no page file there);
- 104: `codex_web_20261113/returns/H104-01` and `H104-02` (16 pages);
- 134-1: `codex_web_20261113/returns/H134-01` (5 pages).

When the second pass of 105-107 is delivered, those pages should be translated again from the corrected text.

## What was kept and how it was checked

The instruction keeps every macro and its arguments (`\scanpage`, `\mspage`, `\margin`, `\deleted`, `\inserted`,
`\unsure`, `\illegible`, `\uline`, diagrams), every formula unchanged, and translates the readings inside
`\deleted`, `\inserted`, `\margin` and `\unsure`, with every alternative of an `\unsure{a|b}` kept.

- **Pilot:** three pages read by Claude against the French before the run: 103 scan 5 (a full page of French prose
  on Picard categories), 106 scan 5 and 134-1 scan 2. All markup and formulas were intact, the deleted and inserted
  readings were translated, both alternatives of each `\unsure` were kept. One fix followed: the request's header
  line ("Cote …, scan …") is dropped before `\scanpage`.
- **Script check of every page** (`scripts/finalize.py`, results in `CHECK.tsv`): the `\scanpage`/`\mspage`
  sequence, the counts of the markup commands, and every math span as a multiset. Pages marked CHECK differ only in
  math spans; in the ones read (104 scans 5, 105 scan 17, 106 scan 9) the difference is French words inside `\text{}`
  or `\texttt{}` (et → and, tel que → such that, computer print-out labels), which the instruction asks to translate.

Scripts: `scripts/prep.py` (requests), `scripts/run.py` (Flex), `scripts/finalize.py` (writing and checks).

## Second job: the English layer of the second-pass pages (17 Nov 2026, ~22:5x-23:3x UTC)

- **Sources:** the Claude second pass only, `second_pass/out/<package>/*_scan*.tex`, never first-pass text. Done:
  cote **148** (72 pages: `MPL_144_168-184+148_001-028` for 148/001-028 and `MPL_148_029-072`) and cote **149**
  (136 pages: `MPL_149_001-090`, `MPL_149_091-136`). 208 pages, written to `148/` and `149/` under their second-pass
  file names; the source of every page is in `CHECK_SECOND_PASS.tsv` and `_work2/files.tsv`.
- **Translation:** GPT-6.1 Sol (OpenAI) at reasoning effort max, Responses API, Flex tier only; requests rejected as
  overloaded were sent again on Flex, never on another tier. Instruction: `_work2/prompt/system.txt`, the first job's
  with three rules from the blind graders: "sans doute" = "probably"; abbreviations written out (rat/K = rational over
  K); an inserted adjective may move to its English position inside its `\inserted{}`. Cost $7.05 (measured usage).
- **Stopped at the budget cap** before `MPL_143+141`. Not done, in order: 143+141 (50 pages), 145 (38), 147 (135 in
  two packages with second-pass pages; 147/138-190 has none), 150-152 with 120 (207), then 105 and 106+107.
- **No second-pass pages exist** on 17 Nov for 146 (`MPL_146_001-099`, `MPL_146_100-134` are empty), 147/138-190,
  105 and 106+107. So the first-pass translations of 105-107 in this folder are not redone.
- **Check events:** `scripts/finalize.py` (type: computation, on form only, not a check of the mathematics or of the
  translation): page markers in order, markup counts, math spans as a multiset. 192 pages OK, 16 flagged; in the
  flagged pages read (148/002, 009, 020, 042) the difference is French words inside `\text{}` in displays,
  translated as the instruction asks, with rows and formulas unchanged. Nobody has read the English against the
  French manuscript.
