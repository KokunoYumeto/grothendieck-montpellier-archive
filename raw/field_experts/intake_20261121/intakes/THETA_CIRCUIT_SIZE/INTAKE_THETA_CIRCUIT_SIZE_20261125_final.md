# THETA_CIRCUIT_SIZE (prompt 94), final of 25 Nov 2026, 03:03 UTC: intake

Intake by Claude Opus 5.5 at effort max (agent a4ee2342403cca87e; pequalnp session 672ae3a0), 25 Nov 2026. Return:
`research_returns/THETA_CIRCUIT_SIZE_final_20261125T0303Z_unzipped/workbench/`. Prompt:
`TO_SEND/PRO/1_Archive_research_by_topic/SENT/94_THETA_CIRCUIT_SIZE/PROMPT.md`. Production model: GPT-6 Astra (ChatGPT Pro
mode); the run's records give its effort as "not exposed". Read: the prompt; README, LEDGER, STATEMENTS (31 rows),
QUESTIONS, CHECK_EVENTS (50 rows); the paper `papers/theta/main.tex` sections 1-4 (statements of Theorems 1.1-1.5 and
the complete proof of Theorem 1.1 with Lemmas 3.1, 3.2, 4.2-4.5). Not opened: the proofs of Theorems 1.2-1.5
(`main.tex` sections 5-6, `leaves.tex`, `oddleaves.tex`), the research reports, the Lean files, the SAT run.

## Most interesting items, ranked by usefulness

1. **The lead question is answered: the theta with paths of 1, 6 and 6 edges needs exactly 18 gates**
   (Corollary 1.3, THETA-003): `not HasCircuitSize 12 F 17`, `HasCircuitSize 12 F 18`. Lower bound = Theorem 1.1 (17
   binary gates even with NOTs, so a 17-gate circuit has no NOT) + the fleet's checked monotone theorem L-meta-615
   (fengqiaoqu) giving 18 for NOT-free circuits. **I checked Theorem 1.1's proof in full (below): no gap.**
2. **Theorem 1.1 (THETA-010), a general tool:** every circuit (AND/OR fan-in two, NOT, sharing) for the edge function
   of a nonempty finite simple graph with minimum degree >= 2 and no 4-cycle has at least n + tau(G) - 1 binary gates;
   a normalized circuit with t NOTs has >= n + tau - 1 + t gates. Corollary 7.2 (THETA-014): for any G without isolated
   vertices and any nonempty induced H of minimum degree 2 without C4, >= |V(G)| - 1 + tau(H) AND/OR gates.
3. **Theorem 1.2 (THETA-012): every simple theta without a 4-cycle has C(G) = C_+(G) = |E| + tau - 1** in the charged
   all-gate model: fengqiaoqu's monotone theorem (fleet L-meta-615) extended to arbitrary negations, with the monotone
   equality case re-proved (Prop. 5.4, credited).
4. **Theorem 1.3 (THETA-015): C_2k with two pendant leaves (k >= 3) needs exactly 3k+1 gates (roots in the same
   bipartition class) or 3k+2 (opposite classes).** At k = 4 with adjacent roots this is 14: **it settles the open fleet
   node L-meta-518.** The requested follow-on (C8, leaves at 0 and 3) is 14 (THETA-016).
5. Theorem 1.4 (THETA-028): odd C_(2k+1), k >= 4, three pairwise nonadjacent roots with odd arcs, one leaf each:
   exactly 3k+5; C9 with leaves at 0, 3, 6 needs exactly 17 (THETA-029).

## 1. Useful or not

Yes. It closes the question the prompt was written for, with a short and general proof, and turns two fleet routes
(the first-branch argument of jiaxun530 and the monotone carrier argument of fengqiaoqu) into a reusable bound
n + tau - 1 that holds with negations. It settles one open fleet node (L-meta-518) and gives the exact all-gate value
for every C4-free theta inside the open universal node L-meta-519.

## 2. What it proved (statements, hypotheses, check status)

Exact model: the fleet's `HasCircuitSize` (fan-in two AND/OR, NOT charged, sharing, the pinned straight-line semantics;
Lemma 3.1 normalizes it without increasing the AND/OR or the NOT count).
- THETA-010 / Theorem 1.1: G nonempty finite simple, min degree >= 2, no C4 (chords allowed): binary gates >= n+tau-1.
  Proof: terminal groups (first branching wire of each input) are independent (Lemma 4.3: a read-once pair cannot be
  AND under one restriction and OR under another through a unary map; Lemma 4.2 via De Morgan and the least common
  ancestor); after deleting earlier groups, active vertices of a group are residual twins (Lemma 4.4: no later-group
  input reaches the terminal; a two-valued code c(S) and the cut factorization d(c(S), T)); no C4 makes each twin group
  meet later groups in a star, so one vertex per group covers (Lemma 4.5); the incidence count g >= n-1+b+t (Lemma 3.2).
  Run checks: independent re-proof (worker independent_reproof) and targeted checks (root, leaf_reproof2), all GPT-6
  Astra (ChatGPT Pro mode). Lean: only the graph step (Lemma 4.5, `lean/BranchCoverCore.lean`) compiled with Lean 4.36.0,
  axioms propext, Classical.choice, Quot.sound.
- THETA-003 / Corollary 1.3: exact 18 for the labelled theta; THETA-001: the 18-gate witness on all 4096 rows.
- THETA-012 / Theorem 1.2: C4-free thetas, all-gate optimum |E|+tau-1; THETA-023 / Prop. 5.4: positive optimum n+tau
  (re-proof of fengqiaoqu's theorem); THETA-021 / Lemma 5.2: positive equality forces a minimum eligible cover and at most
  two consumption slots per carrier.
- THETA-015 / Theorem 1.3 (k >= 3), THETA-016 (C8 leaves 0, 3: 14); THETA-028 / Theorem 1.4 (k >= 4), THETA-029 (C9).
- THETA-013 / Lemma 7.1 (restriction normalization does not increase the branch count) and THETA-014 / Corollary 7.2.
- Corrections in the run: THETA-027 (carrier injectivity without normalization) refuted by a triangle example and
  replaced by THETA-024; THETA-031 (the even-cycle formula without k >= 3) refuted by a 6-gate C4 circuit (64 rows).
- Unnecessary after THETA-003: THETA-019 (hazard route, conditional), THETA-020 (17-gate one-NOT SAT: UNKNOWN at 120 s).
Checks by others: every check event is by workers of the same model, GPT-6 Astra (ChatGPT Pro mode), effort recorded as
"not exposed" (root, independent_reproof, leaf_reproof, leaf_reproof2, branch_bound, adjacent_audit, hazard_attack,
final consistency worker): 21 targeted proof checks, 14 independent re-proofs, 11 computations. No other model and no
human. My checks are in section 8 and in the CHECK_EVENTS file beside this intake.

## 3. New since the prompt's starting point

The prompt gave the interval 17-18, the monotone optimum (L-meta-615) and the hazard route. New: Theorem 1.1 (general,
with negations), Corollary 1.3 (the answer 18), Theorem 1.2 (all-gate exactness for every C4-free theta), Theorems 1.3
and 1.4 (cycles with two or three leaves), Lemma 7.1 / Corollary 7.2 (induced-core restriction). The paper re-proves
the monotone theta theorem in the form needed for the equality case and credits it.

## 4. Open: each question's gate

- Q-GENERAL (L-meta-519, subcubic girth >= 7, |E|+tau-1 with NOTs): open for graphs with more hubs; gate: the
  induced-core binary bound (Cor. 7.2) leaves the deficit |E| - |V| + tau(G) - tau(H); equality obstructions for
  positive circuits must be classified beyond thetas and two- or three-leaf cycles.
- Q-FOUR-MARKED (C12 with leaves at 0, 3, 6, 9): open; a fourth root permits a larger branch deficit.
- Q-FORMAL: the circuit-to-partition bridge (Lemmas 4.3, 4.4) and the positive equality analysis are not in Lean;
  `lean/ThetaDecisionConditional.lean` states the target with the two bounds as hypotheses and is uncompiled.
- Q-SAT (17 gates, one NOT): UNKNOWN; superseded by the proof.

## 5. Relations

- Fleet: L-meta-615 (monotone theta, fengqiaoqu) is the positive input; the first-branch partition is jiaxun530's (the
  1549 proof); L-meta-105 gives the upper bounds; L-meta-519 is the universal statement the corollary instantiates.
- Ours: X-meta-005 / L-meta-647 and our C4-free monotone line (prompt 93's paper 4, FLEET_HARD_LINKS Part B) bound
  monotone circuits; Theorem 1.1 is the first bound of ours that survives arbitrary NOT gates on general C4-free graphs
  of minimum degree 2. Its count n + tau - 1 equals the fleet's |E| + tau - 1 exactly when |E| = n (cycles).
- Literature cited in the paper: Jukna's single-level gap (Thm 2.1), the hazard derivative of Ikenmeyer, Komarath,
  Lenzen, Lysikov, Mokhov and Sreenivasaiah, Jukna's hazard transformation, Ikenmeyer-Komarath-Saurabh games.

## 6. Candidates

- Hexagon note: Theorem 1.1 with Corollary 1.3 and Theorem 1.2 (exact circuit size of C4-free theta graphs with
  negations, after fengqiaoqu and jiaxun530). It is short, general and checked by hand here; the paper's opening already
  carries the credit split.
- X-entries for our public mirror: L-meta-518 (settled, section 8); the theta(1,6,6) value 18 as an instance of
  L-meta-519; Theorem 1.2 as the all-gate form of L-meta-615.
- Lean: the bridge Lemmas 4.2-4.4 are elementary and finite in spirit; with the compiled Lemma 4.5 they would give a
  kernel-checked Theorem 1.1, and with the fleet's checked 615 the literal `not HasCircuitSize 12 F 17`.

## 7. Problems, with the exact passages

- Formal status. README: "The circuit-to-partition argument and literal project-model lower bound are mathematical
  proofs, not complete new Lean certificates. `ThetaDecisionConditional.lean` states the exact target with the two
  formal bridge bounds as explicit hypotheses and is uncompiled." The fleet's desk accepts Lean only; a submission
  needs the bridge formalized.
- Single-model checking. LEDGER: "Parallel checks are by separate workers of that same model, not by independent model
  families or humans."
- Two corrected overstatements, both recorded honestly: THETA-027 ("Unqualified first-branch carrier injectivity for
  all positive legal programs ... refuted; corrected statement THETA-024"; triangle counterexample) and THETA-031 ("Even-
  cycle two-leaf formula without the k>=3 hypothesis ... Explicit6-gate circuit on C4 with opposite leaves").
- The prompt's own Theorem-574 caution ("The odd-thread theorem 574 requires h >= 3") is not needed by the final proof;
  no reliance on it was found in the parts read.

## 8. For the fleet

| Fleet node (live status, mirror of 25 Nov) | Result | Relation |
|---|---|---|
| L-meta-518, open: C8 with leaves at two adjacent cycle vertices, every circuit >= 14 | Theorem 1.3, k = 4, adjacent roots lie in opposite classes: exactly 3k+2 = 14 | **settles** (lower bound; the upper bound is L-meta-105). **Flag for an X-entry.** Check state: proved on paper, same-model independent re-proof (leaf_reproof2, from the statement and published lemmas); I checked the general lower bound it rests on (Thm 1.1) but not the leaf-specific equality argument of `leaves.tex`. |
| L-meta-519, open: subcubic, girth >= 7: |E| + tau <= s + 1 | Corollary 1.3 (theta 1,6,6: 18) and Theorem 1.2 (every C4-free theta) | **settles the theta members** of the class; sharpens (Cor. 7.2 is a general partial bound); the universal statement stays open. |
| L-meta-615, checked: monotone C4-free theta = |E|+tau-1 | Theorem 1.2 | **sharpens** a checked node: same value with arbitrary NOT gates. |
| L-meta-1549, 657, 722, checked (theta all-gate bounds) | Theorem 1.2 | subsumed (special cases). |
| L-meta-1551, open: search <= 14 gates for 1549's theta | Theorem 1.2 (and checked 1549) | refutes the search (already decided by checked 1549). |
| L-meta-595, open: search <= 10 gates, theta with paths 1, 2, 5 | Theorem 1.2 (and checked 722) | refutes the search (already decided by checked 722). |
| L-meta-612, open: C4-free, monotone >= |E|+tau-1 | Theorem 1.1 (n+tau-1 with NOTs) | parallels; equal to 612's value when |E| = n. |
| L-meta-824, open: an explicit 11-gate circuit for C6 with opposite leaves (evaluation) | Theorem 1.3, k = 3, opposite classes: optimum 11 | parallels: shows 824's circuit is optimal; 824 itself is a finite evaluation. |
| L-meta-4756 / 4758, open: theta(2,2,2) 12-gate AND/OR structure | Lemma 5.2 (equality forces minimum cover, two consumption slots) | parallels. |

Checked results that settle an open node: **L-meta-518 by Theorem 1.3** (checked on paper by the run's same-model
re-proof; the general bound it uses checked by me). The decisive concrete statement, `not HasCircuitSize 12 F 17`, has no
open fleet node of its own; it is an instance of open L-meta-519.

### Spot-check of the main new theorem (Theorem 1.1), recorded in the TSV beside this file

Targeted proof check of the full proof: Lemma 4.2 (read-once pair: after pushing negations to the leaves, side subtrees
on the two leaf-to-ancestor paths and above the ancestor must take neutral values, so the two-variable function is the
fixed operation at the ancestor); Lemma 4.3 (neighbours u != j of i and v != i of j exist by minimum degree, are
nonadjacent by no C4; the output on {i, j} is AND with all exterior inputs off and OR with u, v on; both pass through the
same unary map of the same read-once function; AND is neither OR nor its complement); Lemma 4.4 (a later-group input
cannot reach r, since its first branching wire would come at or before r; the singleton code c({u}) differs from c(empty)
whenever u has a remaining neighbour w, because F({u,w}) = 1 and F({w}) = 0; so all active vertices have equal later
neighbourhoods); Lemma 4.5 (two active twins with two common later neighbours form a C4); Lemma 3.2 (2(g - t) + t >=
n + g - 1 + b). No gap found. Computation (my own script, `scratchpad/intake25/theta_check.py`): the 18-gate witness agrees
with F on all 4096 inputs (3799 true rows, as the prompt states), a one-gate mutation fails on 278 rows; minimum degree 2,
13 edges, no C4, tau = 6 with the unique minimum cover {0,1,3,5,8,10}; n + tau - 1 = 17 and |E| + tau - 1 = 18; for
L-meta-518's graph |E| + tau - 1 = 14 (tau = 5).
