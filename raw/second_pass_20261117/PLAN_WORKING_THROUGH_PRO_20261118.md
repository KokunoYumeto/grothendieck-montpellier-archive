# Plan: Pro works through the mathematics of one folder, in its own terms (18 Nov 2026)

Written by the main session (Claude Opus 5.5 at effort max) at the user's request: "build one that works with the
mathematics of one package in its own terms ... contextualized by the full transcription of something like EGA V";
"What is your actual well thought out plan?" The pitfalls are in `PROJECT_RECORD.md`, section 2l. The method of
reading is `PLAN_MATH_THIRD_PASS_20261117.md`, sections 2-5 (a7d5d89d), carried over to GPT-6 Astra (ChatGPT Pro mode).

## 0. The combined pass, planned for effectiveness (18 Nov 00:3x UTC)

The user: "There is [an enormous amount of] pro-prompt notes. Just the processing of that is enormous. We need second
visual passes on stuff. The combination of that would be smart ... You take the math, you take the scans, you go and
make all of it work together, right? Just grind out the math. But you need to plan the fuck out of that. In the sense,
not of like holding yourself back, but making it effective."

**One pass per folder does three jobs at once:**
1. the second visual pass against the scans;
2. Pro's notes consumed;
3. the mathematics ground out: claims decided, his conjectures attacked under the ledger rule.

**Scope** (`reports_20261117/archive_report_data.json`, 17 Nov):
- Outside La Longue Marche and Les Dérivateurs (3,719 pages, already edited), 6,802 pages are transcribed: Pro 4,409,
  Codex 1,060 and API typescripts 1,361. Round 1 of batch K adds about 530, all back by 18 Nov 00:28 UTC.
- 801 of them have a Claude second pass already. Those still need the notes and the mathematics.
- 78 cotes outside the two editions are at least 90 % transcribed, 4,399 pages. They go first, with their holes filled
  in the same run.

**Throughput, estimated until the pilot measures it:**
- A Pro transcription runs at about 3 minutes a scan. The combined pass is estimated at 6-10 minutes a page.
- 7,300 pages is then about 730-1,200 slot-hours, about 180 prompts at about 40 pages each. About 435 prompts are left.
- At 2 runs per account on four accounts, that is about 4-6 days of continuous running.
- The binding limits are therefore slots, the user's sending time on accounts 1-3, and the merge of Chat and Work at
  the end of November. They are not the prompt count. The bulk is front-loaded before the merge.

**Design choices for effectiveness:**
1. **The unit is a folder or a slice of 30-60 pages,** cut at the mathematical units the notes already list, never in
   the middle of an argument. The size is set from the pilot's measured rate, so a run finishes with hourly checkpoints.
2. **A second witness for the visual pass,** so that Pro does not re-read its own text blind to its own errors (the
   triple check: reading with the text in view lets plausible words through).
   - Pro-first-pass folders carry Hua's text as a witness, and Codex's reading where one exists.
   - For a Codex-first-pass folder, Pro is the second witness.
   - Every doubt mark and every logic-bearing word is read on the crop before any existing reading is looked at.
3. **The notes are not a separate stage.**
   - Each pass consumes its folder's notes and doubts: each note gets a verdict.
   - A script-built concordance of the whole topic's raw notes ships with the package, indexed by object, notation and
     stable note id. Building it costs no Pro prompt and no model.
   - The topic dossier then grows by merging each pass's tables as they come back.
   - This replaces the separate Stage A prompts of section 1a: it saves about 25 prompts and a day, and integrates
     through the index and the merge.
4. **Context in the topic's own terms,** per section 2: the topic's complete transcriptions, his published text as TeX,
   the period sources the pages cite. Our results come in a zip opened last.
5. **Order:**
   - the folders at least 90 % done first;
   - topic by topic, the topics the vertical work never touched first;
   - within a topic, in his chronological order, so each pass has the earlier folders' worked-through tables as
     context.
6. **The pipeline:**
   1. A builder script assembles each package (pages, scans and thirds, notes, witness, concordance, context zip,
      results zip; parts under 10 MB) and runs `--lint-math`.
   2. Sending: account 4 by the sender at 2 Pro runs when the user releases it; accounts 1-3 by the user.
   3. Filing by the watcher and filer.
   4. A merge script folds each return's tables into the topic dossier and the global registers.
   5. Claude (the scarce meter) does only these:
      - samples each batch: a few corrections checked on the scans, a few claim statuses worked through again;
      - runs the consequences loop, for corrections that touch our registers or waiting prompts;
      - keeps the running audit current.
7. **Pilot first, then scale on the measured rate:**
   - cote 22: Pro-first, EGA V as context;
   - cote 81: Codex-first, the *Esquisse* as context.

   Measure minutes a page and the quality of the corrections and claim statuses. Then the schedule.

## 0a. Who does which layer (the user, 18 Nov ~01:2x UTC, after the CTRL-148 grading and OpenAI's description of Pro)

The user: "Pro should do the reading, second pass, and then build the corrections mostly on where the mathematics says
that it should be, and then checks that. But it should be doing the math ... which is why it's a good thing that we
mostly had it mathematical note-taking and processing while transcribing, which was what it was good for."

- **Reading the ink belongs to Work: GPT-6.2 Astra at Max.** It read best on CTRL-148 (1.69 errors per 100 words
  against Pro's 3.26, with the load caveat). So:
  - pages with no transcription get one from Work;
  - pages Pro transcribed get a second reading from Work, which gives each page two witnesses;
  - pages Work transcribed already have one Work reading, and Hua's text is the second witness where he has it.
- **The mathematical pass belongs to Pro.** It is built for deep analysis by parallel attempts (OpenAI). Per folder it:
  - works through the mathematics with both readings, Hua's text and its own notes;
  - proposes corrections where the mathematics breaks, and settles each one on the crop;
  - consolidates the notes, does the mathematics, and attacks his conjectures;
  - writes the outputs of section 3.
- **The guard, from the controls** (PLAN_MATH_THIRD_PASS section 3): the mathematics raises the alarm and the ink
  decides. At 3 of the 29 residual places the mathematics favoured the wrong word ("implique" for "indique", an added
  "en prenant", "sommes disjointes"). So:
  - a mathematically expected reading never becomes the first reading on mathematical grounds alone;
  - the logic-bearing words are read on the crop every time.
- **Cost of the second readings by Work:** the 4,409 Pro-transcribed pages at about 0.03x a page come to about 130x. That
  is more than account 4 holds. Accounts 1-3 add 50x and 10x and 10x a week. So the second readings run over about two
  weeks, folders in the order of the mathematical pass. The pass on a folder waits for its second reading, or runs on
  one reading plus Hua's text where time is short.

## 1. What one package is

One complete folder of the archive, worked through by GPT-6 Astra (Pro mode). It is read the way a colleague who means
to use a draft reads it:
- the mathematics is worked through, streamlined and integrated;
- the text is corrected where the mathematics breaks and the ink confirms it;
- Pro's earlier notes on the folder are turned into checked items;
- the groundwork a career algebraic geometer needs is written beside his words.

**Missing pages are filled in the same run** (the user, 18 Nov 00:2x UTC: "if you're missing a page, the scans are there,
go transcribe"). The package carries the scans of the missing pages, and the run transcribes them first. So the 19
near-complete cotes are eligible as well as the 68 complete ones.

## 1a. The notes backlog: consumed, not added to (Stage A replaced by section 0, point 3)

All 103 returns' notes (13.16 MB) are unprocessed. The user: "that's a huge backlog. That needs to be fixed." And:
working through the folders must not leave yet more unprocessed notes behind. Two stages:

**Stage A: one Pro prompt per topic consolidates the notes of the whole topic** (about 20-25 prompts; large topics are
split by cote range). It works on the notes as they are now, before any more are made: the integration that was missed.

Input:
- every Pro notes and doubts file of the topic's returns, and the short notes of Codex returns as weaker leads;
- the topic's transcriptions;
- the topic's own sources;
- the notes-triage files, as an index only. Their "nothing" verdicts are not taken over: in a sample, 8 of 9 carried
  checkable mathematics.

Output, the topic dossier:
1. every note entry once, with a stable id, merged across packages;
2. the topic's claims map: his claims, where they are, their status as far as the transcription decides it,
   computations redone;
3. his open steps and open questions;
4. suspected misreadings and slips, marked for the ink, because they cannot be decided without the scans;
5. links across folders;
6. links to our results, kept apart and marked, since the context zips pulled the notes toward the Longue Marche and
   Dérivateurs.

Notes sizes by topic (17 Nov):

| Topic | Notes | Returns |
|---|---:|---:|
| Around La Longue Marche | 2.34 MB | 16 |
| Motives | 1.81 MB | 13 |
| Combinatorial geometry | 1.47 MB | 11 |
| De Rham | 1.24 MB | 11 |
| Around Pursuing Stacks | 1.09 MB | 4 |
| SGA | 0.92 MB | 7 |
| Stratified spaces | 0.88 MB | 8 |
| Crystals, Picard | 0.58 MB each | |
| The rest | under 0.4 MB each | |

**Stage B: the working-through package of each folder consumes that folder's notes.**
- Each note gets its final verdict against the ink (NOTES_VERDICTS.tsv), with the topic dossier as context.
- The run writes no free-form notes. Its outputs are the fixed tables and files of section 3, which merge by script,
  so the backlog shrinks and does not grow.
- The notes of returns that come in later go into their topic dossier's next update.

## 1b. What "horizontal" means here (the user, 18 Nov 00:3x UTC)

The user: "all those prompts that have thousands of fucking pages of notes, like, they are probably foundational, and
consolidating all of that makes pie in the sky sit on a foundation. Like, not chasing conjectures isn't necessarily the
way to make the foundation strong. It's just like it's developing it like horizontally, as opposed to only a few
pillars. But like taking in those fucking pro notes and making pro second pass all the Astra Max stuff."

So:
- **The foundation is the consolidated notes and the worked-through folders,** across every topic.
- **Conjectures are chased wherever they arise, in every topic,** not only on the few pillars of the Longue Marche,
  Les Dérivateurs and S6.
- **Everything first transcribed by GPT-6 Astra at Max (Codex Work) gets a Pro second pass,** which also writes the
  research notes Codex does not. For a Codex-transcribed folder, the Stage B package is that second pass: the run
  re-reads the Codex text against the scans as a second witness, and writes the Pro layer. Pilot 2 (cote 81, batch J) is
  such a folder.
  - That covers about 1,500 pages now: the 1,060 pages of batches A to J and HC1, round 1 of batch K and the controls.
  - If rounds 2-6 go to Codex, it covers 2,688 more.

## 2. "In its own terms": three rules, applied by me when a package is built

1. **The context is the subject's own, chosen by a fixed rule:**
   - the complete transcriptions of the other folders of the same topic;
   - his published text on the subject (EGA, SGA and the papers), as TeX from our editions;
   - the standard sources of the period that the pages cite, free sources only, TeX where it exists.

   Not in the context: our research registers and the Longue Marche or Dérivateurs results. Those pulled Pro's notes
   toward their own register.
2. **The account of each unit is written first in his notation and his words** (his objects, his names, his order of
   ideas). Today's restatement goes beside it, never instead of it.
3. **Our results come last,** from a second zip opened only after the folder's work is frozen, as the transcription
   prompts already do with their context zip. Only links with evidence go in: the same objects, the same statement. No
   forced links.

The user sees each pilot's context list and can veto or add to it. After the pilots, the rule chooses the context and
the list is in each package's README.

## 3. What the run does: fill the layers, in order (the user, 18 Nov 00:4x UTC)

The user: "foundation transcription with layer one, layer two, notes on transcription, which become a reflection of the
transcription. Layer three, math on that basis ... filling the layers is smart. Now, if you accidentally resolve
massive shit, yeah, oh well, we'll live ... The problem isn't necessarily trying to crack problems. The problem is
like making sure that we're integrating everything and then building on that ... here's the whole stack of notes.
That all needs to be consolidated. When you're consolidating it, you're going to find a whole bunch of research
directions. Note them. After consolidating, work on them. After working on them, correct them ... it builds itself.
And that can be contextualized with the other stuff."

**Layer 1: the transcription, as the foundation.**
- Missing pages are transcribed from the included scans.
- Every page is read against the scans with a second witness: every doubt mark and logic-bearing word on the crop
  first, then every strip checked for ink not yet in the text.
- Readings are corrected where the ink decides. Corrections go to CHANGES.md, with scan, line and confidence.

**Layer 2: the whole stack of notes consolidated into one reflection of the transcription.**
- The folder's Pro notes and doubts, with the topic's concordance of related notes beside them, are merged unit by
  unit:
  - each note once, with its anchor on the ink;
  - its mathematics stated;
  - duplicates merged;
  - contradictions between notes resolved or marked.
- Each of his claims gets a place and a first status.
- **The research directions found while consolidating are noted as they come up,** each with where it comes from.

**Layer 3: the mathematics, on that basis.**
- The noted directions and his own open questions are worked on: claims decided, computations redone, his conjectures
  attacked.
- The push rule and the dated ledger apply, so the run keeps going while rows move and delivers when two reviews show
  no movement.
- If something big resolves, it is recorded with its full proof.

**Then the correction loop: the work corrects the layers below it.**
- What layer 3 found goes back into layer 2 (notes corrected, statuses updated) and into layer 1. A misreading that
  the mathematics exposed is checked on the crop, and the ink decides.
- Then the groundwork (C1) is written beside his words, never mixed with them.

**Last, relating it to the rest.** The results zip is opened. The run says which of our results bear on this folder and
how: the same objects, the same statement, a consequence. It relates them without forcing links.

**Outputs:** the corrected page TeX and CHANGES.md; the consolidated notes (NOTES_CONSOLIDATED.md and
NOTES_VERDICTS.tsv); CLAIMS_STATUS.tsv; RESEARCH_DIRECTIONS.md (where each came from, what was done, the state reached);
GROUNDWORK.md; FOR_EXPERTS.md; CONSEQUENCES.tsv; CHECK_EVENTS.tsv; scripts/. Checkpoints come hourly and hold the
deliverables and documentation only.

## 4. The two pilots

| | Pilot 1: Book I, cote 22 | Pilot 2: Book IV, cote 81 |
|---|---|---|
| Folder | 29 pages, complete: Cohen constructions, formal simplicity, differential kernels | folded maps, 52 of 54 pages; the 2 missing scans transcribed first, in the same run |
| First pass | Pro (package MPL_22+23_002-016; the cote-22 pages only) | Codex Work (J81-01 to J81-07); no Pro notes |
| Pro's notes | the cote-22 part of MPL_22+23_002-016_notes.md (104 KB for the package) | none |
| Scans | its pages, whole and in thirds, as in the transcription packages | the same |
| Hua's text | as a witness, if he has cote 22 | as a witness, if he has cote 81 |
| Context | EGA V in full (cotes 24-25, our API transcription, TeX); EGA 0_IV §§19-22 and the related EGA IV sections from our French edition (TeX); the transcribed parts of cotes 21, 23 and 26 | the *Esquisse* (cote 119, our transcription); the transcribed Book IV neighbours (75; the done parts of 72, 83, 84); the pages of his published work on maps that exist in our corpus |
| Results zip, opened last | RESULTS_STATE and the registers | the same |

**Where they run:** account 4 at 2 Pro runs at a time, or accounts 1-3. Each pilot is one prompt, and a run of several
hours is expected.

## 5. How a pilot is judged, before scaling

By Claude Opus 5.5 at effort max: a7d5d89d, who wrote the method, or the main session.
1. Every correction it proposes, checked on the scan.
2. Ten claim statuses, worked through again.
3. Ten note verdicts, worked through again.
4. One unit's groundwork, read as the expert reader would read it.
5. Its time and checkpoints, and whether every output follows the format.

**Verdict:** scale, adjust the prompt, or stop.

## 6. Scaling

- One package per complete folder: 68 now, and 87 once the 19 near-complete cotes have their few missing pages.
- Topic by topic, with the topics the vertical work never touched first.
- The merged outputs of a topic's finished folders join the context of its next folders, as "earlier folders of this
  topic, worked through". That is a rolling context, kept within the topic.

## 7. Building

- The main session writes PROMPT.md and a builder script that assembles each package from these rules (scans, pages,
  notes, witness, the context zip and the results zip, each zip part under 10 MB).
- The prompt passes `--lint-math`: the push paragraph, the dated ledger, the checkpoints and CHECK_EVENTS.
- Stage A has its own prompt (topic dossiers), which passes `--lint`.
- Nothing is sent before the user has seen the prompt and the two package listings.
