# Fleet mirror: everything pequalnp.com has proved, tagged, with our work linked in

A local, regularly refreshed copy of the fleet's lemma graph, organized so that we can draw consequences from their
results without formalizing anything. Built by `refresh_fleet_mirror.py` (Claude Opus 5.5 at effort max, 23 Nov 2026);
refreshed hourly by `loop_refresh.py` (create `STOP` in this folder to end the loop).

- `RESULTS.tsv` / `RESULTS.json`: one row per lemma: id, program, status and since when, kind, tags, title, plain and
  formal (Lean) statement, depends_on, used_by, the accepted Lean file on the fleet's main branch, the last attempt (who,
  outcome, why it died), and every line of our work that mentions it.
- `BY_PROGRAM/<program>.md`: the readable list per program (gct, meta, clb, pcx, lib, alg), grouped by status.
- `INDEX_BY_TAG.md`: tag -> lemmas (checked ones starred). Topic tags are keyword rules over title and statements
  (list `TOPICS` in the script); structural tags: HARD-LINK, TARGET, SEARCH, restated, has-barrier, attempt-died,
  outside-proof, status:<s>.
- `OURS_BY_FLEET_ID.md`: for each fleet lemma our work touches: where (file:line, the line). Sources: our notes in
  pequalnp_work, the program maps in fleet_map/, the main session's field maps in fleet_map/maps/ (algebraic geometry,
  Hodge theory, analytic number theory, moonshine and the Leech lattice, algebra and combinatorics), the mirror tree,
  Codex's handoffs, our rows of the joint GCT table.
- `GRAVEYARD.md`: refuted and dead lemmas with their statements and why the last attempt died. `PLAN.md`, `SEATS.md`,
  `NEWS.md`: the fleet's published plan, seats and news.
- `CHANGELOG.md`: at every refresh, the new lemmas, the status changes and the fleet's strategy line.
- `FABLE_IMPLICATIONS.md`: what the whole map implies, hunches, and the big things to grind out (Fable agent).

## Added 24 Nov 2026 (~22:0x UTC): the whole fleet, locally, for intakes

- **Every lemma record.** `RESULTS.json` / `RESULTS.tsv`: all lemmas with their title, plain and formal statement,
  status, attempts, seat, dependencies and proof file. Refreshed hourly; network timeouts are now retried.
- **Every Lean file.** `../fleet_lean/lean/PEqualNP/`: an export of the fleet's repository at upstream/main.
  - The commit is in `../fleet_lean/UPSTREAM_COMMIT.txt`.
  - It is re-exported by the hourly refresh whenever upstream moves.
  - First export: 3,163 files, 131 MB, commit 9d8b1ae.
- **`fleet_lookup.py`**: search all lemmas by regex over the id, title, statements and tags, or look up `--id`.
  - Options: `--status`, `--program`, `--full`, `--json`.
  - It prints the status, the formal statement and the local path of the checked proof.
  - For intake agents mapping a result onto the fleet's graph.
- **`INTAKE_FLEET_MAPS.md`** (from `intake_fleet_maps.py`, also run hourly): every fleet lemma named in the main
  session's intakes, with its current status and the intake lines that name it. Open nodes come first.
