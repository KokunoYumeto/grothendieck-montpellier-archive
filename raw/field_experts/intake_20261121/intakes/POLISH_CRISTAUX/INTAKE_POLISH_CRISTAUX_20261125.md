# Intake: POLISH_CRISTAUX (the 92c merge run), checkpoint 45, 25 Nov 2026

Intake by Claude Opus 5.5 at effort max (agent a512cf71295c14ccb), for the main session 329fb1e6 (Claude Opus 5.5 at
effort max), at the user's word (P9819).
- **The run.** GPT-6 Astra (ChatGPT Pro mode); it does not expose its effort setting. All of its checks are same-model,
  with no human check.
- **Brief.** `agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`.
- **Check events.** `INTAKE_POLISH_CRISTAUX_20261125_CHECK_EVENTS.tsv` (12 rows).
- **Scripts.** `INTAKE_POLISH_CRISTAUX_20261125_checks.py` in this folder. The scripts of my two earlier intakes are now
  here as well (section 2).

## 0. Scope

**Return.** `research_returns/POLISH_CRISTAUX_checkpoint_45_20261125T0643Z_unzipped/POLISH_CRISTAUX_checkpoint_45/`
(note the extra folder level).
- **Size.** 21 papers, 717 pages, 604 formal statements, 105 new labelled results.
- **The run is still active.** Review 16 at 06:42 UTC recorded movement, the no-movement streak is 0, checkpoint 46 was
  due at 07:26 and review 17 at 07:41. Later checkpoints may exist.
- **Numbering.** As in 92c (PAPER_NUMBERING.tsv):
  - Paper 18 = A18 + B19, the Lubin-Tate lattices;
  - Papers 19, 20, 21 = B18, B20, B21.

**What was already checked (step one).**
- **Paper 1.** who_checked and the board row P90a: thm:all-primes (surface part) with lem:curve, lem:eigen,
  prop:polarization and lem:roots were checked in full at cp34 by a018e2d2 (Claude Opus 5.5 at effort high), for
  hexagon:2611.00936v3. Paper 1's `main.tex` is word-for-word identical at cp33 and cp45, so that check stands at cp45.
- **The pile.** `reports_20261124/INTAKE_PILE_20261124/AG_POLISH.md` section 2 took in cp33 at statement level (all 58
  NEW_RESULTS rows).
- **This intake.** I take in cp33 to cp45:
  - 47 statements added: Paper 2 9, Paper 9 4, Paper 12 25, Paper 21 9;
  - 5 changed: Paper 9 thm:integral-rational-injection and thm:proper-finiteness; Paper 12 thm:main and
    prop:certificate; Paper 21 thm:hasse-inertia;
  - none removed;
  - the corrections recorded in the ledger since cp33.

**Read.**
- In full:
  - README, CONTINUATION_CURRENT.md and REVIEW_STATUS.md;
  - PAPER_NUMBERING.tsv;
  - the ledger lines on the two corrections;
  - Paper 9's new lemma `lem:integral-first-separated` with its whole proof (main.tex lines 956-1065).
- At statement level: every new or changed statement named in section 1.
- Not read: the proofs of the new Paper 2, 12 and 21 statements, and the programs (not run).

## 1. Verdicts (usefulness first)

| Statement (POLISH_CRISTAUX:id) | What it is good for | Verdict (my check in this task) |
|---|---|---|
| **paper9:thm:general-integral-finiteness.** For every smooth separated finite-type X over a perfect field, H^1(C_X, O) of Grothendieck's weak-formal site is finite free over W(k), of rank at most dim H^1_rig, and p-adically complete. No properness or lift is needed. | **Grothendieck's weak-formal cohomology, the archive's own theory.** Integral degree one is now a lattice in rigid H^1. This is AG built on the archive, the user's second priority. | **Targeted proof check of the deduction, confirmed**, given its lemmas below. |
| paper9:lem:integral-first-separated. The intersection of the p^n M is 0, and M injects into lim H^1(O/p^n). | The one new input. | **Targeted proof check, confirmed**, with three carried inputs: Meredith's affine acyclicity; the description of the rigid comparison by local forms and transition functions; the Caro-D'Addezio injection of rigid into convergent H^1. |
| paper9:lem:complete-dvr-finite-rank. Over a complete DVR, a torsion-free module of finite rank with zero intersection of the pi^n N is finite free. | Turns separation into finiteness. | **Independent re-proof** (dim N/piN <= rank; lift a basis; closedness of N_0 by completeness). |
| paper9:cor:coefficient-limit-cokernel. 0 -> H^1(O) -> lim H^1(O/p^n) -> T_p H^2(O) -> 0. | Locates exactly where the finite-coefficient comparison fails: in T_p H^2, which on A^1 is large by the cp22 H^2 torsion theorem. | **Independent re-proof.** |
| paper9:thm:integral-rational-injection and thm:proper-finiteness (both changed). | Hypotheses widened. | Statement read; consistent with the theorem above. |
| paper2:thm:all-power-multiplier-upper, thm:geometric-sum-multiplier-upper, cor:power-multiplier-consequences, cor:floor-log-character-recovery. Recovery by p^(v+r+1)-torsion for k <= p^r and for k <= 1+p+...+p^r; nu <= floor(log_p e) once (p-1)k > p^3. | The inertia-character index above the cubic band: v+3 <= nu <= v+4 on K_3 < k <= K_4. | **Computation**, consistency only: 2,209,104 cases, no conflict with the mixed lower bound or the cp33 exact bands. Proofs not read. |
| paper2:prop:exact3-all-wild, prop:defect12-minimum-all-levels, prop:cm-three-family. Full rational 3^n-torsion with additive potentially good reduction and defect m in {3, 6, 12}, by an explicit criterion; defect 12 at e = 2·9^(n-1) for every n; the CM curve y^2 + y = x^3 over F(E_0[3^n]), defect 6, e = 2·3^(2n-2). | Our 162/216 correction (cp12) is now a theorem at every level n. | **Computation.** The criterion's least e for defects 6 and 12 is 2·9^(n-1) (162 at n = 3), and 216 meets defect 12. The degree 3^(2n-2) is the full CM image. Proofs not read. |
| paper12: thm:main (now l up to 23), thm:full-support-stable-corank, thm:prime-{5,...,23}-stable-corank, thm:odd-very-ample-discriminant, and 20 more. | Frobenius ranks of curves in \|L\| on abelian surfaces in characteristic two. | **Computation**, arithmetic only: g = l + 1, a relative quotient of dimension l - 1, and stable rank n - 2. The discriminant degree 6N = 3L^2 for K = 0, e = 0. The stable-corank theorems are conditional on det N_s being irreducible. Proofs not read. |
| paper21: thm:ordinary-small-hasse (Hasse divisor irreducible for ordinary types (1,5), (1,7), with no global generation), thm:transvection-full-image, cor:full-image-reduction, thm:ordinary-prime-common-kernel, and 5 more. | Monodromy of Frobenius on sections of ordinary abelian surfaces. | Statement read only. |
| Paper 1 (unchanged since cp33) | The Kodaira and weak-Lefschetz failure in every characteristic, posted in hexagon:2611.00936v3. | **Carried as background without fault found**: a018e2d2's full check at cp34 stands. The run's "symmetric-dual correction" is to its own reconstruction record; the paper's conclusions are unchanged. |
| The run's refutation of `audit:paper2:wild-graph:eq18-unrestricted-preimage`, refined as `audit:paper2:three-branch-newton-preimage` | A supporting audit assertion (p = 3) that was false outside the torsion range. | **Computation:** the refined three-branch function is continuous at both breaks, and D = 6, H = 3, z = 10 gives 4, not 7/3. This is not rc-lem:newton (p >= 5), on which my cp22 check of the single-exception proof rests, so that check is unaffected. |

**Counts:**
- 2 targeted proof checks, both confirmed;
- 2 independent re-proofs;
- 5 computations, 1 of them a records comparison;
- 1 statement-level read;
- 2 carried.

**No refutation by me.**

## 2. What is new

**Against the pile** (INDEX.md and AG_POLISH.md, cp33):
- Paper 9 moved from "integral H^1 injects into rigid H^1" to **finite free, of rank at most rigid, for every smooth
  separated X, with no lift**. It also gained the exact cokernel T_p H^2 of the finite-coefficient comparison.
- Paper 2 gained upper bounds above the cubic band, and the exact-three classification at every level.
- Paper 12 gained degrees 5-23 of the every-coefficient stable corank, conditional on irreducibility.
- Paper 21 gained unconditional Hasse irreducibility for ordinary types (1,5) and (1,7), and a full-image criterion.

**Against the literature I know.**
- I know of no finiteness theorem for the integral weak-formal site. Integral Monsky-Washnitzer H^1 is not finitely
  generated: thread A's thm:affine shows torsion classes on A^1. The new theorem is about the site, and it uses only the
  rigid comparison and the Caro-D'Addezio injection as known inputs.
- Before posting, a search should cover Meredith 1972, Etesse, Le Stum's overconvergent site, and Caro-D'Addezio.
- The discriminant degree 6N is the classical 3L^2 count. Its validity in characteristic two (with one ordinary node)
  is the content of the theorem.

**Two corrections to the pile, for the main session.**
- `INDEX.md` G6 says Paper 1 was "Every step checked by a512cf71 (Claude Opus 5.5 at effort max)". That full check was
  the cp12 intake by ac8bd2a2 (Claude Opus 5.5 at effort high), and a018e2d2 (Claude Opus 5.5 at effort high) checked
  Thm 1.2 at cp34.
- GE-1's "a512cf71 targeted check of Thm 1.2 ranges" was likewise a018e2d2's. I made no check of Paper 1.

**The run's unlocated "1,595 grid".** The run records "the historical 1,595 common-input count remains unverified"
(REVIEW_STATUS; ledger). That number is mine: my final intake's script compared thread A's thm:wild-bands-exact with
thread B's thm:all-wild-bands and thm:wild-few-exceptions.
- Its range: p in {5, 7, 11, 13, 17}, r <= 4, 2 <= k <= p^2. A pair is counted where both threads assert an exact
  value.
- It is now `INTAKE_POLISH_CRISTAUX_20261123_final_checks.py` in this folder; rerun today, it gives 1,595, with 0
  mismatches.
- The run's own "1,597 source-supported" recovery uses another selection.
- If the main session sends a follow-up to the run, attach this script, and the run can close the item.

## 3. What it settles, and the waiting prompts Q03-Q11

**Settled.**
- Grothendieck's weak-formal cohomology in degree one is integrally finite, at the strength of the run's same-model
  proof and my check of its new steps (above).
- In Paper 2 the 162 correction is now a theorem at every level.
- Nothing of the archive's question list is newly decided beyond these.

**The waiting prompts** in `TO_SEND/PRO/1_Archive_research_by_topic/`: **none of Q03-Q11 changes.**
- **Q11 (cote 100, H037).** It attaches POLISH_CRISTAUX Paper 4 from checkpoint 34. Paper 4 is word-identical at cp45,
  so the sentence "Its closing remarks say that it does not classify the bases that are not normal, and that the case
  of a finite normalization needs a descent theorem of its own" stays exact.
- **Q03b (cote 57, H0A2).** Paper 1 is unchanged since cp33, so cp45 adds nothing to the sentence "Our runs report that
  the scheme-level statement ... already fails".
- **Q03, Q04, Q05, Q06, Q09 and Q10** do not touch this run's subjects.

## 4. Candidates for a Hexagon note

1. **Grothendieck's weak-formal H^1 is a finite free W-lattice in rigid H^1**, for every smooth separated X. With it:
   the cokernel T_p H^2 of the coefficient comparison, and the infinite K/W torsion in H^2(A^1) from cp22.
   - New input: Paper 9's three new statements.
   - Needs:
     - a different-model check of the three carried inputs, the Caro-D'Addezio injection opened at its locator
       (Theorem 3.2.1, p. 19, as the paper cites it);
     - the literature search above;
     - the run's final.

   It is the most useful new candidate: the archive's own cohomology, a clean statement, and a short chain.
2. **The complete next wild band for the special inertia character** (my cp22 board row), now with the upper bounds
   above the cubic band. Needs: a different-model check of the midpoint exclusions and of the three carried inputs of
   my cp22 check; the paper is 241 pages, so the note would be a cut-out.
3. **The Lubin-Tate lattices with all elementary divisors** (Paper 18; the pile read it at statement level). Needs: a
   different-model check of the elementary-divisor proof and of the 313-line foundation; our own literature search
   (Lau, Kisin-Ren, Pham).
4. **Paper 1.** Already in hexagon:2611.00936v3; nothing new.
