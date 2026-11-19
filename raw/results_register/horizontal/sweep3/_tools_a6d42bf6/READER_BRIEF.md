# Sweep 3 reader brief: sub-agents of a6d42bf6fe2b0d8a8 (cote 156, SA21), 18 Nov 2026

**What this brief is:**
- You are Claude Opus 5.5 at effort max, a sub-agent of the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max).
- The work is horizontal sweep 3 over the transcription notes of Grothendieck's Montpellier archive.
- The brief comes from the coordinator's messages of 18 Nov, about 22:2x and 22:5x UTC, which relay the main session and the user.
- The user: [the user's words, omitted] The user also asked for reading [the user's words, omitted].
- **Your job:** read one stretch, a cote part and its scan range, in full, and work its mathematics through.

All paths below are under `<local>/Documents\`.

## 1. Read first, for context

- `results_register\horizontal\sweep3\SA21\STUDY.md`:
  - §2 is 156-4, which a6d42bf6 read in full. It covers contrées, figures, multistrates, lieux, the ombre, the four axiom systems and the supports Σ.
  - §5 has the entry of your part, read from its axiom lines only.
- `results_register\horizontal\sweep3\SA21\HUNCHES.md` (H1-H12) and `RESEARCH_PACKAGES.md` (P1-P7).
- `results_register\horizontal\sweep2\SA21\WHAT_IS_WHERE.md` and `sweep2\SA21\OBJECTS.tsv`, for the items SA21-1 to SA21-15.
- `results_register\horizontal\sweep2\REPORTS\cote156_against_tame_topology.md`, the broad agent's report.
- `knowledge\03_archive\hua_project.md`, before you use Michel Hua's project.

## 2. Sources

**The transcription (the frozen text):**
- The Codex web returns are `grothendieck_archive_transcription_20261110\codex_web_20261113\returns\<folder>\out\<folder>_transcription.tex`, with `_doubts.md` and `_audit.md` beside each. The folders are:
  - J156-<n>-NN for 156-3 to 156-9;
  - H156-01 for 156-7, scans 2-9.
- The same .tex and the folder notes are also in `results_register\horizontal\inputs\SA21\codex\`.
- `\scanpage{N}` marks scan N.
- For orientation only, `results_register\horizontal\sweep3\_tools_a6d42bf6\c156-<n>.txt` gives a cleaned text per scan:
  - `\unsure{a|b}` becomes a[?b];
  - deletions are dropped;
  - margins appear as [margin: ...].
- `show.py` in the same folder prints a scan range: `python -I -B show.py <clean.txt> <first> <last> [cap]`.

**The scan images:**
- `grothendieck_archive_montpellier\20_vers_une_geometrie_des_formes\156-<n>.pdf`. Scan N is PDF page N; the archive pencil number is N−1.
- Render with MiKTeX into your scratchpad: `pdftoppm -f N -l N -r DPI [-x X -y Y -W W -H H] -png <pdf> <prefix>`.
- To locate a passage, render the page at about 45 dpi. Then crop at 200-500 dpi.
- **The ink decides every reading.**

**Michel Hua's project:**
- His modernised reading with notes is `ai_math_sources_20261114\hua_michel\commutator_grothendieck-project\transcripts\156-<n>\156-<n>.modern.tex`. His page p is our scan p + 1.
- Use it as a credited source of remarks and as a witness:
  - credit every point taken from it to "Michel Hua's project";
  - quote a phrase, never passages;
  - it is never the basis of a reading.
- His French batch files `batch-NN.fr.tex` serve only as witness H in a reading question.
- On 156-7 his text differs from the ink a great deal, so lean on him least there.

## 3. What to do, item by item in page order

1. What he defines, constructs or claims, with cote and scan.
2. What the page proves. Re-derive the steps that carry it; **each re-derivation is a check event**.
3. What is wrong, with the correction and the reason. Decide every doubtful reading that matters for the mathematics on the scan image.
4. What is open, with the strongest reduction on the page.
5. Dependencies:
   - to 156-4 (STUDY §2), to the other parts of cote 156, and to cotes 120-121, 150-151 and 154;
   - turn the candidate rows of `sweep3\SA21\DEPENDS.tsv` into read rows, with the page that shows each.
6. Hunches, each with its grounds: what may be true, and the links to other topics and to the literature. Say which of H1-H12 it confirms, refutes or sharpens.
7. Known results are cited with exact locators: author, title, journal or book, year, and section or theorem. Mark a locator you cannot check "locator to be checked". Never prove a known result again.
8. Deliverables, per scan range:
   - which passes the transcription has had (one Codex web transcription and one audit per folder, then yours);
   - which readings are open;
   - whether the stretch is ready for an edition, and for translation by GPT-6.2 Sol at reasoning effort max over the API.

## 4. Output

**Write as you go.** The weekly budget is near its end; whatever is cut resumes in the morning.

Write in `results_register\horizontal\sweep3\SA21\readings\`, creating the folder if needed. `<stretch>` is for example `156-6`, and the stretch code is 3, 5, 6, 7, 8 or 9.

- **`<stretch>.md`, the full reading,** readable by the user: what he does in order, with the places, what is proved, checked, wrong and open, and how it connects. Open it with:
  - who: Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8;
  - the date;
  - what was read and how: which pages in full, and which scans were viewed.
- **`<stretch>_CHECK_EVENTS.tsv`:**
  - header `id	date_utc	who	how	result	where`;
  - ids SA21-R<code>-nn;
  - who is "Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8 (reading <stretch>), horizontal sweep 3";
  - `how` begins with the check type: targeted proof check, independent re-proof, computation, targeted check of the reading against the scan image, or refuted, with the refined statement's id;
  - placing or reading an entry is not a check.
- **`<stretch>_CORRECTIONS.tsv`:** header `id	item	where	kind	what	corrected	evidence	decided_by`; ids SA21-K<code>-nn.
- **`<stretch>_DEPENDS.tsv`:** header `item	relation	other	basis	where`. Use items SA21-1 to SA21-15, or "156-<n>/<scan>" where no item fits.
- **`<stretch>_DELIVERABLES.tsv`:**
  - header `cote_part	scans	transcription	folders	passes	unsure_marks	unsure_per_scan	illegible	doubt_rows	open_readings	ready_for_edition	ready_for_translation	next_step`;
  - one row per stretch, with `cote_part` and `scans` exactly as in `sweep3\SA21\DELIVERABLES.tsv`, so that it replaces that row.
- **`<stretch>_INTEGRATION.md`,** with exactly three sections:
  - `## STUDY`: at most 700 words, the part's study in short;
  - `## HUNCHES`: new or sharpened hunches, numbered H<code>-n;
  - `## PACKAGES`: research packages in concept, each with the question, why it matters, what it rests on, the strongest known reduction and the material; or "none".

TSV cells are tab-separated, UTF-8, with no tabs or newlines inside a cell.

## 5. Rules

- Use `python -I -B` for scripts.
- Name the folder for every search. No recursive search over Documents or any big tree.
- No git. Never print or store credentials.
- Write only in `sweep3\SA21\readings\` and in your scratchpad. Everything else is read-only: the returns, the register, the transcriptions, and the other agents' files.
- No research prompt is written tonight; packages are concepts.
- Name every model with its effort setting.
- **Context.** Past 60-70 % of your context, read no more literature to read yourself in, and keep working on your stretch.
- **Compaction.** If you are compacted, your summary is a lead, not the record. Reread this brief and your own files, then go on.
- **Sub-agents.** For a long stretch you may launch your own sub-agents: Claude Opus 5.5 at effort max (model opus, effort max). Give each a scan range, this brief's path and an output name `<stretch>_<part>.md` in the same folder, and integrate their readings into your files.
- **Your final message to a6d42bf6fe2b0d8a8,** at most 200 words: the files written, the counts (check events, corrections), the three most important findings, and what is unfinished. Do not repeat the readings.
