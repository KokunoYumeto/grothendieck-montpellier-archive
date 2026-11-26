# Intake of HODGE_DIVISION by diff: run A checkpoint 34, run B checkpoint 28

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747, the author of the division attack), 22 Nov 2026. Baseline:
part 3 (checkpoint 16 of run A). Seed, written first: `reports_20261122\paper_seeds\SEED_HODGE_DIVISION.md`. Check
events: `INTAKE_HODGE_DIVISION_20261122_cp34_CHECK_EVENTS.tsv`. Programs and outputs:
`reports_20261122\overnight_intake\HODGE_DIVISION\`.

## 0. The two folders

| | Run A | Run B |
|---|---|---|
| Folder in research_returns | `HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped` | `HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped` |
| Started (its own ledger) | 21 Nov 10:38:55 UTC | 21 Nov 10:36:29 UTC |
| Prompt | 46 | 46, then follow-up 46b (resumed 22 Nov 02:43:03 UTC after an inactive gap) |
| Newest here | checkpoint 34, 12:08:55 UTC, review 23 | checkpoint 28, 12:40:47 UTC, review 19 |
| State | active | active |
| Model | GPT-6 Astra (ChatGPT Pro mode) | GPT-6 Astra (ChatGPT Pro mode) |

**The checkpoint_28 folder is a second run of prompt 46, not an older checkpoint.** Both use ids of the same shape for
different statements. My parts 1–3 read run A only and did not know of run B.

**The filing mixed them.** Run A's `_from_earlier_checkpoints` chain contains run B's checkpoints of 12:06, 15:06, 16:36
and 21:07 UTC (their layout and README files are run B's). Anything keyed on "HODGE_DIVISION + checkpoint number" can
retire or overwrite the wrong run.

## 1. What I read, and what I did not

**By content (run A, 16 → 34).** The two manifests: 2,134 files added, none removed, 22 changed
(`diff_cp16_cp34.out`). Every proof file that the seed's explicit results use from run A has the same SHA-256 at
checkpoint 16 and 34: uniform_division, gaussian_fourfold, general_compensation, eisenstein_compensation, g34, g24, gf4,
quantitative_cm, sixfold, semiregular, imprimitive. Parts 1–2's comparisons with earlier checkpoints were not diffed.

**Read, run A:**
- research/uniform_division.tex in full; general_compensation.tex, the proofs of HD-COMP and COMP4;
- g34_section.tex 594–677; cm_lattice_transfer.tex 1–40 and 95–135; quantitative_cm_section.tex 1–62 and 720–760;
- the tex's abstract, scope and input list; the closing gate table (the two long rows cut at 1,500 characters);
- the 112 question rows added since Q5am, at state level, and the first lines of about 60 of the proved ones.

**Read, run B:**
- sections/gaussian.tex in full; extraction.tex 1–107; followup_exact_division.tex in full;
- followup_fixed_surface.tex 1–135, 249–262, 475–600; overview.tex 1–150;
- cm.tex and cm_effective.tex at statement, provenance and last arithmetic; all_fields_fourfolds.tex 1–70;
- the abstract; the first 40 question rows, cut at 260 characters; review 10's and the last review's gates, cut.

**Read, earlier returns:** GHOSTS sections/bounded.tex in full.

**Not read:** the new exclusion proofs of either run (Q2cl–Q2fz, Q5ap–Q5aw; HD-F1-T*, R*, S38–S40, I01–I05); the
G₃₄ proof 131–593; every sixfold proof; the E8 sections; the smoothing and conormal proof S05–S06; every cited paper
(Schoen 1988 pp. 11–12, 25 and 26 were opened on 21 Nov).

**Programs.** I ran none of the runs' code. `check_main_constants.py`, `diff_manifests.py` and `list_changed.py` are mine.

## 2. What is new

**Run A since checkpoint 16: no main gate closed and no new detector.** It has 112 new question rows: 80 proved,
30 refuted, 2 open. They are exclusions and finite parameter bounds for Q2i (monodromy of nonsplit sixfold suppliers)
and Q5i (an auxiliary RM-fourfold object). Its closing table says that the bridge from Q5i to a Weil eightfold (Q5au)
is unproved.

**Run B, new to us, and the strongest results we hold:**

| Id in run B | Statement | Verdict |
|---|---|---|
| HD-Q03 | δ_W ≤ 48 on even principal Gaussian fourfolds; c_t ≤ 141,557,760 δ⌈√T⌉ | confirmed given van Geemen 1996 (not opened) |
| HD-Q04 | odd principal: δ_W ≤ 192; c_t ≤ 2,264,924,160 δ⌈√T⌉ | confirmed |
| HD-D01, D02 | quadratic extraction; 61,440 δ⌈√T⌉D² for Q(i), n = 2 | confirmed; D02 recomputed |
| HD-F1-S07 | δ_W ≤ 36 on the principal Eisenstein component | quotient and descent confirmed; smoothing input not read |
| HD-F1-T05 | multiplier 3δ; c_t ≤ 17δ⌈√T⌉; 3W_Z algebraic | confirmed given S07's class; lattice recomputed |
| HD-F1-S02 | graphs of degree 8 at points with core index p^{4k} | degree and detection confirmed; the sequence not read |
| HD-N07–N10 | split sixfolds over the nine fields: 10^258 d^69 f^33 Δ⁶; all fourfold determinants | statements; Perry preprint as input |
| HD-R02, R03 | Gaussian sixfolds of class −3, explicit | statement |

**Stated here, joining the line: the reduction theorem (seed, "Main theorem").** The Hodge conjecture for all complex
abelian varieties ⟺ c_t bounded on the CM points of every special family ⟺ one degree bound, uniform over those CM
points, for cycles modulo infinitely many primes at each point. All inputs are published. The proof is in the seed. I
wrote it, so my reading is an author's check; it needs an independent check.

## 3. False or superseded in what we hold

**In the runs and their relation to us:**
1. **"2^324 d^57 Δ⁶" (run A, HD-CM6; also HD-U6's 2^661 and 2^658 forms) is not a moderate bound.** There d = 4mL² with
   L = lcm(1, …, 2^2048), about exp(2^2049). The statement is not false, since it says "d as in SF-QC01", but its
   appearance misleads. Run B's 10^258 d^69, with d the squarefree integer, replaces it.
2. **D₀(Q(i)) = 914,248,581,120 and 3,656,994,324,480** (attack §5; parts 1–2; HEXAGON_CANDIDATES H12 around line 223)
   are superseded by 48 and 192.
3. **D₀ = 132,269,760 for principal Eisenstein fourfolds** (GHOSTS R12; attack; H12) is superseded by 36.
4. **Run A's G₃₄ section still prints the fourth-power division bound** (lines 662–676). HD-U replaces it.

**In my own earlier work:**

5. **Attack §0 item 4 and Corollary O″.** "For n ≥ 5 the source must have imprimitive reflection monodromy" is false as
   stated: above the minimal number of branch points more non-reflections are allowed. "Curve sources reach only
   n ≤ 3" holds only for functorial one-copy sources, with hypotheses I did not state.
6. **Attack §0 item 3.** "Never by transport" rests on DEG_L B21 at statement level. Theorem E proves only bounded δ_W
   with unbounded core index.
7. **Attack §0 item 2, R4, §2.5, §5 Status.** The exponent 4, the norm fibre and "Schoen must be read" are stale. R2's
   last paragraph makes 032 look like an input of the abelian-variety equivalence; it is not. Its sentence "every Hodge
   class lies on such an (S,t)" had no proof; the seed has one.
8. **Bridge sketch 2.6.** It reads 032 Remark 8.5 as giving a CM lift on the same special subvariety. GHOSTS C02, from
   the source, refutes that.
9. **Part 2's input table** called the all-determinant Q(i) and Q(ω) fourfolds "published" inputs. They also rest on
   run proofs I had not read. H12's readiness on tests 1–2 for all determinants was therefore overstated; it stands for
   the principal families.
10. **Part 3** said that every new question row was read and that reviews 06–10 all recorded movement. I had seen most
    rows as id and state only, and read review 10 only. Several "statement level" events of parts 1–3 were
    question-row or ledger level.
11. **"Unchanged" without a diff.** HECKE_DIV part 2, THETA3 parts 2–4, SIGN_NEXT part 2 and HODGE_DIVISION part 3 said
    that earlier findings were unchanged without comparing content. For the run A files listed in section 1 this is now
    verified from 16 to 34; for the rest it is not.
12. **Event types.** SL-09 (HODGE_SIGN) and IF-03 (SIGN_NEXT) were computations, not independent re-proofs. GHOSTS C15
    was recorded as confirming a missing sign in Milne's report, which I never opened: open it before anyone writes
    to him.
13. **Schoen.** "S-a settled as printed" needs Lemma 2.6 and the proof of Theorem 2.0, which I did not read.

## 4. How it bears

- **Hodge conjecture for abelian varieties.** The reduction is a theorem with published inputs. What is missing is
  uniformity. 032, if correct, gives each value and no uniform bound.
- **Weil classes.** Split (2n+2)-folds give every determinant in dimension 2n (HD-COMP; Schoen's stabilization). So
  Q2i, both runs' nonsplit-sixfold gate, follows from split eightfolds over the same field. The detector question on
  split families of every n is the single gate for all Weil classes, and it is the seed's research question.
- **A proved lemma that opens a route** (seed, route 3): δ_W is bounded ⟺ the least m for which a complete intersection
  in |mθ| splits off a detecting component is bounded. Run B's 48 is the case m = 2.
- **In the project's terms.** Conditions A, C, I of cote 16 (scans 048–050): positivity inverts the Gram form, the
  projector is the algebraic inverse, and uniform condition A is what remains. Ghosts: finite complexity at every prime,
  unbounded along the primes.

## 5. Hexagon (register not edited)

| Candidate | Tests passed | Gate left |
|---|---|---|
| The reduction theorem (new; contains H12's dichotomy) | complete; self-contained; of interest | independent proof check of the seed's proof; literature search, Hexagon included |
| H12, principal Q(i) and Q(ω) fourfolds | complete for Q(i); checked given the sources | open van Geemen 1996; read HD-F1-S05–S06 and its sources for 36; search |
| H19, split Q(ω) eightfolds | group and rank recomputed | proof read of 131–593 in run A, or g34.tex in run B; the search |
| All-field bounds | — | not self-contained: Perry is a preprint |

## 6. For the prompts and the filing

1. Treat A and B as two runs in names, filing and check events. Repair the merged `_from_earlier_checkpoints`.
2. Before any push, remove the foreign files listed in the seed. Run B's `original_sources` holds 032, Markman,
   van Hoften–Sempliner, Milne's report and Alpöge's files.
3. The successor's main question is bounded detectors on split Weil families of every n. The auxiliary RM-fourfold
   exclusions and the monodromy catalogue have moved no gate since run A's checkpoint 16.
4. Attach the corrections of section 3 with the attack file, or correct the file first.
