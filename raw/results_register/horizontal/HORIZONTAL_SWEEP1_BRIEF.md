# Horizontal sweep 1: the transcription notes, placed (18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max) for the five sweep agents, all Claude Opus 5.5 at effort max.

## Why
- **The user's words:**
  - P6848: "Stack, I guess all the math that we have, notes, etc., passes over it, checking, organizing ... tags,
    see what depends on what"; after the transcription "an enormous horizontal stack of nodes, some light, some heavy,
    some non-existent"; "do a light sweep, see where everything goes, do another light sweep, see how everything
    interlinks, see if there are obvious inconsistencies ... layer per layer".
  - 18 Nov ~14:3x UTC: "Remember, the point is the notes by Pro ... the notes by Pro transcription sessions ... the
    thousands of pages of unchecked notes, the horizontal stuff, the thing that is the foundation of everything";
    "you swept the research runs. That was vertical. Now do the horizontal thing"; "Start with sweep 1 over the actual
    thing that is to do"; "make sure to make it a check register ... keep track of what was checked, how many times,
    how".
- **Sweeps 0-2 covered the research runs only.** This sweep covers the notes that came with the transcriptions:
  - Pro's notes per package (the heavy nodes);
  - Work's and Codex-web's math notes per folder (the light nodes).
- **Sweep 1 is light.** Every entry is placed (what it is about, in today's terms), entries about the same thing are
  merged into one item, and obvious problems are flagged. Literature, proofs and research directions are later sweeps.

## Inputs (all on disk; do not unzip anything)
- `<local>/Documents\results_register\horizontal\inputs\SA<nn>\`, one folder per topic:
  - `NOTES_INDEX.tsv`: one row per note entry (id `<package>#<n>`, heading, kind, scans);
  - `pro\<package>_notes.md` and `pro\<package>_doubts.md`;
  - `second_pass\<package>\`: where Claude checked a package against the scans; a changed reading there is the
    current reading;
  - `codex\<folder>_notes.md`;
  - `TOPIC.md`;
  - the transcriptions `pro\<package>_transcription.tex` and `codex\<folder>_transcription.tex`, with
    `\scanpage{N}` at each scan page;
  - `PREAMBLE.tex`.

  These were built from the stage A dossiers at about 09-11 UTC on 18 Nov; the prompt the dossiers were written for
  is `grothendieck_archive_transcription_20261110\stage_a_20261118\STAGE_A_TEMPLATE.md`, for reference only.
- `results_register\horizontal\inputs\WORK_MATHNOTES_BY_TOPIC.tsv`: every Work and Codex-web math-notes file (363),
  with its topic, cote and path. Most are newer than the stage A inputs, and 196 are on cotes that had no Pro package.
  Their units (sections "What the pages do", "Statements left without proof", and so on) are entries too, with ids
  `work:<folder>#<n>`, the n-th unit of that file.
- **Two dossiers came back from GPT-6 Astra (ChatGPT Pro mode) and are provisional.** Use them as a first reading,
  never as a basis:
  - `grothendieck_archive_transcription_20261110\stage_a_20261118_sent\returns\SA02_final_20261118T1145Z_unzipped\`,
    for topic SA02;
  - `...\SA04_v1_final_20261118T1335Z_unzipped\`. In the v1 numbering, SA04 is "Théorie des motifs part 1", which
    is about topic SA05 here; compare its package list with SA05's.

## What to do, per topic, in the order given to you
1. **Place every entry** of the topic, in `PLACEMENT.tsv` (tab-separated, with this header):
   `entry_id, topic, cote, scans, kind, object, his_term, item, basis, fidelity, flag, note`
   - `object`: what the entry is about, as a short name in today's terms (English). Examples: "Riemann-Roch for
     coherent sheaves on a proper scheme", "the tame fundamental group of a punctured curve", "his reading question
     on 'Tens' vs 'Tors' at 84/112".
   - `his_term`: his word or notation for it.
   - `item`: `SA<nn>-<k>`. Entries about the same thing, in any package or folder of the topic, share an item.
   - `basis`: how you placed it: `index-row` (from the NOTES_INDEX row alone), `entry-read` (you read the entry), or
     `passage-read` (you also read the transcription passage it is about).
   - `fidelity`: only for `passage-read`: agrees / overstates / understates / misreads / not on the page. Otherwise
     `not checked`.
   - Every row of `NOTES_INDEX.tsv`, and every unit of the topic's Work math notes, gets a row. Read the entry
     whenever its heading does not say what it is about. Read the passage for every entry where his mathematics or
     the reading is at stake: a claim of his said to be proved, false or open; a reading question; two notes that
     disagree. Do this as far as your budget allows, and record the basis honestly.
2. **List the items** in `OBJECTS.tsv`:
   `item, object, kind, statement, entries, cotes_scans, status_on_pages, cross_topic, flags`
   - `statement`: one line in today's terms, with your reconstruction marked as yours.
   - `status_on_pages`: as his pages show it (proved there / sketched / stated without proof / corrected by him later
     / open), or `not checked`.
   - `cross_topic`: other topics or cotes where you saw the same object.
3. **Record what you found** in `FLAGS.tsv`: `kind, where, what, evidence`. The kinds are:
   - suspected misreading (the mathematics says the ink may read otherwise; decided later on the scans);
   - note overstates or misreads the page;
   - the same thing noted with different readings or statements;
   - notes that contradict each other;
   - a link across folders;
   - the LM/Dérivateurs lens: a note that reads the topic through La Longue Marche or Les Dérivateurs rather than in
     its own terms.
4. **Write `TOPIC_NOTES.md`:** what the topic's notes cover, the main objects and clusters, what is light and what is
   heavy, the counts (entries, items, basis, fidelity, flags), and what sweep 2 should look at first. If the harness
   refuses the write, put the text in your final message; the main session saves it.
5. **Keep `CHECK_EVENTS.tsv` as you go.** This is a by-product, not the job: the user wants what was checked, how
   many times and how, kept in one standard, easy form.
   - One row per check: `id, date_utc, who, how, result, where`.
     - `id`: the entry id or item id.
     - `who`: "Claude Opus 5.5 at effort max, <your agent id>, horizontal sweep 1".
     - `how`: for example, note checked against the page, or claim checked by computation.
     - `result`: for example, agrees or misreads.
     - `where`: file:line.
   - Placing an entry is not a check, and reading a note is not a check of it.
   - A script merges every `CHECK_EVENTS.tsv` into the central register, `results_register\CHECK_REGISTER.tsv`.

Outputs go to `<local>/Documents\results_register\horizontal\sweep1\SA<nn>\`. Write nothing anywhere else.

## Working together (the user: the broad agent coordinates; the deep agents keep digging and check in with it)
- **After each topic**, append to `results_register\horizontal\sweep1\CHECKINS\<your agent id>.md`:
  - the topic and the time (UTC, from `date -u`);
  - the counts;
  - the five most important flags;
  - the objects you saw cross into other topics.
- **Before each topic**, read `results_register\horizontal\sweep1\INBOX\<your agent id>.md`, if it exists. The broad
  agent writes there what other topics found about your objects.
- **The broad agent** (a0c4bb37) keeps `results_register\horizontal\sweep1\GLOBAL\`:
  - `GLOBAL_OBJECTS.tsv`: one tag space for all topics. Each global object has a 4-character tag (digits and capital
    letters), the items of every topic that are the same object, and its status;
  - `CROSS_TOPIC.md`.

  It reads the check-ins as they arrive, writes into the inboxes what concerns other agents, and runs its own topics
  through its sub-agents.

## Rules
- **Compute bound:** up to 950k tokens of context for each agent (the user's cap), topic by topic. If you reach it
  with topics left, write the state in your check-in and stop.
- Use `python -I -B` for scripts, and name the folder for every search: no recursive search over Documents or a big
  tree. Do not use git. Never print or store credentials.
- Read the topic in its own terms. Your knowledge of the research runs gives links, recorded as links (FLAGS kind "a
  link across folders", or `cross_topic`), never the lens.
- Keep three things apart: what his pages show, what the notes say, and what you infer.
