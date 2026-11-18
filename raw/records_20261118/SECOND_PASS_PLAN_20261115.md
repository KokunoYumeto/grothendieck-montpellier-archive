# Second passes of the Montpellier transcriptions: what is left, how, in what order (15 Nov 2026)

Written by the main session (Claude Opus 5.5 at effort max) at the user's word (15 Nov ~10:1x UTC, P5281-P5285):
plan where the next second passes go and how much of the returned material still needs one; send the Codex-web returns
over Pro for a second pass plus notes; second passes in large chunks; what nobody has seen comes first; Hua's text is a
second witness wherever it exists.

## 1. What has come back (first passes)

| Source | Model | Packages or folders | Pages | Error rate in our checks |
|---|---|---:|---:|---|
| Pro packages | GPT-6 Astra (ChatGPT Pro mode) | 35 | 1,952 | ~0.8 per 100 words (median of the 14 sample checks); 1.9 on the pilot |
| Codex web | GPT-6 Astra at reasoning effort max | 124 | 962 | 0.18 (batch H) and 0.21 (batch J) per 100 words |

The Codex-web first passes are about four times cleaner than Pro's, but their notes were written without the context
packets (RESULTS_STATE, same-cote notes, the section's context sources) that the Pro packages carry.

## 2. Second passes done

- Claude Opus 5.5 at effort max (second_pass/out/): the Longue Marche core, six packages, 390 pages (142, 147_003-137, 149).
- Nothing else. Built and not sent: the two-witness Pro set S001-S029 (second_pass_pro_20261114/, 14 Nov, a302cb2d):
  1,679 scans, one package per returned Pro package (25-96 scans each); 23 full, 6 light (the LM core: Hua-format files and
  a collation list, since our text was already checked).

## 3. What still needs a second pass

| Material | Pages | Method |
|---|---:|---|
| Pro first passes in the two-witness set, full | 1,289 | two witnesses: ours (O) and Hua's (H), against the scans |
| Pro first passes returned since (P001-P005, package 48) | 273 | the same, with H where Hua has text |
| LM core, light | 390 | Hua-format files and collation list only |
| Codex-web returns | 962 | second pass plus notes: the Codex text (C), H where it exists, the cote's context packet |
| **Total** | **2,914** | |

## 4. Method: Pro does the grinding

1. **Two-witness second pass** (template second_pass_pro_20261114/SECOND_PASS_TWO_WITNESSES_TEMPLATE.md): consolidated
   diplomatic text in our conventions, a changes log per page, the same text in Hua's macros for a pull request to their
   project, a collation list. Both witnesses are drafts checked against the ink.
2. **Second pass plus notes for the Codex-web returns** (the user's idea, adopted): Pro checks the Codex text against the
   ink with Hua's text as a second witness, and writes the research notes a first-pass package writes (the notes part of
   ARCHIVE_PROMPT_TEMPLATE.md, with the cote's context packet). This makes the Codex-web returns equal to the Pro returns,
   at the cost of a check rather than a transcription.
3. **Claude** only where a Pro second pass cannot settle a reading (flagged in its changes log), and for spot checks.

## 5. Size: large chunks

At least 90 scans per package, never smaller than the transcription packages (the user, 15 Nov); about 90-135, whole
first-pass packages and cotes kept together; the light LM-core packages may be larger. Expected: about 14 full
two-witness packages, 3 light ones and 8-10 Codex-web ones, so about 25 Pro prompts.

## 6. Order and pace

- **Transcription comes first.** Of the about nine Pro slots (three accounts since 15 Nov): three maths prompts, five
  transcription packages, one second pass at a time (the user, 15 Nov).
- **What nobody has seen comes first** (the user, 15 Nov): cotes with no edition, translation or typesetting by anyone
  (Hua's raw AI pass does not count) before cotes whose editions have been public for years (Pursuing Stacks 134-x, Les
  Dérivateurs 157-160, the Esquisse, published letters). Within each group, the mathematically richest first, and the
  Longue Marche neighbourhood (141-152, the cotes our editions and experts lean on) early in the first group.
- **Pro first passes before Codex-web ones**, alternating once both are built: the second pass adds most where the
  first pass is weakest (about 0.8 errors per 100 words against 0.2); for the Codex-web returns the gain is mostly the
  notes.
- **The LM core light packages last**: their text is already checked; they serve the pull request to Hua's project.

## 7. Building

a302cb2d (Claude Opus 5.5, launched at effort high), which built the two-witness set, re-cuts it into large chunks, adds
P001-P005 and 48, builds the Codex-web second-pass-plus-notes template and packages, and numbers all of them in the send
order above. The old S001-S029 folders stay in a superseded folder. Every prompt passes `push_rule_pro_prompts.py --lint`.
