# Brief for the sweep-3 readers of ae4ae3dc17acaa440 (SA20 and SA22)

From ae4ae3dc17acaa440 (Claude Opus 5.5 at effort max), 18 Nov 2026, after the main session's additions of about 22:5x
and 23:1x UTC. Each reader gets this file and a short message naming its stretch.

## 1. The task

Read your stretch in full and work it through, as the sweep-3 brief asks. The brief is quoted verbatim at the top of
`results_register/horizontal/sweep3/SA20/STUDY.md`; read it first. Then read what is already written for your topic,
for its style and its ids:
- `sweep3/SA20/STUDY.md` (or `sweep3/SA22/STUDY.md`);
- HUNCHES.md and RESEARCH_PACKAGES.md in the same folder;
- the TSV files in the same folder.

For each item of your stretch, in the mathematical order of `results_register/horizontal/sweep2/SA<nn>/WHAT_IS_WHERE.md`:
1. **Read every transcribed page in full:** the `.tex` next to each notes file, with `\scanpage{N}` at each scan, and
   the notes and doubts files of the package. Look at the scan image wherever the reading is in doubt; the ink decides.
2. **Work through the mathematics:**
   - what he defines, constructs or claims;
   - what the page proves;
   - re-derive the steps that carry it; each re-derivation is a check event;
   - what is wrong, with the correction and the reason;
   - what is open, with the strongest reduction on the page.
   Cite known results with exact locators; do not prove them again. Literature you cite from memory is marked "from
   memory".
3. **Close the dependencies by reading.** Turn the candidate and "our reading" rows of `sweep2/SA<nn>/DEPENDS.tsv` for
   your items into read rows, each with the page that shows it, or record that the page shows no such dependence.
4. **Hunches,** each with its grounds: what may be true, what the pages point at, links to other topics and to the
   literature.
5. **Research packages, in concept only** (no prompt is written): the question, why it matters, what it rests on, the
   strongest known reduction, and the material a run would need.
6. **Deliverables,** per cote and scan range:
   - which passes the transcription has had;
   - which readings are open;
   - whether the stretch is ready to be edited as a transcription edition and translated (GPT-6.2 Sol at reasoning
     effort max over the API).

Placing or reading an entry is not a check.

## 2. Files

**Inputs:**
- the packages in `results_register/horizontal/inputs/SA20/` (pro/, codex/, api/), or in `inputs/SA22/`;
- `PREAMBLE.tex` and `NOTES_INDEX.tsv` in the same folder;
- the sweep-2 tables in `sweep2/SA<nn>/`: PLACEMENT, OBJECTS, FLAGS, DEPENDS, CLAIM_LINKS, UNIT_LINKS, CORRECTIONS.

**Scan images:**
- `<local>/Documents\grothendieck_archive_montpellier\<section>\<cote>.pdf`, where scan N is PDF page N. Find
  the section with Glob, pattern `*/<cote>.pdf`, path set to that folder.
- To render a page:
  `python -I -B <local>/AppData/Local/Temp/claude/f2c80a22394db22f/b68718a3-5179-4204-bc56-f8f64eac8af1/scratchpad/s2/scan.py <pdf> <page> <out.png> [x0 y0 x1 y1] [scale] [maxside]`.
  Write the PNG to your own scratchpad, then Read it.

**Compact reading of a .tex:**
`python -I -B .../scratchpad/s2/tx.py <tex> <first line> <last line> > <your scratch file>`, with the same folder as
scan.py.
- It collapses TikZ and shows `\unsure{a|b}` as [a|b], insertions as <+…>, deletions as <-…>, and margins as <m: …>.
- Read its output in parts.

**Michel Hua's project:** `knowledge/03_archive/hua_project.md`, and his modernised readings with their notes,
`Documents/ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts/<cote>/<cote>.modern.tex`.
- His page p is our scan p + 1.
- Credit every point taken from him to "Michel Hua's project", quoting a phrase, not passages.
- He is a witness and a source of remarks, never the basis of a reading: the ink decides.
- His French batch files serve only as witness H in a reading question.

## 3. Outputs

Write only your own files, in `results_register/horizontal/sweep3/SA<nn>/readings/`, named after your stretch.
- Write as you go: create the files at the start and append item by item, so a cut run leaves its work.
- Do not edit STUDY.md, the TSVs of the topic folder, sweep1/ or sweep2/. I integrate your files.

The files:
- `<stretch>.md`: the full working.
- `<stretch>_STUDY_SECTION.md`: a section for STUDY.md, readable by the user, at most about 2,500 words. Follow the
  style of the existing sections: what he does in order, with the places; what is proved, checked, wrong and open; how
  it connects.
- `<stretch>_HUNCHES.md`, with ids H<nn>-<stretch>-1, -2, …
- `<stretch>_PACKAGES.md`, with ids R<nn>-<stretch>-1, …
- `<stretch>_CHECK_EVENTS.tsv`, header `id	date_utc	who	how	result	where`. The `who` column reads
  "Claude Opus 5.5 at effort max, reader <stretch>, horizontal sweep 3".
- `<stretch>_CORRECTIONS.tsv`, header `id	where	kind	what	corrected_or_refined	basis	who	date`.
- `<stretch>_DEPENDS.tsv`, header `item	relation	other	basis	evidence`.
- `<stretch>_DELIVERABLES.tsv`, header
  `cote	scans	folder_or_package	passes	open_readings	ready_for_edition	note	translate_to	why` (wave 2, 19 Nov).
  - `translate_to`: the languages that stretch should be translated into, highest value first. English comes first
    for every stretch of his text. `none` for blank faces and for documents by others.
  - `why`: your own reason, naming the communities that work on the topic. Use
    `knowledge/03_archive/translation_targets.md`: never automatic, weighed against EGA and SGA in the same language;
    Russian not for now.

## 4. Rules

- No git. Use `python -I -B` for scripts. Name the folder for every search; no recursive search over Documents or any
  big tree. Never print or store credentials.
- Name every model with its effort setting.
- **Sub-agents:** the last line of your launch message sets how many you may use. In wave 2 (19 Nov) that is none.
- **Compute bound:** about 400k tokens of context. Past 60–70 % of your context, read no more literature to read
  yourself in; finish the work at hand from the stretch's own files.
- **Typed or printed versos by other authors** (for example Bourbaki drafts): describe them and note them in
  DELIVERABLES for the user's decision. Say it once.
- **Personal data** on administrative documents, such as hiring or appointment minutes and staff lists: describe the
  document in one line. Never reproduce a name, a vote or a date of birth from it. Two such documents are being
  redacted by the GitHub housekeeper: the minutes of a 17 July 1984 commission on a 155 verso, and the 1979 staff list
  68/018.
- **Final report to me,** at most about 400 words:
  - items covered;
  - counts of check events and corrections;
  - what is wrong and what is open;
  - the hunches and the packages;
  - the deliverable stretches;
  - anything not read.
