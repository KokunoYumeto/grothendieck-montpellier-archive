# Grothendieck's Montpellier archive: transcriptions, checks and research notes

This repository is the hub of our work on the manuscripts of Alexander Grothendieck held at the Université de
Montpellier (Fonds Grothendieck; the scans are published by the university at
https://grothendieck.umontpellier.fr/archives-grothendieck/ and are not copied here). Everything below is AI-produced:
AI-transcribed text, AI-written research notes, AI-produced checks and corrections. It is work in progress, published as
it is made, with the prompts that produced it.

## Readers

### Which book to read

Each work comes in several books, all made from one checked transcription. **Start with the reading text** (the English one where there is one): the clean corrected text, for reading the mathematics.

- **Diplomatic**: the typescript or manuscript as it is, page for page, with the author's own corrections shown as they stand, for checking against the archive.
- **Corrected, with apparatus**: the corrected text with every editorial change numbered and listed, for anyone who wants to see what was changed and why. An apparatus entry records one change: what the source has, what the corrected text has, and why.
- **Corrected, with translator's notes** (Esquisse, EGA V): the English translation with the same apparatus and the translator's notes, for seeing how the French was rendered.
- **Annotated master** (Pursuing Stacks): the editors' copy from which the other books are printed; as a PDF it shows the same content as the corrected reader with apparatus.
- **Guide**: a companion on the text and its mathematics.
- **Blass's typescript** (EGA V, cote 24): Piotr Blass's 1987 English translation in the same three forms, a historical witness.

The notes of each release open with the same list for its own books.

- *Esquisse d'un programme* (1984, cote 119), final edition of 14 November 2026: French diplomatic text (both
  typescript copies), French corrected text with apparatus, French reading text, English translation with
  translator's notes, English reading text and a guide, each as PDF and LaTeX, in the release
  [esquisse-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/esquisse-readers-2026-11-14).
  Built by GPT-6 Astra (ChatGPT Pro mode) from the transcription by Claude Opus 5.5 at effort high (Message Batches
  API); the run's records are in `raw/pro_returns/ESQUISSE_READERS_20261114/FINAL_20261114T2138Z/`.
- *Nouveau EGA V* (cote 25) and Piotr Blass's 1987 translation typescript of it (cote 24), final edition of
  14 November 2026: French diplomatic text, corrected text with apparatus and reading text; a new English translation
  (with apparatus and translator's notes, and reading text); Blass's translation in three forms; a guide; each as PDF
  and LaTeX, in the release
  [ega-v-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/ega-v-readers-2026-11-14).
  Built by GPT-6 Astra (ChatGPT Pro mode) from the transcription by Claude Opus 5.5 at effort high (Message Batches
  API); the run's records are in `raw/pro_returns/EGA_V_READERS_20261114/FINAL_20261114T2314Z/`.
- *Pursuing Stacks* (1983, cotes 134-2 to 134-8), with R. Brown's English translation of the appendix, final edition of
  14 November 2026: diplomatic reader, corrected reader with apparatus (11,291 variants), reading text, annotated master
  and guide, as PDF, with the LaTeX sources, in the release
  [ps-readers-2026-11-14](https://github.com/KokunoYumeto/grothendieck-montpellier-archive/releases/tag/ps-readers-2026-11-14).
  Rebuilt on 15 November 2026 with changes to the layout only: each book now opens with the list of the five books and a
  key to its marks, and has running heads (book, archive scan, page) and bookmarks for the numbered sections.
  AI-transcribed by Claude Opus 5.5 at effort high; checked against the scans, corrected and typeset by GPT-6 Astra
  (ChatGPT Pro mode); the run's records are in `raw/pro_returns/PS_READERS_20261114/FINAL_20261114T2230Z/`.

## What is here

- `packages/<package>/first_pass/`: the transcription of one package of scans (cote and scan range in its name), as
  returned: `*_transcription.tex` (all pages), `pages/` (one file per scan), `*_notes.md` (research notes written after
  the transcription was frozen), `*_doubts.md`, `*_inventory.csv`, `progress.log`. A folder named
  `first_pass_checkpoint_<NNN>` holds a checkpoint of a package still being transcribed.
- `packages/<package>/PROMPT.md`: the prompt as sent.
- `packages/<package>/second_pass/`: the line-by-line check against the scans: corrected page files, `*_changes.md`
  (every change with the first reading, the corrected one, what the scan shows and a confidence) and
  `*_notes_checked.md` (the research notes checked), with the prompts in `second_pass/prompts/`.
- `typescripts/api_20261112/`: typed and printed pages transcribed through the Anthropic API (Pursuing Stacks, both EGA
  V versions, two copies of the Esquisse d'un programme, the Montreal seminar of 1970, Tapis de Quillen, the typed part
  of cote 119, Brown's translations of two letters), with the run records.
- `typescripts/codex_web_20261113/`: typed letters, lists, tables and the cote 10 typescript transcribed in Codex web,
  one folder per batch with its prompt.
- `research/plans/`: the archive plan, the section map and the reading of the archive as one programme.
- `research/prompts/`: research prompts on the archive's mathematics (their returns are published with La Longue Marche).

## Packages

| Package | First pass | Prompt as sent | Second pass |
|---|---|---|---|
| `MPL_142_001-093` | yes | yes | yes (100 files) |
| `MPL_142_094-122` | yes | yes | yes (33 files) |
| `MPL_144_001-061` | yes | yes | not yet |
| `MPL_144_062-121` | yes | yes | not yet |
| `MPL_144_122-167` | checkpoint_164 | yes | not yet |
| `MPL_144_168-184+148_001-028` | yes | yes | not yet |
| `MPL_146_001-099` | yes | yes | not yet |
| `MPL_146_100-134` | yes | yes | not yet |
| `MPL_147_003-047` | yes | yes | yes (51 files) |
| `MPL_147_048-137` | yes | yes | yes (100 files) |
| `MPL_147_138-190` | yes | yes | not yet |
| `MPL_149_001-090` | yes | yes | yes (100 files) |
| `MPL_149_091-136` | yes | yes | yes (52 files) |
| `MPL_16+47+54+44` | yes | yes | not yet |
| `MPL_1_002-050` | yes | yes | not yet |
| `MPL_5+6_001-037` | yes | yes | not yet |
| `MPL_6_038-067+7_001-060` | yes | yes | not yet |
| `MPL_7_061-072+8_001-078` | yes | yes | not yet |
| `MPL_8_079-081+9+4+100` | yes | yes | not yet |

## Related repositories

- La Longue Marche à travers la théorie de Galois (edition, companion, research returns):
  https://github.com/KokunoYumeto/grothendieck-longue-marche
- Les Dérivateurs (edition and companion): https://github.com/KokunoYumeto/grothendieck-derivateurs
- The French-school editions (EGA, FGA, SGA) and their site: https://github.com/KokunoYumeto/ega-fga-sga and
  https://kokunoyumeto.github.io/ega-fga-sga/
- SGA in French and English: https://github.com/KokunoYumeto/sga-fr, https://github.com/KokunoYumeto/sga-en

## How it was made

See `METHODOLOGY.md`. In short: first pass by GPT-6 Astra (ChatGPT Pro mode), one package of about 45 scans per
conversation, transcription frozen before any context was opened, then research notes; second pass by Claude Opus 5.5
at effort max, one block of about 15-18 scans per agent; typed pages by Claude Opus 5.5 at effort high (Message Batches
API) and by GPT-6 Astra at its maximum reasoning setting in Codex web; coordination by Claude Opus 5.5 at effort max
(Claude Code).

## Droits / Rights

Les droits sur l'œuvre originale appartiennent à son auteur ou à ses représentants ou ayants droit. Là où nous détenons
des droits, sur la transcription, la traduction, les corrections et la composition produites par IA, ils sont versés au
domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons
aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici,
veuillez ouvrir une issue GitHub et nous la retirerons.

**Prompts et méthode.** Les prompts, les gabarits, les scripts et la méthode de travail publiés ici sont versés au domaine public sous CC0 1.0. Si vous voulez faire un travail semblable, utilisez-les librement ; nous n'y revendiquons aucun droit.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights,
in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain
under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold.
If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it
down.


**Prompts and method.** The prompts, templates, scripts and working method published here are dedicated to the public domain under CC0 1.0. If you want to do similar work, use them freely; we claim no rights in them.