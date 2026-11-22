# Full intake of RESEARCH_SA17 at checkpoint 12: the 221 statements no intake had checked

Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37), 21-22 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode), in
two parts: RESEARCH_SA17 (19 Nov, from 04:00 UTC) and RESEARCH_SA17_FINISH (from 13:06:58 UTC). The user asked for this
on 21 Nov at about 23:5x UTC: "I also want the full intake".

## 0. What was read, and how

- **The return.** `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped/RESEARCH_SA17/`.
- **The list.** The 221 ids of `field_experts/INTAKE_LEDGER.md` section 9, row RESEARCH_SA17:
  - 35 rows in Parts A, A.4, A.5, B and D;
  - 186 rows in Part C.
- **Earlier intakes of mine.** `INTAKE_RESEARCH_SA17_20261119.md` (checkpoint 02) and `INTAKE_RESEARCH_SA17_20261120.md` (checkpoint 12, the main
  rows).
- **The method.** For each id I read the statement and its proof in the return, using `x.py` in the work folder. That
  tool prints each statement and the opening of its proof; for the rows where I needed more, I read further into the
  proof. Recomputations were done by hand. No program of the return was run. No literature was opened in this pass,
  because my context guard stood above 70 %; citations are recorded as carried.
- **The record.** `INTAKE_RESEARCH_SA17_20261121_full_CHECK_EVENTS.tsv` has one event per id: 221 events, every id
  covered. Its columns are statement id, date, who, type and outcome.
- **The work folder.** `intake_RESEARCH_SA17_20261121_full/` holds `ids_221.txt`, `plan.tsv`, `ev.py`, `x.py` and
  `next.py`.
- **The work file.** `agent_notes/ac8bd2a26d00b4f37_NOTES.md`.

## 1. Counts by check type

| Type | Rows |
|---|---|
| targeted proof check, confirmed in full | 98 |
| targeted proof check, partly: the steps named in the outcome were checked, the rest of a long proof was not read | 75 |
| independent re-proof (recomputation by hand of the decisive identities, values or counterexamples) | 30 |
| carried as background without fault found (literature statements: B:NiceIV, B:positive-crystals, B:divided-target, C:field_WG_structure, C:canonical-tuples) | 5 |
| statement read only; not checked | 13 |
| **refuted** | **0** |

- **Read only at statement level (13).** Two are open-gate remarks with nothing to prove: C:allrings_gate and
  C:BO_general_gate. The other eleven are long effective-classification proofs or rows whose statement my reading pass
  did not display:
  - C:C1-henselization-WG, C:global-function-henselization-WG, C:henselian-global-coefficient-WG;
  - C:infinite-residue-henselian-arithmetic, -WG, -new-families;
  - C:perfect_Green_image;
  - C:separably-closed-coefficient-WG, -nonC1-family;
  - C:S3_isotypic_shallow_cancellation;
  - C:ramified-A2-MF-cancellation (I verified only its matrix identity).
- **Re-proved by recomputation (30):**
  - A5:fixed-projective-space; B:PD-bounds, B:PD-two-generator-rejected;
  - C:torsion_generic_kernel, C:normal_domain_counterexample, C:lambda_failure, C:char2_boundary;
  - C:odd_characteristic_failure, C:BO_positive_failure, C:Jordan_Adams_p, C:BO_field_lambda;
  - C:baseline-free-obstruction-example, C:C1_tower_example, C:S3_cyclic_detection, C:algebraic_fields_scalar;
  - C:artinian_algclosed_example, C:perfect-residue-Artin-reduction, C:Om-canonical-example,
    C:complete_unbounded_detection, C:three_cycle_length;
  - C:Om-finite-field-form-example, C:Om-finite-base-form-example, C:flat_nilpotent_kernel,
    C:function-field-constant-bound, C:hermitian_scalar_presentation;
  - C:divisible_nil_invariance, C:finite-ring-powers-scalar, C:valuation-domain-criterion, C:reduced_regular_fibres,
    C:shallow_tangent_quotient.

Together with the 43 events of 20 Nov and the cp02 events, every one of the 271 rows of the register now has a recorded
check event.

## 2. What was checked, by part

- **Part A: closed in full.**
  - The two rows my 20 Nov intake left open are now confirmed by targeted check:
    - A:comparison: Artinian bijectivity implies isomorphism, through adic limits and fpqc descent, without assuming
      noetherianity of the completed tensor square;
    - A:formal-gluing.
  - With them, the gluing step of A:pro7-representability and the base step of A:artinian-base are checked.
  - Also checked: A:local-to-global (under its two hypotheses), A:localiso-qc, A:hensel-adic-failure (the
    Artin-Schreier tower argument), A:hensel-L1-open, and the four abandoned open-relation lemmas.
  - The only step of Part A still carried is the étale equalizer theorem of de Jong-Olander, cited in
    A:hensel-remaining-gate.
- **A.4 and A.5.** A4:artinianflat, A4:flatclosure-scope and A4:boundary-gate are confirmed.
  - A5:fixed-projective-space is re-proved: the disjoint union of the E^r over the disjoint union of Spec k.
  - A5:correspondences: the insufficiency example is confirmed; the positive half rests on Conrad 3.2.1.
- **Part B: every row checked or carried.**
  - Re-proved: B:PD-bounds (the p-adic valuations of p^m/m!, and the non-nilpotence of the divided powers of 2 modulo
    4) and B:PD-two-generator-rejected (v_p C(p²,p) = 1 and the corner functional).
  - B:PD-not-QSyn is confirmed in detail. R* = k[a^{1/p^∞}, b^{1/p^∞}] ×_k k[c,d] is reduced and F-finite. It is not
    quasisyntomic: I/I² = J ⊕ J is not flat. It is PD torsion free, by the partial-Frobenius grading argument.
  - The closure table of B.3 (B:positive-closure, B:closure-reduction, B:largest-literature-class,
    B:positive-exclusion) is confirmed.
  - B:Delta and B:coLie-Dieudonne are confirmed, with a hand check on α_p.
- **Part C.**
  - **C.1: the regular-coherent answer stands.**
    - C:regular-coherent-criterion holds given the Schur-algebra lemma. That lemma, C:Schur-perfect-generation, is
      only partly checked: its inputs from Efimov and Krause are carried.
    - C:valuation-domain-criterion is re-proved: valuation domains are regular coherent by the Smith form.
    - Confirmed: C:squarezero_intrinsic_criterion (the determinant obstruction and divisible-nil invariance), C:DVR,
      C:regular_noetherian, C:regular_modular_locus, C:filtered_colimits and C:allrings_obstructions.
    - The counterexamples recomputed: C:torsion_generic_kernel, C:normal_domain_counterexample,
      C:flat_nilpotent_kernel and C:reduced_regular_fibres, together with the matrix identities of the node and
      cyclotomic rows.
    - C:derived_fibre_twins (T² = I recomputed) shows that two rings with the same rational fibre, the same reduction
      and the same K_0 data can differ on C.1.
  - **C.3: the λ-question is answered for every ring.** C:BO_affine_lambda: split WG(BO_m) over k (2 invertible) is a
    special λ-ring iff m ≤ 2 or k is a Q-algebra.
    - I recomputed the field case C:BO_field_lambda through C:Jordan_Adams_p:
      - ψ^p(V_j) = j·w^{j−1}, with w = V_p − V_{p−1} and w² = 1;
      - the defect is 4p·b_p(w−1) for m ≥ 4, and 2p(p−1)(w−1) for m = 3;
      - the run's program values 12, 40, 84 at p = 3, 5, 7 agree with 2p(p−1).
    - Necessity over a general k is base change to a residue field.
    - Sufficiency rests on Fasel-Haution 2025, Prop. 4.2.2 (carried) and on split = exact for m ≤ 2.
    - C:BO3_wild_gate shows that split WG(BO_3) in characteristic p contains the representations of a wild Schur
      algebra, and C:BO3_not_finitely_generated follows. So the remaining C.3 gate is a wild classification problem,
      not a missing computation.
    - Many of the effective-classification theorems (finite rings, algebraic extensions of finite fields, C₁ fields,
      henselisations, products, profinite rings) are checked in their structure: QSS radical reduction, henselian
      lifting, finite or compact enumeration. Their long algorithmic proofs were read only in part, as recorded.
  - **C.4.** C:baseline-free-realization is partly checked: the classical H³ obstruction.
    - C:baseline-free-obstruction-example is re-proved: o(1,1,1) = 2 in Z/4.
    - The four formal-group rows are confirmed in their proofs.

## 3. Refutations and corrections

**No statement was refuted.** No gap was found in any proof read in full.

Errata and points to correct:
1. **Our finishing prompt (B.3)** asked the run to put each base of B:base-kinds outside the union U. That list
   deliberately includes positive examples, so the request was wrong. The run declined it correctly, in
   B:positive-exclusion. The error was ours, in `pro_prompt_builds/RESEARCH_SA17_FINISH/PROMPT.md`, item B.3(ii).
2. **A possible erratum to the Stacks project.** The run says that the divided-power formula displayed in Stacks Example
   60.22.1 omits the term de·uv at p = 2.
   - On the detector of B:finite-PD the full formula is right: I rechecked it, and γ₂(u+v) = uv.
   - I did not open the Stacks example. A report to Stacks needs that check first.
3. **The cote 127 scan 3 reading.** The run now records it as we decided on 19 Nov (A45 opening): the ink has
   Γ(Y, O_Y), and the prime is the mathematical correction. Nothing further to correct.

## 4. What is new, for us

Checked here, and not found in the literature known to me; no new literature search was done in this pass:
- **B:PD-not-QSyn.** A reduced, F-finite, PD-torsion-free ring that is not quasisyntomic. It shows that the classes of
  Lau and of Anschütz-Le Bras do not nest, and it decides the closure table of the documented positive union.
- **C:BO_affine_lambda, C:BO_field_lambda and C:Jordan_Adams_p.** The complete answer to Grothendieck's λ-question for
  the split WG(BO_m) of cote 133 scan 6, over every ring. This answers L8 beyond characteristic 0.
- **C:BO3_wild_gate and C:BO3_not_finitely_generated.** In odd characteristic, WG(BO_3) is wild and not finitely
  generated even under all operations.
- **The C.1 answer for C:regular-coherent-criterion and C:valuation-domain-criterion.** For regular coherent rings,
  polynomial iff characteristic 0 and K₀ = Z. That covers valuation domains of any rank, and, for number rings, the
  condition is class number one.
- **The square-zero criteria and the node criterion.** For A ⋉ J over a characteristic-0 DVR: polynomial iff p is
  bijective on J (C:squarezero_intrinsic_criterion, C:ramified_squarezero_criterion,
  C:allprime_squarezero_criterion). Nodes xy = 2^n u over a dyadic DVR: polynomial iff n = 1.
- **C:derived_fibre_twins and C:fibre_invisible_kernel.** Fibrewise data do not decide C.1.

## 5. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

| Candidate | 1 Complete | 2 Self-contained | 3 Stable | 4 Checked | 5 Of interest now | Verdict |
|---|---|---|---|---|---|---|
| **The cote 131 theorem**: literal criterion false (A:main-counterexample), pro-modular correction proved (A:pro7-representability), L1 proved, L2 refuted | yes; the one carried step is the de Jong-Olander étale equalizer | inputs published (Murre 294, Stacks, de Jong-Olander); the de Jong-Olander locator still to be opened and checked | no successor planned; no literature search done | targeted checks on 20 and 22 Nov; no independent re-proof of the main counterexample yet | moderate: a Grothendieck statement of 1964/65 corrected, with its proof | **two gates away**: an independent re-proof or check of A:hensel-fpqc and A:hensel-remaining-gate, and a literature search |
| **Full faithfulness of crystalline Dieudonné fails** over F_p[x,y]/(x,y)² and two planes (B:crystal-counterexamples with B:finite-PD), and the closure table with B:PD-not-QSyn | yes | yes: Stacks, Lau, Anschütz-Le Bras, de Jong-Messing; locators not opened by me | the run's own search found no exact match, which we have not repeated | targeted checks plus independent re-proofs (B:finite-PD on 20 Nov, B:PD-two-generator-rejected today) | moderate for p-adic Hodge theory | **one gate away**: our own literature search; then read every page |
| **Split WG(BO_m) special iff m ≤ 2 or Q-algebra** (C:BO_affine_lambda, C:BO_field_lambda, C:Jordan_Adams_p, C:BO3_wild_gate) | yes | yes, with Zibrowius 2015, Fasel-Haution 2025, Bryant-Johnson 2011 and DEMN 1999 carried; locators to verify | final as an iff | targeted check plus my recomputation of the defects; the run's programs | niche: λ-structures on Grothendieck-Witt rings | **one gate away**: literature search (Fasel-Haution may contain the exact-group part) and source locators |
| **C.1 for regular coherent rings** (C:regular-coherent-criterion, C:valuation-domain-criterion) | rests on C:Schur-perfect-generation, only partly checked | inputs: Efimov and Krause on integral Schur algebras | final for this class | partly | modest: answers his scan-29 question for this class | **two gates away**: a full check of the Schur lemma, and a literature search |

None passes all five tests today, and none has a strong test 5. So nothing is flagged for immediate posting. The B.3
counterexample is the closest: one literature search away.

## 6. Bridges (the corrected criterion)

These are as in the 20 Nov intake, section 4. This pass found no row that uses RH, GRH or purity. The C.1 rows over
number rings read "class number one"; GRH for Dirichlet L-functions (Alpöge) adds only effective bounds there. The
λ-rows concern K₀ of representation categories, where the link carries nothing.
