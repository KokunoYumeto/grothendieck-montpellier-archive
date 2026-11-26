# Intake: POLISH_CRISTAUX, from the cp18 intake to the run's final (prompt 92; 92b at cp18), 23 Nov 2026

> **Note added 24 Nov (same agent).** Thread B did not stop at cp18: its checkpoint 22 (21:45 UTC on 23 Nov) is taken in by `INTAKE_POLISH_CRISTAUX_20261124_threadB_cp22.md`. That intake supersedes section 5 below (the 92c changes) and the Paper 2 and Paper 9 board rows of section 6.

Intake by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb, a copy of ac8bd2a26d00b4f37), for the main session
329fb1e6 (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode). It does not expose its effort
setting, and its records say so. Its checks are all same-model, with no human check.
- Brief: `field_experts/intake_20261121/INTAKE_WAVE_20261123_EVENING.md` with `INTAKE_BRIEF_20261121.md`.
- Check events: `INTAKE_POLISH_CRISTAUX_20261123_final_CHECK_EVENTS.tsv` (19 rows).
- Work file: `agent_notes/a512cf71295c14ccb_NOTES.md`.
- My scripts are in my scratchpad folder `pc_final/`: mdiff.py, pdiff.py, ldiff.py, stm.py, ev.py, checks.py. Each ran
  with `python -I -B` against the return folders, never inside them.

## 0. Scope, and the main finding: the final comes from the other thread

**Returns read.** In `grothendieck_archive_transcription_20261110/research_returns/`:
- `POLISH_CRISTAUX_checkpoint_19_20261123T1804Z_unzipped`;
- `POLISH_CRISTAUX_final_20261123T1848Z_unzipped`;
- for comparison, checkpoints 13 and 18.

**cp19 against the final.** cp19 holds nothing that the final lacks (file-by-file comparison):
- no file is only in cp19;
- 629 files are only in the final: 627 audit files and two Paper 2 sections (`boundary_image_exclusion.tex`,
  `image_diagnostics.tex`);
- 29 files changed: the records, and the Paper 2 sources and PDF;
- Paper 2's STATEMENTS.tsv is identical in both.

So I read cp19 no further.

**The two threads.** The run split at checkpoint 13 (11:41 UTC) into two threads that never rejoined:

| | Thread 92 | Thread 92b |
|---|---|---|
| Prompt | the original prompt 92 | the continuation 92b (`SENT/92b_POLISH_CRISTAUX_continue_cp13/`) |
| Start after cp13 | its own review09 at 12:14 UTC | 13:58:55 UTC, from checkpoint 13 |
| Path after cp13 | reviews 12-15; saves of checkpoints 17 and 18 failed; checkpoint 19 saved 18:07:48 | checkpoints 16, 17, 18 |
| Last return filed | final sealed 18:48:55 UTC, after two consecutive no-movement reviews (review15, cutoff 18:05:09) | cp18 (17:44 UTC) |
| Papers | 18 papers, 461 pages | 21 papers |

What the comparison shows:
- The 92b block "Continuation from checkpoint 13" and "Checkpoint 14 delivered" appear in cp16, cp17 and cp18, but not
  in cp19 or the final.
- Only the final has "Scheduled review15".
- **The final therefore does not contain the 92b results** that my cp18 intake took in.
- No later 92b return is filed (7 POLISH_CRISTAUX returns in the folder at the end of this task). Whether that
  conversation is still running should be checked on the ChatGPT side.

**Statement ids per paper.** These come from the papers' own STATEMENTS.tsv files, parsed as quoted TSV. The parenthesis
gives cp13 / cp18 (92b) / final (92).

| Paper | Statements | What changed after cp13 |
|---|---|---|
| 1, 3-7, 11-16 | identical in all three | nothing |
| 2 | 114 / 133 / 114 | 92b registered 19 new ids. 92 has 41 new labelled results in its sources that its STATEMENTS.tsv (still cp13's) does not list. |
| 8 | 8 / 9 / 8 | 92b: thm:minrank. 92: thm:sections and five lemmas, not registered. |
| 9 | 7 / 19 / 7 | 92b: 12 new. The final's main.tex is byte-identical to cp13's (md5). |
| 10 | 33 / 36 / 41 | 92b: 3, the graph reformulation. 92: 8. |
| 17 | 14 / 14 / 14 | 92: a new auxiliary_lemmas.tex with 7 unregistered lemmas. |
| 18 | none / 12 / none | The final's Paper 18 is the Lubin-Tate paper (8 labelled results, no STATEMENTS.tsv). The 92b Papers 18 (12 ids), 19 (5), 20 (12) and 21 (9) are absent from the final; the final's Lubin-Tate paper corresponds to 92b's Paper 19. |

The final's root CHECK_EVENTS.tsv does hold the run's events for its unregistered statements. For example:
- thm:wild-bands-exact has 10 events;
- thm:first-boundary-normal-form has 3;
- Paper 18's thm:threshold has 2.

**What I read in this task.**
- In full:
  - the final README;
  - the final ledger's last blocks (review14 to the final seal);
  - Paper 9's thm:affine with the paragraph of its proof on the Monsky-Washnitzer side.
- At statement level:
  - final Paper 2: thm:wild-bands-exact, thm:mixed-all-indices, thm:all-index-upper, thm:first-boundary-normal-form,
    cor:boundary-nonsplit-cartan-image, thm:one-slope-all-indices and thm:full-supersingular-maximum, and the
    definition of the index (introduction.tex line 14);
  - final Paper 8: thm:sections and thm:surface;
  - final Paper 9: thm:proper and cor:elliptic;
  - the 8 new statements of final Paper 10;
  - final Paper 18: thm:tangent, thm:threshold, lem:necessity, cor:counterexample, prop:comparison;
  - from cp18: Paper 2's thm:wild-few-exceptions and thm:all-wild-bands, and Paper 9's thm:proper-integral-comparison
    and thm:rational;
  - the run's own events for the main statements.
- Not opened:
  - the proofs of Papers 2, 8, 10 and 18 beyond the passages named;
  - Papers 3-7 and 11-17 beyond the README;
  - the run's programs (not run);
  - any cited source.

## 1. The final as a posting candidate, paper by paper (usefulness first)

The run's own scope is in the README column of the final. Every one of its checks is same-model. "My check" lists only
events of this task, plus the earlier intakes' events where I say so.

| Paper (final) | What it is good for | My check | What still blocks posting |
|---|---|---|---|
| **18** Lubin-Tate lattices, 13 pp | **Answers Grothendieck's question on cote 8, sheet 49.** thm:tangent: alpha(A) = 0 for every finite K/Q_p. thm:threshold: the full de Rham and constant lattices agree iff e <= p, for any residue degree and Eisenstein equation, and also for the covariant duals. lem:necessity: valuation p - e for e > p. cor:counterexample: pi^(p+1) = p. | Statements compared with 92b's Paper 19, whose mechanism I checked at cp18 (targeted; a model other than the run's): consistent. The 13-page proof was not read. | (1) No STATEMENTS.tsv in the paper folder. (2) The converse exponent max(0, e - p) is stated only in 92b's 8-page version: merge the two. (3) A full proof check of the text to be posted by a model other than GPT-6 Astra. (4) Our own literature search (Lau's windows, Kisin-Ren, Pham). |
| **8** congruence sections and co-Lie realization, 14 pp | **Extends 8:81.** thm:sections: GL_d(Z/p^2) -> GL_d(F_p) splits iff d = 1 or (d, p) = (2,2), (2,3), (3,2); SL_d iff d = 1 or (2,3), (3,2); Sp_2g iff (g, p) = (1,3). thm:surface: every non-liftable V is realized on a smooth projective surface with non-split co-Lie complex, although [l] = 0 in K_0(S). Together they give 92b's least non-split ranks 4, 3, 2. | **Computation:** seven small cases of thm:sections by exhaustive lift search, all as stated. lem:transvection was re-proved at cp18 (92b text). | (1) thm:surface: proof not checked by me (outline only at cp18); needs a different-model check. (2) The table is classical, and the paper says so: exact locators for the attribution. (3) Six statements are not registered. (4) Merge 92b's thm:minrank as a corollary. |
| **2** full torsion and special inertia characters, 158 pp | **The SA15 inertia-character question.** thm:wild-bands-exact: nu_min(p, k p^r (p-1), 2) = r + 2 for 2 <= k <= (p^2-1)/2 with p not dividing k or k = p, and r + 3 for k divisible by p, k >= 2p. thm:mixed-all-indices: the mixed threshold e > p^(2n-3-v). thm:all-index-upper: nu_min <= ceil(log_p e). thm:first-boundary-normal-form: at k0 = (p^2+1)/2 an unequal pair has a forced normal form. cor:boundary-nonsplit-cartan-image: its image avoids the principal nonsplit Cartan. Further: Cartan and divisorial bounds, and the Liedtke-Matsumoto quotient. | **Computation:** the two threads' exact values agree on all 1,595 overlapping cases. thm:all-index-upper holds at every exact value. The v = 0 values equal the cp12 formula. k0 lies in 92b's exceptional set E_p. Proofs not read. | (1) The merge: 92b's 19 statements (thm:wild-few-exceptions: v + 2 for k <= p^2 outside E_p; cor:wild-next-family; two-slope patterns) are not in the final, and both threads proved overlapping results under different labels (section 2). (2) 41 labelled results are not in the paper's statement register. (3) A different-model check of the main chain, including the cp12 intake's open items (graph bound; mixed constructions). (4) The boundary index at k0 and k in E_p for v >= 1 are open; the boundary results are necessary conditions only. (5) Length: the cp12 intake's restructuring stands. |
| **9** weak-formal cohomology counterexamples, 10 pp (cp13 text) | **Grothendieck's weak-formal cohomology.** thm:affine: H^1(C, O) = 0 on A^1 and on G_m, while integral Monsky-Washnitzer H^1 has [x^(p-1)dx] != 0 with p[x^(p-1)dx] = 0, and H^1_MW(G_m) tensor K = K dx/x. thm:proper: H^1_et(X, F_p) = 0 implies H^1(C_X, O) = 0. cor:elliptic: y^2 z = x^3 - x z^2 over W(Fbar_3): the proper test fails even modulo torsion. | **Targeted proof check** of the Monsky-Washnitzer half of thm:affine (confirmed). **Targeted check** of the deduction of cor:elliptic from thm:proper: the curve is supersingular at 3. The site-side vanishing was not checked. | (1) The final has not changed this paper since cp13. 92b's version adds thm:proper-integral-comparison (H^1(C_X, O) is the limit of the infinitesimal H^1, hence of H^1_et(X, W_n(k)) for connected X over an algebraically closed field) and thm:rational (H^1(C_Gm, O[1/p]) = K). Both are consistent with the final's statements (statement level). Post the merged paper. (2) The weak Nakayama lemma (lem:finite) has only the run's targeted check. (3) A different-model check of lem:detect and thm:proper. |
| **10** mixed polarization indices, 42 pp | thm:eventual-all-mixed: eventual generic defect two (f_C = 9De^2 - 1) for every positive-index mixed pair over any algebraically closed field of characteristic two. Also thm:ample-difference, thm:finite-field (explicit range e > 1 + 4q^m/2^a), and thm:no-ordinary-index-zero-ample-class (a Picard-rank-one surface with no index-zero ample class). | **Independent re-proof** of lem:alpha-two-theta-descent. **Computation:** the genus arithmetic of thm:eventual-all-mixed (adjunction). Proofs of the theorems not read. | (1) A proof check of thm:eventual-all-mixed. (2) Open items named by the run: unclassified smaller degrees, quantitative bounds for arbitrary pairs, the uniform determinant. (3) Merge 92b's three graph statements (no new mathematics). |
| **1** integral crystalline weak Lefschetz | as in the cp12 intake | carried: the cp12 intake's targeted check of every step | A forward literature search. A different-model re-proof of the first-lattice lemma. Reconcile DEPOSIT.md (cp12 intake). |
| **3** stable exact sequence and unit-root count | as in the cp12 intake | carried (cp12 targeted check) | Settle known versus new (Ogus 1975; Katz-Messing): likely known in substance. |
| **4** abelian-scheme extension counterexample | as in the cp12 intake | carried (cp12 targeted check) | A literature search on the ring (Ferrand-Raynaud type) and a different-model check. |
| **5-7, 11-16** | README scopes | none (statement level) | A reading of each main theorem by a model other than the run's, and literature searches. |
| **17** sharp residues and hypersurface monodromy, 49 pp | README scope | none; 7 new auxiliary lemmas not read | Register the 7 lemmas; a different-model check. |

**Material of 92b (cp18) not in the final**, all taken in by my cp18 intake (events there):
- Paper 19 with the exponents;
- Paper 2's thm:wild-few-exceptions and its 18 companions;
- thm:minrank;
- Paper 9's comparison and its 11 companions;
- Paper 10's graph statements;
- Paper 18, invariant covectors, 12 ids;
- Paper 20, GL_8 and GL_80, 12 ids;
- Paper 21, 9 ids.

None of it was withdrawn: the final's thread never saw it.

**Counts of my check events in this task** (19 rows):
- 2 targeted proof checks, both confirmed;
- 1 independent re-proof;
- 8 computations, 3 of them records comparisons;
- 1 carried as background without fault found;
- 7 statement-level reads.

**No refutation.** Wherever the two threads state the same thing, they agree.

## 2. What is new against my cp18 intake

**Results of the final's thread that cp18 does not have:**
- **Paper 2:**
  - the exact bands extended to the half-square, including p | k;
  - the uniform upper bound nu_min <= ceil(log_p e) at every index;
  - one-slope recovery for n >= v_p(e) + 2;
  - the identity nu_min = max(nu_SS, ceil((1 + log_p e + v)/2));
  - the first-boundary package at k0 = (p^2+1)/2, r >= 1, n = r + 3:
    - the normal form z_1 = z_2 = ((p-1)/2) p^n with alpha_2/alpha_1 = -1;
    - split residual representations, with canonical lines exchanged;
    - point-field degrees p^2, p^4, p^6 at r = 1;
    - exclusion of the principal nonsplit Cartan image;
    - the Drinfeld-monomial full Cartan with e = f = p^(n-1);
    - the 6500/78000 indices at p = 5, n = 4;
    - the Liedtke-Matsumoto 2018 cyclic quotient as a warning.
- **Paper 8:** the classification table thm:sections with direct proofs, and thm:surface for every non-liftable V.
- **Paper 10:** eventual sharp rank for every mixed pair; the ample-difference and finite-field ranges; the
  Picard-rank-one example; the alpha_2 theta-descent lemma.
- **Paper 17:** seven auxiliary lemmas.
- **Paper 18:** the Lubin-Tate paper in its 13-page form, with covariant duals and the pi^(p+1) = p counterexample.

**Overlap between the threads.** The two threads proved the same results under different labels. The pairs below are
matched by title; I compared the statements of only the first two:

| Final (92) | cp18 (92b) |
|---|---|
| thm:wild-bands-exact | thm:all-wild-bands |
| thm:mixed-all-indices | thm:all-wild-mixed (same threshold) |
| thm:explicit-hesse-twelve | prop:explicit-defect-twelve |
| cor:three-first-level-table | cor:three-first-level-defects |
| cor:cyclotomic-full-p | cor:cyclotomic-full-p-exclusion |
| thm:one-slope-all-indices | thm:wild-one-slope-comparison and thm:wild-one-slope-pair |

**Against the literature:** I opened no source. The final cites:
- Lau, Kisin-Ren and Pham for Paper 18;
- the classical splitting results for Paper 8;
- Liedtke-Matsumoto 2018, Ex. 5.10, for Paper 2.

**Against our own results:**
- Paper 18 agrees with our correction at 8:50 and answers 8:49.
- Paper 8 agrees with our reading of 8:81.

**Withdrawn or refuted:** nothing.

## 3. Scope of the inputs

No statement of the final uses the Riemann hypothesis, GRH (Alpöge's theorem) or Masullo's draft.
- Papers 15-17 concern Frobenius and monodromy over finite fields of characteristic two; Paper 10 also works in
  characteristic two. None of them uses weights.
- Paper 18 uses Lau's window classification and the Lubin-Tate construction.

## 4. Integration (applied, with backups)

Backups are in `field_experts/intake_20261121/integration_backups/20261123/POLISH_CRISTAUX/`: the `*_before_final.md`
copies, taken before the edits of this task. The log is `INTEGRATION_POLISH_CRISTAUX_20261123.tsv`, rows 9-14.

**Applied:**
- `results_register/horizontal/sweep3/SA15/STUDY.md`: the block "Integration of POLISH_CRISTAUX, the final". It covers
  the two threads, what the final adds, the checks, and the index convention.
- `results_register/horizontal/sweep3/SA15/readings/c7_c8.md`: the block "Integration, the final of POLISH_CRISTAUX",
  on 8:49 (final Paper 18) and 8:81 (final Paper 8).
- `PRIMER_POLISH_CRISTAUX_20261123.md`: rewritten for the final, with my definition of nu_min corrected (section 9).
  The old version is in the backup folder.

**For the main session:**
- the merge prompt (section 5);
- the board rows of section 6;
- the fleet map of section 7.

The cp18 intake's two pending rows (the SA15 sort file at line 47; 162/216 in the successor prompts) still stand.

## 5. Prompt update: a successor that merges the two threads (for the main session)

1. **Inputs.** The final (thread 92) and cp18 (thread 92b), or 92b's own final if one comes back.
2. **One numbering.**
   - Papers 1-17 of the final.
   - Paper 18: final Paper 18 and 92b's Paper 19 as one paper. Keep the covariant duals, the counterexample and the
     exponents max(0, e - p) in both directions.
   - Papers 19-21: 92b's Papers 18, 20 and 21.
3. **Reconcile the overlapping papers.**
   - Paper 2: identify the duplicates of section 2, then register all 41 + 19 new results.
   - Paper 8: put thm:minrank as a corollary of thm:sections and thm:surface.
   - Paper 9: start from 92b's text, which contains the final's 7 statements, and finish its document QA.
   - Paper 10: the final's 8 statements and 92b's 3.
   - Regenerate every paper's STATEMENTS.tsv: Papers 2, 8 and 17 are stale and 18 is missing.
4. **Mathematics left**, under the push rule and the ledger rule:
   - the boundary k0 = (p^2+1)/2: existence or exclusion, and the sharp index;
   - k in E_p for v >= 1;
   - the remaining elementary divisors in the Lubin-Tate paper;
   - quantitative bounds in Paper 10;
   - general primitive and fixed-embedding monodromy (Papers 15, 17, 20).
5. **Rules.** The cp12 intake's prompt items still stand (Proof overview sections, 162/216, p not dividing e). Checkpoint
   ZIPs are lean, and CHECK_EVENTS.tsv carries the rubric types. `push_rule_pro_prompts.py --lint-math` must pass.

## 6. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`, for the main session)

These replace the cp18 intake's rows for Papers 19, 8 and 2, whose gate "the run's final" is now "the merge".

| title | statement | what it adds | gate left |
|---|---|---|---|
| Grothendieck's Lubin-Tate lattices agree exactly when e <= p | final Paper 18 thm:tangent and thm:threshold; 92b Paper 19 thm:main for the exponents max(0, e - p) | answers cote 8:49; alpha(A) = 0 for every finite K/Q_p; first unequal case pi^(p+1) = p | merge the two versions; a full check of the merged proof by a model other than GPT-6 Astra (mine covers the 92b mechanism); our literature search; a STATEMENTS.tsv |
| Sections of GL_d, SL_d, Sp_2g over Z/p^2 and their co-Lie realization | final Paper 8 thm:sections and thm:surface | the complete split table with direct proofs; every non-liftable representation realized on a surface with non-split co-Lie complex, although [l] = 0 in K_0; ranks 4, 3, 2 | a different-model check of thm:surface; locators for the classical table; register the six statements |
| Exact wild indices for the special inertia character, and the first boundary | final Paper 2 thm:wild-bands-exact, thm:mixed-all-indices, thm:all-index-upper, thm:first-boundary-normal-form; 92b thm:wild-few-exceptions | nu exact for every r and 2 <= k <= (p^2-1)/2; v + 2 up to p^2 outside E_p (92b); a forced normal form at k0 | the merge; a different-model check of the main chain; the boundary index (open); the statement register |
| Grothendieck's weak-formal H^1 fails both comparison tests, and what it computes | final Paper 9 thm:affine, thm:proper, cor:elliptic; 92b thm:proper-integral-comparison, thm:rational | the affine test fails integrally on A^1 and rationally on G_m; the proper test fails modulo torsion (y^2 = x^3 - x at 3); 92b: H^1(C_X, O) is the limit of H^1_et(X, W_n(k)) | the merge and 92b's document QA; a different-model check of the site-side proofs |
| Eventual defect two for every mixed abelian surface pair in characteristic two | final Paper 10 thm:eventual-all-mixed, thm:no-ordinary-index-zero-ample-class | removes the finite-field-model and index-zero hypotheses; a Picard-rank-one example | a proof check; the run's open quantitative items |
| (92b only) Full mod-2 monodromy GL_8 and GL_80 | 92b Paper 20 thm:main | as in the cp18 intake | the merge (not in the final); proofs read and certificates rerun independently |
| (carried) Integral crystalline weak Lefschetz fails | final Paper 1 | as in the cp12 intake | forward literature search; Proof overview; DEPOSIT fix |

## 7. For the P vs NP fleet: maps onto `pequalnp_work/fleet_map/PROOF_GRAPH.tsv` (constructed, not graded)

I did not reopen PROOF_GRAPH.tsv in this task. The node ids are those of the cp18 intake's map; I made no edit to the
fleet's files.

- **Section existence for G(Z/p^2) -> G(F_p)** (Paper 8 thm:sections).
  - Nodes: L-meta-683 and L-meta-685 (equations over finite fields of characteristic p).
  - Translation. Write the lifts of the generators of a presentation as X_i = g~_i (1 + p A_i), with A_i in M_d(F_p).
    Since p^2 = 0, every relator evaluates to 1 + p (C_w + a signed sum of conjugates of the A_i). A section therefore
    exists iff an affine-linear system over F_p is solvable. Its size is (number of relators) d^2 by (number of
    generators) d^2; it is the vanishing of the extension class in H^2(G, M_d(F_p)).
  - Both answers have short certificates: a solution, or a dual vector separating the constant term. My exhaustive
    search found the cheapest negative certificates: a generator with no lift of its own order (SL_2(Z/4); GL_2(Z/25)).
  - Work: record this as a library lemma: splitting is linear algebra, with certificates both ways.
- **Iterated Frobenius rank** (Paper 10 lem:stable-rank-open).
  - Node: none identified.
  - Translation: the stable rank is the rank of Phi^[g], a g-fold composite of Frobenius twists. Its entries have degree
    about p^g in the entries of Phi, but g twisted matrix products compute it: a small circuit for a high-degree
    polynomial map.
  - Work: if the fleet has a node on degree against circuit size, attach this as an example. Otherwise nothing.
- **Unchanged from the cp18 map:** the Singer-cycle certificates of 92b's Papers 20 and 21 (L-gct-006, L-lib-200), and the
  transvection identity (L-meta-683, L-meta-685).
- **Papers 2, 9 and 18:** no node.

## 8. Hexagon readiness

No candidate passes the five tests today:
- every proof check of the run is same-model;
- the two threads are not merged;
- the statement registers of Papers 2, 8, 17 and 18 do not cover their papers.

**Closest:** the Lubin-Tate paper. After the merge, the gates left are a different-model check of the merged text and
our literature search; my cp18 check of the 92b mechanism is the first different-model check. Paper 1 remains one gate
away, as before.

## 9. Errata of mine

1. **The primer's definition of the index.** The cp18 primer defined nu_min(p, e, 2) as "the least n such that an
   isomorphism of p^n-torsion forces equal characters". The paper's definition (introduction.tex line 14) is the least nu
   such that M[p^(nu+1)] determines the character, so nu = 2 refers to p^3-torsion. The values in the primer and in our
   STUDY.md were the paper's nu and stay as they were. The definition is corrected in the new primer, and STUDY.md now
   states the convention.
2. **The cp18 intake's gate "the run's final".** In its board rows this gate now reads "the merge": the final belongs
   to the other thread. A note at the head of the cp18 intake says so.
