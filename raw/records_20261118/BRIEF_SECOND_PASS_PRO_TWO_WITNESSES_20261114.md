> **Correction, 15 Nov 2026 (the user):** Michel Hua's text is used only as a witness, never as the basis of a transcription, and nothing goes to his project (no pull requests, no files in his macro set). The 80 pages once routed "Hua + check" had already been transcribed from the scans over the API (Claude Opus 5.5 at effort high, 12-13 Nov). The second-pass set is now SP01-SP20 (second_pass_pro_20261114/PACKAGES_20261115.tsv).

# Brief: Pro second passes with two witnesses (ours and Hua's), 14 Nov 2026 ~20:1x UTC

For a302cb2d (Claude Opus 5.5 at effort high), from the main session (Claude Opus 5.5 at effort max), at the user's word
(P5168: "push a lot over fucking pro wherever we can ... consolidating our two workplaces. That needs to be pushed over
pro as well, more than anything"; the user's plan for Hua, P5164-P5167: where their text is good we take it as our
first-pass basis; where it needs a second pass we send ours as pull requests typeset to their standard; where it falls
short we do it). The Claude allowance must last until Tuesday; GPT-6 Astra in ChatGPT Pro mode is the resource to use.

**The job.** Build, for every returned archive package where both we and Hua have text, a ChatGPT Pro prompt package
(GPT-6 Astra, Pro mode) for a second pass with two witnesses. The run gets the scans, our first pass and Hua's first
pass for the same pages. It delivers:
1. the consolidated diplomatic transcription in our conventions;
2. a changes log per page: our reading, Hua's reading, the final reading, what the scan shows, confidence (the form of
   our Claude second passes, `second_pass/out/*/*_changes.md`);
3. the same text in Hua's macro set, ready for a pull request to Commutator-IO/grothendieck-project (their preamble
   and conventions go in the package; their page n is our scan n + 1);
4. a collation list: folder, their page, our scan, line, their reading, ours, what the scan shows;
5. checkpoint zips per the standing checkpoint rule (as in `ARCHIVE_PROMPT_TEMPLATE.md`).

**How.** Write one template `second_pass_pro_20261114/SECOND_PASS_TWO_WITNESSES_TEMPLATE.md`, based on
`ARCHIVE_PROMPT_TEMPLATE.md` (look at every image, whole page then halves; diplomatic marks; no OCR; nothing left out;
checkpoints) and on the task of the Claude second passes (`second_pass/prompts/` as the model). Both witnesses are
drafts to be checked against the ink, never authorities; where they agree the reading still has to be seen. Then a
builder script that makes one flat upload folder per package (at most 20 files; work files in a `_work` folder):
`PROMPT.md`, the scans zip, a witnesses zip (our first-pass files from `returns/<package>_unzipped/`, Hua's transcript
batches for the same pages from `ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts/` at
commit aef7db2, a page map, their preamble and macro conventions), and a README with provenance (Hua's text is
AI-produced and free to use; credit his project and commit). Every PROMPT.md must pass
`python -I -B C:/Users/user/Documents/claude_tools/push_rule_pro_prompts.py --lint <PROMPT.md>`.

**Order** (send order = folder order, prefix S001_, S002_, ...): the densest hands first, where Hua's text is weakest
and ours is a first pass: 144, 146, 148, 150, 151, 141/143, 145, then 120/121/152/153/155, 1, 5-9, 16/44/47/54, 100;
use your sample figures to refine. 142, 147 and 149 already have checked second passes: for those, only items 3 and 4
(their format and the collation list), which may be a lighter prompt or a script; say which.

**Report** with the template's outline, the packages built (pages, sizes), the send order, and which one is ready to
send first.

Sub-agents allowed: 0.

Compute bound: about 150k tokens more; build the template and the first packages before the rest; report once, when the
template and the packages are built.

Rules: no recursive search over big trees (Documents, F:, home, interlanguage): name the folder each time. Never print a
key or token. Name every model with its effort. Write only inside `grothendieck_archive_transcription_20261110/second_pass_pro_20261114/`.
