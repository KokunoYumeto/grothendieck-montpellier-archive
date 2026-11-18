# The Codex-web transcription method: audit and plan for batch K (17 Nov 2026)

Main session, Claude Opus 5.5 at effort max, at the user's word (P6321-P6322: "a full audit of the methodology ... how
can we improve that? Does it need to be improved? If so, where?"; "these transcriptions now don't carry mathematical
commentary. There's not necessarily a reason they shouldn't ... a lighter pass of mathematical considerations ... can
be piloted"). Read for this: `tools/PROMPT_TEMPLATE_HANDWRITING.md` (in full), this folder's README and COST_NOTES,
and the verdicts of GRADE_HC1-01, SPOT_CHECK_H, SPOT_CHECK_J and SPOT_CHECK_156-7. I also compared it with the Pro
package prompt, and with what the Claude second passes of 13-17 Nov found.

## 1. What the method is, and what it has shown

- GPT-6 Astra at reasoning effort max, in Codex web. One session per folder. Each scan comes as the whole page plus
  three overlapping thirds at full resolution.
- One stream with a notation table, built from the image. Then a full second reading from fresh crops, a per-element
  inventory, a per-page audit, a frozen hash set, and a zip offered as a download.
- No OCR. No compiling in the sandbox. No checkpoint ZIPs (the user, 14 Nov): the page files are the checkpoint.
- **Quality, measured:**
  - HC1-01, grade C (cote 1, dense hand): 1.11 errors per 100 words against Pro's 1.90 on the same pages. Unmarked
    errors: 0.72 against 1.25.
  - Batches H and J (B and B-C hands): about 0.2-0.5 errors per 100 words, below 12 of Pro's 14 checks.
  - It marks doubt freely: about 14 marks per 100 words. That leaves more open places for the second pass, but fewer
    silent errors.
- **Cost, measured:** about 0.03x of a weekly allowance a page (H: 238 pages = 7x; J: 840 pages = about 25x). Wall
  time was about 70 minutes for folders of about 7.5 handwritten pages, of which the second reading is most.

**Verdict: the reading method is sound and better than Pro's on raw accuracy. Do not change how it reads.** The gaps
are elsewhere.

## 2. The gaps, and what to change

| # | Gap | Change | Cost |
|---|---|---|---|
| G1 | **No mathematical commentary.** The notes ask only for steps marked unverified, and for titles, dates and page counts. The Pro packages give research notes (1,387 claims and 56 research items so far), and the companions use them. | A new deliverable, `{ID}_mathnotes.md`, written **after the transcription is frozen**, so it cannot change a reading. Light: what the pages do (one short paragraph per mathematical unit); his statements left without proof; his questions and conjectures; his slips, with the corrected form; where he points to his other texts, cotes or people; the model's own remarks, each labelled with its confidence. No proofs, no literature search, no long derivations. | The time after the freeze, measured in progress.log. Expected +10-25 %. |
| G2 | **Error guards are missing the newest finds.** Today's second passes found errors the template does not name. | Add to "Where readings go wrong": a script capital read as a Greek one (his script T read as Gamma, cotes 143 and 148); a plausible antonym or neighbour in place of the ink ("minimaux" for "maximaux", "loc" for "lac", "cohérente" for "évidente"); a struck word kept as live text (already there; keep). | None. |
| G3 | **A cote cut into several folders** gets several notation tables, which may disagree. | One sentence in each folder: which folders of the same cote come before and after it, and that the notation table is reconciled across them afterwards, so every entry must say where on the page it was seen. The folders stay independent, so they still run in parallel. | None. |
| G4 | The **page-number rule** for the archive's pencil foliation. | Already right in this template: `% archive sheet number: NN`. No change. | - |
| G5 | **Hua's transcription** as a witness for unresolved places, as the Pro packages and the Claude second passes now use it. | Not in batch K. It adds time, and it carries a risk of copying in a first pass. The second pass (Claude or Pro) uses it later, as now. | - |
| G6 | **Folder size.** | The user, P6321: double, about 15-16 scans, about two hours (plus G1). | Fewer sessions to start. |

## 3. The pilot (round 1), and how it is judged

- Round 1, about 35 folders, all with G1-G3.
- **Two control folders**, beyond the 35, of about 15 pages each. Their pages already have a Pro first pass with
  notes and a Claude second pass of 17 Nov (cote 148, scans 44-58; cote 145, scans 20-34), so the corrected text is
  ground truth. They cost about 1x.
- **What is measured**, from the returns:
  - the reading's errors per 100 words on the controls, against the corrected text, and against Pro's first pass on
    the same pages;
  - the notes' overhead: the minutes after the freeze, per page, from progress.log, and the credit drop per round;
  - the notes' value against Pro's notes on the control pages: claims caught, slips caught, false claims. The Claude
    agents that did the 145 and 148 second passes know those pages and can judge this.
- **The decision after round 1:**
  - keep G1 for all rounds if the notes are useful and the overhead is under about 25 %;
  - otherwise drop G1 and give those cotes their notes in the Pro second pass (SECOND_PASS_CODEX_NOTES template).
  - If the reading on the controls is clearly worse than Pro's, stop batch K, and the compute goes to the user's
    second list (EGA translations, grunt work, OLP, Gauss).

## 4. The budget and the order (the user, P6323)

- About 120x of Codex capacity until Friday evening (the subscription renews Saturday 21 Nov). At 0.030-0.037x a
  page, that is about 3,300-4,000 pages.
- **First:** the Montpellier archive, as much of it as the credits allow.
- **Only if Astra at max proves not capable, or credits remain:** EGA translations into the other languages, the grunt
  work, the Open Logic finishing, and Gauss (chunked for Codex web).
- About 200 Pro prompts on the same account, at 2 at a time: about 35-50 runs fit. They go to:
  - the French-school checks;
  - the Pro second passes with notes of the Codex-web returns (folder 4);
  - the top of folder 5;
  - mathematics at night.
