# WTA_90_014-025: cote 90, scans 14-25, variant A, the companion-coded pass (units, keyed notes, status blocks, handbook items, suggested links) (ChatGPT Pro upload folder)

Upload every file of this folder except this README in a new ChatGPT chat with GPT-6 Astra in Pro mode, `PROMPT.md` as a file, no text typed. Range 2 of 2 of the folder: 12 pages; cut by script; 27 note entries; 48 images; expected 54 minutes (estimate, until the pilot measures it). Images: 16.7 MB.

Folder: « KG (X) : notes manuscrites (s.d.). » ([à partir de 1964][79]).

## Files

- `PROMPT.md` (0.03 MB)
- `WTA_90_014-025_context.zip` (0.02 MB)
- `WTA_90_014-025_notes.zip` (0.08 MB)
- `WTA_90_014-025_results.zip` (0.0 MB)
- `WTA_90_014-025_scans.zip` (16.7 MB)
- `WTA_90_014-025_witnesses.zip` (0.16 MB)

## Witnesses

- `first/MPL_90+91_002-018/`: witness O, the first pass by GPT-6 Astra (ChatGPT Pro mode), 16 Nov 2026, for 12 of the 12 pages, with its doubts table and the prompt it was made with (`first_pass_PROMPT.md`, which defines our macros); earlier checks found about 1 to 2.5 errors per 100 words on his dense hand, mostly fluent misreadings, dropped short conditions or symbols, wrong indices, signs and arrow directions, and missed deletions; only a third of them carried a doubt mark.
- `second/K90-02/`: witness W, a second reading by GPT-6.2 Astra at reasoning effort max (ChatGPT Work), 18 Nov 2026, for 12 of the 12 pages, with its doubts table and its audit; a second reading made blind, without the first pass in view; on the control folder CTRL-148 this reader made about 1.7 errors per 100 words against the Pro first pass's 3.3; its notes often call his slips what were misreadings.
- `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/grothendieck-project, commit `aef7db2`), an AI transcription whose batch headers name the Claude model of each pass (Claude Opus 5, Claude Opus 5.5) but no effort setting, in that project's own macros (`hua/transcripts/preamble/grothendieck.sty` says what each means: `\struck` a deletion, `\add` an insertion, `\marginal` a margin note, `\uncertain` a doubtful reading, `\ill` a word they could not read). Their page n is our scan n + 1. H has text for 6 of these 12 pages. Earlier checks found it at about 1.5 errors per 100 words on light pages and 3 to 8 on dense ones: plausible prose in place of the ink, struck text given as live, abbreviations expanded, margins left out, drawings described. A witness only, credited; this run writes nothing in their conventions.

## Context (the subject's own, chosen by rule: CONTEXT_RULES.tsv)

- `this_folder/cote_90.tex`: the whole folder as transcribed so far, each page in the reading a pass starts from, for the argument before and after this range
- `topics/SA02_TOPIC.md`: the catalogue of the topic (its folders, what is transcribed and how)

## Nodes

- 27 entries on these pages; 80 related entries in the concordance; 0 check-register rows.

## Results (opened last by the run)

- 0 statements of our runs whose `his_places` cite these pages.

## Provenance

- **Scans:** Université de Montpellier, fonds Grothendieck (grothendieck.umontpellier.fr); cotes and scan numbers are theirs; rendered from the archive PDFs as in the first-pass packages (largest image, autocontrast, unsharp mask, JPEG 88), whole and in three overlapping strips.
- **Built** 2026-11-19 01:22 UTC by `working_through_20261118/build_working_through.py` (Claude Opus 5.5 at effort max). Lint (--lint-math): pass.
