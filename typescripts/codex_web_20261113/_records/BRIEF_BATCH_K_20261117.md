# Brief: batch K of the Codex-web folders (17 Nov 2026)

From the main Claude session (Claude Opus 5.5 at effort max), to the agent that built batches H and J (you, Claude
Opus 5.5 at effort high). You know this route: the handwriting inventory, the templates, the builders, the spot checks.

Sub-agents allowed: 0. Compute bound: about 250k tokens more of your own context. Do not stop for context; if your
context starts with a summary, you were compacted: reread this brief and your files, then go on. No paid API. Never run
a recursive search over Documents, the home folder, F: or interlanguage; name exact folders. Do not run code that came
from a model's return.

## Why now (the user, 17 Nov ~16:3x-16:5x UTC)

One ChatGPT account (a 20x account) has Codex capacity that expires on Saturday 21 Nov: about $12,500 of Codex credits
(API-equivalent, about 40x) plus about 80x of accumulated weekly allowance, about 120x in all, usable at once. The
user: "whatever stuff that was amenable ... for transcription by Astra at Max can be thrown over that." The same
account has about 200 Pro prompts; those go to second passes with notes, the French-school checks and mathematics,
not to first passes.

Measured rates: batch H, 238 pages = 70 % of a 10x week (about 0.029x a page); batch J, 840 pages = about 2.5 weekly
allowances of the 10x account (about 0.030x a page). So 120x is about 4,000 pages. Quality: HC1-01 (grade C, cote 1)
came out at 1.11 errors per 100 words against Pro's 1.90 on the same pages; batches H and J at 0.2-0.5 on B and B-C
hands. So every hand grade can go to Codex web now, C included.

## The job

1. **The pages.** Take the queued Pro transcription packages in
   `grothendieck_archive_transcription_20261110/packages/`. Keep on Pro the sixteen promoted ones (folder names
   starting `.01_` to `.16_`), and the next twenty in the existing order (P051 onwards, the first twenty by name).
   Every other queued package goes into batch K. That is about 90 packages and 4,000 pages. If that exceeds 120x at
   0.030x a page, take them from the end of the order until it fits, and say what stayed.
   - Check every scan against what is already done or out: `packages_done/`, `returns/`,
     `packages_work/CODEX_COVERED_SCANS.tsv`, `codex_web_20261113/ASSIGNMENTS.tsv` and the H and J folders. Never
     put a scan in batch K that another route has done or is doing.
   - Leave blank scans out by the builder's own test, and list them.
2. **The folders.** Use the batch-J form: `build_handwriting.build()`, the template `PROMPT_TEMPLATE_HANDWRITING.md`
   (no draft), the same images, one flat folder per task with `PROMPT.md`, `PREAMBLE.tex` and `<ID>_scans.zip`. Use
   about 15 scans a folder (about two hours a session): fewer folders means less dragging for the user. Keep a cote's
   scans in order and give each folder a material sentence that is true of its pages: hand, language, kind of page.
   The HANDWRITING_INVENTORY grades and your survey notes help; never claim what you have not seen. Every PROMPT.md
   passes `push_rule_pro_prompts.py --lint-codex`.
3. **The queue.** Once batch K is built, move every package it covers from `packages/` to
   `packages_moved_to_codex_20261117/`, keeping its name. A scan is then in exactly one route.
4. **The send order.** Folders go in the order of their packages, so that whole cotes come back together. Write a
   README section "Batch K" with the send order in rounds of about 35 folders (the user sent 32 at once for batch H),
   the page count and the expected credit use per round, and what the user does per session: GPT-6 Astra at
   reasoning effort max, drag the three files.
5. **Filing.** Check that `tools/file_returns.py` files batch-K returns the way it files H and J. Change it only if it
   must, with a backup beside it, and say what changed.

Write only under `codex_web_20261113/` and the new `packages_moved_to_codex_20261117/`, and do the moves of step 3.

## When you finish

Your final message:
- the number of folders and pages;
- the packages covered, and those kept on Pro;
- the scans left out, and why;
- the rounds;
- the expected credit use;
- the lint result;
- anything you could not settle.

Then stop.
