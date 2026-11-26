# 94_THETA_CIRCUIT_SIZE: update of 24 Nov 2026

By Claude Opus 5.5 at effort max (agent a4348514ce0275bbf), for main session 329fb1e6 (Claude Opus 5.5 at effort max),
following `PROMPT_UPDATE_BRIEF.md`. Codex wrote the prompt; the user authorized updates to every waiting prompt.

**State before the update.** The prompt was not sent: it is absent from `TO_SEND/PRO/SENT_PRO.tsv` and from every SENT
folder.

**Backup.** `TO_SEND/PRO/_backups_20261125/94_THETA_CIRCUIT_SIZE/` holds:
- copies of PROMPT.md and the ZIP;
- `send_folder_as_found/`, the original send folder, moved there unchanged;
- `spec_before_20261125/`, with the spec, the plan and SOURCE_INDEX.tsv as they were;
- `UPDATE_NOTE_20261125.md`, the note for Codex.

**Build.** Built with `build_papers.py 94` and placed with `--place 94`.
- Lints: PASS (the builder runs both).
- 77 files, ZIP 0.6 MB, SHA256 prefix 95eafa6e.
- The prompt is 4,541 words.

## Changes, each with its evidence

1. **A way out removed.** The PUSH line ended with "A strictly stronger necessary condition with a proved exhaustiveness
   boundary is a worthwhile partial result."
   - That sentence offers a cheaper deliverable in place of the answer, and the prompt rules in `Documents/AGENTS.md`
     ("PROMPTS: NO STOPPING BEFORE THE TASK IS DONE") forbid such alternatives.
   - The PUSH line now asks for the minimum, 17 or 18, with a checked witness or a proof covering every eligible DAG.
2. **New inputs: the graph's newer all-gate bounds**, all equal to |E| + τ − 1. Source: the fleet mirror of 24 Nov 2026,
   21:54 UTC (`pequalnp_work/fleet_mirror/RESULTS.tsv`, `fleet_lookup.py --id`).
   - L-meta-1549, checked 24 Nov 05:33 UTC: the theta with paths of 3, 4 and 4 edges needs at least 15 gates. Its hubs
     are not adjacent; its cycles have lengths 7, 7 and 8. The 14-gate attempts L-meta-2452, 2454 and 2456 were refuted.
   - L-meta-657, checked 23 Nov 14:20 UTC: the theta with paths of 4, 4 and 4 edges needs at least 16.
   - L-meta-722, checked 23 Nov 17:01 UTC: the theta with paths of 1, 2 and 5 edges needs at least 11. Its hubs are
     adjacent, but it has a triangle.
   - L-meta-1543 and L-meta-1547, checked 24 Nov: the 7-cycle with three leaves needs at least 14.
   - The Lean proofs of 1549, 657 and 722 are attached in `fleet_lean/`, copied from the local mirror of the fleet's
     tree and indexed in SOURCE_INDEX.tsv with their SHA256.
   - L-meta-519 itself is still a conjecture, with 0 attempts, and no fleet node concerns the theta with paths of 1, 6
     and 6 edges. So the question is not overtaken.
3. **Attack 1 reordered.** It now begins with adapting the certified argument of 1549 and 722 to this theta, or with
   locating the step that adjacent hubs with two long paths break and repairing it.

**What stays.**
- The model, the head-start facts, the witness and its hashes.
- The hazard route, the 21 families, and the eight-cycle follow-on.
- The paper and Lean rules, and the half-hour returns with their review rule.

**Considered and not added.** Our SPLIT_ZERO paper 4 results (L-meta-2237's read-1 case, thm:twomissing and
thm:threemissing) concern monotone circuits. The theta's AND/OR optimum, 18, is already the checked 615. Neither bears on
the NOT-gate question.
