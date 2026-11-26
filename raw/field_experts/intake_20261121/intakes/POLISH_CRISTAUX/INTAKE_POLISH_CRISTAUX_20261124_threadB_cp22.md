# Intake: POLISH_CRISTAUX thread B (the 92b continuation), checkpoint 18 to checkpoint 22, and the changes to 92c

Intake by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb), 24 Nov 2026, for the main session 329fb1e6 (Claude
Opus 5.5 at effort max).
- **The run.** GPT-6 Astra (ChatGPT Pro mode). It does not expose its effort setting. All of its checks are same-model,
  with no human check.
- **Brief.** `field_experts/intake_20261121/INTAKE_WAVE_20261123_EVENING.md`, with `INTAKE_BRIEF_20261121.md`. Both
  are unchanged since I read them; my final intake (`INTAKE_POLISH_CRISTAUX_20261123_final.md`, on the split of the
  threads) was reread first.
- **Check events.** `INTAKE_POLISH_CRISTAUX_20261124_threadB_cp22_CHECK_EVENTS.tsv` (13 rows).
- **Scripts.** In my scratchpad folder `pc_final/`: bdiff.py, stm.py, checks22.py, se_check.py. Each ran with
  `python -I -B` against the return folders.

## 0. Scope

**Return.** `research_returns/POLISH_CRISTAUX_checkpoint_22_20261123T2145Z_unzipped`, compared against thread B's cp18:
- **Thread.** It is thread B: the README says "The continuation began 23 November 2026 at 13:58:55 UTC".
- **Pages.** 21 papers, 508 pages.
- **Carried checkpoints.** The folders for cp19 (19:29 UTC) and cp21 (20:58 UTC) each hold one file,
  `paper19/MANIFEST.sha256`, and nothing that cp22 lacks.

**Thread B was still running at cp22.**
- Reviews 10 (17:59 UTC), 11 (18:59) and 12 (19:58) all recorded qualifying movement, so the stale count was 0.
- Review 13 was due at 20:58:55 UTC, and the next checkpoint at 21:28:55 UTC. The last ledger block is at 20:45:11 UTC.
- So checkpoints after 22 may exist. Whoever holds that ChatGPT conversation should look for them before 92c is sent.

**What I read.**
- In full:
  - the cp22 README;
  - the ledger blocks after checkpoint 18 (lines 628-776);
  - Paper 2 `single_exception.tex` lines 1-301 (statements, the restricted subgroup, rescaling, the chain count, and both
    pattern cases).
- At statement level:
  - Paper 2: thm:next-wild-band-complete, thm:single-wild-exception, prop:single-exception-patterns,
    lem:midpoint-normal-form, thm:matched-midpoint-all, thm:exchanged-midpoint-all;
  - Paper 9: thm:nolift, thm:integral-rational-injection, thm:affine-second-torsion, the revised
    thm:proper-integral-comparison, and rem:torsion in both threads;
  - Paper 21: thm:hasse-reduced, thm:ppav-open, thm:incoming, thm:natural-block, cor:uniform-block.
- Not opened:
  - `all_v_midpoints.tex` and `exchanged_midpoint.tex`: the proofs that the midpoint is excluded at every v;
  - Paper 9's new proofs;
  - Paper 21's proofs;
  - the programs (not run);
  - any cited source.

## 1. Verdicts, usefulness first

| Result (cp22 locator) | What it is good for | My check (this task) |
|---|---|---|
| **Paper 2, thm:next-wild-band-complete.** nu_min(p, (p-1)p^v k, 2) = v + 2 for every v >= 0, 2 <= k <= p^2, p not dividing k; v + 1 at k = 1. The exceptional set E_p of cp18 is gone. | **The SA15 inertia-character question on the whole band 1 <= k <= p^2, at every wild exponent.** It closes cp18's E_p, and thread A's open "first boundary" k = (p^2+1)/2. | Below |
| Paper 2, thm:single-exception-recovery and prop:single-exception-patterns. An unequal-character comparison at p^(v+3) forces k = p^2 - (p-1)/2, in one of two patterns (matched or exchanged). | The step that reduces E_p to one multiplier. | **Targeted proof check, confirmed**, given three carried inputs. The chain count was re-derived. The exchanged case forces p^2 \| k + (p-1)/2, and the matched families were recomputed for every prime 5-79 (1,714 cases). |
| Paper 2, thm:matched-midpoint-all and thm:exchanged-midpoint-all: both patterns are impossible at every v. | Removes the last multiplier. | Statement read only. The proofs (all_v_midpoints.tex, 358 lines; exchanged_midpoint.tex) were not read. The pattern arithmetic and centrality were recomputed. |
| Paper 2, lem:midpoint-normal-form: a height >= 2 law is X + Y through degree p^2 - 1, with lifting and mu_(p-1) clauses. | An input of the midpoint exclusions. | **First sentence re-proved** (Lazard's comparison lemma). The other clauses were not checked. |
| **Paper 9, thm:nolift.** H^1(C_X, O[1/p]) = H^1_rig(X/K) for every smooth separated finite-type X, with no global lift. | **Grothendieck's weak-formal cohomology is rigid cohomology rationally in degree one.** | Statement read |
| Paper 9, thm:integral-rational-injection. Integral H^1 is p-torsion-free and injects into the rational H^1. | It bounds the integral group by the rigid rank. | Statement read; consistent with thread A's Paper 9 |
| Paper 9, thm:affine-second-torsion. On A^1, the finite sites carry countable free W_n families, and H^2(C, O) contains a countable sum of K/W. | The integral theory is not finitely generated; the affine comparison fails in degree one at finite level. | **Targeted check of the H^2 deduction** from H^1(C_A1, O) = 0 and the long exact sequence |
| **Paper 21 (29 pp).** thm:hasse-reduced: in every degree d the Hasse divisor in \|3d Theta\| on an ordinary principally polarized surface (characteristic two) is reduced, of degree 9d^2, with generic corank one. thm:ppav-open: GL_8 on an ordinary moduli open. thm:incoming, thm:natural-block, cor:uniform-block: an actual GL_8 block fixing a complement for every d >= n + 1. | Grothendieck's question on Frobenius on hypersurface sections: first all-degree structure beyond fixed examples. | **Computation:** the degree 9d^2 (the relative H^1 quotient is Omega_P) and deg phi = n^2. Reducedness and the monodromy proofs were not checked. |

**The three carried inputs of the targeted check**, not checked by me:
- rc-lem:newton, the point values (SE.4)-(SE.5);
- pg-lem:primitives, dim Prim = 2n - 1 (SE.7);
- prop:wild-two-slope-patterns, the reduction to two central two-slope objects.

**Counts** (13 events):
- 3 targeted proof checks, all confirmed;
- 1 independent re-proof;
- 4 computations, 2 of them records comparisons;
- 4 statement-level reads;
- 1 carried (the papers unchanged since cp18).

**No refutation.**

**Cross-thread consequence (event 4).** Thread A's necessary form at k = (p^2+1)/2 (thm:first-boundary-normal-form) is
exactly the hypothesis of thread B's exchanged case:
- z_1 = z_2 = ((p-1)/2) p^(v+3);
- alpha_2 = -alpha_1;
- canonical lines exchanged.

B's argument then requires p^2 | (p^2+1)/2 + (p-1)/2 = p(p+1)/2, which fails. So, given B's carried inputs, thread A's
boundary case is empty. Its normal form, nonsplit-Cartan exclusion and point-field results are true statements about a
case that does not occur.

**A trap for the merge.** Both threads call their number k0, and they are different numbers:
- A's k0 = (p^2+1)/2;
- B's k0 = p^2 - (p-1)/2.

These are the smallest and the largest elements of the third family of cp18's E_p, which has (p+1)/2 elements, spaced p
apart.

## 2. The diff of thread B, cp18 against cp22

**Papers.** No paper was added, removed or renumbered: still Papers 1-21 in cp18's numbering.

| Paper | cp18 | cp22 | Statements | Sources |
|---|---|---|---|---|
| 2 | 120 pp | 140 pp | 133 -> 145 (+12) | 3 new tex files (`single_exception.tex`, `all_v_midpoints.tex`, `exchanged_midpoint.tex`); 4 changed |
| 9 | | 40 pp | 19 -> 27 (+8) | 4 new tex files; 3 changed |
| 21 | | 29 pp | 9 -> 22 (+13) | `hasse_reducedness.tex` new; main.tex changed |
| all others (1, 3-8, 10-20) | | | identical | identical |

**Paper 2, new statements** (12):
- thm:next-wild-band-complete and cor:next-wild-band-complete;
- thm:single-wild-exception and thm:single-exception-recovery;
- prop:single-exception-patterns;
- thm:matched-midpoint-exclusion, thm:matched-midpoint-third and thm:matched-midpoint-all;
- thm:exchanged-midpoint-exclusion and thm:exchanged-midpoint-all;
- lem:midpoint-normal-form;
- cor:small-wild-complete.

prop:first-wild-ss changed only editorially (one word; its source file reassigned). thm:wild-few-exceptions (the E_p
theorem) is still in the paper, although the complete band supersedes it.

**Paper 9, new statements** (8):
- thm:nolift;
- thm:integral-rational-injection;
- thm:affine-second-torsion and cor:affine-divisible-torsion;
- prop:projective-line-partial;
- lem:nolift-horizontal, lem:finite-diagonal-constants and lem:nilpotent-power-sum.

Revised:
- thm:proper-integral-comparison: the Ogus clause no longer assumes geometric connectedness;
- rem:torsion: now "in integral first cohomology".

**Paper 21, new statements** (13):
- thm:hasse-reduced and thm:ppav-open;
- thm:incoming, thm:natural-block and cor:uniform-block;
- lem:hecke-saturation, lem:ordinary-residual, lem:simple-contact, lem:extract-block and lem:symmetric-determinant;
- prop:theta-jets, cor:generic-attachment and prop:ordinary-ample-hasse.

The title is now "Ordinary principal surfaces, Hasse divisors and natural monodromy blocks".

**Withdrawn or refuted:** nothing. **Open, by the run's own record:**
- Paper 2: multipliers k > p^2, and realization of the lower examples over a fixed field or by elliptic curves.
- Paper 9:
  - the proper integral comparison without a global lift;
  - rational cohomology in higher degrees;
  - finite generation of integral H^1, and its image.
- Paper 21: the full eventual target image, Hasse irreducibility, stable rank loss, transvections, and an effective R.

**Register.** 677 of the original 1,018 rows are still NOT_YET_RECHECKED (thread A's final: 684).

## 3. Scope of the inputs

No statement uses RH, GRH (Alpöge's theorem) or Masullo's draft. Paper 21 works over fields of characteristic two and
uses no weights. Paper 9 cites the Monsky-Washnitzer/rigid comparison and Ogus.

## 4. Integration (applied, with backups)

Backups taken first in `field_experts/intake_20261121/integration_backups/20261123/POLISH_CRISTAUX/`:
- `SA15__STUDY__before_threadB_cp22.md`;
- `PRIMER_POLISH_CRISTAUX_20261123_before_threadB_cp22.md`.

Logged as rows 15-19 of `INTEGRATION_POLISH_CRISTAUX_20261123.tsv` (3 applied, 2 for the main session).

**Applied:**
- `results_register/horizontal/sweep3/SA15/STUDY.md`: the block "Thread B to checkpoint 22". It records the complete
  band, the exclusion of thread A's boundary, Paper 9's rigid comparison and H^2 torsion, and Paper 21.
- `PRIMER_POLISH_CRISTAUX_20261123.md`: updated in place (Paper 2, Paper 9, the 92b papers, open rows).
- `INTAKE_POLISH_CRISTAUX_20261123_final.md`: a pointer note at its head.

**For the main session:**
- the 92c rebuild of section 5;
- the board rows of section 6;
- the fleet map of section 7.

## 5. What must change in 92c when cp22 replaces cp18

The file is `TO_SEND/PRO/1_Archive_research_by_topic/92c_POLISH_CRISTAUX_merge_threads/PROMPT.md`, section "Sent again:
merge the two threads of the first run". Each change gives the current wording and its replacement.

1. **The Thread B bullet.**
   - Now: "It wrote checkpoints 14 to 18, the last at 17:44 UTC on 23 November, and none after it. Its checkpoint 18 is
     attached as `POLISH_CRISTAUX_threadB_checkpoint_18.zip`."
   - Replace with: "It wrote checkpoints 14 to 22, the last filed at 21:45 UTC on 23 November. It was still active then:
     its review 12 at 19:58 UTC recorded movement. Its checkpoint 22 is attached as
     `POLISH_CRISTAUX_threadB_checkpoint_22.zip`."
   - If a later thread-B checkpoint turns up, attach that one and name it instead.
2. **Checkpoint numbering.** "Number your checkpoints from 20 onwards" becomes "from 23 onwards": thread B used 14-22,
   thread A 14-19 and its final.
3. **Item 1, one numbering.** Unchanged: no thread-B paper was added or renumbered after cp18.
   - Add to the Papers 19-21 line: "thread B's Paper 21 is now 29 pages with 22 statements ('Ordinary principal
     surfaces, Hasse divisors and natural monodromy blocks')".
   - Thread B's Paper 19 (Lubin-Tate) is unchanged since cp18, so the Paper 18 instruction stands.
4. **Item 2, reconcile.** Paper 2: replace "(41 in thread A, 19 in thread B)" with "(41 in thread A; 31 in thread B,
   19 by its checkpoint 18 and 12 more by checkpoint 22)". Then add:
   - "Thread B's thm:next-wild-band-complete gives index v + 2 for every v >= 0 and 2 <= k <= p^2, p not dividing k (v + 1
     at k = 1). It supersedes thread B's E_p theorem (thm:wild-few-exceptions; keep it only as a step, or drop it) and
     thread A's bands for p not dividing k."
   - "Thread A's first-boundary package at k = (p^2+1)/2 concerns a case that thread B's single-exception argument
     excludes. This covers thm:first-boundary-normal-form, cor:boundary-nonsplit-cartan-image, the point-field degrees,
     and the divisorial, Cartan-torus and Liedtke-Matsumoto material. A's normal form is exactly the hypothesis of B's
     exchanged case, which forces p^2 | k + (p-1)/2. Check that exclusion in full. Then keep the package only as a
     recorded necessary-condition analysis, stated as vacuous, or move it to an appendix."
   - "The two threads use k0 for different numbers: A's (p^2+1)/2, B's p^2 - (p-1)/2. Rename one."
   - "The 1,595-value agreement still holds: thread B's values in thread A's range did not change."
5. **Item 2, Paper 9.** Replace the instruction with: "Paper 9: start from thread B's 40-page text of checkpoint 22 (27
   statements, thread A's seven included; its page QA is recorded as complete). Use B's wording of rem:torsion ('in
   integral first cohomology'): thread A's 'absence of p-torsion on the affine-line site' is false in degree two by
   thm:affine-second-torsion."
6. **Item 2, unchanged.** Paper 8, Paper 10, and the regeneration of STATEMENTS.tsv: thread B's Papers 8 and 10 did not
   change after cp18. Add thread B's Paper 21 to the papers whose STATEMENTS.tsv must be regenerated after the merge.
7. **Item 3, the mathematics left.**
   - Delete "the boundary k0 = (p^2+1)/2: existence or exclusion, and the sharp index" and "the indices k in E_p for
     v >= 1".
   - Put in their place:
     - "a complete check of thread B's closure of the band: thm:single-exception-recovery, prop:wild-two-slope-patterns,
       the two midpoint exclusions at every v, and lem:midpoint-normal-form";
     - "the next band, multipliers k > p^2";
     - "realization of the lower examples over a fixed field and by elliptic curves".
   - Keep the Lubin-Tate elementary divisors and the quantitative bounds in Paper 10.
   - Extend the monodromy item to "Papers 15, 17, 20 and 21: general primitive and fixed-embedding monodromy; for Paper 21
     the full eventual image, Hasse irreducibility, stable rank loss and an effective R".
   - Add "Paper 9: the proper integral comparison without a global lift, rational higher degrees, and finite generation
     of integral H^1".
8. **NOT_ATTACHED.tsv.** List cp22's renders and built PDFs as was done for cp18. cp22 unpacked is 163 MB, 3,321 files.

## 6. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)

These change the rows of my final intake as stated; the others stand.

| title | statement | what it adds | gate left |
|---|---|---|---|
| The complete next wild band for the special inertia character | thread B cp22 Paper 2 thm:next-wild-band-complete (with thm:single-exception-recovery, the two midpoint exclusions) | nu_min = v + 2 on the whole band 2 <= k <= p^2, p not dividing k, every v; closes thread A's boundary | the merge; a full check of the midpoint exclusions and of the three carried inputs by a model other than GPT-6 Astra (my targeted check covers the reduction to one multiplier); literature (Hattori, Bondarko, Ozeki-Yoshida as searched by the run). Replaces the row "Exact wild indices ... and the first boundary". |
| Grothendieck's weak-formal H^1: rigid rationally, torsion-free integrally, with infinite torsion in H^2 | thread B cp22 Paper 9 thm:nolift, thm:integral-rational-injection, thm:affine-second-torsion; thread A's thm:affine, thm:proper, cor:elliptic | the rational theory is rigid cohomology without any lift; the integral theory differs and is not finitely generated in degree two | the merge; a check of the torsor and site proofs. Replaces the row "Grothendieck's weak-formal H^1 fails both comparison tests". |
| Reduced Hasse divisors and natural GL_8 blocks in every cubic-theta degree | thread B cp22 Paper 21 thm:hasse-reduced, thm:ppav-open, thm:natural-block, cor:uniform-block | all-degree structure for Frobenius on the sections \|3d Theta\| of ordinary principally polarized surfaces in characteristic two | proofs read and checked by a different model; the eventual full image is open. New row. |

## 7. For the P vs NP fleet (constructed, not graded)

- **The chain count** (Paper 2, se-part 4). A lower bound on the dimension of a primitive space, from distinct labels
  under a diagonalizable grading and an F_p^x scalar: a dimension-counting certificate.
  - Node: none that I know of. I did not reopen PROOF_GRAPH.tsv; the ids I know are those of my cp18 map.
  - Work: record it as a library lemma if the fleet has rank lower bounds from torus-weight labels.
- **The Hasse-Witt determinant on P(H^0(3d Theta))** (Paper 21). An explicit degree-9d^2 form over F_2, the determinant
  of a Frobenius-twisted matrix on Omega_P, shown to be reduced.
  - Nearest node: L-gct-006, as in the cp18 map (determinantal polynomials).
  - Translation: a family of explicit determinantal forms over F_2 that are squarefree.
  - Work: none proposed beyond recording the family.
- **Papers 9 and 19:** no node. I made no edit to the fleet's files.

## 8. Hexagon readiness

No candidate passes the five tests. Every check of the run is same-model, the threads are not merged, and thread B may
have gone on past cp22.

The complete next wild band is now the strongest result of the run. My targeted check of its reduction step is the first
check of it by a different model. It still needs the midpoint exclusions and the three carried inputs checked.

## 9. Superseded items of my earlier intakes

These were correct when written and are now superseded:
- In my final intake, section 5 listed two research items: "the boundary k0 = (p^2+1)/2" and "E_p for v >= 1". Thread
  B claims both settled (section 5 above).
- Its board row "Exact wild indices ... gate: the boundary index (open)" is replaced in section 6.
