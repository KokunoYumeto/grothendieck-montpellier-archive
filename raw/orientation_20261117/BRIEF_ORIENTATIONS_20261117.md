# Brief: curated orientations for the waiting transcription packages (17 Nov 2026)

From: the main session (Claude Opus 5.5 at effort max). For: four agents, Claude Opus 5.5 at effort max, one batch
each.

## Why

141 transcription packages of Grothendieck's Montpellier archive wait to be sent to GPT-6 Astra (ChatGPT Pro mode).
Each run transcribes its scans. Then, after the transcription is frozen, it writes research notes on the mathematics:
141 mathematical analyses. The user, 17 Nov: making their context good "is probably a very outsized impact", and a run
comments on what its background shows it, so the background should be broad and well organized.

Each package already carries a results block of about 70,000 characters, which is broad but long:
- the headline results and a programme map;
- the open items and settled rows of our runs that match its subjects;
- other packages' notes on its cotes;
- Michel Hua's findings and his project's modernised reading of its cotes.

Your job is the short curated layer that goes at the top: what in all that matters for THESE pages, and what the
notes should look for.

## Your batch

Read `orientation_20261117/digests/BATCHES.tsv`: column 1 is the batch number, column 2 the plan folder. Your batch
number is in your launch message. Every folder of your batch has a digest, `orientation_20261117/digests/<plan folder>.md`.
All paths are under `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\`.

Read first, once: `notes_headlines/PROGRAMME_MAP.md`, the whole programme in one page plus every run's open rows.
Then the digests of your batch.

## What to write for each package (at most 2,500 characters, English, plain declarative sentences)

```
## Orientation for this package (curated 17 Nov 2026 by Claude Opus 5.5 at effort max from our records; leads, unrefereed)

- **What these pages are:** ... (from the titles and the place in the plan; one or two sentences)
- **Where they sit:** the work or line they belong to (La Longue Marche / the tower; Les Dérivateurs and homotopy;
  crystals; motives and Galois groups; tensor categories; SGA/EGA; analysis; ...), and the neighbouring cotes.
- **Our open questions they may bear on:** 2-6 items. Each one: the run and id exactly as in the digest or the
  programme map (for example **EXIT_TOWER E.24**, **DELTA_ON_GT A.24**), and one line on why.
- **Our results to use and check:** 0-4 items, by run and id, one line each.
- **What other packages' notes say about these cotes:** 0-4 items, by package and entry.
- **Michel Hua's project (credit it to his project whenever you use it):** what his modernised reading says these pages
  are about (its stations and strands), what it marks as not established, and his findings by id. Paraphrase in one or
  two lines each; do not copy his text.
- **What the notes should look for:** 3-5 concrete things. A precise question to settle on these pages; a claim of
  ours or of Hua's to test against the ink; a link to another cote to check.
```

Rules:
- Use only what the digest and the programme map say. Do not invent ids, titles, results or links. Where a link is
  your own guess, say "possibly", and say why.
- Give exact ids as the digest has them. A package with no matching open item gets none. Then say what the pages may
  open up instead, from the titles and Hua's reading.
- Hua's project is credited every time ("Hua's project", "Hua, modernised reading of cote n", "Hua, findings register,
  id"). Our own notes need no such line.
- Name models with their effort where you name them.

## How to write (fewer tool calls)

Write the orientations in chunks of up to seven packages per file, into `orientation_20261117/raw/batch<k>_part<NN>.md`.
Separate the packages within a chunk by a line of the form

    === FILE: <plan folder>.md ===

followed by the orientation. The main session splits the chunks into `orientation_20261117/<plan folder>.md` by
script. Cover every package of your batch, in the order of BATCHES.tsv.

## Bounds

- Read only the programme map, your batch's digests, and, where a digest leaves a title unclear, the first 40 lines of
  the package's `packages/<P…>/PROMPT.md`.
- No Grep or Glob over Documents or any big tree. Name the exact files.
- No sub-agents.
- Do not stop for context. If your context starts with a summary, you were compacted: reread this brief and your
  chunks so far, then go on.
- When done, reply in at most five lines: packages covered, chunk files written, anything you could not do.
