# Intake: POLISH_TOPOLOGY_PERIODS, checkpoint 12 to checkpoint 13 (23 Nov 2026, evening wave)

This intake is by agent a9e9559d (Claude Opus 5.5 at effort high), the field expert of this run. It wrote the cp12 intake and edited the S20 note, which is now posted as hexagon:2611.00937.

The run is GPT-6 Astra (ChatGPT Pro mode); its numerical effort is not exposed by the runtime. Checkpoint 13 was saved at 10:48 UTC. The ledger's last entry is at 10:42 UTC, and the hourly review due at 11:03 never came. The run looks stalled, and checkpoint 13 is probably its last. The continuation prompt 91b has been sent.

## 0. What I read and the scope

**Return:** `research_returns/POLISH_TOPOLOGY_PERIODS_checkpoint_13_20261123T1048Z_unzipped`. No newer checkpoint is filed: at 19:0x UTC only checkpoints 12 and 13 exist.

**Method: a diff against checkpoint 12.** A recursive tree diff gives 120 entries. Of the seven papers, only these changed:
- Paper 2: 61 lines.
- Paper 4: 293 diff lines, going from 33 to 40 pages.
- Paper 5: two sentences.

Papers 1, 3, 6 and 7 are byte-unchanged. Paper 7 gained only a scope inventory. CORRECTIONS_FOR_AUTHORS.md is unchanged.

**Read in full:**
- the Paper 2 diff, including the new paragraph "Parametrizations of one cone";
- `notes/paper02_collar_refined_statements.md` and `notes/paper02_collar_and_tor_root_release.md`;
- the new Paper 4 statements thm:collar-shape and prop:orange-limit, the latter with its proof;
- `notes/paper04_radius_integral_root_review.md`;
- the Paper 5 diff;
- the LITERATURE.md additions (Igusa 1984, the endpoint gate);
- the ledger entries after 10:04 UTC;
- QUESTIONS.tsv, status counts only.

**Read at statement level:** Paper 2 B082 (result-20), Paper 4 thm:radius-map and thm:radius-limit.

**Not read:** the run's separate frozen proofs of B082 and of the collar family; the Igusa scan.

## 1. Usefulness first

1. **Paper 2's cone convention.** It is good for anyone reading Grothendieck's Additif II c) literally. The space of rigidifications of a fixed cone is contractible only if the parametrizations fix the base pointwise. If they only carry the base onto itself, the space is equivalent to Homeo(Y): two components already for Y = S^0. This sharpens what "II c) is true" means; the 11-arrow outcome table is unchanged. For readers of the Additif and of stratified-space theory.
2. **B082, a universal Tor criterion** for unique coaddition and comultiplication of integer-valued polynomials, Ω(R,S), over an arbitrary unital ring inclusion. It answers Grothendieck's cote 153 question in full generality, and with the S20 note it gives commutative algebraists the complete test. For readers of Elliott's biring programme. The run accepted it after a separate frozen proof; I have not checked it.
3. **Paper 4: collars and radii.** Removing a collar from a hyperbolic surface with geodesic boundary is governed by Δu = e^{2u} − 1 with ∂_n u = k_g. Constant-width cuts lengthen the boundary by more than the cosh factor, but analytic cuts can make u change sign, so there is no pointwise monotonicity. The equal-length pant limit cap is an explicit lens of radius 4/(3√3). For readers of conformal surgery, grafting and Strebel differentials.
4. **Paper 5:** an independent incidence construction confirms every endpoint pairing. This strengthens the computation, but adds no new theorem.

## 2. Verdicts

| Item | Verdict (my checks; the full list is in the CHECK_EVENTS tsv) |
|---|---|
| Cone parametrization product: Par_set ≅ G_Y × Homeo_def(Y), with G_Y contractible | **Targeted proof check, confirmed.** a = h\|_Y, k = h∘C(a^{-1}) fixes Y pointwise, and h = k∘C(a). The bijection is simplicial. For Y = S^0 the identity and the reflection lie in different components. |
| A.105, A.109, A.111, A.112 under the literal base-setwise convention | **Refuted**, with the refined ids P02-A105/A109/A111/A112-normalized (base-fixed convention), in agreement with the run. The normalized statements were read at statement level only. |
| B082, the universal coefficient-syzygy criterion (result-20) | Statement read; carried as background. |
| Torus π_0, now cited to Igusa 1984 Thm 8.a.2 with dimension ≥ 6 (was ≥ 5) | Locator correction read; Igusa not opened by me. |
| S20 blocks (Thms 12.1-12.3, Cor 15.5) | Byte-identical to checkpoint 12; the cp12 check stands. Posted as hexagon:2611.00937. |
| Paper 4 thm:collar-shape, the equation clauses | **Targeted proof check, confirmed.** K' = e^{-2u}(K − Δu) gives Δu = e^{2u} − 1. k' = e^{-u}(k − ∂_n u) gives ∂_n u = k_g. Gauss-Bonnet gives the area −2πχ. The positivity, sign-change and numerical clauses were not checked. |
| Paper 4 prop:orange-limit (lens, R_0 = 4/(3√3)) | **Computation, confirmed.** \|U'(0)\| = 3√3/4 to 10^{-10}; \|U\| = 1 on the boundary and \|U\| < 1 inside. Script: `cp13_lens_conformal_radius.py`. |
| Paper 4 thm:radius-limit, the other two three-point cases | **Checked by hand.** One dominant length gives the slit domain C∖[1,∞), whose radius is 4 by Koebe. Two equal dominant lengths give the half-plane Re z < 1/2, whose radius is 1. |
| Paper 5 incidence gluing; Paper 7 inventory | Carried as background (the run's computations; no new statements). |

Counts for this checkpoint (12 events): 4 targeted proof checks, 1 used and rechecked, 1 computation, 1 refutation with refinement, 5 carried as background.

**The run's own state at checkpoint 13** (QUESTIONS.tsv, 1,028 rows):

| Status | Rows |
|---|---|
| proved (accepted at exact scope) | 364 |
| refuted, with refinement | 9 |
| scoped checks, final acceptance pending | 98 |
| unverified in the session | 557 |

The unverified rows by paper:

| Paper | Unverified rows |
|---|---|
| Paper 2 | 195 |
| Paper 3 | 52 |
| Paper 4 | 292 |
| Paper 7 | 18 |

Accepted rows went from 344 to 364, a net gain of 20. The new acceptances come from the collar family, B082, nine Paper 4 scopes and seven Paper 5 scopes; four rows became refutations with refinements.

## 3. What is new against the literature

- **Cone convention.** This is a precision about Grothendieck's own statement, not a literature result.
- **B082.** The run's LITERATURE.md compares it with Elliott (Birings and plethories, CIRM 2010, Thm 12, Prop 13) and with the 2026 Rethlas paper. A criterion that covers every unital inclusion appears new. Not checked by me.
- **Collar removal.** The PDE and Gauss-Bonnet are standard. The sign-change family and the fixed numerical example appear new. The run credits Fırat (the sphere potential), Liu and Strebel (the extremum), and Mondello (large-boundary limits, Thm 5.12, p. 666).
- **The lens radius.** It is an explicit computation inside Mondello's limit picture.

## 4. What of the run is finished, what is open, and what 91b must carry

**Finished.** Accepted by the run at exact scope, and checked by our intakes where noted.

| Paper | Finished parts |
|---|---|
| 1 | 73 of 74 statements. Thms 1.1 and 1.2 were checked by the cp12 intake. |
| 2 | The collar family under the base-fixed convention; the all-field PL/definable comparison A.160; B082; the Noetherian tensor criterion; Thm 12.2 (S20, posted). |
| 3 | The main dimension table, and the counterexample checked by the cp12 intake; 126 rows. |
| 4 | The single cap and the eigen counterexample (checked by the cp12 intake); the radius map and its image; 22 rows. |
| 5 | The ten main scopes and the genus formula (counting checked by the cp12 intake); 17 rows. |
| 6 | All 43 rows. |
| 7 | The finite interval theorem, event domains, oriented maquettes; 21 rows. |

**Open:**
- 557 unverified rows.
- Paper 1 B6.3 (a glyph).
- Paper 2: the King 1985 comparison (the source was never obtained); 195 rows.
- Paper 3: 52 rows.
- Paper 4: 292 rows; the nodal-q and abelian-fourfold inputs remain hypotheses; the four collar scopes await their worker comparison.
- Paper 5: C.06 (identity with Grothendieck's unspecified gluing).
- Paper 7: the Order 40 (2023) page of Jenča's Corollary 4.5; the contre/atelier bridge.
- Every paper: the HOW.md box 8 section headed "Proof overview".

**What 91b carries.** 91b (`TO_SEND/.../SENT/91b_POLISH_TOPOLOGY_PERIODS_continue_cp13/PROMPT.md`, read by grep) restarts from checkpoint 13 and carries the S20 literature into Paper 2.

**What 91b does not carry.** These go into the prompt that follows 91b's final return. They are logged in `claude_math_notes/PROMPT_UPDATES.md`, state "for the main session":
1. the "Proof overview" heading in every paper;
2. the six non-rubric event types in Paper 2;
3. the effort name in Paper 5's abstract;
4. the infinite-grafting literature (Gupta; Gupta-Mj; Dumas) for the single cap;
5. Jenča's Order page;
6. King 1985, and stating in Section 1 that the literal reading of II c) is false;
7. retitling the Elliott note in CORRECTIONS_FOR_AUTHORS.md as the resolution of a conjecture;
8. splitting Paper 3.

## 5. Integration, applied

The log is `INTEGRATION_POLISH_TOPOLOGY_PERIODS_20261123.tsv`. Backups are in `field_experts/intake_20261121/integration_backups/20261123/POLISH_TOPOLOGY_PERIODS/`.

**Applied: 9 edits in 9 files.**
- The seven `results_register/horizontal/sweep2/SA{07,09,10,11,20,21,22}/TOPIC_NOTES.md` files each received a section "Status after the third-sweep papers". These sections carry the cp12 intake's corrections to our own records (SA07 B.4.1; SA21 extension uniqueness and the Jenča credit; the SA22 67/091 hypotheses; the SA09 credits) and the cp13 changes.
- `reports_20261123/s20_note/RECORDS.md` received §6, after posting.
- `claude_math_notes/PROMPT_UPDATES.md` received the eight items above.

**For the main session:**
- the HEXAGON_BOARD rows below;
- the next prompt;
- the run's own source records under `research_returns` (not edited: they are returns).

## 6. Board candidates (rows for HEXAGON_BOARD.tsv; for the main session)

| id (proposed) | line | result | what it adds | gate left |
|---|---|---|---|---|
| S20 (update) | algebra | Posted as hexagon:2611.00937 | — | Independent re-proof of Thm 1 and a check of Cor 2 by another agent; the Elliott e-mail, on the user's word. |
| P91d | conformal | Removing a collar from a hyperbolic surface with geodesic boundary: the conformal factor solves Δu = e^{2u} − 1, ∂_n u = k_g; constant-width cuts make u > 0 and the new length exceeds L·cosh d; analytic cuts a_1 = 1 + ½cos(2πns/L_1) make u change sign; a fixed example on the (2π,2π,2π) pant | Shows that "cutting a collar shrinks the metric pointwise" fails | The positivity and sign-change proofs need a targeted check; literature (grafting and Fenchel-Nielsen deformation papers); a short note. |
| P91a, P91b, P91c (existing) | — | Unchanged by checkpoint 13 | — | Their cp12 gates stand. |
| P91e (weak) | topology | Grothendieck's II c) for a fixed cone, exactly: the base-fixed rigidifications form a contractible space, while the base-setwise ones are equivalent to Homeo(Y) | A correct reading of II c) | Too small for a post alone; it belongs in a paper on the Additif. |

## 7. For the P vs NP fleet (constructed, not graded)

**Map M1: Lemma 6 of the S20 note (the indicator power step) to node L-clb-033** (conjecture: Beigel-Tarui modulus-amplifying polynomials of degree 2k − 1 that turn 0/1 mod m into 0/1 mod m^k).
- **Translation.** In Lemma 6 we raise H to the power Q^m. This sends πV to π^{Q^m}V and 1 + πV to 1 + π^{m+1}V. For V = Z_p, Q = p it is the amplifier x ↦ x^{p^k}, which turns 0/1 mod p into 0/1 mod p^{k+1}, of degree p^k. That is exponential in k, where Beigel-Tarui have 2k − 1, and it uses that the modulus is a prime power.
- **Work to complete the bridge:**
  1. replace the power map by the Beigel-Tarui (Toda) polynomial of degree 2k − 1, and verify that the indicator construction of Lemma 6 survives with polynomial degree;
  2. state the resulting bound on the degree of integer-valued indicator polynomials of congruence classes mod p^N (the digit polynomial composed N times has degree Q^N; record the degree budget);
  3. the fleet would then consume "low-degree integer-valued polynomials for congruence indicators" as an input to ACC0-type representations (nodes L-clb-002, -009, -010).

No other result of this run maps onto the graph: tubes, collars, periods, conformal radii, oriented-matroid counting and posets have no current node.

## 8. Hexagon readiness

Unchanged from the cp12 intake, except:
- S20 is posted;
- P91d is a new candidate that is one targeted check and a literature search away from a note.

The run's stall does not change any gate.
