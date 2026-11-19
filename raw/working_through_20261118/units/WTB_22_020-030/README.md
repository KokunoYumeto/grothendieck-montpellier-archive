# WTB_22_020-030: cote 22, scans 20-30, variant B, the foundational check (the mathematics, the scan checks and the verdicts; no companion writing) (ChatGPT Pro upload folder)

Upload every file of this folder except this README in a new ChatGPT chat with GPT-6 Astra in Pro mode, `PROMPT.md` as a file, no text typed. Range 3 of 3 of the folder: 11 pages; cut by script; 36 note entries; 44 images; expected 51 minutes (estimate, until the pilot measures it). Images: 17.6 MB.

Folder: « [EGA IV]. [Chapitre] 0 IV. Cohen, différentielles, algèbres formellement simples (Compléments) : tirés à part (1963), tapuscrit annoté (s.d.), notes manuscrites (s.d.). » (1963-[vers 1967][20]).

## Files

- `PROMPT.md` (0.02 MB)
- `WTB_22_020-030_context.zip` (0.51 MB)
- `WTB_22_020-030_notes.zip` (0.09 MB)
- `WTB_22_020-030_results.zip` (0.0 MB)
- `WTB_22_020-030_scans_part1.zip` (8.35 MB)
- `WTB_22_020-030_scans_part2.zip` (8.46 MB)
- `WTB_22_020-030_scans_part3.zip` (0.8 MB)
- `WTB_22_020-030_witnesses.zip` (0.15 MB)

## Witnesses

- `first/MPL_22+23_002-016/`: witness O, the first pass by GPT-6 Astra (ChatGPT Pro mode), 16 Nov 2026, for 11 of the 11 pages, with its doubts table and the prompt it was made with (`first_pass_PROMPT.md`, which defines our macros); earlier checks found about 1 to 2.5 errors per 100 words on his dense hand, mostly fluent misreadings, dropped short conditions or symbols, wrong indices, signs and arrow directions, and missed deletions; only a third of them carried a doubt mark.
- `second/K22-02/`: witness W, a second reading by GPT-6.2 Astra at reasoning effort max (ChatGPT Work), 18 Nov 2026, for 11 of the 11 pages, with its doubts table and its audit; a second reading made blind, without the first pass in view; on the control folder CTRL-148 this reader made about 1.7 errors per 100 words against the Pro first pass's 3.3; its notes often call his slips what were misreadings.
- `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/grothendieck-project, commit `aef7db2`), an AI transcription whose batch headers name the Claude model of each pass (Claude Opus 5, Claude Opus 5.5) but no effort setting, in that project's own macros (`hua/transcripts/preamble/grothendieck.sty` says what each means: `\struck` a deletion, `\add` an insertion, `\marginal` a margin note, `\uncertain` a doubtful reading, `\ill` a word they could not read). Their page n is our scan n + 1. H has text for 8 of these 11 pages. Earlier checks found it at about 1.5 errors per 100 words on light pages and 3 to 8 on dense ones: plausible prose in place of the ink, struck text given as live, abbreviations expanded, margins left out, drawings described. A witness only, credited; this run writes nothing in their conventions.

## Context (the subject's own, chosen by rule: CONTEXT_RULES.tsv)

- `this_folder/cote_22.tex`: the whole folder as transcribed so far, each page in the reading a pass starts from, for the argument before and after this range
- `ega_fr/ega0-19-fr.tex`: EGA 0_IV §19, formally smooth algebras and Cohen rings (French, our edition)
- `ega_fr/ega0-19b-fr.tex`: EGA 0_IV §19, continued (French, our edition)
- `ega_fr/ega0-20-fr.tex`: EGA 0_IV §20, derivations and differentials (French, our edition)
- `ega_fr/ega0-21-fr.tex`: EGA 0_IV §21, differentials in rings of characteristic p (French, our edition)
- `ega_fr/ega0-22-fr.tex`: EGA 0_IV §22, differential criteria of smoothness and regularity (French, our edition)
- `ega_fr/ega0-23-fr.tex`: EGA 0_IV §23, Japanese rings (French, our edition)
- `ega_fr/ega4-16-fr.tex`: EGA IV §16, differential invariants; differentially smooth morphisms (French, our edition)
- `ega_fr/ega4-17-fr.tex`: EGA IV §17, smooth, unramified and étale morphisms (French, our edition)
- `ega_v/cote24_ega_v_english_typescript.tex`: EGA V, the English typescript in the archive (cote 24), transcribed by Claude Opus 5.5 over the API (not yet checked by eye)
- `ega_v/cote25_nouveau_ega_v_typescript.tex`: EGA V, the French typescript in the archive (cote 25), transcribed by Claude Opus 5.5 over the API (not yet checked by eye)
- `neighbours/cote_23.tex`: cote 23, EGA IV Compléments (his notes, letters of 1966 and 1968, a typescript), as transcribed so far
- `neighbours/cote_26.tex`: cote 26, EGA VI: plans, notations, open problems
- `neighbours/cote_21.tex`: cote 21, chapter 0_III, as transcribed so far
- `topics/SA23_TOPIC.md`: the catalogue of the topic (its folders, what is transcribed and how)

## Nodes

- 36 entries on these pages; 36 related entries in the concordance; 2 check-register rows.

## Results (opened last by the run)

- 0 statements of our runs whose `his_places` cite these pages.

## Provenance

- **Scans:** Université de Montpellier, fonds Grothendieck (grothendieck.umontpellier.fr); cotes and scan numbers are theirs; rendered from the archive PDFs as in the first-pass packages (largest image, autocontrast, unsharp mask, JPEG 88), whole and in three overlapping strips.
- **Built** 2026-11-18 16:17 UTC by `working_through_20261118/build_working_through.py` (Claude Opus 5.5 at effort max). Lint (--lint-math): pass.
