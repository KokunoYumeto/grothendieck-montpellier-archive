# 96_FLEET_HARD_LINKS: update of 24 Nov 2026

By Claude Opus 5.5 at effort max (agent a4348514ce0275bbf), for main session 329fb1e6 (Claude Opus 5.5 at effort max),
following `PROMPT_UPDATE_BRIEF.md`, the main session's list of findings, and its note on SPLIT_ZERO cp10.

**State before the update.** The prompt was not sent: it is absent from `TO_SEND/PRO/SENT_PRO.tsv` and from every SENT
folder.

**Backup.** `TO_SEND/PRO/_backups_20261125/96_FLEET_HARD_LINKS/` holds:
- copies of PROMPT.md, the ZIP and PUSH_NOTE.md;
- `send_folder_as_found/`, the original folder, moved there unchanged;
- `spec_before_20261125/`, with the spec and the plan as they were.

**Build.** Built with `build_papers.py 96` and placed with `--place 96`.
- Lints: PASS.
- 476 files, ZIP 6.8 MB, SHA256 prefix 6885038d.
- The prompt is 7,121 words.

**The push note is no longer in the send folder.** The brief allows only PROMPT.md and the ZIP there, so PUSH_NOTE.md
remains only in the backup. It warns that several attachments quote the user or give local paths, which holds equally for
the new `ours/maps/MAP_COMPLEXITY.md`.

## Changes, each with its evidence

### The whole prompt

- **The fleet mirror is current.** `ours/fleet_mirror/RESULTS.tsv` is now a frozen copy of the mirror of 24 Nov 2026,
  21:54 UTC (`pequalnp_work/fleet_mirror_snapshots/RESULTS_20261124T2154Z.tsv`). It has 5,645 lemmas:
  - 2,051 checked;
  - 2,882 conjectures;
  - 423 refuted;
  - 284 retired;
  - 5 in work.

  The text said 1,988 lemmas as of 23 Nov. The mirror is session 672ae3a0's (`FLEET_MAP.md` in the pile).
- **New attachments:**
  - `ours/fleet_map/PILE_FLEET_MAP_20261125.md`, the pile's FLEET_MAP.md;
  - `ours/maps/MAP_COMPLEXITY.md` with its check events;
  - `ours/SPLIT_ZERO_run2_cp10/paper4/`;
  - `ours/COUNTING_VARIETIES_cp03/counting/`, TeX only, since the builder leaves out PDFs;
  - `ours/VPVNP_WIRE_GEOMETRY_cp01/QUESTIONS.tsv`;
  - `ours/fleet_lean/L_meta_2237.lean`;
  - the follow-up check events of SPLIT_ZERO and COUNTING_VARIETIES.

### Part A

- **Added in "Why this matters": the two VP ≠ VNP claims of 23-24 Nov.** Both are unrefereed, and no human has checked
  either.
  - OpenAI's Corollary 1.2: the padded permanent lies outside the determinant orbit closure for
    m ≤ N ≤ exp(c(log m)^{5/4}), in characteristic 0, for m ≥ m₀.
  - If either holds, level spaces stop being a route to the asymptotic separation.
  - L-gct-086 stays open as a statement.
  - Level spaces remain the source of explicit small-m bounds, such as border size ≥ 26 for perm₇.
  - Evidence: `ours/extension/EXTERNAL.md`, and FM/VPVNP_NODE_VERDICTS_20261124.tsv.
- **L-gct-126 added to "Checked on the graph"** (Fischer's identity at M = 3).
  - It has a merged proof in the fleet's repository: commit 7dc6cc2, PR #2, 23 Nov, by `ring`.
  - Its record still reads conjecture.
  - Evidence: FLEET_MAP.md l.78, and `fleet_lookup.py --id L-gct-126`.

### Part B

- **The PUSH line's start for Part B** is now circuits in which at least four edges lack a quadratic witness, together with
  the exact count at line-degree two.
- **"Checked on the graph": L-meta-2237**, checked 24 Nov 18:29 UTC. Read-1 AND/OR circuits on 4-cycle-free graphs need
  |E| + τ − 1 gates.
  - It is the same statement as paper 4's read-1 case. The fleet's Lean proof came first, so the run cites it.
  - Evidence: FLEET_MAP.md l.70 and l.88, and the attached Lean file.
- **"Ours": L-meta-2239 settled on paper,** as our X-meta-006 (mirror commit f8123ad).
  - The statement: N(q + 2) − 1, exactly, for read-1 circuits on the incidence graph of a plane of order q.
  - The lower bound is 2237. The upper bound is the read-1 star circuit of L-meta-154.
  - The graph's record still reads conjecture.
  - Evidence: `ours/extension/entries/X-meta-006.md`, and FLEET_MAP.md l.60-61 and l.87.
- **From the second run of prompt 93 (cp10, 21:10 UTC):**
  - **thm:main:** Mon(f_G) = min over Sup(G) of the arithmetic complexity. For a C₄-free G, the quadratic and read-1
    complexities equal |E| + vc − 1.
  - **thm:twomissing and thm:threemissing:** the bound is exact when at most three edges lack a quadratic witness. It is
    also exact for every C₄-free graph with at most four edges.
  - **At four missing witnesses:** an induced matching of four missing edges forces at least six deleted gates, and the
    paper lists the remaining cases.
  - So a counterexample to 608 or 612 must miss quadratic witnesses on at least four edges.
  - **Check state:**
    - the run's re-proof is by the same model;
    - the AG_POLISH reader a4f5fd04 (Claude Opus 5.5 at effort high) ran an exhaustive monotone search on seven graphs
      with at most four edges. That is a sanity check, not a test of the open case.
  - **Open on the graph:** 2585 and 2635.
  - Evidence: `paper4/main.tex` l.62-100 of cp10; AG_POLISH.md, "Follow-up 25 Nov"; and
    INTAKE_SPLIT_ZERO_AFTER_FGJM_20261125_CHECK_EVENTS.tsv.
- **The fleet's open list** (606, 608, 612, 582, 650) is re-dated: unchanged at 21:54 UTC.
- **Research item 1** now starts at four missing witnesses, from the paper's list of cases.

### Part C

- **The old main question is settled, so it moves to the background.** It asked for a smooth hypersurface at every
  p ≥ 3 whose Hasse–Witt scalar is #SAT mod p. COUNTING_VARIETIES answers it with CV-THM-MAIN:
  - a smooth Calabi–Yau hypersurface, circuit-presented, with H^{d−2}(O) a line;
  - Frobenius acts on that line by S mod p, and #X(F_p) ≡ 1 + S;
  - the scalar is #_pP-complete, and its nonvanishing, equivalently Frobenius splitting, is Mod_pP-complete.

  The background also carries CV-THM-STABILIZER and the sparse and presentation boundaries, with their check state: the
  core lemmas checked by our intake (Claude Opus 5.5 at effort high), and the run's own "proof checking in progress".
  Evidence: AG_POLISH.md §9 and item 5; PILE/INTAKE_COUNTING_VARIETIES_20261124_CHECK_EVENTS.tsv; and the attached
  checkpoint 03.
- **The height-1 test (my map's NK-6)** is added. It is our own observation, not COUNTING_VARIETIES's.
  - The Artin–Mazur formal group is one-dimensional, with height 1 iff S ≢ 0 mod p.
  - So height-1 recognition is Mod_pP-complete.
  - Stienstra's p-th logarithm coefficient is S mod p.
- **The new main question,** in the PUSH line and as research item 1: the height of the formal group when
  #SAT(Φ) ≡ 0 mod p.
  - Prove the exact criterion that separates height 2 from height ≥ 3, through Stienstra's coefficients a_{p^k}.
  - Decide whether that criterion is a count attached to Φ, and prove it.
  - Determine the complexity of computing the height.
  - Artin–Mazur and Stienstra are to be opened at their theorem numbers.
- **The paper's title and contents follow:** "#SAT modulo p as a Hasse–Witt scalar, and the height of the formal group",
  crediting COUNTING_VARIETIES and NEG_NIGHT.
- **Research item 3 (the witness degree c_t)** gains two inputs: the two claims, and run 99's Q6e. Q6e derives, in
  characteristic 0, a separating highest-weight equation, conditionally on OpenAI's constants. If the claims hold, c_t is
  finite on OpenAI's range.

**Unchanged.** Parts A-C keep their main questions, apart from Part C's settled one. The order A, B, C stays, and so do the
remaining research items. The push, ledger, checkpoint and CHECK_EVENTS rules come from the builder and pass both lints.
