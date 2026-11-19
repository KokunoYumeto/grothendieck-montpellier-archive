# Building the sweep-3 research prompts: shared brief

From agent a28ea31fa17dd65e1 (Claude Opus 5.5 at effort max), 19 Nov 2026, at the main session's word. The user asked
why no prompts had come out of the sweeps yet, and wants Pro work on the neglected topics now. Account 4 has about 48
hours of Pro left.

Your message names your topic SA<nn>. You write one research prompt for that topic, for GPT-6 Astra (ChatGPT Pro mode).
If you are compacted, the summary is a lead, not the record: reread this file and your own output, then go on.

## What the prompt covers

**One prompt per topic, bundling one cluster of related questions.** Its parts are:
- every research package in `results_register/horizontal/sweep3/SA<nn>/RESEARCH_PACKAGES.md`;
- the sharpest hunches in `HUNCHES.md` and in `readings/*.md` (merged files, not the `_part` files);
- his open steps, with the strongest reduction on the page;
- the new claims of sweep 3 to push further.

The main session's examples:
- 8.5.7 (cote 4) is now proved: its consequences and the sharper statement, toward his question 8.6;
- the Deuring element xi_p, which 15:54-56 set up and never determine;
- Honda-Tate in weight > 1 (15:100-106);
- his Theorem on 100:3 over non-reduced bases;
- 9:14, the supersingular case.

Every part is a question to settle: proved or refuted, with complete proofs. Write questions, not topics.

## Background (attached files)

1. The topic's sweep-3 files: STUDY, HUNCHES, RESEARCH_PACKAGES, the merged readings, CHECK_EVENTS, CORRECTIONS.
2. `sweep2/SA<nn>/WHAT_IS_WHERE.md`.
3. The Pro transcription `.tex` of his pages that the parts rest on, and the notes files of those packages:
   `grothendieck_archive_transcription_20261110/returns/<pkg>_unzipped/`.
4. A broad layer: related pages of the other three topics of the cluster (motives and crystals: SA05, SA06, SA07,
   SA15), so that the run sees the connections.
5. Literature as LaTeX source wherever we have it, never a PDF when the TeX exists:
   - the user's library index is `knowledge/03_archive/user_literature_library.md`;
   - for example `arxiv_latex/_expanded_by_topic/perfectoid_padic_bundle` holds Bhatt-Scholze, Bhatt-Lurie and the
     prismatic papers;
   - arXiv sources come from `https://arxiv.org/e-print/<id>`;
   - also `sweep3/LITERATURE_CHECK.tsv` once it exists.
6. Michel Hua's modernised readings, if you use any of their remarks
   (`ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts/<cote>/<cote>.modern.tex`). They
   are credited to "Michel Hua's project", and are a witness only.

**Packing.**
- Pack the background into one or a few ZIPs: LaTeX and text only.
- Put a `MANIFEST.tsv` at the root of each ZIP, giving every file with its origin and SHA256.
- No credentials, no private administration, nothing about accounts or costs.

## The text of the prompt

**Model.** `TO_SEND/PRO/05_FINMON_CP2_night/PROMPT.md` is a night research prompt that passes the lint. Follow its
structure:
- title;
- "To be settled";
- "For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA<nn>`";
- who drafted it: you, by model, effort and agent id, on 19 Nov 2026, at the main session's word;
- What is attached;
- Where this comes from: Grothendieck's pages in the Montpellier archive, our AI-produced transcriptions, and the
  sweeps by Claude Opus 5.5 at effort max;
- Results this prompt builds on, each with its status and check events;
- Leads;
- What the outcome must be;
- Parts;
- Rules of proof;
- Check events;
- What to deliver;
- If the execution environment fails;
- Typesetting check;
- Checkpoints.

**Generic paragraphs.** Copy these verbatim from the model, changing only the file prefix:
- the push paragraph;
- the progress check at three hours, with its ledger, "Movement means only" and "two consecutive reviews";
- "When the work is finished";
- the check-events paragraph;
- the failure and checkpoint paragraphs.

The canonical checkpoint and failure text is in `claude_tools/prompts/checkpoint_rule.py` (`clause(name)`, `FAILURE`).

**Rules for the text:**
- Ask for the whole task. Write no minimums ("at least N") and no cheaper alternatives ("or reduce it to", "failing
  that", "if time permits", "where possible", "as far as possible", "optional").
- The only outcomes that finish an item are proved or refuted. There is no "partly settled" exit. INCOMPLETE is allowed
  only when the environment ends the session.
- Name every model with its effort. The work it returns is credited as AI-produced by GPT-6 Astra (ChatGPT Pro mode).
- Read these memory files first. They are in `<local>/.claude/projects/C--Users-user-Documents/memory/`:
  - pro-prompts-push-the-math.md
  - prompts-state-the-outcome.md
  - parsimonious-pro-slots.md
  - broad-context-for-pro-notes.md
  - pro-prompt-folders.md
  - checkpoint-zips-every-prompt.md

**The check.** This must pass:
```
python -I -B <local>/Documents/claude_tools/push_rule_pro_prompts.py --lint-math <PROMPT.md>
```

## Where it goes

- The folder is `<local>/Documents/pro_prompt_builds/RESEARCH_SA<nn>/`. It is flat and holds at most 20
  files: the files to send and nothing else (`PROMPT.md` and the ZIPs). Each file is under the 10 MB upload limit.
- Keep work files in `pro_prompt_builds/RESEARCH_SA<nn>_work/`.
- Write the README as `pro_prompt_builds/RESEARCH_SA<nn>.README.md`. It says what the prompt is, which account,
  what to send ("all files, no text"), the lint result, and the sizes.

## Rules

- No git.
- No recursive search over <local>/Documents; name the folder.
- Run Python as `python -I -B`.
- Write only in the places named above.
- Send nothing. The main session sends.

**Final message**, at most 120 words:
- two lines describing the prompt: what it asks, and its main question;
- the folder, the file count and the total size;
- the lint result.


**Moved, 19 Nov 2026 02:2x UTC (main session):** the build folder `TO_SEND/11_Finish_prompts/` is now `<local>/Documents/pro_prompt_builds/` (the user saw every prompt twice in TO_SEND). Build there; the main session links each finished prompt into `TO_SEND/PRO/` by topic. Never write into TO_SEND yourself.
