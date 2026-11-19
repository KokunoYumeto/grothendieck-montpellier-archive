# First look at the four returns of 17 Nov 2026 (main session, Claude Opus 5.5 at effort max, 10:18 UTC)

The user, 17 Nov ~10:1x UTC: DER_FOLLOWUP, the anabelian follow-up and FINMON crashed out on account 3 (three at once
was too much), so their last checkpoints are their finals; S6_09_PAPERS is final. This note is the zip check: read
from each report and register, not an intake. The intakes (Claude Fable 5.2 at effort high) and the field experts
follow.

## ANABELIAN_A1, checkpoint 03 (final by the user's word; INCOMPLETE as a whole)
- Filed: longue_marche_pro_pilot_20261104/answers/ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped/.
- **A.1 is claimed proved after the full audit.** For every smooth proper geometrically connected curve of genus >= 2
  over every finite field, the point-section map is injective with the whole absolute Galois group and conjugacy by
  the whole geometric prime-to-p group, after every finite constant extension.
- A second [the user's words, omitted] proof removes the finite-exception input (Saïdi-Tamagawa's finiteness) from the final
  contradiction.
- The theorem extends to all hyperbolic curves over fields finitely generated over a finite field (A.33 for the affine
  genus 0 and 1 cases).
- The proof was split among independent auditors inside the run. K1-K6 are all proved.
- B7 is refuted by an explicit henselian field. B9 is proved: pro-reconstruction in characteristic zero.
- Open: A12, B1, B2, B4, B5, B6, B8.
- Register: 121 statements, 105 Proved, 8 Refuted, 1 Known, 7 Open.
- **Status:** the run's claim, checked only inside the run. Our second reader of the whole chain is still to come
  (the A1 expert, then a second reader before anything public).

## DER_FOLLOWUP, checkpoint 03 (final by the user's word)
- Filed: derivateurs_companion_20261109/pro_prompts_max_20261112_work/DER_FOLLOWUP/DER_FOLLOWUP_checkpoint_03_*_unzipped/.
- Register: 65 statements, 49 Proved, 10 Refuted, 6 Known.
- **The truncated-totality tower is strict at every level.** A_n(F_2) lies in Q_n and not in Q_{n+1}, with
  T_1 > Q_2 > T_2 > Q_3 > ... strictly. Totally W_n-dwyerienne sieves fail to compose for every finite n >= 2.
- Lead 6 is proved for every fundamental localizer: A is total for W exactly when BA is W-aspherical and every
  component of every action has a W-aspherical unreduced suspension.
- Part G (the weak localization axiom, XV-XVI): G.1 refuted for W-tilde itself; G.2 decided case by case, with
  repairs; G.3 proved; G.4's general lemma refuted.
- Still open: D.1's C_delta free-monoid subcase.

## FINMON, checkpoint 20 (final by the user's word; INCOMPLETE)
- Filed: .../FINMON/FINMON_checkpoint_20_20261117T0241Z_unzipped/, stored encoded. The report and results were decoded
  with SHA-256 checks into .../FINMON/FINMON_checkpoint_20_decoded_20261117/.
- The one unresolved item is C2: the least finite category with classifying space CP^2 has **17 <= arrows <= 22**.
  16 is now excluded in full (before, only 15 was).
- Complete for 17 arrows: the four-object case (215,194,501 corner tables; no survivors; an independent checker) and
  the two-object profiles with an opposite corner of order <= 4. The rest of 17 is not excluded.
- Register: 695 rows, 625 Proved, 12 Refuted, 1 Unresolved.

## S6_09_PAPERS, final (COMPLETE)
- Filed: s6_pro_prompts_20261112_work/returns/S6_09_PAPERS_final_20261117T0601Z_unzipped/.
- Three papers: I (530 pages; 348 inventory rows), II (659 pages; 313 rows) and III (1,004 pages; 523 rows). 1,184
  inventory rows in all, keeping all 745 rows of the runs.
- The report says every printed result has its complete proof, with credit, a clean LuaLaTeX build and visual
  selected-page checks. "No human has checked the mathematics."
- **Our PDF check, step 1 (the build logs):** overfull boxes 0 / 1 (0.9pt) / 0; none over 2pt. Step 2, rendering and
  looking at pages, is still to do.
- Before publication: paper_completeness_lint and the proof-check requirement (who checked which proof, and how).
- The report declines the prompt's wording that ChatGPT Pro mode has one universal highest effort, citing the
  official documentation; it keeps the Pro-mode designation. The user should see this.

## Added ~11:0x UTC: the A1 expert's second reading (provisional)
The A1 expert ab3f12f2 (Claude Fable 5.2 at effort max) stopped at the edge of its context, at about 963k of 1M.
Note: `EXPERT_A1_SECOND_READING_20261117.md`; its section 0 says where it stopped.
- **Provisional verdict:** on what it read, A.1 stands as stated for all primes other than p.
- **Sound, every step checked:** A.CF2 (AG.41: exactness with the cuspidal kernel made pro-r), A.CF3, A.CF4 (AG.42),
  A.CR1-A.CR2, A.CR4-A.CR5 and A.CR9.
- **The second proof is complete without Saïdi-Tamagawa's finiteness.** A.CR8 (elementary) puts all points with a
  p-primary partner over one proper subfield; A.CR7 (a Weil bound on the Kummer cover) needs only that.
- **K-items:** K2, K3, K4 and K6 are proved as posed. K1 is answered (Boxall's theorem used, not re-proved). K5 (the
  finite test by program) is not checked.
- **Not read:** A.CF5-A.CF12 (the audit form of AG.39, the finite tests), A.CR6 in the audit form, A.CR10-A.CR15, the
  root sections (A.R1 and A.33), B7, and the run's audits, code and paper.
- **Before anything public, a second reader checks:**
  1. A.CF1-A.CF2 line by line (the new exactness everything rests on);
  2. the SGA 1 statements behind A.CF3 and A.CF4, in the source;
  3. A.CR6;
  4. the final statement A.R1 against what is proved;
  5. the literature after 2017 on emptiness of the exceptional set.
