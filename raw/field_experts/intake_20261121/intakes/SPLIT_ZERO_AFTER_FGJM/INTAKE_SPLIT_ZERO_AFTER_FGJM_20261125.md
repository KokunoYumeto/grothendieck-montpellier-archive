# Intake: SPLIT_ZERO_AFTER_FGJM (prompt 93), second run, checkpoint 10 → checkpoint 30

By Claude Opus 5.5 at effort high (agent a018e2d2), 25 Nov 2026, ~15:40–16:30 UTC. Asked for by the main session
(Claude Opus 5.5 at effort max), under the brief `agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`. The run is GPT-6
Astra (ChatGPT Pro mode); its records do not expose an effort setting. Checkpoint 30 was sealed 12:10 UTC, 25 Nov, and
the run is still going.

## 0. Baseline and scope

**Who checked what before.** `who_checked.py --source SPLIT_ZERO` lists 1,003 ids. Almost all of their events are the
run's own (GPT-6 Astra workers). Claude checks are few:
- a2fedc2a (Claude Fable 5.2 at effort max): FND-065, P5-SUPPORT-BALANCE and the h22 prose item;
- the AG_POLISH cluster reader (Claude Opus 5.5 at effort high): P2-032, assignment-bottom-fiber-zero, and the cp10
  items below.

**The pile** took the second run up to cp10 (`INTAKE_PILE_20261124/AG_POLISH.md`, §10 and "Follow-up 25 Nov").
- Paper 4 thm:threemissing: an exhaustive monotone-circuit search on small graphs.
- Paper 1 thm:canonical-ideal: the finite support test by hand.
- The K₁ question F3: the first run's universal nonsplitting is right, and the runs agree.

This intake takes in cp10 → cp30. cp10 itself is no longer on disk, so I worked from the run's CONTINUE.md snapshots
(new canonical statements per checkpoint), the REGISTER and the current papers.

**Papers at cp30:**

| Paper | Topic | Pages |
|---|---|---|
| 1 | projectives over inverse semirings, after FGJM and CFMM | 71 |
| 2 | quotient counts and sign-Tate zeta functions | 25 |
| 3 | boundary K-theory of semilocal adele spaces, after Connes–Consani | 20 |
| 4 | the edge-circuit conjecture at degree one | 49 at cp10 → 169 |
| 5 | lifts of Mulmuley's rank-three algebra, after Forsberg | 33 |

**Read in full:**
- the five abstracts;
- Paper 4 §1 (Thm main, twomissing, threemissing, oneaddition, twosumscomponents, maxfour, and the paragraph listing
  every four-witness proposition);
- prop:missing; prop:oneadditionall; the proof of thm:oneaddition; cor:fourresidualfinal with its proof;
- the CONTINUE.md current-state block (cp29 → cp30 statements SZ4-176 to 184);
- the REGISTER rows of all ids that no one outside the run had checked.

**Not read:** the proofs of the roughly 55 new SZ4 casework propositions, the Paper 1 C16 additions, and the Paper 2
and 5 proposition proofs. My context was above 80 %, and the user ranks P vs NP among the crowded lines.

## 1. Verdicts (my events; rubric types)

| Statement | Type | Outcome |
|---|---|---|
| SPLIT_ZERO_AFTER_FGJM:thm:oneaddition (Paper 4) | targeted proof check | **confirmed** (see below) |
| :prop:oneadditionall | targeted proof check | argument read in full, consistent; its input prop:oldfactors carried as background |
| :prop:missing | carried as background without fault found | it rests on lemmas lowerenvelope, lostgates and threelost, which I did not open |
| :cor:fourresidualfinal | carried as background without fault found | the bookkeeping of the (d, D, e) rows checked; the cited propositions not opened |
| :SZ4-176 … SZ4-184 and the other post-cp10 SZ4 rows | carried as background without fault found | statements only |
| :SZ1-C01-051 (Hurwitz defect values) | targeted proof check | **confirmed**: ζ(−m, a) = −B_{m+1}(a)/(m+1) gives D_t(−m) = [B_{m+1}(1+t) − B_{m+1}(1)]/(m+1), and D_t(0) = t |
| :SZ2-prop-\*, SZ3-034…036, SZ5-prop-\*, SZ1-C15-064, SZ1-C16-\*, SZG-\* | carried as background without fault found | REGISTER statements only |
| :GATE-ZP-001…012, SZ-NOV-\* | carried as background without fault found | unadmitted or open framework rows; nothing to check |

**Refuted:** none.

**thm:oneaddition, my check.**
- **Statement.** Let G be four-cycle-free, and let a positive circuit compute P ∈ Sup(G) with nonzero quadratic part.
  If canonical minimum-degree extraction deletes at most one addition, then |C| ≥ |E| + vc(G) − 1. Missing witnesses,
  retained counts and cover gain are unrestricted.
- **The derivation.** Write r for the number of missing witnesses and d = vc(G) − vc(H) ≤ r.
  - The retained circuit has at least |E(H)| + vc(H) − 1 gates, by the exact quadratic count.
  - prop:oneadditionall gives at least 2^r − 2 deleted products and one deleted addition.
  - For r ≥ 3, 2^r − 1 ≥ 2r ≥ r + d. This gives the bound.
  - r ≤ 3 is thm:threemissing.
- **Inside prop:oneadditionall.** I checked:
  - the single-cut structure, with homogeneity before the cut;
  - the private-product ancestor network, whose connected incidence count gives b ≤ p_g + 1 boundary forms;
  - the two cases, P = P₂ + cg (d = 2) and P = P₂ + gD (d = 1), with D supported in one H-neighbourhood.

  The 2^r bound then comes from prop:oldfactors, which I did not open.

## 2. What is new since cp10, against the pile

1. **Paper 4: the main growth (49 → 169 pp.).**
   - **New exact cases of the star bound |E| + vc − 1:**
     - one deleted addition, any number of missing witnesses (thm:oneaddition);
     - two deleted additions: every nontrivial missing component is K₂ or P₃ (thm:twosumscomponents);
     - four missing witnesses at cover gain 4 (thm:maxfour).
   - **The four-witness case is cut down to one row** (cor:fourresidualfinal): cover gain 3, six deleted gates, zero
     excess, exactly three products and three additions.
     - The outside graph is P₃ ⊔ 2K₂ or the remaining shape.
     - At least two cuts are visible.
     - SZ4-176 to 184 at cp30 exclude further templates in that row.
   - **The fleet's L-meta-608/612** therefore remain open only through this residual row, as far as the run's claims go.
     It is a long, same-model casework proof. Apart from my check of thm:oneaddition and the pile's small-case
     exhaustive search, no one outside the run has checked it.
2. **Paper 1** gained the C16 statements: projective classification under exchange, semiperfect and Jacobson
   conditions. They are background here.
3. **Papers 2, 3 and 5.** Only proposition-level additions or aliases (Hurwitz, Deitmar, fusion, monoid spectrum;
   rank-three table, adelic heights). Paper 3 is still 20 pp. The pile's F3 reconciliation stands.
4. **Framework rows** SZ-NOV-CC-REFINEMENT (a Connes–Consani refinement) and SZ-NOV-NONSTANDARD-RH-REALIZATION are
   explicitly unadmitted. They are not results.

## 3. Consequences for the waiting prompts Q03–Q11

None. The waiting prompts concern:
- anabelian sections (Q03);
- cote 57 Picard points (Q03b);
- Dérivateurs (Q04);
- La Longue Marche (Q05, Q06, Q09);
- Esquisse d'un programme (Q10);
- cote 100 finite normalization (Q11).

This run's mathematics (zero-adjoined inverse semirings, edge-function circuits, sign-Tate quotient counts) touches none
of them, so no sentence there becomes more precisely statable.

## 4. Posting candidates (by the user's priorities: P vs NP is crowded, so close up and publish)

1. **Paper 4, short form: "The star bound for edge-function circuits with at most three missing quadratic witnesses, or
   one deleted addition".**
   - It is self-contained up to the exact quadratic count.
   - **Needs:**
     - a different-model check of thm:threemissing and prop:oneadditionall with prop:oldfactors;
     - the run's final, since the four-witness casework is still moving;
     - a "Proof overview" section.
   - The 169-page casework should not be posted as it stands.
2. **Paper 3 (Connes–Consani boundary K-theory).** This is a Connes-programme item, which the user ranks among his
   priorities.
   - **Needs:** the two runs' records merged, with the first run's universal nonsplitting adopted (pile F3); a check of
     the first run's torsion claims (thm:all-torsion, thm:odd-torsion).
3. **Paper 5: the Mulmuley rank-three coefficient.** This is a correction e-mail, not a post. The draft
   `EMAIL_DRAFT_Mulmuley_20261124.md` is in this folder.
