# Playbook: what gets good results from each model and in prompts (17 Nov 2026)

Kept by the main session (Claude Opus 5.5 at effort max) as its working playbook; this is a public copy for the project's methodology and training data. Each item is a practice that works, with the case that taught it.

How we get good results from the team. Each item is a practice that works, with the case that taught it. Add an item
when a case teaches one.

## Prompts and briefs (any model)
1. **Purpose and scope first.** A paper carries our new results, proved in full. Known and classical results are cited
   with exact locators. The exhaustive version is published beside the paper as a tag-linked proof compendium. Case:
   S6_09_PAPERS (17 Nov) wrote 2,193 pages for about 200 pages of new mathematics. The plan that fixes it is in
   `s6_pro_prompts_20261112_work/S6_10_REVISION/` (LAYOUT_DESIGN v3, KEEP_SKETCH).
2. **Ask for the whole task.** No minimums and no cheaper alternatives. Case: TOTAL_EXACT and S6_02 (12 Nov),
   AGENTS.md.
3. **Only proved or refuted finishes an item.** The three-hour check keeps long runs on the main question. Cases:
   TOTAL_EXACT; LM4 and the LM7 Fermat tower (13 Nov).
4. **Every statement names its hypotheses and choices.** Case: Paper III's "class 0" holds on the reference fan, while
   another fan gives class 3 (S6 intake, 17 Nov).
5. **Ask for real statuses:**
   - proved;
   - proved under hypotheses H, with whether H holds where it is used;
   - open;
   - false as stated, with the counterexample and the corrected statement.

   Not "conditional" (see Astra below).
6. **Check records name every checker.** Write "also checked in this writing" where earlier checks exist and "checked
   only in this writing" where the writing run is the only one. The writing run counts as a checker. We build the
   per-result check ledger by script and give it to the writer. Case: S6_09 mapped outside checks to 28 of 1,184 rows
   (user, 17 Nov).
7. **Checkpoints carry the current state and a list of files, not the whole history.** Case: LM4_SUCCESSOR repacks
   every earlier checkpoint each hour (2.4 GB). Three long runs ended early on 16-17 Nov, all with huge checkpoints.
8. **Context packages: own work first, then the context.** The run freezes its own transcription before opening the
   context. Others' readings (Hua's project) are credited witnesses, corrected where they differ. Case: the four
   transcription finals of 17 Nov used the new context exactly so, at no cost in time or quality.
9. **Use the user's categories, in their sense.** Case: "one derivation" was a label an agent coined and I repeated.
   The user's rule had [the user's words, omitted] and "unchecked", and the writing run counts as a checker (17 Nov).

## Know the team
- **GPT-6 Astra (ChatGPT Pro mode):**
  - A strong mathematician: a result only Astra has checked is not presumed wrong.
  - It proves exhaustively and checks itself pedantically, so tell it what to leave out (item 1).
  - Its caution runs to underclaiming. Read its check records and "open" labels in context.
  - "Conditional" can be genuine, or a polite "not proved" or "wrong as stated". Case: CDP20, which held only far more
    narrowly than claimed and was still called conditional. Ask what the condition is, whether it is ever met, and
    whether the statement as written is true (item 5).
  - Two runs per account at once. Its checkpoints are what survive a crash.
- **Claude Fable 5.2 at effort max:**
  - It reads a field and sees what is true across it. Its hunches are its value.
  - A strong independent second reader before publication, close to a must-have but not a requirement
    (field_experts/CROSS_MODEL_CATCHES.md).
  - Give it bounded problems and the files. Near its context edge, cut a copy with room.
- **Claude Opus 5.5 (the main session):** procedure, records, integration and design. What works:
  - think independently, as the one responsible for the result;
  - read rules in their reasonable sense, and design from the goal and the field's practice. Case: S6 layout v3,
    Lamport's structured proofs, Stacks tags (goals-not-specs);
  - give a hunch of the user's a real hearing: find the version that could be true, check it against the papers the
    user has read, and say precisely what holds and what does not. Do not set it aside by citing a basic fact; that
    lets people think they are wrong when they are not (the user, 17 Nov);
  - notes state the case, its cause in the work, and the fix.
- **GPT-5.6 / GPT-6.1 Sol (API, Codex):** cheap and reliable for translation, ports and builds. Codex keeps the
  maintenance code plug-and-play.

How to apply: read a prompt, brief or design against this list before it goes out.
