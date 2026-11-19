# Sweep 3 readers: shared brief (motives and crystals cluster: SA05, SA06, SA07, SA15)

From agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max), 18 Nov 2026, at the main session's word. You are a reader,
Claude Opus 5.5 at effort max. Your launch prompt names your topic SA<nn> and your stretch. This file is the rest of
your brief. If you are compacted, the summary is a lead, not the record: reread this file and your own output files,
then go on.

## The task

Read every transcribed page of your stretch in full, in page order, and work it through:
1. **Read** the Pro transcription (`.tex`) of each page; `\scanpage{N}` marks scan N. Wherever the reading is in doubt
   (`\unsure`, `\illegible`, a formula that does not parse or contradicts its context), look at the scan image. The ink
   decides.
2. **Work through the mathematics** of each item:
   - what he defines, constructs or claims;
   - what the page proves;
   - re-derive the steps that carry it, and record each re-derivation as a check event;
   - what is wrong, with the correction and the reason;
   - what is open, with the strongest reduction on the page.
   Known results are cited with exact locators, not proved again. A locator you have not opened is marked
   "(locator unverified)".
3. **Dependencies.** Name the items each piece uses (ids from `sweep2/SA<nn>/WHAT_IS_WHERE.md`, any topic), with the page
   that shows it.
4. **Hunches.** Write down every hunch with its grounds: what may be true, what the pages point at, and its links to
   other topics and to the literature.
5. **Deliverable state** of the stretch: the passes it has had (Pro, Codex web, Work notes), the open readings left, and
   whether it is ready to be edited as a transcription edition.
6. **Reused material.** Typescripts or printed leaves that are not his (Bourbaki drafts, "Tribu", others' papers): identify
   them in one line each and do not study them.

## Where things are (all under <local>/Documents)

- **Pro transcription pages:** `grothendieck_archive_transcription_20261110/returns/<pkg>_unzipped/`, in a `pages/` folder,
  named `<pkg>_<cote>_scanNNN.tex`. The notes file is `<pkg>_notes.md` in the same folder.
- **Reader tool**, which prints a stretch with `\deleted` dropped, `\unsure{a|b}` shown as `a(?)` and margins inline:
  ```
  cd <local>/Documents/results_register/horizontal/sweep2/_tools_a28ea31f
  python -I -B readtex.py <pkg> <cote> <first> <last> [keepdel] [--nodiag]
  ```
  It reduces recognized reused typescripts to one line. Redirect long output to your scratchpad and read it in parts.
- **Codex web returns:** `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/<folder>/out/`, holding
  the notes, the math notes and the `.tex`. They are a second witness where they exist.
- **Scans:** `grothendieck_archive_montpellier/<section>/<cote>.pdf`. Cotes 10-16, 18 and 19 are in `03_theorie_des_motifs`;
  cotes 4-9 are in `02_cristaux`; cote 100 is not there. For any other cote, list the section folders one level deep. Scan N is PDF page N, and
  the archive sheet number is N - 1. Render and crop like this:
  ```
  pdftoppm -f N -l N -r 250 -png <pdf> <out>
  magick <png> -crop WxH+X+Y -level 10%,85% <crop.png>
  ```
  Then read the crop.
- **Michel Hua's project** has modernised readings with notes. Read `knowledge/03_archive/hua_project.md` first for the
  rules of that relation. The readings are in
  `ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts/<cote>/<cote>.modern.tex`. His page p
  is our scan p + 1. Use them as a credited witness and a source of remarks, never as the basis of a reading. Credit every
  point taken from them to "Michel Hua's project", quoting a phrase, not passages. Nothing is sent to his project.
- **Context:**
  - items, places and sweep-2 flags: `results_register/horizontal/sweep2/SA<nn>/WHAT_IS_WHERE.md`;
  - what sweep 3 already did: `results_register/horizontal/sweep3/SA<nn>/STUDY.md`.

## What you write (only there)

In `results_register/horizontal/sweep3/SA<nn>/readings/` (create it if needed), with `<stretch>` from your launch prompt:
- `<stretch>.md`, readable by the user. Per item, in page order: the places, what he does, what is proved, what you
  checked, what is wrong, what is open. After the items, give the hunches, the dependencies and the deliverable state.
- `<stretch>_CHECK_EVENTS.tsv`, with a header row and six columns: `id`, `date_utc`, `who`, `how`, `result`, `where`.
  - `id` is `<pkg> (<cote>:<scan>)`.
  - `who` is "Claude Opus 5.5 at effort max, <your agent id or name>, sweep 3 reader".
  - `how` names the type: targeted proof check / independent re-proof / computation / reading decided on the scan
    image / refuted, with the refined statement.
  - Placing or reading an entry is not a check.
- `<stretch>_CORRECTIONS.tsv`, with a header row and five columns: `where`, `what`, `correction`, `reason`, `who`.

**Write as you go:** append after each page or item. The weekly budget may cut you at any moment, and the run resumes from
your files.

## Rules

- No git commands at all.
- No recursive search over Documents or interlanguage; name the folder for every search.
- Run Python as `python -I -B`.
- Write nothing outside your `readings/` folder.
- No prompts are written. No cleanup.
- Name every model with its effort setting.
- Past about 60-70 % of your context, read no more literature; keep working on the pages.

**Long stretches.** You may split a long stretch among your own readers: Claude Opus 5.5 at effort max, this same brief,
one sub-stretch each, at most two at a time. You merge their files into yours, and they write
`<stretch>_part<k>.*` in the same folder. Your launch prompt gives your allowance.

**Your final message** to me is at most 150 words: the files you wrote; the counts of pages read, check events,
corrections and hunches; and the single most important finding. Everything else goes in the files.
