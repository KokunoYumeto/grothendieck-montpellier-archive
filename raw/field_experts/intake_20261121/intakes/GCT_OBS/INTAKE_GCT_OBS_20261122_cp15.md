# Intake of GCT_OBS (prompt 53), checkpoint 15, by diff from checkpoint 05

Intake of 22 November 2026 by Claude Opus 5.5 at effort high (agent a17221e5; launched by the main session, Claude Opus
5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode). Checkpoint 15 was created at 10:27 UTC on 22 November.
The run had not stopped: its review 9 (10:12 UTC) records movement.

## 0. Scope and method

- **Read from** `reports_20261122\overnight_intake\GCT_OBS_cp15\text\`, compared with checkpoint 05. The archive was
  not opened or unpacked.
- **Read, whole proofs:**
  - in GCT_OBS: S-001 to S-004, QC-014, QC-019 (slice bound, growth bound, scaling refinement), and S-025 as printed in
    `work/support_lmr/findings.tex`;
  - in GCT_KRON checkpoint 07, because Paper B rests on them: F-016's support proof, O-030, and the parts of F-024,
    A-030 and A-034 that my earlier intakes had left unread (section 1.4).
- **Read at statement level:** BR-002, BR-006 (with the first part of its proof), QC-021, and the changed rows of
  `QUESTIONS.tsv`, as far as printed by my diff and truncated there for some rows. Also the statements and opening
  lines of A-035 and A-036.
- **Not read:** the proofs of every other new or changed finding. They are listed with an automatic statement excerpt
  in `GCT_OBS_cp05_to_cp15_changed_findings.tsv` (beside this file). I read their ids and most of their titles only,
  and their check by this intake is **none**.
- **The diff's limit.** It compares the text of each TeX section headed by a finding id. A finding changed only in a
  script or certificate would not show. The TSV marks whether the file is included in the paper; provisional and
  duplicate fragments are marked `no`.
- **Code.** No code of the return was run. My programs and their outputs are in `checks\`; each took less than 30
  minutes.

## 1. Findings

### 1.1 What bears on H13, Paper B and the padded question

| id | statement | read | check received here | verdict |
|---|---|---|---|---|
| GCT_KRON O-030 (already in KRON cp07; in none of my intakes and not named in prompt 56) | n ≥ 3, R = n², u ≥ 0, a ≥ k ≥ 0, d = a + uR, Λ = (na + u(q+2) − k, 2u + k, (2u)^{R−2}) with q = R(n−2). Then K_n(Λ) = sk = g = h_n(k), and q_Λ ≥ Σ_{j=0}^{min(u,k)} h_n(k−j). The gap is strict for k = 1 or k ≥ 3 with u ≥ 1, and for k = 2 with u ≥ 2 | whole proof | targeted proof check; computation of the two-row identity for n ≤ 8, k ≤ 15 | confirmed. Uses F-002 and O-006 (binary forms are determinants), whose own sections I did not read |
| GCT_KRON F-016 = GCT_OBS S-001 | every coefficient c_α in a highest-weight vector of weight λ in Sym^d Sym^n has Σ_{i≥j} α_i ≤ λ_j | both proofs | targeted proof check | confirmed. The two proofs use the same flag-minor argument; S-001 is not a different route |
| GCT_OBS S-002 (since cp05 only the display of the definitions changed) | six explicit highest-weight functions P_0, ..., P_4, R are a basis of the ambient space at d = 12, λ = (19,7,2^5), n = 3 | whole proof | targeted proof check; my computations: a = 6 by cycle index and Murnaghan-Nakayama (3560 types); the raising operator kills all six; rank 6 on generic cubics | confirmed |
| GCT_OBS S-003 (unchanged since cp05) | a = 6, ideal multiplicity 1, K_3 = 5, q = 6; the separating equation is Ψ = 2P_0 + 21P_1 + 7P_2 + 35P_3 + 7P_4 | whole proof | targeted proof check; my computations: Ψ vanishes identically when f divides H; evaluation ranks 5 on det_3 and 6 on per_3 | confirmed on both sides. It needs neither F-016 nor the cited values of Landsberg-Manivel-Ressayre |
| GCT_OBS S-004 (unchanged since cp05) | with independent padding the row cap is m²+1. The BIP-range conditions stand, except that M-019's threshold becomes λ_2 ≥ 238356708; 239063403 holds only for r ≤ m² | whole proof | targeted proof check of the argument given; my exact integer check of both thresholds and of the 171 A-025 cases | confirmed, conditional on F-009, M-008, M-013, M-014, M-019 and A-025, of which I have read only M-013 |
| GCT_OBS QC-014 (new) | ℓ^{n−4}q ∈ D_{n,4} for every quaternary quartic q and n ≥ 7. So q_λ ≤ K_n(λ) in every degree, for every λ with at most four rows, at (4, n), n ≥ 7 | whole proof | targeted proof check; my symbolic check of det M = z³Φ and Jacobian rank 35 at a point of my own | confirmed. The nonvacuity value 576((n−3)!)^4 was not recomputed |
| GCT_OBS QC-019, upper bound (new) | K_9(9d−3b, b, b, b) ≤ C(3b+151, 151) | whole proof | targeted proof check; my tangent rank 92, slice dimension 151 | confirmed |
| GCT_OBS S-025 and the QC-019 scaling refinement (new) | 155, respectively 156, algebraically independent padded functions of degree 27 and weight λ_0 = (216,9,9,9), so q(sλ_0) ≥ C(s+155, 155) | proof text as cited | carried as background without fault found | the argument is sound as printed; the Jacobian certificate (minor 13 mod 101) was not recomputed |
| GCT_OBS QC-019, consequence (new) | for z·per_8 against det_9, q(sλ_0) > K_9(sλ_0) at s = 67·28^38, d = 27s | whole proof | targeted proof check; my exact integer comparison (the least s at which these two bounds separate also has 57 digits) | confirmed, conditional on the 156-function certificate and on c_8 = 165 (recomputed in my CUE_GCT intake) |
| GCT_OBS QC-021 (new) | I(D_{n,r})_d = 0 for n ≥ 6 and d ≤ 10 | statement | carried as background without fault found | not checked; it rests on a published degree-five seed that the run did not rerun |
| GCT_OBS OBS-011 to 016, QC-015 to 018, QC-020, QC-026 to 029, S-026, S-028 (new) | complete determinant restrictions in listed degree and tail boxes at (8,9) and (17,23) | QUESTIONS rows and titles | none | not checked |
| GCT_OBS QC-022 to 025, S-023, S-024, S-029 to S-037 (new) | upper-bound routes refuted, null pencils, semistable centres, arc constraints | QUESTIONS rows and titles | none | not checked |

**The state of the padded main question (Q1a, Q1b).** Both are open at their requested strength (a reachable degree and
an explicit separator). As the run records it, without a check by me:
- At (8,9), complete restriction K = a holds in the boxes proved so far. A four-row obstruction there needs second row
  ≥ 15; third row ≥ 12 if the second is 15 or 16; third row ≥ 7 if the second is 17 to 27.
- At (17,23), a four-row obstruction needs second row ≥ 20, among further conditions.
- QC-019 gives a named weight and degree at which an obstruction exists at (8,9), in a degree of 59 digits. It gives
  no equation. CUE_GCT G-11, G-13 and G-17 already gave explicit labels with astronomically large bounds, at statement
  level for us. QC-019 is a much shorter proof with a much smaller bound.

### 1.2 Border rank and everything else

| id | statement | read | check received here | verdict |
|---|---|---|---|---|
| BR-002 (unchanged since cp05) | BR(det_4), BR(per_4) ≥ 43 in every characteristic | statement | carried as background without fault found | not checked |
| BR-006 (unchanged since cp05; only the count in its QUESTIONS row moved) | μ_10 ≥ 18 for det, so BR(det_4) ≥ 44 in characteristic 0 | statement, first part of the proof | carried as background without fault found | not checked; it is not new in cp15 |
| BR-013 to 027, 029 to 031, 034, 036, 038, 040, 041, 043, 046, 050, 057 (new); BR-012 (changed) | exclusions of permanent ten-plane orbits: 10 orbits (6,048 subsets) remain | README, QUESTIONS | none | not checked; moving |
| S-006, S-012, QC-013 (changed); S-013 to S-022, S-027 (new) | finite certificates and relaxations for nonic families | titles | none | not checked |

### 1.3 Effect on the named findings

| finding | effect |
|---|---|
| A-030 | **Not contradicted; generalized by O-030** (it is u = a = k = 1). Its padding paragraph holds for independent z as well, since m²+1 < n². |
| A-034 | **Not contradicted; strengthened by O-030** (it is u = a = k = s). |
| A-035 | **Not contradicted; its padding scope is restated by S-004.** The basic exclusion survives independent padding, since r ≤ m²+1 < n². The stronger statement, coverage of every relevant binary coefficient algebra by the r ≤ 2n injection, needs m²+1 ≤ 2n in place of m² ≤ 2n. I have not read the proof of A-035. |
| A-036 | **Not contradicted.** Its range r < n² contains r ≤ m²+1. It is a lower bound on the determinant for one algebra's copies and compares no other copy. QC-014, S-004 and GCT_OBS's scope paragraph say nothing stronger about it. I have not read its proof. |
| F-016 | **Already proved in GCT_KRON cp07** (`GCT_KRON.tex`, from line 15823), and again in S-001. My earlier statement that it had no written proof was false. |
| F-024 | **Unchanged and confirmed.** I have now read its proof to the end: the character identity with orbit count 4 − 2 − 2 + 1 = 1. |
| F-025 | **The q = 6 > K = 5 example is strengthened by S-002 and S-003:** explicit basis, explicit equation, both sides computed. Its general statement (q = a for at most seven rows and λ_3 ≤ 2) is not replaced by them. |

### 1.4 Faults found in our own records (mine)

1. **F-016.** My GCT_KRON part 3 (section 6) and `CORE_53_GCT_OBS.md` said that F-016 was not written as a numbered
   finding with a full proof. It was. I had not looked for it. The run corrected this.
2. **Extent of reading.**
   - My GCT_KRON part 2 said A-030 was read in full. Its last part was unread: (A-030.12), (A-030.13), (A-030.15),
     (A-030.16) and the padding paragraph.
   - My part 3 said the same of A-034, whose last lines were unread, and it used (A-030.13) and (A-030.15) without my
     having read their proofs.
   - I have read all of these now and found no gap. The verdicts stand; the records of 21 November overstated the
     reading.
3. **Check type.** These events of mine are computations, and I recorded them as "independent re-proof":
   - BR_PENCIL R-04, R-05 (part 1);
   - BR_PENCIL R-08, R-10 (part 2);
   - NEG_NIGHT A001, A017.

   Their type should be "computation or formal certificate". The word "re-proof" in those intakes and in my summaries
   of them should go the same way.
4. **O-030 was missed.** It was in the KRON checkpoint that my part 3 took in as final, and that intake does not list
   it. This is why prompt 56 states B1 in the weaker form.
5. **Return code run unread.** In earlier rounds I ran the BR_PENCIL verifiers and the NEG_NIGHT checkers from copies,
   having read only the start of some of them and not their imports. Those PASS events say only that the return's
   programs ran and printed PASS.

I did not edit those files: they are outside this task's folder. They need a dated correction, and the check events of
point 3 a correcting row.

### 1.5 Faults or limits found in the return

- S-001 calls itself an independent complete proof. It is a complete proof by the argument F-016 already used.
- Q-BR10-EXACT was labelled `proved` in cp05 while its own text said that the exact value was unresolved. Checkpoint 15
  labels it open. No bound was withdrawn.
- Review 8 miscounted the open rows (31 for 23). The run corrected this and says so.
- S-025's heading in the geometric part reads "an actual graded multiplicity gap". The strict gap needs QC-019's upper
  bound as well; S-025 alone proves the lower bound, as its own text says.
- I found no false step in the proofs I read.

## 2. For the follow-up to prompt 56

### 2.1 Stable: add or change

**B1. Replace the ray by the three-parameter family.**
- *Statement.* GCT_KRON O-030, with the hypotheses in 1.1. For fixed n ≥ 3 and every u, a ≥ 1,
  Λ(u,a,1) is an occurrence obstruction (K_n = 0 < q), and for μ = Λ(u,a,1) and every s ≥ 1,
  q(sμ) ≥ p_n(s) > h_n(s) = K_n(sμ). A-030 and A-034 become the case u = a = 1.
- *Lemmas to prove in the paper.* F-002 (two-row rectangular Kronecker numbers), O-006 (binary restriction), the
  nonvanishing of H_0, and A-034's valuation lemma with (A-030.13). F-024 stays for the ambient multiplicity one at
  Λ(1,1,1); O-030's inequality does not need it.
- *Check level.* Targeted proof check, with a computation of the two-row identity. No independent re-proof.
- *Limits to keep.* No equality on the permanent side outside u = 0. No gap is asserted at k = 0, at u = 0, or at
  k = 2 with u = 1. Every member with u > 0 has n² rows.
- *Files.* Already attached: `GCT_KRON/`, in `GCT_KRON.tex` the section O-030 (lines 9423-9764 of cp07) and
  `agents/obstructions/hessian_shift_multiplicity_family.tex`.

**B2. Give both sides by explicit functions.**
- *Statement.* GCT_OBS S-002 and S-003: the basis P_0, ..., P_4, R; the equation Ψ; a = 6, K_3 = 5, q = 6.
- *Proof.* f divides H on seven-variable determinant pencils, since the Hessian of det_3 has rank six at a matrix of
  rank two. That gives K ≤ 5; the evaluation minors give K ≥ 5 and q = 6.
- *The citation.* Landsberg-Manivel-Ressayre, p. 476, is then cited for the determinant-side numbers as known and is
  no longer an input.
- *F-016.* The instruction to write it out is no longer needed for this example. Keep it as a numbered lemma only if
  F-025's general statement is included, and take the proof from F-016 or S-001.
- *Check level.* Targeted proof check, with computations by a second implementation of mine on both sides.
- *Novelty.* The determinant side is published. The paper must say exactly which of "six ambient copies, one in the
  ideal, six on the permanent" Landsberg-Manivel-Ressayre already print.
- *Files to attach.*
  - `work/support_lmr/findings.tex` (S-001 to S-004 are lines 1-468);
  - `work/support_lmr/scripts/check_lmr_ambient.py` and `verify_lmr_explicit.py`, with every module they import;
  - `work/support_lmr/results/lmr_explicit.json`;
  - this intake's `checks/cp15_checks.py`, `checks/cp15_psi_identity.py` and their outputs.

**B3. Fix the padding convention and state it.**
- *Two conventions.* Internal padding x_11^{n−m} per_m has r ≤ m² essential variables. Independent padding
  z^{n−m} per_m has r ≤ m²+1.
- *B1 under padding.* For m < n both caps are below n², so every O-030 member with u > 0 has q = 0 under either
  padding.
- *A-035.* Its basic exclusion holds under both. Its all-binary-algebra corollary needs m² ≤ 2n, respectively
  m²+1 ≤ 2n.
- *A-036.* It holds for 3 ≤ r < n² and speaks of its algebra's copies only. Prove both A-035 and A-036: our intakes
  have their statements only.
- *BIP and IP.* Their thresholds n ≥ m^25 and n > 3m^4 exclude n = m. State which padding each uses.
- *M-019.* If any GCT_KRON necessary condition is quoted, use S-004: 238356708 for independent padding, 239063403
  only for r ≤ m².
- *Files to attach.* S-004 in the same `findings.tex`; `work/support_lmr/scripts/check_external_padding_bounds.py`
  with its imports; `work/support_lmr/dependencies.tsv`; this intake's `checks/s004_thresholds.py` and its output.

**Optional for the main session to decide, stable but outside B1-B3: QC-014.** At (m,n) = (4, n), n ≥ 7, there is no
multiplicity obstruction with at most four rows, in any degree. It would sharpen B3's account of padding. It is a
statement about padding, and prompt 56 says "claim nothing about padded obstructions", so adding it changes that
prompt's scope. Files: `work/quaternary/quartic_padding_containment.tex`, its checker
`work/quaternary/scripts/check_quartic_abp_padding.py`, and from the archive
`work/quaternary/results/quartic_abp_padding.json`.

### 2.2 Moving: do not put into prompt 56

- QC-019 and S-025, the weight and degree for (8,9). The theorem is complete as written, but its lower bound rests on a
  certificate we have not recomputed, the run is sharpening it, and it belongs to H14, outside Paper B.
- Every box and inventory at (8,9) and (17,23), the null-pencil and arc results, and the count of 4,214 remaining
  labels.
- QC-021, until its published seed and its proof are read.
- The permanent 44 gate (10 orbits). BR-002 and BR-006 look stable and belong to a border-rank paper (H03), once an
  intake has checked them.
- Any wording that a padded separator or equation has been found: none has.

## 3. What to keep

Nothing was deleted. The file-by-file classification is `GCT_OBS_cp15_keep_audit.tsv`, the one by folder
`GCT_OBS_cp15_keep_by_folder.tsv`. Both go by names cited in the extracted text. Manifests inside the archive that
were not extracted may bind files that look unreferenced, so "named nowhere" is a candidate for dropping and no proof
that a file is unused.

### 3.1 Keep

- **All deliverables and programs, 733 files, 11.2 MB:** root files, `work/**/*.tex`, `*.md`, `*.tsv`, scripts.
- **Files named by the paper, registers or TeX, 473 files, 651.5 MB.**
- **Certificate folders named in TeX** (about 8.2 GB, the bulk of the archive), apart from the cases in 3.3. In particular:
  - `work/quaternary/results/torus_n9_box16_11_11` and `torus_n9_box15_11_11`, shards included: QC-020's checker binds
    QC-018's companions by bytes;
  - `work/quaternary/results/cyclic_n23_ray8`, `n23_cubic_box_*`, `nonic_small_tail_*`;
  - `work/root/results/cyclic_fourth_n9_*`, `cubic_window_n9_*`, `quartic_n9_b14_streamed`;
  - `work/support_lmr/results/bracket_basis_c9`, `four_nonic_sparse`, `padded_c9_invariant_jacobian_155`, the
    156-function refinement's results, and `lmr_explicit.json`;
  - `work/border/certificates/`: the consolidated det files and every `per10_*` folder that the BR findings name.
- **For prompt 56 alone** the files listed in 2.1 suffice; they need no unpacking of the large folders.

### 3.2 Can go after intake

| pattern | size | note |
|---|---|---|
| `**/tmp/`, `**/logs/`, `work/root/latex/`, `*.aux`, `*.log`, `*.toc`, `__pycache__`, downloaded literature copies | 11.5 MB | keep the source URLs and hashes |
| folders named nowhere in the extracted text (class `folder named nowhere`) | 30 MB | check the archive's manifests first |

### 3.3 Can go only after one named check

| pattern | size | check before dropping |
|---|---|---|
| `work/border/certificates/per10_quadratic_exterior_probe` | 321.2 MB | named only by a program or note; confirm no BR checker imports its output |
| `work/border/certificates/per10_projected_only_flags` | 53.3 MB | the same |
| `work/root/results/quartic_n9_b14` (one file) | 329.4 MB | confirm that `quartic_n9_b14_streamed` supersedes it and that no hash chain names it |
| other folders named only by programs or notes | about 100 MB | in the folder TSV |
| `work/border/certificates/archive` (retries) | 210.7 MB | named in TeX: drop only retries whose orbit has a completed replacement certificate |
| `work/*/results/nonic_saturated_tail36_6_6*` | about 467 MB | the register records a saturated-strip attempt as failed; confirm that QC-029 does not read these shards |
| the `per10_*_flags` working folders | several GB | only when the permanent gate closes or the run ends and a consolidated certificate replaces them |

The files with duplicated content (about 37 MB) should stay: the checkers compare path keys.

## 4. In the project's terms

| finding | in Grothendieck's frameworks and our records |
|---|---|
| O-030 | GL-equivariant restriction maps Γ(P, O(d)) → k[Det_n]_d and k[Per_n]_d on the isotypic pieces. The determinant-line twist moves between them by exact functors, and the Hessian section H_0 is a regular highest-weight section on an integral projective variety (SGA 3 I 4.7.2-4.7.3 as the run cites it; not reopened by me). It is the actual-module form of the two-row λ-identity; a class in K_0 would not see the gap. Rows: GCT_KRON A-030, A-034, QMMAIN; H13. |
| F-016 / S-001 | a weight support of the Cauchy decomposition, the actual direct-summand form of cote 133, scan 028 (a transcription, as the run cites it). |
| S-002, S-003 | the degree-twelve piece of the coherent ideal of Det_3 has multiplicity 1 on S_λ, with the exact sequence of multiplicities 1 → 6 → 5; that of Per_3 has 0. |
| S-004 | a change of the essential-variable subspace variety (rank m² against m²+1), hence of the support of the equivariant module. |
| QC-014 | an inclusion of closed cones {ℓ^{n−4}q} ⊂ D_{n,4}, from a dominant morphism of parameter schemes and closedness; hence a surjection of graded equivariant coordinate rings. |
| QC-019, S-025 | Hilbert functions of two graded rings of semi-invariants: the determinant one is bounded by a slice of Mat_9³ under PGL_9 × (G_a³ ⋊ GL_3), the padded one by a polynomial subalgebra on 156 sections. Rows: CUE_GCT R-14, G-17; GCT_OBS Q1a; H14. |
| QC-021 | vanishing of the first ten graded pieces of the coherent ideal of D_{n,r} for n ≥ 6 (unchecked). |
| OBS and QC boxes | surjectivity statements for relative Taylor (jet) bundles that force isotypic pieces of the ideal sheaf to vanish (unchecked). |
| BR-002, BR-006, BR-013 ff. | avoidance of relative secant loci in Grassmannians of the 2×2-minor space, over Spec Z for 43 and in characteristic zero for 44; rows BR_PENCIL Q-07, Q-17; H03. |

## 5. Hexagon readiness

| entry | complete | self-contained | stable | checked | interest | gate left |
|---|---|---|---|---|---|---|
| **H13**, now O-030 with S-002/S-003 | yes as written | after prompt 56 writes F-002, O-006, A-030.13 in | the statement should change once, to O-030 | targeted proof checks and computations; no independent re-proof | moderate to high | prompt 56 with this follow-up; the literature, Hexagon included, and above all Landsberg-Manivel-Ressayre §3; a read of every page |
| **H14**, with QC-019 | R-14 yes; QC-019 modulo its certificate | yes after write-up | no, the run moves | R-14 and the upper bound checked; the 156 certificate and R-23/26/27 not | high if new | recompute the certificate; check R-23/26/27; the literature; the run's end |
| **H03** | 43 in every characteristic and 44 for det, as written | yes after write-up | no for per | 43 in characteristic 0 checked with the stated 25-case limit; BR-001, BR-002, BR-006 not by us | moderate to high | an intake of BR-001, BR-002, BR-006; the permanent gate |
| **QC-014** (possible note) | yes | yes | yes | targeted proof check and computation | moderate | a literature check of determinantal complexity of quaternary quartics, Hexagon included; small alone |

No entry passes all five tests. No novelty search was done in this intake.
