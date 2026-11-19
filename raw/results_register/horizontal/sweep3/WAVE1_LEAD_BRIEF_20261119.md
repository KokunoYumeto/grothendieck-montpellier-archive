# Sweep 3, wave 1: the lead's brief (19 Nov 2026)

From the main session (Claude Opus 5.5 at effort max), at the user's word ([the user's words, omitted]). Sweep 3 has studied 12 of the 32 topics in depth. Wave 1 takes the least-studied topics next
(sweep2/GLOBAL/NEGLECT.tsv), each to the agent that swept it in sweeps 1-2. If you are compacted, your summary is not
reliable: reread this brief, your launch message and your own output files, then go on.

## The task for each of your topics
1. **Read every transcribed page in full and work it through**, by the reader method of `READER_BRIEF.md` (read the
   transcription; look at the scan wherever the reading is in doubt, the ink decides; work through each item; dependencies;
   hunches; deliverable state; reused material identified in one line).
   - Split the pages into stretches for your readers (sub-agents, Claude Opus 5.5 at effort max, the number your message
     allows, ~300k each). Each reader's launch prompt names its topic and stretch, points to `READER_BRIEF.md`, and states
     "Sub-agents allowed: 0".
   - Read a stretch yourself where that is cheaper than briefing a reader.
2. **Merge** the readers' outputs into the topic's folder `sweep3/SA<nn>/`, in the form of `sweep3/SA05/`: STUDY.md (what
   the pages contain and establish, item by item, with the unread stretches listed), HUNCHES.md, RESEARCH_PACKAGES.md,
   DELIVERABLES.tsv, DEPENDS.tsv, CORRECTIONS.tsv, CHECK_EVENTS.tsv (six fields: statement id, date, who (model, effort,
   run), type, outcome, where), and `readings/`.
3. **Use what exists:** your sweep-1 and sweep-2 files for the topic, `sweep2/SA<nn>/WHAT_IS_WHERE.md`, and the sweep-3.5
   propagation (`sweep3_5/PROPAGATION.tsv`, once it exists) for results from other topics that bear on yours.
4. **The research prompt.** Build the topic's research prompt by `PROMPT_BUILD_BRIEF.md`, in `pro_prompt_builds/RESEARCH_SA<nn>/`.
   Keep the attachments small: the user has seen that prompts carrying ~3 MB rarely die and 200 MB ones often do, so give
   the study, the readings and the transcriptions as text, and no scans. Lint with `--lint-math`. Link and pack it into
   `TO_SEND/PRO/1_Archive_research_by_topic/<next number>_SA<nn>_<short title>_night`, and add its line to ORDER.md there.
5. **Report** in a few lines: what the topic contains, the main open question, the corrections, and the prompt's path.
