# Intake: POLISH_CRISTAUX, checkpoints 13 to 18 (prompts 92 and 92b), 23 Nov 2026, evening wave

> **Note added 23 Nov ~23 UTC (same agent).** Checkpoints 16-18 read here belong to the 92b continuation. The run's final (18:48 UTC) comes from the original prompt-92 thread, which also continued from checkpoint 13 and does not contain these results. Read `INTAKE_POLISH_CRISTAUX_20261123_final.md` sections 0 and 6. In the board rows below, the gate "the run's final" now reads "the merge".

Intake by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb, a copy of ac8bd2a26d00b4f37 cut after its RESEARCH_SA17
intake), for the main session 329fb1e6 (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode); it
does not expose its effort setting, and its records say so. Brief: `field_experts/intake_20261121/INTAKE_WAVE_20261123_EVENING.md`
with `INTAKE_BRIEF_20261121.md`. Work file: `agent_notes/a512cf71295c14ccb_NOTES.md`.

## 0. Scope (updated as the reading goes)

- **Returns.** `research_returns/POLISH_CRISTAUX_checkpoint_18_20261123T1744Z_unzipped/` (sealed 17:43 UTC), against
  the cp12 intake (`INTAKE_POLISH_CRISTAUX_20261123_cp12.md`, Claude Opus 5.5 at effort high). Checkpoints 13, 16 and 17
  were filed; 14 and 15 were not filed but are recorded in the cp18 ledger.
- **Prompts.** 92 (`SENT/92_POLISH_CRISTAUX/PROMPT.md`) and the continuation 92b (`SENT/92b_POLISH_CRISTAUX_continue_cp13/PROMPT.md`,
  sent 23 Nov; the continuation started 13:58:55 UTC from checkpoint 13).
- **The diff in one paragraph** (from the cp18 README and the ledger blocks after checkpoint 12, read in full):
  - four new papers: 18 (abelian hypersurface invariant covectors, characteristic two), 19 (Grothendieck's Lubin-Tate
    lattices), 20 (fixed supersingular hyperplane and cubic monodromy, full GL_8(F_2) and GL_80(F_2)), 21 (ordinary-product
    hyperplane and quadric monodromy, GL_8);
  - Paper 2 grew from 92 to 120 pages: all mixed wild thresholds and wild bands for every valuation, a uniform
    whole-supersingular bound, the exact (p^2-1)p^v family, one-slope recovery, a two-slope theorem, and a full-class
    index equal to v+2 outside an explicit finite exceptional set (normalised k <= p^2);
  - Paper 8: the least co-Lie obstruction ranks 4, 3, 2 in characteristics 2, 3, >= 5, with the GL/SL/Sp splitting
    classification checked at primary scope;
  - Paper 9: the proper integral H^1 comparison for Grothendieck's weak-formal cohomology over every perfect field, now
    without a connectedness assumption (document QA pending at cp18);
  - Paper 10: a graph reformulation of the determinant reduction (no movement credit, by the run's own rule);
  - register: 28 rows left NOT_YET_RECHECKED at Review09 (680 -> 679 at cp18); B-RD8 to B-RD11 compared.

- **What I read.**
  - In full: the cp18 README, the ledger from "Immutable checkpoint 13" to "Immutable checkpoint 18", and Paper 19
    (`workbench/papers/paper19/main.tex`) with every step of its main theorem.
  - Main statements and the decisive lemmas: Paper 8 (`paper8/main.tex`: lem:lift, lem:transvection, thm:minrank,
    thm:surface in outline).
  - Statement level: the 27 new Paper 2 statements (`paper2/STATEMENTS.tsv`, cp12 against cp18), with arithmetic
    consistency checks; the main theorems and abstracts of Papers 18, 20 and 21; Paper 9 from the README and ledger only.
  - Not opened: Papers 3-7 and 10-17 beyond the README rows (unchanged in substance since cp12 apart from the scope
    notes); the run's programs (not run); any cited source.
- **Also read first, as the coordinator asked:** my cp12 intake with its events and email drafts, and the S17a note
  (`reports_20261123/s17a_note/`: RECORDS.md, REVIEW_ac8bd2a2_v1.md, the statements of s17a_note.tex). The S17a note is
  RESEARCH_SA17 mathematics, not this run's; its open gate is unchanged: a second reader's re-proof, preferably by a
  different model.

## 1. Verdicts, with usefulness first

| Result (locator) | What it is good for | Check in this task |
|---|---|---|
| **Paper 19, thm:main**: for a Lubin-Tate formal O_K-module, the special Dieudonné lattice L_0 = M x_W O_K and the integral de Rham lattice L_1 agree iff e <= p; the least a with pi^a L_1 in L_0, and conversely, is max(0, e-p); their tangent images always agree (Grothendieck's alpha(A) = 0) | **Answers Grothendieck's question on cote 8, sheet 49** ("On peut se demander si ces sous-réseaux sont les mêmes"), and fixes his exponent of 8:50. For readers of integral p-adic Hodge theory of Lubin-Tate groups (Kisin-Ren, Pham) | **targeted proof check, confirmed** in its mechanism (exact valuation of the t^{e-1}-coefficient of z^b/t, no cancellation); **example p = 2, e = 3 recomputed** by hand. Lau's window classification carried |
| **Paper 8, thm:minrank**: the least rank of a local system M with non-split co-Lie complex of D(M) is 4, 3, 2 for p = 2, 3, >= 5, attained on smooth projective surfaces with full GL monodromy; below it the complex splits on every base | Extends our reading of **8:81** (his expectation fails in exactly three small cases) to a geometric realization; for readers of Illusie's co-Lie complex and the lifting of Galois/monodromy representations to Z/p^2 | **lem:transvection re-proved** (independent re-proof); lem:lift and the minimal-rank logic confirmed (targeted); the section list for small (p, d) carried; thm:surface read in outline |
| **Paper 2** (92 -> 120 pages): exact wild bands nu_min(p, p^v(p-1), 2) = v+1 and = v+2 for k = 2..p-1; a bracket at every wild index; nu_min(p, (p^2-1)p^v, 2) = v+2; the full-class index is v+2 for k <= p^2 outside an explicit exceptional set E_p of size (3p-5)/2 + floor((p-2)/3); the exact mixed threshold e > p^{2n-3-v}; first wild index nu_min(p, p(p-1), 2) = 2; explicit examples (y^2+y = x^3 over Q_3(zeta_3), defect 6) | Moves the **SA15 inertia-character question** (how much p-power torsion determines the special inertia character) from the tame/mixed range into the wild range, nearly to an exact answer | **computation**: |E_p| recounted; bracket and band values consistent; the explicit cubic's eight rational 3-torsion points recomputed. Proofs **not read** (statement level) |
| **Paper 20, thm:main**: full GL_8(F_2) and GL_80(F_2) mod-2 monodromy for degree 1 and 3 sections of the square of the supersingular cubic in its Segre embedding, over every perfect field | Answers, in the first fixed cases, Grothendieck's crystalline question on how Frobenius-stable cohomology of hypersurface sections varies | **computation** of genus 10, 82 and ranks 8, 80; proof and certificates not read or run |
| **Paper 21**: GL_8 on an ordinary open; F_2^96 x| GL_32 for the quadric system | same | **computation** of genus 10, 37 and ranks 8, 35, and of the stabilizer's shape; proof not read |
| **Paper 18**: invariant covectors of the relative unit-root system of abelian varieties: dimension 2^f - eps_A; zero for odd polarization | same | statement level |
| **Paper 9**: proper integral H^1 comparison for Grothendieck's weak-formal cohomology over every perfect field, without connectedness | Grothendieck's weak-formal cohomology | statement level (document QA pending in the run) |
| **Paper 10**: graph reformulation of the determinant reduction | none yet (no movement, by the run's rule) | statement level |

Counts of my check events (`INTAKE_POLISH_CRISTAUX_20261123_cp18_CHECK_EVENTS.tsv`, 12 events): 2 targeted proof checks
(confirmed), 1 independent re-proof, 6 computations, 3 statement-level reads (plus the cp12 intake's 21 events). **No
refutation.** Nothing the cp12 intake confirmed was withdrawn by the run.

## 2. What is new

- **Against the literature** (from the papers' own searches, which I did not repeat): Paper 19 cites Lubin-Tate, Lau,
  Kisin-Ren and Pham and claims no correction of a classification theorem; its theorem is a computation in a fixed
  normalization, new as an answer to the manuscript question. Paper 8 credits Godeaux-Serre (Serre's construction),
  Bergh-Rydh (the co-Lie formula) and ABM; what it adds is the surface statement with sharp ranks. Paper 2's wild
  bands extend Bondarko, Hattori, Smith and Ozeki-Yoshida as searched at cp12. Papers 18, 20, 21 cite Kantor's
  Singer-cycle theorem for the group step.
- **Against our own results:** Paper 8 agrees with our c7_c8 reading of 8:81 (three exceptional small cases). Paper 19
  agrees with our correction at 8:50 (the sign of alpha) and settles the size question we left open there.
- **Withdrawn or refuted since cp12:** none.

## 3. Scope of the inputs

No statement of this run uses the Riemann hypothesis, GRH (Alpöge) or Masullo's draft. Papers 18, 20, 21 and 15-17
concern Frobenius and monodromy over finite fields of characteristic two; their weights are not used.

## 4. Integration (applied, with backups in `field_experts/intake_20261121/integration_backups/20261123/POLISH_CRISTAUX/`)

The table is `INTEGRATION_POLISH_CRISTAUX_20261123.tsv` (7 rows: 3 applied, 4 for the main session).
- Applied:
  - `results_register/horizontal/sweep3/SA15/INTAKE_RESEARCH_SA15_20261120_part1.md`: a note under cor:B-RD27 that the
    least index for full rational 27-torsion is e = 162 (the cp12 intake's correction 1, which was never applied);
  - `results_register/horizontal/sweep3/SA15/readings/c7_c8.md`: an integration block for 8:49 (Paper 19) and 8:81
    (Paper 8);
  - `results_register/horizontal/sweep3/SA15/STUDY.md`: an integration block for checkpoints 13-18.
- For the main session: the SA15 sort file line 47 (162/216), the successor prompts (162/216 and "p does not divide e"),
  the Hexagon board rows of section 6, and the fleet map of section 7.

## 5. Prompt updates (for a successor of 92b)

Those of the cp12 intake still stand (restructure Paper 2 around its strongest theorems; "Proof overview" sections;
reconcile paper1/DEPOSIT.md; 162/216 and p not dividing e; normalize the event labels; the 679 rows still
NOT_YET_RECHECKED; different-model re-proofs of Paper 1's first-lattice lemma and Paper 2's graph bound and mixed
constructions). New:
1. Paper 2: settle the exceptional set E_p (existence and exact index for k in E_p when v >= 1) and the whole/whole
   two-slope branch at n = v+3.
2. Paper 19: the remaining elementary divisors of L_1 relative to L_0.
3. Papers 20/21: the general primitive and eventual fixed-embedding questions the run records as open; independent
   reruns of the GL_8 and GL_80 certificates by a different program.
4. Paper 9: finish the document QA of the component extension before it replaces the validated 25-page version.

## 6. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)

| title | statement | what it adds | gate left |
|---|---|---|---|
| Grothendieck's Lubin-Tate lattices agree exactly when e <= p | Paper 19 thm:main as in section 1 | answers cote 8:49; exact extremal exponents max(0, e-p); tangent exponent 0 | a different-model re-proof; our own literature search (Kisin-Ren, Pham, Lau); the run's final |
| The least non-split co-Lie rank is 4, 3, 2 | Paper 8 thm:minrank | sharp ranks and surface realization of the Z/p^2-lifting obstruction | full check of thm:surface; literature search (Bergh-Rydh, ABM); the run's final |
| Exact wild indices for the inertia-character question | Paper 2 thm:all-wild-bands, cor:wild-next-family, thm:wild-few-exceptions | the wild range nearly settled (exceptions explicit) | a full-chain check by a different model; E_p open; the run's final |
| Full mod-2 monodromy GL_8 and GL_80 for sections of the supersingular cubic square | Paper 20 thm:main | first exact full images in Grothendieck's hypersurface-section question | proofs read and certificates rerun independently; the run's final |
| (carried from cp12) Integral crystalline weak Lefschetz fails | Paper 1 | as in the cp12 intake | one gate away once the run ends (forward literature search, Proof overview, DEPOSIT fix) |

## 7. For the P vs NP fleet: maps onto `pequalnp_work/fleet_map/PROOF_GRAPH.tsv` (constructed, not graded)

None of these results is about complexity. The mappable pieces and the work that would complete each bridge:
- **Certified full images of finite matrix groups** (Papers 20, 21; the method: exact finite-field specializations
  plus Kantor's Singer-cycle theorem). Nearest nodes: L-gct-006 (orbit closure of the determinant; GCT uses symmetry
  groups of explicit polynomials) and L-lib-200 (finite affine geometry). Translation: "the monodromy group of an
  explicit family contains a Singer cycle and an element of a prescribed type, hence is all of GL_n(F_2)" is a
  stabilizer/symmetry-group certificate of the kind GCT needs for explicit polynomials. Work: add a node for symmetry
  groups of the fleet's explicit polynomials and test whether a Singer-cycle style certificate applies.
- **The lifting obstruction of GL_d(F_p)-representations to Z/p^2** (Paper 8, lem:transvection). Nearest nodes:
  L-meta-683 and L-meta-685 (equations over finite fields of characteristic p). Translation: the transvection
  computation sum T^i = (T-1)^{p-1} on End(V) is an explicit finite-field identity; it has no circuit content yet.
  Work: none proposed beyond recording the identity as a library lemma.
- **Papers 2, 9, 19:** no node; local fields and crystalline comparison have no counterpart in the graph.
- These edits to the fleet's files are for the main session; I made none.

## 8. Hexagon readiness

As in section 6: no candidate passes all five tests today. Paper 1 remains the closest (one gate once the run ends);
Paper 19 is the most self-contained of the new ones (8 pages, published inputs) and is two gates away.
