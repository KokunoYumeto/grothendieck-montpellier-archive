# Sweep 3 reader brief, round 2: sub-agents of a6d42bf6fe2b0d8a8 (SA10, SA11, SA21), 19 Nov 2026

**Who and what:**
- You are Claude Opus 5.5 at effort max, a reader for the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max).
- The work is horizontal sweep 3 over the transcription notes of Grothendieck's Montpellier archive.
- The brief comes from the coordinator's messages of 18 Nov (about 22:2x and 22:5x UTC) and 19 Nov (about 02:2x UTC), which relay the main session and the user. The user: [the user's words, omitted]
- **Your stretch, its topic and its sources are in your launch prompt.** Read that stretch in full, page by page, and work its mathematics through.

**How this brief relates to the first one.**
- The method, the output format and the rules are those of `results_register\horizontal\sweep3\_tools_a6d42bf6\READER_BRIEF.md`, sections 3, 4 and 5. Read it.
- It changes in three ways:
  1. you write in your topic's `readings\` folder (below), not necessarily in SA21's;
  2. you launch **no sub-agents**;
  3. your sources are the ones listed here.

All paths are under `<local>/Documents\`.

## 1. Read first, for context

- **Your topic's sweep-3 files:** `results_register\horizontal\sweep3\SA<nn>\STUDY.md`, `HUNCHES.md`, `RESEARCH_PACKAGES.md`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
- **Its sweep-2 map:** `results_register\horizontal\sweep2\SA<nn>\WHAT_IS_WHERE.md`.
- **The readings your launch prompt names**, which you must not redo. For example:
  - the SA20 readings of cote 120 and of 121/49-73;
  - the first reading of your 156 part.
- **Before you use Michel Hua's project:** `knowledge\03_archive\hua_project.md`.

## 2. Sources

**Pro packages.** Each has a transcription, the first pass's notes and doubts:
- `results_register\horizontal\inputs\SA10\pro\`: cotes 150, 151, 152+120;
- `inputs\SA11\pro\`: cote 154, and 121/49-73 with 153 and 155;
- `inputs\SA20\pro\`: MPL_121_001-048 and MPL_152+120.

The Pro packages were made by GPT-6 Astra (ChatGPT Pro mode).

**Second-pass corrected text (17 Nov 2026).**
- For cotes 150, 151 and 152+120, the transcription was corrected against the scans by second-pass block agents (Claude Opus 5.5 at effort max), with Michel Hua's project as witness.
- The corrected files are `grothendieck_archive_transcription_20261110\second_pass\out\<package>\<package>_<cote>_scanNNN.tex`, one per scan, with `_changes.md` and `_notes_checked.md` per block. **Read those, not the frozen Pro text.**
- There is no second pass yet for cotes 121 and 154: their folders there are empty, so read the Pro text.

**Codex folders:**
- `inputs\SA11\codex\K154-01` and `K154-02`, a second witness for 154/46-76;
- for cote 156, the Codex web returns `grothendieck_archive_transcription_20261110\codex_web_20261113\returns\<folder>\out\` (J156-<n>-NN, H156-01).

**Cleaned text, for orientation.**
- `python -I -B results_register\horizontal\sweep3\_tools_a6d42bf6\clean_tex.py <out.txt> <tex>` writes one block per scan into your scratchpad.
- `show.py <clean.txt> <first> <last> [cap]` prints a scan range.
- Ready-made: `c151b.txt` (151/32-75), `c154a.txt` (154/1-45) and `c156-<n>.txt`, all in `_tools_a6d42bf6\`.
- The .tex is the frozen text. `\scanpage{N}` marks scan N.

**Scan images.** Scan N is PDF page N.
- `grothendieck_archive_montpellier\19_espaces_stratifies\<cote>.pdf` for cotes 150-155;
- `grothendieck_archive_montpellier\13_autour_desquisse_dun_programme\<cote>.pdf` for 120-121;
- `grothendieck_archive_montpellier\20_vers_une_geometrie_des_formes\156-<n>.pdf`.

Render with MiKTeX into your scratchpad: `pdftoppm -f N -l N -r DPI [-x X -y Y -W W -H H] -png <pdf> <prefix>`. Locate a passage at about 45 dpi, then crop at 200-500 dpi. **The ink decides every reading.**

**Michel Hua's project.**
- The files are `ai_math_sources_20261114\hua_michel\commutator_grothendieck-project\transcripts\<cote>\<cote>.modern.tex`.
- His page p is our scan p + 1. Check this offset on the first pages of each cote.
- Use it as a credited witness and a source of remarks:
  - credit every point taken from it to "Michel Hua's project";
  - quote a phrase, never passages;
  - it is never the basis of a reading.
- His French batch files serve only as witness H in a reading question.

## 3. Output

- **Where you write:** `results_register\horizontal\sweep3\SA<nn>\readings\`, creating the folder if needed. For a stretch that serves two topics (cote 121 serves SA11 and, through SA20, SA10), write in the folder your launch prompt names.
- **The files**, in the formats of READER_BRIEF.md §4:
  - `<stretch>.md`;
  - `<stretch>_CHECK_EVENTS.tsv`, `_CORRECTIONS.tsv`, `_DEPENDS.tsv` and `_DELIVERABLES.tsv`;
  - `<stretch>_INTEGRATION.md`, with the sections `## STUDY` (at most 700 words), `## HUNCHES` and `## PACKAGES`.
- **Check-event ids:** use the prefix your launch prompt gives, for example SA10-R150-nn, with CORRECTIONS ids SA10-K150-nn.
- **DELIVERABLES:**
  - write one row for each row of the topic's DELIVERABLES.tsv that your stretch touches;
  - copy `cote_part` and `scans` exactly from that row, so that the merge replaces it;
  - fill the 13 columns of READER_BRIEF.md §4 and leave out translate_to and why, which the merge keeps;
  - in `passes`, keep what was there and add what your reading did, and for which scans.
- **Write as you go,** so that a cut run loses nothing.

## 4. Rules

The rules of READER_BRIEF.md §5 apply, with these changes:
- write only in your readings folder and your scratchpad;
- launch no sub-agents.

In short:
- use `python -I -B` for scripts;
- name the folder for every search, with no recursive search over Documents or any big tree;
- no git, no paid API, never print or store credentials;
- name every model with its effort setting;
- past 60-70 % of your context, read no more literature to read yourself in;
- if you are compacted, your summary is a lead, not the record: reread this brief, READER_BRIEF.md and your own files, then go on.

**Your final message to a6d42bf6fe2b0d8a8,** at most 200 words:
- the files written;
- the counts of check events and corrections;
- the three most important findings;
- what is unfinished.
