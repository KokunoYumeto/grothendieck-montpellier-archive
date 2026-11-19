# Brief: Grothendieck's unproved claims in the Pro notes, the second half of the follow-ups pass (17 Nov 2026)

From the main session (Claude Opus 5.5 at effort max), 17 Nov 2026 03:35 UTC, to the follow-ups reader a9ebc3d6
(Claude Opus 5.5 at effort max). You did the first half: the notes' own ideas and unpursued implications
(`field_experts/FOLLOWUPS_FROM_NOTES_20261117.md`, your working folder `field_experts/followups_work_20261117/`). This is
the second half, which the user asked for in the same words: look through the notes Pro has made [the user's words, omitted].

- Model: Claude Opus 5.5. Effort: max.
- Sub-agents allowed: 0.
- Compute bound: about 600k tokens for this pass.
- If your context is compacted during the work, the summary is not reliable. Reread this brief and your `STATE.md`,
  then continue from the state recorded there.

## The entries

`field_experts/GROTHENDIECK_CLAIMS_MAP_20261117.tsv` (built by
`grothendieck_archive_transcription_20261110/tools_20261113/claims_map.py`) lists every entry of the Pro notes whose
kind is "unproved claim" or "conjecture": 1,387 entries in 53 packages. Number them #1 to #1387 in table order.

Your scope is the 1,137 entries whose `runs` cell is empty, the ones no note ties to any of our runs. Read each one in
full in its notes file:
- `grothendieck_archive_transcription_20261110/returns/<package>_unzipped/<package>_notes.md`, or one level deeper,
  `<package>_unzipped/<package>/<package>_notes.md`;
- a compressed copy as before is fine (it drops search logs and paths, and cuts verbatim quotations to 160
  characters).

Many of these entries are Grothendieck's claims on the page that the note marks as not proved there.

## The verdicts (one per entry)

**(a) Research item.** A statement to prove or refute, with:
- the cote and scans, and his words where they fix the statement (short);
- the cluster;
- a rank from 1 to 3. Rank 1 means it would decide a question he marks as central, or a block of a companion.

The clusters are the six consolidated prompts of `field_experts/UNPROMPTED_IDEAS_AUDIT_20261117.md` (last section): ANAB (points as sections), GT (the tower, structure at infinity), DER (Dérivateurs: localizers, excision, homotopy), S6/companion dictionary, TAME (tame topology, stratified spaces, networks, pseudolines; Esquisse §5-6, §8), CYCLES (cycles, motives, integral PD de Rham, analysers). A clear new cluster gets a plain name.

**(b) Edition matter for the second pass.** A reading, a convention, an error of the page, a dating or provenance
fact, or a cross-reference the companion should carry.

**(c) Nothing further.** One of:
- a standard or known result: say which, with a reference where you know one, without searching;
- a claim that the same notes, or the next pages, settle;
- a duplicate of one of your follow-ups items (name its @n) or of another entry here (name its #n);
- a step too local to matter.

## What our work already covers

The empty `runs` cell means only that the note names no run. A claim may still be settled or open in our registers.
Before calling an entry new, check it against these, by grep, not by reading whole files:
- `grothendieck_archive_transcription_20261110/notes_headlines/PROGRAMME_MAP.md` (every run's main results and open
  rows, in one page);
- `notes_headlines/HEADLINE_RESULTS.md`;
- for a likely match, the run's register.

Where an entry credits Michel Hua's project, keep the credit with his project.

## Write

**`field_experts/CLAIMS_FROM_NOTES_20261117.md` and `.tsv`**, in the format of your follow-ups file:
- scope and method, including what you read in full and what as digests, if you have to switch;
- a summary table by verdict and by cluster;
- the research items by cluster, strongest first, each with #n, package, entry id, cote and scans, statement and
  rank;
- the edition matters by package.

The TSV has one row per entry of your scope: #n, package, entry, verdict, cluster, rank, statement.

**`STATE.md`** in a new working folder `field_experts/claims_work_20261117/`, updated every 100 entries with the last
#n done, so that a compaction loses nothing.

**The final message, short:** the counts, and the ten strongest research items, one line each (#n, cote, scans,
statement in one sentence, cluster, rank).

Write plainly and declaratively. Name every model with its effort.
