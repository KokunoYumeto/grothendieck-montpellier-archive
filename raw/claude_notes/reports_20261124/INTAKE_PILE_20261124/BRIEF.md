# The intake pile of 24-25 November 2026: brief for each cluster reader

From the main session 329fb1e6 (Claude Opus 5.5 at effort max). The user, 24 Nov 2026 ~21:1x UTC: "intake everything, as
in read in everything with like 5.5 agents, and then also recall what the other intake stuff is that we had and that we
didn't work through yet ... since everything's been intaked and thrown in a neat little pile and organized in terms of
interesting stuff ... you can always just do a little conference on all of that and see what kind of interesting stuff
there is." The pile you write is what that conference (Claude Fable 5.2, after the weekly reset) will read first. Write
it for that reader: what is in each run, what is worth attention, and where to find it.

## What to read, for each run of your cluster

1. **The newest return:** the newest folder `<RUN>_<checkpoint_NN|final>_<stamp>_unzipped` in
   `<local>/Documents/grothendieck_archive_transcription_20261110/research_returns/` (older checkpoints sit inside
   it under `_from_earlier_checkpoints/`: open them only for something the newest lacks). A run with several threads
   under one name (POLISH_CRISTAUX: thread A's final, thread B's checkpoint 22, the merge run's checkpoint 33) is read
   thread by thread.
2. **What was asked:** the run's prompt, `<local>/Documents/TO_SEND/PRO/1_Archive_research_by_topic/` (or its
   `SENT/`), folder `<NN>_<RUN>`.
3. **What is already known:** earlier intakes of the run (`<local>/Documents/field_experts/intake_*/intakes/<RUN>*`,
   the run's rows in `field_experts/INTAKE_LEDGER.md`, and `reports_2026112*/` notes naming the run: search by the run's
   name, in those folders only). Do not redo what an intake already did; say what is new since it.
4. **The mathematics itself:** the run's LEDGER.md, QUESTIONS.tsv, CHECK_EVENTS.tsv, CROSSWALK.tsv, DICTIONARY.md and its
   paper (TeX first). Open the proofs of its main theorems; a title or a ledger row is not a reading.

## What to write

Into `<local>/Documents/reports_20261124/INTAKE_PILE_20261124/`:

- **`<CLUSTER>.md`**, opening with **the cluster's most interesting items** (as many as deserve it, ranked by usefulness,
  one paragraph each: what it is, why it matters to its field, its check status, where it is). Then one section per run:
  1. **Useful or not, first:** does it contribute something meaningful to its field, a theorem someone would want, and
     why? (useful / marginal / not useful)
  2. **What it proved:** the main statements with their ids, in their exact form with hypotheses; the run's own check
     status and every check by others (model and effort as their records give them).
  3. **New since the last intake** (or "no earlier intake").
  4. **Open:** each main question's current gate, and what is undecided.
  5. **Relations:** to other runs by name, to the literature with locators, and to Grothendieck's frameworks (schemes
     over Z, λ-rings and K-theory, motives and correspondences, weights; a cote of the archive only where the run shows
     the connection).
  6. **Candidates:** a Hexagon note, a next prompt, a correction to report to its source (name them; draft nothing).
  7. **Problems:** errors, overclaims, gaps, each with the exact passage.
- **`<CLUSTER>_ITEMS.tsv`**: one row per item: run, item id, statement in one line, status (proved and checked by whom /
  proved by the run only / open / refuted), usefulness (useful / marginal / not useful), why it is interesting, locator.
- **Spot checks:** for each run's main new theorem, check the key step where you can. Record each check in
  `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` in the pile folder: statement id (in the run's own register form), date, who
  (Claude Opus 5.5 at effort high, this intake), type (targeted proof check / independent re-proof / computation or
  formal certificate / used and rechecked / carried as background without fault found / refuted, with the refined
  statement's id), outcome. Record only what you did: reading a statement is not a check of it.

If writing a file is refused, put its content in your final message and the main session saves it.

## Rules

- Do not change anything in the run folders. No git.
- Name every model with its effort setting (for the runs: GPT-6 Astra, ChatGPT Pro mode, unless the run says otherwise).
- Leave unopened: SAT_WITNESS*, SAT_KRONECKER* and the prompt-74 files (Codex's), and Codex's runs GCT_FLIP,
  GCT_SEPARATIONS, BORDER_RANK and SIGNED_COUNTS_AND_WINDING; the S6 series is another session's. If a safety notice stops
  you on a paper, drop that paper and move on.
- Keep running notes in `<local>/Documents/agent_notes/<your agent id>_NOTES.md`.
- Your final message: the cluster's ranked most interesting items (short), the files written, and anything you could not
  read with the reason.
