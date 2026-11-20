# Methodology

All text in this repository is AI-produced. Models are named with their effort setting. Revised 19 Nov 2026.

The doubt marks still open, by kind, and what each second-pass design did with them (20 Nov 2026, a working report
rebuilt as returns come in): [reports/doubt_marks_20261120/](reports/doubt_marks_20261120/).

**Compute.** Most of the reading runs on ChatGPT subscriptions (Pro and Work), where a long run costs no more than the
subscription. Claude does the coordination, the checks, the trackers and part of the second pass. We have no special
recognition technique: what we have is many long runs in parallel, plus the measurements below of what finds errors.

## 1. Scans

The university's PDFs, split into packages of about 45 scans (a cote, or neighbouring cotes). We cite the scan (the
PDF page); scan 1 of every PDF is the university's logo sheet.

## 2. First reading

- GPT-6 Astra (ChatGPT Pro mode): one package per conversation, with the scans and a context zip (our transcription of
  La Longue Marche, its research notes, the archive's section map, and the research notes of earlier packages of the
  same cote). The transcription is written first and frozen; only then are the research notes written with the
  context.
- GPT-6.2 Astra at reasoning effort max in ChatGPT Work: folders of 8 to 16 scans.
- GPT-6 Astra at reasoning effort max in Codex web: folders of 4 to 11 pages.
- Typed and printed pages: Claude Opus 5.5 at effort high through the Anthropic Message Batches API (1,361 pages for
  $93.38).
- Marks: `\unsure{a|b}` (a doubtful reading, with its alternatives), `\illegible{n}`, `\deleted{...}`,
  `\inserted{...}`, `\margin{...}`. The prompt as sent is in each package folder.

## 3. Second pass

Every second pass reads the scan against up to three witnesses:

- C, our first reading of the page;
- H, the transcription of the Commutator-IO grothendieck-project (Michel Hua; commit `aef7db2`), used only as a
  second witness, never as the basis of ours, and credited wherever it is used;
- S, the readings our sweeps decided on the scan (section 4).

The second passes so far:

- **Claude Opus 5.5 at effort max (13 Nov 2026).** One block of about 15-18 scans per agent. Every line was read
  against the scan halves and enlarged crops, and every change was logged with its evidence and a confidence.
- **GPT-6 Astra in ChatGPT Pro mode, one reader per piece (from 14 Nov 2026).** The reader reads the whole page, then
  each half line by line against C and H, and enlarges the places it must decide (about 6-7 crops a page in the
  returns of 19 Nov). It then takes a second look at every page. The text is hashed and frozen before the
  mathematical context is opened, so expectation cannot creep into the reading; the research notes come after.
- **Three independent readers and a main reader (from 19 Nov 2026).** Each reader works in its own context and
  follows a fixed order:
  - the page once, for the layout;
  - both halves once, against C and H;
  - a list of what is still open;
  - one tight crop per open place, enlarged deep (a few thousand pixels across) with the contrast raised where it
    helps, and a decided place is never cropped again.

  Each reader returns its reading of the page and every place where it differs from C or from H, with what the half
  or the crop showed. The main reader compares the three readings, looks at the crops only where they differ, and
  decides. The changes log lists all three readings at such a place, with the one the ink supports.

  In the first returns (SP34, SP35), Pro went further on its own. Each reader wrote a structured record: the visible
  strokes as evidence, the crop's coordinates, and a verdict on each of C's doubt marks. The main reader applied its
  decisions to the text with a script for each page. Where a place stayed open, it asked for further independent
  readings instead of cropping again. The prompts did not ask for these.

  From the pieces built on 19 Nov the readers are fresh for every page, with a new context each time. The main reader
  writes the readers' brief, improves it from their disagreements, and reports the workflow and every change to it in
  the piece's workflow file.
- **Doubt marks only (sent 19 Nov 2026).** One Pro run settles every doubt mark of a cote (cote 1: 142 pages, 2,684
  marks). It designs its own workflow and records it, with every change and its measured effect. It also lists the
  first readers' recurring misreadings, so that they can be checked across the archive by script. In its first 40
  minutes it changed its own method four ways:
  - a fresh reader for every page;
  - a page's marks split between two or three readers;
  - a stopping rule for struck-out text: where the strokes that would decide are gone, the doubt stays;
  - neighbouring marks read on one shared crop.
- **One main reader and Pro's three sub-agents, each on a different page (from 20 Nov 2026).** The three-reader design
  read about 2 pages an hour, so it was stopped. The main reader keeps the piece's notation table and hand log. Each of
  Pro's three sub-agents reads a different page, and another sub-agent reads that page a second time. The crops that
  decided a place come back with the return. The first returns read 13-27 pages an hour.
- **A blind second reading, and crops where they matter (from the evening of 20 Nov 2026).** The first returns of
  that design showed three weaknesses:
  - the second reading did nothing: one run logged 20 pages as read again in 10 minutes, with no change;
  - on pages first read in Codex web, it changed our reading at 1 of the 67 words where our reading and Hua's differ.
    On other pages it changed 23 of 232, and the three-reader design 26 of 217;
  - about 30 % of the doubt marks it settled were settled on the page view, without a crop.

  Claude Fable 5.2 at effort max proposed the changes, and the main session (Claude Opus 5.5 at effort max) checked
  them against the returns:
  - a sub-agent that has not read the page reads its hardest places again from the image alone, without either
    witness or the first reading. These are insertions, margin notes, struck passages, formulas with a doubt mark,
    numbers by pen, handwriting on typescripts, words where the witnesses differ and less-than-certain changes;
  - a script compares the two readings, and every difference is decided on a crop;
  - a word where the two witnesses differ, and a doubt mark that is resolved, always get a crop;
  - every strike and insertion of the first reading gets one question on the image.

  The sheet now names our reader's own confusions of Greek letters. The ones it named before were Hua's reader's.
- **What every run reads first: the reading aids in [`methodology/reading_aids/`](methodology/reading_aids/)** (from
  20 Nov 2026):
  - the sheet of the errors that recur in these papers, with measured rates and the letters each cote's readers confuse;
  - how a place is decided: on the ink first, then on his notation and the mathematics where the ink admits two
    readings, and nothing normalised;
  - the hand logs of earlier runs on the same cotes: his habits of hand, whether each holds elsewhere, and whether it
    predicts errors;
  - for each page, a list of where C and H differ, and the notation of earlier passes on the cote.

  Every run returns its own hand log and its feedback on the sheet. The aids are refreshed at every intake of returns,
  and the waiting runs on the same cotes get the new hand-log rows.
- **Implementation runs (from 20 Nov 2026).** Pro runs that put the decided corrections into the pages. Each row is
  decided on the scan as one of:
  - (a) our misreading, changed;
  - (b) his slip or refinement, kept as written, with a note;
  - (c) already done;
  - (d) not on the page.

  A run returns the edited pages and the exact find and replace of each change. The text of record applies it where the
  span stands once on the page. The first three runs (245 rows) changed 38 places and confirmed 106 of his slips as
  written. They found 89 rows not on the page, for two reasons:
  - notes on the dossiers' catalogue, such as whose leaf a sheet is or where a typescript belongs;
  - 11 rows our builder had put on the wrong cote.

  Both kinds have since been left out of the pieces.

Second-pass pieces are 7 to 30 pages long, implementation pieces about 400 rows; every run checkpoints every 45 minutes.

## 4. Sweeps

A sweep reads the notes beside the transcriptions across many packages at once: Pro's research notes and doubts, and
the mathematical notes of Work and Codex web. Where a note says Grothendieck's text is wrong, sweep 1 only flagged the
place; sweeps 2 and 3 checked it on the scan and decided between three outcomes:

- his slip: kept as he wrote it, with a note;
- our misreading: corrected;
- a refinement of his statement: mathematics, not transcription.

About a third of such places turned out to be our misreading (sweep 3: 195 of 538).

## 5. What finds the errors (measured 19 Nov 2026)

- **Where the corrections came from.** On the pages whose Pro second passes have returned, the second pass ruled on
  10,845 places in C: 3,562 confirmed and 5,759 corrected. Of the 5,759 corrections:
  - 2,605 (45 %) were at a doubt mark of the first reading;
  - 2,262 (39 %) were where H reads differently from C;
  - 892 (15 %) were found only by the full correcting pass.

  So the cheap lists point at about 85 % of what a full pass corrects: the doubt marks, the differences between two
  independent readings, and the places the notes call his errors. They are settled first, and every page still gets
  its full pass for the rest.
- **A check of the disagreements only.** Claude Opus 5.5 at effort high checked only the places where C and H
  disagree, on 8 pages (pilot F). Its decisions agreed with Pro's at 136 of 162 places (84 %), and it found 4 of the
  10 places where Pro corrected C.
- **Pace of the Pro second passes.** One reader: 10-15 pages an hour, including the second look and the research
  notes. Three readers: 5-7 pages an hour.

## 6. What image agents cost (pilots of 19 Nov 2026)

The pilots read cote 156-7, scans 2-6, with Claude Opus 5.5:

- A: a lead at effort max with three readers at effort high;
- B: one reader at effort max;
- C: two readers at effort max who debate;
- D: two readers at effort high who debate;
- E: two readers at effort high, each capped at 200,000 tokens and 10 crops a page, on one page;
- F: a check of the disagreements only (section 5).

What they showed:

- Readers left free to crop viewed 30 to 110 images and made 45 to 135 tool calls a page. The 13 Nov blocks had used
  3 to 5 of each.
- An image stays in an agent's context, and every later step reads the whole context again, so the cost of a reader
  grows with the square of the images it holds.
- At effort max a page cost about three times as much as at effort high.

The rules since then:

- one agent on one page first, with its cost measured, before any fan-out;
- every brief states the economy of crops and calls;
- fresh contexts for each page;
- one tight crop per open place;
- no prompt written for one model handed unchanged to another.

## 7. The text of record and the counts

- **Text of record.** For each page, the best reading we have, ranked: Pro second pass, Claude second pass, Pro first
  reading, Codex web, Work, API. The corrections already decided on the scan are applied to it by script, and each
  one is logged. La Longue Marche is not included: its edition is its text.
- **Counts.** Every count of the work (pages, passes, open doubt marks, the fix lists) is generated from the files by
  script after every return. None is typed by hand.

## 8. API runs

Every API run goes through the providers' batch interfaces, at batch prices: the Anthropic Message Batches API, or
OpenAI's Batch or Flex. Never the standard endpoints.

## 9. Ways to catch errors, cheapest first

| # | Way | What it reaches (measured so far) | Cost |
|---|---|---|---|
| 1 | Put the readings already decided on the scan into the text of record | the sweeps' decided misreadings | script |
| 2 | List the places where the notes say his text is wrong | about a third are our misreading | script |
| 3 | Sort the sweeps' free-text rows | more decided readings to put in | text-only model pass |
| 4 | Give the second-pass readers these lists as the places to check first | the 85 % of section 5 | script edit of the prompts |
| 5 | Settle the doubt marks, one tight crop each | 45 % of what second passes corrected | Pro run (doubt marks only) |
| 6 | Check only where two independent readings differ | 39 %; pilot F agreed with Pro at 84 % of places | Claude agent, or a batch |
| 7 | Check the listed places through a batch API, each image read once | not measured yet: Claude Opus 5.5 at effort high against GPT-6.2 at reasoning effort max and high, scored against Pro | batch API |
| 8 | Pro's three-reader correcting pass, fresh readers per page | everything, including the 15 % that no list points at | Pro run-hours |
| 9 | A Work correcting pass, or a fresh Work reading and a diff | not measured yet | Work time |
| 10 | Claude agents reading whole pages | measured: too costly for volume | subscription quota |

## 10. Where AI readers go wrong, and what catches each

A model that reports a task as done has made an attempt at it. We check the claim against the files.

The errors we have caught so far, with what catches each:

- **Plausible text in place of hard ink**, often with no doubt mark. On cote 149, scan 040, our checked second pass had
  « au moins » where the page has « maintenant » (H had it right). Caught by a diff against an independent reading,
  and by the full pass. A check of the doubt marks alone misses it.
- **The common word for the written one.** GPT-6.2 Astra at reasoning effort max, on a control set from cote 148, gave
  « indique » for « implique » and « fermée » for « formée ». It was still the most accurate first reader we measured
  there: 1.69 errors per 100 words, against 3.26 for the Pro first pass. Caught by the same diff. The prompts now
  carry examples of such neighbouring words.
- **Struck text given as live.** On cote 147, scan 063, five struck hats were read as live in both our reading and H.
  Caught by reading the deletions as their own layer in the second pass.
- **Ink corrections on typescripts missed.** Caught by checking the ink layer of every typed page against the scan.
- **Slanted margin notes in fragments.** Caught by a rotated crop.
- **On faint pencil, words that are not on the page.** Caught by a diff, and by asking for the visible strokes as the
  evidence of every reading.
- **Counts and claims in a model's report that the files do not bear out.** Caught by generating every count from the
  files.

## 11. Coordination

Coordination, packaging, the trackers and these files: Claude Opus 5.5 at effort max in Claude Code.
