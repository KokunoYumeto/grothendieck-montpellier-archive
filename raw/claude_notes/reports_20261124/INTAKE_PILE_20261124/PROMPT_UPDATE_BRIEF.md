# Updating the waiting prompts with the pile's findings: brief (24 Nov 2026)

From the main session 329fb1e6 (Claude Opus 5.5 at effort max). The user, 24 Nov 2026 ~22:02 UTC: [the user's words, omitted] And: "Learning
anything that needs to be a prompt but isn't yet. Noting that, we have a backlog, so changing a current prompt with updated
stuff is usually better. But wherever something genuinely deserves a new prompt, findings are old or new, that is also
fine."

## Your prompts

They are named in the message that sent you here. A prompt is a folder under `<local>/Documents/TO_SEND/PRO/`,
holding PROMPT.md and one ZIP. Before you change one, check that it has not been sent:
- its name must not be in `TO_SEND/PRO/SENT_PRO.tsv`;
- it must not sit in a folder named SENT.

A sent prompt is never changed. Report it, and if the findings matter for its run, propose a follow-up message instead.

## What to change

Give each change its evidence: a file and line, or a source and its statement.
- **Settled items.** An item the prompt asks that is now settled, by a checked result of ours or by outside work, becomes a
  result in the background:
  - its statement;
  - where its proof is;
  - its check state.

  The prompt then asks the next question beyond it.
- **Overtaken or known items.** Cite the work, with its exact locator and date, and remove or reframe the question.
- **New inputs.** Add the new results the run should use, ours or outside, to the background:
  - with their exact statements and locators;
  - with their LaTeX source in the ZIP where it exists (the arXiv e-print `https://arxiv.org/e-print/<id>`, our own TeX);
    a PDF only where no source exists.
- **Corrections.** Fix errors found in the material the prompt attaches, and say so in the prompt.
- **New questions.** Add the questions the maps raise that belong to the prompt's topic, in the prompt's order of
  importance.
- **What must stay.** Keep the prompt's force and all its rules:
  - its main questions;
  - the push paragraph;
  - the three-hour ledger check;
  - the checkpoint rules;
  - CHECK_EVENTS.tsv.

  Add no minimums, no ways out and no cheaper alternatives (the prompt rules in `Documents/AGENTS.md`). A run of a prompt
  asks for mathematics: every item is a task, not a request for an opinion.

## Where the findings are

`<local>/Documents/reports_20261124/INTAKE_PILE_20261124/`:
- the cluster files;
- `TOPICALITY_*.md`, `OLDER_RUNS.md`, `OLDER_NOTES.md`, `MAP_*.md`, `FLEET_MAP.md`;
- `LITERATURE_20261124.md`, with every Hexagon post of 14-24 Nov in its appendix;
- `PENDING.md`.

Open every source you rely on at the statement.

## How to change a prompt

- **Back it up first.** Copy the whole folder to `<local>/Documents/TO_SEND/PRO/_backups_20261125/<folder name>/`.
  The send folder itself must keep only PROMPT.md and its one ZIP.
- **Builder-built prompts** have a spec in `<local>/Documents/pro_prompt_builds/PAPERS_20261122/specs/<NN_KEY>.md`
  with a `.plan.json` listing files, trees and arXiv ids.
  1. Edit the spec and the plan.
  2. Run `python -I -B <local>/Documents/pro_prompt_builds/PAPERS_20261122/build_papers.py NN`.
  3. When both lints pass, run the same command with `--place NN`.
- **Other prompts.**
  1. Edit PROMPT.md.
  2. Rebuild the ZIP flat, keeping every existing member and adding the new ones. Update its MANIFEST, if it has one, with
     each new file's origin and SHA256. `<local>/Documents/claude_tools/prompts/pack_one_zip.py` repacks a send
     folder.
  3. Lint it with `python -I -B <local>/Documents/claude_tools/push_rule_pro_prompts.py --lint-math PROMPT.md`
     for mathematics, or `--lint` for anything else.
  4. For a prompt that writes a paper, also run `python -I -B <local>/Documents/claude_tools/paper_completeness_lint.py PROMPT.md`.
- **Prompts in another session's folder** stay as they are. Prompts 74*, 78 and `9_S6_papers/` are not yours.

## New prompts

The user prefers that a waiting prompt be updated. Where a finding still deserves a run of its own, with no waiting prompt
that can take it, propose one in your report:
- its main question;
- why it matters;
- what exists already;
- its inputs.

Do not build it; the main session decides.

## Report

Write `PROMPT_UPDATES/<folder>_UPDATE.md` in the pile folder: every change with its evidence, the lint results, and the
proposals. Your final message gives:
- the prompts changed, one line each;
- the lint results;
- the proposals;
- anything you left alone, and why.

## Rules

- Name every model with its effort setting.
- Leave unopened SAT_WITNESS*, SAT_KRONECKER* and the prompt-74 files.
- If a safety notice stops you on a paper, drop that paper and move on.
- Nothing is sent or published. No git.
- Keep your work file, `<local>/Documents/agent_notes/<your agent id>_NOTES.md`.
